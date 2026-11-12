#!/usr/bin/env python3
"""X10-043: supervised semantic review of existing-CAP reuse proposals.

Never fetches source, self-verifies a run, changes Product Bibles, creates a
PR, grants an agent capability or promotes a Golden. Verification callbacks
must come from a separate authenticated control plane.
"""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Callable

SHA40 = re.compile(r"^[a-f0-9]{40}$")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
CAP = re.compile(r"^CAP-[0-9]{4,}$")
REPO = re.compile(r"^riccardopinato/[A-Za-z0-9_.-]+$")
REVIEW_STATES = {"APPROVED", "REJECTED", "DEFERRED"}
LICENSE_STATES = {"INTERNAL_APPROVED", "SPDX_VERIFIED"}


class SemanticReviewError(ValueError):
    pass


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise SemanticReviewError(reason)


def signature(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=True).encode("ascii")).hexdigest()


def prepare(
    candidate: dict[str, Any],
    donor: dict[str, Any],
    consumer: dict[str, Any],
    review: dict[str, Any] | None,
    *,
    trusted_receipt_verifier: Callable[[dict[str, Any]], bool] | None = None,
) -> dict[str, Any]:
    """A human review is only recorded when separately identity-verified.

    A synthetic callback returning True in tests is not evidence of real
    signed review, checked license, actual CI or consumer Product Bible.
    """
    require(all(isinstance(x, dict) for x in (candidate, donor, consumer)),
            "INVALID_INPUT")
    cid, cap_id = candidate.get("candidate_id"), candidate.get("cap_id")
    source_repo, source_sha = candidate.get("producer_repo"), candidate.get("producer_sha")
    target_repo, target_sha = candidate.get("consumer_repo"), candidate.get("consumer_inventory_sha")
    path_sha = candidate.get("source_path_sha256")
    require(isinstance(cid, str) and cid.startswith("x10_") and len(cid) <= 80
            and isinstance(cap_id, str) and CAP.fullmatch(cap_id) is not None
            and all(isinstance(x, str) and SHA40.fullmatch(x) is not None
                    for x in (source_sha, target_sha))
            and all(isinstance(x, str) and REPO.fullmatch(x) is not None
                    for x in (source_repo, target_repo))
            and isinstance(path_sha, str) and SHA256.fullmatch(path_sha) is not None,
            "CANDIDATE_IDENTITY_INVALID")
    require(candidate.get("automatic_adoption") is False
            and candidate.get("requires_license_review") is True
            and candidate.get("requires_product_owner_approval") is True
            and candidate.get("ci_verified_this_run") is False,
            "CANDIDATE_AUTHORITY_INVALID")
    state = candidate.get("status")
    require(state in {"NEEDS_REVIEW", "STALE", "BLOCKED"}, "UNKNOWN_CANDIDATE_STATE")

    require(donor.get("repository") == source_repo
            and donor.get("source_sha") == source_sha
            and donor.get("source_path_sha256") == path_sha
            and donor.get("cap_id") == cap_id,
            "DONOR_PROVENANCE_MISMATCH")
    require(consumer.get("repository") == target_repo
            and consumer.get("source_sha") == target_sha
            and consumer.get("cap_id") == cap_id,
            "CONSUMER_PROVENANCE_MISMATCH")
    require(isinstance(donor.get("semantic_description"), str)
            and 15 <= len(donor["semantic_description"].strip()) <= 500
            and isinstance(consumer.get("compatibility_assessment"), str)
            and 15 <= len(consumer["compatibility_assessment"].strip()) <= 500,
            "SEMANTIC_EVIDENCE_MISSING")
    require(isinstance(donor.get("ci_source_sha"), str)
            and donor["ci_source_sha"] == source_sha
            and isinstance(donor.get("test_paths"), list)
            and bool(donor["test_paths"])
            and all(isinstance(path, str) and path.strip() and len(path) <= 256
                    for path in donor["test_paths"]),
            "SOURCE_TEST_EVIDENCE_MISSING")
    ci_url = donor.get("ci_run_url")
    require(isinstance(ci_url, str)
            and ci_url.startswith("https://github.com/")
            and "/actions/runs/" in ci_url,
            "CI_REFERENCE_REQUIRED")
    license_kind = donor.get("license_decision")
    license_ref = donor.get("license_reference")
    require(license_kind in LICENSE_STATES
            and isinstance(license_ref, str)
            and license_ref.startswith("https://github.com/")
            and isinstance(donor.get("license_file_sha256"), str)
            and donor["license_file_sha256"] == path_sha,
            "PER_FILE_LICENSE_REQUIRED")
    product_ref = consumer.get("product_bible_ref")
    require(isinstance(product_ref, str)
            and product_ref.startswith("https://github.com/")
            and target_sha in product_ref
            and consumer.get("product_owner_policy") == "REVIEW_REQUIRED",
            "PRODUCT_BIBLE_SCOPE_REQUIRED")

    review = review or {}
    require(isinstance(review, dict), "REVIEW_INPUT_INVALID")
    decision = review.get("decision", "DEFERRED")
    require(decision in REVIEW_STATES, "UNKNOWN_REVIEW_DECISION")
    if decision == "APPROVED":
        require(isinstance(review.get("reviewer"), str)
                and 3 <= len(review["reviewer"]) <= 70
                and isinstance(review.get("review_ref"), str)
                and review["review_ref"].startswith("https://github.com/")
                and isinstance(review.get("approval_scope"), str)
                and 10 <= len(review["approval_scope"]) <= 300
                and review.get("donor_sha") == source_sha
                and review.get("consumer_sha") == target_sha
                and review.get("cap_id") == cap_id,
                "HUMAN_APPROVAL_NOT_SOURCE_BOUND")
    trusted = False
    if state == "NEEDS_REVIEW" and decision == "APPROVED" and callable(trusted_receipt_verifier):
        try:
            trusted = trusted_receipt_verifier({
                "candidate": candidate, "donor": donor, "consumer": consumer,
                "review": review,
            }) is True
        except (ValueError, TypeError, KeyError):
            trusted = False

    reasons = []
    if state != "NEEDS_REVIEW":
        reasons.append("CANDIDATE_" + state)
    if decision != "APPROVED":
        reasons.append("HUMAN_" + decision)
    if decision == "APPROVED" and not trusted:
        reasons.append("INDEPENDENT_REVIEW_PROVENANCE_NOT_VERIFIED")
    status = ("SCOPED_REVIEW_RECORDED" if state == "NEEDS_REVIEW"
              and decision == "APPROVED" and trusted else "BLOCKED_PENDING_REVIEW")
    return {
        "schema_version": 1,
        "record_type": "X10_043_SUPERVISED_REUSE_PROPOSAL",
        "candidate_id": cid, "cap_id": cap_id,
        "producer_repo": source_repo, "producer_sha": source_sha,
        "consumer_repo": target_repo, "consumer_sha": target_sha,
        "source_path_sha256": path_sha, "ci_run_url": ci_url,
        "review_state": status, "reason_codes": reasons,
        "review_fingerprint": signature([cid, cap_id, source_sha, target_sha,
                                           donor, consumer, review]),
        "authority": "ADVISORY_ONLY", "approval_verified": trusted,
        "independent_consumer_ci_required": True,
        "requires_scoped_pr": True,
        "automatic_code_change": False,
        "automatic_merge": False,
        "golden_promotion": False,
        "consumer_runtime_verified": False,
    }
