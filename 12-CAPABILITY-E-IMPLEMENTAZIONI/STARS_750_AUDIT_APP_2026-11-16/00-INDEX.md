# Audit specifico di ogni app — stelle GitHub, CAP, roadmap (16 novembre 2026)

**Perimetro completo:** 35 repository GitHub accessibili (26 app/prototipi e 9 infrastrutture/registri), più 24 app e concept presenti fra i 199 CAP ma senza repository omonimo verificato: **59 schede, 197 interventi**, ognuno con **Priorità P** e **Fattibilità F** 0–100. Livello delle 24 schede CAP-only inferiore: non attribuire a codice reale il contenuto di una CAP proposta.

**Confini di evidenza:** repo source/HEAD + README/roadmap/Product Bible dove disponibili; non è stato eseguito un full repository deep code audit, l’intera suite CI su 35 HEAD né prove fisiche. L'attività classifica opportunità e blocchi, non implementa funzioni. PR draft ≠ main. APK firmato ≠ nuova source. Le licenze per file richiedono gate separati; le percentuali non sono probabilità.

**Factory baseline:** `riccardopinato/App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29 · registry v2. **Stars source:** [737 pubbliche/110 nuove](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/main/research/CLASSIFICA_CURATA_110_2026-11-16.md), 17 non precedentemente catalogate dopo OSS95 e 4 altre fonti già note; 13 non identificabili in API pubblica rispetto alle 750 riferite dall'utente.

## Metodo dei punteggi

**Priorità P (0–100):** protezione dell'utente/sicurezza, blocco di release o core flow, impatto UX, riuso trasversale, urgenza di contenuto verificabile. **Fattibilità F (0–100):** compatibilità stack esistente, complessità e invasività, copertura QA possibile, dipendenze hardware/provider, necessità di dati/licenze; non è una probabilità. P 95–100 = P0/P1 prioritario, 80–94 = alta, 65–79 = media, sotto 65 = futura/solo studio; F >=85 = intervento circoscritto, 70–84 = ragionevole, 50–69 = complesso, <50 = altamente condizionato. Non applicare automaticamente gli score ai budget/sprint senza Product Bible e stime vere.

## Schede dettagliate

| Dossier | App/ambito | Interventi | Priorità più alta | Fattibilità del primo intervento prioritario | Evidenza |
|---|---|---:|---:|---:|---|
| [01_APP_A_M](01_APP_A_M.md#180flipcharge-rotate-180) | 180FlipCharge — Rotate 180° | 3 | **97** | **70** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#adaptive-landscape-deskland) | Adaptive Landscape / Deskland | 4 | **99** | **55** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#annas-diary) | Anna’s Diary | 4 | **99** | **76** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#android-omni-cleaner) | Android Omni Cleaner | 4 | **99** | **76** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#corpo-umano) | Corpo Umano | 4 | **94** | **74** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#framelab-repo-principale) | FrameLab (repo principale) | 4 | **97** | **79** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#battery-guard) | Battery Guard | 4 | **99** | **68** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#btrader-arbitraggio-crypto) | bTrader — arbitraggio crypto | 3 | **98** | **66** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#camperboss) | CamperBoss | 4 | **96** | **70** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#cozy-game-progetto) | Cozy game — progetto | 3 | **91** | **66** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#interview-prep-coach-pwa) | Interview Prep Coach PWA | 3 | **92** | **87** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#focusense) | FocuSense | 4 | **99** | **68** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#framelab-repo-parallelo) | FrameLab (repo parallelo) | 3 | **97** | **91** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#in-cucina-con-gli-anime-cooking-anime) | In Cucina con gli Anime / Cooking Anime | 4 | **99** | **67** | HEAD + DOC |
| [01_APP_A_M](01_APP_A_M.md#neon-arcade-runner) | Neon Arcade Runner | 4 | **97** | **63** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#notes-ecosistema) | Notes — Ecosistema | 6 | **98** | **74** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#notification-control) | Notification Control | 4 | **99** | **63** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#pdf-unifier) | PDF Unifier | 4 | **97** | **82** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#phone-guard) | Phone Guard | 4 | **99** | **64** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#pocket-guard-pockara) | Pocket Guard / Pockara | 4 | **98** | **70** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#send-to-pc) | Send to PC | 4 | **99** | **67** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#tabletop-motion-alarm) | Tabletop Motion Alarm | 4 | **99** | **69** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#tasteai) | TasteAI | 5 | **97** | **80** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#trailpath) | TrailPath | 5 | **100** | **53** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#wonderlog) | Wonderlog | 4 | **99** | **64** | HEAD + DOC |
| [02_APP_N_Z](02_APP_N_Z.md#world-days) | World Days | 5 | **100** | **70** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#1000-ai-collection-tools-archivio-esterno) | 1000 AI Collection Tools — archivio esterno | 3 | **90** | **95** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#applab) | AppLab | 5 | **99** | **65** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#app-factory-agent-core) | App Factory Agent Core | 4 | **99** | **54** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#finance-intelligence-agent) | Finance Intelligence Agent | 5 | **99** | **79** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#interactive-scene-core) | Interactive Scene Core | 4 | **98** | **86** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#design-app-repository-stili) | Design-App — repository stili | 4 | **98** | **84** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#app-factory-core) | App Factory Core | 4 | **96** | **82** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#analisi-delle-mie-stelle-github) | Analisi delle mie stelle GitHub | 4 | **97** | **46** | HEAD + DOC |
| [03_INFRA_AGENTI](03_INFRA_AGENTI.md#idee-app-catalogo-e-capability) | Idee-app — catalogo e capability | 4 | **99** | **88** | HEAD + DOC |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#app-profiles) | App-Profiles | 3 | **87** | **84** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#beerclass-ai) | BeerClass AI | 3 | **91** | **71** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#cashmate-ai) | CashMate AI | 3 | **96** | **79** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#cleanos) | CleanOS | 2 | **95** | **89** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#cmdpocket) | CmdPocket | 3 | **91** | **84** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#deskpilot) | DeskPilot | 2 | **91** | **56** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#devpocket-tools) | DevPocket Tools | 2 | **85** | **91** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#downloads-butler) | Downloads Butler | 2 | **90** | **78** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#easy-debloat) | Easy Debloat | 3 | **98** | **71** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#edgedock) | EdgeDock | 2 | **93** | **63** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#grillboss) | GrillBoss | 2 | **83** | **73** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#home-assets-passport) | Home Assets Passport | 2 | **92** | **78** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#mealmate) | MealMate | 3 | **89** | **77** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#pdf-pocket-tools) | PDF Pocket Tools | 2 | **95** | **84** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#safeshare) | SafeShare | 2 | **94** | **82** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#sleepmax-coach) | SleepMax Coach | 3 | **96** | **78** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-002) | WEB-002 | 2 | **94** | **69** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-004) | WEB-004 | 2 | **95** | **61** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-008) | WEB-008 | 2 | **90** | **67** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-009) | WEB-009 | 2 | **94** | **88** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-012) | WEB-012 | 2 | **91** | **80** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-014) | WEB-014 | 2 | **96** | **72** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#web-utility) | WEB-UTILITY | 2 | **82** | **91** | CAP-only |
| [04_CAP_ONLY_NO_REPO](04_CAP_ONLY_NO_REPO.md#work-time-keeper) | Work-Time-Keeper | 3 | **92** | **80** | CAP-only |

## P0/P1 prioritari delle app/repository verificabili

| Progetto | Intervento | P | F | Tipo |
|---|---|---:|---:|---|
| World Days | Wave editoriali sulle 626 ricorrenze senza dossier originale: fonti istituzionali e 6 lingue con checkpoint | 100 | 70 | GATE |
| TrailPath | Rilevare e correggere cause routing fallito e percorsi deviati: provider, snap, percorso breve, trace | 100 | 53 | GATE |
| Idee-app — catalogo e capability | Allineare inventory da 31 a 35 repo live con HEAD pin, scope e stato per ciascuno | 99 | 88 | GATE |
| Finance Intelligence Agent | Schema quotazioni, valuta, corporate actions, delay, trading calendar e provider con licenza dati | 99 | 79 | GATE |
| Anna’s Diary | APK firmato da main v135/v136 con installazione in-place e regression test account/media/backup | 99 | 76 | GATE |
| Android Omni Cleaner | Chiudere PR #23: schermate dedicate e Gallery a proporzioni originali con lettore video e scelta elimina/conserva | 99 | 76 | GATE |
| Tabletop Motion Alarm | Test allarme screen-off, movimento e recovery dopo kill/reboot su Pixel/Samsung/Xiaomi | 99 | 69 | GATE |
| Battery Guard | Certificazione OEM: FGS, temperatura, notifica soglie, allarmi 20–90% e aggiornamento in-place | 99 | 68 | GATE |
| FocuSense | Sensori reali e falsi positivi pickup/schermo spento, microfono FGS, burn-in AMOLED e batteria | 99 | 68 | GATE |
| Android Omni Cleaner | Test fisici per MediaStore, Android Trash, SAF, partial access, keeper duplicati e restore verificato | 99 | 67 | GATE |
| In Cucina con gli Anime / Cooking Anime | Riconciliare 20 ricette runtime con lotti draft (fino a 112) e review culinaria/traduzioni | 99 | 67 | GATE |
| Send to PC | Collaudo Android ↔ browser su reti reali, router isolati, hotspot, IP change e recovery download grandi | 99 | 67 | GATE |
| AppLab | Concludere self-canary repair con 3 riparazioni indipendenti a SHA verificato prima di dichiarare autonomia | 99 | 65 | GATE |
| Phone Guard | Collaudo fisico multipiattaforma FGS, screen-off, sensori, vibrazione/sirena e recovery | 99 | 64 | GATE |
| Wonderlog | Parità Flutter rispetto legacy: import/upgrade, media, mappe, note e lossless sync con dati reali | 99 | 64 | GATE |
| Notification Control | Matrix Android/OEM NotificationListenerService: kill, reboot, DND, permessi, process death, dati duplicati | 99 | 63 | GATE |
| TrailPath | GPS fisico e persistenza track/GPX con Doze, background, riavvio e rete intermittente | 99 | 61 | GATE |
| Adaptive Landscape / Deskland | P0 launcher/home: fallback al launcher originale, Android gesture navigation e recovery dopo crash/OEM | 99 | 55 | GATE |
| App Factory Agent Core | Collegare worker Windows/WSL reale a JobGraph con lease, retry, idempotenza, credenziali e approve-boundaries | 99 | 54 | GATE |
| World Days | Chiudere 7 hold filippini con fonti legali ufficiali, date mobili e controllo lingua | 99 | 48 | GATE |
| Interactive Scene Core | Audit provenienza file e isolamento GPL del Deskland originale prima di estrarre codice/asset | 98 | 86 | GATE |
| Design-App — repository stili | Per ogni source pin: SPDX per file, eventuali asset protetti, licenze SDK e limiti commerciali | 98 | 84 | GATE |
| Idee-app — catalogo e capability | Reconcile stati CAP per app e consumer code, de-duplicare sinonimi tra 199 CAP | 98 | 82 | GATE |
| Finance Intelligence Agent | Motore P&L, fee, FX, concentrazione e drawdown con fixture sintetiche e test numerici | 98 | 76 | GATE |
| Notes — Ecosistema | Audit full journey Smart Inbox suggerimento → preview → writer canonico con permessi, undo e account switch | 98 | 74 | GATE |
| Send to PC | UX sicurezza TLS: fingerprint leggibile, QR/PIN e warning self-signed spiegati senza bypass silenzioso | 98 | 72 | GATE |
| Pocket Guard / Pockara | False positives e veri furti simulati: movimento tasca/borsa, trasporto, dispositivi diversi, Doze | 98 | 70 | GATE |
| bTrader — arbitraggio crypto | Audit dipendenze Rust, autenticazione e compatibilità API exchange prima di esecuzioni o fork | 98 | 66 | GATE |
| App Factory Agent Core | Test end-to-end interruzioni, resume, collisioni multi-repo e stop/approvazione esplicita | 98 | 62 | GATE |
| Notification Control | Validazione Store e privacy: restricted settings, permessi, retention e recovery di media con limiti Play | 98 | 61 | GATE |
| Notes — Ecosistema | Rendere Web durabile per dataset grandi: migrazione versionata localStorage → IndexedDB/SQLite Web, backup e rollback | 98 | 58 | GATE |
| FrameLab (repo parallelo) | Diff di sorgenti, dipendenze, contenuti e build SHA tra i due FrameLab; scegliere source of truth | 97 | 91 | GATE |
| AppLab | Introdurre Trivy per SBOM/CVE/secrets in modalità read-only, report-only prima di blocking | 97 | 85 | RIUSO |
| PDF Unifier | Test PDF uniti: ordine pagine, orientamento, bookmark, dimensioni, password, input malformato e recovery | 97 | 82 | GATE |
| TasteAI | Pipeline PDF ricette: estrazione, normalizzazione, dedup e verifica ingredienti/allergeni/manuale | 97 | 80 | GATE |
| FrameLab (repo principale) | Chiudere hardening MVP, avvio APK Android e regressioni visuali/materiali prima della pubblicazione | 97 | 79 | GATE |
| In Cucina con gli Anime / Cooking Anime | Diritti dei riferimenti anime, originalità illustrazioni, sicurezza alimentare e pubblicazione asset | 97 | 75 | GATE |
| Phone Guard | Tuning grace, calibrazione e protezione da allarmi errati quando viene recuperato il telefono | 97 | 71 | GATE |

## Quick wins: P ≥ 85 e F ≥ 82 (top 24)

| Progetto | Intervento | P | F |
|---|---|---:|---:|
| FrameLab (repo parallelo) | Diff di sorgenti, dipendenze, contenuti e build SHA tra i due FrameLab; scegliere source of truth | 97 | 91 |
| Idee-app — catalogo e capability | Allineare inventory da 31 a 35 repo live con HEAD pin, scope e stato per ciascuno | 99 | 88 |
| 1000 AI Collection Tools — archivio esterno | Non trattare la presenza di un nome in lista come licenza o codice da integrare | 90 | 95 |
| TrailPath | Riorganizzare i cinque controlli circolari, layout 320–390px, safe area e gesture accessibili | 94 | 90 |
| Interactive Scene Core | Audit provenienza file e isolamento GPL del Deskland originale prima di estrarre codice/asset | 98 | 86 |
| AppLab | Introdurre Trivy per SBOM/CVE/secrets in modalità read-only, report-only prima di blocking | 97 | 85 |
| Design-App — repository stili | Per ogni source pin: SPDX per file, eventuali asset protetti, licenze SDK e limiti commerciali | 98 | 84 |
| Idee-app — catalogo e capability | Reconcile stati CAP per app e consumer code, de-duplicare sinonimi tra 199 CAP | 98 | 82 |
| Interview Prep Coach PWA | Percorso test end-to-end PWA: avvio, sessione, salvataggio progresso, reset cache e offline | 92 | 87 |
| Finance Intelligence Agent | Non riusare direttamente bTrader/Binance per azioni/ETF né abilitare ordini automatici | 92 | 87 |
| App Factory Core | Resolver CURRENT + source SHA a prova di stale context su 35 repos con stato CI esplicito | 94 | 85 |
| PDF Unifier | Test PDF uniti: ordine pagine, orientamento, bookmark, dimensioni, password, input malformato e recovery | 97 | 82 |
| Analisi delle mie stelle GitHub | Registrazione crosswalk app/CAP con storico delle decisioni e no auto-ingestion product | 91 | 87 |
| App Factory Core | Gates automatici per distinguere stato PROPOSED/CI/E4, device e licenze nel flusso CAP/Golden | 96 | 82 |
| Tabletop Motion Alarm | Step7 localizzazione completa IT/EN/ES/DE/FR/PT, notifiche ed errori | 89 | 88 |
| Idee-app — catalogo e capability | Roadmap per app con dependency graph, blocker e priorità/fattibilità come dati versionati | 92 | 85 |
| Android Omni Cleaner | Scansioni sicurezza APK con MobSF e Trivy in AppLab, senza dipendenze incorporate | 90 | 86 |
| FrameLab (repo parallelo) | Definire modalità mirror/donor read-only e una sola pipeline editoriale certificante | 90 | 86 |
| Idee-app — catalogo e capability | Tracciamento storico decisions e provenance da stelle → ricerca → CAP → app → test | 90 | 86 |
| Analisi delle mie stelle GitHub | Diff hash README/commit automatico per le 19 fonti OSS95 variate e triage su feature effettive | 89 | 84 |
| Analisi delle mie stelle GitHub | Rendere il ranking incrementale e normalizzare rename, source lineage, licenza e use case per app | 85 | 86 |
| 1000 AI Collection Tools — archivio esterno | Verificare link, sopravvivenza progetti, termini e provider prima di usare catalogo come fonte | 88 | 83 |
| TasteAI | Lista della spesa generata da ricette presenti e quantità/porzioni con edit esplicito | 88 | 82 |
| 180FlipCharge — Rotate 180° | Eccezioni per-app: fallback esplicito quando Android ignora orientamento e tile non disponibile | 87 | 82 |

## Migliorie/riuso tecnicamente promettenti (non solo gate)

| Progetto | Miglioria | P | F | Tipo |
|---|---|---:|---:|---|
| TrailPath | Riorganizzare i cinque controlli circolari, layout 320–390px, safe area e gesture accessibili | 94 | 90 | MIGLIORIA |
| AppLab | Introdurre Trivy per SBOM/CVE/secrets in modalità read-only, report-only prima di blocking | 97 | 85 | RIUSO |
| App Factory Core | Resolver CURRENT + source SHA a prova di stale context su 35 repos con stato CI esplicito | 94 | 85 | MIGLIORIA |
| Analisi delle mie stelle GitHub | Registrazione crosswalk app/CAP con storico delle decisioni e no auto-ingestion product | 91 | 87 | MIGLIORIA |
| Idee-app — catalogo e capability | Roadmap per app con dependency graph, blocker e priorità/fattibilità come dati versionati | 92 | 85 | MIGLIORIA |
| AppLab | Introdurre Semgrep/CodeQL con regole Flutter/Kotlin + triage falsi positivi su PR | 96 | 81 | RIUSO |
| Android Omni Cleaner | Scansioni sicurezza APK con MobSF e Trivy in AppLab, senza dipendenze incorporate | 90 | 86 | RIUSO |
| FrameLab (repo parallelo) | Definire modalità mirror/donor read-only e una sola pipeline editoriale certificante | 90 | 86 | MIGLIORIA |
| Idee-app — catalogo e capability | Tracciamento storico decisions e provenance da stelle → ricerca → CAP → app → test | 90 | 86 | MIGLIORIA |
| Anna’s Diary | Completare e collaudare Quaderno iOS Journal del Calendario e Week con selezione, densità e accessibilità | 94 | 81 | MIGLIORIA |
| Analisi delle mie stelle GitHub | Diff hash README/commit automatico per le 19 fonti OSS95 variate e triage su feature effettive | 89 | 84 | MIGLIORIA |
| Design-App — repository stili | Matrice pixel/motion per Notes, Anna e Deskland con benchmark visivi e accessibilità | 93 | 79 | MIGLIORIA |
| Analisi delle mie stelle GitHub | Rendere il ranking incrementale e normalizzare rename, source lineage, licenza e use case per app | 85 | 86 | MIGLIORIA |
| TasteAI | Lista della spesa generata da ricette presenti e quantità/porzioni con edit esplicito | 88 | 82 | MIGLIORIA |
| Battery Guard | Spiegazioni livello di confidenza del Battery Health Lab e qualità delle misurazioni | 84 | 85 | MIGLIORIA |
| In Cucina con gli Anime / Cooking Anime | Checklist ricetta passo-passo, porzioni, unità e ingredienti con fallback offline | 84 | 85 | MIGLIORIA |
| 180FlipCharge — Rotate 180° | Eccezioni per-app: fallback esplicito quando Android ignora orientamento e tile non disponibile | 87 | 82 | MIGLIORIA |
| TasteAI | Anti-Waste con spiegazione degli ingredienti effettivamente usati, senza presunte scadenze | 85 | 83 | MIGLIORIA |
| World Days | Feed quotidiano, preferiti/letture salvate, serie tematiche e ricerca incrociata per retention | 85 | 83 | MIGLIORIA |
| Interview Prep Coach PWA | Flashcard con spaced repetition e spiegazioni per ruoli tech da Anki, senza import codice GPL | 82 | 86 | RIUSO |
| Notification Control | Audit restore/rollback crittografato dei backup e switching profilo, revisioni Vault e indicatori affidabilità | 94 | 75 | MIGLIORIA |
| Tabletop Motion Alarm | Onboarding e preset sensibilità per tavoli instabili con modalità test | 87 | 79 | MIGLIORIA |
| Pocket Guard / Pockara | Scelta modalità assistita con test rapido sensori e diagnostica permission-health | 84 | 81 | MIGLIORIA |
| App Factory Core | Golden template per external security-tools orchestration AppLab dopo prove riproducibili | 89 | 76 | MIGLIORIA |

## Guardrail

- Prima leggere il README, Product Bible e la roadmap riferiti al commit esatto, poi aprire una PR separata per ogni ambito autorizzato. Qui non si modifica codice delle app.
- Le CAP già esistenti restano le stesse: CAP-0031 voce offline, CAP-0042 cataloghi editoriali, CAP-0068 evidence ladder, CAP-0098 mind-map, CAP-0112 flashcard, CAP-0144 widget, CAP-0148 Smart Inbox, CAP-0161 editor, CAP-0167 CRDT, CAP-0182 sticky desktop e altre citate nelle schede. Nessuna nuova CAP duplicata è stata introdotta.
- Per le 24 idee senza repo non dichiarare build, implementazione, monetizzazione o device-pass: l'evidenza è il catalogo CAP, non il codice.
- Priorità release: risolvere difetti core e dati prima di aggiungere moduli AI, widget, animazioni o monetizzazione non funzionante.

## Download dati

- JSON in [`data/APP_BY_APP_STARS_AUDIT_2026-11-16.json`](./data/APP_BY_APP_STARS_AUDIT_2026-11-16.json) con ID record, fonte, HEAD, score, CAP, rationale, classe di evidenza. I file Markdown per gruppo sono source of truth narrativa e restano disponibili anche senza JSON.

