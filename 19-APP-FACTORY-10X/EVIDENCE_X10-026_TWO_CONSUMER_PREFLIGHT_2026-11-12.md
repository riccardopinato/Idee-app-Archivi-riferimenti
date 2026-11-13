# X10-026 — Due consumer Flutter: intake e gap reali (NON certificato)

> **Aggiornamento 13/11/2026:** preflight storico; il test reale sui due consumer è stato eseguito con esito positivo in [AppLab #231](EVIDENCE_X10-026_REAL_CONSUMERS_2026-11-13.md), ma manca il rollback **semver** richiesto da X10-018. X10-026 rimane PLANNED; non usare le righe preflight qui sotto come stato corrente.

Baseline Factory: [App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619](https://github.com/riccardopinato/App-Factory-Core/commit/c5adc147046beb7024629466d10eeb799c3c2619), Master 27, Golden Index 29.

## SOURCE CHECKED at 12 Nov 2026

| Consumer | GitHub source SHA | Flutter/AppLab config | Existing consumer CI signal | Factory kits already installed? |
| --- | --- | --- | --- | --- |
| [Anna's Diary](https://github.com/riccardopinato/Agenda-per-Anna) | `8fbfe14f7a21d41af274cf259c462df2eab9dc69` | `applab.project.json`: Flutter 3.47.5, Java 17, `com.riccardopinato.agenda_per_anna`; `pubspec.yaml`: `agenda_per_anna 1.0.0-rc.6+129`, SDK >=3.10.0 | [Development checks on main](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43018701168) SUCCESS; [auto signed ARM64 RC](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43019458528) SUCCESS | **No** `factory_*_kit` dependencies in pinned `pubspec.yaml` |
| [CamperBoss](https://github.com/riccardopinato/CamperBoss) | `fe3b10d435e120cc952a90cd6bc06c66b6b2521a` | Flutter 3.47.6, Java 21, `com.camperboss.camperboss`; `pubspec.yaml`: `camperboss 0.2.2+18`, SDK >=3.4.0 | [Flutter CI on main](https://github.com/riccardopinato/CamperBoss/actions/runs/43023616125) SUCCESS; [AppLab Production Gate prior PR head](https://github.com/riccardopinato/CamperBoss/actions/runs/43017408936) SUCCESS | **No** `factory_*_kit` dependencies in pinned `pubspec.yaml` |

**Scope:** Actual GitHub source metadata and observed workflow run status, not proof that factory kits were integrated or that any new tests were run. The successful production gate is for a prior CamperBoss PR head, not certification of the pinned present main with these new kits. The observed context-snapshot schedule workflows on 12 Nov failed independently (Anna run 43255419421, CamperBoss run 43225906512); do not hide these unrelated outstanding issues.

## Canonical kit source and contract

- [X10-025 composition v0.1.0](flutter_kits/composition/README.md) combines profile, identity, backup and notifications **as pure Dart**, local path dependencies in the archive; no real Flutter/Android consumer integration.
- [AppLab X10-018 compatibility harness](https://github.com/riccardopinato/AppLab/blob/db263d48cf1dbdaf85933e3c044dd5d9ccbf7559/scripts/golden_compat_harness_x10.py) already requires version-pinned donor/consumer/rollback receipts and SDK matrix. Reuse this, do **not** add another compatibility engine.
- Minimum consumer pairing must cover profile and safe export/backup. Login/OAuth, native notifications and monetization remain excluded until product/provider/native gates are independently approved. Do not modify user data or use destructive migrations.

## Real execution gates to complete X10-026

1. Decide **one** bounded, low-risk kit/adaptation for both consumers; separately review each Product Bible and affected existing architecture. Existing profile/backup implementations must be extended or left unchanged, not duplicated.
2. Choose a reusable package distribution/adoption mechanism (current archive packages have sibling-local path dependencies and are not published). Pin immutable kit version and provider compatibility for Flutter 3.47.5/3.47.6, JDK 17/21 and their own SDK declarations, without blindly lowering requirements.
3. Create **separate consumer PRs** with staged changes and rollback instructions. Preserve Anna's Diary private/offline data and CamperBoss GPS/background permissions.
4. Run real Dart/Flutter tests, source CI and AppLab appropriate FAST/FULL on each exact consumer SHA, then run relevant real device tests for provider/native features. Capture same-bytes evidence.
5. Use existing X10-018 harness with **1 donor + both consumer receipts + tested SDK pairs + 1 rollback receipt**; verify actual CI run URLs and rollback independently. Exact-head Codex/review before any merges.
6. Only then request Golden admission; passing structural harness alone returns `STRUCTURAL_PASS_REVIEW_REQUIRED` and **does not** certify a Golden.

**Status:** X10-026 remains `PLANNED / REAL_CONSUMER_INTEGRATION_NOT_VERIFIED`. This dossier is a verified-source *preflight*, not X10-026 acceptance or product authorization.
