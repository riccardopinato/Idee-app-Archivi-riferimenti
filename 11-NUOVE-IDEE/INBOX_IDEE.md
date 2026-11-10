# Inbox nuove idee — da valutare e conservare

## AL-ANDROID-2026-001 — Adaptive Landscape, wallpaper Android adattivo (10/11/2026)

**APP ATTIVA / SOURCE_MERGED v0.3.2** nel [repo dedicato](https://github.com/riccardopinato/Adaptive-Landscape-Android) a `main@6e434c0a`; [PR #3](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/3) CI Flutter analyze/19 tests/Kotlin Android + APK ottimizzato/Web e GitHub Pages main [#42813678089](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42813678089) PASS. **Beach v0.3** corretta in [PR #7](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/7), Pages [#42822909836 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42822909836); **v0.3.1** speed fix [PR #8](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/8) merge su `main@72de4ff0`, deploy main [run #42825324425 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42825324425). [Beach v0.3.2 PR #9](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/9) GPU per-pixel, mare vuoto e dock manuale: [CI PR PASS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42847066074), main Pages in verifica. **Web visuale, Device/OEM, Play signing e Store ancora NON VERIFICATI**. Fonte [Deskland GPL-3.0](https://github.com/BLEZZ0102/Deskland) bloccata al commit `9818b577402ff476e1b59da07970c56472713126`: solo **reference E1**, nessun Donor E3 certificato, nessuna copia codice/asset. Flutter UI + WallpaperService Kotlin; griglia di calibrazione manuale perché Android non fornisce coordinate universali delle icone. Vendita standalone ipotizzata **€1,99–€2,99**, niente abbonamenti o ads. [Scheda tecnica, licenze, Golden e cinque maxi-step](ADAPTIVE_LANDSCAPE_ANDROID_2026-11-10.md).


## Template Notion — catalogazione per tutte le app (09/11/2026)

Nuovo [protocollo multi-app](../17-RICERCA-TEMPLATE-UX/ROUTING_MULTI_APP.md) per la sezione `docs/TEMPLATE_NOTION` in ogni app, alimentata da un [registro unico di 11 fonti](../17-RICERCA-TEMPLATE-UX/TEMPLATE_ROUTING_REGISTRY.json) ricavate da 12 ZIP (Design Brief duplicato). Nessuna CAP/Golden, integrazione Flutter, store o acquisto automatico; l'[idea template premium originale](../17-RICERCA-TEMPLATE-UX/IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md) resta backlog.


## TPL-STORE-2026-01 — Store interno di template originali (IDEA VALIDA, 09/11/2026)

**Decisione dell'utente:** conservare come **idea valida** lo store di template acquistabili separatamente all'interno di Notes e Anna's Diary; **€3,99 per template** è un'ipotesi di prezzo, non un prezzo approvato/attivato. La [scheda tecnica e commerciale](../17-RICERCA-TEMPLATE-UX/IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md) definisce catalogo, anteprime, acquisti una tantum, diritti, ripristino, compatibilità e gate. **Non autorizza** oggi sviluppo, nuove API/cloud, billing o release.

**Progettazione quattro pack originali (09/11):** [blueprint Notes/Anna](../17-RICERCA-TEMPLATE-UX/BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md), con due ipotesi Notes (Project Launch Studio e Study Sprint Studio) e due Anna (Atlante dei ricordi e Dodici settimane che contano). **DESIGN CANDIDATE / nessuna approvazione dello sviluppo premium**: non sono SKU, prodotti acquistabili, contenuti già realizzati o entitlement. \n\nLa vendita deve riguardare **template originali per le app**. Gli ZIP Notion di terzi sono fonti di ricerca, **non merce rivendibile**. Second Brain, Book Tracker e quattro altri export hanno [schede E2 o incompleto](../17-RICERCA-TEMPLATE-UX/README.md) con assegnazione primaria specifica.


## Ricerca template UX (09/11/2026) — TPLUX-001…008

Otto candidati di miglioramento, NON nuove app e NON nuove CAP, deduplicabili nella [scheda di riuso](../17-RICERCA-TEMPLATE-UX/CANDIDATI_RIUSO.md). Area di ricerca: template guidati, vision board sui canvas esistenti, home modulare, goal/review, mini-planner Noi, Second Brain read-only, Study Web e giornata realistica. [Matrice sorgente per Notes e Anna](../17-RICERCA-TEMPLATE-UX/CROSSWALK_NOTES_ANNA_2026-11-09.md). **PROPOSTA**: nessuna modifica a Product Bible, runtime, roadmap delle app o CAP registry; dati privati delle ricevute esclusi.


## Algoritmi ML leggeri, zero API e on-device — 04/11/2026

[Catalogo decisionale di 23 tecniche, 10 candidature nuove e mappa verso CAP/Golden](./CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md). Fonte: Machine Learning.txt dell'utente. ID stabili ML26-001…023. Nessun modello o codice integrato. Le 10 idee sono ora ammesse come CAP proposte, senza mutare le app.
**Aggiornamento di ammissione 04/11:** le dieci candidature ML26-001/002/004/008/009/013/015/016/018/019 sono state registrate rispettivamente come CAP-0152/0160/0151/0153/0154/0155/0159/0156/0157/0158, tutte PROPOSTA/E0. Le altre 13 restano riferite a CAP gia esistenti. [Audit Golden completo](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md).


## Notes-Ecosistema — audit 4 fonti e delta implementativi (04/11/2026)

Origine: audit condiviso dall'utente su **AI Valley, Hugging Face, GitHub/JSON Canvas e GitLab**. Le proposte **NOTES-AUD4-001…009** sono state ricondotte alle CAP canoniche esistenti quando pertinente; Smart Inbox action flow, JSON Canvas e Daily Note Hub non vanno assimilati a CAP solo simili. [Crosswalk con evidenze GitHub e roadmap ancora aperta](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_QUATTRO_FONTI_NOTES_2026-11-04.md).

**Stato:** audit/intake e delta di funzioni parziali; nessuna nuova app. Non promuove il registro CAP né cambia gli stati generati. Priorità operative: Smart Inbox #46, Project blockers #51, quindi Study #47, Duplicate Review #48 e JSON Canvas #49.

## Anna's Diary — 15 proposte NotebookLM (02/11/2026)

**Analizzate e mappate su 7 nuove CAP + 5 estensioni, non approvate in roadmap.** [Classifica e valutazioni](ANNA_NOTEBOOKLM_2026-11-02.md); [correzione CAP](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_ANNA_NOTEBOOKLM_2026-11-02.md); [offerta commerciale](../08-MONETIZZAZIONE/ANNA_DIARY_FREEMIUM_IPOTESI_2026-11-02.md). P1: domanda Noi, lettera futura, capsula, widget Oggi. Privacy #215 congelata.


| Nome | Categoria | Stato | Prossimo controllo |
|---|---|---|---|
| PDF Pocket Tools | utility | candidato con donor `PDF-Unifier` in codice | valutare estensione commerciale e licenze PDF, non partire da zero |
| EdgeDock / SideHub | Android launcher/overlay | candidato | permessi, policy |
| CmdPocket / TLDR Offline | developer | candidato | attribuzione dataset |
| Android QA Cockpit | desktop/B2B | candidato | rapporto con AppLab |
| DevBridge | dev/native | donor/candidato | GPL, Shizuku |
| Palette Lens | fotografia | feature FrameLab prima | algoritmo clean-room |
| ComicShelf | reader | backlog | licenza e mercato |

| Home Assets Passport | Suite consumer | NUOVA IPOTESI NON APPROVATA | BoxFinder + Purchase Guard + manuali/garanzie; verificare differenziazione |
| ShootWindow | foto / meteo / luce | NUOVA IPOTESI NON APPROVATA | prima funzione FrameLab, poi validare standalone |
| Pocket POI Offline | offline / geodata | NUOVA IPOTESI NON APPROVATA | licenze, qualità e freschezza POI, non clonare CamperBoss |
| DriveDay | auto / dati pubblici | NUOVA IPOTESI NON APPROVATA | combinare Parking Buddy, Fuel, Trip Cost, Vehicle Check |
| Trip Ready | travel checklist | NUOVA IPOTESI NON APPROVATA | testare prima in Wonderlog/CamperBoss/TrailPath |
| FileFlow Kit | file / privacy / transfer | NUOVA IPOTESI NON APPROVATA | non duplicare Send to PC, Foto→Chiavetta, SafeShare |
| Local Data Health Cockpit | B2B / AppLab | NUOVA IPOTESI NON APPROVATA | verificare adapter e copertura provider |

Prima di assegnare nuovi ID controllare i [cataloghi esistenti](../01-PORTAFOGLIO/CATALOGO_APP.md). Per una scheda dettagliata usare il [modello app](../10-MODELLI/SCHEDA_APP.md). Le proposte restano qui anche dopo promozione o rinvio, con stato e link aggiornati.

## Nuove candidate da r/BestGitHubRepos — 01/11/2026 (non promosse)

| Nome | Tipo | Decisione | Collegamento / prossimo gate |
|---|---|---|---|
| **DevPocket Tools** | mini suite web/Android | **NUOVA IDEA da valutare**, distinta da CmdPocket | CAP-0084; testare conversioni locali JSON/Base64/QR e differenza rispetto a WEB-001…016, licenza GPL reference-only |
| **DiskScope** | storage visualizer standalone | **FEATURE-FIRST / RINVIATA** | CAP-0083: introdurre treemap in Android Omni Cleaner prima di validare nuova app a pagamento |
| **GeoPulse Live** | esploratore di layer pubblici | **IPOTESI NON APPROVATA / RINVIATA** | CAP-0087; provider/ToS/meteo/earthquake; no allerta di sicurezza o navigazione operativa |
| **DeskPilot** | Android desktop workspace | **BASSA PRIORITA / BLOCCO OEM** | CAP-0088, Dextop GPL e HyperOS non supportato; non sovrapporre a EdgeDock/App Profiles |

Le idee restano in 11; i singoli comportamenti sono in 12 con ID CAP. Nessuna apertura app repo o promozione al portafoglio senza approvazione distinta.

## Hugging Face «to do» — 12 proposte funzionali, 01/11/2026 (NON nuove app)

Tutte **PROPOSTA**; destinazione principale Notes-Ecosistema, subset essenziale Anna's Diary. Scheda completa con punteggi, fonti, licensing e gate: [RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md).

| # | Idea conservata | Stato |
| --- | --- | --- |
| 1 | **01 Smart Task Capture** — CAP-0092 | PROPOSTA / non in roadmap |
| 2 | **02 Note → Checklist** — CAP-0093 | PROPOSTA / non in roadmap |
| 3 | **03 Sticky Kanban** — CAP-0094 | PROPOSTA / non in roadmap |
| 4 | **04 Voice → Actions** — CAP-0031/0092/0095 | PROPOSTA / non in roadmap |
| 5 | **05 Meeting Intelligence** — CAP-0095 | PROPOSTA / non in roadmap |
| 6 | **06 Task collegate/ricorrenti** — CAP-0096 | PROPOSTA / non in roadmap |
| 7 | **07 Project Memory** — CAP-0097 | PROPOSTA / non in roadmap |
| 8 | **08 Mind Map** — CAP-0098 | PROPOSTA / non in roadmap |
| 9 | **09 Planner studio** — CAP-0099 | PROPOSTA / non in roadmap |
| 10 | **10 Kanban collaborativa** — CAP-0100 | PROPOSTA / non in roadmap |
| 11 | **11 Productivity Dashboard** — CAP-0101 | PROPOSTA / non in roadmap |
| 12 | **12 Task Recovery** — CAP-0017/0018/0075 | PROPOSTA / non in roadmap |

Nessun progetto standalone o migrazione AI approvato; i CAP nuovi sono CAP-0092…CAP-0101. I CAP esistenti restano canonici per backup, lifecycle, voce e ricerca.

## Hugging Face «to do» — seconda ricerca, idee 13–28, 01/11/2026

Tutte **PROPOSTA** (funzioni, non nuove app). Approfondimento con punteggi, fonti dirette/distinte da inferenze, licenze e gate: [Seconda ricerca Hugging Face «to do»](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md).

| # | Idea | CAP collegati | Stato |
| --- | --- | --- | --- |
| 13 | **Smart Rescheduler** | CAP-0102, CAP-0001 | PROPOSTA — non in roadmap |
| 14 | **Dependency Map** | CAP-0103, CAP-0096, CAP-0028 | PROPOSTA — non in roadmap |
| 15 | **Goal Timeline** | CAP-0104, CAP-0099 | PROPOSTA — non in roadmap |
| 16 | **Smart Priority Engine** | CAP-0105 | PROPOSTA — non in roadmap |
| 17 | **Workload Guard** | CAP-0106, CAP-0001 | PROPOSTA — non in roadmap |
| 18 | **Project Blueprint Import** | CAP-0107, CAP-0093, CAP-0075 | PROPOSTA — non in roadmap |
| 19 | **Backward Planning** | CAP-0104, CAP-0001 | PROPOSTA — non in roadmap |
| 20 | **Task Time Accuracy** | CAP-0108, CAP-0101 | PROPOSTA — non in roadmap |
| 21 | **Focus Notes** | CAP-0109 | PROPOSTA — non in roadmap |
| 22 | **Eisenhower Visual Board** | CAP-0105, CAP-0094 | PROPOSTA — non in roadmap |
| 23 | **Quick Start Mode** | CAP-0110, CAP-0109 | PROPOSTA — non in roadmap |
| 24 | **Weekly Review** | CAP-0111, CAP-0101 | PROPOSTA — non in roadmap |
| 25 | **Learning Recall** | CAP-0112, CAP-0099 | PROPOSTA — non in roadmap |
| 26 | **Alternative Plans** | CAP-0102, CAP-0001 | PROPOSTA — non in roadmap |
| 27 | **Focus Protection** | CAP-0109, CAP-0077 | PROPOSTA — non in roadmap |
| 28 | **Meeting Load Heatmap** | CAP-0106, CAP-0101 | PROPOSTA — non in roadmap |

Le 16 idee si traducono in 11 nuovi CAP (CAP-0102…CAP-0112) e collegamenti a CAP preesistenti, evitando doppioni. La ricerca originale 1–12 resta nel documento precedente.

## Hugging Face Notes — terza e quarta ricerca: idee #29–56, 01/11/2026

**28 proposte funzionali archiviate, nessuna nuova app approvata.** Schede dettagliate: [idee #29–44](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md) e [idee #45–56](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md); originali #1–28 preservate.

| # | Idea conservata | Stima editoriale | Capability | Stato |
| --- | --- | --- | --- | --- |
| 29 | Privacy Shield | 9,9/10 | [CAP-0114](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0114.md) | PROPOSTA / non in roadmap |
| 30 | Contradiction Finder | 9,8/10 | [CAP-0115](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0115.md) | PROPOSTA / non in roadmap |
| 31 | Duplicate Notes Cleaner | 9,7/10 | [CAP-0116](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0116.md) | PROPOSTA / non in roadmap |
| 32 | Sketch-to-Diagram | 9,7/10 | [CAP-0117](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0117.md) | PROPOSTA / non in roadmap |
| 33 | Document Delta | 9,6/10 | [CAP-0118](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0118.md) | PROPOSTA / non in roadmap |
| 34 | Citation Integrity Checker | 9,5/10 | [CAP-0119](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0119.md) | PROPOSTA / non in roadmap |
| 35 | Accessible Image Notes | 9,4/10 | [CAP-0120](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0120.md) | PROPOSTA / non in roadmap |
| 36 | Easy Reading Mode | 9,4/10 | [CAP-0121](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0121.md) | PROPOSTA / non in roadmap |
| 37 | Table Capture | 9,3/10 | [CAP-0122](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0122.md) | PROPOSTA / non in roadmap |
| 38 | Bilingual Notes Reader | 9,2/10 | [CAP-0123](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0123.md) | PROPOSTA / non in roadmap |
| 39 | Topic Discovery | 9,2/10 | [CAP-0124](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0124.md) | PROPOSTA / non in roadmap |
| 40 | Chart-to-Data | 9,1/10 | [CAP-0125](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0125.md) | PROPOSTA / non in roadmap |
| 41 | Living Glossary | 9,0/10 | [CAP-0126](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0126.md) | PROPOSTA / non in roadmap |
| 42 | Video Chapter Notes | 9,0/10 | [CAP-0127](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0127.md) | PROPOSTA / non in roadmap |
| 43 | Form-to-Card | 8,9/10 | [CAP-0128](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0128.md) | PROPOSTA / non in roadmap |
| 44 | Knowledge Freshness | 8,9/10 | [CAP-0129](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0129.md) | PROPOSTA / non in roadmap |
| 45 | Notes to Slides | 9,8/10 | [CAP-0130](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0130.md) | PROPOSTA / non in roadmap |
| 46 | Math Ink | 9,7/10 | [CAP-0131](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0131.md) | PROPOSTA / non in roadmap |
| 47 | Soundscape Journal | 9,6/10 | [CAP-0132](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0132.md) | PROPOSTA / non in roadmap |
| 48 | Smart Reading Flow | 9,6/10 | [CAP-0133](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0133.md) | PROPOSTA / non in roadmap |
| 49 | Document Auto-Sorter | 9,5/10 | [CAP-0134](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0134.md) | PROPOSTA / non in roadmap |
| 50 | Evidence Board | 9,5/10 | [CAP-0135](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0135.md) | PROPOSTA / non in roadmap |
| 51 | Smart Cutout Canvas | 9,4/10 | [CAP-0136](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0136.md) | PROPOSTA / non in roadmap |
| 52 | 3D Memory Objects | 9,3/10 | [CAP-0137](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0137.md) | PROPOSTA / non in roadmap |
| 53 | Audio-Linked Ink | 9,3/10 | [CAP-0138](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0138.md) | PROPOSTA / non in roadmap |
| 54 | Motion Study Notes | 9,2/10 | [CAP-0139](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0139.md) | PROPOSTA / non in roadmap |
| 55 | Scientific Figure Studio | 9,1/10 | [CAP-0130](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0130.md) | PROPOSTA / non in roadmap |
| 56 | Image Authenticity Inspector | 9,0/10 | [CAP-0140](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0140.md) | PROPOSTA / non in roadmap |

Il caso #55 e #45 condivide una sola capability; nessuna delle due idee e stata scartata. Link, licensing, demo offline e impatto APK sono documentati nelle schede di ricerca.

## Importazione IA 02/11/2026 — idee in analisi (non promosse)

| Lotto | Natura | Stato | Schede e ranking | Prossimo gate |
|---|---|---|---|---|
| IA26-001…IA26-100 | 100 idee originali #1–#100; nessun ID app nuovo | ANALISI / NON APPROVATE | [Indice 100](IA-2026-11-02/INDICE_100_SCHEDE.md) · [ranking](IA-2026-11-02/RANKING_100_COMPLETO.md) | concorrenza, review codice, licenze, policy |
| IA26-E01…E06 | 6 idee non numerate, conservate separatamente | ANALISI / NON APPROVATE | [Indice extra](IA-2026-11-02/INDICE_IDEE_EXTRA_NON_NUMERATE.md) | prototipi tecnici, target, domanda |
| 14 fusioni della fonte | valutazione combinazioni, nessun prodotto fuso approvato | ANALISI | [Fusioni e reuse](IA-2026-11-02/FUSIONI_E_RIUSO.md) | gate di coerenza prodotto e donor |

## Secondo lotto ML10 on-device — 04/11/2026

Fonte: messaggio utente 04/11 con elenchi ripetuti. Dieci famiglie distinte: Isolation Forest/LOF, MinHash+LSH, agglomerative clustering, HMM, PCA/TruncatedSVD, Naive Bayes, kNN, logistic regression, visione/audio LiteRT/Core ML, exponential smoothing/Holt-Winters. Tutte mappate a CAP esistenti, senza nuova app o duplicazione CAP. [Audit approfondito e scelte](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md). Due reference engine puri integrati da [Core PR #71](https://github.com/riccardopinato/App-Factory-Core/pull/71), [CI main SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497699); zero modifiche ai prodotti. Certificazione donor consumer / Golden ancora da dimostrare ([gate #72](https://github.com/riccardopinato/App-Factory-Core/issues/72)).

## ML10 — esecuzione P1/P2/P3 e revisione generale (04/11/2026)

I motori puramente matematici ora esistono come reference implementation in [Core #71](https://github.com/riccardopinato/App-Factory-Core/pull/71) e [Core #73](https://github.com/riccardopinato/App-Factory-Core/pull/73), con CI Dart/Factory verde; **non** significa modelli ML addestrati né motori certificati sul dispositivo. Il classificatore Vision/Audio resta bloccato per mancanza di checkpoint/licenze/benchmark. [Audit completo 160 CAP / 385 associazioni](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_COMPLETO_ML10_2026-11-04.md) ricalcola le priorità e la facilità per app soltanto dove nuove prove giustificano la modifica; nessuna nuova CAP duplicata.

## ML10 consumer delta verificato — 04/11/2026

App Factory Core resta source of truth delle Golden Rules; Ideas mantiene il registro a 160 CAP e le 385 associazioni. [Notes #57](https://github.com/riccardopinato/Notes-Ecosistema/pull/57) è un consumer MinHash/LSH read-only, non merge reversibile; [TasteAI #2](https://github.com/riccardopinato/TasteAI/pull/2) un consumer P2 kNN ricette correlate, non prova di migliori risultati anti-spreco. [Registro con delta app e sorgenti](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_CONSUMER_POSTMERGE_2026-11-04.md), [screening modelli P3](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_MODEL_SCREENING_2026-11-04.md). Nessuna nuova CAP, nessuna promozione Golden/Store.
