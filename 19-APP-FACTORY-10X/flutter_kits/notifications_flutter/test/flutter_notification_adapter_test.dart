import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:factory_notification_flutter_adapter/factory_flutter_notification_adapter.dart';
import 'package:factory_notification_flutter_adapter/plugin_android_notification_backend.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

final now = DateTime.utc(2026, 11, 12, 22);
final future = DateTime.utc(2026, 11, 13, 22);

class FakeNative implements NotificationDeviceBackend {
  NotificationDeviceState snapshot = NotificationDeviceState(
    checkedAtUtc: now,
    supported: true,
    permissionGranted: true,
    channelEnabled: true,
    schedulerAvailable: true,
    exactAllowed: true,
  );
  int scheduled = 0;
  int cancelled = 0;
  bool accepted = true;
  bool? lastExact;
  bool throwProbe = false;

  @override
  Future<NotificationDeviceState> probeDevice() async {
    if (throwProbe) throw StateError('device_lost');
    return snapshot;
  }
  @override
  Future<bool> scheduleDevice(ReminderRequest r,
      {required bool exact}) async {
    scheduled++;
    lastExact = exact;
    return accepted;
  }
  @override
  Future<bool> cancelDevice(String id) async {
    cancelled++;
    return true;
  }
}

ReminderRequest request({bool exact = false}) => ReminderRequest(
  stableId: 'anna:reminder-1',
  scheduledAtUtc: future,
  title: 'A verified reminder intent',
  body: 'Not an OS delivery receipt',
  timezoneId: 'Europe/Rome',
  requireExact: exact,
);

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  test('fresh real-native probe mapping never mints delivery receipts', () async {
    final fake = FakeNative();
    final health = await FlutterNotificationPlatformPort(fake).probe();
    expect(health.deliveryReceiptVerified, isFalse);
    expect(health.statusFor(nowUtc: now, reminderId: 'anna:reminder-1'),
        CapabilityStatus.available);
    expect(fake.scheduled, 0);
  });
  test('Android 13 permission refusal stops schedule', () async {
    final fake = FakeNative()
      ..snapshot = NotificationDeviceState(
        checkedAtUtc: now, supported: true, permissionGranted: false,
        channelEnabled: true, schedulerAvailable: true, exactAllowed: true,
      );
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request()), ScheduleDecision.deniedPermission);
    expect(fake.scheduled, 0);
  });
  test('channel blocked stops schedule even if app permission granted', () async {
    final fake = FakeNative()
      ..snapshot = NotificationDeviceState(
        checkedAtUtc: now, supported: true, permissionGranted: true,
        channelEnabled: false, schedulerAvailable: true, exactAllowed: true,
      );
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request()), ScheduleDecision.blockedChannel);
    expect(fake.scheduled, 0);
  });
  test('no exact alarm entitlement -> explicit user opt-in fallback only', () async {
    final fake = FakeNative()
      ..snapshot = NotificationDeviceState(
        checkedAtUtc: now, supported: true, permissionGranted: true,
        channelEnabled: true, schedulerAvailable: true, exactAllowed: false,
      );
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request(exact: true)), ScheduleDecision.failed);
    expect(fake.scheduled, 0);
    expect(await c.schedule(request(exact: true),
        allowInexactFallback: true), ScheduleDecision.acceptedInexact);
    expect(fake.lastExact, isFalse);
  });
  test('native acceptance cannot be promoted to delivered', () async {
    final fake = FakeNative();
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request(exact: true)),
        ScheduleDecision.acceptedExact);
    expect(fake.scheduled, 1);
    expect((await FlutterNotificationPlatformPort(fake).probe())
        .deliveryReceiptVerified, isFalse);
    expect(fake.lastExact, isTrue);
  });
  test('stale native health is unknown and denied', () async {
    final fake = FakeNative()
      ..snapshot = NotificationDeviceState(
        checkedAtUtc: now.subtract(const Duration(hours: 1)),
        supported: true, permissionGranted: true, channelEnabled: true,
        schedulerAvailable: true, exactAllowed: true,
      );
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request()), ScheduleDecision.unsupported);
    expect(fake.scheduled, 0);
  });
  test('native exception is isolated from consumer data writes', () async {
    final fake = FakeNative()..throwProbe = true;
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.schedule(request()), ScheduleDecision.failed);
    expect(fake.scheduled, 0);
  });
  test('Android API24/25 no-channel semantics and API26+ restrictions', () {
    expect(androidChannelEnabledForSdk(
      sdkInt: 24, channels: const [], channelId: 'reminders'), isTrue);
    expect(androidChannelEnabledForSdk(
      sdkInt: 25, channels: const [], channelId: 'reminders'), isTrue);
    expect(androidChannelEnabledForSdk(
      sdkInt: 26, channels: const [], channelId: 'reminders'), isFalse);
    expect(androidChannelEnabledForSdk(
      sdkInt: null, channels: const [], channelId: 'reminders'), isNull);
    expect(androidChannelEnabledForSdk(
      sdkInt: 35, channels: null, channelId: 'reminders'), isNull);
    expect(androidChannelEnabledForSdk(
      sdkInt: 35, channels: const [
        AndroidNotificationChannel(
          'reminders', 'Reminders', importance: Importance.none,
        ),
      ], channelId: 'reminders'), isFalse);
    expect(androidChannelEnabledForSdk(
      sdkInt: 35, channels: const [
        AndroidNotificationChannel(
          'reminders', 'Reminders', importance: Importance.high,
        ),
      ], channelId: 'reminders'), isTrue);
  });

  test('Unicode IDs use UTF-8, not truncated UTF-16', () {
    expect(notificationIdFor('reminder:Ł'),
        isNot(notificationIdFor('reminder:A')));
  });

  test('stable ID is deterministic positive and cancel maps consistently', () async {
    expect(notificationIdFor('a:b'), notificationIdFor('a:b'));
    expect(notificationIdFor('a:b'), isNonNegative);
    expect(notificationIdFor('a:b'), lessThan(0x80000000));
    final fake = FakeNative();
    final c = NotificationCoordinator(FlutterNotificationPlatformPort(fake),
        nowUtc: () => now);
    expect(await c.cancel('a:b'), isTrue);
    expect(fake.cancelled, 1);
    expect(await c.cancel(''), isFalse);
  });
}
