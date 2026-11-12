/// X10-036 — local opt-in, in-memory aggregate event gate.
/// No device ID, user identity, network, persistent storage or SDK is included.
/// A true retention cohort and attribution need separate user-reviewed designs.
enum PrivacyMetric {
  appOpen,
  featureOpen,
  valueAction,
  paywallView,
  purchaseCompleted,
}

class MetricSnapshot {
  MetricSnapshot({
    required this.counts,
    required this.consentGranted,
    required this.releasable,
  });
  final Map<PrivacyMetric, int> counts;
  final bool consentGranted;
  final bool releasable;
  bool get containsUserIdentifiers => false;
  bool get isRuntimeCertification => false;
}

class OptInAggregateMetrics {
  OptInAggregateMetrics({this.minCohort = 5})
      : assert(minCohort >= 2 && minCohort <= 1000);

  final int minCohort;
  final Map<PrivacyMetric, int> _counts = {};
  bool _consent = false;
  int _eligibleSessions = 0;

  bool get enabled => _consent;
  int get eligibleSessions => _eligibleSessions;

  /// Requires independent consent from the host; never assumes UI consent.
  void setConsent({required bool granted}) {
    if (!_consent && granted) {
      _consent = true;
      return;
    }
    if (!granted) {
      _consent = false;
      _counts.clear();
      _eligibleSessions = 0;
    }
  }

  /// Only an explicit caller declaration of a consented session increments
  /// the cohort. This is not a user retention or unique-user measurement.
  void beginConsentedSession() {
    if (!_consent) return;
    _eligibleSessions += 1;
  }

  void record(PrivacyMetric event) {
    if (!_consent) return;
    _counts[event] = (_counts[event] ?? 0) + 1;
  }

  /// Fail closed: until at least [minCohort] *consented sessions* exist,
  /// no metrics can leave the private process; no persistent state.
  MetricSnapshot snapshot() {
    final releasable = _consent && _eligibleSessions >= minCohort;
    return MetricSnapshot(
      counts: Map<PrivacyMetric, int>.unmodifiable(
        releasable ? Map.of(_counts) : <PrivacyMetric, int>{},
      ),
      consentGranted: _consent,
      releasable: releasable,
    );
  }

  void erase() {
    _consent = false;
    _counts.clear();
    _eligibleSessions = 0;
  }
}
