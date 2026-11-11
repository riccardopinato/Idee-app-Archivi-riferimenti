# X10-004 — Mappa AppLab closed-loop esistente e gap Agent 10x

**Data:** 12/11/2026. **Fonte pinned:** [AppLab/main@2d57d9cea85ac03016b24e103046e47b6f02acb5](https://github.com/riccardopinato/AppLab/commit/2d57d9cea85ac03016b24e103046e47b6f02acb5) (commit nel link autorevole; abbreviazione interna di questa riga non è hash di prova).  
**Metodo:** audit statico di file e documentazione di contratto, non test runtime. L'AppLab v6.2 non è certificato oltre `SELF_CANARY`.

## Componenti esistenti da riusare (non reimplementare)

| Componente AppLab | File fonte nel commit osservato | Contratto osservato | Prossima integrazione |
|---|---|---|---|
| Durable per-repo queue | [durable_queue_v54e.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/durable_queue_v54e.py) | SQLite, queue states `QUEUED/DEFERRED/LEASED/DONE/BLOCKED/SUPERSEDED`, policy retry/protected classes | Adattare schema job Agent Core, non rifare database concorrente |
| Controlled event/delivery | [controlled_event_v54g.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/controlled_event_v54g.py) | Admission evento, idempotency e limiti per repo (max 2 ready global, 1 per repo) | Rispettare i limiti esistenti prima del parallelismo 10x |
| Causal investigation | [causal_repo_investigator_v60b.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/causal_repo_investigator_v60b.py) | Map path/diagnostics, restrizioni protected paths, evidenza source-linked | Adapter read-only e test negativo su path non autorizzati |
| Bounded patch worker | [bounded_fix_worker_v60c.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/bounded_fix_worker_v60c.py) | Diff/patch, workspace temporaneo, test weakening guard, restrictions | Riutilizzare in `X10-012`, non nuovo patch engine |
| Verify-repair loop | [v6 roadmap](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/integration/roadmap/APPLAB_V6_CLOSED_LOOP_AGENTIC_ENGINEERING.md) | `evidence → diagnosis → bounded correction → PR draft`; authority separata | Entry point operativo con evidence contract per Agent |
| Draft PR stewardship | [draft_pr_steward_v60e.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/draft_pr_steward_v60e.py) | Draft-only, SHA256 e work-item scope, `self_approval_performed=False` | Adapter PR con exact-head, review indipendente |
| v6.2 bounded self-canary | [autonomous_repair_v62a.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/autonomous_repair_v62a.py) | Proposal deterministica → `live_repair_attempt_v62a`; no pilot stage escalation | NON promuovere oltre SELF_CANARY senza campagna e prove reali |
| Reuse planning | [factory_reuse_planner_v57d.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/factory_reuse_planner_v57d.py) | Consuma Factory `CURRENT.yaml` e Registry; set di Golden Flutter/general predefiniti | `X10-003` inventario donor; candidate, non Golden automatico |
| Cross-app intelligence | [cross_app_intelligence.py](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/scripts/cross_app_intelligence.py) | Report analitici con provenance e senza alterare PASS/FAIL | `X10-040/042`: input knowledge, non secondo catalogo canonico |

## Evidenza e limiti
- Vengono **verificati la presenza e i contratti nel source**, non l'effettiva invocazione da Agent Core.
- [Operational proof v6.2](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/integration/roadmap/APPLAB_V62_OPERATIONAL_PROOF.md) segnala `NOT VERIFIED (0/3)` per la prova di repair longitudinali. La roadmap principale richiede `SELF_CANARY`, senza promo `PILOT_3` implicita.
- Il framework 10x propone max 3 task **di programma** in repo distinti, non sovrascrive il limite runtime AppLab di max 2 ready global / 1 active global del componente di evento.
- Nessuna importazione codice cross-repo fino a provenance, licenza e semantica degli adapter. Nessuna licenza dedotta da nome cartella.
- App Factory Agent Core main [@78dc19318b5905fd83b52b8840e082c5fec51b45](https://github.com/riccardopinato/App-Factory-Agent-Core/commit/78dc19318b5905fd83b52b8840e082c5fec51b45) è un repository distinto e non contiene il runner Windows originale in produzione; la semplice presenza di script `context_reliability.py` non è un agente di sviluppo.

## Proposta di adapter (NON ancora implementata)
```
10x task / GitHub event
  -> Agent Core authorization & JobContract (source SHA / scope / audit)
  -> AppLab durable queue (adapter, no duplicate scheduler)
  -> causal_repo_investigator_v60b
  -> bounded_fix_worker_v60c (isolated + negative tests)
  -> verify_repair_loop
  -> draft_pr_steward_v60e
  -> independent CI/review + approved merge
  -> evidence receipt -> program queue update
```

**Prossimi gate:** `X10-009` per contratti adapter esistenti; `X10-010` per permission gateway; `X10-012` per workspace e patch; `X10-046/047` per due consumer indipendenti. Prima di autorizzare l'esecuzione è obbligatorio rispettare Product Bible/branch rules di ogni consumer. Non avviare un secondo orchestrator parallelo a quello di AppLab.

Questo documento chiude un **audit statico** `X10-004`, non prova `QA_RUNTIME_PASS` o agent live.
