#!/usr/bin/env python3
"""Offline, privacy-safe KPI contract validator. No fake baseline or calculated 10x claims."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "19-APP-FACTORY-10X/data/METRICS_LEDGER_v1.json"
IDS = {
    "verified_features_per_week", "lead_time_hours",
    "manual_interventions_per_feature", "reuse_ratio",
    "qa_regressions_escaped", "pilot_retention_d30",
    "net_revenue_per_product", "agent_job_success_recovery",
}
SHA = re.compile(r"^[0-9a-f]{40}$")


def validate(data: dict) -> dict:
    if data.get("schema_version") != 1 or data.get("program_id") != "APP_FACTORY_10X_2026":
        raise ValueError("Invalid 10x metrics schema")
    if not SHA.fullmatch(str(data.get("factory_baseline_sha", ""))):
        raise ValueError("Missing Factory baseline SHA")
    if not str(data.get("canonical_delivery_ledger", "")).startswith(
        "https://github.com/riccardopinato/App-Factory-Core/blob/"
    ):
        raise ValueError("PR elapsed lifecycle must use canonical v27 ledger")
    metrics = data.get("metrics", [])
    if not isinstance(metrics, list) or {m["id"] for m in metrics} != IDS or len(metrics) != len(IDS):
        raise ValueError("Metric registry mismatch")
    count = 0
    for metric in metrics:
        if not metric.get("unit") or not metric.get("definition") or not metric.get("acceptance"):
            raise ValueError("Missing metric contract")
        baseline = metric.get("baseline")
        if not isinstance(baseline, dict):
            raise ValueError("Missing metric baseline")
        if baseline.get("status") == "NOT_MEASURED":
            if baseline.get("value") is not None:
                raise ValueError("NOT_MEASURED cannot contain invented numeric baseline")
        elif baseline.get("status") != "REVIEWED":
            raise ValueError("Unknown baseline status")
        if baseline["status"] == "REVIEWED":
            if not isinstance(baseline.get("value"), (int, float)) or isinstance(baseline.get("value"), bool):
                raise ValueError("Baseline value requires numeric evidence")
            if not baseline.get("source_url") or not str(baseline["source_url"]).startswith("https://"):
                raise ValueError("Baseline must be source-backed")
            if not SHA.fullmatch(str(baseline.get("source_sha", ""))):
                raise ValueError("Baseline must pin commit")
        seen = set()
        samples = metric.get("observations")
        if not isinstance(samples, list):
            raise ValueError("Observations must be list")
        if metric["id"] == "net_revenue_per_product" and samples:
            raise ValueError("Public repo must not store financial provider observations")
        for row in samples:
            if not isinstance(row, dict):
                raise ValueError("Bad observation")
            if not row.get("gate_reviewed") is True:
                raise ValueError("No unreviewed observed KPI")
            if not SHA.fullmatch(str(row.get("source_sha", ""))):
                raise ValueError("KPI receipt missing exact source SHA")
            if not str(row.get("source_url", "")).startswith("https://github.com/"):
                raise ValueError("Only GitHub source-linked receipts in public registry")
            if not isinstance(row.get("value"), (int, float)) or isinstance(row.get("value"), bool):
                raise ValueError("KPI must be numeric")
            if row["value"] < 0:
                raise ValueError("Negative KPI unsupported")
            if metric["unit"] == "share" and row["value"] > 1:
                raise ValueError("Ratios must be in [0,1]")
            if not row.get("cohort") or not row.get("period"):
                raise ValueError("No cohort/period definition")
            try:
                datetime.fromisoformat(str(row.get("checked_at", "")).replace("Z", "+00:00"))
            except ValueError as exc:
                raise ValueError("Timestamp required") from exc
            if not str(row["checked_at"]).endswith("Z"):
                raise ValueError("Timestamp must be UTC Z")
            key = (row["cohort"], row["period"], row["source_sha"])
            if key in seen:
                raise ValueError("Duplicate KPI sample")
            seen.add(key)
            count += 1
        if metric.get("assurance") == "VERIFIED" and not samples:
            raise ValueError("Cannot attest measurement without reviewed samples")
    return {"metrics": len(metrics), "verified_samples": count, "unmeasured": sum(
        m["baseline"]["status"] == "NOT_MEASURED" for m in metrics
    )}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    doc = json.loads(LEDGER.read_text(encoding="utf-8"))
    result = validate(doc)
    if args.summary:
        print("App Factory 10x — KPI evidence ledger (no automatic measurement)")
        for m in doc["metrics"]:
            print(f'{m["id"]}: {m["baseline"]["status"]} / {len(m["observations"])} reviewed samples')
    else:
        print("APP_FACTORY_10X_METRICS_CHECK_PASS " + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
