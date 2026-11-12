/// X10-023: platform-independent notification health and scheduling policy.
/// No plugin, Android permission, timezone database or receiver is installed.

enum CapabilityStatus {
  unknown,
  unsupported,
  permissionRequired,
  denied,
  systemChannelBlocked,
  schedulerUnavailable,
  available,
  degraded,
  healthy,
}

enum ScheduleDecision {
  acceptedExact,
  acceptedInexact,
  deniedPermission,
  blockedChannel,
  unsupported,
  invalidTime,
  failed,
}

class NotificationHealth {
  const NotificationHealth({
    required this.checkedAtUtc,
    required this.supported,
    required this.permissionGranted,
    required this.channelEnabled,
    required this.schedulerAvailable,
    required this.exactAllowed,
    this.deliveryReceiptVerified = false,
    this.deliveryReceiptReminderId,
    this.lastErrorCode,
  });

  final DateTime checkedAtUtc;
  final bool? supported;
  final bool? permissionGranted;
  final bool? channelEnabled;
  final bool? schedulerAvailable;
  final bool? exactAllowed;
  final bool deliveryReceiptVerified;
  final String? deliveryReceiptReminderId;
  final String? lastErrorCode;

  CapabilityStatus statusFor({
    required DateTime nowUtc,
    required String reminderId,
    Duration validFor = const Duration(minutes: 5),
  }) {
    // Never show a historical PASS as today's health, even after system
    // permissions, channels or background settings may have changed.
    if (!nowUtc.isUtc ||
        !checkedAtUtc.isUtc ||
        nowUtc.isBefore(checkedAtUtc) ||
        nowUtc.difference(checkedAtUtc) > validFor ||
        validFor <= Duration.zero) {
      return CapabilityStatus.unknown;
    }
    if (supported == false) return CapabilityStatus.unsupported;
    if (supported == null) return CapabilityStatus.unknown;
    if (permissionGranted == false) return CapabilityStatus.permissionRequired;
    if (permissionGranted == null) return CapabilityStatus.unknown;
    if (channelEnabled == false) return CapabilityStatus.systemChannelBlocked;
    if (channelEnabled == null) return CapabilityStatus.unknown;
    if (schedulerAvailable == false) return CapabilityStatus.schedulerUnavailable;
    if (schedulerAvailable == null) return CapabilityStatus.unknown;
    if (lastErrorCode != null) return CapabilityStatus.degraded;
    if (deliveryReceiptVerified && deliveryReceiptReminderId == reminderId) {
      return CapabilityStatus.healthy;
    }
    return CapabilityStatus.available;
  }
}

class ReminderRequest {
  ReminderRequest({
    required this.stableId,
    required this.scheduledAtUtc,
    required this.title,
    required this.body,
    required this.timezoneId,
    this.requireExact = false,
  });

  final String stableId;
  final DateTime scheduledAtUtc;
  final String title;
  final String body;
  /// IANA timezone is validated/resolved by the supplied platform adapter.
  final String timezoneId;
  final bool requireExact;
}

abstract interface class NotificationPlatformPort {
  /// Must independently interrogate OS/channel/permission/scheduler state;
  /// a successful call to schedule does not prove delivery.
  Future<NotificationHealth> probe();
  Future<bool> schedule(ReminderRequest request, {required bool exact});
  Future<bool> cancel(String stableId);
}

class NotificationCoordinator {
  NotificationCoordinator(this.platform, {required this.nowUtc});

  final NotificationPlatformPort platform;
  final DateTime Function() nowUtc;

  bool _valid(ReminderRequest request) {
    final now = nowUtc();
    return now.isUtc &&
        request.scheduledAtUtc.isUtc &&
        request.scheduledAtUtc.isAfter(now) &&
        request.stableId.trim().isNotEmpty &&
        request.stableId.length <= 96 &&
        request.title.trim().isNotEmpty &&
        request.title.length <= 256 &&
        request.body.length <= 2048 &&
        request.timezoneId.trim().isNotEmpty &&
        request.timezoneId.length <= 96;
  }

  Future<ScheduleDecision> schedule(
    ReminderRequest request, {
    bool allowInexactFallback = false,
  }) async {
    if (!_valid(request)) return ScheduleDecision.invalidTime;
    try {
      final health = await platform.probe();
      final status = health.statusFor(
        nowUtc: nowUtc(),
        reminderId: request.stableId,
      );
      if (status == CapabilityStatus.unknown ||
          status == CapabilityStatus.unsupported) {
        return ScheduleDecision.unsupported;
      }
      if (status == CapabilityStatus.permissionRequired ||
          status == CapabilityStatus.denied) {
        return ScheduleDecision.deniedPermission;
      }
      if (status == CapabilityStatus.systemChannelBlocked) {
        return ScheduleDecision.blockedChannel;
      }
      if (status == CapabilityStatus.schedulerUnavailable ||
          status == CapabilityStatus.degraded) {
        return ScheduleDecision.failed;
      }
      if (request.requireExact && health.exactAllowed != true) {
        if (!allowInexactFallback) return ScheduleDecision.failed;
        final accepted = await platform.schedule(request, exact: false);
        return accepted
            ? ScheduleDecision.acceptedInexact
            : ScheduleDecision.failed;
      }
      final exact = request.requireExact && health.exactAllowed == true;
      final accepted = await platform.schedule(request, exact: exact);
      return accepted
          ? exact
              ? ScheduleDecision.acceptedExact
              : ScheduleDecision.acceptedInexact
          : ScheduleDecision.failed;
    } catch (_) {
      // Notifications must not throw through the consumer's core data save.
      return ScheduleDecision.failed;
    }
  }

  Future<bool> cancel(String stableId) async {
    if (stableId.trim().isEmpty || stableId.length > 96) return false;
    try {
      return await platform.cancel(stableId);
    } catch (_) {
      return false;
    }
  }
}
