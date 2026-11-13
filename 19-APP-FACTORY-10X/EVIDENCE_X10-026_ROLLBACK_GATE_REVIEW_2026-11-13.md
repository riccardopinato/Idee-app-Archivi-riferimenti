# X10-026 — Verifica gate rollback X10-018 (13 novembre 2026)

**Decisione del controllo: PARTIAL SOURCE+CI VERIFIED; X10-018 SEMVER ROLLBACK NOT VERIFIED; X10-026 remains PLANNED.**

## Provenienza e baseline

- Factory baseline `riccardopinato/App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` (Master 27, Golden Index 29).
- Kit `factory_profile_kit@0.1.0` da `riccardopinato/Idee-app-Archivi-riferimenti@1d1a8628e25f58b788b013cf6955763d00363cdc`.
- Consumer A `riccardopinato/Agenda-per-Anna@984a34462ba527b2ea98dbc3a337bdd8614b88d4`.
- Consumer B `riccardopinato/TasteAI@61a83aa638654f4e885d503e024408d2dcddebc2`.
- AppLab source verifier `d1ec6f94198b0ef9ddd2e520ec39b71df6887e23`, PR [#231](https://github.com/riccardopinato/AppLab/pull/231).
- AppLab **post-merge exact-main** source regression + pre-adoption source rollback: [run 43332484371](https://github.com/riccardopinato/AppLab/actions/runs/43332484371), job `131580345353`, SUCCESS. All steps including donor Dart tests, Anna/TasteAI Flutter regression and historical source worktree tests returned SUCCESS.
- Post-merge [AppLab CI 43332484298](https://github.com/riccardopinato/AppLab/actions/runs/43332484298) and [CodeQL 43332484283](https://github.com/riccardopinato/AppLab/actions/runs/43332484283): SUCCESS on `d1ec6f9`.
- [TasteAI Flutter CI 43330930127](https://github.com/riccardopinato/TasteAI/actions/runs/43330930127): SUCCESS on `61a83aa`. PR [TasteAI #7](https://github.com/riccardopinato/TasteAI/pull/7) fixed Flutter 3.47.5 pinning.
- PR #231 Codex review completed on source head `f2a70d1ce7eb96a34f3077fbc40a696e3e8061a9`, without reported major findings.

## X10-018 compatibility assessment

The active AppLab [X10-018 harness](https://github.com/riccardopinato/AppLab/blob/d1ec6f94198b0ef9ddd2e520ec39b71df6887e23/scripts/golden_compat_harness_x10.py) requires one authentic `ROLLBACK` receipt with:
- `from_version` equal to the pinned package version (`0.1.0`);
- `to_version` equal to the declared `release.rollback_version`, a real SemVer lower than `0.1.0`;
- pinned donor SHA, actual PASS run URL and matching Dart/Flutter SDK pair;
- independent validation that the referenced run truly executed the relevant test.

No lower real published/retrievable `factory_profile_kit` version with a package-version rollback test has been identified in the reviewed evidence. In particular **do not fabricate `0.0.0`**, downgrade source checkouts as if they were package versions, or fabricate synthetic `ROLLBACK` receipts. Merely creating a new number without real compatible source and a tested rollback does not close X10-018.

The existing X10-026 workflow establishes a **pre-adoption source rollback rehearsal** to Anna `8fbfe14f7a21d41af274cf259c462df2eab9dc69` and TasteAI `8e880be68d74686c6c6b7e6a992a5fdc6fa6c384`. This is **not** a versioned rollback of `factory_profile_kit` from `0.1.0` to an earlier version.

## Remaining acceptance sequence (no bypass)

1. Prepare a **genuine new package version** in a separately scoped, reviewed package PR (or identify a genuine compatible prior version); confirm the complete version lineage, licenses, immutable donor SHA, package dependencies and support matrix. No unnecessary new product feature or release.
2. On real immutable package sources, execute package-version upgrade and downgrade tests with at least the two approved consumers, preserving their existing preference/restore invariants. Record an authentic X10-018 `ROLLBACK` receipt, exact runner/source identity, CI URL and tested Dart/Flutter versions.
3. Run the unmodified X10-018 harness against a correctly pinned package manifest and real donor, consumer and rollback receipts; inspect CI logs independently. `STRUCTURAL_PASS_REVIEW_REQUIRED` alone cannot authorize certification.
4. Update this evidence dossier, reconcile `PROGRAM_QUEUE.json` and changelog through branch/PR/exact-head CI and review. Only promote X10-026 to `VERIFIED` after its actual **package-version rollback** and both consumer acceptance gates pass.
5. Golden admission is a **separate** process. Physical APK upgrade/downgrade, persisted device data and Play Store evidence remain `NOT_VERIFIED`, not inherited from source-level tests.

## Decision

**Do not promote X10-026**. This record upgrades auditability and post-merge CI provenance only; it does not revise X10-018 criteria, create a package release, modify consumer data or approve a Golden.
