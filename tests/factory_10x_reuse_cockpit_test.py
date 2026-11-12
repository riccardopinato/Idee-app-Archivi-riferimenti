"""X10-044: synthetic ranking fixtures. No real CAP proposal is authenticated here."""
import copy
import unittest

from scripts.factory_10x_reuse_cockpit import CockpitError, rank

A = "a" * 40
B = "b" * 40
C = "c" * 40
F = "f" * 40
H = "1" * 64
BASELINE = F
DAY = "2026-11-12"


def fixture():
    inv = {
        "schema_version": 1,
        "updated_at": DAY,
        "repositories": [
            {"name": "Agenda-per-Anna", "head_sha": A, "head_observed_at": DAY},
            {"name": "FocuSense", "head_sha": B, "head_observed_at": DAY},
            {"name": "World-Days", "head_sha": C, "head_observed_at": DAY},
        ],
    }
    def proposal(cid, target="FocuSense", target_sha=B):
        return {
            "schema_version": 1, "record_type": "X10_043_SUPERVISED_REUSE_PROPOSAL",
            "authority": "ADVISORY_ONLY",
            "candidate_id": cid, "cap_id": "CAP-0001",
            "producer_repo": "riccardopinato/Agenda-per-Anna", "producer_sha": A,
            "consumer_repo": "riccardopinato/" + target, "consumer_sha": target_sha,
            "source_path_sha256": H, "review_fingerprint": H,
            "review_state": "BLOCKED_PENDING_REVIEW", "approval_verified": False,
            "requires_scoped_pr": True,
            "independent_consumer_ci_required": True,
            "automatic_code_change": False, "automatic_merge": False,
            "golden_promotion": False, "consumer_runtime_verified": False,
        }
    def estimate(cid, impact=5, risk=2, effort=2, dependencies=None):
        return {
            "candidate_id": cid,
            "impact": impact, "cross_app_reuse": 4, "evidence": 3,
            "risk": risk, "effort": effort,
            "dependencies": dependencies or [],
            "assumptions": "Illustrative assessment only; no market evidence or actual product approval.",
        }
    return inv, proposal, estimate


def run(ps, es, inv=None):
    if inv is None:
        inv = fixture()[0]
    return rank(ps, es, inv, factory_sha=BASELINE, observed_on=DAY)


class ReuseCockpitTests(unittest.TestCase):
    def test_empty_real_pipeline_yields_empty_cockpit_not_fabricated_opportunity(self):
        result = run([], [])
        self.assertEqual(result["ranked"], [])
        self.assertEqual(result["input_proposals"], 0)
        self.assertFalse(result["consumer_writes_performed"])

    def test_ranking_high_impact_low_risk_effort_first(self):
        inv, p, e = fixture()
        hi = p("x10_candidate_one")
        lo = p("x10_candidate_two", target="World-Days", target_sha=C)
        a = e("x10_candidate_one")
        b = e("x10_candidate_two", impact=2, risk=5, effort=5)
        result = run([lo, hi], [b, a], inv)
        self.assertEqual([x["candidate_id"] for x in result["ranked"]],
                         ["x10_candidate_one", "x10_candidate_two"])
        self.assertEqual([x["review_queue_position"] for x in result["ranked"]], [1, 2])
        self.assertEqual(result["ranked"][1]["score_kind"], "UNVERIFIED_RELATIVE_ESTIMATE")
        self.assertFalse(result["ranked"][0]["automatic_adoption"])

    def test_ranking_is_deterministic_independent_of_input_order(self):
        inv, p, e = fixture()
        ps = [p("x10_a"), p("x10_b", target="World-Days", target_sha=C)]
        es = [e("x10_a"), e("x10_b")]
        self.assertEqual(run(ps, es, inv), run(list(reversed(ps)), list(reversed(es)), inv))

    def test_inventory_staleness_is_never_overridden_by_score(self):
        inv, p, e = fixture()
        stale = p("x10_stale", target="World-Days", target_sha=C)
        fresh = p("x10_fresh")
        inv["repositories"][2]["head_observed_at"] = "2026-11-01"
        result = run(
            [stale, fresh],
            [e("x10_stale"), e("x10_fresh", impact=0, risk=5, effort=5)],
            inv,
        )
        self.assertEqual(result["ranked"][0]["candidate_id"], "x10_fresh")
        self.assertEqual(result["ranked"][1]["state"], "STALE_RECHECK")
        self.assertEqual(result["ranked"][1]["recommended_next_action"],
                         "REFRESH_PINNED_INVENTORY")

    def test_missing_consumer_is_stale_and_cannot_be_guessed(self):
        inv, p, e = fixture()
        row = p("x10_ghost", target="MissingRepo", target_sha=C)
        res = run([row], [e("x10_ghost")], inv)["ranked"][0]
        self.assertIn("CONSUMER_SOURCE_STALE_OR_UNKNOWN", res["reason_codes"])
        self.assertEqual(res["state"], "STALE_RECHECK")

    def test_reported_human_approval_does_not_enable_auto_merge(self):
        inv, p, e = fixture()
        row = p("x10_approved")
        row["review_state"] = "SCOPED_REVIEW_RECORDED"
        row["approval_verified"] = True
        ranked = run([row], [e("x10_approved")], inv)["ranked"][0]
        self.assertFalse(ranked["automatic_adoption"])
        self.assertFalse(ranked["consumer_ci_verified_by_cockpit"])
        self.assertFalse(ranked["license_verified_by_cockpit"])
        self.assertFalse(ranked["product_approved_by_cockpit"])
        self.assertEqual(ranked["state"], "REVIEW_BACKLOG")

    def test_incoherent_claimed_approval_rejected(self):
        inv, p, e = fixture()
        row = p("x10_fake")
        row["review_state"] = "SCOPED_REVIEW_RECORDED"
        with self.assertRaisesRegex(CockpitError, "INCOHERENT_REVIEW_STATE"):
            run([row], [e("x10_fake")], inv)

    def test_untrusted_or_automatic_proposal_rejected(self):
        inv, p, e = fixture()
        for field, value in (("automatic_merge", True), ("authority", "AUTO_WRITE"),
                             ("consumer_runtime_verified", True),
                             ("golden_promotion", True),
                             ("requires_scoped_pr", False)):
            row = p("x10_bad")
            row[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(
                CockpitError, "UNTRUSTED_SEMANTIC_PROPOSAL"
            ):
                run([row], [e("x10_bad")], inv)

    def test_missing_assessment_and_extra_assessment_both_denied(self):
        inv, p, e = fixture()
        with self.assertRaisesRegex(CockpitError, "MISSING_ASSESSMENT"):
            run([p("x10_one")], [], inv)
        with self.assertRaisesRegex(CockpitError, "UNMATCHED_ASSESSMENT"):
            run([], [e("x10_one")], inv)

    def test_duplicate_ids_and_case_only_repo_inventory_denied(self):
        inv, p, e = fixture()
        with self.assertRaisesRegex(CockpitError, "DUPLICATE_PROPOSAL"):
            run([p("x10_dup"), p("x10_dup")], [e("x10_dup")], inv)
        inv["repositories"].append({
            "name": "focusense", "head_sha": B, "head_observed_at": DAY,
        })
        with self.assertRaisesRegex(CockpitError, "DUPLICATE_INVENTORY_REPO"):
            run([], [], inv)

    def test_bad_numeric_and_dependency_input_fails_closed(self):
        inv, p, e = fixture()
        for value in (True, -1, 6, 2.5, "5"):
            estimate = e("x10_bad")
            estimate["risk"] = value
            with self.subTest(value=value), self.assertRaisesRegex(
                CockpitError, "INVALID_SCORE_RISK"
            ):
                run([p("x10_bad")], [estimate], inv)
        estimate = e("x10_bad", dependencies=["X10-008", "X10-008"])
        with self.assertRaisesRegex(CockpitError, "INVALID_DEPENDENCIES"):
            run([p("x10_bad")], [estimate], inv)

    def test_dependency_and_high_risk_cannot_disappear_from_results(self):
        inv, p, e = fixture()
        estimate = e("x10_dep", risk=4, dependencies=["X10-008", "X10-018"])
        row = run([p("x10_dep")], [estimate], inv)["ranked"][0]
        self.assertIn("UNRESOLVED_DEPENDENCIES", row["reason_codes"])
        self.assertIn("HIGH_RISK_REVIEW", row["reason_codes"])
        self.assertIn("HUMAN_REVIEW_PENDING", row["reason_codes"])
        self.assertEqual(row["dependencies"], ["X10-008", "X10-018"])


if __name__ == "__main__":
    unittest.main()
