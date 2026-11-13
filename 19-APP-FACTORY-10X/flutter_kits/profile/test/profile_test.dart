import 'dart:async';
import 'dart:convert';

import 'package:factory_profile_kit/factory_profile_kit.dart';
import 'package:test/test.dart';

class MemoryStore implements ProfilePreferencesStore {
  String? document;
  bool failNextWrite = false;
  int writes = 0;

  @override
  Future<String?> read() async => document;

  @override
  Future<void> writeAtomically(String jsonDocument) async {
    if (failNextWrite) {
      failNextWrite = false;
      throw StateError('disk_full');
    }
    document = jsonDocument;
    writes++;
  }
}

class DeferredReadStore implements ProfilePreferencesStore {
  final Completer<String?> completion = Completer<String?>();
  int reads = 0;
  String? document;

  @override
  Future<String?> read() {
    reads++;
    return completion.future;
  }

  @override
  Future<void> writeAtomically(String jsonDocument) async {
    document = jsonDocument;
  }
}

void main() {
  test('defaults to local-first, no telemetry consent and system theme', () async {
    final controller = ProfileSettingsController(MemoryStore());
    final prefs = await controller.load();
    expect(prefs.displayName, '');
    expect(prefs.locale, 'system');
    expect(prefs.theme, ProfileTheme.system);
    expect(prefs.analyticsOptIn, isFalse);
  });

  test('simultaneous load shares one read and cannot clobber a later update', () async {
    final store = DeferredReadStore();
    final controller = ProfileSettingsController(store);
    final first = controller.load();
    final second = controller.load();
    expect(store.reads, 1);
    store.completion.complete(jsonEncode({
      'schema_version': 1,
      'display_name': 'Old',
      'locale': 'it',
      'theme': 'system',
      'analytics_opt_in': false,
    }));
    await Future.wait([first, second]);
    await controller.update((p) => p.copyWith(displayName: 'New'));
    expect((await controller.load()).displayName, 'New');
    expect(store.reads, 1);
    expect(jsonDecode(store.document!)['display_name'], 'New');
  });

  test('atomic write failure never changes the visible state', () async {
    final store = MemoryStore();
    final controller = ProfileSettingsController(store);
    await controller.load();
    store.failNextWrite = true;
    await expectLater(
      controller.update((p) => p.copyWith(displayName: 'Anna')),
      throwsStateError,
    );
    expect(controller.current.displayName, '');
    expect(store.writes, 0);
    await controller.update((p) => p.copyWith(displayName: 'Rita'));
    expect(controller.current.displayName, 'Rita');
    expect(store.writes, 1);
  });

  test('concurrent edits are serialized, not last-write-wins from old snapshot', () async {
    final store = MemoryStore();
    final controller = ProfileSettingsController(store);
    await controller.load();
    await Future.wait([
      controller.update((p) => p.copyWith(displayName: 'A')),
      controller.update((p) => p.copyWith(locale: 'it')),
      controller.update((p) => p.copyWith(theme: ProfileTheme.dark)),
    ]);
    expect(controller.current.displayName, 'A');
    expect(controller.current.locale, 'it');
    expect(controller.current.theme, ProfileTheme.dark);
    expect(store.writes, 3);
  });

  test('legacy version zero migrates in memory, never writes implicitly', () async {
    final store = MemoryStore()
      ..document = jsonEncode({
        'schema_version': 0,
        'name': 'Marco',
        'language': 'it',
        'theme': 'light',
      });
    final controller = ProfileSettingsController(store);
    expect((await controller.load()).displayName, 'Marco');
    expect(store.writes, 0);
    await controller.update((p) => p.copyWith(locale: 'en'));
    expect(jsonDecode(store.document!)['schema_version'], 1);
  });

  test('corrupt preferences remain intact and are not automatically erased', () async {
    final store = MemoryStore()..document = '{corrupt';
    final controller = ProfileSettingsController(store);
    await controller.load();
    expect(controller.recoveredFromInvalidPreferences, isTrue);
    expect(store.document, '{corrupt');
    expect(store.writes, 0);
  });

  test('oversized stored profile is not decoded, erased, or rewritten', () async {
    final original = jsonEncode({'schema_version': 1, 'display_name': List.filled(20000, 'x').join()});
    final store = MemoryStore()..document = original;
    final controller = ProfileSettingsController(store);
    expect((await controller.load()).displayName, '');
    expect(controller.recoveredFromInvalidPreferences, isTrue);
    expect(store.document, original);
    expect(store.writes, 0);
  });

  test('future schema and unknown locale do not get silently migrated', () {
    expect(
      () => ProfilePreferences.fromJson({'schema_version': 2}),
      throwsFormatException,
    );
    expect(
      () => const ProfilePreferences(locale: 'xx').toJson(),
      throwsFormatException,
    );
  });

  test('profile JSON never contains OAuth token or account credentials', () {
    final exported = const ProfilePreferences(displayName: 'Me').toJson();
    expect(exported.keys, isNot(contains('token')));
    expect(exported.keys, isNot(contains('email')));
    expect(exported.keys, isNot(contains('password')));
    expect(exported['analytics_opt_in'], isFalse);
  });

  test('explicit privacy opt-in persists but is not triggered by settings load', () async {
    final store = MemoryStore();
    final controller = ProfileSettingsController(store);
    await controller.load();
    expect(store.writes, 0);
    await controller.update((p) => p.copyWith(analyticsOptIn: true));
    expect(jsonDecode(store.document!)['analytics_opt_in'], isTrue);
  });

  test('unsupported theme and invalid consent type fail closed', () {
    expect(
      () => ProfilePreferences.fromJson({
        'schema_version': 1,
        'theme': 'neon',
      }),
      throwsFormatException,
    );
    expect(
      () => ProfilePreferences.fromJson({
        'schema_version': 1,
        'analytics_opt_in': 'true',
      }),
      throwsFormatException,
    );
  });
}
