"""Offline regression contract for optional GitHub Projects V2 mirror.

No network, PAT, GitHub Project or app repository required to run these tests.
"""
import json
import sys
import unittest
from unittest.mock import patch
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import projects_sync as mirror


def fake_fields():
    return {
        "App": {"id": "F_APP", "__typename": "ProjectV2Field",
                "name": "App", "dataType": "TEXT"},
        "Priorità": {"id": "F_PRI", "__typename": "ProjectV2Field",
                     "name": "Priorità", "dataType": "NUMBER"},
        "Facilità": {"id": "F_EASE", "__typename": "ProjectV2Field",
                     "name": "Facilità", "dataType": "NUMBER"},
        "Fase": {"id": "F_PHASE", "__typename": "ProjectV2SingleSelectField",
                 "name": "Fase", "options": [
                     {"id": "O_A", "name": "Da valutare"},
                     {"id": "O_B", "name": "Già integrati"},
                     {"id": "O_C", "name": "Da verificare"},
                 ]},
    }


class FakeMutationClient:
    """Captures and executes API mutation effects in memory."""
    def __init__(self):
        self.items = []
        self.creates = self.writes = 0

    def call(self, query, variables=None):
        variables = variables or {}
        if "addProjectV2DraftIssue" in query:
            self.creates += 1
            incoming = variables["input"]
            item_id = "PVTI_" + str(len(self.items) + 1)
            item = {"id": item_id, "title": incoming["title"],
                    "body": incoming["body"], "values": {}}
            self.items.append(item)
            return {"addProjectV2DraftIssue": {
                "projectItem": {"id": item_id, "content": {"id": "D_" + item_id}}
            }}
        if "updateProjectV2ItemFieldValue" in query:
            for payload in variables.values():
                self.writes += 1
                item = next(i for i in self.items if i["id"] == payload["itemId"])
                value = next(iter(payload["value"].values()))
                item["values"][payload["fieldId"]] = value
            return {"ok": True}
        raise AssertionError("Unsupported test API operation")


class ProjectsMirrorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = mirror.load_rows()

    def test_source_coverage_all_apps_without_any_score_cutoff(self):
        data = json.loads((ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI" /
                           "REGISTRO_CAPABILITY.json").read_text(encoding="utf-8"))
        pairs = sum(len(c["app_states"]) for c in data["records"])
        self.assertEqual(pairs, len(self.rows))
        self.assertEqual(len(self.rows), 342)
        self.assertEqual(len({r["app"] for r in self.rows}), 48)
        self.assertEqual(len({mirror.row_key(r) for r in self.rows}), len(self.rows))
        self.assertEqual(Counter(r["category"] for r in self.rows), {
            "DA_VALUTARE": 214, "GIA_INTEGRATI": 8, "DA_VERIFICARE": 120,
        })
        self.assertTrue(any(r["score"] == 94 and r["ease"] == 80
                            and r["category"] == "DA_VALUTARE" for r in self.rows))

    def test_app_specific_state_does_not_leak_to_other_app(self):
        indexed = {(r["app"], r["cap"]): r for r in self.rows}
        self.assertEqual(indexed["Agenda-per-Anna", "CAP-0001"]["category"],
                         "GIA_INTEGRATI")
        self.assertEqual(indexed["FocuSense", "CAP-0001"]["category"],
                         "DA_VALUTARE")
        self.assertEqual(indexed["Agenda-per-Anna", "CAP-0075"]["category"],
                         "DA_VERIFICARE")

    def test_pilot_has_all_three_states_and_unique_ids(self):
        pilot = mirror.pilot_rows(self.rows)
        self.assertEqual(len(pilot), 6)
        self.assertEqual({r["category"] for r in pilot}, set(mirror.CATEGORIES))
        self.assertEqual(len({mirror.row_key(r) for r in pilot}), 6)

    def test_no_writes_in_dry_run_even_without_credentials(self):
        mirror.main(["--mode", "dry-run"])

    def test_marker_roundtrip_is_stable(self):
        for row in mirror.pilot_rows(self.rows):
            tag = mirror.marker(row)
            match = mirror.MARKER_PATTERN.search(mirror.draft_body(row))
            self.assertEqual((match.group(1), match.group(2)), mirror.row_key(row))
            self.assertIn(row["reference"], mirror.draft_body(row))
            self.assertIn("APP_FACTORY_CAP_PAIR", tag)

    def test_pilot_then_full_is_idempotent_without_deletes(self):
        client = FakeMutationClient()
        fields, project, existing = fake_fields(), {"id": "PROJECT_TEST"}, {}
        pilot = mirror.pilot_rows(self.rows)
        mirror.upsert(client, project, fields, pilot, existing)
        self.assertEqual(client.creates, 6)
        self.assertEqual(len(existing), 6)
        pilot_writes = client.writes
        mirror.upsert(client, project, fields, pilot, existing)
        self.assertEqual(client.creates, 6)
        self.assertEqual(client.writes, pilot_writes)
        mirror.upsert(client, project, fields, self.rows, existing)
        self.assertEqual(client.creates, len(self.rows))
        self.assertEqual(len(existing), len(self.rows))
        full_writes = client.writes
        mirror.upsert(client, project, fields, self.rows, existing)
        self.assertEqual(client.creates, len(self.rows))
        self.assertEqual(client.writes, full_writes)
        self.assertEqual(len(client.items), len(self.rows))

    def test_rate_limited_batches_cover_all_342_without_duplicates(self):
        fields = fake_fields()
        project_id = "PROJECT_TEST"
        empty = {}
        batch, remaining = mirror.select_pending(
            self.rows, empty, fields, project_id)
        self.assertEqual(len(batch), mirror.MAX_ITEMS_PER_RUN)
        self.assertEqual(remaining, len(self.rows))
        self.assertEqual(mirror.MAX_ITEMS_PER_RUN, 180)
        self.assertGreaterEqual(mirror.MUTATION_INTERVAL_SECONDS, 1.0)

        existing = {}
        for idx, row in enumerate(batch):
            fields_for_row = mirror.desired_fields(row, fields)
            existing[mirror.row_key(row)] = {
                "item_id": "PV_" + str(idx),
                "values": {key: next(iter(value.values()))
                           for key, value in fields_for_row.items()},
            }
        second, count = mirror.select_pending(
            self.rows, existing, fields, project_id)
        self.assertEqual(count, len(self.rows) - len(batch))
        self.assertEqual(len(second), len(self.rows) - len(batch))
        self.assertFalse({mirror.row_key(x) for x in batch} &
                         {mirror.row_key(x) for x in second})

    def test_eventual_consistency_does_not_recreate_pilot_items(self):
        rows = mirror.pilot_rows(self.rows)
        fields = fake_fields()
        fully_indexed = {}
        for idx, row in enumerate(rows):
            desired = mirror.desired_fields(row, fields)
            fully_indexed[mirror.row_key(row)] = {
                "item_id": "PV_" + str(idx),
                "values": {name: next(iter(value.values()))
                           for name, value in desired.items()},
            }
        missing_last = dict(fully_indexed)
        missing_last.pop(mirror.row_key(rows[-1]))
        with patch.object(mirror, "read_project_items",
                          side_effect=[missing_last, fully_indexed]) as remote_read, \
             patch.object(mirror.time, "sleep") as sleep:
            verified = mirror.assert_remote(None, 1, rows, fields)
        self.assertEqual(verified, fully_indexed)
        self.assertEqual(remote_read.call_count, 2)
        sleep.assert_called_once()

    def test_verification_fails_without_mutations_if_remote_never_settles(self):
        rows = mirror.pilot_rows(self.rows)
        with patch.object(mirror, "read_project_items",
                          return_value={}) as remote_read, \
             patch.object(mirror.time, "sleep") as sleep:
            with self.assertRaisesRegex(RuntimeError, "did not settle"):
                mirror.assert_remote(None, 1, rows, fake_fields(), max_attempts=3)
        self.assertEqual(remote_read.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_changes_only_update_owned_fields(self):
        client = FakeMutationClient()
        fields, project, existing = fake_fields(), {"id": "PROJECT_TEST"}, {}
        row = dict(self.rows[0])
        mirror.upsert(client, project, fields, [row], existing)
        created = client.creates
        writes = client.writes
        changed = dict(row, score=row["score"] - 1, ease=row["ease"] - 2)
        mirror.upsert(client, project, fields, [changed], existing)
        self.assertEqual(client.creates, created)
        self.assertEqual(client.writes, writes + 2)
        self.assertEqual(client.items[0]["values"]["F_PRI"], float(changed["score"]))
        self.assertEqual(client.items[0]["values"]["F_EASE"], float(changed["ease"]))

    def test_existing_unrelated_items_are_not_targeted(self):
        pilot = mirror.pilot_rows(self.rows)
        existing = {mirror.row_key(pilot[0]): {"item_id": "P1", "values": {}}}
        a, b = mirror.project_plan(pilot, existing)
        self.assertEqual(len(a), 5)
        self.assertEqual(len(b), 1)
        self.assertNotIn(("unrelated", "CAP-0001"),
                         {mirror.row_key(x) for x in a})


if __name__ == "__main__":
    unittest.main()
