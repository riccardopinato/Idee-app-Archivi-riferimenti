#!/usr/bin/env python3
"""App Factory 10x continuous roadmap: offline DAG validator and uncapped safe-ready selector.

No GitHub writes, no network, no async agents, no automatic approval/promotion.
This is a durable executable queue contract, NOT a self-resuming ChatGPT worker.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "19-APP-FACTORY-10X" / "PROGRAM_QUEUE.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
ID = re.compile(r"^X10-\d{3}$")
PRIORITY = {"P0": 0, "P1": 1, "P2": 2}
MODES = {"READ_ONLY", "PR_GATED", "HUMAN_GATE"}
STATUSES = {"PLANNED", "IN_PROGRESS", "BLOCKED", "VERIFIED", "DEFERRED"}
PROOF_KINDS = {"AUDIT", "PR", "CI", "RUNTIME", "DEVICE", "MARKET", "RELEASE", "DECISION"}


def load():
    return json.loads(QUEUE.read_text(encoding="utf-8"))


def validate(program):
    """Structural gates. URL shape alone is NOT independent proof; PR review checks it."""
    if program.get("schema_version") != 1 or program.get("program_id") != "APP_FACTORY_10X_2026":
        raise ValueError("Unsupported roadmap schema")
    if not SHA.fullmatch(program.get("factory_baseline", "")):
        raise ValueError("Unpinned Factory baseline")
    phases = program.get("waves", [])
    if len(phases) < 6 or len({w["id"] for w in phases}) != len(phases):
        raise ValueError("Waves absent or duplicated")
    wave_order = {w["id"]: i for i, w in enumerate(phases)}
    streams = program.get("streams", {})
    tasks = program.get("tasks", [])
    if len(tasks) < 20:
        raise ValueError("Queue must include successors beyond five steps")
    ids = [t.get("id") for t in tasks]
    if len(set(ids)) != len(ids) or any(not isinstance(i, str) or not ID.fullmatch(i) for i in ids):
        raise ValueError("Task ID missing/duplicated")
    by_id = {t["id"]: t for t in tasks}
    for t in tasks:
        tid = t["id"]
        if t.get("wave") not in wave_order or t.get("stream") not in streams:
            raise ValueError("Unknown wave or stream: " + tid)
        if t.get("priority") not in PRIORITY or t.get("mode") not in MODES:
            raise ValueError("Unknown priority/mode: " + tid)
        if t.get("status") not in STATUSES:
            raise ValueError("Unknown status: " + tid)
        if not t.get("title") or not t.get("acceptance"):
            raise ValueError("Missing acceptance: " + tid)
        if not re.fullmatch(r"riccardopinato/[A-Za-z0-9_.-]+", t.get("owner_repo", "")):
            raise ValueError("Invalid owner repo: " + tid)
        if not isinstance(t.get("impact"), int) or not 1 <= t["impact"] <= 5:
            raise ValueError("Invalid impact: " + tid)
        if not isinstance(t.get("effort"), int) or not 1 <= t["effort"] <= 5:
            raise ValueError("Invalid effort: " + tid)
        deps = t.get("dependencies")
        if not isinstance(deps, list) or len(set(deps)) != len(deps) or tid in deps:
            raise ValueError("Bad dependency list: " + tid)
        for d in deps:
            if d not in by_id or wave_order[by_id[d]["wave"]] > wave_order[t["wave"]]:
                raise ValueError("Missing/future dependency: " + tid + " -> " + d)
        if t["status"] == "VERIFIED":
            evidence = t.get("evidence", [])
            if not evidence or not t.get("gate_reviewed", False):
                raise ValueError("VERIFIED requires reviewed evidence: " + tid)
            if any(not receipt_ok(r) for r in evidence):
                raise ValueError("Malformed evidence receipt: " + tid)
            if any(by_id[d]["status"] != "VERIFIED" for d in deps):
                raise ValueError("Dependency was not verified: " + tid)
        if t["status"] == "BLOCKED" and not t.get("blocker"):
            raise ValueError("BLOCKED must state reason: " + tid)
        if t["status"] == "IN_PROGRESS" and any(by_id[d]["status"] != "VERIFIED" for d in deps):
            raise ValueError("IN_PROGRESS before prerequisite: " + tid)
    visiting, visited = set(), set()
    def walk(tid):
        if tid in visiting:
            raise ValueError("Dependency cycle at " + tid)
        if tid in visited:
            return
        visiting.add(tid)
        for d in by_id[tid]["dependencies"]:
            walk(d)
        visiting.remove(tid)
        visited.add(tid)
    for tid in ids:
        walk(tid)
    policy = program.get("operating_rules", {})
    parallel = policy.get("parallelism", {})
    if (policy.get("auto_safe_mode") != "READ_ONLY"
            or parallel.get("strategy") != "ALL_READY_WITHOUT_FIXED_NUMERIC_CAP"
            or parallel.get("numeric_task_limit", "MISSING") is not None
            or parallel.get("read_only_same_repository_allowed") is not True
            or parallel.get("uncoordinated_writers_same_repository_forbidden") is not True
            or parallel.get("replace_blocked_tasks_immediately") is not True
            or parallel.get("replan_on_verified_or_blocked") is not True):
        raise ValueError("Dynamic parallelism safety policy invalid")
    if "max_parallel" in policy or policy.get("parallel_only_distinct_owner_repos") is True:
        raise ValueError("Legacy numeric cap detected")
    for task in tasks:
        if "write_paths" not in task and "scope_reviewed" not in task:
            continue
        if task["mode"] != "PR_GATED" or task.get("scope_reviewed") is not True:
            raise ValueError("Isolated scopes require PR_GATED review: " + task["id"])
        paths = task.get("write_paths")
        branch = task.get("write_branch")
        if (not isinstance(paths, list) or not paths or len(set(paths)) != len(paths)
                or any(not isinstance(path, str) or not path or path.startswith("/")
                       or ".." in path.split("/") or "*" in path for path in paths)
                or not isinstance(branch, str)
                or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_./-]*", branch)):
            raise ValueError("Unsafe or ambiguous write scope: " + task["id"])
    if policy.get("never_autoclose_from_scheduled_run") is not True:
        raise ValueError("Automatic task completion prohibited")
    return {"total": len(tasks), "waves": len(phases),
            "by_status": dict(Counter(t["status"] for t in tasks))}


def receipt_ok(receipt):
    if not isinstance(receipt, dict):
        return False
    if receipt.get("kind") not in PROOF_KINDS:
        return False
    url = receipt.get("url")
    if not isinstance(url, str) or not url.startswith("https://github.com/"):
        return False
    if not SHA.fullmatch(str(receipt.get("source_sha", ""))):
        return False
    return True


def next_tasks(program, limit=None):
    """Select only dependency-ready tasks; do not schedule two PRs on one repo."""
    validate(program)
    by_id = {t["id"]: t for t in program["tasks"]}
    wave_index = {w["id"]: i for i, w in enumerate(program["waves"])}
    ready = []
    waiting = []
    for t in program["tasks"]:
        if t["status"] not in ("PLANNED",):
            continue
        missing = [d for d in t["dependencies"] if by_id[d]["status"] != "VERIFIED"]
        if missing:
            waiting.append({"id": t["id"], "missing": missing})
        else:
            ready.append(t)
    ready.sort(key=lambda t: (PRIORITY[t["priority"]], wave_index[t["wave"]],
                              -(t["impact"] / t["effort"]), t["id"]))
    max_parallel = limit or program["operating_rules"]["max_parallel"]
    selected, approval, skipped, repos = [], [], [], set()
    for t in ready:
        if t["mode"] == "HUMAN_GATE":
            approval.append(t)
        elif len(selected) >= max_parallel or t["owner_repo"] in repos:
            skipped.append(t)
        else:
            selected.append(t)
            repos.add(t["owner_repo"])
    return {"selected": selected, "awaiting_human_gate": approval,
            "ready_not_selected": skipped, "awaiting_dependencies": waiting,
            "blocked": [t for t in program["tasks"] if t["status"] == "BLOCKED"],
            "verified": sum(t["status"] == "VERIFIED" for t in program["tasks"]),
            "total": len(program["tasks"])}


def summary_markdown(program, selection):
    def show(t):
        return f'- **{t["id"]}** [{t["priority"]}, {t["mode"]}, {t["stream"]}] {t["title"]} — {t["owner_repo"]}. Gate: {t["acceptance"]}.'
    lines = ["## App Factory 10x — prossima coda (non esecuzione)",
             f'Factory: {program["factory_baseline"]}; {selection["verified"]}/{selection["total"]} task con gate VERIFIED.',
             "", "### Prossimi task eseguibili — repository distinti"]
    lines += [show(t) for t in selection["selected"]] or ["- Nessun task eseguibile: controllare prerequisiti e gate."]
    lines += ["", "### Gate umani già pronti"]
    lines += [show(t) for t in selection["awaiting_human_gate"]] or ["- Nessun gate umano pronto."]
    lines += ["", f'In attesa di dipendenze: {len(selection["awaiting_dependencies"])}; '
              f'in coda dopo i limiti di parallelismo: {len(selection["ready_not_selected"])}; '
              f'bloccati: {len(selection["blocked"])}.', "",
              "**Attenzione:** la schedule verifica/ordina la coda ma NON modifica repository, "
              "non sviluppa codice, non auto-mergia PR, non marca VERIFIED e non riapre ChatGPT da sola."]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--next", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    doc = load()
    counts = validate(doc)
    if args.next:
        result = next_tasks(doc)
        if args.json:
            print(json.dumps({"selected": [t["id"] for t in result["selected"]],
                              "human_gate": [t["id"] for t in result["awaiting_human_gate"]],
                              "waiting": len(result["awaiting_dependencies"]),
                              "blocked": len(result["blocked"]),
                              "verified": result["verified"]}, indent=2))
        else:
            print(summary_markdown(doc, result))
    else:
        print("APP_FACTORY_10X_QUEUE_CHECK_PASS " + json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
