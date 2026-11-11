# App Factory 10x — roadmap continua approvata

**Approvazione strategica:** 12 novembre 2026 · **Baseline unica di questa sessione:** `riccardopinato/App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29.  
**Fonte della coda:** [PROGRAM_QUEUE.json](PROGRAM_QUEUE.json) · **Validazione/successori:** [script](../scripts/factory_10x_queue.py) · **Regole di continuità:** [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md).

## Missione, non solo cinque migliorie
L'obiettivo non è sviluppare indiscriminatamente più repository: è moltiplicare il numero di **funzionalità utili, verificate e distribuibili** per unità di tempo/costo, costruendo un sistema che seleziona, riusa, sviluppa, verifica, pubblica sotto gate e impara da risultati reali.

I cinque pilastri approvati restano:
1. **Agente AI operativo:** task → workspace isolato → test → PR con approvazione e recovery;
2. **Componenti riutilizzabili:** Flutter starter e Golden versionati, non semplici documenti;
3. **AppLab come QA/release factory:** CI, emulatori, visual QA, APK/AAB firmati e prove immutabili;
4. **Business misurabile:** scegliere 2–3 prodotti su domanda reale, misurare uso, retention, conversioni e ricavi;
5. **Intelligenza centrale:** differenze nel codice → ipotesi di riuso → review per-app con prove e licenza.

Il programma aggiunge una sesta corsia trasversale **governance/operatività continua**, necessaria per non perdere il lavoro dopo una singola chat.

## Stato iniziale verificato e confini
- **AppLab:** già presente il programma closed-loop v6 nel [ROADMAP.md](https://github.com/riccardopinato/AppLab/blob/main/ROADMAP.md). Prima integrare quanto già sviluppato; non duplicare un runner teorico.
- **App-Factory-Agent-Core:** repository e helper context-sync CI già presenti; il codice originale Windows v0.1–v0.4 **non è ancora acquisito nel repo** e il vero coding-agent resta non verificato. [Roadmap locale](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/ROADMAP.md).
- **Golden/Donor:** v29 definisce livelli di evidenza, non autorizza automaticamente a estrarre o importare codice in app terze.
- **Fleet GitHub 35/35:** workflow installati, ma solo btrader ha PR creata realmente dal bot provata; automazioni `schedule` e permessi dei quattro canary restano gate separati [roadmap infrastrutturale](../18-AGENT-FACTORY/ROADMAP_CONTEXT_AUTOMATION_35_REPOS_2026-11-11.md).
- **Monetizzazione/Play:** nessun dato utenti o ricavi inventato. Nuovo billing, analytics e pubblicazione Store restano soggetti ad approvazioni e obblighi provider.
- Il target **10x è un obiettivo**, non un miglioramento numerico già dimostrato. Il confronto sarà su metriche e coorti comparabili.

## Come procede senza fermarsi dopo cinque step
La coda contiene **57 task stabili, 8 ondate e sei lane**. Ogni task ha ID, dipendenze DAG, repo owner, modalità, descrizione del gate e stato; una volta `VERIFIED` tramite **PR documentata e prove con commit SHA**, i dipendenti diventano automaticamente eleggibili nella prossima selezione. I task già svolti non sono riscritti o eliminati.

- `python3 scripts/factory_10x_queue.py --check`: controlla DAG, sicurezza, fonti di prova e struttura.
- `python3 scripts/factory_10x_queue.py --next`: propone fino a **tre task indipendenti** con owner repository differenti; evidenzia gate umani, dipendenze e blocchi.
- [Workflow GitHub Actions](../.github/workflows/app-factory-10x-queue.yml): su PR/push, run manuale e cron quotidiano **06:23 UTC** verifica la coda e scrive il prossimo piano nel GitHub Job Summary, **senza usare token in scrittura, né fare commit/merge o eseguire sviluppo**.
- Il task ChatGPT già esistente `App Factory v27 — Tempo reale` può consumare la coda durante i suoi run programmati per tentare progressivamente **lavoro autorizzato in Chat** e registrare le prove. Non equivale a un ChatGPT sempre in esecuzione: tra i run non esiste lavoro di Chat asincrono. L'agente locale, quando davvero importato e collaudato, potrà eseguire i task compatibili in autonomia secondo contratti e permessi.
- Se la lane principale è bloccata si opera sulle altre lane pronte, non si inventa una chiusura `PASS`. Prima che W7 finisca, si aggiunge **W8+** per nuovi problemi/supporto, sempre con IDs nuovi e revisione.

**Autorizzazione di principio ≠ permesso illimitato:** `READ_ONLY` eseguibile dove esiste un runner; `PR_GATED` branch/CI exact-head/review/merge secondo governance; `HUMAN_GATE` richiede input specifico, connessione, dispositivo, budget o approvazione prodotto. Nessun auto-store, no API a pagamento, no bypass branch protection, no auto Golden promotion.

## Onrate per ondata — il lavoro resta sempre preparato
### W0 · Governance, selezione e misurazione
Stabilire baseline reale, portafoglio pilota, risorse e metriche prima di scalare.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-001` | Governance e continuità | Baseline multi-repo fonte verità e gap analysis | indipendente | `READ_ONLY` |
| `X10-002` | Prodotti, utenti e monetizzazione | Selezione shortlist 2–3 app commerciali | indipendente | `READ_ONLY` |
| `X10-003` | Kit Flutter e Golden | Inventario Golden/donor e consumatori | indipendente | `READ_ONLY` |
| `X10-004` | AppLab QA e release | Audit capability AppLab riusabili | indipendente | `READ_ONLY` |
| `X10-005` | Prodotti, utenti e monetizzazione | North Star KPI e ledger tempi/costi/ricavi | `X10-001` | `PR_GATED` |
| `X10-006` | Governance e continuità | Coda esecuzione con evidence gates | `X10-001` | `PR_GATED` |
| `X10-007` | Agente AI e integrazione AppLab | Inventario agente Windows locale richiesto | `X10-001` | `READ_ONLY` |


### W1 · Agente AI integrato e controllato
Integrare i moduli AppLab esistenti con l'agent locale, senza ricostruire ciò che esiste.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-008` | Agente AI e integrazione AppLab | Acquisizione codice Windows verificato | `X10-007` | `HUMAN_GATE` |
| `X10-009` | Agente AI e integrazione AppLab | Selezione adapter AppLab esistente | `X10-004` | `READ_ONLY` |
| `X10-010` | Agente AI e integrazione AppLab | Contract API job e permission gateway | `X10-009` | `PR_GATED` |
| `X10-011` | Agente AI e integrazione AppLab | Coda durevole / retry/idempotency | `X10-010` | `PR_GATED` |
| `X10-012` | Agente AI e integrazione AppLab | Workspace isolato con source SHA | `X10-010` | `PR_GATED` |
| `X10-013` | Agente AI e integrazione AppLab | Orchestrazione bounded con adapter | `X10-011`, `X10-012` | `PR_GATED` |
| `X10-014` | Agente AI e integrazione AppLab | PR agent con CI exact-head | `X10-013` | `PR_GATED` |
| `X10-015` | Agente AI e integrazione AppLab | Test end-to-end agente locale | `X10-008`, `X10-013` | `HUMAN_GATE` |
| `X10-016` | Agente AI e integrazione AppLab | Adapter agenti ricerca/QA | `X10-014` | `PR_GATED` |


### W2 · Componenti Flutter riutilizzabili
Estrarre componenti versionati con test di compatibilità e doppio consumer.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-017` | Kit Flutter e Golden | Contratto package Golden e versioning | `X10-003` | `PR_GATED` |
| `X10-018` | Kit Flutter e Golden | Harness compatibility per Golden | `X10-004`, `X10-017` | `PR_GATED` |
| `X10-019` | Kit Flutter e Golden | Flutter starter kit minimale | `X10-017` | `PR_GATED` |
| `X10-020` | Kit Flutter e Golden | Kit identity/login opt-in | `X10-019` | `PR_GATED` |
| `X10-021` | Kit Flutter e Golden | Kit profilo/impostazioni | `X10-019` | `PR_GATED` |
| `X10-022` | Kit Flutter e Golden | Kit backup/recovery | `X10-019` | `PR_GATED` |
| `X10-023` | Kit Flutter e Golden | Kit notifiche/health | `X10-019` | `PR_GATED` |
| `X10-024` | Kit Flutter e Golden | Kit monetizzazione modulare | `X10-019` | `HUMAN_GATE` |
| `X10-025` | Kit Flutter e Golden | Kit composizione e dependency chooser | `X10-020`, `X10-021`, `X10-022` | `PR_GATED` |
| `X10-026` | Kit Flutter e Golden | Due consumer Flutter certificati per kit | `X10-018`, `X10-025` | `PR_GATED` |


### W3 · Qualità, APK/AAB e release
Creare delivery verificabile, QA visivo e identità dei build artifact.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-027` | AppLab QA e release | Matrice QA esistente e gap release | `X10-004` | `READ_ONLY` |
| `X10-028` | AppLab QA e release | QA test router condiviso | `X10-027` | `PR_GATED` |
| `X10-029` | AppLab QA e release | Visual regression automation | `X10-028` | `PR_GATED` |
| `X10-030` | AppLab QA e release | Performance e accessibilità gate | `X10-028` | `PR_GATED` |
| `X10-031` | AppLab QA e release | Signed release provenance pipeline | `X10-028` | `PR_GATED` |
| `X10-032` | AppLab QA e release | Physical QA e Play internal testing | `X10-031` | `HUMAN_GATE` |
| `X10-033` | AppLab QA e release | Gate CI->QA->release decision | `X10-029`, `X10-030`, `X10-031` | `PR_GATED` |


### W4 · Portafoglio, utenti e monetizzazione
Validare pochi prodotti con dati di domanda e utilizzo reali.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-034` | Prodotti, utenti e monetizzazione | Validazione ricerca domanda/competitor | `X10-002` | `READ_ONLY` |
| `X10-035` | Prodotti, utenti e monetizzazione | Decisione 2–3 prodotti e budget | `X10-002`, `X10-034` | `HUMAN_GATE` |
| `X10-036` | Prodotti, utenti e monetizzazione | Sistema privacy-first product analytics | `X10-005`, `X10-035` | `PR_GATED` |
| `X10-037` | Prodotti, utenti e monetizzazione | Pricing e monetization experiment plan | `X10-035` | `HUMAN_GATE` |
| `X10-038` | Prodotti, utenti e monetizzazione | Pilot acquisition e release approval | `X10-036`, `X10-037` | `HUMAN_GATE` |
| `X10-039` | Prodotti, utenti e monetizzazione | Decisioni basate su coorti reali | `X10-038` | `READ_ONLY` |


### W5 · Intelligenza e riuso trans-app
Trasformare modifiche e problemi in proposte con provenance e approval.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-040` | Intelligenza centrale | Architettura knowledge/reuse centrale | `X10-003`, `X10-006` | `READ_ONLY` |
| `X10-041` | Intelligenza centrale | Diff-aware monitor repository | `X10-040` | `PR_GATED` |
| `X10-042` | Intelligenza centrale | Dedup capability/donor hypotheses | `X10-041` | `PR_GATED` |
| `X10-043` | Intelligenza centrale | Semantic review workflow supervisionato | `X10-042` | `PR_GATED` |
| `X10-044` | Intelligenza centrale | Riuso recommendation cockpit | `X10-043` | `PR_GATED` |
| `X10-045` | Intelligenza centrale | Feedback loop failure→donor | `X10-043`, `X10-028` | `PR_GATED` |


### W6 · Piloti e hardening
Provare la Factory su due prodotti diversi e recuperare failure reali.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-046` | Agente AI e integrazione AppLab | Pilota sviluppo feature A | `X10-014`, `X10-031` | `HUMAN_GATE` |
| `X10-047` | Agente AI e integrazione AppLab | Pilota feature B su repo diverso | `X10-046` | `HUMAN_GATE` |
| `X10-048` | Kit Flutter e Golden | Compatibilità kit nel secondo consumer | `X10-026`, `X10-047` | `HUMAN_GATE` |
| `X10-049` | AppLab QA e release | Campaign regressioni cross-app | `X10-033`, `X10-047` | `PR_GATED` |
| `X10-050` | Intelligenza centrale | Knowledge feedback su due consumer | `X10-044`, `X10-047` | `PR_GATED` |


### W7 · Scala e ottimizzazione continua
Gestione permanente, costi, rinnovi, batch successivi e manutenzione.

| ID | Lane | Task | Prerequisiti | Esecuzione |
|---|---|---|---|---|
| `X10-051` | Governance e continuità | Portfolio queue continua con recovery | `X10-006`, `X10-047` | `PR_GATED` |
| `X10-052` | Governance e continuità | Cost/performance benchmark rispetto al baseline | `X10-051` | `READ_ONLY` |
| `X10-053` | Kit Flutter e Golden | Scoped donor/process admission | `X10-048` | `HUMAN_GATE` |
| `X10-054` | AppLab QA e release | Release train per 2–3 app | `X10-049` | `PR_GATED` |
| `X10-055` | Prodotti, utenti e monetizzazione | Conferma scaling prodotti | `X10-039`, `X10-052` | `HUMAN_GATE` |
| `X10-056` | Intelligenza centrale | Reprioritizzazione cross-app basata su dati | `X10-050`, `X10-052` | `PR_GATED` |
| `X10-057` | Governance e continuità | Nuova ondata mantenendo storico | `X10-052`, `X10-056` | `PR_GATED` |


## Criteri oggettivi di svolta
La Factory deve dimostrare, attraverso [metriche nella coda](PROGRAM_QUEUE.json), non solo consegnare documentazione:
- **Agente:** due consumer diversi con PR approvate e testate, più recovery effettivo dopo fault;
- **Golden:** riduzione misurata di lavoro ripetuto e test donor + consumer su due app, senza regressioni;
- **AppLab:** pipeline reproducibile e artifact firmato con SHA/test; device e Store come gate separati;
- **Business:** 2–3 prodotti selezionati su dati, first release revisionata e retention/ricavi attribuibili;
- **Intelligenza:** due modifiche reali producono proposte reuse con source SHA, license/test, feedback su due consumer;
- **10x reale:** baseline misurata di tempo attivo e output verificato, confronto longitudinale senza confondere PR-open→merge con lavoro effettivo.

## Regole di priorità e parallelismo
- P0 e prerequisiti prima dei P1; a parità, ondata e rapporto impatto/sforzo. Non interrompere un lavoro in corso solo perché appare un nuovo task.
- Massimo **tre task simultanei**, su repository distinti, con scope indipendente. Un solo writer PR per repository alla volta; QA/ricerca READ_ONLY possono avanzare in parallelo.
- BLOCCHI P0 per privacy, permessi, dato non verificato o branch protection. Nessuna modifica al Master/Golden senza PR separata.
- Durata attesa è una stima di complessità (1–5), non un calendario promesso né ore di lavoro misurate.
- Salva ogni avanzamento nella coda e CHANGELOG con link a PR/evidenza; le differenze di prodotto richiedono aggiornamento dei documenti canonici della singola app, non semplici tick in questa tabella.

## Primi lavori eleggibili
Il resolver trova inizialmente `X10-001` (baseline/gap), `X10-002` (shortlist commerciale), `X10-003` (inventario Golden) e `X10-004` (audit AppLab). Poiché 001/002/003 condividono l'archivio, il selettore sceglie al massimo uno di questi come writer corrente insieme a X10-004, così nessuna PR concorrente può sovrascrivere lo stesso repo.

Le prossime dipendenze sono già codificate: quando 001 è effettivamente verificato si sbloccano 005/006/007; 004 sblocca 009/027; 003 sblocca 017/040; e così per tutte le 57 attività. Le approvazioni umane richieste sono isolate e non fermano le lane indipendenti.

## Riferimenti
- [Contratto di esecuzione e recovery](OPERATING_CONTRACT.md)
- [App Factory Agent Core](https://github.com/riccardopinato/App-Factory-Agent-Core)
- [AppLab](https://github.com/riccardopinato/AppLab)
- [Contesto infrastrutturale 35 repository](../18-AGENT-FACTORY/README.md)
- [Golden Index corrente pinned](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/golden/GOLDEN_INDEX_CURRENT.txt)
