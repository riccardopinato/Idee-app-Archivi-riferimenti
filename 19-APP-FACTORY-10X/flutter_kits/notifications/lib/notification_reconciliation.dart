/// X10-023: restart/timezone/permission reconciliation *decision plan* only.
/// Never infer OS delivery, create alarms, move user data or auto-enable exact.
/// A per-platform adapter must independently verify timezone and OS state.
import 'factory_notification_kit.dart';

enum ReminderClockPolicy { fixedUtcInstant, fixedLocalWallClock, floatingDeviceWallClock }

enum ReconcileTrigger {
  appStart,
  osReboot,
  appUpgraded,
  deviceTimezoneChanged,
  systemClockChanged,
  permissionChanged,
}

enum ReconcileAction {
  leaveUnchanged,
  proposeExactSchedule,
  proposeInexactSchedule,
  needsUserChoice,
  expiredNeedsOwnerPolicy,
  blockedPlatformEvidence,
  blockedPermission,
  blockedChannel,
  blockedScheduler,
  blockedExactAlarm,
  blockedTimezone,
}

/// Local civil time as written by the user (not an implicitly normalized
/// DateTime in whatever timezone the process happens to use).
class CivilTime {
  const CivilTime(this.year, this.month, this.day, this.hour, this.minute);

  final int year, month, day, hour, minute;

  bool get valid {
    if (year < 2000 || year > 2100 || month < 1 || month > 12 ||
        day < 1 || day > 31 || hour < 0 || hour > 23 ||
        minute < 0 || minute > 59) return false;
    final normalized = DateTime.utc(year, month, day, hour, minute);
    return normalized.year == year && normalized.month == month &&
        normalized.day == day && normalized.hour == hour &&
        normalized.minute == minute;
  }
}

class StoredReminderIntent {
  const StoredReminderIntent({
    required this.id,
    required this.policy,
    this.fixedAtUtc,
    this.wallClock,
    this.zoneId,
    this.lastScheduledAtUtc,
    this.enabled = true,
    this.requireExact = false,
    this.allowInexactFallback = false,
  });

  final String id;
  final ReminderClockPolicy policy;
  final DateTime? fixedAtUtc;
  final CivilTime? wallClock;
  final String? zoneId;
  final DateTime? lastScheduledAtUtc;
  final bool enabled;
  final bool requireExact;
  final bool allowInexactFallback;
}

/// Return precisely the possible UTC instants for this local civil timestamp.
/// [] means DST gap, [one] is unambiguous, [two] means DST overlap.
/// No IANA timezone database is bundled into the pure Dart contract.
abstract interface class TimezoneResolutionPort {
  List<DateTime> possibleUtcInstants(CivilTime local, String zoneId);
}

class ReconcileEnvironment {
  const ReconcileEnvironment({
    required this.nowUtc,
    required this.deviceZoneId,
    required this.health,
    required this.trigger,
  });

  final DateTime nowUtc;
  final String deviceZoneId;
  final NotificationHealth health;
  final ReconcileTrigger trigger;
}

class ReconcileRecommendation {
  const ReconcileRecommendation({
    required this.id,
    required this.action,
    required this.reason,
    this.proposedAtUtc,
    this.proposedZoneId,
  });

  final String id;
  final ReconcileAction action;
  final String reason;
  final DateTime? proposedAtUtc;
  final String? proposedZoneId;
  bool get platformSchedulePerformed => false;
  bool get delivered => false;
}

class ReconciliationPlanner {
  const ReconciliationPlanner(this.timezone);

  final TimezoneResolutionPort timezone;

  List<ReconcileRecommendation> plan(
    List<StoredReminderIntent> reminders,
    ReconcileEnvironment env,
  ) {
    if (!env.nowUtc.isUtc || reminders.length > 128) {
      throw const FormatException('invalid_reconciliation_batch');
    }
    final seen = <String>{};
    final planned = <ReconcileRecommendation>[];
    for (final r in reminders) {
      if (r.id.trim().isEmpty || r.id.length > 96 ||
          !seen.add(r.id) ||
          (r.lastScheduledAtUtc != null && !r.lastScheduledAtUtc!.isUtc)) {
        throw const FormatException('invalid_or_duplicate_reminder_id');
      }
      if (!r.enabled) {
        planned.add(ReconcileRecommendation(
          id: r.id, action: ReconcileAction.leaveUnchanged,
          reason: 'USER_DISABLED',
        ));
        continue;
      }

      DateTime? target;
      String? zone;
      if (r.policy == ReminderClockPolicy.fixedUtcInstant) {
        if (r.fixedAtUtc == null || !r.fixedAtUtc!.isUtc ||
            r.wallClock != null) {
          throw const FormatException('invalid_fixed_instant');
        }
        target = r.fixedAtUtc!;
      } else {
        if (r.wallClock == null || !r.wallClock!.valid ||
            r.fixedAtUtc != null) {
          throw const FormatException('invalid_wall_clock');
        }
        zone = r.policy == ReminderClockPolicy.floatingDeviceWallClock
            ? env.deviceZoneId
            : r.zoneId;
        if (zone == null || !_zoneLabelSafe(zone)) {
          planned.add(ReconcileRecommendation(
            id: r.id, action: ReconcileAction.blockedTimezone,
            reason: 'TIMEZONE_INVALID_OR_UNKNOWN',
          ));
          continue;
        }
        List<DateTime> possibilities;
        try {
          possibilities = timezone.possibleUtcInstants(r.wallClock!, zone);
        } catch (_) {
          possibilities = const [];
        }
        if (possibilities.isEmpty || possibilities.length > 2 ||
            possibilities.any((t) => !t.isUtc)) {
          planned.add(ReconcileRecommendation(
            id: r.id, action: ReconcileAction.blockedTimezone,
            reason: 'DST_GAP_OR_RESOLVER_FAILURE',
          ));
          continue;
        }
        if (possibilities.length > 1) {
          planned.add(ReconcileRecommendation(
            id: r.id, action: ReconcileAction.needsUserChoice,
            reason: 'DST_AMBIGUOUS_WALL_CLOCK',
          ));
          continue;
        }
        target = possibilities.single;
      }

      if (!target.isAfter(env.nowUtc)) {
        planned.add(ReconcileRecommendation(
          id: r.id, action: ReconcileAction.expiredNeedsOwnerPolicy,
          reason: 'DUE_AT_OR_BEFORE_NOW',
        ));
        continue;
      }

      final capability = env.health.statusFor(
        nowUtc: env.nowUtc, reminderId: r.id,
      );
      final ReconcileAction? blocked;
      switch (capability) {
        case CapabilityStatus.permissionRequired:
        case CapabilityStatus.denied:
          blocked = ReconcileAction.blockedPermission;
          break;
        case CapabilityStatus.systemChannelBlocked:
          blocked = ReconcileAction.blockedChannel;
          break;
        case CapabilityStatus.schedulerUnavailable:
          blocked = ReconcileAction.blockedScheduler;
          break;
        case CapabilityStatus.unknown:
        case CapabilityStatus.unsupported:
        case CapabilityStatus.degraded:
          blocked = ReconcileAction.blockedPlatformEvidence;
          break;
        case CapabilityStatus.available:
        case CapabilityStatus.healthy:
          blocked = null;
          break;
      }
      if (blocked != null) {
        planned.add(ReconcileRecommendation(
          id: r.id, action: blocked, reason: 'NATIVE_HEALTH_NOT_READY',
        ));
        continue;
      }
      if (r.requireExact && env.health.exactAllowed != true &&
          !r.allowInexactFallback) {
        planned.add(ReconcileRecommendation(
          id: r.id, action: ReconcileAction.blockedExactAlarm,
          reason: 'EXACT_ALARM_CONSENT_OR_OS_CAPABILITY_REQUIRED',
        ));
        continue;
      }

      // App restart is not evidence the OS lost a previously registered
      // alarm. Reconcile only after a known platform invalidation trigger.
      final mustRecheck = env.trigger != ReconcileTrigger.appStart ||
          r.lastScheduledAtUtc != target;
      if (!mustRecheck) {
        planned.add(ReconcileRecommendation(
          id: r.id, action: ReconcileAction.leaveUnchanged,
          reason: 'UNCHANGED_SOURCE_REMINDER_NO_DELIVERY_PROOF',
        ));
        continue;
      }
      final exact = r.requireExact && env.health.exactAllowed == true;
      planned.add(ReconcileRecommendation(
        id: r.id,
        action: exact ? ReconcileAction.proposeExactSchedule
            : ReconcileAction.proposeInexactSchedule,
        reason: 'OS_RESCHEDULE_REQUIRED_OR_STATUS_UNCERTAIN',
        proposedAtUtc: target,
        proposedZoneId: zone,
      ));
    }
    return List<ReconcileRecommendation>.unmodifiable(planned);
  }

  bool _zoneLabelSafe(String zone) {
    if (zone == 'UTC') return true;
    return zone.length <= 80 &&
        RegExp(r'^[A-Za-z_]+(?:/[A-Za-z0-9_+-]+)+$').hasMatch(zone);
  }
}
