# X10-021 — Profile & Settings (Dart core)

Version 0.1.1, pure Dart. Backwards-compatible with 0.1.0: schema v1 unchanged.
Patch hardening: oversized preference documents are rejected before JSON decode;
original storage bytes remain intact, with an explicit corruption indicator. No Flutter/plugin/provider dependencies.
Adapt through a consumer-approved Product Bible and the authoritative
Core Golden `profile_standard` at c5adc147. It is not itself a certified Golden.

Included: immutable profile preferences, locale/system theme/analytics consent
defaults, validated schema v0->v1 lazy migration, atomic persist port,
serialized writes and explicit non-destructive corruption recovery.

Excluded: login, OAuth, passwords, session tokens, shared AuthService,
browser widgets, native localization, underlying storage implementation,
and consent/legal policy or device certification.

Wire a consumer-specific `ProfilePreferencesStore` (owner/account scoped)
with a true atomic-write guarantee. Test with Dart 3.6.0+
using `dart pub get && dart analyze && dart test`.
No consumer repository has imported this package or passed device tests.
