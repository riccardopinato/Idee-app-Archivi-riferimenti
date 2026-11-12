import 'dart:async';
import 'dart:convert';

import 'package:factory_backup_kit/factory_backup_kit.dart';
import 'package:test/test.dart';

final time = DateTime.utc(2026, 11, 12, 12);
const appId = 'com.example.factory';

BackupBundle bundle({Map<String, List<int>>? entries}) => BackupBundle.build(
      appId: appId,
      appVersion: '1.0.0+3',
      createdAtUtc: time,
      userOwnedEntries: entries ??
          {
            'data.json': utf8.encode('{"notes":[1,2]}'),
            'trash.json': utf8.encode('{"deleted":[]}'),
            'media/img_001.bin': [1, 2, 3, 4],
          },
    );

class FakeRestorePort implements RestoreTransactionPort {
  String active = 'original';
  Map<String, List<int>>? staged;
  int snapshots = 0;
  int stages = 0;
  int commits = 0;
  int rollbacks = 0;
  bool failSnapshot = false;
  bool failStage = false;
  bool failCommit = false;
  bool failRollback = false;
  Completer<void>? holdSnapshot;

  @override
  Future<Object> createSafetySnapshot() async {
    snapshots++;
    if (holdSnapshot != null) await holdSnapshot!.future;
    if (failSnapshot) throw StateError('snapshot_failed');
    return active;
  }

  @override
  Future<void> stage(Map<String, List<int>> verifiedEntries) async {
    stages++;
    if (failStage) throw StateError('stage_failed');
    staged = Map<String, List<int>>.from(verifiedEntries);
  }

  @override
  Future<void> commitStaged() async {
    commits++;
    active = 'imported';
    if (failCommit) throw StateError('commit_failed_midway');
  }

  @override
  Future<void> rollbackTo(Object safetySnapshot) async {
    rollbacks++;
    if (failRollback) throw StateError('rollback_failed');
    active = safetySnapshot as String;
    staged = null;
  }
}

void main() {
  test('valid manifest includes data, trash, media and checksums', () {
    final pack = bundle();
    final check = inspectBackup(pack, expectedAppId: appId);
    expect(check.verified, isTrue);
    expect(check.entryCount, 3);
    expect(pack.manifest.entries['data.json']!.sha256.length, 64);
    expect(pack.manifest.createdAtUtc.isUtc, isTrue);
  });

  test('changed payload after manifest creation is rejected before restore', () async {
    final original = bundle();
    final tampered = BackupBundle(
      manifest: original.manifest,
      entries: {...original.entries, 'data.json': utf8.encode('{"notes":[]}')},
    );
    final port = FakeRestorePort();
    expect(await BackupRestorer(port, expectedAppId: appId).restore(tampered),
        RestoreOutcome.invalidBundle);
    expect(port.snapshots, 0);
    expect(port.stages, 0);
    expect(port.active, 'original');
  });

  test('missing media or extra undeclared entry blocks restore', () {
    final original = bundle();
    final missing = BackupBundle(
      manifest: original.manifest,
      entries: Map.of(original.entries)..remove('media/img_001.bin'),
    );
    expect(inspectBackup(missing, expectedAppId: appId).verified, isFalse);
    final extra = BackupBundle(
      manifest: original.manifest,
      entries: {...original.entries, 'media/extra.bin': [1]},
    );
    expect(inspectBackup(extra, expectedAppId: appId).verified, isFalse);
  });

  test('path traversal, secrets and case-collision paths rejected on export', () {
    for (final path in [
      '../token',
      '/absolute',
      'media/../evil.bin',
      '.env',
      'refresh_token.txt',
      'cache/index.db',
    ]) {
      expect(
        () => bundle(entries: {'data.json': [1], path: [1]}),
        throwsFormatException,
      );
    }
    expect(
      () => bundle(entries: {
        'data.json': [1],
        'media/A.bin': [2],
        'media/a.bin': [3],
      }),
      throwsFormatException,
    );
  });

  test('future schema and wrong app identity are never restored', () {
    final original = bundle();
    final future = BackupBundle(
      manifest: BackupManifest(
        schemaVersion: 2,
        appId: appId,
        appVersion: '2.0.0',
        createdAtUtc: time,
        entries: original.manifest.entries,
      ),
      entries: original.entries,
    );
    expect(inspectBackup(future, expectedAppId: appId).verified, isFalse);
    expect(inspectBackup(original, expectedAppId: 'com.other.app').verified, isFalse);
  });

  test('entry budget rejects oversized data before storage mutation', () {
    expect(
      () => bundle(entries: {
        'data.json': List<int>.filled(BackupLimit.maxEntryBytes + 1, 0),
      }),
      throwsFormatException,
    );
  });

  test('successful restore stages and commits only verified bytes', () async {
    final port = FakeRestorePort();
    final result = await BackupRestorer(port, expectedAppId: appId).restore(bundle());
    expect(result, RestoreOutcome.applied);
    expect(port.snapshots, 1);
    expect(port.stages, 1);
    expect(port.commits, 1);
    expect(port.rollbacks, 0);
    expect(port.active, 'imported');
  });

  test('failed stage rolls back snapshot without touching active state', () async {
    final port = FakeRestorePort()..failStage = true;
    expect(await BackupRestorer(port, expectedAppId: appId).restore(bundle()),
        RestoreOutcome.failedButRolledBack);
    expect(port.active, 'original');
    expect(port.rollbacks, 1);
  });

  test('partial commit failure restores prior active state', () async {
    final port = FakeRestorePort()..failCommit = true;
    expect(await BackupRestorer(port, expectedAppId: appId).restore(bundle()),
        RestoreOutcome.failedButRolledBack);
    expect(port.active, 'original');
    expect(port.rollbacks, 1);
  });

  test('rollback failure returns recoveryRequired, never data-safe status', () async {
    final port = FakeRestorePort()
      ..failCommit = true
      ..failRollback = true;
    expect(await BackupRestorer(port, expectedAppId: appId).restore(bundle()),
        RestoreOutcome.recoveryRequired);
    expect(port.active, 'imported');
  });

  test('snapshot failure never begins staged mutation', () async {
    final port = FakeRestorePort()..failSnapshot = true;
    expect(await BackupRestorer(port, expectedAppId: appId).restore(bundle()),
        RestoreOutcome.safetySnapshotFailed);
    expect(port.stages, 0);
    expect(port.commits, 0);
  });

  test('simultaneous restore is explicitly busy, not second transaction', () async {
    final port = FakeRestorePort()..holdSnapshot = Completer<void>();
    final restorer = BackupRestorer(port, expectedAppId: appId);
    final first = restorer.restore(bundle());
    expect(await restorer.restore(bundle()), RestoreOutcome.busy);
    port.holdSnapshot!.complete();
    expect(await first, RestoreOutcome.applied);
    expect(port.snapshots, 1);
  });
}
