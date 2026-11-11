import copy
import json
import unittest
from pathlib import Path

from scripts.context_fleet import FLEET, reconcile, validate


class ContextFleetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FLEET.read_text(encoding="utf-8"))

    def test_35_slot_evidence_integrity(self):
        s = validate(self.data)
        self.assertEqual(s["total"], 35)
        self.assertEqual(s["public"], 32)
        self.assertEqual(s["private"], 3)
        self.assertEqual(s["bot_pr_verified"], 1)
        self.assertEqual(s["schedule_verified"], 0)

    def test_private_references_redacted(self):
        for record in self.data["repositories"]:
            if record["visibility"] == "private":
                self.assertIsNone(record["repository"])
                self.assertIsNone(record["source_sha"])
                self.assertIsNone(record["source_url"])
                self.assertIsNone(record["last_snapshot_run"])

    def test_block_forged_cron_success(self):
        d = copy.deepcopy(self.data)
        row = next(x for x in d["repositories"] if x["id"] == "180FlipCharge")
        row["schedule_verified"] = True
        with self.assertRaises(ValueError):
            validate(d)

    def test_block_fake_pr_proof(self):
        d = copy.deepcopy(self.data)
        row = next(x for x in d["repositories"] if x["id"] == "AppLab")
        row["bot_pr_verified"] = True
        with self.assertRaises(ValueError):
            validate(d)

    def test_no_op_does_not_change_data(self):
        x = reconcile(self.data, [], "2026-11-11T17:30:00Z")
        self.assertEqual(x, self.data)

    def test_pr_actor_is_mandatory(self):
        data = copy.deepcopy(self.data)
        obs = [{"id":"AppLab","event":"workflow_dispatch","result":"success",
                "run_url":"https://github.com/riccardopinato/AppLab/actions/runs/7",
                "pr_url":"https://github.com/riccardopinato/AppLab/pull/3","author":"untrusted"}]
        with self.assertRaises(ValueError):
            reconcile(data, obs, "2026-11-11T17:30:00Z")

    def test_valid_receipt_appends_history(self):
        obs = [{"id":"AppLab","event":"workflow_dispatch","result":"success",
                "run_url":"https://github.com/riccardopinato/AppLab/actions/runs/7"}]
        got = reconcile(self.data, obs, "2026-11-11T17:30:00Z")
        row = next(x for x in got["repositories"] if x["id"] == "AppLab")
        self.assertTrue(row["dispatch_verified"])
        self.assertFalse(row["schedule_verified"])
        self.assertEqual(len(got["history"]), 1)
        self.assertEqual(reconcile(got, obs, "2026-11-11T17:30:00Z"), got)

    def test_no_cross_repo_urls(self):
        d = copy.deepcopy(self.data)
        row = next(x for x in d["repositories"] if x["id"] == "AppLab")
        row["evidence_url"] = "https://github.com/other/other/actions"
        with self.assertRaises(ValueError):
            validate(d)


if __name__ == "__main__":
    unittest.main()
