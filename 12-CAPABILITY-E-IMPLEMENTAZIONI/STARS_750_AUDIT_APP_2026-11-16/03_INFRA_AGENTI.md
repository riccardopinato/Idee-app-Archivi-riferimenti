# Audit specifico — infrastrutture, agenti, cataloghi e donor, 16 novembre 2026

Perimetro: 9 repository non classificabili tutti come app consumer. Inclusi per coprire **ogni repository effettivamente visibile** nell’account (35 totali) e distinguere automazione, tool QA, nuove idee e fonti.

Score **P** (priorità) e **F** (fattibilità tecnica) sono valutazioni comparative 0–100 non probabilità, licenze/Store/device/consenso sono gate non cancellati da un buon punteggio. Stati accertati da README/roadmap/HEAD; non è stata eseguita una test suite per ogni repo in questa passata.

## 1000 AI Collection Tools — archivio esterno
Source: [1000-AI-collection-tools@e78e1dce82f2d5b9e3a9c692942900684be94666](https://github.com/riccardopinato/1000-AI-collection-tools/tree/e78e1dce82f2d5b9e3a9c692942900684be94666) · [README.md](https://github.com/riccardopinato/1000-AI-collection-tools/blob/e78e1dce82f2d5b9e3a9c692942900684be94666/README.md).
**Stato documentale:** Raccolta README di tool AI esterni; non un'app o donor eseguibile certificato.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Verificare link, sopravvivenza progetti, termini e provider prima di usare catalogo come fonte | **88** | **83** | — | Liste aggregate possono contenere prodotti non più disponibili |
| MIGLIORIA | Taggare tool per Notes/FrameLab/WorldDays/Agent con API, costi e privacy verificabili | **74** | **87** | — | Rinvii al catalogo centrale, niente fork del suo archivio |
| RICERCA | Non trattare la presenza di un nome in lista come licenza o codice da integrare | **90** | **95** | — | Governance e provenance |

## AppLab
Source: [AppLab@0b45e4a474fe958a141430a6447c50ccf6d114b2](https://github.com/riccardopinato/AppLab/tree/0b45e4a474fe958a141430a6447c50ccf6d114b2) · [ROADMAP.md](https://github.com/riccardopinato/AppLab/blob/0b45e4a474fe958a141430a6447c50ccf6d114b2/ROADMAP.md).
**Stato documentale:** Harness QA, app runtime e remediation self-canary: percorsi fonte, artifacts e closed-loop previsti; alcune prove di repair end-to-end ancora non certificate.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Concludere self-canary repair con 3 riparazioni indipendenti a SHA verificato prima di dichiarare autonomia | **99** | **65** | CAP-0068 | README segna 0/3 verified in un precedente milestone; evidenze correnti da consolidare |
| RIUSO | Introdurre Trivy per SBOM/CVE/secrets in modalità read-only, report-only prima di blocking | **97** | **85** | CAP-0068 | Apache-2.0; tool CI esterno, niente bundling negli APK |
| RIUSO | Introdurre Semgrep/CodeQL con regole Flutter/Kotlin + triage falsi positivi su PR | **96** | **81** | CAP-0068 | Verificare supporto linguaggi e licenza distribuzione |
| RIUSO | MobSF per APK/AAB statico e, su runner isolato, device dinamico autorizzato | **93** | **68** | CAP-0068 | GPL come strumento separato, accesso a binary e network controllato |
| GATE | Matrice Android reale di upgrade/firma/storage/FGS e screenshot flow, preservando evidence ladder | **96** | **73** | CAP-0068 | Niente certificati E4 inventati dalla CI |

## App Factory Agent Core
Source: [App-Factory-Agent-Core@f2b4c28cc3a9afa4ef39c6d32fe0a8ef14dac512](https://github.com/riccardopinato/App-Factory-Agent-Core/tree/f2b4c28cc3a9afa4ef39c6d32fe0a8ef14dac512) · [ROADMAP.md](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/f2b4c28cc3a9afa4ef39c6d32fe0a8ef14dac512/ROADMAP.md).
**Stato documentale:** Contratti job e adapter source parzialmente implementati; agent Windows locale e trusted live execution non ancora integrati/certificati.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Collegare worker Windows/WSL reale a JobGraph con lease, retry, idempotenza, credenziali e approve-boundaries | **99** | **54** | — | La sola PR di orchestrazione non è un agente autonomo live |
| GATE | Test end-to-end interruzioni, resume, collisioni multi-repo e stop/approvazione esplicita | **98** | **62** | CAP-0068 | Nessuna esecuzione autonoma merge/release senza autorizzazione |
| RIUSO | Valutare OpenHands Agent Canvas come console/sandbox multi-backend, non sostituto automatico | **88** | **61** | — | MIT core ma integrazione con code proprietario locale richiede protocollo |
| MIGLIORIA | Usare GBrain MCP già attivo per decisioni, checkpoint e provenance, senza duplicare memoria | **83** | **76** | — | Source of truth GitHub ancora prevale |

## Finance Intelligence Agent
Source: [Finance-Intelligence-Agent@44a947f043c720bd95ddb1014428f0c08148c6a6](https://github.com/riccardopinato/Finance-Intelligence-Agent/tree/44a947f043c720bd95ddb1014428f0c08148c6a6) · [ROADMAP.md](https://github.com/riccardopinato/Finance-Intelligence-Agent/blob/44a947f043c720bd95ddb1014428f0c08148c6a6/ROADMAP.md).
**Stato documentale:** Design/knowledge bootstrap, NON bot di trading attivo e NON connessione broker/portfolio reale.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Schema quotazioni, valuta, corporate actions, delay, trading calendar e provider con licenza dati | **99** | **79** | — | È ancora il primo maxi-step non completato |
| GATE | Motore P&L, fee, FX, concentrazione e drawdown con fixture sintetiche e test numerici | **98** | **76** | — | Nessuna decisione finanziaria affidabile senza contabilità corretta |
| MIGLIORIA | Watchlist e report con fonti citabili, timestamp espliciti, cooldown alert e controllo falsi positivi | **85** | **75** | — | Read-only prima di analisi automatica |
| RIUSO | GBrain per memoria fonti/decisioni e Agent Core per schedulazione solo quando gate E3 | **78** | **62** | — | Mai mettere dati conto in repository pubblico |
| RICERCA | Non riusare direttamente bTrader/Binance per azioni/ETF né abilitare ordini automatici | **92** | **87** | — | Domini e rischi finanziari differenti |

## Interactive Scene Core
Source: [Interactive-Scene-Core@1ab3a7a22ff7d8f9da0bef59ae1e6e20b2d66012](https://github.com/riccardopinato/Interactive-Scene-Core/tree/1ab3a7a22ff7d8f9da0bef59ae1e6e20b2d66012) · [ROADMAP.md](https://github.com/riccardopinato/Interactive-Scene-Core/blob/1ab3a7a22ff7d8f9da0bef59ae1e6e20b2d66012/ROADMAP.md).
**Stato documentale:** Candidate extraction, solo contratti descrittivi; renderer/scene-model non ancora estratti dal prodotto Deskland.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Audit provenienza file e isolamento GPL del Deskland originale prima di estrarre codice/asset | **98** | **86** | CAP-0024 | Originale Deskland solo UX, non donor copiabile |
| GATE | Estrarre modelli puri viewport/zones/objects/occupancy con schema-2 e test migrazioni | **93** | **77** | CAP-0028/0029 | Senza dipendenze shader o wallpaper |
| MIGLIORIA | Benchmark separati Flutter Canvas e Kotlin Wallpaper GPU, frame pacing e batteria | **88** | **56** | CAP-0024 | No certificazione finché manca prova su device |
| RIUSO | Esperimento opzionale in Notes Vision Board dopo test e Product Bible, non nuovo launcher | **73** | **69** | CAP-0029 | Testare due consumer prima di Golden |

## Design-App — repository stili
Source: [Design-App@cfcd6643537cfcf0987a058af83009b2e69eb54f](https://github.com/riccardopinato/Design-App/tree/cfcd6643537cfcf0987a058af83009b2e69eb54f) · [sources/STARS_750_VISUAL_INTAKE_2026-11-16.md](https://github.com/riccardopinato/Design-App/blob/cfcd6643537cfcf0987a058af83009b2e69eb54f/sources/STARS_750_VISUAL_INTAKE_2026-11-16.md).
**Stato documentale:** Registro 105 fonti esterne dopo PR #24; 7 nuove tldraw/Excalidraw/xyflow/Markmap/OpenWidget/AppFlowyEditor/Nodus, tutte REFERENCE; nessun asset o codice importato.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Per ogni source pin: SPDX per file, eventuali asset protetti, licenze SDK e limiti commerciali | **98** | **84** | CAP-0023 | NOASSERTION non significa MIT, tldraw richiede gate SDK |
| MIGLIORIA | Matrice pixel/motion per Notes, Anna e Deskland con benchmark visivi e accessibilità | **93** | **79** | CAP-0023/0024 | Riutilizzare design token, non copiare UI senza verifica |
| RIUSO | Studio xyflow per grafi App Factory e AppFlowy Editor per editor Flutter Notes | **88** | **72** | CAP-0161 | Due progetti diversi: scegliere componenti solo dopo benchmark |
| MIGLIORIA | Preview visiva delle source con overlay e URL, audit duplicati e riferimenti alle immagini autorizzate | **79** | **85** | CAP-0023 | Link verificabili, evitare duplicare immagini in repo senza diritti |

## App Factory Core
Source: [App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619](https://github.com/riccardopinato/App-Factory-Core/tree/c5adc147046beb7024629466d10eeb799c3c2619) · [CURRENT.yaml](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/CURRENT.yaml).
**Stato documentale:** CURRENT punta a Master v27, Golden Index v29, Registry v2; è fonte normativa di riuso della Factory.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Gates automatici per distinguere stato PROPOSED/CI/E4, device e licenze nel flusso CAP/Golden | **96** | **82** | CAP-0068 | Mai promuovere fonte esterna a donor per analogia |
| MIGLIORIA | Golden template per external security-tools orchestration AppLab dopo prove riproducibili | **89** | **76** | CAP-0068 | Trivy/Semgrep/CodeQL come tool, senza duplicare AppLab |
| MIGLIORIA | Resolver CURRENT + source SHA a prova di stale context su 35 repos con stato CI esplicito | **94** | **85** | — | Evitare linee storiche e checkout non pinnati |
| RICERCA | Nessuna nuova Golden visiva da queste stelle finché manca un donor E3 e consumer test | **84** | **90** | CAP-0023 | Master governance non equivale a codice pronto |

## Analisi delle mie stelle GitHub
Source: [Analisi-delle-mie-stelle-github@dc3d3e6cdf5bdfb6ca8d2984b430adde1aff7d1e](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/tree/dc3d3e6cdf5bdfb6ca8d2984b430adde1aff7d1e) · [research/INCROCIO_OSS95_2026-11-16.md](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/dc3d3e6cdf5bdfb6ca8d2984b430adde1aff7d1e/research/INCROCIO_OSS95_2026-11-16.md).
**Stato documentale:** 737 stelle pubbliche, 110 nuove vs 632 ottobre; 89 già OSS95, 4 note altrove, 17 senza dossier precedente; gap 13 con conteggio UI 750.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Ottenere solo con accesso autorizzato il gap di 13 stelle non enumerabili e deduplica storica | **97** | **46** | — | No token in chat; usare fonte autenticata/export esplicito |
| MIGLIORIA | Diff hash README/commit automatico per le 19 fonti OSS95 variate e triage su feature effettive | **89** | **84** | — | README diverso non è codice modificato |
| MIGLIORIA | Rendere il ranking incrementale e normalizzare rename, source lineage, licenza e use case per app | **85** | **86** | — | Conservare 632/737/110 e non sovrascrivere snapshot storici |
| MIGLIORIA | Registrazione crosswalk app/CAP con storico delle decisioni e no auto-ingestion product | **91** | **87** | — | La ricerca non promuove nuove CAP senza anti-dedup |

## Idee-app — catalogo e capability
Source: [Idee-app-Archivi-riferimenti@a0922a114af04d806888765e9dcf3e336bdaf184](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/tree/a0922a114af04d806888765e9dcf3e336bdaf184) · [12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/a0922a114af04d806888765e9dcf3e336bdaf184/12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
**Stato documentale:** 199 CAP, inventory HEAD del 08/11 su 31 repo, account ora 35 repo; fonti stelle e nuove idee registrate nella PR #168.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Allineare inventory da 31 a 35 repo live con HEAD pin, scope e stato per ciascuno | **99** | **88** | — | Non inferire implementazioni da cataloghi storici |
| GATE | Reconcile stati CAP per app e consumer code, de-duplicare sinonimi tra 199 CAP | **98** | **82** | — | Nuove fonti non corrispondono a 110 CAP nuove |
| MIGLIORIA | Roadmap per app con dependency graph, blocker e priorità/fattibilità come dati versionati | **92** | **85** | — | Tenere separato implementato, verificato e proposto |
| MIGLIORIA | Tracciamento storico decisions e provenance da stelle → ricerca → CAP → app → test | **90** | **86** | CAP-0068 | Permette aggiornamenti senza perdere decisioni precedenti |

