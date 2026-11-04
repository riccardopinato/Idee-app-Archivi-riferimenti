#!/usr/bin/env python3
"""Admit exactly six Anna's Diary partial-reuse ideas to product evaluation.

Safe, deterministic one-shot. It does NOT change source state, priority score,
product approval, roadmap, build or Golden certification. All 58 historical
candidate/source decisions remain auditable in the linked decision dossier.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI" / "REGISTRO_CAPABILITY.json"
APP = "Agenda-per-Anna"
STAMP = "ANNA_58_EVALUATION_2026-11-04"
FACTORY_SHA = "8052b45b771bf3c5694fc6dd8d037bd83233b37a"
APP_SHA = "ab5360b78187a643e2b101be21e6951441406059"
CATALOG_SHA = "40756900473dad1b73a6ba0bc2c747e679d9f3b4"
REPORT = ("12-CAPABILITY-E-IMPLEMENTAZIONI/"
          "AUDIT_ANNA_58_DA_VERIFICARE_2026-11-04.md")

# (bounded product evaluation scope, value rationale, next decision gate,
#  technical dependencies/relevant existing donor boundaries)
ADMISSIONS = {
    "CAP-0093": (
        "Estrarre righe checklist esplicite da testo personale del diario in "
        "un task canonico con selezione/anteprima; NON gerarchie di progetto.",
        "Un solo flusso di cattura gia esiste; Notes-Ecosistema espone un "
        "donor deterministico per le liste; riduce digitazione ripetuta.",
        "Decidere UX di selezione e fonte; prototipo senza scritture, quindi "
        "conferma task privato, link origine, undo e test duplicati/ACL.",
        ["lib/src/unified_capture.dart", "lib/src/event_preparation.dart"],
        ["Notes-Ecosistema/flutter_app/lib/src/domain/note_to_checklist.dart",
         "App-Factory-Core/golden/data/GOLDEN_LOCAL_RULES_AUTOMATION_ENGINE_v1_DRAFT.txt"],
    ),
    "CAP-0092": (
        "Estrarre facoltativamente un semplice task da frase dell'agenda/nota "
        "nel compositore corrente; NON assistente conversazionale autonomo.",
        "Parser evento e Unified Capture sono operativi; possibile "
        "estensione locale deterministica senza nuovo motore AI.",
        "Validare ambiguita IT/EN/ES/FR/PT, date e fusi; anteprima "
        "di un task e salvataggio solo su conferma e revisione ACL.",
        ["lib/src/natural_event_parser.dart", "lib/src/unified_capture.dart"],
        ["App-Factory-Core/reference_engines/lib/src/local_ml_candidates.dart",
         "App-Factory-Core/reference_engines/lib/src/contextual_suggestions.dart"],
    ),
    "CAP-0120": (
        "Campo opzionale di descrizione accessibile scritta dall'utente per "
        "foto del diario/Ricordi; NON generazione BLIP/cloud automatica.",
        "Foto e media hanno gia owner canonici, e il Product Bible richiede "
        "screen reader e semantica; evita nuovi pesi e permessi.",
        "Scegliere metadati media e ciclo di vita sicuro; test assistivi "
        "screen reader, backup, modifica, Trash, tutte le 5 lingue.",
        ["lib/src/diary/diary_memories.dart", "lib/src/domain_models.dart"],
        ["App-Factory-Core/golden/ui/GOLDEN_APP_SHELL_RESPONSIVE_VISUAL_QA_FLUTTER_v1_DRAFT.txt"],
    ),
    "CAP-0147": (
        "Riordinare opzionalmente solo 2-3 card gia presenti nella Home Oggi "
        "con reset; NON una nuova dashboard o un secondo store.",
        "Presets/moduli e preferenze sono proprieta dell'app; il Golden "
        "Progressive Disclosure e il donor Anna sono riusabili per UX.",
        "Decidere quali card e fallback legacy; prove UI5 per 5 lingue, "
        "small screen, contrasto, focus, privacy e account switch.",
        ["lib/src/domain_models.dart", "lib/src/screens/personalization_screen.dart",
         "lib/src/planner_views.dart"],
        ["App-Factory-Core/golden/ui/GOLDEN_PROGRESSIVE_DISCLOSURE_MODULE_VISIBILITY_FLUTTER_v1_DRAFT.txt"],
    ),
    "CAP-0145": (
        "Griglia privata di frequenza dei ricordi effettivamente registrati; "
        "NO mood inferito, ciclo/Vault, sentiment o statistiche condivise.",
        "Ricordi e archivio gia supportano proiezioni/aggregazioni read-only; "
        "una visualizzazione di densita puo facilitare rilettura annuale.",
        "Confermare valore UX e definizione presenza/assenza dati; test "
        "zero vs non registrato, Trash, consenso e filtri privacy.",
        ["lib/src/diary/diary_memories.dart", "lib/src/life_archive_domain.dart",
         "lib/src/year_review_domain.dart"],
        ["App-Factory-Core/golden/data/GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT.txt"],
    ),
    "CAP-0101": (
        "Aggiungere al massimo tre metriche semplici di task personali "
        "nella Weekly Review esistente; NON una dashboard aziendale.",
        "WeeklyReviewSummary conta gia completate/pending/scadute e usa "
        "task canoniche; nessuna nuova analytics pipeline necessaria.",
        "Verificare sovrapposizione con CAP-0111 e utilita reale; "
        "definire metriche e denominatori, filtri Trash/Noi e UX opt-in.",
        ["lib/src/weekly_review.dart", "lib/src/realistic_day_advice.dart"],
        ["App-Factory-Core/golden/data/GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT.txt"],
    ),
}


def main():
    raw = json.loads(PATH.read_text(encoding="utf-8"))
    records = raw["records"]
    apps = {app for record in records for app in record["app_states"]}
    links = sum(len(record["app_states"]) for record in records)
    if len(records) != 160 or len(apps) != 48 or links != 385:
        raise SystemExit(f"Unexpected registry {len(records)}/{len(apps)}/{links}")
    if sum(APP in rec["app_states"] for rec in records) != 74:
        raise SystemExit("Unexpected 74-link Anna catalogue")
    if raw.get("anna_evaluation_intake_20261104") == STAMP:
        print("ALREADY_APPLIED", STAMP)
        return
    if any(raw.get("anna_evaluation_intake_20261104") for _ in [0]):
        raise SystemExit("An existing audit version requires manual reconciliation")
    by_id = {record["id"]: record for record in records}
    if len(by_id) != len(records):
        raise SystemExit("Duplicate CAP ID")
    if any(r.get("app_evaluation_admissions", {}).get(APP)
           for r in records):
        raise SystemExit("Preexisting Anna admissions; stop instead of overwriting")

    for cap, (scope, rationale, next_gate, paths, donors) in ADMISSIONS.items():
        record = by_id[cap]
        status = record["app_states"].get(APP)
        audit = record.get("anna_full_source_audit", {})
        if status != "PROPOSTA" or audit.get("classification") != "PARTIAL_REUSE":
            raise SystemExit(f"{cap} source already changed: {status}/{audit}")
        if not all(isinstance(x, str) and x for x in paths + donors):
            raise SystemExit("Missing provenance for " + cap)
        record.setdefault("app_evaluation_admissions", {})[APP] = {
            "decision": "READY_FOR_PRODUCT_EVALUATION",
            "assessed_at": "2026-11-04",
            "factory_sha": FACTORY_SHA,
            "app_sha": APP_SHA,
            "catalog_baseline_sha": CATALOG_SHA,
            "scope": scope,
            "rationale": rationale,
            "next_gate": next_gate,
            "source_paths": paths,
            "donor_or_golden_refs": donors,
            "report": REPORT,
            "implementation_approved": False,
            "source_state_changed": False,
            "physical_device_verified": False,
            "product_bible_changed": False,
        }
    raw["anna_evaluation_intake_20261104"] = STAMP
    PATH.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    print("ADMITTED", ",".join(ADMISSIONS), "6; retained 52; unchanged 160/385")


if __name__ == "__main__":
    main()
