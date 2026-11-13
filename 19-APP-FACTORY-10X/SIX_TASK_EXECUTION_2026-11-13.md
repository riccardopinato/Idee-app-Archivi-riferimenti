# App Factory 10x — six-task gated execution, 13 November 2026

**X10-026 FINAL SCOPED ACCEPTANCE:** Real versioned Dart source-package rollback `0.1.1 → 0.1.0` and two consumer integrations are **VERIFIED SOURCE+CI**, following independently green exact-head reviews and post-merge CI on AppLab `bb59e05`, Anna `ffa3d98` and TasteAI `2e6cb12`. Original sections below preserve the historical pre-merge gate sequence. This is NOT Golden certification, Android installed APK/device user-data rollback, or Play testing. Canonical queue: 35 VERIFIED / 21 PLANNED / 1 BLOCKED.

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` (Master v27; Golden Index v29). This evidence dossier is not a release decision, does not promote any Golden and does not grant spending/Store or device authority.

## X10-026 — Two real Flutter consumer integrations with genuine SemVer rollback

- **Donor 0.1.0:** `riccardopinato/Idee-app-Archivi-riferimenti@1d1a8628e25f58b788b013cf6955763d00363cdc`.
- **Donor 0.1.1:** `riccardopinato/Idee-app-Archivi-riferimenti@710e83261bcadc1cfd5eda3e28d77bed8b8bc576`. Genuine non-destructive corrupted-profile guard; no invented `0.0.0`.
- **AppLab:** [PR #232](https://github.com/riccardopinato/AppLab/pull/232) merged `bb59e05dea0e0aace1128cf965fa1a2ae7ab8ab7` after 0.1.0 → 0.1.1 → 0.1.0 source-package version regression on both consumer source trees; exact-head [CI #43337856699](https://github.com/riccardopinato/AppLab/actions/runs/43337856699) success (donor tests, Anna/Taste tests before/after, lockfile restore). X10-018 unmodified harness reports `STRUCTURAL_PASS_REVIEW_REQUIRED` with real log execution, counts `DONOR=1, CONSUMER=2, ROLLBACK=1`; independent Codex review exact-head clean. Evidence [artifact #13997144592](https://github.com/riccardopinato/AppLab/actions/runs/43337856699) digest `sha256:ec07934d8090d6630ca80a89c2cc903708f1b0fb4a0ff58ad6b25bb7b8717c45` (metadata, **not** a phone APK).
- **Anna's Diary:** [PR #310](https://github.com/riccardopinato/Agenda-per-Anna/pull/310) merged `ffa3d98c21b6f04c8d5fe904e930cff003c6aa31`; pins 0.1.1 in `pubspec.yaml` and `pubspec.lock`, no canonical store change.
- **TasteAI:** [PR #9](https://github.com/riccardopinato/TasteAI/pull/9) merged `2e6cb127a081365efe565d5f0b8ad1435c2fe4ba`; same pinned 0.1.1 dependency, no settings store change.
- **Trust boundary:** GitHub run logs were inspected independently, and exact PR-head reviews/checks were green before merge. Post-merge `main` CI **must independently complete** before queue promotion is decided; source-package downgrade is **not** an Android installed APK downgrade or persisted device-data upgrade. The structural harness is not an independent receipt certifier and does not authorize automatic Golden admission.

## X10-023 — Notification native bridge

- Existing native integration test in [PR #155](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/155), [API29 run #43336767350 attempt 2](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/43336767350/attempts/2) **PASS** after fixing UTC location handling. It tests Android native plugin channel, inexact schedule pending state and cancel, not delivery.
- #155 was closed **unmerged** due a concurrent documentation conflict; [replacement PR #160](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/160) carries the fix/fixture on current main. **PR #160 exact-head checks/review required** before its merge. No actual OEM, Doze/reboot, FCM or receiving app certificate. **X10-023 PLANNED** (source gate only).

## X10-024 — Provider-neutral modular monetization

- [PR #159](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/159) merged `2a461505d610e15b8f58ba24af4627d575e253ed`, with independent source CI and Codex review on its exact head. The pure Dart kit has no AdMob, RevenueCat, Play Billing or network.
- Covers entitlement, provider-verified Premium/Lifetime, missing expiration fail-closed, bounded offline grace, QA isolation, consent and product placement gate, test/live ad-unit segregation. No production ad request or purchase is initiated.
- **X10-024 PLANNED / HUMAN_GATE** until owner explicitly approves product-level monetization and actual AdMob UMP / provider / Play sandbox / device QA are independently verified. Technical SOURCE+CI candidate is not billing certification.

## X10-032 — Physical QA and Play Internal Testing

- [Canonical AppLab X10-032 handoff](https://github.com/riccardopinato/AppLab/blob/main/integration/agent_core/X10-032_PHYSICAL_PLAY_HANDOFF.md) supplies source-only deterministic plan and native scenario matrix. Its statuses remain `PLAN_ONLY / NOT_VERIFIED`.
- A confirmed GitHub build run alone is not same-bytes/physical proof: require final APK/AAB artifact SHA256, signer fingerprint, source SHA, versionCode + previous versionCode, actual device models/OS and observable install/upgrade/no-data-loss/reboot results, verified by `scripts/physical_evidence.py` and genuine Google Play Internal Testing receipt.
- No suitably complete **verified** physical/Play evidence was available during this source-only round. **X10-032 remains PLANNED / HUMAN_GATE**; do not synthesize an APK hash or call a simulated emulator a phone.

## X10-035 — 2–3 product commercial decision

- The latest canonical [commercial comparison](X10-035_PORTFOLIO_COMMERCIAL_COMPARISON_2026-11-12.md) and [owner decision proposal](X10-035_OWNER_DECISION_PROPOSAL.json) shortlist `180FlipCharge`, `Android-Omni-Cleaner`, `Battery_Guard`, with `World-Days` conditional.
- Owner confirmed a **100 EUR maximum ceiling only**: currently **0 EUR expenditure authorized**, no products approved, no AdMob/billing/analytics campaign/store action.
- Source proposals cannot turn into a Go decision by CI. **X10-035 remains PLANNED / HUMAN_GATE** until an explicit owner selection and separate spending/experiment authorization.

## X10-015 — Real Windows AppFactoryAgent end-to-end worker

- [Source intake](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/docs/X10-007_WINDOWS_SOURCE_INTAKE.md) documents sanitization, SHA manifest and fail-closed local checks, but the original Windows v0.1–v0.4 code is **not** in the accessible GitHub source.
- Its dependency `X10-008` remains `BLOCKED`; no actual worker invocation, job persistence, isolated worktree, recoverable patch, tests or GitHub PR produced *by* that worker have been verified. AppLab tooling or a ChatGPT-authored PR is not such evidence.
- **X10-015 remains PLANNED / HUMAN_GATE** until sanitized source, actual Windows/WSL worker receipt and interrupted-run recovery proof are available.

## Queue decision

The 5 additional workstreams had two source implementation advances (X10-023, X10-024) and three verified external authorization/evidence blockers (X10-032, X10-035, X10-015). Do not mark HUMAN_GATE tasks VERIFIED from this dossier. X10-026 eligibility must be reconciled against actual post-merge main CI and independently checked receipts. Golden admission, physical Android, Play, budget/spending and autonomous Windows agent claims remain separate.
