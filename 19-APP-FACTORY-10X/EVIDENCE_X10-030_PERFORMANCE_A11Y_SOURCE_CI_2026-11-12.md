# X10-030 — Performance + accessibility report gate: SOURCE+CI
Factory: App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619 Master v27 Golden Index v29.

AppLab [PR #227](https://github.com/riccardopinato/AppLab/pull/227) merged squash `db263d48cf1dbdaf85933e3c044dd5d9ccbf7559`. Exact PR head `5cf99a11ad8654cc788f74bcffb814f3329969ba`: **7/7** workflows SUCCESS (AppLab CI, CodeQL, Governance, Runtime Fixture, Autonomous Review, Live Browser E2E, Emulator Self Test). Codex review completed with zero findings at this exact head; all historical CodeQL and two Codex P2 threads replied/resolved before merge.

Implementation: `scripts/x10_performance_a11y_gate.py`, `backend/tests/test_x10_performance_a11y_gate.py`, `integration/agent_core/X10-030_PERFORMANCE_A11Y_GATE.md`. Same immutable source SHA + artifact checksum + workflow run + device id across >=3 performance samples. Reuses existing AppLab Performance Lab comparison; display-density 48dp touch-target checks, missing labels, long-clickable controls and bounds. Baselines require valid startup/PSS/jank measurements. Missing baseline, regressed or WARN findings stay review-required.

**Scope: source+CI only.** Simulated performance reports and CI emulator self-test prove this adapter, not real low-end physical device data, consumer startup times, TalkBack, physical QA or Play rollout. HUMAN_GATE X10-032 remains independent; X10-033 may now be developed.
