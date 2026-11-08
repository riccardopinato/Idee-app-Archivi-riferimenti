#!/usr/bin/env python3
"""Read-only, heuristic scan of local Flutter/Dart checkouts.

Findings are candidates, not proof of runtime defects. No network, no writes to
scanned repositories, no automatic fixes or promotion of capability evidence.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RULES = (
    ("deprecated_button", "LEGACY_API", re.compile(r"\b(?:RaisedButton|FlatButton|OutlineButton)\s*\(")),
    ("legacy_snackbar", "LEGACY_API", re.compile(r"\bScaffold\s*\.\s*of\s*\([^)]*\)\s*\.\s*showSnackBar\s*\(")),
    ("legacy_geolocator_instance", "LEGACY_API", re.compile(r"\bGeolocator\s*\(")),
    ("legacy_theme_field", "REVIEW", re.compile(r"\b(?:accentColor|buttonColor|hintColor)\s*:")),
    ("named_navigation", "REVIEW", re.compile(r"\bNavigator\s*\.\s*pushNamed\s*\(")),
    ("legacy_preferences", "REVIEW", re.compile(r"\bSharedPreferences\s*\.\s*getInstance\s*\(")),
    ("native_dart_io", "REVIEW", re.compile(r"\b(?:import|export)\s+['\"]dart:io['\"]")),
    ("eager_listview", "REVIEW", re.compile(r"\bListView\s*\(")),
    ("async_void_handler", "REVIEW", re.compile(r"\bvoid\s+\w+\s*\([^;{}]*\)\s*async\s*\{", re.S)),
)
SKIP_DIRS = {".git", ".dart_tool", "build", "node_modules", ".symlinks", ".fvm"}
SKIP_SUFFIXES = (".g.dart", ".freezed.dart", ".gr.dart", ".mocks.dart")


def scan(root: Path, max_findings: int = 5000) -> dict:
    if not root.is_dir():
        raise ValueError(f"Not a local directory: {root}")
    findings = []
    scanned = 0
    skipped = 0
    for path in sorted(root.rglob("*.dart")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts) or path.name.endswith(SKIP_SUFFIXES):
            skipped += 1
            continue
        if path.is_symlink():
            skipped += 1
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            skipped += 1
            continue
        scanned += 1
        for rid, category, pattern in RULES:
            for match in pattern.finditer(content):
                if len(findings) >= max_findings:
                    return {
                        "root": str(root), "scanned_dart_files": scanned,
                        "skipped_files": skipped, "truncated": True,
                        "findings": findings,
                        "notice": "Heuristic candidates, not confirmed bugs or verified absence.",
                    }
                line = content.count("\n", 0, match.start()) + 1
                snippet = content.splitlines()[line - 1].strip()[:160]
                findings.append({
                    "rule": rid, "category": category, "file": rel.as_posix(),
                    "line": line, "excerpt": snippet,
                })
    return {
        "root": str(root), "scanned_dart_files": scanned,
        "skipped_files": skipped, "truncated": False,
        "findings": findings,
        "notice": "Heuristic candidates, not confirmed bugs or verified absence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", nargs="+", type=Path, help="local repository directories")
    parser.add_argument("--fail-on-legacy-api", action="store_true", help="fail only on high-confidence deprecated APIs")
    parser.add_argument("--max-findings", type=int, default=5000)
    args = parser.parse_args()
    if args.max_findings < 1:
        parser.error("--max-findings must be positive")
    try:
        reports = [scan(root, max_findings=args.max_findings) for root in args.checkout]
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({"schema_version": 1, "reports": reports}, ensure_ascii=False, indent=2))
    return int(args.fail_on_legacy_api and any(
        finding["category"] == "LEGACY_API"
        for report in reports for finding in report["findings"]
    ))


if __name__ == "__main__":
    raise SystemExit(main())
