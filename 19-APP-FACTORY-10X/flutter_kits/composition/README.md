# X10-025 — Kit composition, pure Dart source fixture

Version 0.1.0. Combines four source packages from sibling folders via
local path dependencies: profile, identity, backup and notifications.

The chooser outputs a deterministic *proposal* for supported source kits and
blocks monetization outright. Every selected package remains unconfigured:
identity requires a real independent OAuth/PKCE verifier, backup requires an
atomic domain/media storage port, notifications require native permission
and channel probes and physical delivery tests, and profile needs an actual
owner-scoped local store. Web native notifications are refused.

The integration test imports and executes all four packages in one Dart
process with fake adapters, without networking, secrets, billing, physical
devices or modifying consumer app repositories.

The flag `productBibleReviewed` is declarative; it never authenticates
a human approval. This package does NOT wire Flutter widgets or platform
plugins or certify any Golden. All consumer-specific adapters and actual
platform test gates remain open.

Run `dart pub get && dart analyze --fatal-infos && dart test`.
