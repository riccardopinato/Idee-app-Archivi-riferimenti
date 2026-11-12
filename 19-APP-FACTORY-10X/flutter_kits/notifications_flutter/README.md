# X10-023 — Real Flutter Android notification API adapter (source/CI candidate)

Factory baseline: App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619 (Master v27, Golden Index v29). Applicable GOLDEN_NOTIFICATION_RELIABILITY_FLUTTER_v1, COPY_READY but per-app provider review required. The native reliability Golden is a draft, NOT a certification.

The Dart-only policy and reconciliation live in [../notifications](../notifications/). This optional Flutter package consumes that policy via **a real `flutter_local_notifications` Android backend** and has a fake-backend test seam. The application supplies `ensureConsumerPluginInitialized` (with its callbacks intact) and `androidSdkInt` from an actual OS SDK query. The adapter does not initialize/overwrite the application's callbacks. Its production-facing implementation probes `areNotificationsEnabled`, configured Android channel importance, `canScheduleExactNotifications` and plugin initialization separately. It uses an IANA `timezone` resolver for user-supplied zones, stable UTF-8 SHA256-derived 31-bit notification IDs, and native `zonedSchedule`/`cancel`. It does not request permissions, create a background service or claim delivery when registration succeeds.

## Adoption checklist (mandatory per consumer)

1. Confirm existing notification **owner** and persisted stable reminder ID; do not create a second database or duplicate scheduler.
2. Existing app must install/configure `POST_NOTIFICATIONS` runtime permission on Android 13+, its AndroidManifest `RECEIVE_BOOT_COMPLETED` and actual plugin receivers as applicable. Verify declared exact alarm permission/policy *only when necessary*; permission cannot be presumed.
3. Reuse the existing `FlutterLocalNotificationsPlugin` singleton, app-specific channel/icon, localization and callbacks. Inject `ensureConsumerPluginInitialized` for callback-preserving app initialization and `androidSdkInt` for real Android Build.VERSION.SDK_INT. On Android API24–25 channels do not exist; on 26+ the configured channel must be enabled. The backend NEVER calls `plugin.initialize()` itself. Prefer a product-adapted facade if app has an existing notification service.
4. Independently validate notification/channel/FGS/OS exact-alarm permissions on the actual device. This kit does **not** start an FGS; background delivery depends on OS AlarmManager/receivers already installed by the consumer, not a hidden always-on service.
5. Run AppLab exact signed artifact and Android emulator/device tests: denied/regranted notification permission, blocked channel, exact unavailable, inexact fallback with user consent, timezone DST gap/overlap, reboot, app update, system time, tap/cancel/duplicate, Xiaomi/Samsung OEM/Doze restrictions. Validate *actual delivered* notification separately from native schedule registration.
6. Validate privacy and source/binary licensing before release; no permission, checkout, backend, ads or billing should be silently introduced.

## Evidence boundary

- Flutter host CI verifies source, API typing, and fake-platform tests. It **cannot** prove Android notification delivery, process death/reboot recovery, privileged exact alarm entitlement, device/OEM support or Store compatibility.
- No consumer app is mutated by this PR. X10-023 stays PLANNED until one real Android consumer integrates, the platform/native instrumented tests and physical same-APK evidence exist; the existing Android QA dossier remains the evidence plan rather than a trusted provider.
- The adapter does not mint physical receipts; consume `physical_evidence.py` from AppLab for independent evidence. A signed APK, CI PASS, schedule acceptance or plugin init is not a delivery receipt.
- Stable SHA256 IDs map to Android's 31 bits, so rare collisions are possible. App's canonical reminder store must detect/reject ambiguous IDs before registration; do not change existing ID scheme without a reviewed migration.

Tests: run `flutter pub get && flutter analyze && flutter test` in this package, Flutter 3.47.5 pinned in CI. Source uses versions already present in Anna's Diary; no external cost.
