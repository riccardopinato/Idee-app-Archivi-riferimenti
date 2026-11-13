/// Pure decision policy; never authorizes billing, loads ads or verifies a store receipt.
/// App provider adapters own actual purchase/consent validation.
enum FactoryPlan { free, premium, lifetime }

enum FactoryEntitlementSource { unknown, providerVerified, offlineCache, qaOverride }

class FactoryEntitlement {
  const FactoryEntitlement({
    this.plan = FactoryPlan.free,
    this.source = FactoryEntitlementSource.unknown,
    this.verifiedAtUtc,
    this.expiresAtUtc,
    this.offlineGraceUntilUtc,
  });

  final FactoryPlan plan;
  final FactoryEntitlementSource source;
  final DateTime? verifiedAtUtc;
  final DateTime? expiresAtUtc;
  final DateTime? offlineGraceUntilUtc;

  /// Fail closed on unknown, expired or future verification timestamps.
  /// QA entitlement is usable only in explicitly marked non-release tests.
  bool hasPaidAccess(DateTime nowUtc, {bool qaOverrideAllowed = false}) {
    if (plan == FactoryPlan.free) return false;
    final now = nowUtc.toUtc();
    if (source == FactoryEntitlementSource.qaOverride) return qaOverrideAllowed;
    if (source == FactoryEntitlementSource.unknown ||
        verifiedAtUtc == null || verifiedAtUtc!.isAfter(now)) return false;
    if (source == FactoryEntitlementSource.offlineCache &&
        (offlineGraceUntilUtc == null ||
         !now.isBefore(offlineGraceUntilUtc!.toUtc()))) return false;
    if (expiresAtUtc != null && !now.isBefore(expiresAtUtc!.toUtc())) {
      return source == FactoryEntitlementSource.offlineCache &&
          offlineGraceUntilUtc != null &&
          now.isBefore(offlineGraceUntilUtc!.toUtc());
    }
    return true;
  }
}

class FactoryAdRequestPolicy {
  const FactoryAdRequestPolicy({
    this.ownerApprovedPlacement = false,
    this.providerMayRequestAds = false,
    this.isReleaseBuild = false,
    this.usesTestAdUnits = true,
  });

  final bool ownerApprovedPlacement;
  /// Result of the real provider's consent gate (e.g. UMP canRequestAds()).
  final bool providerMayRequestAds;
  final bool isReleaseBuild;
  final bool usesTestAdUnits;

  /// A real production request is impossible unless explicitly approved,
  /// provider consent is affirmative and the build uses non-test units.
  /// A preview request is only permitted with test ad units.
  bool mayRequestAds(FactoryEntitlement entitlement, DateTime nowUtc) {
    if (!ownerApprovedPlacement || !providerMayRequestAds) return false;
    if (entitlement.hasPaidAccess(nowUtc, qaOverrideAllowed: !isReleaseBuild)) {
      return false;
    }
    return isReleaseBuild ? !usesTestAdUnits : usesTestAdUnits;
  }
}
