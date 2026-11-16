#!/usr/bin/env python3
"""Fail-closed audit integrity check: scores, source grades, app coverage and CAP refs."""
from collections import Counter
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'12-CAPABILITY-E-IMPLEMENTAZIONI'
AUDIT=BASE/'STARS_750_AUDIT_APP_2026-11-16'
data=json.loads((AUDIT/'data/APP_BY_APP_STARS_AUDIT_2026-11-16.json').read_text(encoding='utf-8'))
caps=json.loads((BASE/'REGISTRO_CAPABILITY.json').read_text(encoding='utf-8'))
cap_ids={item['id'] for item in caps['records']}
rows=data['records']
assert len(rows)==197, f'Expected 197 interventions, found {len(rows)}'
assert len({r['id'] for r in rows})==197
assert len({(r['project'],r['intervention']) for r in rows})==197
assert data['scope']=={'github_repositories':35,'github_product_repos':26,'github_factory_repos':9,'cap_only_projects':24,'projects':59,'interventions':197}
assert len({r['project'] for r in rows})==59
assert sum(r['source_kind']=='REPO_HEAD' for r in rows)==141
assert sum(r['source_kind']=='CAP_ONLY' for r in rows)==56
assert len({r['project'] for r in rows if r['source_kind']=='REPO_HEAD'})==35
assert len({r['project'] for r in rows if r['source_kind']=='CAP_ONLY'})==24
assert len({r['repository'] for r in rows if r['repository']})==35
assert all(r['priority'] in range(101) and r['feasibility'] in range(101) for r in rows)
assert all(r['type'] in {'GATE','MIGLIORIA','RIUSO','NUOVA','RICERCA'} for r in rows)
assert all(r['implementation_status'] in {'NOT_ASSERTED_IMPLEMENTED','CAP_ONLY_NOT_CODE_VERIFIED'} for r in rows)
for r in rows:
    if r['source_kind']=='REPO_HEAD':
        assert r['repository'] and re.fullmatch('[a-f0-9]{40}',r['head_sha'])
        assert r['evidence_path']
        assert r['implementation_status']=='NOT_ASSERTED_IMPLEMENTED'
    else:
        assert r['repository'] is None and r['head_sha'] is None
        assert r['implementation_status']=='CAP_ONLY_NOT_CODE_VERIFIED'
    for cap_id in re.findall(r'CAP-\d{4}',r['cap_refs']):
        assert cap_id in cap_ids,(r['project'],cap_id)
    assert r['source_document'] in {'01_APP_A_M.md','02_APP_N_Z.md','03_INFRA_AGENTI.md','04_CAP_ONLY_NO_REPO.md'}
    assert r['intervention'] and r['rationale']

index=(AUDIT/'00-INDEX.md').read_text(encoding='utf-8')
for name in ['01_APP_A_M.md','02_APP_N_Z.md','03_INFRA_AGENTI.md','04_CAP_ONLY_NO_REPO.md']:
    assert (AUDIT/name).exists(),name
    assert name in index,name
for project in set(r['project'] for r in rows):
    assert project in index,project
counts=Counter(r['type'] for r in rows)
print('APP_BY_APP_AUDIT_PASS',len(rows),'interventions, 59 projects, 35 GitHub, 24 CAP-only; types',dict(counts))
