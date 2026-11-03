"""Regression tests for working-list vs source-integrated separation."""
import csv
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_status_views import parse_ideas, proven_cap, render  # noqa: E402


class OperationalStatusViewTests(unittest.TestCase):
    def test_all_100_idea_ids_are_preserved(self):
        ids = [x["n"] for x in parse_ideas()]
        self.assertEqual(set(ids), set(range(1, 101)))
        self.assertEqual(len(ids), 100)

    def test_only_exact_code_evidence_is_integrated(self):
        data = json.loads((ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
                           / "REGISTRO_CAPABILITY.json").read_text(encoding="utf-8"))
        by_id = {x["id"]: x for x in data["records"]}
        self.assertTrue(proven_cap(by_id["CAP-0001"], "Agenda-per-Anna", "CI_VERIFIED"))
        self.assertFalse(proven_cap(by_id["CAP-0055"], "Agenda-per-Anna", "SOURCE_CONFIRMED"))

    def test_source_reported_ideas_are_not_marked_as_integrated(self):
        views = render()
        self.assertIn("IA26-044.md", views["DA_VALUTARE.md"])
        self.assertNotIn("IA26-044.md", views["GIA_INTEGRATI.md"])
        self.assertIn("IA26-050.md", views["GIA_INTEGRATI.md"])
        self.assertIn("IA26-062.md", views["GIA_INTEGRATI.md"])

    def test_capability_status_is_app_scoped(self):
        views = render()
        self.assertIn("CAP-0001.md", views["GIA_INTEGRATI.md"])
        self.assertIn("CAP-0001.md", views["DA_VALUTARE.md"])

    def test_unbalanced_scores_remain_in_operational_queue(self):
        text = render()["DA_VALUTARE.md"]
        pending = text.split("## Tutte le capability ancora da valutare (", 1)[1].split(
            "## Verificare lo stato", 1)[0]
        self.assertNotIn("## Priorità alta: almeno 85/85", text)
        self.assertNotIn("## Altre capability ancora da valutare", text)
        # Both are high-priority proposals below the old 85% ease cutoff.
        self.assertIn("| CamperBoss | [CAP-0017]", pending)
        self.assertIn("| Wonderlog | [CAP-0017]", pending)
        self.assertIn("| 94 | 80% | PROPOSTA |", pending)
        # Verified source integrations are still excluded.
        self.assertNotIn("| Agenda-per-Anna | [CAP-0001]", pending)

    def test_every_app_is_partitioned_once_and_exported(self):
        data = json.loads((ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
                           / "REGISTRO_CAPABILITY.json").read_text(encoding="utf-8"))
        expected_by_app = {}
        for rec in data["records"]:
            for app in rec["app_states"]:
                expected_by_app.setdefault(app, set()).add(rec["id"])
        views = render()
        self.assertIn("12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/README.md", views)
        for app, expected_ids in expected_by_app.items():
            with self.subTest(app=app):
                folder = "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/" + app + "/"
                groups = {}
                for state in ("DA_VALUTARE", "GIA_INTEGRATI", "DA_VERIFICARE"):
                    content = views[folder + state + ".md"]
                    # Each data row begins with its own canonical CAP link.
                    import re
                    ids = set(re.findall(r"^\\| \\[CAP-(\\d{4})\\]", content, re.M))
                    groups[state] = {"CAP-" + code for code in ids}
                    self.assertEqual(
                        len(ids), content.count("](../../REGISTRO_CAPABILITY/"))
                self.assertEqual(
                    set.union(*groups.values()), expected_ids)
                for left in groups:
                    for right in groups:
                        if left != right:
                            self.assertFalse(groups[left] & groups[right])
                with io.StringIO(views[folder + "TABELLA.csv"]) as stream:
                    exported = list(csv.DictReader(stream))
                self.assertEqual(len(exported), len(expected_ids))
                self.assertEqual({r["CAP_ID"] for r in exported}, expected_ids)
                self.assertEqual({r["Categoria"] for r in exported},
                                 {k for k, v in groups.items() if v})

    def test_one_app_integrated_does_not_mark_other_app_integrated(self):
        views = render()
        base = "12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/"
        anna = views[base + "Agenda-per-Anna/GIA_INTEGRATI.md"]
        focus = views[base + "FocuSense/DA_VALUTARE.md"]
        self.assertIn("CAP-0001", anna)
        self.assertIn("CAP-0001", focus)
        self.assertIn("CAP-0075",
                      views[base + "Agenda-per-Anna/DA_VERIFICARE.md"])
        self.assertNotIn("CAP-0075",
                         views[base + "Agenda-per-Anna/DA_VALUTARE.md"])

    def test_repository_views_match_generator(self):
        for name, expected in render().items():
            with self.subTest(view=name):
                self.assertEqual((ROOT / name).read_text(encoding="utf-8"), expected)


if __name__ == "__main__":
    unittest.main()
