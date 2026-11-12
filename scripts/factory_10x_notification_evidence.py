#!/usr/bin/env python3
"""X10-023: inspect an externally collected Android notification QA dossier.

This is an *untrusted claim-format validator*, NOT a device attestor.
A locally authored JSON file, even with hashes and PASS claims, cannot
certify actual OS notifications or delivery. Independent external AppLab
verification and physical device execution remain mandatory.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SHA = re.compile(r"^[a-f0-9]{40}$")
HASH = re.compile(r"^[a-f0-9]{64}$")
PACKAGE = re.compile(r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$")
SCENARIOS = (
    "PERMISSION_DENIED", "PERMISSION_GRANTED",
    "REMINDER_CHANNEL_ENABLED", "REMINDER_CHANNEL_BLOCKED",
    "EXACT_ALARM_ALLOWED", "EXACT_DENIED_USER_CHOSEN_FALLBACK",
    "IMMEDIATE_NOTIFICATION_VISIBLE", "SCHEDULED_ALARM_REGISTERED",
    "SCHEDULED_NOTIFICATION_DELIVERED", "STABLE_REMINDER_ID",
    "EDIT_REPLACES_ALARM", "DELETE_CANCELS_ALARM",
    "PAST_TIME_NOT_SCHEDULED", "IANA_TIMEZONE_RESOLVED",
    "REBOOT_RECONCILIATION", "COLD_START_TAP_ROUTE",
    "CORE_DATA_SAVED_ON_SCHEDULE_ERROR",
    "SIGNED_RELEASE_IDENTITY",
)
RESULTS = frozenset({"PASS", "FAIL", "BLOCKED", "NOT_VERIFIED"})
PHYSICAL = frozenset({
    "IMMEDIATE_NOTIFICATION_VISIBLE", "SCHEDULED_NOTIFICATION_DELIVERED",
    "REBOOT_RECONCILIATION", "COLD_START_TAP_ROUTE",
})
REQUIRED_PROOFS = frozenset({"screenshot", "video", "log", "trace"})
MAX_BYTES = 128_000


class EvidenceContractError(ValueError):
    pass


def require(condition: bool, code: str) -> None:
    if not condition:
        raise EvidenceContractError(code)


def nonempty(value: object, max_length: int = 160) -> bool:
    return isinstance(value, str) and bool(value.strip()) and len(value) <= max_length


def classify(record: dict[str, Any], *, expected_source_sha: str) -> dict[str, Any]:
    require(isinstance(record, dict)
            and record.get("schema_version") == 1
            and record.get("record_type") == "X10_023_ANDROID_NOTIFICATION_QA_DOSSIER",
            "INVALID_SCHEMA")
    require(isinstance(expected_source_sha, str)
            and SHA.fullmatch(expected_source_sha) is not None,
            "INVALID_EXPECTED_SOURCE")
    identity = record.get("identity")
    require(isinstance(identity, dict), "MISSING_IDENTITY")
    repo = identity.get("repository")
    require(nonempty(repo, 120) and repo.startswith("riccardopinato/")
            and repo.count("/") == 1,
            "INVALID_REPOSITORY")
    require(identity.get("source_sha") == expected_source_sha,
            "UNPINNED_OR_MISMATCHED_SOURCE")
    require(isinstance(identity.get("artifact_sha256"), str)
            and HASH.fullmatch(identity["artifact_sha256"]) is not None
            and isinstance(identity.get("version_code"), int)
            and type(identity["version_code"]) is int
            and identity["version_code"] > 0
            and isinstance(identity.get("package_id"), str)
            and PACKAGE.fullmatch(identity["package_id"]) is not None,
            "INVALID_ARTIFACT_IDENTITY")
    device = record.get("device")
    require(isinstance(device, dict)
            and device.get("platform") == "Android"
            and nonempty(device.get("manufacturer"), 80)
            and nonempty(device.get("model"), 80)
            and nonempty(device.get("os_build"), 120)
            and type(device.get("sdk_int")) is int
            and 23 <= device["sdk_int"] <= 99,
            "INVALID_DEVICE_IDENTITY")
    claims = record.get("scenarios")
    require(isinstance(claims, list) and len(claims) <= 40, "INVALID_SCENARIO_LIST")
    observed: dict[str, str] = {}
    for row in claims:
        require(isinstance(row, dict) and row.get("id") in SCENARIOS
                and row["id"] not in observed and row.get("result") in RESULTS,
                "INVALID_OR_DUPLICATE_SCENARIO")
        scenario, state = row["id"], row["result"]
        proofs = row.get("proofs", [])
        require(isinstance(proofs, list) and len(proofs) <= 4,
                "INVALID_PROOFS")
        require(state != "PASS" or bool(proofs),
                "PASS_WITHOUT_PROOF")
        for proof in proofs:
            require(isinstance(proof, dict)
                    and proof.get("kind") in REQUIRED_PROOFS
                    and isinstance(proof.get("sha256"), str)
                    and HASH.fullmatch(proof["sha256"]) is not None
                    and nonempty(proof.get("ref"), 180)
                    and not str(proof["ref"]).startswith(("http:", "https:"))
                    and ".." not in str(proof["ref"]),
                    "UNSAFE_OR_UNBOUND_PROOF_REF")
        if scenario in PHYSICAL and state == "PASS":
            require(row.get("acquisition") == "PHYSICAL_DEVICE_OBSERVATION",
                    "PHYSICAL_SCENARIO_NOT_OBSERVED")
        observed[scenario] = state

    missing = sorted(set(SCENARIOS).difference(observed))
    failures = sorted(k for k, v in observed.items() if v == "FAIL")
    not_passed = sorted(k for k, v in observed.items()
                        if v in {"BLOCKED", "NOT_VERIFIED"})
    # An external trusted actor must rehash evidence bytes, bind exact
    # APK/source and independently observe actual notification delivery.
    # Self-reported PASS and hash strings CANNOT grant such authority.
    return {
        "schema_version": 1,
        "record_type": "X10_023_DEVICE_QA_STRUCTURAL_REVIEW",
        "source_sha": expected_source_sha,
        "artifact_sha256": identity["artifact_sha256"],
        "scenario_count": len(observed),
        "total_required_scenarios": len(SCENARIOS),
        "missing_scenarios": missing,
        "failed_scenarios": failures,
        "blocked_or_not_verified_scenarios": not_passed,
        "claimed_scenarios_pass": len(missing) == len(failures) == len(not_passed) == 0,
        "disposition": ("CLAIMS_INCOMPLETE_OR_FAILED"
                        if missing or failures or not_passed
                        else "UNTRUSTED_COMPLETE_CLAIM_REQUIRES_INDEPENDENT_VERIFICATION"),
        "external_artifact_bytes_rehashed": False,
        "trusted_os_execution_observed": False,
        "device_verified": False,
        "platform_release_verified": False,
        "golden_promoted": False,
        "x10_023_eligible_for_verification": False,
        "next_gate": "INDEPENDENT_APPLAB_ARTIFACT_REHASH_AND_PHYSICAL_DELIVERY_REVIEW",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--source-sha", required=True)
    args = parser.parse_args()
    require(args.input.is_file() and args.input.stat().st_size <= MAX_BYTES,
            "DOSSIER_NOT_FOUND_OR_TOO_LARGE")
    record = json.loads(args.input.read_text(encoding="utf-8"))
    print(json.dumps(classify(record, expected_source_sha=args.source_sha),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
