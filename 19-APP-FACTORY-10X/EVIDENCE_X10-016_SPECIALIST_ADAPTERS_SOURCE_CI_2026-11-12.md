# X10-016 — Agent Research + QA specialist adapters (SOURCE+CI)
Factory baseline: App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619, Master 27 / Golden Index 29.

[Agent Core PR #22](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/22) MERGED `35a0e4f111e00d7193ac087f122afcfaf0eda68f`. PR exact head `8d7efc65b436bc05e2b55a735a8350e688fa233b` had *Validate context contracts* SUCCESS and independent Codex exact-head clean review. Prior P2 URL encoding fixed with path quoting and negative test, thread resolved.

Files `scripts/agent_specialist_adapters.py`, `tests/test_agent_specialist_adapters.py`, `docs/X10-016_RESEARCH_QA_SPECIALISTS.md`.

- Reuses existing Agent Core authorization gateway; no new LLM/executor/PR engine.
- Research accepts bounded pinned-source metadata and external authenticated lookup, outputs declared SPDX for later legal verification, never certifies donor/Golden.
- QA forwards the existing AppLab X10-028 router to an authorized injected executor, wraps the result as REPORT_ONLY even if a synthetic test returns PASS.
- No live Windows importer, external research provider, real AppLab test executor, physical device or Finance provider connected by this PR. No secret, account or portfolio access.

Status VERIFIED only for **SOURCE+CI** scope. X10-015 remains HUMAN_GATE and X10-008 Windows source intake remains BLOCKED.
