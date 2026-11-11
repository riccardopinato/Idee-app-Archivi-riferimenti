import copy
import unittest

from scripts.factory_10x_queue import (
    load, next_tasks, receipt_ok, summary_markdown, validate,
)


class ContinuousRoadmapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = load()

    def test_57_tasks_and_8_waves(self):
        d = validate(self.document)
        self.assertEqual(d["total"], 57)
        self.assertEqual(d["waves"], 8)
        self.assertEqual(d["by_status"]["PLANNED"], 57)

    def test_next_tasks_parallel_no_same_repo(self):
        q = next_tasks(self.document)
        tasks = q["selected"]
        self.assertGreaterEqual(len(tasks), 2)
        self.assertLessEqual(len(tasks), 3)
        self.assertEqual(len({t["owner_repo"] for t in tasks}), len(tasks))
        self.assertTrue(all(t["status"] == "PLANNED" for t in tasks))

    def test_57_tasks_are_not_falsely_complete(self):
        p = summary_markdown(self.document, next_tasks(self.document))
        self.assertIn("0/57", p)
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
        p = copy.deepcopy(self.document)
        p["tasks"][0]["status"] = "VERIFIED"
        with self.assertRaises(ValueError):
            validate(p)

    def test_valid_reviewed_evidence_unblocks_dependent(self):
        p = copy.deepcopy(self.document)
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
        p = copy.deepcopy(self.document)
        next(t for t in p["tasks"] if t["id"] == "X10-013")["status"] = "IN_PROGRESS"
        with self.assertRaises(ValueError):
            validate(p)

    def test_reviewed_proof_must_be_github_sha(self):
        self.assertFalse(receipt_ok({"kind": "CI", "url": "http://evil", "source_sha": "a" * 40}))
        self.assertFalse(receipt_ok({"kind": "CI", "url": "https://github.com/a/b", "source_sha": "bad"}))
        self.assertFalse(receipt_ok({"kind": "CERTIFIED_GOLDEN", "url": "https://github.com/a/b", "source_sha": "a" * 40}))

    def test_human_gate_not_auto_executable(self):
        p = copy.deepcopy(self.document)
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
