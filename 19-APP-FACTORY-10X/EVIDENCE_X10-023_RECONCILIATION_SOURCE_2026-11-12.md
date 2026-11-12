# X10-023 — Reconciliation policy for OS reboot, timezone and permission changes

**Factory baseline** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` (Master v27, Golden Index v29). Related Golden `notification_reliability` = COPY_READY but **provider-sensitive / NEEDS_REVIEW**, no runtime/Play certification inferred.

## Source implementation

[Policy planner](flutter_kits/notifications/lib/notification_reconciliation.dart) uses persisted user-owned reminder intents (no second reminder database), explicit fixed UTC / pinned local civil / floating-device local civil semantics and a separately provided IANA timezone resolution port. Proposals are bounded to 128 items, fail closed on duplicate IDs, bad civil dates, DST gaps, DST ambiguous overlaps, untrusted resolver outputs and missing timezone.

Reconciliation triggers include OS reboot, app upgrade, timezone/clock changes, permission changes and ordinary app launch. The planner observes the existing [health model](flutter_kits/notifications/lib/factory_notification_kit.dart), which must be independently populated by the real OS. A denied permission, blocked Android channel, absent scheduler, stale/unknown health, or exact-alarm restriction does not yield a false schedule. Exact-to-inexact degradation remains **explicit user opt-in**. Existing disabled/expired reminders are not silently removed or changed.

Every output is an **advisory decision**, not an OS call, delivered receipt or data mutation. Actual timezone lookup, boot-completed receiver, notification channel registration, Android 13+ runtime permission, Android exact alarm policy, foreground/background state, native cancellation and device delivery have **not** been implemented by this source module.

[Regression tests](flutter_kits/notifications/test/reconciliation_test.dart) cover restart, timezone switch with UTC preservation, explicit local zone, DST ambiguity/gap, denial/channel/scheduler, stale probe, fallback consent, disabled and expired records, duplicates, invalid data and untrusted timezone provider. CI runs pinned Dart 3.6.0 analyze/test. No physical Android evidence.

**Canonical queue state stays X10-023 PLANNED.** Acceptance requires a real Android provider/permission-channel-timezone bridge and platform tests plus physical delivery/reboot validation. Completion of policy fixtures does not satisfy that.
