#!/usr/bin/env python3
"""Project-safe import *proposal* from AppLab's reviewed REA research output.

Never writes canonical records, never allocates CAP IDs, E3/E5 or Golden status.
The review's source/evidence must be checked by AppLab before this step.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHA40 = re.compile(r"^[a-f0-9]{40}$")
SHA64 = re.compile(r"^[a-f0-9]{64}$")
DECISIONS = {"ADOPT_CANDIDATE", "REFERENCE_ONLY", "DEFER", "REJECT"}


def route(report: dict) -> dict:
    if (report.get("schema_version") != 1
            or report.get("report_type") != "REA_DONOR_RESEARCH_DECISIONS"
            or report.get("classification") != "E1_RESEARCH_REVIEW_PENDING_CATALOG_PR"
            or report.get("catalog_mutated") is not False
            or report.get("certified_donors") != 0
            or report.get("golden_promoted") is not False
            or report.get("execution_of_target") != "NONE"):
        raise ValueError("Unreviewed or falsely certified REA report")
    repository = report.get("source_repository")
    source_sha = report.get("source_sha")
    target_sha = report.get("target_sha256")
    if (not isinstance(repository, str) or repository.count("/") != 1
            or not SHA40.fullmatch(str(source_sha or ""))
            or not SHA64.fullmatch(str(target_sha or ""))):
        raise ValueError("Missing immutable source/artifact identity")
    rows = report.get("findings")
    if not isinstance(rows, list) or len(rows) > 100:
        raise ValueError("Invalid bounded finding rows")
    reviewed = []
    ids = set()
    for index, finding in enumerate(rows, start=1):
        if not isinstance(finding, dict) or finding.get("decision") not in DECISIONS:
            raise ValueError("Invalid source-review decision")
        ident = finding.get("id")
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Za-z0-9_.:-]{2,72}", ident) or ident in ids:
            raise ValueError("Duplicate or invalid discovery ID")
        ids.add(ident)
        source_comparison = finding.get("source_comparison")
        rights = finding.get("rights")
        if source_comparison not in ("NEW_BEYOND_SOURCE","ALREADY_IN_SOURCE","CONFLICT","NOT_VERIFIED") or rights not in ("AUTHORIZED_FOR_RESEARCH","INCOMPATIBLE_FOR_COPY","REVIEW_REQUIRED"):
            raise ValueError("Invalid evidence/license classification")
        decision = finding["decision"]
        if decision == "ADOPT_CANDIDATE" and (source_comparison != "NEW_BEYOND_SOURCE" or rights != "AUTHORIZED_FOR_RESEARCH"):
            raise ValueError("ADOPT_CANDIDATE requires new, authorized discovery")
        if not isinstance(finding.get("reason"), str) or len(finding["reason"]) < 12:
            raise ValueError("Insufficient source comparison explanation")
        reviewed.append({
            "research_candidate_id": f"REI-{target_sha[:12]}-{index:03d}",
            "external_id": ident,
            "decision": decision,
            "source_comparison": source_comparison,
            "license_status": rights,
            "reason": finding["reason"],
            "evidence_operation": finding.get("evidence_operation"),
            "admission": "E1_RESEARCH_ONLY",
            "requires_ordinary_catalog_pr": decision == "ADOPT_CANDIDATE",
        })
    return {
        "schema_version": 1, "type": "REA_CATALOG_INTAKE_PROPOSAL",
        "factory_golden_id": "rea_cli_reverse_intelligence",
        "factory_golden_scope": "COPY_READY_PROCESS_ONLY",
        "donor_certified": False, "golden_certified": False,
        "automatic_write": False, "source_repository": repository,
        "source_sha": source_sha, "artifact_sha256": target_sha,
        "findings": reviewed,
        "candidate_count": sum(x["decision"] == "ADOPT_CANDIDATE" for x in reviewed),
        "state": "READY_FOR_HUMAN_OR_IA_REVIEW_AND_BRANCH_PR_NOT_ADMITTED",
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--review-json", required=True, type=Path)
    args = p.parse_args()
    try:
        path = args.review_json
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 2 * 1024 * 1024:
            raise ValueError("Review must be a bounded regular local file")
        report = json.loads(path.read_text(encoding="utf-8"))
        result = route(report)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("REA CATALOG ROUTING BLOCKED: " + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
