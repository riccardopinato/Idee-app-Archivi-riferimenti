#!/usr/bin/env python3
"""Build/validate the App Factory cross-application capability catalogue.

Source of truth: 12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json.
No network, API keys, user data, external dependencies or repository mutations
outside the derived catalogue paths. --check is read-only and fail-closed.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT_ROOT = ROOT / '13-KIT-INTEGRAZIONE'
BASE = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
JSON_FILE = BASE / "REGISTRO_CAPABILITY.json"
KNOWN = {"PROPOSTA", "ROADMAP_STORICA", "SOURCE_REPORTED", "DONOR_REPORTED",
         "SOURCE_CONFIRMED", "CI_VERIFIED", "DEVICE_VERIFIED", "RELEASE", "BLOCKED"}
DOCUMENTED_STAGES = {"SOURCE_REPORTED", "DONOR_REPORTED", "SOURCE_CONFIRMED",
                     "CI_VERIFIED", "DEVICE_VERIFIED", "RELEASE"}

def md_table(headers, rows):
    def clean(x):
        return str(x).replace("|", "/").replace("\n", " ")
    return (
        "| " + " | ".join(headers) + " |\n"
        + "| " + " | ".join("---" for _ in headers) + " |\n"
        + "".join("| " + " | ".join(clean(x) for x in row) + " |\n" for row in rows)
    )

def brief(value, limit=118):
    value = " ".join(value.split())
    if len(value) <= limit:
        return value
    return value[:limit-1].rsplit(" ", 1)[0] + "…"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check derivations without modifying files")
    args = parser.parse_args()
    data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    records = data["records"]
    inventory = json.loads((BASE / "SOURCE_INVENTORY.json").read_text(encoding="utf-8"))
    repos = inventory["repositories"]
    if len(repos) != len({r["name"] for r in repos}) or any(not r["default_branch"] for r in repos):
        raise SystemExit("Invalid or duplicate repository inventory")
    ids = [r["id"] for r in records]
    if data["schema_version"] != 1 or len(ids) != len(set(ids)):
        raise SystemExit("Invalid schema or duplicate capability ID")
    numeric_ids = []
    for rec in records:
        match = re.fullmatch(r"CAP-(\d{4})", rec["id"])
        if not match:
            raise SystemExit("Invalid ID " + rec["id"])
        numeric_ids.append(int(match.group(1)))
        if not rec["title"] or not rec["description"] or not rec["next_gate"]:
            raise SystemExit("Incomplete capability " + rec["id"])
        if not rec["source"].get("ref") or not rec["source"].get("type"):
            raise SystemExit("Missing provenance " + rec["id"])
        if not rec["app_states"]:
            raise SystemExit("Capability without an app: " + rec["id"])
        ease = rec.get("integration_ease_percent")
        if not isinstance(ease, dict) or set(ease) != set(rec["app_states"]):
            raise SystemExit("Missing per-app integration estimate: " + rec["id"])
        if any(type(value) is not int or not 0 <= value <= 100 for value in ease.values()):
            raise SystemExit("Invalid per-app integration ease percentage: " + rec["id"])
        if not set(rec["app_states"].values()).issubset(KNOWN):
            raise SystemExit("Invalid app status in " + rec["id"])
        s = rec["scores"]
        if not all(isinstance(s[k], int) and 1 <= s[k] <= 5 for k in
                   ("user_value", "cross_app_reuse", "feasibility", "evidence_strength", "risk_control")):
            raise SystemExit("Invalid factor in " + rec["id"])
        # Decimal rounding matches ordinary nearest-integer for these inputs.
        expected = int(20 * (0.35*s["user_value"] + 0.25*s["cross_app_reuse"] +
                             0.20*s["feasibility"] + 0.10*s["evidence_strength"] +
                             0.10*s["risk_control"]) + 0.5)
        label = "P1" if expected >= 92 else "P2" if expected >= 79 else "P3"
        if rec["score"] != expected or rec["priority"] != label:
            raise SystemExit("Score/priority drift in " + rec["id"])
    if numeric_ids != sorted(numeric_ids) or numeric_ids[0] < 1:
        raise SystemExit("Capability IDs must be ordered and never reused")
    apps = sorted({a for rec in records for a in rec["app_states"]})
    rank = sorted(records, key=lambda rec: (-rec["score"], rec["id"]))
    versions = {}
    versions["CLASSIFICA_PRIORITA.md"] = (
        f"# Classifica capability — snapshot {data['updated_at']}\n\n"
        "**Ranking tecnico-editoriale relativo, NON approvazione di roadmap.** P1: >=92, P2: 79–91, P3: <79. P0 e riservato ai veri incidenti di sicurezza/dati, non alla ricerca di idee.\n\n"
        + md_table(["#","ID","Capability","Ambito","Score","Kit tecnico","Classe","App interessate","Prossima verifica"], [
            [i, f"[{rec['id']}](REGISTRO_CAPABILITY/{rec['id']}.md)", rec["title"], rec["domain"], rec["score"],
             f"[Apri](../13-KIT-INTEGRAZIONE/{rec['id']}/README.md)", rec["priority"], ", ".join(rec["app_states"].keys()), rec["next_gate"]]
            for i, rec in enumerate(rank, 1)])
        + "\nIl ranking NON usa metriche economiche reali; la priorita finale spetta alla roadmap della singola app.\n"
    )
    versions["MATRICE_APP.md"] = (
        "# Matrice capability per app\n\n"
        "_Generato da REGISTRO_CAPABILITY.json. Ogni cella e una fotografia di ricerca, non prova runtime._\n\n"
        + md_table(["App / prodotto","N. capability candidate/riuso","Prime 8 per punteggio"], [
            [app, sum(app in rec["app_states"] for rec in records),
             "; ".join(f"{rec['id']} {rec['title']} ({rec['app_states'][app]})" for rec in
                       [rec for rec in rank if app in rec["app_states"]][:8])]
            for app in apps])
        + "\nPer il dettaglio di tutte le associazioni consultare `REGISTRO_CAPABILITY.json` e le schede individuali.\n"
    )
    status_rows = [[stage, sum(stage == status for rec in records for status in rec["app_states"].values()), desc]
                   for stage, desc in data["statuses"].items()]
    existing = [rec for rec in records if any(s in DOCUMENTED_STAGES
                                             for s in rec["app_states"].values())]
    versions["STATO_IMPLEMENTAZIONI.md"] = (
        f"# Stato delle implementazioni — audit {data['updated_at']}\n\n"
        "Gli stati sono **per app**, non globali. `SOURCE_REPORTED` indica fonte repo/audit consultata, non esecuzione del codice ne CI/DEVICE PASS verificati in questa sessione.\n\n"
        + md_table(["Stato","Associamenti app-capability","Interpretazione"], status_rows)
        + "\n"
        + md_table(["Capability con donor o sorgente documentata","App","Prova"], [
            [rec["id"] + " " + rec["title"],
             ", ".join(f"{app} ({status})" for app, status in rec["app_states"].items()
                       if status in DOCUMENTED_STAGES), rec["source"]["ref"]]
            for rec in existing])
        + "\nNon promuovere a `CI_VERIFIED`, `DEVICE_VERIFIED` o `RELEASE` senza evidence esatta del repo e della build pertinente.\n"
    )
    for rec in records:
        apps_text = "\n".join(f"  - {app}: `{status}`" for app, status in rec["app_states"].items())
        versions[f"REGISTRO_CAPABILITY/{rec['id']}.md"] = (
            f"# {rec['id']} — {rec['title']}\n\n"
            f"- **Categoria:** {rec['domain']}\n"
            f"- **Priorita:** {rec['priority']} — {rec['score']}/100 (stima relativa)\n"
            f"- **Problema / funzione:** {rec['description']}\n"
            f"- **App e stato**:\n{apps_text}\n"
            f"- **Fonte e livello:** {rec['source']['type']} — {rec['source']['ref']}\n"
            f"- **Fattibilita / prossimo gate:** {rec['next_gate']}\n"
            "- **Validazione:** NON VERIFICATA in questo audit; distinguere codice, CI, dispositivo e distribuzione.\n"
            "- **Stato commerciale:** idea catalogata, non approvazione implicita del Product Bible.\n"
            f"- **Revisione:** {rec['reviewed_at']}\n"
            f"- **Kit tecnico:** [Apri il kit](../../13-KIT-INTEGRAZIONE/{rec['id']}/README.md)\n\n"
            "La scheda e generata dalla fonte canonica `REGISTRO_CAPABILITY.json`. Cambiare prima il JSON e rigenerare le viste.\n"
        )
    for app in apps:
        items = [rec for rec in rank if app in rec["app_states"]]
        versions[f"PER_APP/{app}.md"] = (
            f"# {app} — capability e priorita\n\n"
            "Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.\n\n"
            + md_table(["ID","Capability","Priorita","Score","Facilita integrazione (%)","Descrizione breve","Kit tecnico","Stato nell'app","Prossimo gate"], [
                [f"[{rec['id']}](../REGISTRO_CAPABILITY/{rec['id']}.md)", rec["title"], rec["priority"],
                 rec["score"], f"{rec['integration_ease_percent'][app]}%", brief(rec["description"]),
                 f"[Apri](../../13-KIT-INTEGRAZIONE/{rec['id']}/README.md)",
                 rec["app_states"][app], rec["next_gate"]] for rec in items])
            + f"\n**Totale associazioni:** {len(items)}. Non modificare automaticamente la roadmap del prodotto.\n"
        )
    problems=[]
    required_kit_files = ("README.md", "SPECIFICHE.md", "CODICE_RIFERIMENTO.txt", "INTEGRAZIONE_FLUTTER.md", "LICENZE_E_DIPENDENZE.md", "TEST_E_VALIDAZIONE.md")
    for rec in records:
        for filename in required_kit_files:
            kit_path = KIT_ROOT / rec["id"] / filename
            if not kit_path.is_file():
                problems.append(str(kit_path.relative_to(ROOT)))
    for relative, content in versions.items():
        path=BASE/relative
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                problems.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    actual_cards = {p.name for p in (BASE/"REGISTRO_CAPABILITY").glob("CAP-*.md")}
    expected_cards = {rec["id"] + ".md" for rec in records}
    if actual_cards - expected_cards:
        problems.extend(sorted(actual_cards-expected_cards))
    actual_apps = {p.name for p in (BASE/"PER_APP").glob("*.md")}
    expected_apps = {app + ".md" for app in apps}
    if actual_apps - expected_apps:
        problems.extend(sorted(actual_apps-expected_apps))
    if problems:
        raise SystemExit("Catalogue drift:\n" + "\n".join(problems[:30]))
    print(f"VALID: {len(records)} capabilities, {len(apps)} app names, "
          f"{sum(len(rec['app_states']) for rec in records)} associations")

if __name__ == "__main__":
    main()
