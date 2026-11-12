"""X10-003 verifies pinned golden/donor evidence; no copy-ready promotion."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "19-APP-FACTORY-10X/data/reuse_inventory_v1.json"
SHA = re.compile(r"^[0-9a-f]{40}$")

class ReuseInventoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(PATH.read_text(encoding="utf-8"))

    def test_provenance_and_counts(self):
        d=self.data
        self.assertEqual(d["schema_version"],1)
        self.assertTrue(SHA.fullmatch(d["baseline_factory_sha"]))
        self.assertEqual(len(d["goldens"]),61)
        self.assertEqual(len(d["passports"]),20)
        self.assertEqual(d["totals"]["goldens"],61)
        self.assertEqual(d["totals"]["passports"],20)

    def test_unique_golden_and_donor_pasports(self):
        d=self.data
        self.assertEqual(len({g["id"] for g in d["goldens"]}),61)
        self.assertEqual(len({p["id"] for p in d["passports"]}),20)
        for g in d["goldens"]:
            self.assertTrue(g["status"])
            self.assertTrue(g["source_url"].startswith("https://github.com/riccardopinato/App-Factory-Core/blob/"+d["baseline_factory_sha"]+"/"))
            self.assertIn(g["freshness"],("CURRENT","NEEDS_REVIEW","STALE","UNKNOWN",None))
        for p in d["passports"]:
            self.assertTrue(SHA.fullmatch(p["source_sha"]))
            self.assertTrue(p["ci_url"].startswith("https://github.com/"))

    def test_no_false_promotion(self):
        d=self.data
        self.assertEqual(sum(g["status"]=="CERTIFIED GOLDEN" for g in d["goldens"]),2)
        self.assertEqual(sum(g["admission"]=="COPY_READY" for g in d["goldens"]),13)
        self.assertEqual(sum(p["certification"]=="E3_EXACT_HEAD_TESTS" for p in d["passports"]),15)
        self.assertIn("Site snapshot",d["passports_age_warning"])
        self.assertIn("No code imported",d["policy"])

if __name__=="__main__":
    unittest.main()
