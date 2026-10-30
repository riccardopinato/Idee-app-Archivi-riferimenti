# Audit trasversale App utility — opportunità, gap e idee (30 ottobre 2026)

## 0. Mandato, autorità, copertura e limiti

**Decisione cercata:** quali aggiunte apportano più valore ai prodotti esistenti e quali nuove idee meritano una scheda/validazione commerciale; evitare funzionalità duplicate e suite immaginarie.

**Source of truth:** App-Factory-Core [CURRENT](https://github.com/riccardopinato/App-Factory-Core/blob/main/CURRENT.yaml) — Master v27, Golden Index v23 @ `e9507056601c4a6751510da4c5d1f61601a5dc25`; Product Bible/roadmap dei singoli repo, codice e prove per lo stato implementato. AppLab v6.3 per QA. Questo archivio è conoscenza di portafoglio e non sovrascrive quelle fonti.

**Materiale considerato:** documenti del Project (Backlog idee app, Idee che mi vengono in mente per le app, Classifica idee app, Analisi stelle GitHub, Anna's Diary e Checkpoint, informazioni Battery Guard, ripresa Anna), registro master, portfolio Web Utility allegato DOCX/PDF (16 idee), archivio GitHub, catalogo 632 stelle e deep dive OSS, Design-App, repository principali e informazioni chat recuperabili. Il file `SKM_C301i26103009270.pdf` è una versione scannerizzata di 8 pagine del portfolio Web Utility e **non** va contato come nuova fonte autonoma di idee.

**Limite:** ricognizione completa delle **fonti di idee accessibili**, NON code review/test fisici di tutte le app, ogni chat privata pregressa, né lettura del codice delle 632 stelle. Identificare una funzionalità in roadmap non equivale a eseguirla; un repo non individuato non dimostra che non sia stato sviluppato. Le date e gli SHA sono snapshot.

**Qualità della prova:** `A` = funzione/limite esplicito in roadmap o codice repo; `B` = decisione precedente in file/chat del Project non ancora riconciliata con repo; `C` = proposta nuova di questo audit, non approvata. **Score 0–100 = giudizio di priorità opportunità**, non stima fatturato.

## 1. Correzioni anti-duplicazione: idee già trasformate in codice

| Area | Idea presente nei file/chat | Verifica attuale | Implicazione |
|---|---|---|---|
| Anna | Shopping List privata/Noi ♡ | **A: completata v0.71**, screen e test `v071_shopping_list_test.dart` | NON ricostruire |
| Anna | Scheda palestra / allenamento | **A: multisport v0.72**, modelli/storia e test | valutare solo import foto/PDF originale |
| Anna | Calendario esterno | **A: overlay Android read-only v0.73**, servizio/test | fase successiva è export esplicito, non nuovo overlay |
| Anna | Universal Delete, Trash e account erasure | **A: lifecycle v0.48 + regression v0.74**, `docs/LIFECYCLE_AUDIT.md` | audit di REGRESSIONE, non nuova piattaforma Delete |
| Anna | Memories Map e Then & Now | **A: v1.05-B1 PR #128 merged** | focus UX/prove, non reimplementare |
| Anna | Year in Review 2.0 | **A: v1.05-B2 PR #129 merged** | misurare UX ed export |
| Anna | Collections / Life Threads | **A: v1.05-B3 PR #130 merged** | migliorare presentation/efficienza |
| Notes | Trash, purge, allegati, shared lifecycle | **A: `flutter_app/LIFECYCLE_0_32.md`**, policy e test documentati | test cross-feature e restore, non clone Delete Engine |
| Notes | Canvas/sfondo sketch + note, AI locale Needle | **A: roadmap/main 0.56.3**, Needle model pack on-demand | fisico/latency/memory, niente doppio modello |
| TasteAI | Ricette da ingredienti / Anti-Waste | **A: v0.13**, 111 ricette e motore grounded | evitare una MealMate identica prima di misurare domanda |
| Notification Control | Undo/Pausa/FollowUp/Critical/Pickup/Luminous | **A: suite in codice Step 27F** | non presentare moduli come idee non sviluppate |
| Phone Guard | Tabletop + Pocket + Bag/Journey/Charging/Accessory | **A: v0.9.7, sei protezioni** | i donor Pockara/Tabletop restano acquistabili a parte |
| Omni Cleaner | pulizia file/download/galleria/EXIF | **A: v1.0.0 RC1** | non duplicare questi motori in SafeShare/Downloads |
| PDF-Unifier | merge/split/lock/rotate/OCR/PDF reader | **A: Kotlin in codice** | PDF Pocket Tools è nuovo packaging/ampliamento |
| World Days | dataset, localizzazione, reminder, widget, Ads | **A: 296 titoli verified overview e 28 rich editorial** | gap principalmente profondità editoriale e release |
| Design-App | libreria Flutter Motion, Icon, Semantic Sound | **A: Motion Flutter COPY_READY library-level; icons Flutter COPY_READY; Sound LIBRARY_VERIFIED** | riuso mirato nelle app, NON Golden cross-app automaticamente |

Fonti principali: [Anna ROADMAP](https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md), [Anna lifecycle](https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/LIFECYCLE_AUDIT.md), [Notes lifecycle](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/flutter_app/LIFECYCLE_0_32.md), [World Days ROADMAP](https://github.com/riccardopinato/World-Days/blob/main/ROADMAP.md), [Design-App pack roadmap](https://github.com/riccardopinato/Design-App/blob/main/packs/ROADMAP_COPY_READY.md).

## 2. Funzioni da apportare o consolidare: matrice prioritaria

Punteggi sono valutazioni **relative** di beneficio commerciale, riuso, urgenza e costo/rischio; non sono misurazioni clienti. Stati: `GATE` = dimostrare funzionamento reale; `GAP` = capacità parziale; `APPROVATO_STORICO` = accettato nel Project ma non provato in roadmap corrente; `IPOTESI` = nuova proposta da sottoporre al Product Bible.

| # | App | Proposta / intervento | Tipo / prova | Score | Perché / condizione |
|---:|---|---|---|---:|---|
| 1 | Anna's Diary | UI5 DF-01–DF-35, visual regression ed exact-head merge | GATE A | **96** | PR #154 aperta: non duplicare feature/UI |
| 2 | TrailPath | unificare v1.5/Smart Trace/Pro dal feature branch e testare routing/gestures fisici | GATE A | **96** | main v0.9.15, PR #27 aperta; prima correttezza |
| 3 | Wonderlog + Core | riconciliare Bridge CERTIFIED dichiarato vs Golden Candidate e test roundtrip | GATE A | **94** | conflitto di autorità da non perpetuare |
| 4 | CamperBoss | catalogo POI/offline provider, licenze e vera navigazione offline | GAP A | **93** | Step 16 bloccato: non promettere POI produzione |
| 5 | Battery Guard | exact-artifact device test: update in-place, avvisi e protezione hardware truth | GATE A | **92** | codice 1.8.1 pronto, rilascio esterno aperto |
| 6 | Notification Control | accessibilità notifiche + battery/perf + Play Internal + billing | GATE A | **91** | suite implementata; evitare feature proliferation |
| 7 | Phone Guard | multi-OEM false positives e lifecycle background su tutte le modalità | GATE A | **91** | promessa anti-manomissione dipende dal dispositivo |
| 8 | World Days | 50 nuovi Rich Editorial validati; prioritizzare i 268 senza approfondimento | GAP A | **90** | 296/296 overview, solo 28/296 rich |
| 9 | Cooking Anime | scalare 20 ricette approvate con audit culinario/artwork, poi F4B Play | GAP A | **90** | 122 candidate in review ≠ ricette pubblicabili |
| 10 | Notes-Ecosistema | AI Needle 3 on-device quality/performance e Plus entitlement | GATE A | **90** | pack 35,3 MB separato, Play/device pending |
| 11 | Send to PC | guida di pairing TLS self-signed/fingerprint e test browser/rete reali | GAP A | **88** | first-connect friction, nessun cloud |
| 12 | Notes | Universal Delete regression su nuovi sidecar/sync/backup | GATE A/B | **88** | ciclo base già implementato in 0.32 |
| 13 | Anna | accesso al calendario esterno: «Aggiungi anche al calendario» esplicito | APPROVATO_STORICO B | **85** | overlay v0.73 già presente; no two-way automatico |
| 14 | Notes | Professional Wallet (CV, attestati, QR/vCard) come vista su Documents | APPROVATO_STORICO B | **85** | evitare secondo vault e verificare Product Bible |
| 15 | Notes | External Calendar overlay read-only, poi write-through opt-in | APPROVATO_STORICO B | **84** | non rilevato come capability verificata in main; controllo scoped richiesto |
| 16 | FrameLab | 9C: catalogo editoriale, poi Golden Hour + Palette da foto | GAP/IPOTESI A/C | **84** | salvare foto/palette, non introdurre cloud inutilmente |
| 17 | PDF Pocket Tools / Notes | riuso dal PDF-Unifier per operazioni locali e OCR | IPOTESI con donor A | **84** | license/provenance, package e feature parity |
| 18 | Anna | import foto/PDF delle schede workout oltre a TXT/CSV | APPROVATO_STORICO B | **83** | requisito originale non interamente coperto |
| 19 | Omni Cleaner → SafeShare | Photo EXIF safe-copy come donor di un Clean Link/Metadata workflow | IPOTESI con donor A | **82** | riuso senza duplicare motore o permessi |
| 20 | World Days | validare 59 date mobili irrisolte nel discovery backlog | GAP A | **82** | originator & recurrence proof, non publish automatico |
| 21 | TasteAI | weekly meal plan + shopping list derivata da ricette, senza duplicare il catalogo | IPOTESI C | **81** | testare domanda; MealMate separata solo se posizionamento diverso |
| 22 | Wonderlog/TrailPath | journey/memory COPY/LINK manuale con provenienza e fallback locali | GAP/GATE A | **81** | non creare shared DB, import solo su scelta utente |
| 23 | GrillBoss | schede taglio/temperatura alimentare + weather window con dati verificati | IPOTESI C | **80** | food safety: non dare garanzie dal meteo |
| 24 | Web Utility WEB-012/008/014 | una sola location base e provider/market adapter per Sun/Meteo/AQI | RIUSO B | **80** | SEO-native, non Flutter Web primario |
| 25 | FocuSense | usare Design-App Motion/Sound in modo sottile e nessun annuncio durante focus | IPOTESI C | **77** | Best Conditions già presente; non duplicarlo |
| 26 | Human Zoom | verificare progressione didattica e version truth README 0.18 vs pubspec 0.32 | GATE A | **76** | evitare nuova tassonomia senza copertura corretta |
| 27 | App Profiles | estrarre solo rotation/brightness/screen awake in micro-app, poi suite | IPOTESI donor A | **76** | Android permessi/limitazioni app foreground |
| 28 | CleanOS | integrare donor Easy Debloat + audit privilegi Shizuku/ADB, safe restore | IPOTESI donor B | **75** | non confondere con Omni Cleaner |
| 29 | Battery/Trail/Notes (cross-app) | piccoli pack Design-App certificati, baseline visuali e a11y | RIUSO A | **75** | biblioteca COPY_READY non prova cross-app |
| 30 | AppLab | coverage-gap/routing source-bound, differentiating CI from actual physical proof | GATE A | **75** | no autonomic self-certification |

**Non integrare in automatico** nessuna proposta `IPOTESI` in un'app: deve essere accettata da Product Bible/roadmap, con gate e proprietario.

## 3. Fonti dati e librerie con elevato rendimento trasversale

| Fonte / donor | Target primario | Opportunità | Gate licenza/prodotto |
|---|---|---|---|
| OSM + Geofabrik | TrailPath, CamperBoss, Wonderlog, Web Utility | offline base geo/POI | ODbL, provisioning; NO tile.openstreetmap.org bulk |
| Overture Maps Places | CamperBoss, Wonderlog, Pocket POI Offline candidato | catalogo POI geografico in batch | Places licenze permissive; controllare singola fonte/tema |
| Wikidata/Wikimedia | World Days, travel, heritage | curiosità e immagini con origine | licenze asset individuali e autenticità contenuto |
| Open-Meteo | CamperBoss, TrailPath, GrillBoss, FrameLab, WEB-008/014 | weather windows e meteo contestuale | **Free API non commerciale**; app con pubblicità/abbonamento richiede piano commerciale o soluzione conforme; CC BY 4.0 |
| SunCalc | FrameLab, TrailPath, WEB-012 | golden hour, sunset return, phases | calcolo locale; distinguere luce teorica da previsione |
| MIMIT carburanti | WEB-002, WEB-009, CamperBoss/DriveDay | prezzi carburanti ufficiali Italia | frequenza, market e attribuzione |
| Valhalla / OSRM / GraphHopper | TrailPath, CamperBoss, WEB-009 | routing e matching | hosting/quote/accuratezza; non inventare percorsi |
| GTFS/GTFS-RT | WEB-010, eventuale viaggi | mezzi e avvisi | formato, feed per operatore, diritti distinti |
| Joplin | Notes | clipper, version history, import/export | reference only prima della verifica licenza |
| scrcpy + LeakCanary | AppLab/Android QA Cockpit | physical evidence, leak audit | license, integrazione e hosting |
| PDF-Unifier (interno) + PdfUnifier OSS | Notes, PDF Pocket Tools | engine PDF | priorità donor interno, licenza OSS per file |
| Colorwaver / Penpot | FrameLab / Notes | palette / canvas UX | reference e rewrite ove necessario |
| Wireless ADB Switch / UAD NG | Easy Debloat/CleanOS | pairing e cataloghi sicurezza | permessi, rootlessness non automatica, licenze |
| Design-App packs | tutte le app | Motion, sound, icons, visual QA | copy-ready library ≠ certified integration |

Fonte ufficiale Open-Meteo: https://open-meteo.com/en/terms e https://open-meteo.com/en/pricing . Fonte Overture: https://docs.overturemaps.org/guides/places/ . [Sorgenti Project catalogate](../04-FONTI-DATI/REGISTRO_FONTI_API.md).

## 4. Prodotti già esistenti nella storia ma non registrati nell'inbox come «nuove idee»

Non creare record duplicati per:
- **CasePhone / Cold DM**, mystery fake-phone episodico — concetto già nel registro master.
- **Court Manager Padel/Tennis**, B2B gestione campi — idea storica.
- **ReelForge / ClipForge**, editing video/AI — idea storica, costo API prima di aprire codice.
- **Focus Kingdom**, gamification focus — già registrata nel master, possibile relazione con FocuSense.
- **Anti-Truffa**, **Senior Safe Home**, **HomeFix**, **CuraVestiti**, **MealMate**, **BoxFinder**, **Phone Health Check**, **Parking Buddy**, **Bluetooth Guardian**, **Purchase Guard**, **Web Utility WEB-001…016** — idee/linee già note, non presentarle come nuove.
- Le **7 idee già in 11-NUOVE-IDEE** (PDF Pocket Tools, EdgeDock, CmdPocket, QA Cockpit, DevBridge, Palette Lens, ComicShelf) mantengono la loro identità.

## 5. Raccomandazione commerciale complessiva

**Prima colmare i gap di qualità/distribuzione delle app mature, poi riusare i donor, poi sperimentare nuove app.** Le nuove proposte sono catalogate separatamente e non alterano la classifica consolidata finché non vengono validate.

- **5 maxi-step:** (1) baseline e source truth PR/main di Anna/TrailPath/Wonderlog; (2) physical/Play acceptance di Battery, Notification, Phone, Send-to-PC; (3) editorial release train World Days/Cooking Anime; (4) source/provider licensing POI/meteo/routing per CamperBoss/TrailPath/Web; (5) due esperimenti commerciali a basso rischio fra PDF Core e un nuovo packaging Home Assets/ShootWindow, con schede prodotto.
- **Non progettare per trattenere artificialmente l'utente**: usare task completion e retention significativa, ad request solo in pause naturali.
- **Non confondere certificazione con disponibilità**: ogni prodotto mantiene `mainSha`, `featureBranchSha`, `artifactSha`, `physicalEvidence`, `billingStatus`, `storeStatus`.
