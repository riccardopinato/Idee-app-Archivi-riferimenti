import copy
import unittest

from scripts.factory_10x_cap_dedup import join, digest, DedupError

FACTORY = "f" * 40
A = "a" * 40
B = "b" * 40
TODAY = "2026-11-12"


def fixture():
    path = "lib/src/calendar_free_slots.dart"
    monitor = {
        "schema_version": 1, "record_type": "X10_041_DIFF_HINTS",
        "authority": "ADVISORY_ONLY", "repository": "riccardopinato/Agenda-per-Anna",
        "head_sha": A, "monitor_key": "e" * 64,
        "source_code_copied": False, "automated_pr_created": False,
        "signals": [{"path_sha256": digest(["path", path]), "signals": ["storage"]}],
    }
    registry = {
        "schema_version": 1, "factory_baseline": "riccardopinato/App-Factory-Core@" + FACTORY,
        "updated_at": TODAY, "records": [
            {"id": "CAP-0001",
             "app_states": {"Agenda-per-Anna": "CI_VERIFIED", "FocuSense": "PROPOSTA"},
             "implementation_evidence": {
                 "Agenda-per-Anna": {"source_path": path, "source_sha": A,
                                     "ci_exact_head_sha": A}}}
        ],
    }
    inventory = {
        "schema_version": 1, "updated_at": TODAY,
        "repositories": [
            {"name": "Agenda-per-Anna", "head_sha": A, "head_observed_at": TODAY},
            {"name": "FocuSense", "head_sha": B, "head_observed_at": TODAY},
        ],
    }
    return monitor, registry, inventory


class DedupTests(unittest.TestCase):
    def assess(self, changes=None):
        monitor, registry, inventory = fixture()
        if changes:
            changes(monitor, registry, inventory)
        return join(monitor, registry, inventory, factory_sha=FACTORY, observed_on=TODAY)

    def test_same_source_same_candidate_id_without_new_cap(self):
        a, b = self.assess(), self.assess()
        self.assertEqual(a, b)
        self.assertEqual(len(a["candidates"]), 1)
        row = a["candidates"][0]
        self.assertEqual(row["cap_id"], "CAP-0001")
        self.assertEqual(row["status"], "NEEDS_REVIEW")
        self.assertFalse(row["automatic_adoption"])
        self.assertEqual(a["new_cap_ids_created"], 0)

    def test_nonmatching_path_hash_does_not_guess_cap(self):
        def wrong(m, r, i):
            m["signals"][0]["path_sha256"] = "9" * 64
        self.assertEqual(self.assess(wrong)["candidates"], [])

    def test_stale_producer_inventory_sha_stays_stale(self):
        def stale(m, r, i):
            i["repositories"][0]["head_sha"] = "c" * 40
        row = self.assess(stale)["candidates"][0]
        self.assertEqual(row["status"], "STALE")
        self.assertIn("PRODUCER_INVENTORY_STALE", row["reason_codes"])

    def test_factory_baseline_stale_rejected_from_actionable(self):
        def stale(m, r, i):
            r["factory_baseline"] = "riccardopinato/App-Factory-Core@" + "c" * 40
        row = self.assess(stale)["candidates"][0]
        self.assertEqual(row["status"], "STALE")
        self.assertIn("CAP_REGISTRY_FACTORY_BASELINE_STALE", row["reason_codes"])

    def test_source_evidence_old_commit_stale(self):
        def stale(m, r, i):
            r["records"][0]["implementation_evidence"]["Agenda-per-Anna"]["source_sha"] = "c" * 40
        row = self.assess(stale)["candidates"][0]
        self.assertEqual(row["status"], "STALE")
        self.assertIn("CAP_SOURCE_SHA_DIFFERS", row["reason_codes"])

    def test_consumer_already_implemented_is_not_new_proposal(self):
        def already(m, r, i):
            r["records"][0]["app_states"]["FocuSense"] = "CI_VERIFIED"
        self.assertEqual(self.assess(already)["candidates"], [])

    def test_two_records_same_cap_id_fail_closed(self):
        def duplicate(m, r, i):
            r["records"].append(copy.deepcopy(r["records"][0]))
        with self.assertRaisesRegex(DedupError, "DUPLICATE_CAP_ID"):
            self.assess(duplicate)

    def test_unknown_consumer_repo_does_not_invent_head(self):
        def missing(m, r, i):
            i["repositories"].pop()
        self.assertEqual(self.assess(missing)["candidates"], [])

    def test_no_raw_file_path_or_source_text_in_advice(self):
        output = str(self.assess())
        self.assertNotIn("calendar_free_slots.dart", output)
        self.assertIn("source_path_sha256", output)

    def test_old_consumer_snapshot_not_auto_promoted(self):
        def stale(m, r, i):
            i["repositories"][1]["head_observed_at"] = "2026-11-08"
        self.assertIn("CONSUMER_INVENTORY_STALE",
                      self.assess(stale)["candidates"][0]["reason_codes"])

    def test_monitor_identity_and_dup_hints_fail_closed(self):
        def wrong(m, r, i):
            m["authority"] = "DEPLOY_CODE"
        with self.assertRaisesRegex(DedupError, "UNTRUSTED_MONITOR"):
            self.assess(wrong)
        def duplicated(m, r, i):
            m["signals"].append(copy.deepcopy(m["signals"][0]))
        with self.assertRaisesRegex(DedupError, "DUPLICATE_HASHED_PATH_HINT"):
            self.assess(duplicated)


if __name__ == "__main__":
    unittest.main()
