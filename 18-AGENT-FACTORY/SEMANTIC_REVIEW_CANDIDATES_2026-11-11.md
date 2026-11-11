# Proposte di revisione semantica — App Factory Context Sync

**Data:** 11 novembre 2026 · **Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`.
Stato: `SEMANTIC_REVIEW_PENDING`; nessuna nuova CAP, nessuna Product Bible aggiornata, nessuna promozione di donor/Golden.

## Metodo autorizzato
Un cambio SHA produce soltanto un **candidato da esaminare**. La proposta deve avere: commit esatto, file cambiati, CI run al PR head, consumer candidati e limiti. Un'app non adotta nulla senza Product Bible e roadmap; Store/Device rimangono separati.

### CXT-2026-001 — Guardrail operativi Agent Core
- Fonte: [App-Factory-Agent-Core PR #12](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/12), main `32d4d41a3774d465c28056de7dfb83469c631d06`.
- Diff: `scripts/context_reliability.py`, `tests/test_context_reliability.py`.
- Prova CI: [validate run 43058327470](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43058327470) al PR head; errori/timeout/retry e idempotency coperti da test *offline*.
- Interpretazione limitata: decision helper deterministico per l'orchestrazione metadata-only. Non viene importato oggi in nessun altro workflow; `REAL_RUNNER_INTEGRATION_NOT_VERIFIED`.
- Consumer candidati: Finance-Intelligence-Agent, Interactive-Scene-Core, AppLab e gli altri workflow della flotta. Nessuna installazione autorizzata o implicita.
- Decisione: `REVIEW_CANDIDATE`; richiedere benchmark, test nel consumer, source/versions e privacy prima di passare a Donor scoped.

### CXT-2026-002 — Registro 35-repo e vista Site
- Fonte: [Idee-app-Archivi-riferimenti PR #97](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/97), merge `15b7ab25464df9897bd5756fd2dbc0c40e092bd3`.
- File: `16-APP-FACTORY-SITE/data/context_fleet.json`, `src/index.html`, `scripts/context_fleet.py`, `tests/context_fleet_test.py`, CI workflow.
- Prova: [site validation run 43059674362](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/43059674362), test offline e source JS; stato Site **SOURCE_MERGED + CI_VERIFIED**, non deploy online.
- Interpretazione: monitor metadata con 32 repo pubblici e tre slot privati anonimi; snapshot temporale, NON backend live.
- Decisione: `REVIEW_CANDIDATE` per sistemi di observability e QA, **non** CAP d'app né Golden.

### CXT-2026-003 — E2E GitHub PR-only pattern
- Fonte: [btrader GitHub Actions run #43040885976](https://github.com/riccardopinato/btrader/actions/runs/43040885976) e [bot PR #5](https://github.com/riccardopinato/btrader/pull/5), creata dall'account `github-actions[bot]` con diff ristretto a due file docs.
- Prova: una PR aperta, rerun e successive riconciliazioni SHA senza creare duplicati. Testato su evento `push`, NON `schedule`.
- Decisione: `SCOPED_PATTERN_EVIDENCE`; non dimostra seconda installazione completa indipendente; non certifica processo/Golden.

## Barriere alla promozione
- Mancano **due consumer indipendenti** con run giornaliero/dispatch, PR bot, retry/recovery e audit ledger reali.
- `GITHUB_TOKEN` non può creare PR in quattro canary per configurazione repo-specifica; correzione amministrativa ancora necessaria.
- Source helper Agent non è un coding agent Windows e non dimostra QA fisica/prodotto.
- Nessun algoritmo semantico/LLM analizza automaticamente codice di prodotto: soltanto proposte deterministiche e revisione guidata.
- I file privati non vengono copiati nell'archivio pubblico.

## Stato delle decisioni
`PROPOSED` per tutti e tre; nessuna decisione `APPROVED_FOR_CONSUMER`, `VERIFIED_DONOR` o `CERTIFIED_GOLDEN`. L'owner dovrà indicare le destinazioni e approvare il test sotto i rispettivi gate.
