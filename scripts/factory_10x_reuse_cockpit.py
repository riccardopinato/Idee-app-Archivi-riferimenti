#!/usr/bin/env python3
"""X10-044: offline, review-only priority ranking over X10-043 proposals.

All inputs must be acquired from authenticated pinned GitHub sources by caller.
Rankings are hypotheses for human triage, not permission to integrate code.
No network, CAP/Golden write, release, hidden approval or CI authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

SHA40 = re.compile(r"^[a-f0-9]{40}$")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
CAP = re.compile(r"^CAP-[0-9]{4,}$")
REPO = re.compile(r"^riccardopinato/[A-Za-z0-9_.-]+$")
BLOCKED_STATES = {"BLOCKED_PENDING_REVIEW", "SCOPED_REVIEW_RECORDED"}
# X10-043.prepare() emits these codes. Unknown future codes must not
# disappear silently: update this adapter and its regression fixtures first.
UPSTREAM_CODES = frozenset({
    "CANDIDATE_STALE", "CANDIDATE_BLOCKED", "HUMAN_REJECTED", "HUMAN_DEFERRED",
    "INDEPENDENT_REVIEW_PROVENANCE_NOT_VERIFIED",
})
HARD_BLOCK = frozenset({"CANDIDATE_BLOCKED", "HUMAN_REJECTED"})
UPSTREAM_STALE = frozenset({"CANDIDATE_STALE"})
REVIEW_UNVERIFIED = frozenset({"INDEPENDENT_REVIEW_PROVENANCE_NOT_VERIFIED"})


class CockpitError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise CockpitError(message)


def _score_number(value: object, label: str) -> int:
    _require(type(value) is int and 0 <= value <= 5, "INVALID_SCORE_" + label)
    return value


def _snapshot(inventory: dict[str, Any]) -> dict[str, dict[str, Any]]:
    _require(isinstance(inventory, dict) and inventory.get("schema_version") == 1
             and isinstance(inventory.get("repositories"), list),
             "INVALID_INVENTORY")
    indexed = {}
    for row in inventory["repositories"]:
        _require(isinstance(row, dict)
                 and isinstance(row.get("name"), str) and row["name"].strip()
                 and "/" not in row["name"]
                 and isinstance(row.get("head_sha"), str)
                 and SHA40.fullmatch(row["head_sha"]) is not None,
                 "INVALID_REPO_INVENTORY_ROW")
        key = row["name"].casefold()
        _require(key not in indexed, "DUPLICATE_INVENTORY_REPO")
        indexed[key] = row
    return indexed


def rank(
    proposals: list[dict[str, Any]],
    estimates: list[dict[str, Any]],
    inventory: dict[str, Any],
    *,
    factory_sha: str,
    observed_on: str,
) -> dict[str, Any]:
    """Calculate review ordering without changing any evidence level.

    A high score never removes legal, product, stale source or review gates.
    No individual estimate is treated as validated market demand.
    """
    _require(isinstance(proposals, list) and isinstance(estimates, list)
             and len(proposals) <= 100 and len(estimates) <= 100,
             "INVALID_COCKPIT_INPUT")
    _require(isinstance(factory_sha, str) and SHA40.fullmatch(factory_sha) is not None
             and isinstance(observed_on, str)
             and re.fullmatch(r"\d{4}-\d{2}-\d{2}", observed_on) is not None,
             "INVALID_CHECKPOINT")
    indexed = _snapshot(inventory)
    by_id = {}
    for estimate in estimates:
        _require(isinstance(estimate, dict)
                 and isinstance(estimate.get("candidate_id"), str)
                 and estimate["candidate_id"].startswith("x10_")
                 and len(estimate["candidate_id"]) <= 80,
                 "INVALID_ESTIMATE")
        cid = estimate["candidate_id"]
        _require(cid not in by_id, "DUPLICATE_ESTIMATE")
        _require(isinstance(estimate.get("assumptions"), str)
                 and 15 <= len(estimate["assumptions"].strip()) <= 500,
                 "MISSING_ESTIMATE_RATIONALE")
        for key in ("impact", "cross_app_reuse", "evidence", "risk", "effort"):
            _score_number(estimate.get(key), key.upper())
        dependencies = estimate.get("dependencies")
        _require(isinstance(dependencies, list) and len(dependencies) <= 12
                 and all(isinstance(x, str) and 1 <= len(x) <= 100 for x in dependencies),
                 "INVALID_DEPENDENCIES")
        _require(len(dependencies) == len(set(dependencies)),
                 "DUPLICATE_DEPENDENCIES")
        by_id[cid] = estimate

    seen = set()
    results = []
    for p in proposals:
        _require(isinstance(p, dict) and p.get("schema_version") == 1
                 and p.get("record_type") == "X10_043_SUPERVISED_REUSE_PROPOSAL"
                 and p.get("authority") == "ADVISORY_ONLY"
                 and p.get("automatic_code_change") is False
                 and p.get("automatic_merge") is False
                 and p.get("golden_promotion") is False
                 and p.get("consumer_runtime_verified") is False
                 and p.get("requires_scoped_pr") is True
                 and p.get("independent_consumer_ci_required") is True,
                 "UNTRUSTED_SEMANTIC_PROPOSAL")
        cid, cap = p.get("candidate_id"), p.get("cap_id")
        src, dst = p.get("producer_repo"), p.get("consumer_repo")
        srcsha, dstsha = p.get("producer_sha"), p.get("consumer_sha")
        _require(isinstance(cid, str) and cid.startswith("x10_") and len(cid) <= 80
                 and isinstance(cap, str) and CAP.fullmatch(cap) is not None
                 and all(isinstance(repo, str) and REPO.fullmatch(repo) is not None
                         for repo in (src, dst))
                 and all(isinstance(sha, str) and SHA40.fullmatch(sha) is not None
                         for sha in (srcsha, dstsha))
                 and isinstance(p.get("source_path_sha256"), str)
                 and SHA256.fullmatch(p["source_path_sha256"]) is not None
                 and p.get("review_state") in BLOCKED_STATES
                 and type(p.get("approval_verified")) is bool
                 and isinstance(p.get("review_fingerprint"), str)
                 and SHA256.fullmatch(p["review_fingerprint"]) is not None,
                 "PROPOSAL_PROVENANCE_MISSING")
        _require((p["review_state"] == "SCOPED_REVIEW_RECORDED")
                 == p["approval_verified"], "INCOHERENT_REVIEW_STATE")
        upstream = p.get("reason_codes")
        _require(isinstance(upstream, list) and len(upstream) <= len(UPSTREAM_CODES)
                 and all(isinstance(code, str) and code in UPSTREAM_CODES
                         for code in upstream)
                 and len(set(upstream)) == len(upstream),
                 "UNKNOWN_OR_INVALID_UPSTREAM_REASONS")
        _require(not (p["review_state"] == "SCOPED_REVIEW_RECORDED" and upstream),
                 "REVIEW_APPROVAL_CONTRADICTS_UPSTREAM_REASONS")
        _require(cid not in seen, "DUPLICATE_PROPOSAL")
        seen.add(cid)
        assessment = by_id.get(cid)
        _require(assessment is not None, "MISSING_ASSESSMENT")
        producer = indexed.get(src.split("/", 1)[1].casefold())
        consumer = indexed.get(dst.split("/", 1)[1].casefold())
        # Preserve the exact X10-043 source-side blockers, even if a newer
        # inventory snapshot happens to match both current source SHAs.
        reasons = list(upstream)
        if producer is None or producer["head_sha"] != srcsha:
            reasons.append("PRODUCER_SOURCE_STALE_OR_UNKNOWN")
        elif producer.get("head_observed_at") != observed_on:
            reasons.append("PRODUCER_OBSERVATION_STALE")
        if consumer is None or consumer["head_sha"] != dstsha:
            reasons.append("CONSUMER_SOURCE_STALE_OR_UNKNOWN")
        elif consumer.get("head_observed_at") != observed_on:
            reasons.append("CONSUMER_OBSERVATION_STALE")
        if p["review_state"] != "SCOPED_REVIEW_RECORDED":
            reasons.append("HUMAN_REVIEW_PENDING")
        if assessment["dependencies"]:
            reasons.append("UNRESOLVED_DEPENDENCIES")
        if assessment["risk"] >= 4:
            reasons.append("HIGH_RISK_REVIEW")
        # Ordinal triage score. No unit of time, money or probability.
        priority = (4 * assessment["impact"]
                    + 3 * assessment["cross_app_reuse"]
                    + 2 * assessment["evidence"]
                    - 3 * assessment["risk"]
                    - 2 * assessment["effort"]
                    - 2 * len(assessment["dependencies"]))
        # A reviewed or high-score estimate cannot rehabilitate a donor
        # rejected by the owner or blocked by its upstream CAP provenance.
        if HARD_BLOCK.intersection(upstream):
            state = "BLOCKED_UPSTREAM"
            next_action = "HONOR_REJECTION_OR_RESOLVE_CAP_BLOCKER"
        elif UPSTREAM_STALE.intersection(upstream):
            state = "STALE_RECHECK"
            next_action = "RECHECK_UPSTREAM_CAP_SOURCE_AND_FACTORY"
        elif REVIEW_UNVERIFIED.intersection(upstream):
            state = "BLOCKED_REVIEW_PROVENANCE"
            next_action = "VERIFY_INDEPENDENT_REVIEW_PROVENANCE"
        elif any("STALE" in x or "UNKNOWN" in x for x in reasons):
            state = "STALE_RECHECK"
            next_action = "REFRESH_PINNED_INVENTORY"
        else:
            state = "REVIEW_BACKLOG"
            next_action = "HUMAN_SCOPE_AND_LICENSE_REVIEW"
        results.append({
            "candidate_id": cid, "cap_id": cap,
            "producer_repo": src, "producer_sha": srcsha,
            "consumer_repo": dst, "consumer_sha": dstsha,
            "review_fingerprint": p["review_fingerprint"],
            "triage_score": priority,
            "score_kind": "UNVERIFIED_RELATIVE_ESTIMATE",
            "state": state,
            "reason_codes": reasons,
            "dependencies": list(assessment["dependencies"]),
            "estimate_factors": {key: assessment[key] for key in
                                 ("impact", "cross_app_reuse", "evidence", "risk", "effort")},
            "assumptions_sha256": hashlib.sha256(
                assessment["assumptions"].encode("utf-8")).hexdigest(),
            "recommended_next_action": next_action,
            "automatic_adoption": False,
            "license_verified_by_cockpit": False,
            "product_approved_by_cockpit": False,
            "consumer_ci_verified_by_cockpit": False,
        })
    _require(len(by_id) == len(seen), "UNMATCHED_ASSESSMENT")
    # Only normal review backlog can rank ahead of upstream stale, denied,
    # or unverifiable candidates. Score NEVER overrides a hard blocker.
    state_order = {
        "REVIEW_BACKLOG": 0, "STALE_RECHECK": 1,
        "BLOCKED_REVIEW_PROVENANCE": 2, "BLOCKED_UPSTREAM": 3,
    }
    results.sort(key=lambda item: (state_order[item["state"]],
                                   -item["triage_score"], item["cap_id"],
                                   item["consumer_repo"], item["candidate_id"]))
    for i, item in enumerate(results):
        item["review_queue_position"] = i + 1
    return {
        "schema_version": 1,
        "record_type": "X10_044_REUSE_REVIEW_COCKPIT",
        "factory_sha": factory_sha,
        "inventory_updated_at": inventory.get("updated_at"),
        "observed_on": observed_on,
        "authority": "ADVISORY_ONLY",
        "input_proposals": len(proposals),
        "ranked": results,
        "automatic_pr_created": False,
        "consumer_writes_performed": False,
        "golden_promotion_performed": False,
        "runtime_verified": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposals", required=True, type=Path)
    parser.add_argument("--estimates", required=True, type=Path)
    parser.add_argument("--inventory", required=True, type=Path)
    parser.add_argument("--factory-sha", required=True)
    parser.add_argument("--observed-on", required=True)
    args = parser.parse_args()
    output = rank(json.loads(args.proposals.read_text(encoding="utf-8")),
                  json.loads(args.estimates.read_text(encoding="utf-8")),
                  json.loads(args.inventory.read_text(encoding="utf-8")),
                  factory_sha=args.factory_sha, observed_on=args.observed_on)
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
