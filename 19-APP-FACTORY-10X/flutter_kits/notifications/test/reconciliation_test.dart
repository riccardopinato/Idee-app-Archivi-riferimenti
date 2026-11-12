import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:factory_notification_kit/notification_reconciliation.dart';
import 'package:test/test.dart';

final now = DateTime.utc(2026, 11, 12, 12);
final future = DateTime.utc(2026, 11, 13, 12);

class FakeTz implements TimezoneResolutionPort {
  List<DateTime> possible = [future];
  int calls = 0;
  String? resolvedZone;
  bool explode = false;
  @override
  List<DateTime> possibleUtcInstants(CivilTime local, String zoneId) {
    calls++;
    resolvedZone = zoneId;
    if (explode) throw StateError('no_timezone_database');
    return possible;
  }
}

NotificationHealth healthy({
  bool? permission = true,
  bool? channel = true,
  bool? scheduler = true,
  bool? exact = true,
  DateTime? checkedAt,
}) => NotificationHealth(
      checkedAtUtc: checkedAt ?? now,
      supported: true,
      permissionGranted: permission,
      channelEnabled: channel,
      schedulerAvailable: scheduler,
      exactAllowed: exact,
    );

ReconcileEnvironment env({
  ReconcileTrigger trigger = ReconcileTrigger.osReboot,
  String zone = 'Europe/Rome',
  NotificationHealth? health,
}) => ReconcileEnvironment(
      nowUtc: now,
      deviceZoneId: zone,
      health: health ?? healthy(),
      trigger: trigger,
    );

StoredReminderIntent fixed({
  String id = 'owner:reminder-1',
  DateTime? at,
  DateTime? scheduled,
  bool exact = false,
  bool fallback = false,
  bool enabled = true,
}) => StoredReminderIntent(
      id: id,
      policy: ReminderClockPolicy.fixedUtcInstant,
      fixedAtUtc: at ?? future,
      lastScheduledAtUtc: scheduled,
      requireExact: exact,
      allowInexactFallback: fallback,
      enabled: enabled,
    );

StoredReminderIntent wall({
  ReminderClockPolicy policy = ReminderClockPolicy.fixedLocalWallClock,
  String? zone = 'Europe/Rome',
}) => StoredReminderIntent(
      id: 'owner:reminder-2',
      policy: policy,
      wallClock: const CivilTime(2026, 11, 13, 13, 0),
      zoneId: zone,
    );

void main() {
  test('reboot reschedule is only a proposal and no fake delivery', () {
    final resolver = FakeTz();
    final item = const ReconciliationPlanner(resolver)
        .plan([fixed(scheduled: future)], env()).single;
    expect(item.action, ReconcileAction.proposeInexactSchedule);
    expect(item.proposedAtUtc, future);
    expect(item.platformSchedulePerformed, isFalse);
    expect(item.delivered, isFalse);
    expect(resolver.calls, 0);
  });

  test('app start leaves already scheduled instant unchanged; not a receipt', () {
    final row = ReconciliationPlanner(FakeTz()).plan(
      [fixed(scheduled: future)],
      env(trigger: ReconcileTrigger.appStart),
    ).single;
    expect(row.action, ReconcileAction.leaveUnchanged);
    expect(row.delivered, isFalse);
  });

  test('timezone change preserves fixed UTC instant', () {
    final row = ReconciliationPlanner(FakeTz()).plan(
      [fixed()],
      env(trigger: ReconcileTrigger.deviceTimezoneChanged, zone: 'Asia/Tokyo'),
    ).single;
    expect(row.proposedAtUtc, future);
    expect(row.proposedZoneId, isNull);
  });

  test('wall-clock policy retains chosen IANA timezone', () {
    final tz = FakeTz();
    final row = ReconciliationPlanner(tz).plan(
      [wall()], env(zone: 'America/New_York'),
    ).single;
    expect(row.action, ReconcileAction.proposeInexactSchedule);
    expect(row.proposedZoneId, 'Europe/Rome');
    expect(tz.resolvedZone, 'Europe/Rome');
  });

  test('floating wall-clock uses current device zone after switch', () {
    final tz = FakeTz();
    final row = ReconciliationPlanner(tz).plan(
      [wall(policy: ReminderClockPolicy.floatingDeviceWallClock)],
      env(trigger: ReconcileTrigger.deviceTimezoneChanged, zone: 'Asia/Tokyo'),
    ).single;
    expect(row.proposedZoneId, 'Asia/Tokyo');
    expect(tz.resolvedZone, 'Asia/Tokyo');
  });

  test('spring DST gap and resolver failure are blocked not guessed', () {
    final tz = FakeTz()..possible = [];
    var row = ReconciliationPlanner(tz).plan([wall()], env()).single;
    expect(row.action, ReconcileAction.blockedTimezone);
    tz.explode = true;
    row = ReconciliationPlanner(tz).plan([wall()], env()).single;
    expect(row.action, ReconcileAction.blockedTimezone);
  });

  test('autumn DST repeated local timestamp needs owner choice', () {
    final tz = FakeTz()..possible = [
      DateTime.utc(2026, 11, 13, 11),
      DateTime.utc(2026, 11, 13, 12),
    ];
    final row = ReconciliationPlanner(tz).plan([wall()], env()).single;
    expect(row.action, ReconcileAction.needsUserChoice);
    expect(row.proposedAtUtc, isNull);
  });

  test('unknown or malformed timezone never passes resolver', () {
    final tz = FakeTz();
    for (final zone in [null, '', '../Rome', 'Europe/../../secret']) {
      final row = ReconciliationPlanner(tz).plan([
        wall(policy: ReminderClockPolicy.fixedLocalWallClock, zone: zone),
      ], env()).single;
      expect(row.action, ReconcileAction.blockedTimezone);
    }
    expect(tz.calls, 0);
  });

  test('denied permission and channel disabled cannot become schedule', () {
    for (final h in [
      healthy(permission: false),
      healthy(channel: false),
    ]) {
      final row = ReconciliationPlanner(FakeTz()).plan(
        [fixed()], env(health: h),
      ).single;
      expect(row.action, anyOf(
        ReconcileAction.blockedPermission,
        ReconcileAction.blockedChannel,
      ));
      expect(row.proposedAtUtc, isNull);
    }
  });

  test('unknown/stale probes cannot create proposals', () {
    for (final h in [
      healthy(permission: null),
      healthy(checkedAt: now.subtract(const Duration(hours: 1))),
      healthy(scheduler: false),
    ]) {
      final row = ReconciliationPlanner(FakeTz()).plan(
        [fixed()], env(health: h),
      ).single;
      expect(row.action, anyOf(
        ReconcileAction.blockedPlatformEvidence,
        ReconcileAction.blockedScheduler,
      ));
    }
  });

  test('exact alarm fallback is never implicit', () {
    final context = env(health: healthy(exact: false));
    final strict = ReconciliationPlanner(FakeTz())
        .plan([fixed(exact: true)], context).single;
    expect(strict.action, ReconcileAction.blockedExactAlarm);
    final consent = ReconciliationPlanner(FakeTz())
        .plan([fixed(exact: true, fallback: true)], context).single;
    expect(consent.action, ReconcileAction.proposeInexactSchedule);
  });

  test('disabled user reminders and expired records are preserved', () {
    final items = ReconciliationPlanner(FakeTz()).plan([
      fixed(enabled: false),
      fixed(id: 'expired', at: now),
    ], env());
    expect(items[0].action, ReconcileAction.leaveUnchanged);
    expect(items[1].action, ReconcileAction.expiredNeedsOwnerPolicy);
  });

  test('duplicate IDs and impossible civil time reject the whole batch', () {
    const planner = ReconciliationPlanner(FakeTz());
    expect(() => planner.plan([fixed(), fixed()], env()), throwsFormatException);
    final invalid = StoredReminderIntent(
      id: 'invalid_date',
      policy: ReminderClockPolicy.fixedLocalWallClock,
      wallClock: const CivilTime(2026, 2, 30, 12, 0),
      zoneId: 'Europe/Rome',
    );
    expect(() => planner.plan([invalid], env()), throwsFormatException);
  });

  test('unstable resolver returning non UTC instant is rejected', () {
    final tz = FakeTz()..possible = [DateTime(2026, 11, 13, 12)];
    final row = ReconciliationPlanner(tz).plan([wall()], env()).single;
    expect(row.action, ReconcileAction.blockedTimezone);
  });

  test('reconciliation batch upper bound rejects massive replays', () {
    final items = List.generate(129, (index) => fixed(id: 'id_${index}'));
    expect(() => ReconciliationPlanner(FakeTz())
        .plan(items, env()), throwsFormatException);
  });
}
