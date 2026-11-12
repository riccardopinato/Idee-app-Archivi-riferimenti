# X10-036 — Privacy metrics: prototype source only (no product activation)

This small pure-Dart module is **not** a marketing attribution SDK. It allows only five fixed event counters, in memory, after explicit opt-in injected by the host. Any revocation calls `erase`, destroys counters and consent; minimum five consented **sessions**, not five unique people, gate export. No user/session identifier, timestamps, email, device fingerprint, location, persistent storage, network, Play payments or third-party tracker.

**Does not meet X10-036 production acceptance.** Real retention, conversion and attribution need independently reviewed consent, privacy notices, aggregate correctness and decision X10-035; session counts cannot be used to claim unique users or cohorts. The module must not be imported into any production app yet. Test: `dart pub get && dart analyze --fatal-infos && dart test`; CI entry in the archive kit matrix is source-only.
