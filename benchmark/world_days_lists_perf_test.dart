// Temporary CI widget benchmark. Copied into World-Days checkout; app source unchanged.
// It measures widget-test pump wall time, NOT device GPU frame times, jank or RAM.
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'package:world_days/app/app_controller.dart';
import 'package:world_days/data/catalog_repository.dart';
import 'package:world_days/data/preferences_repository.dart';
import 'package:world_days/domain/observance.dart';
import 'package:world_days/features/saved/saved_page.dart';
import 'package:world_days/features/discover/around_the_world_page.dart';
import 'package:world_days/core/widgets/observance_card.dart';
import 'package:world_days/l10n/app_localizations.dart';

import '../support/world_days_test_support.dart';

const _authority = ObservanceAuthority(
  name: 'Benchmark authority',
  type: 'TEST',
  officiality: 'OFFICIAL_INSTITUTIONAL',
);
const _source = ObservanceSource(
  tier: 'TEST',
  url: 'https://example.com/benchmark',
  verifiedAt: '2026-11-09',
);

AppController _createFixture(int count) {
  final records = List<Observance>.generate(
    count,
    (i) => Observance(
      id: 'benchmark-$i',
      title: 'Benchmark observance number $i',
      periodKind: 'DAY',
      scope: 'NATIONAL',
      countries: const ['IT'],
      regions: const [],
      authority: _authority,
      sources: const [_source],
      rules: const [],
      aliases: const [],
      categories: const ['LEARNING'],
      visualKey: 'learning',
      lastVerifiedAt: '2026-11-09',
    ),
    growable: false,
  );
  final controller = AppController(
    notificationService: FakeNotificationGateway(),
    homeWidgetService: FakeHomeWidgetGateway(),
    entitlementService: buildTestEntitlementService(),
    contentPackManager: buildTestContentPackManager(),
  );
  controller.catalog = CatalogSnapshot(
    records: records,
    byId: {for (final item in records) item.id: item},
    occurrences2026: const [],
    editorialByLocale: const {
      'en': {}, 'it': {}, 'es': {}, 'fr': {}, 'de': {}, 'pt': {},
    },
    yearOverrides: const [],
    datasetVersion: 'benchmark',
  );
  controller.preferences = UserPreferences(
    favoriteIds: {for (final item in records) item.id},
    marketCode: 'IT',
  );
  return controller;
}

Widget _appFor(String page, AppController controller) => MaterialApp(
  debugShowCheckedModeBanner: false,
  locale: const Locale('it'),
  supportedLocales: AppLocalizations.supportedLocales,
  localizationsDelegates: const [
    AppLocalizations.delegate,
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  home: page == 'saved'
      ? SavedPage(controller: controller)
      : AroundTheWorldPage(controller: controller),
);

double _roundMs(int microseconds) =>
    (microseconds / 1000 * 1000).round() / 1000;

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('UI audit: Italy country picker overflows at 390 px',
      (tester) async {
    await tester.binding.setSurfaceSize(const Size(390, 844));
    addTearDown(() => tester.binding.setSurfaceSize(null));
    final controller = _createFixture(10);
    addTearDown(controller.dispose);
    await tester.pumpWidget(_appFor('around_the_world', controller));
    final issues = <Object>[];
    while (true) {
      final issue = tester.takeException();
      if (issue == null) break;
      issues.add(issue);
    }
    final overflow = issues.any((issue) =>
        issue.toString().contains('RenderFlex overflowed'));
    print('WORLD_DAYS_UI_AUDIT|' + jsonEncode({
      'page': 'around_the_world',
      'viewport_logical_px': '390x844',
      'locale': 'it',
      'renderflex_overflow_detected': overflow,
      'exception_count': issues.length,
      'widget_location': 'lib/features/discover/around_the_world_page.dart:57',
      'source_sha': const String.fromEnvironment('WD_SOURCE_SHA',
          defaultValue: 'unknown'),
    }));
    expect(overflow, isTrue,
        reason: 'The existing 390px overflow must be recorded, not ignored.');
  });

  for (final page in ['saved', 'around_the_world']) {
    for (final count in [10, 50, 150, 300]) {
      testWidgets('widget-pump benchmark $page N=$count', (tester) async {
        await tester.binding.setSurfaceSize(const Size(480, 844));
        addTearDown(() => tester.binding.setSurfaceSize(null));
        final controller = _createFixture(count);
        addTearDown(controller.dispose);

        final samples = <int>[];
        int? totalWidgetChildren;
        int? mountedCards;
        // Warmup first 2 rebuilds; measure 7 fresh mounts.
        for (var i = 0; i < 9; i++) {
          await tester.pumpWidget(const SizedBox.shrink());
          final watch = Stopwatch()..start();
          await tester.pumpWidget(_appFor(page, controller));
          await tester.pump();
          watch.stop();

          final view = tester.widget<ListView>(find.byType(ListView).first);
          totalWidgetChildren = view.childrenDelegate.estimatedChildCount;
          mountedCards = find.byType(ObservanceCard).evaluate().length;
          if (i >= 2) samples.add(watch.elapsedMicroseconds);
        }

        expect(totalWidgetChildren, greaterThanOrEqualTo(count));
        samples.sort();
        final median = samples[samples.length ~/ 2];
        final p95 = samples[(samples.length * .95).ceil() - 1];
        print('WORLD_DAYS_BENCH|' + jsonEncode({
          'page': page,
          'scenario_record_count': count,
          'viewport_logical_px': '480x844',
          'metric': 'flutter_widget_test_pump_wall_clock_not_device_frame',
          'warmups': 2,
          'samples': samples.length,
          'sample_ms_sorted': samples.map(_roundMs).toList(),
          'median_pump_ms': _roundMs(median),
          'p95_pump_ms': _roundMs(p95),
          'list_delegate_total_children': totalWidgetChildren,
          'mounted_visible_observance_cards': mountedCards,
          'source_sha': const String.fromEnvironment('WD_SOURCE_SHA',
              defaultValue: 'unknown'),
        }));
      }, timeout: const Timeout(Duration(minutes: 5)));
    }
  }
}
