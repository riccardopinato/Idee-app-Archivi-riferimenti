# X10-020 — Optional identity core (pure Dart)

0.1.0 source contract. No Google, Supabase or Android SDK is initialized here.
The consumer owns OAuth/PKCE, platform redirect, token signature/nonce
verification, auth storage, account-specific data partitioning and logout.

Consumers supply `InteractiveIdentityProvider`,
`IndependentIdentityVerifier` and `AccountPartitionBoundary`. A session
exists only after explicit user gesture and both exact issuer/audience/time
checks plus independent verifier acceptance. Account switching must prepare
an isolated data partition first; rejection forces guest state without
deleting previous user-owned data. No credentials or tokens are serialized.

Reuses conceptual constraints of Core Golden `google_auth_supabase`
(COPY_READY but provider-sensitive, NEEDS_REVIEW). Do NOT treat unit tests
using fake providers as successful production Google OAuth. No registered
callback, provider credentials, app consumer or physical tests are claimed.

Run: `dart pub get && dart analyze --fatal-infos && dart test`.
