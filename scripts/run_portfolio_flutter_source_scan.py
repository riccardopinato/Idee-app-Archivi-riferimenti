#!/usr/bin/env python3
"""Read-only GitHub Actions full-checkout scanner for public Flutter repositories."""
from __future__ import annotations
import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI" / "SOURCE_INVENTORY.json"
SCANNER = ROOT / "scripts" / "audit_flutter_antipatterns.py"
PRIVATE = {"Cozy-game-nome-da-scegliere-", "desktop-tutorial", "FrameLab-Google-AI-Studio"}
INFRA = {"App-Factory-Core", "AppLab", "Idee-app-Archivi-riferimenti"}
spec = importlib.util.spec_from_file_location("flutter_source_scan", SCANNER)
scan_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan_module)

def scan_checkout(item, workdir):
    name, branch = item["name"], item["default_branch"]
    entry = {"repo": name, "default_branch": branch}
    if name in PRIVATE:
        return dict(entry, status="SKIPPED_PRIVATE_GITHUB_ACTIONS")
    if name in INFRA:
        return dict(entry, status="EXCLUDED_INFRASTRUCTURE")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", name) or branch not in {"main", "master"}:
        return dict(entry, status="INVALID_INVENTORY")
    dest = workdir / name
    p = subprocess.run([
        "git", "-c", "http.version=HTTP/1.1", "clone", "--depth=1",
        "--single-branch", "--branch", branch,
        "https://github.com/riccardopinato/" + name + ".git", str(dest),
    ], capture_output=True, text=True, timeout=210, env={
        **os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1",
    })
    if p.returncode:
        return dict(entry, status="CLONE_FAILED", error=p.stderr[-1000:])
    entry["source_sha"] = subprocess.check_output(
        ["git", "-C", str(dest), "rev-parse", "HEAD"], text=True,
    ).strip()
    pubspecs = []
    for f in dest.rglob("pubspec.yaml"):
        rel = f.relative_to(dest)
        if any(segment.startswith(".") or segment in scan_module.SKIP_DIRS for segment in rel.parts):
            continue
        try:
            src = f.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        if re.search(r"(?m)^\s{2}flutter\s*:\s*$", src):
            pubspecs.append(rel.as_posix())
    entry["flutter_pubspec_paths"] = sorted(pubspecs)
    if not pubspecs:
        return dict(entry, status="NOT_FLUTTER")
    report = scan_module.scan(dest, max_findings=30000)
    entry.update(
        status="SCANNED",
        scanned_dart_files=report["scanned_dart_files"],
        skipped_dart_files=report["skipped_files"],
        truncated=report["truncated"],
        legacy_api_detected=report["legacy_api_detected"],
        findings=report["findings"],
        counts=dict(Counter(x["rule"] for x in report["findings"])),
    )
    return entry

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--markdown", type=Path, required=True)
    args = ap.parse_args()
    args.workdir.mkdir(parents=True, exist_ok=True)
    items = json.loads(INVENTORY.read_text(encoding="utf-8"))["repositories"]
    results = []
    for item in items:
        try:
            entry = scan_checkout(item, args.workdir)
        except (OSError, subprocess.TimeoutExpired, ValueError) as exc:
            entry = {"repo": item["name"], "status": "SCAN_FAILED", "error": str(exc)[:500]}
        results.append(entry)
        print("SOURCE_SCAN|" + json.dumps({k: v for k, v in entry.items() if k != "findings"}, ensure_ascii=False), flush=True)
    complete = [x for x in results if x["status"] == "SCANNED"]
    failures = [x for x in results if x["status"] in ("SCAN_FAILED", "CLONE_FAILED", "INVALID_INVENTORY")]
    summary = {
        "schema_version": 1,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "method": "Temporary full git checkouts of public owner repos; lexical .dart scanning; no runtime verification.",
        "inventory_count": len(items),
        "flutter_public_scanned": len(complete),
        "public_failures": len(failures),
        "private_excluded": [x["repo"] for x in results if x["status"] == "SKIPPED_PRIVATE_GITHUB_ACTIONS"],
        "legacy_repo_count": sum(bool(x["legacy_api_detected"]) for x in complete),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Flutter portfolio scanner — evidenze da checkout completo",
        "",
        "Data UTC: " + summary["generated_at_utc"],
        "Numero repo inventariati: " + str(summary["inventory_count"]),
        "Repo Flutter pubblici scansionati: " + str(summary["flutter_public_scanned"]),
        "Errori pubblici: " + str(summary["public_failures"]),
        "Repo privati esclusi da GitHub Actions: " + ", ".join(summary["private_excluded"]),
        "",
        "| Repository | SHA | Dart | Legacy API | Review | Stato |",
        "|---|---|---:|---:|---:|---|",
    ]
    for x in results:
        counts = x.get("counts", {})
        old = sum(v for k, v in counts.items() if k in {
            "deprecated_button", "legacy_snackbar", "legacy_geolocator_instance"})
        lines.append("| " + x["repo"] + " | " + x.get("source_sha", "-")[:12] +
                     " | " + str(x.get("scanned_dart_files", 0)) +
                     " | " + str(old) + " | " + str(sum(counts.values()) - old) +
                     " | " + x["status"] + " |")
        if x.get("legacy_api_detected"):
            lines.append("")
            lines.append("## Legacy findings — " + x["repo"])
            legacy = [f for f in x.get("findings", []) if f["category"] == "LEGACY_API"]
            for found in legacy[:15]:
                lines.append("- " + found["file"] + ":" + str(found["line"]) +
                             " " + found["rule"] + " — " + found["excerpt"])
            if len(legacy) > 15:
                lines.append("- altri " + str(len(legacy) - 15) + " nel JSON")
    lines += ["", "NOTE: non è flutter analyze né benchmark runtime.",
              "Gli zero findings significano solo nessun pattern euristico trovato.",
              "I risultati REVIEW non provano bug. Codice generato e path esclusi dichiarati nel JSON."]
    args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("SOURCE_SCAN_SUMMARY|" + json.dumps({
        k: v for k, v in summary.items() if k != "results"
    }, ensure_ascii=False), flush=True)
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
