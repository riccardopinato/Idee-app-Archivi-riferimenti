import copy
import unittest

from scripts.factory_10x_queue import (
    load, next_tasks, receipt_ok, summary_markdown, validate,
)


class ContinuousRoadmapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = load()

    def fixture_baseline(self):
        # Scenario tests must not depend on the current live program checkpoint.
        p = copy.deepcopy(self.document)
        for task in p["tasks"]:
            if task["id"] not in {"X10-001", "X10-004"}:
                task["status"] = "PLANNED"
                task["evidence"] = []
                task["blocker"] = None
                task.pop("gate_reviewed", None)
        return p

    def test_57_tasks_and_8_waves(self):
        d = validate(self.document)
        self.assertEqual(d["total"], 57)
        self.assertEqual(d["waves"], 8)
        self.assertEqual(sum(d["by_status"].values()), 57)
        self.assertGreaterEqual(d["by_status"].get("VERIFIED", 0), 0)

    def test_uncapped_parallel_selection_including_same_repo_read_only(self):
        result = next_tasks(self.fixture_baseline())
        ids = {t["id"] for t in result["selected"]}
        self.assertGreater(len(ids), 3)
        self.assertIn("X10-002", ids)
        self.assertIn("X10-003", ids)  # Both READ_ONLY and same repository
        self.assertIn("X10-007", ids)
        self.assertIn("X10-009", ids)
        self.assertIn("X10-027", ids)
        writers = {"X10-005", "X10-006"}
        self.assertEqual(len(writers & ids), 1)
        self.assertEqual({c["id"] for c in result["writer_conflicts"]} & writers, writers - ids)
        self.assertTrue(all(t["status"] == "PLANNED" for t in result["selected"]))

    def test_live_queue_checkpoint_preserves_future_work(self):
        live = next_tasks(self.document)
        self.assertNotIn("X10-008", {t["id"] for t in live["selected"]})
        self.assertNotIn("X10-015", {t["id"] for t in live["selected"]})
        self.assertEqual(live["verified"], sum(t["status"] == "VERIFIED" for t in self.document["tasks"]))

    def test_unlimited_ready_read_only_tasks_no_fixed_number(self):
        p = self.fixture_baseline()
        seed = next(t for t in p["tasks"] if t["id"] == "X10-003")
        for i in range(58, 70):
            t = copy.deepcopy(seed)
            t["id"] = f"X10-{i:03d}"
            t["title"] = f"Read only independent {i}"
            t["dependencies"] = []
            t["evidence"] = []
            t["status"] = "PLANNED"
            p["tasks"].append(t)
        result = next_tasks(p)
        self.assertEqual(len([t for t in result["selected"]
                              if t["id"] >= "X10-058"]), 12)
        self.assertGreater(len(result["selected"]), 12)

    def test_blocked_writer_is_replaced_with_other_ready(self):
        p = self.fixture_baseline()
        current = next_tasks(p)
        first = next(t for t in current["selected"] if t["mode"] == "PR_GATED")
        first["status"] = "BLOCKED"
        first["blocker"] = "Repository approval pending; no writer resources reserved"
        result = next_tasks(p)
        ids = {t["id"] for t in result["selected"]}
        other = ({"X10-005", "X10-006"} - {first["id"]}).pop()
        self.assertNotIn(first["id"], ids)
        self.assertIn(other, ids)
        self.assertIn("X10-003", ids)

    def test_in_progress_writer_reserves_repo(self):
        p = self.fixture_baseline()
        first = next(t for t in p["tasks"] if t["id"] == "X10-005")
        first["status"] = "IN_PROGRESS"
        result = next_tasks(p)
        self.assertNotIn("X10-006", {t["id"] for t in result["selected"]})
        self.assertIn("X10-003", {t["id"] for t in result["selected"]})

    def test_two_writers_can_run_with_reviewed_nonoverlapping_paths(self):
        p = self.fixture_baseline()
        left = next(t for t in p["tasks"] if t["id"] == "X10-005")
        right = next(t for t in p["tasks"] if t["id"] == "X10-006")
        left.update(write_paths=["docs/a.md"], write_branch="feat/x10-005", scope_reviewed=True)
        right.update(write_paths=["tests/b.py"], write_branch="feat/x10-006", scope_reviewed=True)
        ids = {t["id"] for t in next_tasks(p)["selected"]}
        self.assertIn("X10-005", ids)
        self.assertIn("X10-006", ids)

    def test_overlapping_scopes_still_block_parallel_writes(self):
        p = self.fixture_baseline()
        left = next(t for t in p["tasks"] if t["id"] == "X10-005")
        right = next(t for t in p["tasks"] if t["id"] == "X10-006")
        left.update(write_paths=["docs"], write_branch="feat/x10-005", scope_reviewed=True)
        right.update(write_paths=["docs/b.md"], write_branch="feat/x10-006", scope_reviewed=True)
        selected = {t["id"] for t in next_tasks(p)["selected"]}
        self.assertEqual(len(selected & {"X10-005", "X10-006"}), 1)

    def test_write_scope_needs_review(self):
        p = self.fixture_baseline()
        next(t for t in p["tasks"] if t["id"] == "X10-005").update(
            write_paths=["docs/a.md"], write_branch="feat/x10-005", scope_reviewed=False)
        with self.assertRaises(ValueError):
            validate(p)

    def test_57_tasks_are_not_falsely_complete(self):
        p = summary_markdown(self.document, next_tasks(self.document))
        self.assertIn(f'{sum(t["status"] == "VERIFIED" for t in self.document["tasks"])}/57', p)
        self.assertIn("NON modifica repository", p)

    def test_missing_dependency_fails_closed(self):
        p = copy.deepcopy(self.document)
        p["tasks"][0]["dependencies"] = ["X10-999"]
        with self.assertRaises(ValueError):
            validate(p)

    def test_cycle_fails_closed(self):
        p = copy.deepcopy(self.document)
        p["tasks"][0]["dependencies"] = ["X10-006"]
        with self.assertRaises(ValueError):
            validate(p)

    def test_not_verified_without_independent_evidence(self):
        # Use an unverified fixture: the live X10-002 may already carry valid receipts.
        p = self.fixture_baseline()
        next(t for t in p["tasks"] if t["id"] == "X10-002")["status"] = "VERIFIED"
        with self.assertRaises(ValueError):
            validate(p)

    def test_valid_reviewed_evidence_unblocks_dependent(self):
        p = self.fixture_baseline()
        r = next(t for t in p["tasks"] if t["id"] == "X10-001")
        r["status"] = "VERIFIED"
        r["gate_reviewed"] = True
        r["evidence"] = [{
            "kind": "AUDIT",
            "url": "https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/100",
            "source_sha": "a" * 40,
        }]
        validate(p)
        self.assertTrue(any(t["id"] == "X10-006" for t in next_tasks(p)["ready_not_selected"] + next_tasks(p)["selected"]))

    def test_precondition_blocks_active(self):
        # Use the dependency-incomplete fixture, not the changing live checkpoint:
        # X10-011/012 can become VERIFIED without weakening this negative case.
        p = self.fixture_baseline()
        next(t for t in p["tasks"] if t["id"] == "X10-013")["status"] = "IN_PROGRESS"
        with self.assertRaises(ValueError):
            validate(p)

    def test_reviewed_proof_must_be_github_sha(self):
        self.assertFalse(receipt_ok({"kind": "CI", "url": "http://evil", "source_sha": "a" * 40}))
        self.assertFalse(receipt_ok({"kind": "CI", "url": "https://github.com/a/b", "source_sha": "bad"}))
        self.assertFalse(receipt_ok({"kind": "CERTIFIED_GOLDEN", "url": "https://github.com/a/b", "source_sha": "a" * 40}))

    def test_human_gate_not_auto_executable(self):
        p = self.fixture_baseline()
        for task in p["tasks"]:
            if task["id"] == "X10-008":
                task["dependencies"] = []
                break
        q = next_tasks(p)
        self.assertTrue(any(t["id"] == "X10-008" for t in q["awaiting_human_gate"]))
        self.assertFalse(any(t["id"] == "X10-008" for t in q["selected"]))

    def test_blocked_requires_reason(self):
        p = copy.deepcopy(self.document)
        p["tasks"][0]["status"] = "BLOCKED"
        with self.assertRaises(ValueError):
            validate(p)


if __name__ == "__main__":
    unittest.main()
