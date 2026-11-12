import 'package:factory_identity_kit/factory_identity_kit.dart';
import 'package:test/test.dart';

final now = DateTime.utc(2026, 11, 12, 12);

IdentityClaims claims(String subject, {String issuer = 'test-issuer', String audience = 'demo'}) {
  return IdentityClaims(
    subject: subject,
    issuer: issuer,
    audience: audience,
    expiresAtUtc: now.add(const Duration(hours: 1)),
  );
}

class FakeIdentityProvider implements InteractiveIdentityProvider {
  int logins = 0;
  int logouts = 0;
  IdentityClaims? next;
  bool throwsOnConnect = false;
  bool throwsOnLogout = false;

  @override
  Future<IdentityClaims?> signInInteractively() async {
    logins++;
    if (throwsOnConnect) throw StateError('provider_unavailable');
    return next;
  }

  @override
  Future<void> signOut() async {
    logouts++;
    if (throwsOnLogout) throw StateError('remote_logout_failed');
  }
}

class FakeVerifier implements IndependentIdentityVerifier {
  bool accept = true;
  int checks = 0;

  @override
  Future<bool> verify(IdentityClaims claims) async {
    checks++;
    return accept;
  }
}

class FakePartitions implements AccountPartitionBoundary {
  bool allow = false;
  int switches = 0;

  @override
  Future<bool> prepareSwitch(String fromSubject, String toSubject) async {
    switches++;
    return allow;
  }
}

void main() {
  late FakeIdentityProvider provider;
  late FakeVerifier verifier;
  late FakePartitions partitions;
  late OptInIdentityController controller;

  setUp(() {
    provider = FakeIdentityProvider();
    verifier = FakeVerifier();
    partitions = FakePartitions();
    controller = OptInIdentityController(
      provider: provider,
      verifier: verifier,
      accountPartition: partitions,
      expectedIssuer: 'test-issuer',
      expectedAudience: 'demo',
      clock: () => now,
    );
  });

  test('guest mode never initializes interactive provider', () async {
    expect(controller.currentIdentity, isNull);
    expect(await controller.connect(explicitlyRequested: false),
        IdentityOutcome.userActionRequired);
    expect(provider.logins, 0);
    expect(verifier.checks, 0);
  });

  test('real provider and independent verifier are both required', () async {
    provider.next = claims('user-A');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.connected);
    expect(controller.currentIdentity?.subject, 'user-A');
    expect(verifier.checks, 1);
  });

  test('cancellation never creates a session', () async {
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.cancelled);
    expect(controller.currentIdentity, isNull);
  });

  test('invalid audience or issuer never creates a session', () async {
    provider.next = claims('user-A', audience: 'other');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.verificationDenied);
    expect(verifier.checks, 0);
    provider.next = claims('user-A', issuer: 'untrusted');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.verificationDenied);
  });

  test('expired or missing subject never creates a session', () async {
    provider.next = IdentityClaims(
      subject: '',
      issuer: 'test-issuer',
      audience: 'demo',
      expiresAtUtc: now.subtract(const Duration(minutes: 1)),
    );
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.verificationDenied);
  });

  test('fake verified field cannot bypass independent verifier', () async {
    provider.next = claims('user-A');
    verifier.accept = false;
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.verificationDenied);
    expect(controller.currentIdentity, isNull);
  });

  test('account switch blocked cannot expose old or new partition', () async {
    provider.next = claims('user-A');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.connected);
    provider.next = claims('user-B');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.isolatedSwitchBlocked);
    expect(controller.currentIdentity, isNull);
    expect(partitions.switches, 1);
  });

  test('account switch requires explicitly prepared partition', () async {
    provider.next = claims('user-A');
    await controller.connect(explicitlyRequested: true);
    partitions.allow = true;
    provider.next = claims('user-B');
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.connected);
    expect(controller.currentIdentity?.subject, 'user-B');
    expect(partitions.switches, 1);
  });

  test('provider exception falls back to guest without local data deletion', () async {
    provider.throwsOnConnect = true;
    expect(await controller.connect(explicitlyRequested: true),
        IdentityOutcome.providerFailure);
    expect(controller.currentIdentity, isNull);
    expect(controller.isBusy, isFalse);
  });

  test('signout clears local claims before remote logout succeeds or fails', () async {
    provider.next = claims('user-A');
    await controller.connect(explicitlyRequested: true);
    provider.throwsOnLogout = true;
    await expectLater(controller.disconnect(), throwsStateError);
    expect(controller.currentIdentity, isNull);
    expect(provider.logouts, 1);
  });

  test('claims contain no token, password, refresh token or cloud key fields', () {
    final projected = claims('A');
    expect(projected.subject, 'A');
    expect(projected.expiresAtUtc.isUtc, isTrue);
    // This contract intentionally has no JSON serializer for sessions.
    expect(projected.toString(), isNot(contains('access_token')));
  });
}
