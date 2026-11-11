# M1 — prove reali dello snapshot GitHub Actions (11 novembre 2026)

**Ambito:** verifica E2E su cinque classi di repository dopo il rollout del workflow su 35/35 default branch.
**Factory pin di sessione:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29.
**Verdetto M1:** `PARTIAL_E2E_VERIFIED / BLOCKED_ADMIN_SETTING / SCHEDULE_NOT_VERIFIED`. NON dichiarare `ALL_35_VERIFIED`.

## Metodo: trigger reale, non simulazione
Il connettore GitHub collegato non espone l'azione REST `workflow_dispatch`, e nessun cron era ancora eseguito al preflight. È stato quindi applicato, mediante PR e gate normali, un trigger temporaneo `push` limitato ai cambiamenti del solo file workflow e del solo default branch. Le PR sono state unite a main/master, producendo **reali GitHub Actions runs con `event=push`**. Sono stati letti log e file generati sul branch bot. Dopo le prove, un'ulteriore PR per repository ha eliminato interamente il trigger temporaneo.

Un trigger `push` provato è evidenza del job e dei suoi permessi **per quell'evento**; non sostituisce la prova `schedule` / `workflow_dispatch`.

## Matrice d'evidenza E2E

| ID / tipo | Repository | Run reale / Evento | Esito verificato | Trigger QA + cleanup |
|---|---|---|---|---|
| PUB-MAIN-01 | [180FlipCharge](https://github.com/riccardopinato/180FlipCharge) | [run 43040857811](https://github.com/riccardopinato/180FlipCharge/actions/runs/43040857811), `push` | HTTP GitHub OK; file snapshot creati; branch `automation/app-factory-context` pubblicato; **FAIL** al `gh pr create`: Actions non autorizzato a creare PR | [QA #10](https://github.com/riccardopinato/180FlipCharge/pull/10), [cleanup #11](https://github.com/riccardopinato/180FlipCharge/pull/11) |
| PRIV-REDACTED-01 | Repository privato (nome e URL non pubblicati nel catalogo) | Run privato verificato, `push` | SHA snapshot pubblici corretti; branch bot creato; **FAIL** solo al `gh pr create`: medesimo blocco permessi; URL dei log consultabile direttamente nel repo privato | QA e cleanup **merged**, nomi PR riservati al repository privato |
| PUB-MASTER-01 | [btrader](https://github.com/riccardopinato/btrader), default `master` | [run 43040885976](https://github.com/riccardopinato/btrader/actions/runs/43040885976), `push`, prima esecuzione e retry `attempt=2` | **PASS E2E**: due docs snapshot; branch `automation/app-factory-context`; [PR #5](https://github.com/riccardopinato/btrader/pull/5) realmente **creata da `github-actions[bot]`**. Rerun PASS, solo una PR aperta, `SNAPSHOT_UNCHANGED` | [QA #4](https://github.com/riccardopinato/btrader/pull/4), [cleanup #6](https://github.com/riccardopinato/btrader/pull/6) |
| ORIGINAL-01 | [App-Factory-Agent-Core](https://github.com/riccardopinato/App-Factory-Agent-Core), workflow originale `context-snapshot.yml` | [run 43040897071](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43040897071), `push` | `CONTEXT_SNAPSHOT_WRITE_PASS`, `CONTEXT_SNAPSHOT_CHECK_PASS`, branch `automation/context-snapshot` pubblicato; **FAIL** al create PR per permessi | [QA #5](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/5), [cleanup #6](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/6) |
| PROTECTED-01 | [World-Days](https://github.com/riccardopinato/World-Days), regole main | [run 43041253853](https://github.com/riccardopinato/World-Days/actions/runs/43041253853), `push` | PR QA superata con check richiesti; snapshot e branch bot pubblicati; **FAIL** al create PR per permessi, senza bypass ruleset | [QA #91](https://github.com/riccardopinato/World-Days/pull/91), [cleanup #92](https://github.com/riccardopinato/World-Days/pull/92) |

**Risultato numerico:** 5/5 trigger reali eseguiti, 5/5 snapshot validi su branch bot, **1/5 PR create autonomamente con successo**; quattro create PR bloccate da opzione di repository. Tra i quattro: pubblico standard, privato, workflow originale e repo protetto.

## Verifica del dato osservato
- I quattro branch bot pubblicati nei test con blocco contengono le versioni allineate degli upstream: `App-Factory-Core/main@c5adc147046beb7024629466d10eeb799c3c2619` e `Idee-app-Archivi-riferimenti/main@c2a1aa39766828d60ec5994f489f268a4a9c8bf8` al momento dell'esecuzione.
- Il workflow Agent Core osserva anche `AppLab/main@2d57d9cea85ac03016b24e103046e47b6f02acb5`.
- La PR di btrader contiene **esclusivamente** `docs/APP_FACTORY_CONTEXT.json` e `docs/APP_FACTORY_CONTEXT.md`, con SHA upstream e date corrispondenti alla fonte GitHub. Nessun codice di trading è stato aggiornato dal workflow.
- Su btrader il secondo tentativo del run non ha creato una seconda PR: conteggio delle PR aperte sul branch bot = **1**. Dopo l'integrazione del rapporto M1, `Idee-app-Archivi-riferimenti/main` è avanzato a `9a32d3cf6ea960cbc6e5ff15da2df3b7f74a4e39`. Il **terzo tentativo effettivo** del medesimo [run 43040885976](https://github.com/riccardopinato/btrader/actions/runs/43040885976) ha aggiornato la **stessa** [PR #5](https://github.com/riccardopinato/btrader/pull/5), nuova HEAD `1bfb3d644a14908ad6d30ceaeb0f9b59e58af68c`, e i due file JSON/MD ora riportano tale SHA. Stato PASS `UPSTREAM_SHA_CHANGE / EXISTING_PR_RECONCILED / IDEMPOTENT`, con un'unica PR bot aperta.
- I cinque file workflow sui default branch sono stati ricontrollati dopo il cleanup: trigger temporaneo `push` **assente**, `schedule` e `workflow_dispatch` **presenti**; nessuna regola di branch protection è stata abbassata.

## Root cause verificata su quattro repository
GitHub Actions log: `pull request create failed: GraphQL: GitHub Actions is not permitted to create or approve pull requests (createPullRequest)`.

**Owner action richiesta:** in ciascun repository coinvolto: `Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests → Save`. Non occorre concedere al token tutti i permessi; lo scope nel job resta `contents: write` / `pull-requests: write` per il solo snapshot. Il connettore GitHub attuale non permette di modificare questa impostazione di amministrazione. **Non affermare che sia abilitata sugli altri 30 repository senza verifica.**

Dopo l'abilitazione, usare `rerun failed job` sulle esecuzioni esistenti o `workflow_dispatch` dal pannello GitHub, poi verificare PR davvero creata da `github-actions[bot]`, nessuna duplicazione e nessun bypass dei gate. Finché il permesso non è impostato, i cron possono continuare a fallire in fase di apertura PR; questo è un blocker operativo, non un bug di import dei dati.

## Gate M1 ancora aperti
- [x] Lanciare un job snapshot reale su pubblico, privato, `master`, originale e ruleset rigido tramite *push canary* delimitato.
- [x] Validare snapshot con source SHA e branch bot, comportamento fail-closed su permesso negato.
- [x] Confermare PR Actions realmente creata almeno su un consumer e retry senza duplicazione.
- [x] Cambiamento upstream vero e successiva riconciliazione automatica della PR bot #5 già aperta (`attempt=3` PASS), senza nuova PR.
- [x] Rimuovere trigger temporaneo attraverso CI e PR; confermare assenza di `on.push` in tutti e cinque.
- [ ] Abilitare opzione Actions create PR nei **quattro canary bloccati** e ripetere gli stessi job, senza confondere rerun con schedule.
- [ ] Eseguire e registrare `workflow_dispatch` effettivo su pubblico, privato e originale (tramite UI o tool con permessi).
- [ ] Eseguire e registrare almeno un evento effettivo `schedule` e la creazione/NO_OP della sua PR.
- [ ] Verificare eventuali restrizioni create PR e health sui **restanti 30 repo** (non dedurre il loro stato da questi cinque).
- [ ] Completare recovery su `branch push OK → PR create FAIL → permesso corretto → PR recuperata`, con URL della PR e audit idempotenza.

**Authority:** evidenza di infrastruttura GitHub Actions, non `CI_VERIFIED` di funzioni app, non `DEVICE_VERIFIED`, non Golden certificato, non import del runner Windows.
