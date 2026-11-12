import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:test/test.dart';

final now = DateTime.utc(2026, 11, 12, 12);

NotificationHealth health({
  bool? supported = true,
  bool? permission = true,
  bool? channel = true,
  bool? scheduler = true,
  bool? exact = true,
  bool receipt = false,
  String? observedId,
  DateTime? checkedAt,
  String? error,
}) =>
    NotificationHealth(
      checkedAtUtc: checkedAt ?? now,
      supported: supported,
      permissionGranted: permission,
      channelEnabled: channel,
      schedulerAvailable: scheduler,
      exactAllowed: exact,
      deliveryReceiptVerified: receipt,
      deliveryReceiptReminderId: observedId,
      lastErrorCode: error,
    );

ReminderRequest reminder({
  DateTime? when,
  bool exact = false,
  String id = 'user_123:meeting_456',
}) =>
    ReminderRequest(
      stableId: id,
      scheduledAtUtc: when ?? now.add(const Duration(minutes: 20)),
      title: 'A meeting',
      body: 'Reminder text',
      timezoneId: 'Europe/Rome',
      requireExact: exact,
    );

class FakePort implements NotificationPlatformPort {
  NotificationHealth next = health();
  int scheduleCount = 0;
  int cancelCount = 0;
  int probeCount = 0;
  bool? requestedExact;
  bool accept = true;
  bool fail = false;

  @override
  Future<NotificationHealth> probe() async {
    probeCount++;
    if (fail) throw StateError('platform_failure');
    return next;
  }

  @override
  Future<bool> schedule(ReminderRequest request, {required bool exact}) async {
    scheduleCount++;
    requestedExact = exact;
    if (fail) throw StateError('native_failure');
    return accept;
  }

  @override
  Future<bool> cancel(String stableId) async {
    cancelCount++;
    if (fail) throw StateError('cancel_failure');
    return true;
  }
}

void main() {
  test('permission and channel are distinct, unknown is not healthy', () {
    expect(
      health(permission: false).statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.permissionRequired,
    );
    expect(
      health(channel: false).statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.systemChannelBlocked,
    );
    expect(
      health(supported: null).statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.unknown,
    );
  });

  test('last scheduled is not a delivered receipt and wrong ID does not count', () {
    expect(
      health().statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.available,
    );
    expect(
      health(receipt: true, observedId: 'other')
          .statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.available,
    );
    expect(
      health(receipt: true, observedId: 'id')
          .statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.healthy,
    );
  });

  test('stale or future samples never count as healthy', () {
    for (final when in [
      now.subtract(const Duration(minutes: 6)),
      now.add(const Duration(seconds: 1)),
    ]) {
      final state = health(
        receipt: true,
        observedId: 'id',
        checkedAt: when,
      ).statusFor(nowUtc: now, reminderId: 'id');
      expect(state, CapabilityStatus.unknown);
    }
  });

  test('exact policy never silently falls back to inexact', () async {
    final port = FakePort()..next = health(exact: false);
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder(exact: true)), ScheduleDecision.failed);
    expect(port.scheduleCount, 0);
    expect(await c.schedule(reminder(exact: true), allowInexactFallback: true),
        ScheduleDecision.acceptedInexact);
    expect(port.requestedExact, isFalse);
  });

  test('exact allowed is still accepted not device delivered', () async {
    final port = FakePort();
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder(exact: true)),
        ScheduleDecision.acceptedExact);
    expect(port.requestedExact, isTrue);
    expect(
      port.next.statusFor(nowUtc: now, reminderId: 'user_123:meeting_456'),
      CapabilityStatus.available,
    );
  });

  test('OS disabled permission/channel does not invoke schedule', () async {
    final port = FakePort()..next = health(permission: false);
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder()),
        ScheduleDecision.deniedPermission);
    port.next = health(channel: false);
    expect(await c.schedule(reminder()),
        ScheduleDecision.blockedChannel);
    expect(port.scheduleCount, 0);
  });

  test('unsupported/stale probe does not pretend to schedule', () async {
    final port = FakePort()..next = health(supported: false);
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder()), ScheduleDecision.unsupported);
    port.next = health(checkedAt: now.subtract(const Duration(hours: 1)));
    expect(await c.schedule(reminder()), ScheduleDecision.unsupported);
    expect(port.scheduleCount, 0);
  });

  test('invalid scheduled time and ID do not invoke native provider', () async {
    final port = FakePort();
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder(when: now)), ScheduleDecision.invalidTime);
    expect(await c.schedule(reminder(id: '')), ScheduleDecision.invalidTime);
    expect(port.probeCount, 0);
  });

  test('native errors are isolated from consumer data writes', () async {
    final port = FakePort()..fail = true;
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder()), ScheduleDecision.failed);
    expect(await c.cancel('id'), isFalse);
  });

  test('cancel is stable and invalid ID never reaches provider', () async {
    final port = FakePort();
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.cancel(''), isFalse);
    expect(await c.cancel('id'), isTrue);
    expect(port.cancelCount, 1);
  });

  test('provider refusal never produces false scheduling success', () async {
    final port = FakePort()..accept = false;
    final c = NotificationCoordinator(port, nowUtc: () => now);
    expect(await c.schedule(reminder()), ScheduleDecision.failed);
    expect(port.scheduleCount, 1);
  });

  test('diagnostic error degrades health even with old receipt', () {
    expect(
      health(receipt: true, observedId: 'id', error: 'CHANNEL_ERROR')
          .statusFor(nowUtc: now, reminderId: 'id'),
      CapabilityStatus.degraded,
    );
  });
}
