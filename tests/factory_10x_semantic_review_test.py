import copy
import unittest

from scripts.factory_10x_semantic_review import (
    SemanticReviewError, prepare, signature
)

A, B = "a" * 40, "b" * 40
PATH = signature(["path", "lib/src/calendar_free_slots.dart"])
DONOR_REPO = "riccardopinato/Agenda-per-Anna"
CONSUMER_REPO = "riccardopinato/FocuSense"


def fixture():
    candidate = {
        "candidate_id": "x10_" + "c" * 24,
        "cap_id": "CAP-0001",
        "producer_repo": DONOR_REPO,
        "producer_sha": A,
        "consumer_repo": CONSUMER_REPO,
        "consumer_inventory_sha": B,
        "source_path_sha256": PATH,
        "status": "NEEDS_REVIEW",
        "automatic_adoption": False,
        "ci_verified_this_run": False,
        "requires_license_review": True,
        "requires_product_owner_approval": True,
    }
    donor = {
        "repository": DONOR_REPO,
        "source_sha": A,
        "source_path_sha256": PATH,
        "cap_id": "CAP-0001",
        "semantic_description": "Local free-slot suggestions from structured calendar events.",
        "ci_source_sha": A,
        "ci_run_url": "https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/123",
        "test_paths": ["test/calendar_free_slots_test.dart"],
        "license_decision": "INTERNAL_APPROVED",
        "license_reference": f"https://github.com/riccardopinato/Agenda-per-Anna/blob/{A}/LICENSE",
        "license_file_sha256": PATH,
    }
    consumer = {
        "repository": CONSUMER_REPO,
        "source_sha": B,
        "cap_id": "CAP-0001",
        "compatibility_assessment": "A proposed workday-planner adapter, not yet verified in FocuSense.",
        "product_bible_ref": f"https://github.com/riccardopinato/FocuSense/blob/{B}/PRODUCT_BIBLE.md",
        "product_owner_policy": "REVIEW_REQUIRED",
    }
    review = {
        "decision": "APPROVED",
        "reviewer": "independent-reviewer",
        "review_ref": "https://github.com/riccardopinato/FocuSense/pull/123",
        "approval_scope": "Propose a scoped PR only; require consumer QA and owner signoff.",
        "donor_sha": A,
        "consumer_sha": B,
        "cap_id": "CAP-0001",
    }
    return candidate, donor, consumer, review


class SemanticReviewTests(unittest.TestCase):
    def assess(self, mutation=None, trusted=None):
        c, d, t, r = fixture()
        if mutation:
            mutation(c, d, t, r)
        return prepare(c, d, t, r, trusted_receipt_verifier=trusted)

    def test_approval_claim_alone_never_mints_authority(self):
        result = self.assess()
        self.assertEqual(result["review_state"], "BLOCKED_PENDING_REVIEW")
        self.assertFalse(result["approval_verified"])
        self.assertFalse(result["automatic_code_change"])
        self.assertFalse(result["automatic_merge"])
        self.assertFalse(result["golden_promotion"])

    def test_independently_verified_approval_still_only_authorizes_review(self):
        result = self.assess(trusted=lambda receipt: True)
        self.assertEqual(result["review_state"], "SCOPED_REVIEW_RECORDED")
        self.assertTrue(result["approval_verified"])
        self.assertTrue(result["requires_scoped_pr"])
        self.assertTrue(result["independent_consumer_ci_required"])
        self.assertFalse(result["consumer_runtime_verified"])

    def test_stale_or_blocked_candidates_cannot_be_reapproved(self):
        for status in ("STALE", "BLOCKED"):
            def mutate(c, d, t, r):
                c["status"] = status
            result = self.assess(mutate, trusted=lambda receipt: True)
            self.assertFalse(result["approval_verified"])
            self.assertEqual(result["review_state"], "BLOCKED_PENDING_REVIEW")

    def test_donor_sha_or_source_hash_mismatch_fails(self):
        def sha(c, d, t, r):
            d["source_sha"] = "d" * 40
        with self.assertRaisesRegex(SemanticReviewError, "DONOR_PROVENANCE_MISMATCH"):
            self.assess(sha)
        def path(c, d, t, r):
            d["source_path_sha256"] = "d" * 64
        with self.assertRaisesRegex(SemanticReviewError, "DONOR_PROVENANCE_MISMATCH"):
            self.assess(path)

    def test_ci_sha_missing_or_unmatching_fails(self):
        def alter(c, d, t, r):
            d["ci_source_sha"] = B
        with self.assertRaisesRegex(SemanticReviewError, "SOURCE_TEST_EVIDENCE_MISSING"):
            self.assess(alter)

    def test_license_per_file_is_a_separate_gate(self):
        for field, value in (("license_decision", "UNKNOWN"),
                             ("license_reference", ""),
                             ("license_file_sha256", "f" * 64)):
            def alter(c, d, t, r):
                d[field] = value
            with self.assertRaisesRegex(SemanticReviewError, "PER_FILE_LICENSE_REQUIRED"):
                self.assess(alter)

    def test_product_bible_must_be_exact_consumer_sha(self):
        def alter(c, d, t, r):
            t["product_bible_ref"] = "https://github.com/example/app/blob/main/PRODUCT_BIBLE.md"
        with self.assertRaisesRegex(SemanticReviewError, "PRODUCT_BIBLE_SCOPE_REQUIRED"):
            self.assess(alter)

    def test_claimed_human_approval_must_be_source_bound(self):
        def alter(c, d, t, r):
            r["consumer_sha"] = "f" * 40
        with self.assertRaisesRegex(SemanticReviewError, "HUMAN_APPROVAL_NOT_SOURCE_BOUND"):
            self.assess(alter)

    def test_deferred_or_rejected_status_never_calls_verifier(self):
        for decision in ("REJECTED", "DEFERRED"):
            calls = []
            def alter(c, d, t, r):
                r["decision"] = decision
            out = self.assess(alter, trusted=lambda payload: calls.append(payload))
            self.assertEqual(calls, [])
            self.assertFalse(out["approval_verified"])

    def test_verifier_failure_does_not_grant_approval(self):
        def broken(payload):
            raise ValueError("provider unavailable")
        result = self.assess(trusted=broken)
        self.assertEqual(result["review_state"], "BLOCKED_PENDING_REVIEW")
        self.assertIn("INDEPENDENT_REVIEW_PROVENANCE_NOT_VERIFIED",
                      result["reason_codes"])

    def test_review_proposal_does_not_export_private_semantic_content(self):
        result = self.assess()
        self.assertNotIn("Local free-slot suggestions", str(result))
        self.assertNotIn("independent-reviewer", str(result))
        self.assertEqual(result["source_path_sha256"], PATH)
        self.assertEqual(result["authority"], "ADVISORY_ONLY")

    def test_deterministic_review_fingerprint(self):
        self.assertEqual(self.assess()["review_fingerprint"],
                         self.assess()["review_fingerprint"])


if __name__ == "__main__":
    unittest.main()
