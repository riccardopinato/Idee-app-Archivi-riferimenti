"""Canonical REA donor-catalog importer may only propose E1 candidates."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "rea_review_to_catalog.py"
spec = importlib.util.spec_from_file_location("rea_catalog", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def specimen():
    return {
        "schema_version": 1, "report_type": "REA_DONOR_RESEARCH_DECISIONS",
        "classification": "E1_RESEARCH_REVIEW_PENDING_CATALOG_PR",
        "catalog_mutated": False, "certified_donors": 0,
        "golden_promoted": False, "execution_of_target": "NONE",
        "source_repository": "riccardopinato/Android-Omni-Cleaner",
        "source_sha": "a" * 40, "target_sha256": "b" * 64,
        "findings": [{
            "id": "manifest_permission",
            "source_comparison": "ALREADY_IN_SOURCE",
            "decision": "REFERENCE_ONLY", "rights": "AUTHORIZED_FOR_RESEARCH",
            "evidence_operation": "inspect-android-package",
            "reason": "Only the existing declared permission has been reobserved."
        }]
    }


def test_reviewed_source_observation_remains_e1():
    result = module.route(specimen())
    assert result["factory_golden_scope"] == "COPY_READY_PROCESS_ONLY"
    assert result["donor_certified"] is False
    assert result["golden_certified"] is False
    assert result["automatic_write"] is False
    assert result["candidate_count"] == 0
    assert result["findings"][0]["admission"] == "E1_RESEARCH_ONLY"


def test_new_authorized_finding_can_only_propose():
    report = specimen()
    report["findings"][0].update(
        decision="ADOPT_CANDIDATE", source_comparison="NEW_BEYOND_SOURCE")
    result = module.route(report)
    assert result["candidate_count"] == 1
    assert result["findings"][0]["requires_ordinary_catalog_pr"]
    assert not result["donor_certified"]


@pytest.mark.parametrize("key,bad", [
    ("certified_donors", 1), ("golden_promoted", True),
    ("catalog_mutated", True), ("classification", "CERTIFIED"),
    ("source_sha", "invalid"), ("target_sha256", "invalid"),
])
def test_forged_certification_or_identity_refused(key, bad):
    report = specimen()
    report[key] = bad
    with pytest.raises(ValueError):
        module.route(report)


def test_fake_novelty_or_unsafe_rights_refused():
    report = specimen()
    report["findings"][0]["decision"] = "ADOPT_CANDIDATE"
    with pytest.raises(ValueError, match="new, authorized"):
        module.route(report)
    report["findings"][0]["source_comparison"] = "NEW_BEYOND_SOURCE"
    report["findings"][0]["rights"] = "INCOMPATIBLE_FOR_COPY"
    with pytest.raises(ValueError, match="new, authorized"):
        module.route(report)
