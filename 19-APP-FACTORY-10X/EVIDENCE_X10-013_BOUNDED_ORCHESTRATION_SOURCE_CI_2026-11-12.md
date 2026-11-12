# X10-013 — Orchestrazione bounded AppLab nell'Agent Core

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29.

## Evidenza controllata

- Repository owner: `riccardopinato/App-Factory-Agent-Core`.
- [PR #20](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/20) **MERGED** (squash commit `f0f8085cb2609a79cbdccee8de1223a97bf9ea09`).
- Exact PR head: `a8e000ad831d00a6bba566e2ba1f782cce9e01f8`.
- GitHub Actions: `Validate context contracts` **PASS** sullo stesso SHA.
- Review esterna: commento `chatgpt-codex-connector[bot]` con `codex-review-state:v1` — `code_review.status=completed`, `commit_sha=a8e000ad831d00a6bba566e2ba1f782cce9e01f8`, `has_any_findings=false`, `has_unresolved_findings=false`. I precedenti rilievi su autorizzazione WorkItem e leasing erano stati corretti e risolti.

## Codice e limiti

- `scripts/bounded_applab_orchestrator.py` delega le operazioni a code/worker AppLab già esistenti senza creare scheduler autonomi o autorizzare merge.
- Cattura l'identità originale della lease, rifiuta timestamp obsoleti, manomissione dell'authority envelope e worker reassignment durante il preflight; verifica i gate al callback boundary.
- `tests/test_bounded_applab_orchestrator.py` usa fixture sintetiche per permission/replay, lease scaduta, callback e mutazioni del chiamante.
- Documentazione locale: `docs/X10-013_BOUNDED_ORCHESTRATION.md`.

**Stato canonico: VERIFIED esclusivamente per SOURCE+PYTHON_CI.** Questo rispetta l'accettazione di X10-013 a livello di adapter + replay fixtures, non certifica funzionalità reale dell'agente Windows, recovery di processo interrotto o atomicità cross-process; il sorgente originale Windows v0.1–0.4 resta assente e X10-008 BLOCKED. Non vi sono prove di AppLab worker live, prova consumer, Play, APK o deployment.

Il successore X10-014 può essere sviluppato in PR isolata e con CI/review; non può eseguire merge automatici o release senza autorità esplicita. Per il test end-to-end reale dell'agente resta X10-015 (HUMAN_GATE, dipende X10-008).
