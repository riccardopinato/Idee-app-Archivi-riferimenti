/// X10-020: opt-in sign-in policy. No Google SDK, Supabase secret or token
/// persistence. Consumer supplies the real provider, verifier and data boundary.
enum IdentityOutcome {
  connected,
  userActionRequired,
  cancelled,
  verificationDenied,
  isolatedSwitchBlocked,
  providerFailure,
  alreadyBusy,
}

class IdentityClaims {
  const IdentityClaims({
    required this.subject,
    required this.issuer,
    required this.audience,
    required this.expiresAtUtc,
  });

  final String subject;
  final String issuer;
  final String audience;
  final DateTime expiresAtUtc;
}

/// Adapter to a REAL user-initiated OAuth/PKCE and auth-state provider.
/// Never construct these claims from UI field data or unchecked ID tokens.
abstract interface class InteractiveIdentityProvider {
  /// Null means the user cancelled without committing a new identity.
  Future<IdentityClaims?> signInInteractively();
  Future<void> signOut();
}

/// Trust result must be established by a real trusted Google/Supabase adapter
/// and/or server, including ID token signature, audience and nonce/PKCE.
abstract interface class IndependentIdentityVerifier {
  Future<bool> verify(IdentityClaims claims);
}

/// Move to an isolated user data partition before exposing a new identity.
/// Returning false denies access to both old and new partitions until
/// the user reestablishes a trusted session. Never delete existing user data.
abstract interface class AccountPartitionBoundary {
  Future<bool> prepareSwitch(String fromSubject, String toSubject);
}

class OptInIdentityController {
  OptInIdentityController({
    required InteractiveIdentityProvider provider,
    required IndependentIdentityVerifier verifier,
    required AccountPartitionBoundary accountPartition,
    required String expectedIssuer,
    required String expectedAudience,
    DateTime Function()? clock,
  })  : _provider = provider,
        _verifier = verifier,
        _accountPartition = accountPartition,
        _expectedIssuer = expectedIssuer,
        _expectedAudience = expectedAudience,
        _clock = clock ?? DateTime.now;

  final InteractiveIdentityProvider _provider;
  final IndependentIdentityVerifier _verifier;
  final AccountPartitionBoundary _accountPartition;
  final String _expectedIssuer;
  final String _expectedAudience;
  final DateTime Function() _clock;

  IdentityClaims? _current;
  bool _busy = false;

  bool get isBusy => _busy;

  // Never call provider.login merely because the app booted.
  // Expired claims are not a valid active identity.
  IdentityClaims? get currentIdentity {
    final current = _current;
    if (current == null || !current.expiresAtUtc.isAfter(_clock().toUtc())) {
      return null;
    }
    return current;
  }

  bool _validShape(IdentityClaims claims) {
    return claims.subject.trim().isNotEmpty &&
        claims.subject.length <= 256 &&
        claims.issuer == _expectedIssuer &&
        claims.audience == _expectedAudience &&
        claims.expiresAtUtc.isUtc &&
        claims.expiresAtUtc.isAfter(_clock().toUtc());
  }

  Future<IdentityOutcome> connect({required bool explicitlyRequested}) async {
    if (!explicitlyRequested) return IdentityOutcome.userActionRequired;
    if (_busy) return IdentityOutcome.alreadyBusy;
    _busy = true;
    try {
      final old = currentIdentity;
      final claims = await _provider.signInInteractively();
      if (claims == null) return IdentityOutcome.cancelled;
      if (!_validShape(claims) || !await _verifier.verify(claims)) {
        // Provider may already have changed its effective identity: fail
        // closed rather than exposing cached old-account data.
        _current = null;
        return IdentityOutcome.verificationDenied;
      }
      if (old != null && old.subject != claims.subject) {
        final isolated = await _accountPartition.prepareSwitch(
          old.subject,
          claims.subject,
        );
        if (!isolated) {
          _current = null;
          return IdentityOutcome.isolatedSwitchBlocked;
        }
      }
      _current = claims;
      return IdentityOutcome.connected;
    } catch (_) {
      _current = null;
      return IdentityOutcome.providerFailure;
    } finally {
      _busy = false;
    }
  }

  /// Fail closed immediately; remote signout may fail, but local user-owned
  /// data and profile preferences are not erased by this method.
  Future<void> disconnect() async {
    _current = null;
    await _provider.signOut();
  }
}
