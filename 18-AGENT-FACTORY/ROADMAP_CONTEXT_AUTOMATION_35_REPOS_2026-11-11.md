# Roadmap operativa — aggiornamento automatico del contesto App Factory (35 repo)
**Data stato:** 2026-11-11 · **Factory baseline:** `riccardopinato/App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29.

**Proprietà del documento:** questo hub traccia il rollout trasversale, non modifica `CURRENT.yaml`, AGENTS, Product Bible o roadmap delle singole app. Il workflow non esegue sviluppo autonomo né aggiorna semanticamente il codice.

## M0 — rollout tecnico completato (evidence)
- [x] Inventario **35/35** repository GitHub di proprietà dell'utente (32 pubblici, 3 privati) verificato al 2026-11-11.
- [x] Workflow su **default branch di 35/35 repo**: 32 repository aggiunti al rollout e 3 repository Agent/Finance/Scene già inizializzati e successivamente irrobustiti.
- [x] Per i 32: `.github/workflows/app-factory-context.yml` (v2), schedule quotidiana UTC distribuita, `workflow_dispatch`, controllo PR, checkout fissato all'SHA Golden `3d3c42e5aac5ba805825da76410c181273ba90b1`.
- [x] Nei tre originali: `.github/workflows/context-snapshot.yml`, script `scripts/sync_context.py`, repository configurati in `automation/SOURCES.json`; hardening della riconciliazione tramite PR #3.
- [x] PR effettuate mediante commit esatto + check CI, senza aggirare gate. Evidenze finali: [CamperBoss #32](https://github.com/riccardopinato/CamperBoss/pull/32) merge `fe3b10d435e120cc952a90cd6bc06c66b6b2521a`; [World-Days #88](https://github.com/riccardopinato/World-Days/pull/88) merge `d06cb1df4a4ae3f2dbb38ca69fdf445e7c3bd543`; [AppLab #215](https://github.com/riccardopinato/AppLab/pull/215) merge `2d57d9cea85ac03016b24e103046e47b6f02acb5`; [Notification-Control #37](https://github.com/riccardopinato/Notification-Control/pull/37) merge `3a38648f730fff591a85e48b5f4757073adc4663`.
- [x] Hardening successivo ai code review: avvio dal default branch, PR recovery se lo snapshot non cambia, push del branch aggiornato, job `validate-app-factory-context` non ambiguo, pin della Action coerente col Golden.
- [ ] **Esecuzione reale schedulata/dispatch e creazione PR automatica da cron:** NON_VERIFICATO. I check `pull_request` attestano esclusivamente il contratto CI, non l'esecuzione dello snapshot.
- [ ] **Aggiornamento semantico automatico di Product Bible/ROADMAP/GOLDEN/CAP o sorgenti:** NON IMPLEMENTATO e non autorizzato dal workflow metadata-only.
- [ ] **Codice agente Windows AppFactoryAgent v0.1–v0.4 nel repository:** NON IMPORTATO; non confondere con il rollout Actions.

**Stato M0:** `ROLLOUT_MERGED / CONTRACT_CI_VERIFIED`; **non** `SCHEDULE_VERIFIED`, `DEVICE_VERIFIED`, `AUTONOMOUS_AGENT_READY` o `CERTIFIED_GOLDEN`.

## Prossimi 5 maxi-step — ordine di esecuzione

### 1. Collaudo end-to-end dello scheduler e PR bot — P0 / PARTIALLY_VERIFIED + BLOCKED_ADMIN_SETTINGS
**Risultati live dell'11/11:** [Matrice di prove effettive E2E su cinque canary](EVIDENCE_M1_CONTEXT_SYNC_CANARY_2026-11-11.md).
- [x] Trigger reale `push` su 5/5 canary: pubblico standard, privato (nome non pubblicato qui), `master`, workflow originale e repo con regole rigide.
- [x] Eseguito il job reale e verificato lo snapshot GitHub upstream in 5/5 branch bot, non solo job CI di contratto.
- [x] PR **automaticamente creata da `github-actions[bot]`** su [btrader #5](https://github.com/riccardopinato/btrader/pull/5), default `master`, esclusivamente due file di metadata; [run E2E](https://github.com/riccardopinato/btrader/actions/runs/43040885976) PASS.
- [x] Rerun del job btrader `attempt=2`: PASS, `SNAPSHOT_UNCHANGED`, numero PR bot aperte sul branch = 1; nessuna PR duplicata.
- [x] Fail-closed effettivamente osservato su 4/5: branch e JSON/MD corretti ma `gh pr create` rifiutato da impostazione GitHub Actions. Log esempio [180FlipCharge](https://github.com/riccardopinato/180FlipCharge/actions/runs/43040857811) e [World-Days](https://github.com/riccardopinato/World-Days/actions/runs/43041253853).
- [x] Trigger QA temporanei **rimossi** da tutti e cinque i default branch tramite PR e CI; `schedule`/`workflow_dispatch` preservati.
- [ ] **Owner action P0:** abilitare GitHub Actions a creare PR nei 4 canary bloccati sotto `Settings → Actions → General → Workflow permissions`, senza estendere i permessi del token ad altri job; verificare la restrizione nei restanti 30.
- [ ] Rilanciare job falliti e registrare prova completa di recovery `branch pushed → PR denied → admin setting fixed → bot PR created`.
- [ ] Avviare almeno un vero `workflow_dispatch` per pubblico, privato, originale e ruleset (il connettore attuale non espone l'azione dispatch).
- [ ] Raccogliere almeno una prova reale `schedule` cron, con log e differenze/NO_OP. Nessun `push` canary equivale a schedulazione.
- [x] Verificato nuovo upstream SHA reale: dopo il merge di [Ideas PR #94](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/94), il rerun `attempt=3` del [workflow btrader](https://github.com/riccardopinato/btrader/actions/runs/43040885976) ha aggiornato i due file della **PR #5** esistente allo SHA Idee `9a32d3cf6ea960cbc6e5ff15da2df3b7f74a4e39`, conservando una sola PR bot.

**Gate M1:** `PARTIAL_E2E_VERIFIED`, non `SCHEDULE_VERIFIED`, non `ALL_35_PR_BOT_VERIFIED`. I test push provano funzionamento del worker e idempotenza su un repo; la configurazione amministrativa attuale impedisce un rollout end-to-end globale. La prima PR bot osservata non è stata auto-mergiata.

### 2. Resilienza, least privilege e manutenzione del template — P0 / FIX_CURRENT_STEP
- [ ] Testare fallimenti API/rate-limit, disattivazione Actions, token senza permesso PR, branch bot divergente e conflitti con `main`; fallire senza perdere snapshot precedente.
- [ ] Testare retry dopo «branch push riuscito ma PR create fallita», `workflow_dispatch` da feature branch, snapshot senza diff e branch principale avanzato.
- [ ] Verificare `permissions` minimi per job, Action SHA Golden, assenza di token custom, dati privati e segreti nei log.
- [ ] Distinguere un upstream `SOURCE_CHANGED` da una modifica `CI_VERIFIED`; validare policy di consumo/rate-limit per 35 repo.
**Gate:** test positivi e negativi, registri di recovery, test idempotenza, nessun bypass protezioni e nessuna auto-promozione Donor/Golden.

### 3. Registro centrale di stato e riconciliazione 35/35 — P1 / BACKGROUND_MAINTENANCE
- [ ] Consolidare inventario persistente `repo, visibility, default_branch, workflow_version, last_run, last_success, last_checked_SHA, open_snapshot_PR, error, blocked_reason` con provenance.
- [ ] Classificare `INSTALLED`, `CONTRACT_CI_VERIFIED`, `SCHEDULE_VERIFIED`, `PR_FLOW_VERIFIED`, `SEMANTIC_REVIEW_PENDING`, `BLOCKED`.
- [ ] Collegare al catalogo CAP e alla dashboard App Factory tramite **lettura dei dati**, non tramite riscrittura di stati applicativi.
- [ ] Analizzare nuovi repository GitHub, repository archiviati, cambio di visibilità e rename; preparare onboarding esplicito non distruttivo.
**Gate:** riconciliazione 35/35 replicabile, failure evidenziati e nessuna confusione tra test CI, device e release.

### 4. Aggiornamento semantico supervisionato, fonti e costo — P1 / FUTURE (richiede scope approvato)
- [ ] Definire diff semantici con source SHA e owner: cosa è cambiato, cosa richiede aggiornamento di roadmap/idea/CAP, quali test realmente dimostrano la funzione.
- [ ] Preparare PR di documentazione **solo dopo revisione esplicita delle evidenze**, non in base al solo incremento di SHA.
- [ ] Deduplicare notifiche, proteggere quote Actions, mantenere log minimizzati; nessuna API LLM a pagamento senza consenso.
- [ ] Valutare integrazione opzionale con App-Factory-Agent-Core **solo dopo import e test della sua sorgente locale**, separando orchestrazione persistente da chat.
**Gate:** nessun falso `IMPLEMENTED/PASS/CERTIFIED`, costi misurati, provenance e review obbligatoria.

### 5. Promozione a processo riutilizzabile e manutenzione stabile — P2 / FUTURE
- [ ] Raccogliere evidenze di due consumer indipendenti con cron + PR + recovery provati, non soltanto workflow CI verdi.
- [ ] Distinguere donor locale, candidato Golden e processo riutilizzabile; eventuale proposta al Core solo tramite admission gate e PR dedicata.
- [ ] Stabilire controlli periodici drift template/Golden, manutenzione Action SHA, branch orfani e prossima scadenza del runner.
- [ ] Documentare rollback per-repo, stop globale e supervisione senza forzare Work, APK o deploy.
**Gate:** evidence multi-repo, recovery rehearsal e decisione separata sulla certificazione.

## Dipendenze e priorità
`M0 [MERGED]` → `M1 [NEXT/P0]` → `M2 [P0]` → `M3 [P1]` → `M4 [P1, APPROVAL-REQUIRED]` → `M5 [P2]`.

La priorità è il collaudo operativo dell'Action e delle PR, **non** aggiungere altre automazioni prima di aver verificato le prime. I cinque maxi-step della [roadmap di prodotto Agent Core](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/ROADMAP.md) restano separati e aperti.

## Fonti e politica di aggiornamento
- `App-Factory-Core/CURRENT.yaml` e Golden pertinenti: processi e policy, non cron state.
- Codice workflow su default branch dei 35 repo e CI al PR head: prova di installazione/contratto.
- GitHub Actions `schedule` o `workflow_dispatch` e PR bot: **prova successiva da raccogliere**; test in PR non sostituisce trigger reale.
- Qualsiasi stato inferito o non osservato è `NOT_VERIFIED` fino al relativo run/commit/PR.
- Questo documento si aggiorna con branch → PR → check → merge; non viene riscritto da Actions.
