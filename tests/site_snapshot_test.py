"""Static Site source and dataset integrity, no live GitHub or Vercel required."""
import json
import pathlib
import re
import shutil
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1] / "16-APP-FACTORY-SITE"
DATA = ROOT / "data/snapshot.json"
HTML = ROOT / "src/index.html"
SHA40 = re.compile(r"^[0-9a-f]{40}$")


class SiteSnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = json.loads(DATA.read_text(encoding="utf-8"))
        cls.rows = cls.raw["data"]

    def test_canonical_counts(self):
        d = self.rows
        self.assertEqual(len(d["goldens"]), 61)
        self.assertEqual(len(d["passports"]), 20)
        self.assertEqual(len(d["capabilities"]), 441)
        self.assertEqual(len({x["id"] for x in d["capabilities"]}), 199)
        self.assertEqual(len({(x["id"], x["project"]) for x in d["capabilities"]}), 441)
        self.assertEqual(len(d["consumerMatrix"]), 48)
        self.assertEqual(len({x["registry_id"] for x in d["goldens"]}), 61)
        self.assertEqual(len({x["id"] for x in d["passports"]}), 20)
        self.assertEqual(len(d["reusable"]), 20)

    def test_evidence_and_unpromoted_parent(self):
        d = self.rows
        self.assertEqual(self.raw["factoryBaseline"]["goldenIndex"], "29")
        self.assertTrue(SHA40.fullmatch(self.raw["factoryBaseline"]["sha"]))
        by_id = {x["registry_id"]: x for x in d["goldens"]}
        for name in ("hybrid_local_search_ephemeral_scoped", "gpx_read_only_preview_scoped"):
            self.assertEqual(by_id[name]["status"], "CERTIFIED GOLDEN")
        for name in ("hybrid_local_search_engine", "gpx_interoperability_engine"):
            self.assertIn("DRAFT", by_id[name]["status"])
        self.assertEqual(sum(x["status"] == "CERTIFIED GOLDEN" for x in d["goldens"]), 2)
        self.assertEqual(sum(x["certification"] == "E3_EXACT_HEAD_TESTS" for x in d["passports"]), 15)
        self.assertEqual(self.rows["registryMetrics"]["normalized_e3_certified"], 15)
        self.assertEqual(self.rows["registryMetrics"]["exact_head_e3_upgrade_batch"], 6)
        for p in d["passports"]:
            self.assertTrue(SHA40.fullmatch(p["source_sha"]))
            self.assertTrue(p["ci_url"].startswith("https://github.com/"))
            self.assertTrue(p["consumer_gate"])
        for x in d["goldens"]:
            self.assertTrue(x["status"])
            self.assertTrue(x["url"].startswith("https://github.com/riccardopinato/App-Factory-Core/blob/"))
            self.assertTrue(SHA40.fullmatch(x["source_sha"]))

    def test_ui_and_js_syntax(self):
        source = HTML.read_text(encoding="utf-8")
        self.assertIn("function goldenPage()", source)
        self.assertIn("function applyGoldenFilters()", source)
        self.assertIn("db.passports=remote.data.passports", source)
        self.assertIn("appfactory-control-center-v1", source) # do not erase existing localStorage
        self.assertIn("Golden Index v29", source)
        self.assertNotIn("ghp_", source)
        self.assertNotIn("sk-proj-", source)
        self.assertIn("<script>", source)
        js = source.split("<script>", 1)[1].split("</script>", 1)[0]
        if shutil.which("node"):
            result = subprocess.run(["node", "--check", "-"], input=js, text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
