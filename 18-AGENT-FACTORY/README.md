# Agent Factory — hub di riuso e repository
Data 2026-11-11. Baseline Core ee72dbb1b0de2cd71bc4aac42c350853c6915159.
Questa cartella è un hub di registrazione e scaffold DOCUMENTALE, non un repository eseguibile.
Dossier: [Agent Factory / Finance / Deskland](../11-NUOVE-IDEE/AGENT_FACTORY_FINANCE_DESKLAND_2026-11-11.md).

## Destinazioni e stato attuale
| ID | Repo destinazione proposto | Stato |
|---|---|---|
| AGF-2026-001 | [App-Factory-Agent-Core](https://github.com/riccardopinato/App-Factory-Agent-Core) | BOOTSTRAP MERGED + CI PASS; sorgenti Windows non importate |
| FIN-2026-001 | [Finance-Intelligence-Agent](https://github.com/riccardopinato/Finance-Intelligence-Agent) | BOOTSTRAP MERGED + CI PASS; motore finanziario non implementato |
| INT-2026-001 | [Interactive-Scene-Core](https://github.com/riccardopinato/Interactive-Scene-Core) | BOOTSTRAP MERGED + CI PASS; estrazione renderer non avviata |
| DESK-EXISTING | riccardopinato/Adaptive-Landscape-Android | ESISTE; code owner del prodotto Android |
| REF-CRYPTO | riccardopinato/btrader | ESISTE; arbitraggio crypto, diverso prodotto |

## Source of truth
- Policies: riccardopinato/App-Factory-Core/CURRENT.yaml (Master 27, Golden Index 29 al 11/11).
- AGENTS.md locale per ciascun nuovo repo; Product Bible per ciascun prodotto; ROADMAP e IMPLEMENTATION_LOG; CODE_PROVENANCE con SHA/licenze; TEST_EVIDENCE con tool/date/result; CHANGELOG; decision records.
- Mai creare una copia del Master o dei Golden in questi repo; solo link/pin commit.
- Originale Deskland BLEZZ0102/Deskland GPL-3.0: prodotto/UX reference; non importare code/assets direttamente in Adaptive Landscape commerciale.

## Convezioni di stato per aggiornamenti
IDEA -> IN_ROADMAP -> IN_CODICE -> CI_VERIFIED -> DEVICE_VERIFIED -> RELEASE; status e freshness distinti.
AGF: schemi job, adapter strumenti e gating indipendenti.
FIN: dati/licenze, timestamp, paper-only e divieto trading reale come default.
INT: interoperabilità Flutter/Kotlin, permessi Android, FPS/batteria e doppio consumer prima di Golden.
Ogni modifica: task/issue -> branch -> commit -> PR -> exact-head tests -> merge condizionale -> changelog e aggiornamento link qui. Nessuna esecuzione in background implicita.

## Bootstrap minimo per nuovi repo
1. Crea repository separato con visibilità valutata (per Agent e Finance preferibilmente privato).
2. Introduci README.md, AGENTS.md, PRODUCT_BIBLE.md, ROADMAP.md, CHANGELOG.md, docs/ARCHITECTURE.md, docs/SECURITY.md, docs/PROVENANCE.md, evidence/README.md.
3. Per AGF migra il codice esistente solo dal path locale verificato, con commit e licenza; nessun codice fittizio.
4. Per FIN importa solo modelli dati anonimi/sintetici, nessuna chiave né posizioni personali.
5. Per INT estrai dal repo Adaptive Landscape soltanto dopo benchmark, review licenze e test di consumer.
6. Collegamento reciproco con il presente hub e con il dossier principale. Non sovrascrivere repository preesistenti.

## Context control — M2/M3/M4/M5 (11/11/2026)
- [**Registro tecnico 35/35**](../16-APP-FACTORY-SITE/data/context_fleet.json) con tre repo privati anonimi, verificato da CI e mostrato nella sezione Repository del [sorgente Site](../16-APP-FACTORY-SITE/src/index.html); nessun deploy online attestato.
- [**Review semantiche candidate**](SEMANTIC_REVIEW_CANDIDATES_2026-11-11.md): proposte con diff/source/test, nessuna capability o Golden auto-promossa.
- [**Ammissione Donor/Golden**](CONTEXT_SYNC_REUSE_ADMISSION_2026-11-11.md): stato PROCESS_CANDIDATE, secondo consumer indipendente e cron reali ancora mancanti.
- [**Recovery playbook**](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/docs/CONTEXT_SYNC_RECOVERY_PLAYBOOK.md) e [**guardrail offline**](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/scripts/context_reliability.py), PR #12 merged con CI.

## Automatic maintenance — rollout 35/35 (11/11/2026)
**Roadmap operativa aggiornata:** [Automazione contesto su tutti i 35 repo — 5 maxi-step](ROADMAP_CONTEXT_AUTOMATION_35_REPOS_2026-11-11.md).

**Ultimo audit M1 35/35:** [prova live, retry reali, difetto Git corretto e permessi amministrativi ancora bloccanti](EVIDENCE_M1_35_REPO_SWEEP_AND_RETRY_2026-11-11.md). I trigger cron/dispatch sono installati ma **non ancora eseguiti**; nessuna nuova attività pianificata è stata creata (limite 5 attive).

- **Installazione MERGED:** 35/35 repository (`main` oppure `master`); 32 workflow di rollout `app-factory-context.yml` e 3 workflow originali `context-snapshot.yml` con hardening.
- **CI di contratto:** validazioni delle PR effettuate, con pin Action SHA Golden e aggiornamento dei branch senza bypass. Esempi conclusivi: [CamperBoss PR #32](https://github.com/riccardopinato/CamperBoss/pull/32), [World Days PR #88](https://github.com/riccardopinato/World-Days/pull/88).
- **Prova E2E parziale osservata:** 5 trigger reali `push` canary, snapshot e branch bot verificati; su [btrader PR #5](https://github.com/riccardopinato/btrader/pull/5) creata davvero da `github-actions[bot]`, con rerun idempotente. **Quattro** altri canary bloccati da permesso GitHub Actions di creare PR. [Evidence completa](EVIDENCE_M1_CONTEXT_SYNC_CANARY_2026-11-11.md).
- **NON VERIFICATI:** gli eventi `schedule` e `workflow_dispatch`, il recupero delle quattro PR dopo configurazione admin e la capacità di creare PR dei restanti 30 repository.
- **Non implementato:** aggiornamento semantico automatico di codice, Product Bible, roadmap, CAP e Golden; il cron osserva commit SHA/data pubblici e propone **solo** snapshot documentali tramite PR.
- **Factory CURRENT:** Master v27 / Golden Index v29, baseline del successivo audit `c5adc147046beb7024629466d10eeb799c3c2619`; il precedente `ee72dbb...` nell'intestazione documenta il bootstrap originale.
- La sincronizzazione semantica ChatGPT dedicata resta distinta da questo workflow; nessuna nuova attività ChatGPT è stata creata.
