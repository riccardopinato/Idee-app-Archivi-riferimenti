# X10-024 — Provider-neutral monetization policy (SOURCE CANDIDATE)

Version 0.1.0. Pure Dart functions for entitlement and ad request eligibility.

**Factory baseline:** App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619, Master 27, Golden Index 29. Follows the existing provider-agnostic `GOLDEN_ENTITLEMENT_CONTRACT_FLUTTER_v1` (COPY-READY), and the distinct AdMob safe/consent candidate. Does **not** replace either Golden or clone a consumer billing service.

## What is implemented
- Distinguish Free, Premium and Lifetime plans; no paid access without a verified source and valid date.
- Offline grace is explicitly bounded by a caller-supplied deadline; unknown and expired states fail closed without deleting user-owned content.
- QA entitlement override only when the caller opts into non-production QA.
- Before a call to any Ad SDK, a pure decision denies ad requests unless **owner-approved placement**, **provider-approved consent**, and **test/prod ad-unit configuration** all agree. Paid access suppresses ads.
- No SDK/network, billing account, user ID, paywall price, telemetry, persistence, attribution, product ID or ad unit ID.

## Critical adoption gates

**X10-024 remains HUMAN_GATE / PLANNED**. This package is SOURCE_CANDIDATE only. The owner must choose a real product, price/offer, ads/IAP model and expressly approve provider configuration. For AdMob, the consumer must implement and verify the native UMP canRequestAds gate, privacy options, actual test ad IDs, store metadata, no accidental clicks, and the app's product/age/location treatment. For IAP, the real billing adapter must verify signed transactions or authoritative provider state, handle pending/refund/revocation and test actual Play sandbox restore.

The package itself does not fetch or authenticate entitlements; `FactoryEntitlementSource.providerVerified` requires **trusted consumer adapter** evidence, never arbitrary UI input. Provider approval is not implied by green tests.

## Source tests
`dart pub get && dart analyze --fatal-infos && dart test`. Independent CI uses pinned Flutter/Dart 3.47.5; it cannot certify real AdMob/UMP, purchase flows or Play distribution.
