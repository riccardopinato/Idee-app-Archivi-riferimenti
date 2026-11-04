# ML10 — actual consumer postmerge reconciliation (04/11/2026)

- Updated after the [complete 160/385 registry audit](AUDIT_COMPLETO_ML10_2026-11-04.md).
- Catalog baseline: 160 capabilities, 385 app relationships, 48 app/idea names.
- App status/effort changes here are SCOPED, not full feature/Store claims.
- Notes CAP-0116 / Notes-Ecosistema: PROPOSTA → SOURCE_REPORTED;
  ease 83 → 85
  from merged read-only [PR #57](https://github.com/riccardopinato/Notes-Ecosistema/pull/57),
  exact-head [Flutter APK/AAB CI PASS](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41840769025),
  source `e10b058a43e3b238e59eb946138540287756d784`. Full merge/undo and role/account-switch test pending.
- TasteAI CAP-0044: existing SOURCE_REPORTED status, priority and ease RETAINED;
  added adjacent kNN [PR #2](https://github.com/riccardopinato/TasteAI/pull/2),
  source `fc2f80e43f91b441863f8e3a77ae7196251979cf`, [Flutter/Apple CI](https://github.com/riccardopinato/TasteAI/actions/runs/41842952989).
  This does not measure anti-waste accuracy or ingredient/allergen safety.
- No new capability, no Golden promotion, no source data write, no new model/SDK.
- Master v27, Index v28, Registry v2. The central math references and scoped
  donor E3 are recorded in Core `evidence/ML10_PORTFOLIO_CAPABILITY_LEDGER_2026-11-04.md`.
- E4 physical/native/store, note merge workflow, role/ACL and label/model
  quality gates remain open. Do not replace those with green CI.
