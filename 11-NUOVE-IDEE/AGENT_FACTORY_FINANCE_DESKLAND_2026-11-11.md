# Agent Factory, Finance Agent e riuso Deskland — dossier di prodotto
Data: 2026-11-11. Fonte: decisione esplicita utente in ChatGPT. Stato: IN_ROADMAP documentale, non implementazione certificata.
Baseline: App-Factory-Core@ee72dbb1b0de2cd71bc4aac42c350853c6915159; CURRENT Master 27, Golden Index 29.
Questa scheda registra una decisione di ARCHITETTURA/PORTFOLIO; non autorizza acquisti, trading live, integrazione di dati privati, pubblicazione, modifiche automatiche a repository altrui o promozione Golden.

## ID stabili
- AGF-2026-001 — Agent Factory Core: piattaforma per creare agenti specializzati e automatizzare in modo sorvegliato task di sviluppo, QA e ricerca.
- FIN-2026-001 — Finance Intelligence Agent: agente per azioni, ETF, portafoglio, mercati e rischio; read-only e paper trading prima di eventuali operazioni reali.
- INT-2026-001 — Interactive Scene Core: estrazione delle componenti grafiche Android/Flutter dal progetto Adaptive Landscape, solo dopo prove e isolamento delle dipendenze.
- DESK-EXISTING — Adaptive Landscape Android: prodotto già esistente, NON creare un secondo clone.

## Repository e provenienza verificata
- Prodotto Android già esistente: https://github.com/riccardopinato/Adaptive-Landscape-Android . La scheda esistente è ADAPTIVE_LANDSCAPE_ANDROID_2026-11-10.md. È il solo consumer Android di riferimento, da verificare all'HEAD esatto prima del riuso.
- Riferimento originale: https://github.com/BLEZZ0102/Deskland , GPL-3.0 al commit 9818b577402ff476e1b59da07970c56472713126, citato nell'archivio: reference prodotto/UX E1; codice e asset NON copiati nell'app proprietaria.
- Agente Windows in sperimentazione locale nella conversazione del 10/11/2026: il repository GitHub non è stato identificato e nessun codice dell'agente è stato importato qui. Non dichiarare "codice pronto" senza percorso, SHA, test e licenza.
- https://github.com/riccardopinato/btrader è un repository esistente che documenta arbitraggio crypto/Binance in Rust, NON il Finance Intelligence Agent per azioni: solo candidato da valutare come reference, nessun riuso assunto.
- Nuovi repository di destinazione PROPOSTI: riccardopinato/App-Factory-Agent-Core, riccardopinato/Finance-Intelligence-Agent, riccardopinato/Interactive-Scene-Core. Riservati come nomi, NON ESISTENZA CONFERMATA. Verificare disponibilità e crearli con permessi appropriati prima di scrivervi.

## Architettura: riuso e isolamento
App-Factory-Core (policy e Golden) -> Agent Factory Core (runner/tool gateway/job state) -> agenti Developer, QA, Research, Finance.
Interactive Scene Core (renderer, scene graph, gesture) -> Adaptive Landscape e futuri consumer grafici.
Finance Agent usa motore agentico ma ha namespace proprio, provider di market data separati, autorizzazioni minime, nessun accesso a GitHub secrets dell'App Factory e nessun permesso di operare su broker in MVP.

## Scope AGF-2026-001
- Job spec versionata, input schema validation, idempotency key, orchestrator, durable checkpoints, retry/backoff bounded, timeout, cancel, dead-letter, resumable result.
- Tool adapters a privilegi minimi (GitHub read/write distinto, process/build, QA); policy approval gate per PR/merge/deploy; audit log append-only; evidence receipts; task attribution.
- Scheduler/worker Windows/WSL separato dalla chat; non presumere che le chat proseguano autonomamente o si riaprano da sole.
- Secret storage non nel repo; no auto-escalation; no auto-modifica del Master/Golden; manual review per azioni finanziarie e release.
- Metriche: success rate, falsi positivi, job duration, retry, costi, regressioni, SHA di sorgente, CI status, physical QA.
- Destinazioni: App Factory developer agent; AppLab QA agent; donor/research agent; Finance come estensione separata.

## Scope FIN-2026-001
MVP 1 READ-ONLY: watchlist, prezzi con ritardo dichiarato, OHLCV e corporate actions con fonti/licenze, calendario earnings e news con timestamp/provenienza, posizioni inserite volontariamente, prezzo medio, valute e P&L. Nessuna credenziale broker richiesta.
MVP 2 ANALITICO: allocazione per titolo/settore/valuta, concentrazione, correlazioni su finestre dichiarate, volatilità, drawdown, stress scenario; benchmark, costi/tasse ipotetici chiaramente marcati.
MVP 3 REPORT & ALERT: threshold alert con debounce/quiet hours, digest, spiegazione trasparente, confidence, link fonte, log dei cambiamenti e segnali duplicati.
MVP 4 SIMULAZIONI: paper trading/backtest con survivorship/look-ahead bias, slippage, commissioni, FX, eventi societari, split/dividendi, out-of-sample; risultati non promettono performance.
FUORI SCOPE MVP: ordini reali, leva, gestione discrezionale, advice personalizzato a terzi, copy trading, accesso broker trading, broker credentials sul client, abbonamenti dati senza approvazione.
Provider: selezione dopo verifica di termini, rate limit, licenza commerciale e freschezza; non assumere dati real-time gratuiti. Verificare obblighi normativi per prodotti distribuiti (MiFID II/CONSOB, GDPR, market data agreements).

## Scope INT-2026-001
Identificare nel consumer attuale renderer scene, ciclo di vita WallpaperService, GPU shader, scene contract, preferenze, gestures/calibration, quality modes, throttling e release behavior.
Estrarre soltanto pezzi generici e compatibili, senza introdurre permessi sensibili o dipendenze Windows. Flutter widget/adapters separati da Kotlin Android. Valutare benchmarking FPS/CPU/RAM/batteria, diverse risoluzioni/refresh, device OEM e test reali. Lo shader acqua non deve essere dipendenza obbligatoria di Notes.
Consumer candidati: Adaptive Landscape, Notes Vision Board/canvas, launcher, giochi 2D, app educative. Ogni consumer richiede esplicita ammissione prodotto e test; non tutto il core è utile a tutti.

## Rischi prioritari
1. Confondere la GPL-3.0 di Deskland con codice libero da incorporare in un prodotto chiuso.
2. Confondere una preview Web o CI con accettazione visiva o test fisici Android.
3. Trattare un agente autonomo come capace di riprendere una chat senza runner persistente/scheduler.
4. Confondere tool accessibile e autorizzazione a modificare/mergiare/pubblicare.
5. Financial hallucination, dataset sporchi, date non allineate, licenze delle quotazioni, ordini non autorizzati.
6. Duplicare un repo Android o trasformare btrader crypto in un finance agent azionario senza nuova Product Bible.

## Cinque maxi-step approvati come piano (non come lavoro già eseguito)
S1 — Inventory e verità: commit esatti, codice realmente presente, licenze, mappa capability e test in Adaptive Landscape e nell'agente PC.
S2 — Contratti e confini: pacchetti agent-core, financial-domain e interactive-scene; AGENTS.md, Product Bible, threat model, versioned schemas.
S3 — Estrazione e test: agent-core indipendente e renderer core per primo consumer, fail-closed, CI e benchmarking; registrazione Donor solo con evidence.
S4 — Finance Intelligence MVP read-only: provider catalog, portfolio import sicuro, rischio, news/alert, storico e paper-only.
S5 — QA cross-consumer e aggiornamento incrementale: CI + evidenze runtime, Provenance/Reuse Ledger, eventuale proposta Golden e catalogo.
Per ogni passaggio: issue/PR, SOURCE SHA, owner, acceptance tests, rischio, costo di manutenzione, blocchi, follow-up.

## Regola di aggiornamento
- Il repo idee registra ID, decisioni, potenziale di riuso e link; ogni repo consumer possiede codice e stato reale.
- Ogni modifica significativa nei repo dedicati aggiorna README/ROADMAP/CHANGELOG/EVIDENCE con SHA/PR/test esatti e torna a linkare questo dossier.
- Non duplicare interi sorgenti tra repo; usare dipendenze versionate/pacchetti, contract tests, documentazione dell'API e compatibilità.
- Stato operativo iniziale delle tre iniziative: proposta strutturata. Nessun repo nuovo, implementazione, deploy o test dichiarato senza verifica separata.
