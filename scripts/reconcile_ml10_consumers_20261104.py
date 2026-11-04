#!/usr/bin/env python3
"""Reconcile verified ML10 consumer integrations after independent PR merges.

Idempotent post-audit delta. Canonical registry remains owner of app values;
do not re-run the one-time full-audit score uplift or promote complete CAP.
Run build_catalog.py afterward to regenerate all cross-app views.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
REG = BASE / "REGISTRO_CAPABILITY.json"
INV = BASE / "SOURCE_INVENTORY.json"
STAMP = "ML10_CONSUMER_ADMISSIONS_2026-11-04"
NOTE_SHA = "e10b058a43e3b238e59eb946138540287756d784"
TASTE_SHA = "REPLACE_ON_VERIFIED_MERGE"  # set only after exact-source TasteAI PR merge
NOTE_CI = "https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41840769025"
TASTE_CI = "REPLACE_WITH_ACTUAL_EXACT_HEAD_CI"

def main():
    if not re.fullmatch("[0-9a-f]{40}", TASTE_SHA):
        raise SystemExit("TasteAI merge/main SHA not proven; gate closed.")
    if "REPLACE_" in TASTE_CI:
        raise SystemExit("TasteAI exact-head CI not established; gate closed.")
    data = json.loads(REG.read_text(encoding="utf-8"))
    if data.get("ml10_consumer_admission_stamp") == STAMP:
        print("Already admitted; no re-application.")
        return
    records = data["records"]
    if len(records) != 160 or sum(len(c["app_states"]) for c in records) != 385:
        raise SystemExit("Registry changed: re-audit before changing values")
    caps = {rec["id"]: rec for rec in records}

    notes = caps["CAP-0116"]
    if notes["app_states"]["Notes-Ecosistema"] not in {"PROPOSTA", "SOURCE_REPORTED"}:
        raise SystemExit("Notes CAP-0116 state changed; manual review required")
    notes["app_states"]["Notes-Ecosistema"] = "SOURCE_REPORTED"
    previous_ease = notes["integration_ease_percent"]["Notes-Ecosistema"]
    notes["integration_ease_percent"]["Notes-Ecosistema"] = min(100, previous_ease + 2)
    notes["reviewed_at"] = "2026-11-04"
    notes["next_gate"] = ("User-visible source and attachment diff; explicit KEEP/VARIANT/merge with reversible canonical writes, "
                          "role/account-switch ACL and revision conflict tests; quantified device quality before Golden.")
    notes.setdefault("partial_source_evidence_ml10", {})["Notes-Ecosistema"] = {
        "source_sha": NOTE_SHA,
        "source_path": "flutter_app/lib/src/domain/note_duplicate_review.dart",
        "consumer_path": "flutter_app/lib/src/screens/notes_screen.dart",
        "test_path": "flutter_app/test/note_duplicate_review_test.dart",
        "pr": "https://github.com/riccardopinato/Notes-Ecosistema/pull/57",
        "ci": NOTE_CI,
        "scope": "Read-only filtered MinHash/LSH candidate preview and canonical-editor open; does NOT implement reversible merge/undo",
        "full_capability_complete": False, "device_pass": False, "golden_e5": False,
    }
    notes.setdefault("ml10_consumer_revisions", {})["Notes-Ecosistema"] = {
        "before": previous_ease,
        "after": notes["integration_ease_percent"]["Notes-Ecosistema"],
        "reason": "Source-backed read-only duplicate review now merged; reversible merge, attachment diff and account ACL not completed.",
        "not_success_probability": True,
    }

    taste = caps["CAP-0044"]
    if taste["app_states"]["TasteAI"] not in {"SOURCE_REPORTED", "SOURCE_CONFIRMED", "CI_VERIFIED"}:
        raise SystemExit("TasteAI anti-waste evidence unexpectedly unverified")
    # Existing CAP-0044 anti-waste implementation and score are UNCHANGED.
    # Similar recipes are adjacent bounded kNN functionality, not evidence that
    # anti-waste ingredient selection became more accurate or safety-certified.
    taste.setdefault("partial_source_evidence_ml10", {})["TasteAI"] = {
        "source_sha": TASTE_SHA,
        "source_path": "lib/domain/search/local_recipe_nearest_neighbors.dart",
        "consumer_path": "lib/features/recipes/recipe_widgets.dart",
        "test_path": "test/local_recipe_nearest_neighbors_test.dart",
        "pr": "https://github.com/riccardopinato/TasteAI/pull/2",
        "ci": TASTE_CI,
        "scope": "Adjacent related-recipes suggestion using canonical recipe IDs and Premium entitlement; not new anti-waste quality evidence",
        "full_capability_complete": False, "device_pass": False, "golden_e5": False,
    }
    taste["reviewed_at"] = "2026-11-04"

    inventory = json.loads(INV.read_text(encoding="utf-8"))
    by_repo = {row["name"]: row for row in inventory["repositories"]}
    for name, sha in (("Notes-Ecosistema", NOTE_SHA), ("TasteAI", TASTE_SHA),
                      ("App-Factory-Core", "1229d8c4d411fda76ccc58a6ed0118da1f7245e4"),
                      ("Idee-app-Archivi-riferimenti", "54705d4c5317e88d2a183cc5a47aa6e64ec886fc")):
        if name not in by_repo:
            raise SystemExit("Missing observed repo " + name)
        by_repo[name]["head_sha"] = sha
        by_repo[name]["head_observed_at"] = "2026-11-04"
    INV.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    data["ml10_consumer_admission_stamp"] = STAMP
    data["factory_baseline"] = "riccardopinato/App-Factory-Core@1229d8c4d411fda76ccc58a6ed0118da1f7245e4"
    REG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    output = f"""# ML10 — actual consumer postmerge reconciliation (04/11/2026)

- Updated after the [complete 160/385 registry audit](AUDIT_COMPLETO_ML10_2026-11-04.md).
- Catalog baseline: 160 capabilities, 385 app relationships, 48 app/idea names.
- App status/effort changes here are SCOPED, not full feature/Store claims.
- Notes CAP-0116 / Notes-Ecosistema: PROPOSTA → SOURCE_REPORTED;
  ease {previous_ease} → {notes['integration_ease_percent']['Notes-Ecosistema']}
  from merged read-only [PR #57](https://github.com/riccardopinato/Notes-Ecosistema/pull/57),
  exact-head [Flutter APK/AAB CI PASS]({NOTE_CI}),
  source \`{NOTE_SHA}\`. Full merge/undo and role/account-switch test pending.
- TasteAI CAP-0044: existing SOURCE_REPORTED status, priority and ease RETAINED;
  added adjacent kNN [PR #2](https://github.com/riccardopinato/TasteAI/pull/2),
  source \`{TASTE_SHA}\`, [Flutter/Apple CI]({TASTE_CI}).
  This does not measure anti-waste accuracy or ingredient/allergen safety.
- No new capability, no Golden promotion, no source data write, no new model/SDK.
- Master v27, Index v28, Registry v2. The central math references and scoped
  donor E3 are recorded in Core \`evidence/ML10_PORTFOLIO_CAPABILITY_LEDGER_2026-11-04.md\`.
- E4 physical/native/store, note merge workflow, role/ACL and label/model
  quality gates remain open. Do not replace those with green CI.
"""
    (BASE / "ML10_CONSUMER_POSTMERGE_2026-11-04.md").write_text(
        output.replace("\\`", "`"), encoding="utf-8")
    print("UPDATED Notes CAP-0116 scoped and TasteAI adjacent kNN; 160/385 retained")

if __name__ == "__main__":
    main()
