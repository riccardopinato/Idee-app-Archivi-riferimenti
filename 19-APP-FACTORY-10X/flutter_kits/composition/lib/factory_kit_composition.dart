/// X10-025: cross-kit dependency chooser. A source dependency is NOT
/// provider activation, product owner approval or physical device proof.
enum TargetPlatform { android, ios, web }

enum KitFeature { profile, identity, backup, notifications, monetization }

const sourcePackages = <KitFeature, String>{
  KitFeature.profile: 'factory_profile_kit',
  KitFeature.identity: 'factory_identity_kit',
  KitFeature.backup: 'factory_backup_kit',
  KitFeature.notifications: 'factory_notification_kit',
};

const _reviewGates = <KitFeature, List<String>>{
  KitFeature.profile: [
    'CONSUMER_OWNER_SCOPED_ATOMIC_STORE_REQUIRED',
    'LOCALIZATION_AND_UI_CONSUMER_TESTS_REQUIRED',
  ],
  KitFeature.identity: [
    'PRODUCT_IDENTITY_OPTIONAL_BY_DEFAULT',
    'INDEPENDENT_OAUTH_PKCE_AND_CLAIM_VERIFIER_REQUIRED',
    'ACCOUNT_PARTITION_SWITCH_TEST_REQUIRED',
    'PROVIDER_FRESHNESS_REVIEW_REQUIRED',
  ],
  KitFeature.backup: [
    'BACKUP_GOLDEN_CANDIDATE_NOT_COPY_READY',
    'TRANSACTIONAL_DOMAIN_AND_MEDIA_PORT_REQUIRED',
    'CONSUMER_DATA_LOSS_AND_CRASH_TEST_REQUIRED',
  ],
  KitFeature.notifications: [
    'NATIVE_PERMISSION_CHANNEL_TIMEZONE_ADAPTER_REQUIRED',
    'DEVICE_DELIVERY_AND_REBOOT_TEST_REQUIRED',
    'PROVIDER_FRESHNESS_REVIEW_REQUIRED',
  ],
};

class KitAssemblyRequest {
  KitAssemblyRequest({
    required this.target,
    required Set<KitFeature> requested,
    this.productBibleReviewed = false,
  }) : requested = Set<KitFeature>.unmodifiable(requested);

  final TargetPlatform target;
  final Set<KitFeature> requested;

  /// Declarative owner input, NOT a verified human approval receipt.
  final bool productBibleReviewed;
}

class KitSelection {
  const KitSelection({
    required this.feature,
    required this.sourcePackage,
    required this.requiredGates,
  });

  final KitFeature feature;
  final String sourcePackage;
  final List<String> requiredGates;
}

class AssemblyProposal {
  const AssemblyProposal({
    required this.selections,
    required this.refused,
    required this.globalGates,
  });

  final List<KitSelection> selections;
  final Map<KitFeature, String> refused;
  final List<String> globalGates;

  /// The chooser never grants operational permissions or edits app projects.
  bool get runtimeEnabled => false;
  bool get productionReady => false;
  bool get consumerCodeModified => false;
  bool get providerConfigured => false;
  bool get goldenPromoted => false;
  bool get releaseApproved => false;
}

class KitDependencyChooser {
  const KitDependencyChooser();

  AssemblyProposal propose(KitAssemblyRequest request) {
    final selected = <KitSelection>[];
    final refused = <KitFeature, String>{};
    final global = <String>['PRODUCT_BIBLE_AND_PLATFORM_DELTA_REVIEW_REQUIRED'];
    if (!request.productBibleReviewed) {
      global.add('PRODUCT_BIBLE_NOT_REVIEWED');
    }
    for (final feature in KitFeature.values) {
      if (!request.requested.contains(feature)) continue;
      if (feature == KitFeature.monetization) {
        refused[feature] = 'HUMAN_BILLING_ADMOB_STORE_GATE_REQUIRED';
        continue;
      }
      if (feature == KitFeature.notifications && request.target == TargetPlatform.web) {
        refused[feature] = 'NATIVE_NOTIFICATION_PROVIDER_NOT_SUPPORTED_ON_WEB';
        continue;
      }
      final name = sourcePackages[feature];
      final gates = _reviewGates[feature];
      if (name == null || gates == null) {
        refused[feature] = 'MODULE_UNREGISTERED';
        continue;
      }
      selected.add(KitSelection(
        feature: feature,
        sourcePackage: name,
        requiredGates: List<String>.unmodifiable(gates),
      ));
    }
    return AssemblyProposal(
      selections: List<KitSelection>.unmodifiable(selected),
      refused: Map<KitFeature, String>.unmodifiable(refused),
      globalGates: List<String>.unmodifiable(global),
    );
  }
}
