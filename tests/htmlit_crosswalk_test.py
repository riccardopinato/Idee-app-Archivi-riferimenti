"""Regression: HTML.it is a pattern source, not a code donor or 12 new CAPs."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CAP_DIR = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"


class HtmlItReferenceCrosswalkTest(unittest.TestCase):
    def test_existing_cap_dedup_and_license_gate(self):
        register = json.loads((CAP_DIR / "REGISTRO_CAPABILITY.json").read_text(encoding="utf-8"))
        reference = json.loads((CAP_DIR / "HTMLIT_FLUTTER_REFERENCE_CROSSWALK_2026-11-09.json").read_text(encoding="utf-8"))
        cap_ids = {entry["id"] for entry in register["records"]}
        rows = reference["crosswalk"]
        self.assertEqual(len(rows), 12)
        self.assertEqual(len({row["reference_id"] for row in rows}), 12)
        self.assertEqual(reference["existing_cap_count"], len(cap_ids))
        self.assertEqual(reference["new_cap_count"], 0)
        self.assertEqual(reference["new_app_association_count"], 0)
        self.assertFalse(reference["copy_code_permitted"])
        self.assertTrue(reference["reference_only"])
        self.assertEqual(reference["source_evidence_grade"], "E0_REFERENCE_ONLY")
        for row in rows:
            self.assertTrue(row["existing_cap_ids"])
            self.assertTrue(set(row["existing_cap_ids"]) <= cap_ids)
            self.assertEqual(row["evidence"], "REFERENCE_ONLY")
            self.assertFalse(row["app_implementation_claim"])
            self.assertFalse(row["golden_promotion"])


if __name__ == "__main__":
    unittest.main()
