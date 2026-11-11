#!/usr/bin/env python3
"""Validate and conservatively reconcile the public App Factory fleet projection.

Never alters source repositories, PRs, Master, CAP or Golden.
No GitHub token, SDK or network calls are used by this module.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLEET = ROOT / "16-APP-FACTORY-SITE/data/context_fleet.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
ALLOWED = {"CONTRACT_CI_VERIFIED", "BLOCKED_PR_PERMISSION",
           "PR_FLOW_VERIFIED", "SCHEDULE_VERIFIED", "SEMANTIC_REVIEW_PENDING"}
GITHUB = "https://github.com/"


def validate(data):
    if data.get("schema_version") != 1 or not SHA.fullmatch(str(data.get("factory_baseline_sha", ""))):
        raise ValueError("Invalid schema or Factory baseline")
    if not data.get("generated_at", "").endswith("Z"):
        raise ValueError("generated_at must be UTC ISO")
    rows = data.get("repositories")
    if not isinstance(rows, list) or len(rows) != 35:
        raise ValueError("Must reconcile exactly 35 current repository slots")
    ids = [r["id"] for r in rows]
    if len(set(ids)) != 35:
        raise ValueError("Duplicate repository IDs")
    public = [r for r in rows if r["visibility"] == "public"]
    private = [r for r in rows if r["visibility"] == "private"]
    if len(public) != 32 or len(private) != 3:
        raise ValueError("Unexpected public/private coverage; re-audit inventory")
    for r in rows:
        if r.get("state") not in ALLOWED:
            raise ValueError("Invalid or uncertified workflow status")
        if not (r.get("schedule_configured") and r.get("dispatch_configured")):
            raise ValueError("Missing workflow trigger configuration")
        if r["visibility"] == "private":
            for key in ("repository", "source_sha", "source_url", "last_checked_sha",
                        "schedule_cron_utc", "evidence_url", "last_snapshot_run",
                        "last_successful_snapshot_run", "open_snapshot_pr"):
                if r.get(key) is not None:
                    raise ValueError("Private repository identity or evidence leaked: " + key)
        else:
            repo = r["repository"]
            sha = r.get("source_sha")
            if not repo or not repo.startswith("riccardopinato/"):
                raise ValueError("Invalid public repository name")
            if not SHA.fullmatch(str(sha)) or not SHA.fullmatch(str(r.get("last_checked_sha"))):
                raise ValueError("Source commit SHA unavailable")
            if r["source_url"] != GITHUB + repo + "/commit/" + sha:
                raise ValueError("Source provenance does not pin exact repo commit")
            if not r.get("schedule_cron_utc") or not r.get("workflow_file"):
                raise ValueError("Workflow source missing")
            for field in ("last_snapshot_run", "open_snapshot_pr", "evidence_url"):
                value = r.get(field)
                if value is not None and not value.startswith(GITHUB + repo + "/"):
                    raise ValueError("Cross-repository evidence URL: " + field)
        if r["bot_pr_verified"]:
            if r["state"] not in ("PR_FLOW_VERIFIED", "SCHEDULE_VERIFIED") or not r.get("open_snapshot_pr") or not r.get("last_successful_snapshot_run"):
                raise ValueError("Bot PR state requires live run + bot-created PR")
        if r["schedule_verified"]:
            if r.get("last_snapshot_event") != "schedule" or r.get("last_snapshot_result") != "success":
                raise ValueError("Schedule claim without schedule success")
        if r["dispatch_verified"] and r.get("last_snapshot_event") != "workflow_dispatch":
            raise ValueError("Dispatch claim without manual event")
    summary = data.get("summary", {})
    expected = {"total": len(rows), "public": len(public), "private": len(private),
                "workflow_installed": len(rows), "config_verified": len(rows),
                "bot_pr_verified": sum(r["bot_pr_verified"] for r in rows),
                "schedule_verified": sum(r["schedule_verified"] for r in rows),
                "dispatch_verified": sum(r["dispatch_verified"] for r in rows),
                "known_create_pr_blocked": sum(r["state"] == "BLOCKED_PR_PERMISSION" for r in rows),
                "runtime_not_verified": sum(r["last_snapshot_event"] is None for r in rows)}
    if summary != expected:
        raise ValueError("Derived summary inconsistent with underlying source rows")
    return expected


def reconcile(current, observations, as_of):
    """Apply externally verified receipts, append change history; never trust a bare SHA to prove success."""
    out = copy.deepcopy(current)
    validate(out)
    indexed = {r["id"]: r for r in out["repositories"]}
    if not isinstance(observations, list):
        raise ValueError("observations must be list")
    if not isinstance(as_of, str) or not as_of.endswith("Z"):
        raise ValueError("invalid UTC timestamp")
    for obs in observations:
        if not isinstance(obs, dict):
            raise ValueError("invalid observation")
        ident = obs.get("id")
        if ident not in indexed:
            raise ValueError("Unknown repo: " + str(ident))
        row = indexed[ident]
        if row["visibility"] != "public":
            raise ValueError("Private records require a separate private registry")
        event, result = obs.get("event"), obs.get("result")
        url = obs.get("run_url")
        if event not in ("schedule", "workflow_dispatch", "push") or result not in ("success", "failure"):
            raise ValueError("Invalid event/result")
        if not isinstance(url, str) or not url.startswith(GITHUB + row["repository"] + "/actions/runs/"):
            raise ValueError("Missing canonical evidence run URL")
        changed = {"last_snapshot_event": event, "last_snapshot_result": result,
                   "last_snapshot_run": url, "last_checked_at": as_of[:10]}
        if result == "success":
            changed["last_successful_snapshot_run"] = url
        if event == "schedule" and result == "success":
            changed["schedule_verified"] = True
            changed["state"] = "SCHEDULE_VERIFIED"
        if event == "workflow_dispatch" and result == "success":
            changed["dispatch_verified"] = True
        pr = obs.get("pr_url")
        if pr is not None:
            if not pr.startswith(GITHUB + row["repository"] + "/pull/") or obs.get("author") != "github-actions[bot]" or result != "success":
                raise ValueError("Bot PR requires action result and verified actor")
            changed.update(open_snapshot_pr=pr, bot_pr_verified=True)
            if event != "schedule":
                changed["state"] = "PR_FLOW_VERIFIED"
        elif result == "failure" and obs.get("reason") == "PR_CREATE_DENIED":
            changed.update(state="BLOCKED_PR_PERMISSION", error="GITHUB_ACTIONS_CREATE_PR_NOT_ALLOWED",
                           blocked_reason="Owner must enable PR creation in GitHub Actions settings")
        before = {k: row.get(k) for k in changed}
        if before != changed:
            row.update(changed)
            out.setdefault("history", []).append({"id": ident, "at": as_of, "event": event,
                                                   "run_url": url, "before": before, "after": changed})
    out["summary"] = {
        "total": 35, "public": 32, "private": 3,
        "workflow_installed": 35, "config_verified": 35,
        "bot_pr_verified": sum(r["bot_pr_verified"] for r in out["repositories"]),
        "schedule_verified": sum(r["schedule_verified"] for r in out["repositories"]),
        "dispatch_verified": sum(r["dispatch_verified"] for r in out["repositories"]),
        "known_create_pr_blocked": sum(r["state"] == "BLOCKED_PR_PERMISSION" for r in out["repositories"]),
        "runtime_not_verified": sum(r["last_snapshot_event"] is None for r in out["repositories"]),
    }
    if out != current:
        out["generated_at"] = as_of
    validate(out)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Offline schema and provenance verification")
    parser.add_argument("--observations", type=Path, help="Strict receipt JSON input; no network")
    parser.add_argument("--as-of", help="UTC ISO string for observed receipts")
    args = parser.parse_args()
    old = json.loads(FLEET.read_text(encoding="utf-8"))
    validate(old)
    if args.observations:
        if not args.as_of:
            parser.error("--as-of is required with --observations")
        receipts = json.loads(args.observations.read_text(encoding="utf-8"))
        updated = reconcile(old, receipts, args.as_of)
        if updated != old:
            FLEET.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("CONTEXT_FLEET_RECONCILED" if updated != old else "CONTEXT_FLEET_NO_OP")
    else:
        print("CONTEXT_FLEET_CHECK_PASS")


if __name__ == "__main__":
    main()
