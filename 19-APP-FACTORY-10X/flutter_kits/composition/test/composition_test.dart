import 'dart:convert';

import 'package:factory_backup_kit/factory_backup_kit.dart';
import 'package:factory_identity_kit/factory_identity_kit.dart';
import 'package:factory_kit_composition/factory_kit_composition.dart';
import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:factory_profile_kit/factory_profile_kit.dart';
import 'package:test/test.dart';

final nowUtc = DateTime.utc(2026, 11, 12, 12);
const appId = 'com.example.factorydemo';

class MemoryProfile implements ProfilePreferencesStore {
  String? json;
  int writes = 0;
  @override
  Future<String?> read() async => json;
  @override
  Future<void> writeAtomically(String jsonDocument) async {
    json = jsonDocument;
    writes++;
  }
}

class CancelProvider implements InteractiveIdentityProvider {
  int attempts = 0;
  @override
  Future<IdentityClaims?> signInInteractively() async {
    attempts++;
    return null;
  }
  @override
  Future<void> signOut() async {}
}

class ClosedVerifier implements IndependentIdentityVerifier {
  int calls = 0;
  @override
  Future<bool> verify(IdentityClaims claims) async {
    calls++;
    return false;
  }
}

class ClosedPartition implements AccountPartitionBoundary {
  int calls = 0;
  @override
  Future<bool> prepareSwitch(String fromSubject, String toSubject) async {
    calls++;
    return false;
  }
}

class MemoryRestore implements RestoreTransactionPort {
  String state = 'original';
  int transactions = 0;
  @override
  Future<Object> createSafetySnapshot() async => state;
  @override
  Future<void> stage(Map<String, List<int>> verifiedEntries) async {
    transactions++;
  }
  @override
  Future<void> commitStaged() async {
    state = 'restored';
  }
  @override
  Future<void> rollbackTo(Object safetySnapshot) async {
    state = safetySnapshot as String;
  }
}

class DeniedNativeNotifier implements NotificationPlatformPort {
  int schedules = 0;
  @override
  Future<NotificationHealth> probe() async => NotificationHealth(
        checkedAtUtc: nowUtc,
        supported: true,
        permissionGranted: false,
        channelEnabled: false,
        schedulerAvailable: true,
        exactAllowed: false,
      );
  @override
  Future<bool> schedule(ReminderRequest request, {required bool exact}) async {
    schedules++;
    return true;
  }
  @override
  Future<bool> cancel(String stableId) async => false;
}

void main() {
  test('minimal profile source does not auto-activate other features', () {
    final result = const KitDependencyChooser().propose(
      KitAssemblyRequest(target: TargetPlatform.android,
          requested: {KitFeature.profile}),
    );
    expect(result.selections.map((x) => x.feature).toList(),
        [KitFeature.profile]);
    expect(result.globalGates, contains('PRODUCT_BIBLE_NOT_REVIEWED'));
    expect(result.runtimeEnabled, isFalse);
    expect(result.productionReady, isFalse);
    expect(result.releaseApproved, isFalse);
  });

  test('all source kit choices have explicit consumer-level gates', () {
    final result = const KitDependencyChooser().propose(
      KitAssemblyRequest(
        target: TargetPlatform.android,
        productBibleReviewed: true,
        requested: {KitFeature.notifications, KitFeature.identity,
                    KitFeature.backup, KitFeature.profile},
      ),
    );
    expect(result.selections.map((x) => x.sourcePackage).toList(), [
      'factory_profile_kit',
      'factory_identity_kit',
      'factory_backup_kit',
      'factory_notification_kit',
    ]);
    expect(result.selections.every((x) => x.requiredGates.isNotEmpty), isTrue);
    expect(result.globalGates, isNot(contains('PRODUCT_BIBLE_NOT_REVIEWED')));
    expect(result.providerConfigured, isFalse);
    expect(result.consumerCodeModified, isFalse);
    expect(result.goldenPromoted, isFalse);
  });

  test('monetization human gate never satisfied by a feature flag', () {
    final result = const KitDependencyChooser().propose(
      KitAssemblyRequest(
        target: TargetPlatform.android,
        productBibleReviewed: true,
        requested: {KitFeature.monetization, KitFeature.identity},
      ),
    );
    expect(result.refused[KitFeature.monetization],
        'HUMAN_BILLING_ADMOB_STORE_GATE_REQUIRED');
    expect(result.selections.map((x) => x.feature), contains(KitFeature.identity));
    expect(result.releaseApproved, isFalse);
  });

  test('Web cannot pretend native notification plugin exists', () {
    final result = const KitDependencyChooser().propose(
      KitAssemblyRequest(
        target: TargetPlatform.web,
        requested: {KitFeature.notifications, KitFeature.profile},
      ),
    );
    expect(result.refused[KitFeature.notifications],
        'NATIVE_NOTIFICATION_PROVIDER_NOT_SUPPORTED_ON_WEB');
    expect(result.selections.length, 1);
  });

  test('request flags are snapshot immutable and do not change with caller set', () {
    final userFlags = <KitFeature>{KitFeature.profile};
    final request = KitAssemblyRequest(
      target: TargetPlatform.ios, requested: userFlags);
    userFlags.add(KitFeature.monetization);
    final result = const KitDependencyChooser().propose(request);
    expect(result.refused, isEmpty);
    expect(result.selections.length, 1);
  });

  test('inter-kit smoke test uses actual 4 packages and no real provider', () async {
    final planned = const KitDependencyChooser().propose(
      KitAssemblyRequest(target: TargetPlatform.android,
          requested: {KitFeature.profile, KitFeature.identity,
                      KitFeature.backup, KitFeature.notifications}),
    );
    expect(planned.selections.length, 4);
    final store = MemoryProfile();
    final profile = ProfileSettingsController(store);
    await profile.load();
    await profile.update((p) => p.copyWith(displayName: 'Local',
                                             locale: 'it',
                                             analyticsOptIn: false));
    expect(store.writes, 1);

    final provider = CancelProvider();
    final verifier = ClosedVerifier();
    final partitions = ClosedPartition();
    final identity = OptInIdentityController(
      provider: provider, verifier: verifier, accountPartition: partitions,
      expectedIssuer: 'issuer', expectedAudience: 'audience', clock: () => nowUtc);
    expect(await identity.connect(explicitlyRequested: false),
        IdentityOutcome.userActionRequired);
    expect(provider.attempts, 0);
    expect(await identity.connect(explicitlyRequested: true),
        IdentityOutcome.cancelled);
    expect(identity.currentIdentity, isNull);
    expect(verifier.calls, 0);
    expect(partitions.calls, 0);

    // Export data only from an explicit owner-provided allowlist. This demo
    // does NOT claim automatic redaction of arbitrary app domain fields.
    final preferenceSnapshot = profile.current.toJson();
    final userData = utf8.encode(jsonEncode({
      'notes': ['one'],
      'display_name': preferenceSnapshot['display_name'],
    }));
    final bundle = BackupBundle.build(
      appId: appId,
      appVersion: '0.1.0',
      createdAtUtc: nowUtc,
      userOwnedEntries: {'data.json': userData, 'trash.json': utf8.encode('{}')},
    );
    expect(inspectBackup(bundle, expectedAppId: appId).verified, isTrue);
    final backupPort = MemoryRestore();
    expect(await BackupRestorer(backupPort, expectedAppId: appId).restore(bundle),
        RestoreOutcome.applied);
    expect(backupPort.transactions, 1);
    expect(backupPort.state, 'restored');
    expect(store.json, isNot(contains('access_token')));
    expect(utf8.decode(userData), isNot(contains('refresh_token')));

    final notifyPort = DeniedNativeNotifier();
    final notifications = NotificationCoordinator(notifyPort, nowUtc: () => nowUtc);
    final outcome = await notifications.schedule(ReminderRequest(
      stableId: 'local-note-reminder',
      scheduledAtUtc: nowUtc.add(const Duration(hours: 1)),
      title: 'Reminder',
      body: 'Hello',
      timezoneId: 'Europe/Rome',
    ));
    expect(outcome, ScheduleDecision.deniedPermission);
    expect(notifyPort.schedules, 0);
    expect(profile.current.displayName, 'Local');
    expect(identity.currentIdentity, isNull);
  });
}
