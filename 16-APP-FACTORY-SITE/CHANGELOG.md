# App Factory Control Center — Changelog

## 2026-11-14 — Gateway MCP status view (source-only)

- Added an isolated, public, **date-scoped** Gateway progress dataset to `data/gateway_progress.json`, covering PRs #25–#32 of App-Factory-Agent-Core with observed exact-head CI links and dependencies.
- Added an Italian read-only Gateway page to the existing `src/index.html`: PR search, draft/blocker filter, source links, explicit review and deploy caveats.
- Existing `data/snapshot.json`, `data/context_fleet.json`, the `appfactory-control-center-v1` browser storage key, manual history, CAP, donor and Golden data are NOT touched.
- Added `tests/gateway_site_test.py` and CI coverage to reject false approvals, incorrect SHA/run identities, missing DOM hooks and broken JS syntax.
- Updated repository and Site indexes for discoverability. The status is a **snapshot, not a live connector or deployed site**; no new GitHub token or web service.
- No merges or releases claimed. Review/branch-protection gates of downstream PRs are still NOT_VERIFIED.
