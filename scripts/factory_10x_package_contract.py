#!/usr/bin/env python3
"""Golden package candidate contract: do not confuse a document with a tested library."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "19-APP-FACTORY-10X/contracts"
SCHEMA = CONTRACTS / "golden_package_v1.schema.json"
EXAMPLE = CONTRACTS / "PROFILE_STANDARD_CANDIDATE.json"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PKG = re.compile(r"^[a-z][a-z0-9_]{2,63}$")
STATE = ("DESIGN_ONLY", "SOURCE_EXTRACTED", "PACKAGE_TESTED",
         "CONSUMER_VERIFIED", "CERTIFIED_MULTI_CONSUMER")
SOURCE = ("INTERNAL_GOLDEN", "INTERNAL_DONOR", "NEW_IMPLEMENTATION")


def verify(data: dict) -> str:
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Unsupported package schema")
    if not PKG.fullmatch(str(data.get("package_name", ""))) or not SEMVER.fullmatch(str(data.get("version", ""))):
        raise ValueError("Invalid package name or version")
    level = data.get("package_state")
    if level not in STATE:
        raise ValueError("Invalid package state")
    if not SHA40.fullmatch(str(data.get("factory_sha", ""))):
        raise ValueError("Factory commit not pinned")
    golden, prov = data.get("golden"), data.get("provenance")
    if not isinstance(golden, dict) or not isinstance(prov, dict):
        raise ValueError("Missing Golden and donor provenance")
    if golden.get("registry_sha") != data["factory_sha"] or not golden.get("path", "").startswith("golden/"):
        raise ValueError("Golden registry must be pinned to Factory baseline")
    if not golden.get("id") or not golden.get("registry_status"):
        raise ValueError("Golden ID/status missing")
    if prov.get("origin") not in SOURCE or not SHA40.fullmatch(str(prov.get("donor_sha", ""))):
        raise ValueError("Invalid donor provenance")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", str(prov.get("donor_repo", ""))):
        raise ValueError("Donor repository invalid")
    src = prov.get("source_url", "")
    if not isinstance(src, str) or not src.startswith("https://github.com/") or data["factory_sha"] not in src:
        raise ValueError("Source link must be pinned")
    paths = prov.get("source_files")
    if not isinstance(paths, list) or len(set(paths)) != len(paths):
        raise ValueError("Source file inventory invalid")
    if any(not isinstance(p, str) or not p or p.startswith("/") or ".." in p.split("/") for p in paths):
        raise ValueError("Source paths unsafe")
    license = data.get("license")
    if license not in {"NOT_REVIEWED", "INTERNAL_APPROVED", "SPDX_VERIFIED"}:
        raise ValueError("Unknown license state")
    compat, tests = data.get("compatibility"), data.get("tests")
    if not isinstance(compat, dict) or not isinstance(tests, dict):
        raise ValueError("Missing compatibility/test metadata")
    pairs = compat.get("tested_pairs")
    if not isinstance(pairs, list):
        raise ValueError("Tested pairs missing")
    urls = tests.get("donor_ci_urls"), tests.get("consumer_ci_urls")
    if not all(isinstance(x, list) for x in urls):
        raise ValueError("Tests must be arrays")
    if any(not isinstance(u, str) or not u.startswith("https://github.com/") for seq in urls for u in seq):
        raise ValueError("Tests require GitHub source URLs")
    if any(not isinstance(p, dict) or not p.get("dart") or not p.get("flutter") or
           not str(p.get("test_url", "")).startswith("https://github.com/") for p in pairs):
        raise ValueError("Compatibility tests require exact evidence")
    dependencies = data.get("dependencies")
    if not isinstance(dependencies, dict) or any(
        not isinstance(k, str) or not PKG.fullmatch(k) or not isinstance(v, str)
        or not SEMVER.fullmatch(v) for k, v in dependencies.items()
    ):
        raise ValueError("Unpinned or invalid dependencies")
    consumers = data.get("consumers")
    if not isinstance(consumers, list):
        raise ValueError("Invalid consumer matrix")
    repos = set()
    for c in consumers:
        if not isinstance(c, dict) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", str(c.get("repo", ""))):
            raise ValueError("Invalid consumer repository")
        if c["repo"] in repos or not SHA40.fullmatch(str(c.get("source_sha", ""))):
            raise ValueError("Duplicate/missing consumer exact head")
        repos.add(c["repo"])
        if c.get("approved") is not True or not str(c.get("test_url", "")).startswith("https://github.com/"):
            raise ValueError("Consumer needs approval and CI proof")
    release = data.get("release")
    if not isinstance(release, dict) or not isinstance(release.get("publish_authorized"), bool):
        raise ValueError("Missing release gate")
    artifact = release.get("artifact_sha256")
    if artifact is not None and not SHA256.fullmatch(str(artifact)):
        raise ValueError("Invalid package artifact identity")
    if level != "DESIGN_ONLY":
        if not paths or license == "NOT_REVIEWED":
            raise ValueError("Extracted package requires source files and license review")
        if not SEMVER.fullmatch(data["version"]) or data["version"] == "0.0.0":
            raise ValueError("Extracted package requires non-placeholder version")
    if STATE.index(level) >= STATE.index("PACKAGE_TESTED"):
        if not pairs or not urls[0] or not compat.get("dart_sdk") or not compat.get("flutter_sdk"):
            raise ValueError("Package tests and SDK matrix required")
    if STATE.index(level) >= STATE.index("CONSUMER_VERIFIED"):
        if not consumers or not urls[1]:
            raise ValueError("Consumer adoption needs test evidence")
    if level == "CERTIFIED_MULTI_CONSUMER" and len(consumers) < 2:
        raise ValueError("Certification requires two independent consumers")
    if release["publish_authorized"]:
        if STATE.index(level) < STATE.index("CONSUMER_VERIFIED") or not artifact:
            raise ValueError("Publish gate requires scoped consumer and built artifact")
        if not release.get("rollback_version"):
            raise ValueError("Publish gate requires rollback")
    elif artifact and level == "DESIGN_ONLY":
        raise ValueError("Design-only manifest cannot claim a real package artifact")
    return level


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, default=EXAMPLE)
    ap.add_argument("--check", action="store_true")
    args=ap.parse_args()
    json.loads(SCHEMA.read_text(encoding="utf-8"))
    data=json.loads(args.manifest.read_text(encoding="utf-8"))
    state=verify(data)
    print("GOLDEN_PACKAGE_CONTRACT_CHECK_PASS "+state+" "+data["package_name"])


if __name__=="__main__":
    main()
