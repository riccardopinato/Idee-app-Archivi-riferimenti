#!/usr/bin/env python3
"""Generate operational views; no API/network, no external dependencies.

Only confirmed exact-scope source evidence goes to GIA_INTEGRATI.
Historical score tables remain immutable; this script splits the working queue.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAP = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI" / "REGISTRO_CAPABILITY.json"
IDEA = ROOT / "11-NUOVE-IDEE" / "IA-2026-11-02"
STATUS = IDEA / "INTEGRATION_STATUS.json"
RANKING = IDEA / "RANKING_100_COMPLETO.md"
VERIFIED = {"SOURCE_CONFIRMED", "CI_VERIFIED", "DEVICE_VERIFIED", "RELEASE"}
REPORTED = {"SOURCE_REPORTED", "DONOR_REPORTED"}


def clean(text):
    return str(text).replace("|", "/").replace("\n", " ").strip()


def table(headers, rows):
    if not rows:
        return "_Nessuna voce in questa sezione._\n"
    return (
        "| " + " | ".join(headers) + " |\n"
        + "| " + " | ".join("---" for _ in headers) + " |\n"
        + "".join("| " + " | ".join(clean(v) for v in row) + " |\n" for row in rows)
    )


def proven_cap(c, app, state):
    ev = c.get("implementation_evidence", {}).get(app, {})
    sha = ev.get("source_sha")
    path = ev.get("source_path")
    if (state in VERIFIED and sha and path and ev.get("merged_pr")
            and ev.get("ci_check_url") and ev.get("source_state") == "MERGED"):
        return "https://github.com/riccardopinato/" + app + "/blob/" + sha + "/" + path
    source = c.get("source", {}).get("ref", "")
    if state == "SOURCE_CONFIRMED" and re.match(
            r"^https://github[.]com/riccardopinato/[^/]+/blob/[0-9a-f]{40}/[^ ]+", source):
        return source
    return None


def parse_ideas():
    result = []
    for line in RANKING.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*\d+\s*\|\s*\d+\s*\|", line):
            continue
        parts = [x.strip() for x in line.strip().strip("|").split("|")]
        n = int(parts[1])
        title_match = re.search(r"\[([^]]+)\]", parts[2])
        if not title_match:
            raise ValueError("Ranking without linked title: " + str(n))
        result.append({
            "n": n, "title": title_match.group(1),
            "score": int(re.search(r"\d+", parts[3]).group()),
            "ease": int(re.search(r"\d+", parts[4]).group()),
        })
    if len(result) != 100 or {x["n"] for x in result} != set(range(1, 101)):
        raise ValueError("The historical 100-idea ranking is incomplete")
    return result


def render():
    reg = json.loads(CAP.read_text(encoding="utf-8"))
    st = json.loads(STATUS.read_text(encoding="utf-8"))
    items = st["records"]
    lookup = {int(x["id"].rsplit("-", 1)[1]): x for x in items}
    if len(lookup) != len(items) or not set(lookup).issubset(set(range(1, 101))):
        raise ValueError("Duplicate or unknown IA source ID")
    cap_done, cap_pending, cap_review = [], [], []
    for c in reg["records"]:
        for app, state in c["app_states"].items():
            item = {
                "app": app, "id": c["id"], "title": c["title"],
                "score": c["score"], "ease": c["integration_ease_percent"][app],
                "state": state, "gate": c["next_gate"],
            }
            url = proven_cap(c, app, state)
            if url:
                item["url"] = url
                cap_done.append(item)
            elif state in VERIFIED or state in REPORTED:
                cap_review.append(item)
            else:
                cap_pending.append(item)
    sort_cap = lambda x: (-x["score"], -x["ease"], x["id"], x["app"])
    for arr in (cap_done, cap_pending, cap_review):
        arr.sort(key=sort_cap)

    idea_done, idea_pending, idea_review = [], [], []
    for idea in parse_ideas():
        status = lookup.get(idea["n"])
        if status:
            idea["state"] = status["state"]
            idea["app"] = status["app"]
            idea["url"] = status["evidence_url"]
            idea["scope"] = status["scope"]
            idea["gate"] = status["remaining_gate"]
        else:
            idea["state"] = "IDEA"
            idea["app"] = "-"
            idea["gate"] = "Valutare domanda, differenziazione, codice e rischio"
        if status and status["state"] == "INTEGRATED" and re.search(
                r"^https://github[.]com/riccardopinato/[^/]+/blob/[0-9a-f]{40}/", status["evidence_url"]):
            idea_done.append(idea)
        elif status and status["state"] in {"PARTIAL", "SOURCE_REPORTED", "INTEGRATED"}:
            idea_review.append(idea)
        else:
            idea_pending.append(idea)
    sort_idea = lambda x: (-x["score"], -x["ease"], x["n"])
    for arr in (idea_done, idea_pending, idea_review):
        arr.sort(key=sort_idea)

    def cap_link(x):
        return "[" + x["id"] + "](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/" + x["id"] + ".md) " + clean(x["title"])

    def idea_link(x):
        n = str(x["n"]).zfill(3)
        return "[#" + str(x["n"]) + "](11-NUOVE-IDEE/IA-2026-11-02/SCHEDE/IA26-" + n + ".md) " + clean(x["title"])

    def cap_rows(arr, done=False):
        return [[clean(x["app"]), cap_link(x), x["score"], str(x["ease"]) + "%",
                 clean(x["state"]), ("[codice](" + x["url"] + ")" if done else clean(x["gate"])[:125])]
                for x in arr]

    def idea_rows(arr, done=False):
        return [[idea_link(x), x["score"], str(x["ease"]) + "%",
                 clean(x["app"]), clean(x["state"]),
                 ("[codice](" + x["url"] + ")" if done else clean(x["gate"])[:125])]
                for x in arr]

    cap_headers = ["App", "Capability", "Priorità", "Facilità", "Stato", "Prova" ]
    pend_headers = ["App", "Capability", "Priorità", "Facilità", "Stato", "Prossimo gate"]
    idea_headers = ["Idea", "Priorità", "Facilità", "App correlata", "Stato", "Prova"]
    idea_pending_headers = ["Idea", "Priorità", "Facilità", "App correlata", "Stato", "Prossimo gate"]

    spotlight = [x for x in cap_pending if x["score"] >= 85 and x["ease"] >= 85]
    other = [x for x in cap_pending if x not in spotlight]
    remaining = (
        "# Da valutare — coda operativa App Factory\n\n"
        "> Generato da REGISTRO_CAPABILITY.json e dallo storico delle 100 idee. "
        "Non modifica alcuna roadmap o app. Snapshot dei dati del repository; "
        "non è una scansione live dei dispositivi.\n\n"
        "**Regola filtro:** priorità >=85 e facilità >=85 sono misurate **per singola app**. "
        "Elementi già confermati nel codice sono esclusi; elementi con sola prova "
        "documentale vanno in **Verifica stato**, non sono nuove implementazioni da suggerire.\n\n"
        "## Priorità alta: almeno 85/85 — da valutare (" + str(len(spotlight)) + ")\n\n"
        + table(pend_headers, cap_rows(spotlight)) + "\n"
        + "## Altre capability ancora da valutare (" + str(len(other)) + ")\n\n"
        + table(pend_headers, cap_rows(other)) + "\n"
        + "## Verificare lo stato prima di proporre sviluppo (" + str(len(cap_review)) + ")\n\n"
        + "Queste voci potrebbero essere **già in codice**. Non proporle come nuove feature "
        "finché non si controllano app, codice, SHA e test.\n\n"
        + table(pend_headers, cap_rows(cap_review)) + "\n"
        + "## Idee esterne non confermate integrate (" + str(len(idea_pending)) + ")\n\n"
        + "La priorità e la facilità seguenti provengono dal ranking **IA26** (metodo distinto dal CAP).\n\n"
        + table(idea_pending_headers, idea_rows(idea_pending)) + "\n"
        + "## Idee esterne parziali o con stato da verificare (" + str(len(idea_review)) + ")\n\n"
        + "Non riimplementare il nucleo esistente; risolvere prima il delta funzionale.\n\n"
        + table(idea_pending_headers, idea_rows(idea_review)) + "\n"
        + "[Già integrati](GIA_INTEGRATI.md) · "
        "[Classifica storica CAP](12-CAPABILITY-E-IMPLEMENTAZIONI/CLASSIFICA_PRIORITA.md) · "
        "[Ranking storico 100 idee](11-NUOVE-IDEE/IA-2026-11-02/RANKING_100_COMPLETO.md)\n"
    )
    done = (
        "# Già integrati — archivio delle implementazioni confermate\n\n"
        "> Esclusi automaticamente da DA_VALUTARE per la stessa app. "
        "CI verificata non significa prova fisica né pubblicazione Play. "
        "La stessa capability può essere integrata in un'app e ancora proposta in un'altra.\n\n"
        + "## Capability con prova di codice puntuale (" + str(len(cap_done)) + ")\n\n"
        + table(cap_headers, cap_rows(cap_done, done=True)) + "\n"
        + "## Idee IA26 con funzione equivalente già in codice (" + str(len(idea_done)) + ")\n\n"
        + table(idea_headers, idea_rows(idea_done, done=True)) + "\n"
        + "Le integrazioni **parziali** non sono conteggiate come completate: "
        "sono riportate in [Da valutare, sezione verifica](DA_VALUTARE.md).\n\n"
        + "[Da valutare](DA_VALUTARE.md) · "
        "[Stato tecnico originario](12-CAPABILITY-E-IMPLEMENTAZIONI/STATO_IMPLEMENTAZIONI.md)\n"
    )
    return {"DA_VALUTARE.md": remaining, "GIA_INTEGRATI.md": done}


def main(check=None):
    if check is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("--check", action="store_true")
        check = parser.parse_args().check
    rendered = render()
    mismatches = []
    for name, contents in rendered.items():
        p = ROOT / name
        if check:
            if not p.exists() or p.read_text(encoding="utf-8") != contents:
                mismatches.append(name)
        else:
            p.write_text(contents, encoding="utf-8")
    if mismatches:
        raise SystemExit("Operational views drift: " + ", ".join(mismatches))
    print("STATUS_VIEWS_VALID: " + ", ".join(rendered))


if __name__ == "__main__":
    main()
