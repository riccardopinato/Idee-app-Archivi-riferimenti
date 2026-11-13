import 'package:factory_monetization_policy/factory_monetization_policy.dart';
import 'package:test/test.dart';

void main() {
  final now = DateTime.utc(2026, 11, 13);
  const free = FactoryEntitlement();

  test('default free and provider unknown never grants paid access or ads', () {
    expect(free.hasPaidAccess(now), isFalse);
    expect(const FactoryAdRequestPolicy().mayRequestAds(free, now), isFalse);
  });
  test('verified premium works until expiry', () {
    final snapshot = FactoryEntitlement(
      plan: FactoryPlan.premium, source: FactoryEntitlementSource.providerVerified,
      verifiedAtUtc: now.subtract(const Duration(days: 2)),
      expiresAtUtc: now.add(const Duration(days: 1)));
    expect(snapshot.hasPaidAccess(now), isTrue);
    expect(snapshot.hasPaidAccess(now.add(const Duration(days: 1))), isFalse);
  });
  test('lifetime requires verification but not recurring expiry', () {
    final snapshot = FactoryEntitlement(
      plan: FactoryPlan.lifetime, source: FactoryEntitlementSource.providerVerified,
      verifiedAtUtc: now);
    expect(snapshot.hasPaidAccess(now.add(const Duration(days: 365))), isTrue);
  });
  test('offline grace cannot silently be permanent', () {
    final snapshot = FactoryEntitlement(
      plan: FactoryPlan.premium, source: FactoryEntitlementSource.offlineCache,
      verifiedAtUtc: now.subtract(const Duration(days: 6)),
      expiresAtUtc: now.subtract(const Duration(days: 1)),
      offlineGraceUntilUtc: now.add(const Duration(hours: 5)));
    expect(snapshot.hasPaidAccess(now), isTrue);
    expect(snapshot.hasPaidAccess(now.add(const Duration(hours: 5))), isFalse);
    expect(const FactoryEntitlement(plan: FactoryPlan.premium,
      source: FactoryEntitlementSource.offlineCache).hasPaidAccess(now), isFalse);
  });
  test('future-dated provider receipts fail closed', () {
    final future = FactoryEntitlement(plan: FactoryPlan.lifetime,
      source: FactoryEntitlementSource.providerVerified,
      verifiedAtUtc: now.add(const Duration(minutes: 1)));
    expect(future.hasPaidAccess(now), isFalse);
  });
  test('qa override cannot grant in release', () {
    const qa = FactoryEntitlement(plan: FactoryPlan.lifetime,
      source: FactoryEntitlementSource.qaOverride);
    expect(qa.hasPaidAccess(now), isFalse);
    expect(qa.hasPaidAccess(now, qaOverrideAllowed: true), isTrue);
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: true,
      usesTestAdUnits: false).mayRequestAds(qa, now), isTrue);
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: false,
      usesTestAdUnits: true).mayRequestAds(qa, now), isFalse);
  });
  test('ad requests require owner placement and provider consent', () {
    expect(const FactoryAdRequestPolicy(
      providerMayRequestAds: true, usesTestAdUnits: true).mayRequestAds(free, now),
      isFalse);
    expect(const FactoryAdRequestPolicy(
      ownerApprovedPlacement: true).mayRequestAds(free, now), isFalse);
  });
  test('real release cannot request sample test ads, debug cannot use live ads', () {
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: true,
      usesTestAdUnits: true).mayRequestAds(free, now), isFalse);
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: false,
      usesTestAdUnits: false).mayRequestAds(free, now), isFalse);
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: false,
      usesTestAdUnits: true).mayRequestAds(free, now), isTrue);
  });
  test('verified premium suppresses ads before any SDK request', () {
    final paid = FactoryEntitlement(plan: FactoryPlan.premium,
      source: FactoryEntitlementSource.providerVerified,
      verifiedAtUtc: now);
    expect(const FactoryAdRequestPolicy(ownerApprovedPlacement: true,
      providerMayRequestAds: true, isReleaseBuild: true,
      usesTestAdUnits: false).mayRequestAds(paid, now), isFalse);
  });
}
