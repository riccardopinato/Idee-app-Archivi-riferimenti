import 'package:factory_notification_kit/factory_notification_kit.dart';

/// This adapter translates a real, independently probed native backend into
/// the source-only X10-023 policy. No delivery receipt is minted.
abstract interface class NotificationDeviceBackend {
  Future<NotificationDeviceState> probeDevice();
  Future<bool> scheduleDevice(ReminderRequest reminder, {required bool exact});
  Future<bool> cancelDevice(String stableId);
}

/// A snapshot from the actual platform adapter, not UI preferences or a
/// previously registered alarm. Null always means UNKNOWN (fail closed).
class NotificationDeviceState {
  const NotificationDeviceState({
    required this.checkedAtUtc,
    required this.supported,
    required this.permissionGranted,
    required this.channelEnabled,
    required this.schedulerAvailable,
    required this.exactAllowed,
    this.errorCode,
  });

  final DateTime checkedAtUtc;
  final bool? supported;
  final bool? permissionGranted;
  final bool? channelEnabled;
  final bool? schedulerAvailable;
  final bool? exactAllowed;
  final String? errorCode;
}

/// Use NotificationCoordinator with this port to keep schedule admission and
/// fallback policy shared and to isolate native failures from user data saves.
class FlutterNotificationPlatformPort implements NotificationPlatformPort {
  const FlutterNotificationPlatformPort(this.device);

  final NotificationDeviceBackend device;

  @override
  Future<NotificationHealth> probe() async {
    final state = await device.probeDevice();
    return NotificationHealth(
      checkedAtUtc: state.checkedAtUtc,
      supported: state.supported,
      permissionGranted: state.permissionGranted,
      channelEnabled: state.channelEnabled,
      schedulerAvailable: state.schedulerAvailable,
      exactAllowed: state.exactAllowed,
      // Must come from a separately observed notification receipt, never
      // from a schedule() return value or pending OS queue inspection.
      deliveryReceiptVerified: false,
      deliveryReceiptReminderId: null,
      lastErrorCode: state.errorCode,
    );
  }

  @override
  Future<bool> schedule(ReminderRequest request, {required bool exact}) =>
      device.scheduleDevice(request, exact: exact);

  @override
  Future<bool> cancel(String stableId) => device.cancelDevice(stableId);
}
