#!/usr/bin/env python3
"""Non-destructive, one-way mirror from the App Factory catalogue into GitHub Projects V2.

The canonical registry, per-app Markdown, CSV exports, product roadmaps and source
repositories are never modified. GitHub Project draft items are *derived views*.
No delete, archive, close, issue creation or visibility-change mutation exists here.

Modes:
  dry-run   Validate every app/CAP pair, print counts and sample without any API.
  pilot     Upsert 6 category-spanning records and read them back.
  bootstrap Pilot + verify, then upsert and verify ALL source records.
  full      Reconcile every source pair, without removing old project items.

Live use requires APP_FACTORY_PROJECT_TOKEN (classic PAT with 'project' scope,
or an appropriately privileged GitHub App installation token).
"""
import argparse
import csv
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
REGISTRY = BASE / "REGISTRO_CAPABILITY.json"
PROJECT_TITLE = "App Factory — Capability Dashboard"
OWNER = "riccardopinato"
TOKEN_ENV = "APP_FACTORY_PROJECT_TOKEN"
CATEGORIES = {
    "DA_VALUTARE": "Da valutare",
    "GIA_INTEGRATI": "Già integrati",
    "DA_VERIFICARE": "Da verificare",
}
MARKER_PREFIX = "<!-- APP_FACTORY_CAP_PAIR:"
MARKER_PATTERN = re.compile(
    r"^<!-- APP_FACTORY_CAP_PAIR:([^|\r\n]+)\|(CAP-\d{4}) -->", re.M
)
FIELD_SPECS = {"App": "TEXT", "Priorità": "NUMBER", "Facilità": "NUMBER",
               "Fase": "SINGLE_SELECT"}
VIEW_NAMES = {
    "Tutte le capability": "",
    "Da valutare": 'Fase:"Da valutare"',
    "Già integrati": 'Fase:"Già integrati"',
    "Da verificare": 'Fase:"Da verificare"',
}


def load_rows(root=ROOT):
    """Read generated source views; fail closed if any pair is missing or repeated."""
    base = root / "12-CAPABILITY-E-IMPLEMENTAZIONI"
    source = json.loads((base / "REGISTRO_CAPABILITY.json").read_text("utf-8"))
    canonical = {}
    for cap in source["records"]:
        for app in cap["app_states"]:
            key = (app, cap["id"])
            if key in canonical:
                raise ValueError("Duplicate canonical pair: " + repr(key))
            canonical[key] = (
                cap["score"], cap["integration_ease_percent"][app], cap["title"]
            )
    rows = {}
    for file in sorted((base / "PER_APP").glob("*/TABELLA.csv")):
        with file.open(encoding="utf-8-sig", newline="") as handle:
            for item in csv.DictReader(handle):
                key = (item["App"], item["CAP_ID"])
                if item["App"] != file.parent.name:
                    raise ValueError("CSV path/app mismatch: " + str(file))
                if key in rows:
                    raise ValueError("Duplicate CSV pair: " + repr(key))
                if item["Categoria"] not in CATEGORIES:
                    raise ValueError("Unknown category: " + repr(key))
                if key not in canonical:
                    raise ValueError("Unknown source pair: " + repr(key))
                score, ease, name = canonical[key]
                if (int(item["Priorita"]), int(item["Facilita_percento"]),
                        item["Capability"]) != (score, ease, name):
                    raise ValueError("CSV drift from JSON: " + repr(key))
                rows[key] = {
                    "app": key[0], "cap": key[1], "title": name,
                    "score": score, "ease": ease,
                    "category": item["Categoria"],
                    "reference": (
                        "https://github.com/riccardopinato/Idee-app-Archivi-riferimenti"
                        "/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/"
                        "REGISTRO_CAPABILITY/" + key[1] + ".md"
                    ),
                    "proof": item.get("Prova_codice_URL", ""),
                }
    if set(rows) != set(canonical):
        missing = sorted(set(canonical) - set(rows))
        extra = sorted(set(rows) - set(canonical))
        raise ValueError("Missing/extra project rows: " + str((missing[:10], extra[:10])))
    return sorted(
        rows.values(),
        key=lambda r: (-r["score"], -r["ease"], r["cap"], r["app"].casefold())
    )


def row_key(row):
    return (row["app"], row["cap"])


def marker(row):
    return MARKER_PREFIX + row["app"] + "|" + row["cap"] + " -->"


def draft_body(row):
    evidence = row["proof"] or "(non verificata: consultare scheda canonica)"
    return (
        marker(row) + "\n\n"
        "Scheda derivata **sola lettura** da App Factory. "
        "Il registro JSON e i repository delle app restano autoritativi.\n\n"
        "Fonte canonica: " + row["reference"] + "\n\n"
        "Prova codice (se disponibile): " + evidence + "\n\n"
        "Questo elemento non è un'approvazione di roadmap o una Issue del prodotto.\n"
    )


def pilot_rows(rows, size=6):
    """Guarantee all known classes are represented in the smoke test."""
    picked, seen = [], set()
    for category in CATEGORIES:
        for row in rows:
            key = row_key(row)
            if row["category"] == category and key not in seen:
                picked.append(row)
                seen.add(key)
                break
    for row in rows:
        if len(picked) >= size:
            break
        key = row_key(row)
        if key not in seen:
            picked.append(row)
            seen.add(key)
    return picked


def project_plan(rows, existing):
    """Pure idempotence plan. Existing project items NEVER get deleted."""
    adds, updates = [], []
    for row in rows:
        current = existing.get(row_key(row))
        if current is None:
            adds.append(row)
        else:
            updates.append((row, current))
    return adds, updates


class GitHubGraphQL:
    def __init__(self, token):
        if not token:
            raise ValueError("Missing " + TOKEN_ENV)
        self.token = token

    def call(self, query, variables=None):
        body = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
        req = Request(
            "https://api.github.com/graphql", data=body, method="POST",
            headers={"Authorization": "Bearer " + self.token,
                     "Accept": "application/vnd.github+json",
                     "Content-Type": "application/json",
                     "X-GitHub-Api-Version": "2022-11-28"},
        )
        # Retrying an unknown-result mutation can duplicate a newly-created item.
        # Only reads can be retried; on mutation failure the next run re-reads.
        is_mutation = query.lstrip().startswith("mutation")
        max_attempts = 1 if is_mutation else 3
        for attempt in range(max_attempts):
            try:
                with urlopen(req, timeout=35) as response:
                    result = json.loads(response.read().decode("utf-8"))
                if result.get("errors"):
                    # Never print credentials; fail on partial GraphQL writes.
                    raise RuntimeError("GitHub GraphQL error: " +
                                       str(result["errors"])[:950])
                return result["data"]
            except HTTPError as error:
                if error.code in (429, 502, 503, 504) and attempt < max_attempts - 1:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise RuntimeError("GitHub API HTTP " + str(error.code)) from None
            except URLError as error:
                if attempt < max_attempts - 1:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise RuntimeError("GitHub API connection unavailable") from None
        raise RuntimeError("GitHub API retries exhausted")


def get_or_create_project(api):
    query = """
    query($owner:String!, $after:String) {
      viewer { login }
      user(login:$owner) {
        id
        projectsV2(first:100, after:$after) {
          nodes { id number title url }
          pageInfo { hasNextPage endCursor }
        }
      }
    }"""
    cursor = None
    matches = []
    while True:
        data = api.call(query, {"owner": OWNER, "after": cursor})
        viewer = data["viewer"]["login"]
        if viewer.casefold() != OWNER.casefold():
            raise RuntimeError("Token owner " + viewer + " is not " + OWNER +
                               "; refusing creation in another account")
        owner = data["user"]
        if not owner:
            raise RuntimeError("Project owner not found")
        listing = owner["projectsV2"]
        matches.extend(p for p in listing["nodes"] if p["title"] == PROJECT_TITLE)
        if not listing["pageInfo"]["hasNextPage"]:
            break
        cursor = listing["pageInfo"]["endCursor"]
    if len(matches) > 1:
        raise RuntimeError("Multiple matching projects; refuse ambiguous writes")
    if matches:
        print("PROJECT_REUSED", matches[0]["url"])
        return matches[0]
    data = api.call("""
      mutation($owner:ID!, $title:String!) {
        createProjectV2(input:{ownerId:$owner, title:$title}) {
          projectV2 { id number title url }
        }
      }""", {"owner": owner["id"], "title": PROJECT_TITLE})
    result = data["createProjectV2"]["projectV2"]
    print("PROJECT_CREATED", result["url"])
    return result


def get_metadata(api, number):
    data = api.call("""
      query($owner:String!, $number:Int!) {
        user(login:$owner) { projectV2(number:$number) {
          id url
          fields(first:100) { nodes {
            __typename
            ... on ProjectV2Field { id name dataType }
            ... on ProjectV2SingleSelectField { id name options { id name } }
          }}
          views(first:100) { nodes { id name filter } }
        }}
      }""", {"owner": OWNER, "number": number})
    meta = data["user"]["projectV2"]
    if not meta:
        raise RuntimeError("Project read failed")
    return meta


def ensure_fields(api, project):
    meta = get_metadata(api, project["number"])
    fields = {f["name"]: f for f in meta["fields"]["nodes"] if f and f.get("name")}
    for name, dtype in FIELD_SPECS.items():
        if name in fields:
            field = fields[name]
            actual = ("SINGLE_SELECT" if field["__typename"] ==
                      "ProjectV2SingleSelectField" else field.get("dataType"))
            if actual != dtype:
                raise RuntimeError("Field type conflict: " + name)
        else:
            variables = {"project": project["id"], "name": name, "dtype": dtype}
            options = (
                [{"name": "Da valutare", "color": "GRAY",
                  "description": "Proposta non integrata"},
                 {"name": "Già integrati", "color": "GREEN",
                  "description": "Evidenza puntuale di implementazione"},
                 {"name": "Da verificare", "color": "YELLOW",
                  "description": "Fonte riportata o riuso parziale"}]
                if dtype == "SINGLE_SELECT" else None
            )
            data = api.call("""
              mutation($input:CreateProjectV2FieldInput!) {
                createProjectV2Field(input:$input) {
                  projectV2Field {
                    __typename
                    ... on ProjectV2Field { id name dataType }
                    ... on ProjectV2SingleSelectField {
                      id name options { id name }
                    }
                  }
                }
              }""", {"input": {
                "projectId": project["id"], "name": name, "dataType": dtype,
                **({"singleSelectOptions": options} if options else {})
            }})
            fields[name] = data["createProjectV2Field"]["projectV2Field"]
            print("FIELD_CREATED", name)
    option_names = {x["name"]: x["id"] for x in fields["Fase"]["options"]}
    if any(name not in option_names for name in CATEGORIES.values()):
        raise RuntimeError("Fase field missing one or more required options")
    return fields


def ensure_views(api, project):
    meta = get_metadata(api, project["number"])
    views = {v["name"]: v for v in meta["views"]["nodes"]}
    visible = [
        item["id"] for item in meta["fields"]["nodes"]
        if item and item.get("name") in ("Title", "App", "Priorità", "Facilità", "Fase")
    ]
    for name, filter_text in VIEW_NAMES.items():
        if name in views:
            current = views[name].get("filter") or ""
            if current == filter_text:
                continue
            if current:
                # Keep user-defined filters untouched. The script owns no
                # permission to replace manually customized views.
                print("VIEW_FILTER_UNCHANGED", name)
                continue
            if filter_text:
                # Recover a view created before an interrupted filter update.
                api.call("""
                  mutation($input:UpdateProjectV2ViewInput!) {
                    updateProjectV2View(input:$input) {
                      projectV2View { id filter }
                    }
                  }""", {"input": {"viewId": views[name]["id"],
                                   "filter": filter_text}})
                print("VIEW_FILTER_REPAIRED", name)
            continue
        result = api.call("""
          mutation($input:CreateProjectV2ViewInput!) {
            createProjectV2View(input:$input) {
              projectV2View { id name }
            }
          }""", {"input": {"projectId": project["id"],
                             "name": name, "layout": "TABLE_LAYOUT",
                             "configuration": {"visibleFieldIds": visible}}})
        view_id = result["createProjectV2View"]["projectV2View"]["id"]
        if filter_text:
            api.call("""
              mutation($input:UpdateProjectV2ViewInput!) {
                updateProjectV2View(input:$input) {
                  projectV2View { id filter }
                }
              }""", {"input": {"viewId": view_id, "filter": filter_text}})
        print("VIEW_CREATED", name)


def read_project_items(api, number):
    query = """
    query($owner:String!, $number:Int!, $after:String) {
      user(login:$owner) { projectV2(number:$number) {
        items(first:100, after:$after) {
          nodes {
            id
            content {
              __typename
              ... on DraftIssue { id title body }
            }
            fieldValues(first:40) { nodes {
              __typename
              ... on ProjectV2ItemFieldTextValue {
                text field { ... on ProjectV2Field { name } }
              }
              ... on ProjectV2ItemFieldNumberValue {
                number field { ... on ProjectV2Field { name } }
              }
              ... on ProjectV2ItemFieldSingleSelectValue {
                optionId field { ... on ProjectV2SingleSelectField { name } }
              }
            }}
          }
          pageInfo { hasNextPage endCursor }
        }
      }}
    }"""
    found = {}
    cursor = None
    while True:
        data = api.call(query, {"owner": OWNER, "number": number, "after": cursor})
        page = data["user"]["projectV2"]["items"]
        for item in page["nodes"]:
            content = item.get("content") or {}
            if content.get("__typename") != "DraftIssue":
                continue
            match = MARKER_PATTERN.search(content.get("body") or "")
            if not match:
                continue  # unrelated items are NEVER modified
            key = (match.group(1), match.group(2))
            if key in found:
                raise RuntimeError("Duplicate Project key: " + repr(key))
            values = {}
            for v in item["fieldValues"]["nodes"]:
                field = (v or {}).get("field") or {}
                name = field.get("name")
                if not name:
                    continue
                if v["__typename"] == "ProjectV2ItemFieldNumberValue":
                    values[name] = v["number"]
                elif v["__typename"] == "ProjectV2ItemFieldTextValue":
                    values[name] = v["text"]
                elif v["__typename"] == "ProjectV2ItemFieldSingleSelectValue":
                    values[name] = v["optionId"]
            found[key] = {"item_id": item["id"], "content_id": content["id"],
                          "values": values}
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return found


def desired_fields(row, fields):
    option_ids = {o["name"]: o["id"] for o in fields["Fase"]["options"]}
    return {
        "App": {"text": row["app"]},
        "Priorità": {"number": float(row["score"])},
        "Facilità": {"number": float(row["ease"])},
        "Fase": {"singleSelectOptionId": option_ids[CATEGORIES[row["category"]]]},
    }


def changed_inputs(row, item, fields, project_id):
    desired = desired_fields(row, fields)
    changes = []
    values = item.get("values", {})
    for name, value in desired.items():
        current = values.get(name)
        wanted = next(iter(value.values()))
        if current == wanted:
            continue
        changes.append({"projectId": project_id, "itemId": item["item_id"],
                        "fieldId": fields[name]["id"], "value": value})
    return changes


def set_fields(api, inputs):
    if not inputs:
        return
    # All four field changes in ONE GraphQL call, avoiding 4x API traffic.
    names = [f"v{i}" for i in range(len(inputs))]
    query = (
        "mutation(" + ", ".join("$" + x +
        ":UpdateProjectV2ItemFieldValueInput!" for x in names) + ") { " +
        " ".join(f"f{i}:updateProjectV2ItemFieldValue(input:$v{i})"
                 "{ projectV2Item { id } }" for i in range(len(inputs))) + " }"
    )
    api.call(query, dict(zip(names, inputs)))


def upsert(api, project, fields, rows, existing):
    adds, others = project_plan(rows, existing)
    adding = {row_key(row) for row in adds}
    created = updated = unchanged = 0
    for row in rows:
        key = row_key(row)
        item = existing.get(key)
        if item is None:
            data = api.call("""
              mutation($input:AddProjectV2DraftIssueInput!) {
                addProjectV2DraftIssue(input:$input) {
                  projectItem { id content { ... on DraftIssue { id } } }
                }
              }""", {"input": {
                "projectId": project["id"],
                "title": row["cap"] + " · " + row["app"] + " — " + row["title"],
                "body": draft_body(row)
            }})
            node = data["addProjectV2DraftIssue"]["projectItem"]
            item = {"item_id": node["id"], "content_id": node["content"]["id"],
                    "values": {}}
            existing[key] = item  # Avoid duplicates after a partial run.
            created += 1
        changes = changed_inputs(row, item, fields, project["id"])
        if changes:
            set_fields(api, changes)
            for name, value in desired_fields(row, fields).items():
                item["values"][name] = next(iter(value.values()))
            if key not in adding:
                updated += 1
        elif key not in adding:
            unchanged += 1
    print("SYNC_SUMMARY", json.dumps(
        {"requested": len(rows), "created": created, "updated": updated,
         "unchanged": unchanged, "deleted": 0}, ensure_ascii=False))


def assert_remote(api, number, rows, fields):
    existing = read_project_items(api, number)
    for row in rows:
        item = existing.get(row_key(row))
        if not item:
            raise RuntimeError("Pilot/full verification missing pair " + repr(row_key(row)))
        changes = changed_inputs(row, item, fields, "verify")
        if changes:
            raise RuntimeError("Pilot/full verification field mismatch " +
                               repr(row_key(row)))
    print("REMOTE_VERIFIED", len(rows))
    return existing


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dry-run", "pilot", "bootstrap", "full"),
                        default="dry-run")
    args = parser.parse_args(argv)
    rows = load_rows()
    counts = dict(Counter(row["category"] for row in rows))
    print("SOURCE_VALID", json.dumps(
        {"apps": len({r["app"] for r in rows}), "pairs": len(rows),
         "categories": counts}, ensure_ascii=False, sort_keys=True))
    sample = pilot_rows(rows)
    print("PILOT_SELECTED", json.dumps(
        [{"app": r["app"], "cap": r["cap"],
          "score": r["score"], "ease": r["ease"],
          "category": r["category"]} for r in sample], ensure_ascii=False))
    if args.mode == "dry-run":
        print("DRY_RUN_ONLY: no GitHub Project created or changed")
        return
    api = GitHubGraphQL(os.environ.get(TOKEN_ENV, ""))
    project = get_or_create_project(api)
    fields = ensure_fields(api, project)
    ensure_views(api, project)
    existing = read_project_items(api, project["number"])
    if args.mode in ("pilot", "bootstrap"):
        upsert(api, project, fields, sample, existing)
        existing = assert_remote(api, project["number"], sample, fields)
        print("PILOT_PASS")
        if args.mode == "pilot":
            return
    if args.mode in ("bootstrap", "full"):
        upsert(api, project, fields, rows, existing)
        assert_remote(api, project["number"], rows, fields)
        print("FULL_SYNC_PASS", len(rows), project["url"])


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError, TypeError, OSError) as error:
        print("PROJECT_SYNC_BLOCKED:", str(error), file=sys.stderr)
        sys.exit(1)
