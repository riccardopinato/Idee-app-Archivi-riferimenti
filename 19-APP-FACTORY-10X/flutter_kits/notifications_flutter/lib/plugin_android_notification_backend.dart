import 'package:crypto/crypto.dart';
import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:timezone/data/latest.dart' as timezone_data;
import 'package:timezone/timezone.dart' as tz;

import 'factory_flutter_notification_adapter.dart';

/// Real flutter_local_notifications Android backend, isolated from source
/// policy. The app owns its reminders, Manifest/receivers, channel and UX.
/// No notification permission request or foreground service is performed.
class PluginAndroidNotificationBackend implements NotificationDeviceBackend {
  PluginAndroidNotificationBackend({
    required this.plugin,
    required this.nowUtc,
    required this.channelId,
    required this.channelName,
    this.channelDescription = 'Scheduled reminders',
    this.androidSmallIcon = '@mipmap/ic_launcher',
  });

  final FlutterLocalNotificationsPlugin plugin;
  final DateTime Function() nowUtc;
  final String channelId;
  final String channelName;
  final String channelDescription;
  final String androidSmallIcon;

  bool _initialized = false;

  bool get _android =>
      !kIsWeb && defaultTargetPlatform == TargetPlatform.android;

  Future<AndroidFlutterLocalNotificationsPlugin?> _prepare() async {
    if (!_android) return null;
    final android = plugin.resolvePlatformSpecificImplementation<
        AndroidFlutterLocalNotificationsPlugin>();
    if (android == null || channelId.isEmpty || channelName.isEmpty) {
      return null;
    }
    if (!_initialized) {
      timezone_data.initializeTimeZones();
      final ok = await plugin.initialize(
        settings: InitializationSettings(
          android: AndroidInitializationSettings(androidSmallIcon),
        ),
      );
      if (ok == false) return null;
      await android.createNotificationChannel(AndroidNotificationChannel(
        channelId,
        channelName,
        description: channelDescription,
        importance: Importance.high,
      ));
      _initialized = true;
    }
    return android;
  }

  @override
  Future<NotificationDeviceState> probeDevice() async {
    final checkedAt = nowUtc().toUtc();
    if (!_android) {
      return NotificationDeviceState(
        checkedAtUtc: checkedAt,
        supported: false,
        permissionGranted: null,
        channelEnabled: null,
        schedulerAvailable: false,
        exactAllowed: null,
      );
    }
    try {
      final android = await _prepare();
      if (android == null) throw StateError('NATIVE_PLUGIN_NOT_READY');
      final allowed = await android.areNotificationsEnabled();
      final channels = await android.getNotificationChannels();
      final exact = await android.canScheduleExactNotifications();
      final channel = channels == null
          ? null
          : channels.where((c) => c.id == channelId).firstOrNull;
      return NotificationDeviceState(
        checkedAtUtc: checkedAt,
        supported: true,
        permissionGranted: allowed,
        channelEnabled: channels == null
            ? null
            : (channel != null && channel.importance != Importance.none),
        // A prepared plugin is an API admission check only, not an OS
        // delivery observation. Physical validation is still required.
        schedulerAvailable: true,
        exactAllowed: exact,
      );
    } catch (_) {
      return NotificationDeviceState(
        checkedAtUtc: checkedAt,
        supported: true,
        permissionGranted: null,
        channelEnabled: null,
        schedulerAvailable: null,
        exactAllowed: null,
        errorCode: 'NATIVE_PROBE_FAILURE',
      );
    }
  }

  @override
  Future<bool> scheduleDevice(ReminderRequest reminder,
      {required bool exact}) async {
    try {
      final android = await _prepare();
      if (android == null || !reminder.scheduledAtUtc.isUtc) return false;
      // Never schedule without a fresh permission/channel/exact probe.
      final health = await probeDevice();
      if (health.permissionGranted != true ||
          health.channelEnabled != true ||
          health.schedulerAvailable != true ||
          (exact && health.exactAllowed != true)) return false;
      final zone = tz.getLocation(reminder.timezoneId);
      final at = tz.TZDateTime.from(reminder.scheduledAtUtc, zone);
      if (!reminder.scheduledAtUtc.isAfter(nowUtc().toUtc())) return false;
      await plugin.zonedSchedule(
        id: notificationIdFor(reminder.stableId),
        title: reminder.title,
        body: reminder.body,
        scheduledDate: at,
        notificationDetails: NotificationDetails(
          android: AndroidNotificationDetails(
            channelId, channelName,
            channelDescription: channelDescription,
            importance: Importance.high,
            priority: Priority.high,
          ),
        ),
        androidScheduleMode: exact
            ? AndroidScheduleMode.exactAllowWhileIdle
            : AndroidScheduleMode.inexactAllowWhileIdle,
        payload: reminder.stableId,
      );
      // "true" means native schedule accepted, never delivered.
      return true;
    } catch (_) {
      return false;
    }
  }

  @override
  Future<bool> cancelDevice(String stableId) async {
    try {
      final android = await _prepare();
      if (android == null || stableId.isEmpty) return false;
      await plugin.cancel(id: notificationIdFor(stableId));
      return true;
    } catch (_) {
      return false;
    }
  }
}

/// Deterministic positive 31-bit ID. Collision review belongs to the app's
/// persisted reminder owner; the kit does not keep another mapping database.
int notificationIdFor(String stableId) {
  final bytes = sha256.convert(stableId.codeUnits).bytes;
  final n = (bytes[0] << 24) | (bytes[1] << 16) |
      (bytes[2] << 8) | bytes[3];
  return n & 0x7fffffff;
}
