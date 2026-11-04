#!/usr/bin/env python3
"""Evidence-scoped 160 CAP / 385 app-link ML10 audit and deterministic regrade.

Input is the canonical registry. No network/API/secrets or app repo writes.
Run on a throwaway branch and regenerate all views through build_catalog.py.
No blanket uplift for the mere existence of mathematical reference engines.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
REGISTRY = BASE / "REGISTRO_CAPABILITY.json"
INVENTORY = BASE / "SOURCE_INVENTORY.json"
STAMP = "ML10_160_CAP_385_LINKS_2026-11-04"
BASELINE = "riccardopinato/App-Factory-Core@02f3cd94f0ee6f19bc06fc0cb329fdf5398a739b"
DATE = "2026-11-04"
CORE_CI = "https://github.com/riccardopinato/App-Factory-Core/actions/runs/41838055370"
NOTES_CI = "https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41822558551"
POCKET_CI = "https://github.com/riccardopinato/Pocket-Guard/actions/runs/41822147632"
GH = "https://github.com/riccardopinato/"

# Exact, observed main heads for only repositories that changed in the
# 31/31 live head check; unchanged heads remain pinned in SOURCE_INVENTORY.
OBSERVED_HEADS = {
    "App-Factory-Core": "02f3cd94f0ee6f19bc06fc0cb329fdf5398a739b",
    "Idee-app-Archivi-riferimenti": "b61934710e4f69301d338c890cae53d16d480c24",
    "Notes-Ecosistema": "ab254e7a8927778498bc3035d1b97bf21d323fcc",
    "Pocket-Guard": "dcec7d82e374e955f1e06c2c8d0a9143c418b6d7",
}

# Only changes justified by new proof or by an acknowledged risk/footprint
# correction. Scores are NOT percentages of predicted product success.
FACTORS = {
    "CAP-0116": ({"feasibility": 4},
        "Small read-only MinHash/LSH source and guarded consumer pilot reduce narrow technical implementation cost; reversible canonical merge is NOT proven.",
        GH + "App-Factory-Core/pull/71"),
    "CAP-0153": ({"evidence_strength": 4},
        "Exact-main test of bounded logistic/Holt numerical reference increases math evidence only; no personal task-delay calibration.",
        GH + "App-Factory-Core/pull/73"),
    "CAP-0046": ({"feasibility": 3},
        "No validated licensed vision checkpoint, runtime/model footprint or Italian ingredient-dataset accuracy; reduce feasibility.",
        GH + "Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md"),
    "CAP-0132": ({"feasibility": 2},
        "Audio model pack, rights, microphone UX and on-device profiling remain unverified; reference ML math does not implement an audio classifier.",
        GH + "Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md"),
}

# A small adjusted effort estimate per specific consumer; bounded in [0,100].
# No ease changes for unobserved app-code or merely analogous algorithms.
EASE = {
    ("CAP-0116", "Notes-Ecosistema"): 6,
    ("CAP-0152", "Notes-Ecosistema"): 2,
    ("CAP-0160", "Notes-Ecosistema"): 2,
    ("CAP-0158", "Pocket-Guard"): 2,
    ("CAP-0153", "Notes-Ecosistema"): 3,
    ("CAP-0153", "Agenda-per-Anna"): 2,
    ("CAP-0153", "FocuSense"): 1,
    ("CAP-0154", "Agenda-per-Anna"): 1,
    ("CAP-0124", "Notes-Ecosistema"): 2,
    ("CAP-0044", "In-Cucina-con-gli-Anime"): 2,
    ("CAP-0044", "TasteAI"): 1,
    ("CAP-0046", "In-Cucina-con-gli-Anime"): -6,
    ("CAP-0046", "TasteAI"): -6,
    ("CAP-0132", "Notes-Ecosistema"): -5,
    ("CAP-0132", "Wonderlog"): -5,
    ("CAP-0132", "Agenda-per-Anna"): -5,
    ("CAP-0061", "Battery_Guard"): 3,
    ("CAP-0057", "Pocket-Guard"): 1,
    ("CAP-0032", "Notes-Ecosistema"): 1,
    ("CAP-0159", "Wonderlog"): 1,
}
EASE_REASON = {
    "CAP-0116": "Core ML10 MinHash reference and candidate preview reduce lexical implementation effort; source permissions and merge/undo remain unproven.",
    "CAP-0152": "Notes existing local bounded fuzzy fallback merged in PR #56; account ACL/save-time gate remains.",
    "CAP-0160": "Notes editor local TF-IDF suggestions merged in PR #56; human Save and ACL remain app duties.",
    "CAP-0158": "Pocket Guard live-session EWMA shadow sample observer merged #6; hardware/OEM and alarm-decision gate remain.",
    "CAP-0153": "Core numerical logistic/Holt tested; no trained, calibrated user-forecast predictor in any app.",
    "CAP-0154": "Core Viterbi math available; labeled emissions and opt-in behavioral model missing.",
    "CAP-0124": "Core HAC small-N reference; no topical structure changes or personal-note grouping validated.",
    "CAP-0044": "Core bounded kNN can rank user-visible recipe features; allergy, rights and canonical ingredient constraints external.",
    "CAP-0046": "No licensed, benchmarked offline image classifier model and preprocessing/ABI contract.",
    "CAP-0132": "No licensed, benchmarked offline audio classifier model and microphone/privacy permission validation.",
    "CAP-0061": "Core EWMA/Holt additive seasonality reference only; phone fuel-gauge ETA accuracy unmeasured.",
    "CAP-0057": "Core LOF/isolation math does not supplant Android real-world sensor truth or alarm state policy.",
    "CAP-0032": "Core bounded PCA/SVD projection provides optional math; no actual semantic model recall uplift claimed.",
    "CAP-0159": "Existing grid and radius geospatial reference remains preferable to bounded HAC on thousands of map POIs.",
}

# This is partial-app source evidence. No generic CAP is treated as fully
# integrated if the documented product scope includes extra behavior.
PARTIAL = {
    ("CAP-0152", "Notes-Ecosistema"): {
        "source_sha": "ab254e7a8927778498bc3035d1b97bf21d323fcc",
        "source_path": "flutter_app/lib/src/domain/note_local_signals.dart",
        "scope": "Typo fallback; bounded active notes, no independent source ACL attestation",
        "pr": GH + "Notes-Ecosistema/pull/56", "ci": NOTES_CI,
    },
    ("CAP-0160", "Notes-Ecosistema"): {
        "source_sha": "ab254e7a8927778498bc3035d1b97bf21d323fcc",
        "source_path": "flutter_app/lib/src/domain/note_local_signals.dart",
        "scope": "TF-IDF tags offered in editor; explicit Save but no certified ACL/revision",
        "pr": GH + "Notes-Ecosistema/pull/56", "ci": NOTES_CI,
    },
    ("CAP-0158", "Pocket-Guard"): {
        "source_sha": "dcec7d82e374e955f1e06c2c8d0a9143c418b6d7",
        "source_path": "app/src/main/java/com/riccardopinato/pocketguard/detection/SmartProtectionEngine.kt",
        "scope": "Diagnostic shadow motion score only, NOT alarm decision",
        "pr": GH + "Pocket-Guard/pull/6", "ci": POCKET_CI,
    },
}
# Later merge Notes PR #57 before marking CAP-0116 partial consumer source.

def score(s):
    return int(20 * (
        .35 * s["user_value"] + .25 * s["cross_app_reuse"] +
        .20 * s["feasibility"] + .10 * s["evidence_strength"] +
        .10 * s["risk_control"]) + .5)

def priority(value):
    return "P1" if value >= 92 else "P2" if value >= 79 else "P3"

def write_csv(name, rows, columns):
    with (BASE / name).open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

def main():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("ml10_full_audit_stamp") == STAMP:
        print("ML10 audited state already applied; no repeat increments.")
        return
    records = data["records"]
    apps = {app for r in records for app in r["app_states"]}
    associations = sum(len(r["app_states"]) for r in records)
    if len(records) != 160 or len(apps) != 48 or associations != 385:
        raise SystemExit(f"WRONG_BASELINE {len(records)}/{len(apps)}/{associations}")
    if {r["id"] for r in records} != {
            f"CAP-{i:04d}" for i in range(1, 161)}:
        raise SystemExit("Non-contiguous capability IDs; stop instead of rewriting")
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    if len(inventory["repositories"]) != 31:
        raise SystemExit("Source inventory 31 changed; recheck source heads")
    for row in inventory["repositories"]:
        if row["name"] in OBSERVED_HEADS:
            row["head_sha"] = OBSERVED_HEADS[row["name"]]
            row["head_observed_at"] = DATE
    INVENTORY.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cap_rows = []
    app_rows = []
    for record in records:
        key = record["id"]
        before = record["score"]
        previous = dict(record["scores"])
        rationale = "RETAIN: no new consumer/quality evidence for a defensible score change"
        cite = record["source"].get("ref", "")
        if key in FACTORS:
            changed, rationale, cite = FACTORS[key]
            record["scores"].update(changed)
        after = score(record["scores"])
        record["score"] = after
        record["priority"] = priority(after)
        record["reviewed_at"] = DATE
        record["ml10_global_audit"] = {
            "before": before, "after": after, "before_factors": previous,
            "rationale": rationale, "scope": "CAP-level, not an app certification",
            "evidence": cite, "factory": BASELINE,
        }
        cap_rows.append({
            "cap_id": key, "title": record["title"],
            "before": before, "after": after, "delta": after-before,
            "priority": record["priority"], "rationale": rationale,
            "source": cite,
        })
        record.setdefault("ml10_app_audit", {})
        for app in record["app_states"]:
            old_ease = record["integration_ease_percent"][app]
            old_state = record["app_states"][app]
            delta = EASE.get((key, app), 0)
            new_ease = max(0, min(100, old_ease + delta))
            evidence = PARTIAL.get((key, app))
            if evidence and old_state in {"PROPOSTA", "ROADMAP_STORICA"}:
                record["app_states"][app] = "SOURCE_REPORTED"
                record.setdefault("partial_source_evidence_ml10", {})[app] = {
                    **evidence, "full_capability_complete": False,
                    "device_pass": False, "golden_e5": False,
                }
            record["integration_ease_percent"][app] = new_ease
            reason = (EASE_REASON[key] if delta
                      else "RETAIN: no new verified app-source/adaptation evidence")
            record["ml10_app_audit"][app] = {
                "before": old_ease, "after": new_ease,
                "before_state": old_state, "after_state": record["app_states"][app],
                "rationale": reason, "measured": False,
            }
            app_rows.append({
                "cap_id": key, "app": app, "before_ease": old_ease,
                "after_ease": new_ease, "delta": new_ease-old_ease,
                "before_state": old_state, "after_state": record["app_states"][app],
                "rationale": reason,
            })
    data["factory_baseline"] = BASELINE
    data["updated_at"] = DATE
    data["ml10_full_audit_stamp"] = STAMP
    data["ml10_full_audit_report"] = (
        "12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_COMPLETO_ML10_2026-11-04.md")
    REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")

    write_csv("AUDIT_COMPLETO_CAP_ML10_2026-11-04.csv", cap_rows,
              ["cap_id", "title", "before", "after", "delta",
               "priority", "rationale", "source"])
    write_csv("AUDIT_COMPLETO_APP_ML10_2026-11-04.csv", app_rows,
              ["cap_id", "app", "before_ease", "after_ease", "delta",
               "before_state", "after_state", "rationale"])
    changed = [r for r in cap_rows if r["delta"]]
    changed_ease = [r for r in app_rows if r["delta"]]
    changed_state = [r for r in app_rows if r["before_state"] != r["after_state"]]
    md = [
        "# Audit completo capability / ML10 — 4 novembre 2026",
        "",
        f"**Baseline:** \\u0060{BASELINE}\\u0060; Master v27 / Golden Index v28 / Registry v2.",
        "**Scope:** tutte le 160 CAP e 385 associazioni riferite alle 48 app/idee;",
        "31 repository GitHub confrontati per HEAD prima del presente pass.",
        "**Importante:** 160/385 e un audit completo **del registro e delle evidenze note**;",
        "non sono 160 implementazioni ispezionate end-to-end ne 48 test hardware.",
        "Le 17 app senza repo nell'inventario mantengono SOURCE NON VERIFICATA.",
        "",
        f"- Ricalcolate e controllate: **{len(cap_rows)}/160 score**, **{len(app_rows)}/385 stime app**.",
        f"- Score modificati con motivazione: **{len(changed)}**; invariati: **{160-len(changed)}**.",
        f"- Facilita modificate con motivazione: **{len(changed_ease)}**; invariati: **{385-len(changed_ease)}**.",
        f"- Stati per app modificati con evidenza scoped: **{len(changed_state)}**.",
        "- Nuove CAP: 0. Golden certificati: 0. Nessuna modifica al Product Bible.",
        "- Numeri di facilità: stime relative, NON probabilità empiriche.",
        "",
        "## Score modificati",
        "",
        "| CAP | Prima | Dopo | Motivo / fonte |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in changed:
        md.append(f"| {row['cap_id']} | {row['before']} | {row['after']} | {row['rationale']} ({row['source']}) |")
    md.extend([
        "",
        "## Facilità app modificate",
        "",
        "| CAP / app | Prima | Dopo | Motivo |",
        "| --- | ---: | ---: | --- |",
    ])
    for row in changed_ease:
        md.append(f"| {row['cap_id']} / {row['app']} | {row['before_ease']} | {row['after_ease']} | {row['rationale']} |")
    md.extend([
        "",
        "## Scoring and validation limits",
        "",
        "I cinque fattori originali hanno pesi 35% valore, 25% riuso, 20% fattibilità,",
        "10% evidenza, 10% rischio. Non si alterano score non corroborati.",
        "CAP-0116 include esplicitamente merge reversibile: un read-only reviewer non completa il CAP.",
        "CAP-0158 Pocket osserva i sensori in SHADOW, non pilota allarmi.",
        "LiteRT/Core ML image/audio mancano di checkpoint licenziati e test dispositivi.",
        "Core Dart numerics CI: " + CORE_CI,
        "Notes verified historical fuzzy + TF-IDF main CI: " + NOTES_CI,
        "Pocket shadow postmerge: " + POCKET_CI,
        "ML10 audit and architecture: " + GH + "Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md",
        "",
        "## 160/385 machine-readable full audit",
        "",
        "- [Full CAP before/after and evidence CSV](AUDIT_COMPLETO_CAP_ML10_2026-11-04.csv)",
        "- [Full app-CAP before/after and state CSV](AUDIT_COMPLETO_APP_ML10_2026-11-04.csv)",
        "- [Canonical registry and per-record rationale](REGISTRO_CAPABILITY.json)",
        "- Per-app generated operational views: \\u0060PER_APP/<app>/\\u0060.",
        "",
        "## Remaining physical/quality gates",
        "",
        "Notes Duplicate Review: source ACL, account switch, revision at merge-time,",
        "attachment diff, explicit reversible merge and real precision/recall.",
        "Pocket Guard: OEM, false positives, battery/lifecycle multi-device.",
        "HMM / LOF / logistic: labeled independent validation, opt-in and power budgets.",
        "Vision/audio: rights, model checksum, preprocessing, ABI and on-device tests.",
        "Golden promotion needs its own reviewed, validated Core PR and E5 proof.",
        "",
    ])
    # Avoid injecting invented metric percentages for any app.
    (BASE / "AUDIT_COMPLETO_ML10_2026-11-04.md").write_text(
        "\n".join(md).replace("\\u0060", "`"), encoding="utf-8")
    print("AUDIT_DONE", len(cap_rows), len(app_rows),
          "score_changed", len(changed), "ease_changed", len(changed_ease),
          "state_changed", len(changed_state))

if __name__ == "__main__":
    main()
