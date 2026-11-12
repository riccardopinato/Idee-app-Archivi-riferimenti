#!/usr/bin/env python3
"""X10-042: deterministic CAP-ID lookup for X10-041 hashed source hints.

Never creates IDs, promotes status, downloads donor code or changes consumers.
Only records from the existing REGISTRO_CAPABILITY are eligible for matches.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any

CAP = re.compile(r"^CAP-[0-9]{4,}$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
IMPLEMENTED = {"SOURCE_CONFIRMED", "CI_VERIFIED", "DEVICE_VERIFIED", "RELEASE"}
KNOWN_STATES = IMPLEMENTED | {"PROPOSTA", "ROADMAP_STORICA", "SOURCE_REPORTED",
                              "DONOR_REPORTED", "BLOCKED"}
REPO_PREFIX = "riccardopinato/"


class DedupError(ValueError):
    pass


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=True).encode("ascii")).hexdigest()


def _require(ok: bool, reason: str) -> None:
    if not ok:
        raise DedupError(reason)


def join(
    monitor: dict[str, Any], registry: dict[str, Any], inventory: dict[str, Any], *,
    factory_sha: str, observed_on: str,
) -> dict[str, Any]:
    """Inputs must be loaded from pinned, trusted GitHub sources by caller."""
    _require(all(isinstance(x, dict) for x in (monitor, registry, inventory)), "INVALID_INPUT")
    _require(monitor.get("record_type") == "X10_041_DIFF_HINTS"
             and monitor.get("authority") == "ADVISORY_ONLY"
             and monitor.get("source_code_copied") is False
             and monitor.get("automated_pr_created") is False,
             "UNTRUSTED_MONITOR")
    source_repo, source_sha = monitor.get("repository"), monitor.get("head_sha")
    _require(isinstance(source_repo, str) and source_repo.startswith(REPO_PREFIX)
             and isinstance(source_sha, str) and SHA40.fullmatch(source_sha) is not None
             and isinstance(monitor.get("monitor_key"), str)
             and SHA256.fullmatch(monitor["monitor_key"]) is not None,
             "MONITOR_IDENTITY_INVALID")
    _require(isinstance(factory_sha, str) and SHA40.fullmatch(factory_sha) is not None
             and isinstance(observed_on, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", observed_on) is not None,
             "TRUSTED_EPOCH_INVALID")
    _require(registry.get("schema_version") == 1 and isinstance(registry.get("records"), list)
             and inventory.get("schema_version") == 1
             and isinstance(inventory.get("repositories"), list), "SOURCE_SCHEMA_INVALID")
    signals = monitor.get("signals")
    _require(isinstance(signals, list) and len(signals) <= 30
             and all(isinstance(row, dict) and
                     isinstance(row.get("path_sha256"), str)
                     and SHA256.fullmatch(row["path_sha256"]) is not None
                     and isinstance(row.get("signals"), list) for row in signals),
             "INVALID_MONITOR_HINTS")
    target_hashes = {row["path_sha256"] for row in signals}
    _require(len(target_hashes) == len(signals), "DUPLICATE_HASHED_PATH_HINT")
    snap = {}
    for row in inventory["repositories"]:
        _require(isinstance(row, dict) and isinstance(row.get("name"), str)
                 and isinstance(row.get("head_sha"), str)
                 and SHA40.fullmatch(row["head_sha"]) is not None,
                 "INVENTORY_RECORD_INVALID")
        name = row["name"].casefold()
        _require(name not in snap, "DUPLICATE_INVENTORY_REPO")
        snap[name] = row
    producer = snap.get(source_repo.split("/", 1)[1].casefold())
    _require(producer is not None, "PRODUCER_NOT_IN_INVENTORY")
    producer_current = (producer["head_sha"] == source_sha
                        and producer.get("head_observed_at") == observed_on)
    factory_fresh = registry.get("factory_baseline") == REPO_PREFIX + "App-Factory-Core@" + factory_sha
    index = set()
    found = []
    for cap in registry["records"]:
        _require(isinstance(cap, dict) and isinstance(cap.get("id"), str)
                 and CAP.fullmatch(cap["id"]) is not None, "INVALID_CAP_ID")
        _require(cap["id"] not in index, "DUPLICATE_CAP_ID")
        index.add(cap["id"])
        evidence = cap.get("implementation_evidence", {})
        _require(isinstance(evidence, dict), "INVALID_CAP_EVIDENCE")
        source_entry = None
        for name, ref in evidence.items():
            if not isinstance(name, str) or not isinstance(ref, dict):
                continue
            if name.casefold() == source_repo.split("/", 1)[1].casefold():
                source_entry = ref
                break
        if not source_entry:
            continue
        path = source_entry.get("source_path")
        sha = source_entry.get("source_sha")
        if not isinstance(path, str) or not path or digest(["path", path]) not in target_hashes:
            continue
        _require(isinstance(sha, str) and SHA40.fullmatch(sha) is not None,
                 "CAP_SOURCE_PROVENANCE_INVALID")
        path_hash = digest(["path", path])
        states = cap.get("app_states", {})
        _require(isinstance(states, dict), "CAP_APP_STATES_INVALID")
        for app, state in sorted(states.items()):
            _require(isinstance(app, str) and bool(app.strip())
                     and isinstance(state, str) and state in KNOWN_STATES,
                     "CAP_CONSUMER_STATE_INVALID")
            if state in IMPLEMENTED:
                continue
            if app.casefold() == source_repo.split("/", 1)[1].casefold():
                continue
            consumer = snap.get(app.casefold())
            # Never silently guess the target HEAD from an old historical URL.
            if consumer is None:
                continue
            consumer_sha = consumer["head_sha"]
            reason = []
            if not producer_current:
                reason.append("PRODUCER_INVENTORY_STALE")
            if source_sha != sha:
                reason.append("CAP_SOURCE_SHA_DIFFERS")
            if not factory_fresh:
                reason.append("CAP_REGISTRY_FACTORY_BASELINE_STALE")
            if consumer.get("head_observed_at") != observed_on:
                reason.append("CONSUMER_INVENTORY_STALE")
            if state == "BLOCKED":
                reason.append("RECORDED_CONSUMER_BLOCKER")
            identity = [source_repo.casefold(), source_sha, cap["id"],
                        (REPO_PREFIX + app).casefold(), consumer_sha, "REVIEW_REUSE"]
            found.append({
                "candidate_id": "x10_" + digest(identity)[:24],
                "cap_id": cap["id"], "producer_repo": source_repo,
                "producer_sha": source_sha, "source_path_sha256": path_hash,
                "consumer_repo": REPO_PREFIX + app, "consumer_inventory_sha": consumer_sha,
                "consumer_state_recorded": state,
                "status": "BLOCKED" if state == "BLOCKED" else
                          "STALE" if reason else "NEEDS_REVIEW",
                "reason_codes": sorted(reason), "requires_license_review": True,
                "requires_product_owner_approval": True,
                "automatic_adoption": False, "ci_verified_this_run": False,
            })
    ids = [c["candidate_id"] for c in found]
    _require(len(ids) == len(set(ids)), "DUPLICATE_CANDIDATE_ID")
    found.sort(key=lambda x: (x["cap_id"], x["consumer_repo"]))
    return {"schema_version": 1, "record_type": "X10_CAP_REUSE_DEDUP_PROPOSALS",
            "authority": "ADVISORY_ONLY", "factory_sha": factory_sha,
            "monitor_key": monitor["monitor_key"], "registry_updated_at": registry.get("updated_at"),
            "inventory_updated_at": inventory.get("updated_at"),
            "observed_on": observed_on, "candidates": found,
            "new_cap_ids_created": 0, "consumer_writes_performed": False,
            "golden_promotion_performed": False, "runtime_verified": False}
