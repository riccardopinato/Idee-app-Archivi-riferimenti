/// X10-022: bounded manifest integrity and staged restore transaction.
/// This is NOT a ZIP archive, encrypted export, file-picker or provider sync.
import 'dart:collection';

import 'package:crypto/crypto.dart';

class BackupLimit {
  static const int maxEntries = 128;
  static const int maxEntryBytes = 16 * 1024 * 1024;
  static const int maxTotalBytes = 32 * 1024 * 1024;
}

bool _validEntryPath(String path) {
  if (path == 'data.json' || path == 'trash.json') return true;
  return RegExp(r'^media/[A-Za-z0-9_-]{1,64}\.bin$').hasMatch(path);
}

bool _validAppId(String id) {
  return RegExp(r'^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$').hasMatch(id);
}

class EntryReceipt {
  const EntryReceipt({required this.sizeBytes, required this.sha256});

  final int sizeBytes;
  final String sha256;
}

class BackupManifest {
  const BackupManifest({
    required this.schemaVersion,
    required this.appId,
    required this.appVersion,
    required this.createdAtUtc,
    required this.entries,
  });

  final int schemaVersion;
  final String appId;
  final String appVersion;
  final DateTime createdAtUtc;
  final Map<String, EntryReceipt> entries;
}

/// Holds allowlisted, uncompressed bytes. Real import/export adapters must
/// enforce byte caps on the wire *before* allocating their full input.
class BackupBundle {
  const BackupBundle({required this.manifest, required this.entries});

  final BackupManifest manifest;
  final Map<String, List<int>> entries;

  factory BackupBundle.build({
    required String appId,
    required String appVersion,
    required DateTime createdAtUtc,
    required Map<String, List<int>> userOwnedEntries,
  }) {
    if (!_validAppId(appId) ||
        appVersion.isEmpty ||
        appVersion.length > 64 ||
        !createdAtUtc.isUtc) {
      throw const FormatException('invalid_backup_identity');
    }
    if (!userOwnedEntries.containsKey('data.json') ||
        userOwnedEntries.length > BackupLimit.maxEntries) {
      throw const FormatException('invalid_backup_entries');
    }
    final copies = <String, List<int>>{};
    final manifestEntries = <String, EntryReceipt>{};
    final folded = <String>{};
    var total = 0;
    for (final item in userOwnedEntries.entries) {
      final name = item.key;
      final data = item.value;
      if (!_validEntryPath(name) || !folded.add(name.toLowerCase())) {
        throw const FormatException('unsafe_or_duplicate_entry');
      }
      if (data.length > BackupLimit.maxEntryBytes ||
          total + data.length > BackupLimit.maxTotalBytes ||
          data.any((byte) => byte < 0 || byte > 255)) {
        throw const FormatException('backup_budget_exceeded');
      }
      total += data.length;
      final frozen = List<int>.unmodifiable(data);
      copies[name] = frozen;
      manifestEntries[name] = EntryReceipt(
        sizeBytes: frozen.length,
        sha256: sha256.convert(frozen).toString(),
      );
    }
    return BackupBundle(
      manifest: BackupManifest(
        schemaVersion: 1,
        appId: appId,
        appVersion: appVersion,
        createdAtUtc: createdAtUtc,
        entries: UnmodifiableMapView(manifestEntries),
      ),
      entries: UnmodifiableMapView(copies),
    );
  }
}

class Inspection {
  const Inspection(this.errors, this.entryCount, this.totalBytes);

  final List<String> errors;
  final int entryCount;
  final int totalBytes;

  bool get verified => errors.isEmpty;
}

Inspection inspectBackup(BackupBundle bundle, {required String expectedAppId}) {
  final errors = <String>[];
  final manifest = bundle.manifest;
  if (manifest.schemaVersion != 1 ||
      !_validAppId(manifest.appId) ||
      manifest.appId != expectedAppId ||
      manifest.appVersion.isEmpty ||
      manifest.appVersion.length > 64 ||
      !manifest.createdAtUtc.isUtc) {
    errors.add('MANIFEST_IDENTITY_OR_VERSION');
  }
  final names = bundle.entries.keys.toSet();
  final declared = manifest.entries.keys.toSet();
  if (!names.contains('data.json') ||
      names.length != declared.length ||
      !names.containsAll(declared) ||
      !declared.containsAll(names)) {
    errors.add('ENTRY_MANIFEST_MISMATCH');
  }
  if (names.length > BackupLimit.maxEntries) {
    errors.add('ENTRY_COUNT_EXCEEDED');
  }
  final folded = <String>{};
  var total = 0;
  for (final item in bundle.entries.entries) {
    final name = item.key;
    final bytes = item.value;
    if (!_validEntryPath(name) || !folded.add(name.toLowerCase())) {
      errors.add('UNSAFE_OR_DUPLICATE_PATH');
      continue;
    }
    if (bytes.length > BackupLimit.maxEntryBytes ||
        total + bytes.length > BackupLimit.maxTotalBytes ||
        bytes.any((byte) => byte < 0 || byte > 255)) {
      errors.add('SIZE_OR_BYTE_BUDGET');
      continue;
    }
    total += bytes.length;
    final receipt = manifest.entries[name];
    if (receipt == null ||
        receipt.sizeBytes != bytes.length ||
        !RegExp(r'^[a-f0-9]{64}$').hasMatch(receipt.sha256) ||
        receipt.sha256 != sha256.convert(bytes).toString()) {
      errors.add('INTEGRITY_MISMATCH');
    }
  }
  return Inspection(List<String>.unmodifiable(errors), names.length, total);
}

/// Consumer implementation must stage privately, snapshot user-owned state
/// and atomically switch or restore original snapshot if commit fails.
abstract interface class RestoreTransactionPort {
  Future<Object> createSafetySnapshot();
  Future<void> stage(Map<String, List<int>> verifiedEntries);
  Future<void> commitStaged();
  Future<void> rollbackTo(Object safetySnapshot);
}

enum RestoreOutcome {
  applied,
  invalidBundle,
  safetySnapshotFailed,
  failedButRolledBack,
  recoveryRequired,
  busy,
}

class BackupRestorer {
  BackupRestorer(this._port, {required this.expectedAppId});

  final RestoreTransactionPort _port;
  final String expectedAppId;
  bool _working = false;

  Future<RestoreOutcome> restore(BackupBundle bundle) async {
    if (_working) return RestoreOutcome.busy;
    _working = true;
    try {
      // Freeze caller-owned memory before the first await. The same frozen
      // bytes are inspected and staged; data can't change while awaiting I/O.
      final snapshotEntries = <String, List<int>>{
        for (final entry in bundle.entries.entries)
          entry.key: List<int>.unmodifiable(entry.value),
      };
      final frozen = BackupBundle(
        manifest: bundle.manifest,
        entries: UnmodifiableMapView(snapshotEntries),
      );
      if (!inspectBackup(frozen, expectedAppId: expectedAppId).verified) {
        return RestoreOutcome.invalidBundle;
      }
      late final Object safety;
      try {
        safety = await _port.createSafetySnapshot();
      } catch (_) {
        return RestoreOutcome.safetySnapshotFailed;
      }
      try {
        await _port.stage(frozen.entries);
        await _port.commitStaged();
        return RestoreOutcome.applied;
      } catch (_) {
        try {
          await _port.rollbackTo(safety);
          return RestoreOutcome.failedButRolledBack;
        } catch (_) {
          // Never claim no data loss if the rollback itself failed.
          return RestoreOutcome.recoveryRequired;
        }
      }
    } finally {
      _working = false;
    }
  }
}
