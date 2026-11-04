"""Anna 58→52/14 scoped intake: preserve source evidence, no Golden promotion."""
import csv
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_status_views import admitted_product_evaluation, render  # noqa: E402

BASE = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
ADMITTED = {
    "CAP-0092", "CAP-0093", "CAP-0101",
    "CAP-0120", "CAP-0145", "CAP-0147",
}

class AnnaEvaluationAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((BASE / "REGISTRO_CAPABILITY.json")
                              .read_text(encoding="utf-8"))
        cls.records = cls.data["records"]
        cls.views = render()

    def test_exact_admission_and_canonical_app_states(self):
        self.assertEqual(len(self.records), 160)
        self.assertEqual(sum(len(r["app_states"]) for r in self.records), 385)
        self.assertEqual(sum("Agenda-per-Anna" in r["app_states"]
                             for r in self.records), 74)
        selected = {
            r["id"] for r in self.records
            if "Agenda-per-Anna" in r.get("app_evaluation_admissions", {})
        }
        self.assertEqual(selected, ADMITTED)
        for record in self.records:
            admission = record.get("app_evaluation_admissions", {}).get("Agenda-per-Anna")
            if admission is None:
                continue
            with self.subTest(cap=record["id"]):
                self.assertEqual(record["app_states"]["Agenda-per-Anna"],
                                 "PROPOSTA")
                self.assertEqual(record["anna_full_source_audit"]["classification"],
                                 "PARTIAL_REUSE")
                self.assertFalse(admission["implementation_approved"])
                self.assertFalse(admission["physical_device_verified"])
                self.assertFalse(admission["source_state_changed"])
                self.assertEqual(admission["factory_sha"],
                    "8052b45b771bf3c5694fc6dd8d037bd83233b37a")
                self.assertIsNotNone(admitted_product_evaluation(
                    record, "Agenda-per-Anna", "PROPOSTA", "PARTIAL_REUSE"))

    def test_queue_has_exactly_14_pending_8_integrated_52_verify(self):
        prefix = "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/Agenda-per-Anna/"
        pages = {
            name: self.views[prefix + name + ".md"]
            for name in ("DA_VALUTARE", "GIA_INTEGRATI", "DA_VERIFICARE")
        }
        import re
        ids = {
            page: {"CAP-" + c for c in re.findall(
                r"^\\| \\[CAP-(\\d{4})\\]", text, re.M)}
            for page, text in pages.items()
        }
        self.assertEqual([len(ids[k]) for k in (
            "DA_VALUTARE", "GIA_INTEGRATI", "DA_VERIFICARE")],
            [14, 8, 52])
        self.assertTrue(ADMITTED.issubset(ids["DA_VALUTARE"]))
        self.assertFalse(ADMITTED & ids["DA_VERIFICARE"])
        self.assertEqual(len(set.union(*ids.values())), 74)
        self.assertIn("PROPOSTA / PARTIAL_REUSE", pages["DA_VALUTARE"])
        self.assertIn("non sono", pages["DA_VALUTARE"].lower())

        with io.StringIO(self.views[prefix + "TABELLA.csv"]) as stream:
            entries = list(csv.DictReader(stream))
        self.assertEqual(len(entries), 74)
        for row in entries:
            if row["CAP_ID"] in ADMITTED:
                self.assertEqual(row["Categoria"], "DA_VALUTARE")
                self.assertEqual(row["Stato"], "PROPOSTA / PARTIAL_REUSE")
            self.assertIn(row["Categoria"], {"DA_VALUTARE",
                "DA_VERIFICARE", "GIA_INTEGRATI"})

    def test_fail_closed_for_existing_source_or_out_of_scope(self):
        record = next(r for r in self.records if r["id"] == "CAP-0093")
        with self.assertRaises(ValueError):
            admitted_product_evaluation(
                record, "Agenda-per-Anna", "SOURCE_REPORTED", "PARTIAL_REUSE")
        with self.assertRaises(ValueError):
            admitted_product_evaluation(
                record, "Agenda-per-Anna", "PROPOSTA", "OUT_OF_SCOPE")
        with self.assertRaises(ValueError):
            admitted_product_evaluation(
                record, "Notes-Ecosistema", "PROPOSTA", "PARTIAL_REUSE")
        self.assertIsNone(admitted_product_evaluation(
            record, "FocuSense", "PROPOSTA", "PARTIAL_REUSE"))

    def test_original_existing_source_and_cross_app_queues_remain(self):
        prefix = "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/Agenda-per-Anna/"
        self.assertIn("CAP-0015", self.views[prefix+"DA_VERIFICARE.md"])
        self.assertIn("CAP-0102", self.views[prefix+"DA_VERIFICARE.md"])
        self.assertIn("CAP-0142", self.views[prefix+"DA_VERIFICARE.md"])
        self.assertIn("CAP-0146", self.views[prefix+"DA_VERIFICARE.md"])
        self.assertIn("CAP-0001", self.views[prefix+"GIA_INTEGRATI.md"])
        self.assertIn("CAP-0093", self.views["DA_VALUTARE.md"])
        self.assertIn("CAP-0093", self.views[
            "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/Agenda-per-Anna/DA_VALUTARE.md"])
        self.assertIn("CAP-0093", self.views[
            "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/Notes-Ecosistema/DA_VERIFICARE.md"])

if __name__ == "__main__":
    unittest.main()
