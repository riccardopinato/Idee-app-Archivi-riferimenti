#!/usr/bin/env python3
"""Check the ML source intake registry and relative documentation links.

This checks the catalog *shape*, not licensing, model quality or E3/E5 evidence.
"""
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
HUB = ROOT / "14-MACHINE-LEARNING"
FILES = [
    "README.md",
    "INBOX_REPOSITORY.md",
    "PROTOCOLLO_AUDIT_ML.md",
    "TEMPLATE_SCHEDA_REPOSITORY.md",
    "CROSSWALK_ML_ESISTENTE.md",
    "REGISTRO_FONTI_ML.json",
]

def main() -> None:
    for name in FILES:
        assert (HUB / name).is_file(), f"Missing ML hub file: {name}"

    obj = json.loads((HUB / "REGISTRO_FONTI_ML.json").read_text(encoding="utf-8"))
    assert obj.get("schema_version") == 1, "Unexpected ML registry schema"
    assert obj.get("canonical_capability_registry") == (
        "12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json"
    ), "ML records must not replace the canonical CAP registry"
    rows = obj.get("records")
    assert isinstance(rows, list), "ML records must be a list"

    seen_ids = set()
    seen_urls = set()
    required = {"id", "url", "first_seen_date", "status", "source_sha",
                "audit_depth", "licensing", "technical_roles", "capability_ids",
                "summary_file", "evidence_urls", "next_gate"}
    for row in rows:
        assert isinstance(row, dict) and required.issubset(row), "Incomplete ML source entry"
        key = row["id"]
        url = row["url"].rstrip("/").lower()
        assert re.fullmatch(r"MLR-[0-9]{4,}", key), f"Invalid MLR ID: {key}"
        assert key not in seen_ids and url not in seen_urls, f"Duplicate MLR: {key} / {url}"
        assert url.startswith("https://github.com/"), f"Expected GitHub source URL: {url}"
        sha = row["source_sha"]
        assert sha is None or sha == "NON_VERIFICATO" or (
            isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{40}", sha)
        ), f"Bad SHA in {key}"
        seen_ids.add(key)
        seen_urls.add(url)

    for md in HUB.glob("*.md"):
        body = md.read_text(encoding="utf-8")
        for dest in re.findall(r"\]\(([^\s)]+)\)", body):
            if dest.startswith(("https://", "http://", "#", "mailto:")):
                continue
            rel = unquote(dest.split("#", 1)[0])
            if not rel:
                continue
            path = (md.parent / rel).resolve()
            assert path.is_relative_to(ROOT.resolve()), f"Escaping link {dest} from {md.name}"
            assert path.exists(), f"Broken link {dest} from {md.name}"

    homepage = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "14-MACHINE-LEARNING/README.md" in homepage, "Missing home navigation"
    print(f"ML intake validation PASS: {len(FILES)} files, {len(rows)} sources, documentation links")


if __name__ == "__main__":
    main()
