import 'package:test/test.dart';
import 'package:factory_privacy_metrics_kit/factory_privacy_metrics_kit.dart';

void main() {
  test('default state denies all observations', () {
    final metrics = OptInAggregateMetrics();
    metrics.record(PrivacyMetric.appOpen);
    metrics.beginConsentedSession();
    expect(metrics.snapshot().counts, isEmpty);
    expect(metrics.snapshot().releasable, isFalse);
  });

  test('consent allows local collection but blocks below session threshold', () {
    final metrics = OptInAggregateMetrics();
    metrics.setConsent(granted: true);
    for (var i = 0; i < 4; i++) {
      metrics.beginConsentedSession();
      metrics.record(PrivacyMetric.appOpen);
    }
    expect(metrics.snapshot().counts, isEmpty);
    expect(metrics.snapshot().releasable, isFalse);
    metrics.beginConsentedSession();
    metrics.record(PrivacyMetric.featureOpen);
    final snapshot = metrics.snapshot();
    expect(snapshot.releasable, isTrue);
    expect(snapshot.counts[PrivacyMetric.appOpen], 4);
    expect(snapshot.counts[PrivacyMetric.featureOpen], 1);
    expect(snapshot.containsUserIdentifiers, isFalse);
    expect(snapshot.isRuntimeCertification, isFalse);
    expect(() => snapshot.counts[PrivacyMetric.appOpen] = 999, throwsUnsupportedError);
  });

  test('revoke irreversibly clears unpersisted totals', () {
    final metrics = OptInAggregateMetrics();
    metrics.setConsent(granted: true);
    for (var i = 0; i < 6; i++) {
      metrics.beginConsentedSession();
      metrics.record(PrivacyMetric.valueAction);
    }
    expect(metrics.snapshot().releasable, isTrue);
    metrics.setConsent(granted: false);
    expect(metrics.enabled, isFalse);
    expect(metrics.snapshot().counts, isEmpty);
    metrics.setConsent(granted: true);
    expect(metrics.snapshot().counts, isEmpty);
    expect(metrics.snapshot().releasable, isFalse);
  });

  test('erase also clears consent state', () {
    final metrics = OptInAggregateMetrics();
    metrics.setConsent(granted: true);
    metrics.beginConsentedSession();
    metrics.record(PrivacyMetric.purchaseCompleted);
    metrics.erase();
    expect(metrics.enabled, isFalse);
    expect(metrics.eligibleSessions, 0);
    expect(metrics.snapshot().counts, isEmpty);
  });

  test('only a fixed event vocabulary can be recorded', () {
    expect(PrivacyMetric.values.length, 5);
    final result = OptInAggregateMetrics().snapshot();
    expect(result.counts, isEmpty);
  });
}
