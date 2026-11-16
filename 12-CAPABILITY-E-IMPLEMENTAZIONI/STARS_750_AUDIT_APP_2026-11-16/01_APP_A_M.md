# Audit specifico per app — blocco A–M, 16 novembre 2026

**Metodo:** verificati GitHub HEAD, README e roadmap/Product Bible disponibili. P = priorità strategica e rischio prodotto (100 massima). F = fattibilità tecnica/operativa stimata (100 più semplice). Non sono probabilità; gate licenza, Play, device e accessibilità restano separati. `GATE` = evidenza/punto bloccante; `MIGLIORIA` = estensione su codice esistente; `NUOVA` = proposta nuova; `RIUSO` = pattern/donor da verificare; `RICERCA` = sola indagine.

**Limiti:** questa ricognizione NON è un audit completo di tutto il codice né una prova hardware. Le PR aperte non sono su `main`; README e roadmap non provano da soli la presenza di funzionalità runtime. Fonti delle opportunità: [classifica stelle](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/main/research/CLASSIFICA_CURATA_110_2026-11-16.md), [registro CAP](../REGISTRO_CAPABILITY.json), [audit OSS95](../OSS95_SOURCE_SNAPSHOT_2026-11-08.json).

## 180FlipCharge — Rotate 180°
Source: [180FlipCharge@7de05b83e3465225f9732da489c08e6140026c46](https://github.com/riccardopinato/180FlipCharge/tree/7de05b83e3465225f9732da489c08e6140026c46) · [README.md](https://github.com/riccardopinato/180FlipCharge/blob/7de05b83e3465225f9732da489c08e6140026c46/README.md).
**Stato verificato documentalmente:** Kotlin/Compose 0.8.3: rotazione 0°/180°, Tile, automazione ricarica e budget APK dichiarati; release fisica non dimostrata da questa scansione.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Collaudo rotazione reale su Xiaomi/Pixel/Samsung, schermata bloccata e app full-screen | **97** | **70** | — | Priorità a stabilità/compatibilità prima di aggiungere modalità |
| MIGLIORIA | Eccezioni per-app: fallback esplicito quando Android ignora orientamento e tile non disponibile | **87** | **82** | CAP-0058 | Non alterare la politica 0°/180° e non promettere rotazioni non supportate |
| MIGLIORIA | Profilo rapido con spiegazioni accessibili, diagnostica dello stato e benchmark consumo overlay | **78** | **86** | CAP-0058 | Feature circoscritta, senza monitoraggi invasivi |

## Adaptive Landscape / Deskland
Source: [Adaptive-Landscape-Android@2dcaf70a1d4962e9e81490d84df4f89f355cb7d4](https://github.com/riccardopinato/Adaptive-Landscape-Android/tree/2dcaf70a1d4962e9e81490d84df4f89f355cb7d4) · [docs/ROADMAP.md](https://github.com/riccardopinato/Adaptive-Landscape-Android/blob/2dcaf70a1d4962e9e81490d84df4f89f355cb7d4/docs/ROADMAP.md).
**Stato verificato documentalmente:** Flutter + WallpaperService; upstream Deskland solo reference GPL; numerosi esperimenti Home aperti in PR non ancora in main.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | P0 launcher/home: fallback al launcher originale, Android gesture navigation e recovery dopo crash/OEM | **99** | **55** | CAP-0088 | Main non include automaticamente le PR sperimentali #34-38; serve matrice fisica |
| GATE | Qualità realistica dell'acqua e mappatura effettiva di icone/widget su schermi e launcher | **96** | **50** | CAP-0088 | Confronto screenshot Android/Web e collaudo visuale, non solo CI |
| MIGLIORIA | FPS, memoria, GPU e consumo con Adaptive Quality e reduced-motion su device reale | **93** | **64** | CAP-0024 | Prima di animazioni nuove evitare battery drain |
| RIUSO | HUD, dock, widget e modalità gioco ispirati a OpenWidget/OpenTaskbar/LumaBar | **76** | **60** | CAP-0088 | Riferimenti Windows/proprietari solo UX, dopo stabilità launcher |

## Anna’s Diary
Source: [Agenda-per-Anna@adef11af02d638e0064bd9d5e3fdb0b23774c9cb](https://github.com/riccardopinato/Agenda-per-Anna/tree/adef11af02d638e0064bd9d5e3fdb0b23774c9cb) · [README.md](https://github.com/riccardopinato/Agenda-per-Anna/blob/adef11af02d638e0064bd9d5e3fdb0b23774c9cb/README.md).
**Stato verificato documentalmente:** Flutter diario privato/condiviso; main integra dashboard +135; PR #335 calendario v136 aperta; APK firmato +134 documentato, non automaticamente uguale a main.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | APK firmato da main v135/v136 con installazione in-place e regression test account/media/backup | **99** | **76** | CAP-0068 | Firmato +134 è un'altra sorgente; non equiparare CI/Web a collaudo fisico |
| MIGLIORIA | Completare e collaudare Quaderno iOS Journal del Calendario e Week con selezione, densità e accessibilità | **94** | **81** | CAP-0023/0024 | PR #335 aperta, non contare in main |
| RIUSO | Widget calendario Android privacy-safe con filtri/aggiornamento come Todo Agenda | **79** | **68** | CAP-0144 | Riusare proiezioni dati canonici; evitare visualizzazione privata sul lock screen |
| NUOVA | Cattura vocale locale di un ricordo con revisione testuale facoltativa | **57** | **55** | CAP-0031 | whisper.cpp reference; modello on-demand e permessi espliciti, non prioritaria |

## Android Omni Cleaner
Source: [Android-Omni-Cleaner@984474d9af62d8b7e17b975a31332161f24f2df7](https://github.com/riccardopinato/Android-Omni-Cleaner/tree/984474d9af62d8b7e17b975a31332161f24f2df7) · [PRODUCT_BIBLE.md](https://github.com/riccardopinato/Android-Omni-Cleaner/blob/984474d9af62d8b7e17b975a31332161f24f2df7/PRODUCT_BIBLE.md).
**Stato verificato documentalmente:** Kotlin/Compose rc1, indicizzazione SQLite e safe trash; PR #23 audit e #22 design sono draft aperte, non main.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Chiudere PR #23: schermate dedicate e Gallery a proporzioni originali con lettore video e scelta elimina/conserva | **99** | **76** | CAP-0023/0024 | Scansione attuale main non certifica il codice draft né l'APK |
| GATE | Test fisici per MediaStore, Android Trash, SAF, partial access, keeper duplicati e restore verificato | **99** | **67** | CAP-0068 | Operazioni distruttive: verifica invarianti e OEM prima di rilascio |
| RIUSO | Scansioni sicurezza APK con MobSF e Trivy in AppLab, senza dipendenze incorporate | **90** | **86** | CAP-0068 | Sicurezza e regressione di release |
| NUOVA | Raggruppamento immagini simili con hash percettivo e revisione manuale, non cancellazione automatica | **69** | **59** | CAP-0083 | Differente dalla deduplica esatta già implementata; P2 dopo collaudo |

## Corpo Umano
Source: [App-corpo-umano@65c79df53209e727918d316bb2fa6b625a15c6fa](https://github.com/riccardopinato/App-corpo-umano/tree/65c79df53209e727918d316bb2fa6b625a15c6fa) · [README.md](https://github.com/riccardopinato/App-corpo-umano/blob/65c79df53209e727918d316bb2fa6b625a15c6fa/README.md).
**Stato verificato documentalmente:** App didattica Flutter 0.18.0+18; README minimale, copertura anatomica non certificabile dalla sola introduzione.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Audit anatomico di contenuti, etichette e fonti rispetto ai modelli realmente inclusi | **94** | **74** | — | Non dedurre dal nome/vecchie chat completezza dei 206 elementi |
| RIUSO | Flashcard e ripasso distribuito da Anki/AnkiDroid con revisione delle risposte | **84** | **76** | CAP-0112 | Opzionale e collegato alle unità didattiche canoniche |
| MIGLIORIA | Quiz su immagini con zoom, accessibilità e motivazione didattica degli errori | **82** | **81** | CAP-0023 | Test 390px/touch e contenuti realmente presenti |
| NUOVA | Modelli anatomici 3D esplorabili offline con livelli e performance budget | **62** | **43** | — | Alto costo 3D/asset, non priorità MVP |

## FrameLab (repo principale)
Source: [app-fotografia@d310ab4e549f4c9cdb6f081e902cba3e469635e9](https://github.com/riccardopinato/app-fotografia/tree/d310ab4e549f4c9cdb6f081e902cba3e469635e9) · [ROADMAP.md](https://github.com/riccardopinato/app-fotografia/blob/d310ab4e549f4c9cdb6f081e902cba3e469635e9/ROADMAP.md).
**Stato verificato documentalmente:** Flutter offline-first, Step 8 QA MVP e Step 9 pipeline editoriale non conclusi; esiste repo parallelo omonimo.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Chiudere hardening MVP, avvio APK Android e regressioni visuali/materiali prima della pubblicazione | **97** | **79** | CAP-0068 | Step 8 segnalato in corso nella roadmap |
| GATE | Completare Step 9C della pipeline editoriale con fonti, traduzioni, licenze immagini e quality gates | **95** | **78** | CAP-0042 | Non promuovere testi non revisionati |
| MIGLIORIA | Percorsi fotografici e sfide guidate collegate agli stessi contenuti offline e alla libreria personale | **81** | **81** | CAP-0042 | Gamification leggera, non cloud AI |
| RIUSO | Workflow audit immagini/semantica da Cooking Anime e World Days per nuovi lotti | **88** | **75** | CAP-0082 | Riusare gate editoriali, non asset o branding |

## Battery Guard
Source: [Battery_Guard@1343f09d21ace8adf3976b3fd347183f38e5ab68](https://github.com/riccardopinato/Battery_Guard/tree/1343f09d21ace8adf3976b3fd347183f38e5ab68) · [ROADMAP.md](https://github.com/riccardopinato/Battery_Guard/blob/1343f09d21ace8adf3976b3fd347183f38e5ab68/ROADMAP.md).
**Stato verificato documentalmente:** Flutter 1.8.1+27, device intelligence e Charge Protection; firmatura interna e test CI, physical upgrade e Store non certificati.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Certificazione OEM: FGS, temperatura, notifica soglie, allarmi 20–90% e aggiornamento in-place | **99** | **68** | CAP-0068 | Hardware e servizi in background sono gate E4 |
| GATE | Provider AdMob/UMP/Billing, firma produzione e layout annunci su hardware reale | **95** | **64** | — | Source ready non significa store ready |
| MIGLIORIA | Spiegazioni livello di confidenza del Battery Health Lab e qualità delle misurazioni | **84** | **85** | — | Evitare percentuali di salute non supportate |
| MIGLIORIA | Confronto sessioni per cavo/caricatore e diagnostica anomalie già tracciate | **75** | **86** | — | Estendere Charge Doctor senza duplicare Session Store |

## bTrader — arbitraggio crypto
Source: [btrader@efcd884d1b58475fc01e3a9ffa53a22489399eaf](https://github.com/riccardopinato/btrader/tree/efcd884d1b58475fc01e3a9ffa53a22489399eaf) · [README.md](https://github.com/riccardopinato/btrader/blob/efcd884d1b58475fc01e3a9ffa53a22489399eaf/README.md).
**Stato verificato documentalmente:** Fork/reference Rust/Cargo 0.2.0 GPL-3.0 con dipendenze Binance datate; nessuna prova di live trading affidabile.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Audit dipendenze Rust, autenticazione e compatibilità API exchange prima di esecuzioni o fork | **98** | **66** | — | GPL e marketplace, source legacy: non adatto a trading live senza audit |
| MIGLIORIA | Modalità replay/paper con fee, spread, slippage, limiti liquidità e latenza misurata | **95** | **65** | — | Prima risultati simulati verificabili; nessun automatismo ordini |
| GATE | Separare segreti, rate limit e kill switch da Finance Intelligence Agent azionario | **92** | **68** | — | Nessuna esposizione chiavi o portafogli in repo pubblici |

## CamperBoss
Source: [CamperBoss@fe3b10d435e120cc952a90cd6bc06c66b6b2521a](https://github.com/riccardopinato/CamperBoss/tree/fe3b10d435e120cc952a90cd6bc06c66b6b2521a) · [README.md](https://github.com/riccardopinato/CamperBoss/blob/fe3b10d435e120cc952a90cd6bc06c66b6b2521a/README.md).
**Stato verificato documentalmente:** Flutter local-first Android/Web: veicolo, viaggi, mappe, offline e documenti; iOS e StoreKit intenzionalmente differiti.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Validare offline POI, tile MapLibre, riapertura e revisioni dei luoghi con data/fonte visibile | **96** | **70** | CAP-0087 | Necessaria evidenza device, no disponibilità POI inventata |
| GATE | Revisione fisica Android di planner, persistenza documenti e pagamento Pro | **93** | **72** | CAP-0068 | Web test non copre ciclo di vita Android |
| RIUSO | Scambio esplicito diario viaggio ↔ Wonderlog/Anna via Life Bridge COPY/LINK | **82** | **74** | CAP-0020 | Evitare un secondo storage condiviso |
| MIGLIORIA | Checklist manutenzione e costi per viaggio con andamento reale e filtri | **77** | **86** | CAP-0101 | Riusare CRUD locale già presente |

## Cozy game — progetto
Source: [Cozy-game-nome-da-scegliere-@09709a681ed25c9e9be43db71b9b5fd284b08e90](https://github.com/riccardopinato/Cozy-game-nome-da-scegliere-/tree/09709a681ed25c9e9be43db71b9b5fd284b08e90) · [README.md](https://github.com/riccardopinato/Cozy-game-nome-da-scegliere-/blob/09709a681ed25c9e9be43db71b9b5fd284b08e90/README.md).
**Stato verificato documentalmente:** Repo quasi solo documentale; non verificato un gioco installabile dal README.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Definire vertical slice giocabile offline, core loop e obiettivo di sessione prima di backlog aggiuntivo | **91** | **66** | — | Non dichiarare render/gameplay già implementati |
| MIGLIORIA | Sistema save/load idempotente con replay/crash recovery e test deterministici | **82** | **77** | — | Da iniziare quando esiste core di gioco |
| RIUSO | Valutare Interactive Scene Core per gesture e rendering solo dopo benchmark consumer | **65** | **54** | CAP-0024 | Niente motore 3D/AI superfluo |

## Interview Prep Coach PWA
Source: [desktop-tutorial@02c814d0c4fbb0b1c6e907e15f2d22a2519e4bc7](https://github.com/riccardopinato/desktop-tutorial/tree/02c814d0c4fbb0b1c6e907e15f2d22a2519e4bc7) · [README.md](https://github.com/riccardopinato/desktop-tutorial/blob/02c814d0c4fbb0b1c6e907e15f2d22a2519e4bc7/README.md).
**Stato verificato documentalmente:** Demo PWA HTML mobile-first con flashcard; non è app Flutter Android certificata.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Percorso test end-to-end PWA: avvio, sessione, salvataggio progresso, reset cache e offline | **92** | **87** | CAP-0068 | Verificare build corrente e stato localStorage |
| RIUSO | Flashcard con spaced repetition e spiegazioni per ruoli tech da Anki, senza import codice GPL | **82** | **86** | CAP-0112 | La flashcard semplice è già inclusa: aggiungere solo scheduling |
| MIGLIORIA | Simulazione colloquio e feedback rubricato, deterministico, con export locale | **79** | **81** | — | Nessuna LLM necessaria per MVP |

## FocuSense
Source: [FocuSense@99cce9e78963238854e3bbf4fb9c3f6e5e79d6ed](https://github.com/riccardopinato/FocuSense/tree/99cce9e78963238854e3bbf4fb9c3f6e5e79d6ed) · [ROADMAP.md](https://github.com/riccardopinato/FocuSense/blob/99cce9e78963238854e3bbf4fb9c3f6e5e79d6ed/ROADMAP.md).
**Stato verificato documentalmente:** Android focus utility RC1 con Environment Score/Focus Integrity; roadmap registra CI, firma e physical QA non conclusi.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Sensori reali e falsi positivi pickup/schermo spento, microfono FGS, burn-in AMOLED e batteria | **99** | **68** | CAP-0068 | E4 su OEM prima di estendere monitoraggio |
| GATE | Chiudere CI esatta, APK firmato, AdMob/UMP e purchase restore Pro su sandbox | **96** | **71** | CAP-0068 | Roadmap RC1 segnala gate esterni aperti |
| RIUSO | Statistiche attività locali e AFK volontario da ActivityWatch, senza audio/video registrati | **82** | **67** | CAP-0176 | Consent-first e batterie, non app stalking |
| MIGLIORIA | Ricompense Focus Core collegate a progressi verificabili, opzionali e non invasive | **61** | **88** | CAP-0183 | Game layer già presente: solo piccoli miglioramenti |

## FrameLab (repo parallelo)
Source: [FrameLab-Google-AI-Studio@1ff96408d54153dc6504312650112e47ced19354](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/tree/1ff96408d54153dc6504312650112e47ced19354) · [ROADMAP.md](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/blob/1ff96408d54153dc6504312650112e47ced19354/ROADMAP.md).
**Stato verificato documentalmente:** Secondo repository FrameLab con roadmap molto simile al repo app-fotografia; non assumere due app indipendenti.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Diff di sorgenti, dipendenze, contenuti e build SHA tra i due FrameLab; scegliere source of truth | **97** | **91** | CAP-0068 | Evitare due cicli di release divergenti |
| MIGLIORIA | Definire modalità mirror/donor read-only e una sola pipeline editoriale certificante | **90** | **86** | CAP-0042 | Le migliorie nuove vanno al repo canonico scelto |
| RICERCA | Raccogliere da repo secondario solo componenti non già presenti, con provenance e license gate | **72** | **79** | CAP-0023 | Nessun merge automatico al buio |

## In Cucina con gli Anime / Cooking Anime
Source: [In-Cucina-con-gli-Anime@fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465](https://github.com/riccardopinato/In-Cucina-con-gli-Anime/tree/fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465) · [README.md](https://github.com/riccardopinato/In-Cucina-con-gli-Anime/blob/fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465/README.md).
**Stato verificato documentalmente:** Flutter 0.9: 20 ricette illustrate revisionate nel runtime; attività R1 e catalogo draft più ampi non tutti pubblicati.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Riconciliare 20 ricette runtime con lotti draft (fino a 112) e review culinaria/traduzioni | **99** | **67** | CAP-0042 | Non certificare contenuti draft per presenza in PR |
| GATE | Diritti dei riferimenti anime, originalità illustrazioni, sicurezza alimentare e pubblicazione asset | **97** | **75** | CAP-0082 | Licenza e contenuto distinti dalla build |
| MIGLIORIA | Checklist ricetta passo-passo, porzioni, unità e ingredienti con fallback offline | **84** | **85** | CAP-0155 | Solo contenuti catalogati e verificati, non ricette inventate |
| GATE | AdMob, consenso, Billing e release Google Play su account reale | **93** | **67** | CAP-0068 | F4A privacy non include SDK/entitlement automaticamente |

## Neon Arcade Runner
Source: [Neon-arcade-runner@53cfae4b6cca45ce0e3b9d5c74a483a16329f374](https://github.com/riccardopinato/Neon-arcade-runner/tree/53cfae4b6cca45ce0e3b9d5c74a483a16329f374) · [ROADMAP.md](https://github.com/riccardopinato/Neon-arcade-runner/blob/53cfae4b6cca45ce0e3b9d5c74a483a16329f374/ROADMAP.md).
**Stato verificato documentalmente:** React/TypeScript Canvas mobile game con daily content e monetizzazione policy; Android store wiring da completare.

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Integrazione reale ads/IAP Android e prova no-ads lifetime senza doppie entitlement | **97** | **63** | CAP-0068 | Separazione mock/provider già prevista |
| GATE | FPS, touch hitbox, suoni, Back/exit e safe area su Android reale a 60Hz/120Hz | **96** | **72** | CAP-0024 | La correzione fullscreen è già implementata: testare, non rifarla |
| MIGLIORIA | Recovery partita sospesa Premium e migrazione progressi dopo update | **86** | **76** | — | Modalità Premium parziale esistente, validare persistence |
| NUOVA | Eventi e sfide settimanali locali da missioni esistenti con no FOMO/paywall aggressivo | **74** | **85** | — | Valore retention ma non blocca release |

