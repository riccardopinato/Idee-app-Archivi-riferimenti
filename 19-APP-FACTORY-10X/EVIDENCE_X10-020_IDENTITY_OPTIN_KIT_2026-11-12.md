# X10-020 — Identity/login opt-in (Dart core)

**Baseline:** App-Factory-Core c5adc147046beb7024629466d10eeb799c3c2619, Master v27, Golden Index v29. Golden google_auth_supabase is COPY_READY, provider-sensitive and NEEDS_REVIEW since provider docs may change. No Google/Supabase production SDK is initialized by this package.

## Delivered source
[Identity Dart package](flutter_kits/identity/) factory_identity_kit 0.1.0: local-first guest state, explicit-gesture login, typed claims containing only subject/issuer/audience/UTC expiry, independent injected trust verifier for real signed OAuth claims, validated expected issuer/audience/expiry, account partition boundary on changes, predictable logout isolation and token-free in-memory session projection.

**Security boundaries:** the application must supply a real OAuth/PKCE provider and signature/nonce verifier, validate Android/Web callbacks and token/session storage, and ensure old/new account content cannot overlap. This Dart policy cannot attest that external providers are configured or that tokens were verified. Even a fake provider in unit tests is not trusted in production. Calling connect with explicitlyRequested=false never opens OAuth. A failed account switch fails closed to guest without deleting locally owned data.

## Verification
Real Dart 3.6.0 CI in [shared kit workflow](../.github/workflows/app-factory-10x-dart-kits.yml) runs dart analyze --fatal-infos and dart test on this package. Tests cover cancellation, issuer/audience mismatch, expired claims, independent verifier rejection, guarded account switch, failed provider and logout behavior. CI proves only pure Dart logic on exact head.

**NOT_VERIFIED:** Google OAuth provider flow, Supabase Auth session persistence, Android callback, iOS universal links, Web redirect, account erasure, real data isolation, access control, device/login UX, multi-consumer adoption, Google Cloud setup. No new secrets, permissions, cloud service, Product Bible or Golden admission-level change.
