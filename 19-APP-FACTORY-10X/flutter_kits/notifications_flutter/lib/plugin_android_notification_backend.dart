import 'dart:convert';

import 'package:crypto/crypto.dart';
import 'package:factory_notification_kit/factory_notification_kit.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:timezone/data/latest.dart' as timezone_data;
import 'package:timezone/timezone.dart' as tz;

import 'factory_flutter_notification_adapter.dart';

/// Android backend for the consumer's existing initialized plugin singleton.
/// The app, not this adapter, owns initialization and notification callbacks.
/// Manifest permissions/receivers, alarm policy and physical QA remain app-owned.
class PluginAndroidNotificationBackend implements NotificationDeviceBackend {
  PluginAndroidNotificationBackend({
    required this.plugin,
    required this.nowUtc,
    required this.channelId,
    required this.channelName,
    required this.ensureConsumerPluginInitialized,
    required this.androidSdkInt,
    this.channelDescription = 'Scheduled reminders',
  });

  final FlutterLocalNotificationsPlugin plugin;
  final DateTime Function() nowUtc;
  final String channelId;
  final String channelName;
  final String channelDescription;

  /// Call the consumer-owned initializer that preserves its existing tap and
  /// action callbacks. Never call plugin.initialize() in this shared backend.
  final Future<bool> Function() ensureConsumerPluginInitialized;

  /// Actual Android Build.VERSION.SDK_INT, supplied by the consumer platform.
  /// No SDK inference from a channel list (API 24-25 have no channels).
  final Future<int?> Function() androidSdkInt;

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
      final sdk = await androidSdkInt();
      if (sdk == null || sdk < 21) return null;
      if (!await ensureConsumerPluginInitialized()) return null;
      timezone_data.initializeTimeZones();
      if (sdk >= 26) {
        await android.createNotificationChannel(AndroidNotificationChannel(
          channelId,
          channelName,
          description: channelDescription,
          importance: Importance.high,
        ));
      }
      _initialized = true;
    }
    return android;
  }

  @override
  Future<NotificationDeviceState> probeDevice() async {
    final checkedAt = nowUtc().toUtc();
    if (!_android) {
      return NotificationDeviceState(
        checkedAtUtc: checkedAt, supported: false,
        permissionGranted: null, channelEnabled: null,
        schedulerAvailable: false, exactAllowed: null,
      );
    }
    try {
      final android = await _prepare();
      if (android == null) throw StateError('NATIVE_PLUGIN_NOT_READY');
      final allowed = await android.areNotificationsEnabled();
      final sdk = await androidSdkInt();
      final channels = await android.getNotificationChannels();
      final exact = await android.canScheduleExactNotifications();
      return NotificationDeviceState(
        checkedAtUtc: checkedAt,
        supported: true,
        permissionGranted: allowed,
        channelEnabled: androidChannelEnabledForSdk(
          sdkInt: sdk, channels: channels, channelId: channelId,
        ),
        // Plugin readiness != actual delivery; the same APK still requires
        // device validation, Doze/reboot/Android permission tests.
        schedulerAvailable: true,
        exactAllowed: exact,
      );
    } catch (_) {
      return NotificationDeviceState(
        checkedAtUtc: checkedAt,
        supported: true, permissionGranted: null, channelEnabled: null,
        schedulerAvailable: null, exactAllowed: null,
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
            channelId,
            channelName,
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
      // Only OS scheduling requested: no delivery receipt is generated.
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

/// UTF-8 stable IDs, truncated to Android's positive 31-bit notification ID.
/// The app's canonical reminder store MUST guard residual 31-bit collisions.
int notificationIdFor(String stableId) {
  final bytes = sha256.convert(utf8.encode(stableId)).bytes;
  final n = (bytes[0] << 24) | (bytes[1] << 16) |
      (bytes[2] << 8) | bytes[3];
  return n & 0x7fffffff;
}

/// Android 7.x (API 24-25) has no channel subsystem. Empty channel lists
/// are expected and must not be mistaken for a disabled channel. On 26+,
/// a real configured and enabled channel must exist. Missing SDK evidence
/// always yields unknown, never fabricated healthy.
bool? androidChannelEnabledForSdk({
  required int? sdkInt,
  required List<AndroidNotificationChannel>? channels,
  required String channelId,
}) {
  if (sdkInt == null || sdkInt < 21) return null;
  if (sdkInt < 26) return true;
  if (channels == null) return null;
  for (final channel in channels) {
    if (channel.id == channelId) {
      return channel.importance != Importance.none;
    }
  }
  return false;
}
