#!/usr/bin/env python3
"""Parse actual flutter test benchmark output. Never estimate missing timings."""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path

PREFIX = "WORLD_DAYS_BENCH|"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--markdown", type=Path, required=True)
    ap.add_argument("--dataset", type=Path)
    args = ap.parse_args()
    log = args.log.read_text(encoding="utf-8", errors="replace")
    rows = []
    for line in log.splitlines():
        if PREFIX not in line:
            continue
        data = json.loads(line.split(PREFIX, 1)[1])
        rows.append(data)
    expected = {(page, n) for page in ("saved", "around_the_world")
                for n in (10, 50, 150, 300)}
    found = {(row["page"], row["scenario_record_count"]) for row in rows}
    complete = found == expected and len(rows) == len(expected)
    dataset = {}
    if args.dataset and args.dataset.is_file():
        dataset = json.loads(args.dataset.read_text(encoding="utf-8"))
    payload = {
        "schema_version": 1,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "benchmark_type": "real World Days page widget-test pump time",
        "is_device_performance": False,
        "is_release_profile": False,
        "scenario_complete": complete,
        "expected": len(expected),
        "observed": len(rows),
        "dataset": dataset,
        "rows": sorted(rows, key=lambda x: (x["page"], x["scenario_record_count"])),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# World Days — benchmark widget di due liste",
        "",
        "Fonte: widget reali SavedPage e AroundTheWorldPage montati in test Flutter",
        "Motore: Flutter widget test CI (Linux), viewport 390x844 logici.",
        "Misura: wall-clock pumpWidget+pump, 2 warmup + 7 sample, mediana e p95.",
        "NON misura frame GPU su telefono, RAM fisica, scroll reale o successo Store.",
        "",
        "| Pagina | Record sintetici | Child delegate | Card montate | Mediana ms | P95 ms |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in payload["rows"]:
        lines.append("| {page} | {scenario_record_count} | {list_delegate_total_children} | {mounted_visible_observance_cards} | {median_pump_ms} | {p95_pump_ms} |".format(**row))
    if dataset:
        lines.extend(["", "## Dataset distribuito (contesto reale)", "",
                      "Record totali: " + str(dataset.get("total_records")),
                      "Paesi: " + json.dumps(dataset.get("country_counts", {}), ensure_ascii=False)])
    lines.extend(["", "Completezza dei 8 scenari: " + str(complete),
                  "I campioni sintetici aumentano la pressione per rilevare scaling; non descrivono il volume per-pagina dell'utente.",
                  "Ogni correzione richiede test comparativo prima/dopo a identico SHA, SDK e runner."])
    args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("WORLD_DAYS_BENCH_SUMMARY|" + json.dumps({
        "scenario_complete": complete, "rows": len(rows),
        "results": [{k: v for k, v in row.items()
                     if k in ("page", "scenario_record_count", "median_pump_ms",
                              "p95_pump_ms", "list_delegate_total_children")}
                    for row in payload["rows"]],
    }, ensure_ascii=False), flush=True)
    return 0 if complete else 1

if __name__ == "__main__":
    raise SystemExit(main())
