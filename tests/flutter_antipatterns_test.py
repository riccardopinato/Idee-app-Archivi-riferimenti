"""Tests for bounded, read-only Flutter static heuristic scanner."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_flutter_antipatterns.py"
spec = importlib.util.spec_from_file_location("htmlit_flutter_scan", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FlutterAntipatternScannerTest(unittest.TestCase):
    def test_scan_flags_legacy_without_misreading_future_void(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "lib").mkdir()
            (root / "lib" / "demo.dart").write_text(
                "Future<void> save() async {}\n"
                "void onPressed() async { await save(); }\n"
                "final x = RaisedButton(onPressed: null);\n"
                "final y = ListView(children: []);\n"
                "final z = Scaffold.of(context).showSnackBar(a);\n",
                encoding="utf-8",
            )
            (root / "lib" / "generated.g.dart").write_text("RaisedButton();", encoding="utf-8")
            report = module.scan(root)
            rules = [x["rule"] for x in report["findings"]]
            self.assertEqual(report["scanned_dart_files"], 1)
            self.assertEqual(report["skipped_files"], 1)
            self.assertEqual(rules.count("deprecated_button"), 1)
            self.assertIn("legacy_snackbar", rules)
            self.assertIn("eager_listview", rules)
            self.assertEqual(rules.count("async_void_handler"), 1)
            self.assertFalse(any(x["line"] == 1 and x["rule"] == "async_void_handler" for x in report["findings"]))

    def test_safe_code_is_not_bug(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "main.dart").write_text(
                "Future<void> save() async { await repo.write(); }\n"
                "final list = ListView.builder(itemBuilder: build);\n",
                encoding="utf-8",
            )
            report = module.scan(root)
            self.assertEqual(report["findings"], [])


if __name__ == "__main__":
    unittest.main()
