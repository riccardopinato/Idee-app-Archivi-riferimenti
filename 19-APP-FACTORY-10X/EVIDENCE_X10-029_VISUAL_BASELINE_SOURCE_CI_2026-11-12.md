# X10-029 — Baseline visual regression: SOURCE+CI acceptance

**Factory baseline:** App-Factory-Core@`c5adc147046beb7024629466d10eeb799c3c2619`; Master 27 / Golden Index 29.

- AppLab [PR #226](https://github.com/riccardopinato/AppLab/pull/226) MERGED, main squash `de6058c78bc572821635e8cf0f5b3079ee716b7b`.
- Exact PR head `4c9de3873ee9ba526eeabace808e6cf9801e5e80`; seven workflows all SUCCESS (Fixture Build, CodeQL, Governance, Autonomous Review, Live Emulator Browser E2E, AppLab CI, Emulator Self Test). Independent Codex exact-head review completed no findings.
- Previous CI `9c73f66b009fb021abfbb837e3fbd5cd4a7014bb`: two failures due to shared mutable display profile in synthetic test fixture; fixed before exact-head rerun. No tests weakened or skipped to pass.
- Files: `scripts/x10_visual_baseline_gate.py`, `backend/tests/test_x10_visual_baseline_gate.py`, `integration/agent_core/X10-029_VISUAL_BASELINE_ADOPTION.md`.
- Reuse: existing `scripts/visual_regression.py` comparator, approved baseline lookup, screenshot and UI hierarchy SHA-256, profile matching (theme/locale/screen/form-factor/text scale), interaction source/run-bound receipts. Missing baseline -> NO_BASELINE, comparator WARN/excessive mask -> HUMAN REVIEW, no automated acceptance of false positives.

**VERIFIED SOURCE+CI only.** Real consumer baselines, Android screenshot capture, independently checked UI interaction, physical-device acceptance and product runtime are **NOT VERIFIED**. X10-030 remains the next dependency for X10-033's final gate.
