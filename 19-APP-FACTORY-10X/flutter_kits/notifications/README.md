# X10-023 — Notification scheduling + health (pure Dart contract)

This package models health and scheduling decisions only; it does not
register a notification channel, Android foreground service, iOS permission,
OS alarm, plugin receiver, exact-alarm entitlement or timezone database.

The provider MUST probe actual OS support, permission, channel, scheduler
and report a *separately observed receipt* before claiming HEALTHY.
Schedule accepted means scheduling requested, NOT delivered.
Stale probe results become UNKNOWN. Exact scheduling can degrade to
inexact only under explicit consumer permission.

The consumer owns persisted reminder records, stable identity, reboot/
package-update/timezone reconciliation, provider permissions and native
user-facing text localization. These must be physically tested per device.
Golden notification_reliability is COPY_READY but provider-sensitive and
NEEDS_REVIEW. No native or Android notification can be certified by
these pure Dart unit tests.

Run dart pub get && dart analyze --fatal-infos && dart test.
