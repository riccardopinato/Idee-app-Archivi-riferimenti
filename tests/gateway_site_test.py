"""Gateway read-only Site snapshot integrity (no network or live deploy)."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1] / "16-APP-FACTORY-SITE"
DATA = ROOT / "data/gateway_progress.json"
HTML = ROOT / "src/index.html"
SHA = re.compile(r"^[0-9a-f]{40}$")
URL = re.compile(r"^https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/\d+$")


class GatewaySiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads(DATA.read_text(encoding="utf-8"))

    def test_source_separation_and_snapshot_staleness_labels(self):
        d = self.rows
        self.assertEqual(d["schema_version"], 1)
        self.assertEqual(d["record_type"], "APP_FACTORY_GATEWAY_SOURCE_SNAPSHOT")
        self.assertTrue(SHA.fullmatch(d["factory_baseline_sha"]))
        self.assertFalse(d["auto_refresh_verified"])
        self.assertFalse(d["source_is_canonical"])
        self.assertFalse(d["certification_granted"])
        self.assertEqual(d["merged_count"], 0)
        self.assertEqual(d["pr_count"], len(d["prs"]))

    def test_exact_head_ci_and_no_false_approvals(self):
        d = self.rows
        self.assertEqual(len(d["prs"]), len({r["number"] for r in d["prs"]}))
        self.assertEqual([r["number"] for r in d["prs"]], list(range(25, 33)))
        for r in d["prs"]:
            self.assertTrue(SHA.fullmatch(r["head_sha"]))
            self.assertFalse(r["merged"])
            self.assertFalse(r["formal_approval_observed"])
            self.assertFalse(r["branch_protection_verified"])
            self.assertFalse(r["deploy_verified"])
            self.assertFalse(r["certification_granted"])
            self.assertIn("FORMAL_APPROVAL_NOT_OBSERVED", r["blockers"])
            self.assertTrue(r["ci_evidence"])
            for run in r["ci_evidence"]:
                self.assertEqual(run["source_sha"], r["head_sha"])
                self.assertEqual(run["result"], "success")
                self.assertTrue(URL.fullmatch(run["url"]))

    def test_site_uses_separate_feed_preserving_manual_changes(self):
        s = HTML.read_text(encoding="utf-8")
        self.assertIn("appfactory-control-center-v1", s)
        self.assertIn("function gatewayPage()", s)
        self.assertIn("function gatewayTableRows()", s)
        self.assertIn("function loadGatewayStatus()", s)
        self.assertIn("gateway:gatewayPage", s)
        self.assertIn("bindGatewayControls()", s)
        self.assertIn("source_is_canonical!==false", s)
        self.assertIn("CI osservata a commit esatto", s)
        self.assertIn("loadFleetStatus()", s)
        self.assertNotIn("ghp_", s)
        self.assertNotIn("sk-proj-", s)
        if shutil.which("node"):
            js = s.split("<script>", 1)[1].split("</script>", 1)[0]
            p = subprocess.run(["node", "--check", "-"], input=js,
                               text=True, capture_output=True)
            self.assertEqual(p.returncode, 0, p.stderr)


if __name__ == "__main__":
    unittest.main()
