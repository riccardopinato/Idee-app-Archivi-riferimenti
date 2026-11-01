"""Regression: evidence promotion must never remove a documented capability."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
SCANNER = ROOT / "scripts" / "build_catalog.py"
EVIDENCE_STAGES = ("SOURCE_CONFIRMED", "CI_VERIFIED", "DEVICE_VERIFIED", "RELEASE")


class CapabilityEvidencePromotionTest(unittest.TestCase):
    def test_promoted_status_remains_in_implementations(self):
        original = json.loads((CAT / "REGISTRO_CAPABILITY.json").read_text(encoding="utf-8"))
        inventory = (CAT / "SOURCE_INVENTORY.json").read_text(encoding="utf-8")
        script = SCANNER.read_text(encoding="utf-8")
        for stage in EVIDENCE_STAGES:
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "scripts").mkdir()
                (root / "scripts" / "build_catalog.py").write_text(script, encoding="utf-8")
                base = root / "12-CAPABILITY-E-IMPLEMENTAZIONI"
                base.mkdir()
                data = json.loads(json.dumps(original))
                record = next(rec for rec in data["records"] if rec["id"] == "CAP-0004")
                record["app_states"]["Agenda-per-Anna"] = stage
                (base / "REGISTRO_CAPABILITY.json").write_text(
                    json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
                (base / "SOURCE_INVENTORY.json").write_text(inventory, encoding="utf-8")
                # This fixture isolates evidence promotion from donor kit contents.
                # The generator also validates six kit files per CAP: stub only their
                # required presence here, keeping full repository checks strict.
                kit_root = root / "13-KIT-INTEGRAZIONE"
                required_kit_files = (
                    "README.md", "SPECIFICHE.md", "CODICE_RIFERIMENTO.txt",
                    "INTEGRAZIONE_FLUTTER.md", "LICENZE_E_DIPENDENZE.md",
                    "TEST_E_VALIDAZIONE.md",
                )
                for capability in data["records"]:
                    kit_dir = kit_root / capability["id"]
                    kit_dir.mkdir(parents=True, exist_ok=True)
                    for filename in required_kit_files:
                        (kit_dir / filename).touch()

                generated = subprocess.run(
                    [sys.executable, str(root / "scripts" / "build_catalog.py")],
                    capture_output=True, text=True, check=True)
                self.assertIn("VALID:", generated.stdout)
                status_page = (base / "STATO_IMPLEMENTAZIONI.md").read_text(encoding="utf-8")
                self.assertIn(f"Agenda-per-Anna ({stage})", status_page)
                self.assertIn("CAP-0004 Overlay calendari esterni read-only", status_page)
                subprocess.run(
                    [sys.executable, str(root / "scripts" / "build_catalog.py"), "--check"],
                    capture_output=True, text=True, check=True)


if __name__ == "__main__":
    unittest.main()
