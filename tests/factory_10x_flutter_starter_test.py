import json
import tempfile
import unittest
from pathlib import Path

from scripts.factory_10x_flutter_starter import bootstrap, FILES


class StarterKitTests(unittest.TestCase):
    def test_generates_complete_minimal_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "starter"
            paths = bootstrap("demo_starter", root)
            self.assertEqual(len(paths), len(FILES))
            self.assertEqual({p.relative_to(root).as_posix() for p in paths}, set(FILES))
            pubspec = (root / "pubspec.yaml").read_text()
            self.assertIn("name: demo_starter", pubspec)
            self.assertIn("flutter_localizations:", pubspec)
            self.assertNotIn("firebase", pubspec.lower())
            for locale in ("en", "it"):
                data = json.loads((root / f"lib/l10n/app_{locale}.arb").read_text())
                self.assertEqual(data["@@locale"], locale)
                self.assertEqual(set(data) - {"@@locale"}, {"homeTitle", "continueLabel", "welcomeMessage"})
            self.assertIn("MaterialApp(", (root / "lib/main.dart").read_text())
            self.assertIn("AppTokens.theme", (root / "lib/main.dart").read_text())
            self.assertIn("Brightness.dark", (root / "lib/main.dart").read_text())
            self.assertIn("testWidgets", (root / "test/widget_test.dart").read_text())
            self.assertNotIn("__APP_NAME__", "\n".join(p.read_text() for p in paths))

    def test_rejects_unsafe_names(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ("../escape", "BadPackage", "xy", "has spaces", "app-name"):
                with self.assertRaises(ValueError):
                    bootstrap(name, Path(directory) / name.replace("/", "_"))

    def test_non_destructive_if_destination_exists(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "existing"
            root.mkdir()
            important = root / "important.txt"
            important.write_text("keep")
            with self.assertRaises(FileExistsError):
                bootstrap("good_name", root)
            self.assertEqual(important.read_text(), "keep")

    def test_rejects_symlink_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target"
            target.mkdir()
            link = Path(directory) / "link"
            link.symlink_to(target, target_is_directory=True)
            with self.assertRaises(ValueError):
                bootstrap("good_name", link)


if __name__ == "__main__":
    unittest.main()
