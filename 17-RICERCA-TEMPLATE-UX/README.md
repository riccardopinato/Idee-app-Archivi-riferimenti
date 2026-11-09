# Ricerca template UX — Notes-Ecosistema / Anna's Diary

Ricerca **pubblica** su pattern di template, Second Brain, planner, journal e dashboard. Scopo: selezionare idee riusabili senza importare contenuti privati o copiare asset. La matrice è ancorata ai sorgenti GitHub, non a descrizioni commerciali.

## Fonti analizzate
- **TPLUX-REF-0001** — [Second Brain (PARA Dashboard), Abdo Karamallah](SCHEDE/TPLUX-REF-0001-SECOND_BRAIN_PARA_ABDO.md): E1 su Marketplace e anteprima; pagina Notion originale non letta; E2 pending. Pattern: Quick Actions, Areas, Projects, Resources, Archive e Tasks. Nessun asset copiato.

## Cataloghi Template Notion per app

Questa cartella conserva il **riferimento pubblico master** (un record TPLUX-REF per fonte); ciascuna app conserva la propria **scheda di ammissione e utilizzo**. Non registrare duplicati come fonti distinte.

| Destinazione | Sezione proprietaria | Stato |
|---|---|---|
| **Notes-Ecosistema** | [Template Notion — Notes](https://github.com/riccardopinato/Notes-Ecosistema/tree/main/docs/TEMPLATE_NOTION) | Sei riferimenti di ricerca; UX Book Tracker approvata; Step3 [PR #96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96) **MERGED**, CI source PASS; device NOT VERIFIED |
| **Anna's Diary** | [Template Notion — Anna](https://github.com/riccardopinato/Agenda-per-Anna/tree/main/docs/TEMPLATE_NOTION) | Cinque riferimenti di ricerca; UX Rituali gentili approvata; Step3 [PR #290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290) **MERGED**, CI source PASS; device NOT VERIFIED |

| **Wonderlog** | [Template Notion — Wonderlog](https://github.com/riccardopinato/Wonderlog/tree/main/docs/TEMPLATE_NOTION) | UX Trip Planner approvata; Step3 [PR #26](https://github.com/riccardopinato/Wonderlog/pull/26) **MERGED**, CI source PASS; device NOT VERIFIED; non routing o prenotazioni |

**Routing nuovo template**: esaminare il Product Bible e scegliere la destinazione primaria prima di aggiungere una scheda. Il master TPLUX-REF conserva le prove della fonte; le schede locali individuano solo opportunità e gate pertinenti a quella app. I cataloghi privati delle ricevute rimangono fuori da GitHub.

## Nuovi export Notion analizzati — 09/11/2026

- **TPLUX-REF-0002** — [Routines Activities](SCHEDE/TPLUX-REF-0002-ROUTINES_ACTIVITIES.md). **Destinazione:** Anna's Diary. E2 export strutturale (1 MD/4 JPEG); routine statiche, non un habit tracker completo.
- **TPLUX-REF-0003** — [Weekly Planner](SCHEDE/TPLUX-REF-0003-WEEKLY_PLANNER.md). **Destinazione:** Anna's Diary, solo attesa. Export incompleto: 1 MD introduttivo/upsell, non il planner reale.
- **TPLUX-REF-0004** — [Book Tracker (Mindful Setups)](SCHEDE/TPLUX-REF-0004-BOOK_TRACKER.md). **Destinazione:** Notes-Ecosistema. E2 export (24 MD/14 CSV/23 immagini); licenza esplicita personal-use, resale vietata.
- **TPLUX-REF-0005** — [Subscription Tracker](SCHEDE/TPLUX-REF-0005-SUBSCRIPTION_TRACKER.md). **Destinazione:** CashMate, NON Notes/Anna. E2 export (10 MD/3 CSV/MP4); analytics dipendono da NotionStats esterno.
- **TPLUX-REF-0006** — [Weight Loss Tracker](SCHEDE/TPLUX-REF-0006-WEIGHT_LOSS_TRACKER.md). **Destinazione:** Anna solo valutazione privacy. E2 export (5 MD/2 CSV/GIF), dati sensibili; nessuna adozione di prodotto.

**Monetizzazione, idea valida (backlog):** [Store interno di template originali, prezzo candidato €3,99](IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md). Valida come concetto, **non approvata per implementazione o pubblicazione**. Non rivendere ZIP o asset di terzi.

## Routing multi-app (12 ZIP, 11 fonti uniche)

- [Audit degli export e assegnazione alle app](LOTTO_NOTION_2026_11_09_12_ZIP.md)
- [Routing e schema dei cataloghi locali](ROUTING_MULTI_APP.md)
- [Registro centrale JSON](TEMPLATE_ROUTING_REGISTRY.json)

I due ZIP Design Brief sono duplicati nei contenuti; fonti finanziarie e immobiliari senza app coerente restano non assegnate. Nessun template viene copiato o venduto.

## Maxi-step 2 — Template nativi in progettazione

[Piloti UX Notes / Anna / Wonderlog](UX_STEP2_PILOTI_2026_11_09.md): tre demo app-specifiche, UX **approvate il 09/11/2026**. Implementazioni Flutter in PR Step3 separate da CI/merge/QA; nessuno Store derivato dalle demo.

## Maxi-step 3 — Implementazione nativa

[Registro dei tre piloti, adapter e gate residui](UX_STEP3_IMPLEMENTAZIONE_2026_11_09.md) · Notes [#96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96), Anna [#290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290), Wonderlog [#26](https://github.com/riccardopinato/Wonderlog/pull/26). Tutte le PR Step3 integrate in `main` con check CI superati; stato runtime fisico ancora non verificato.

## Documenti
- [Crosswalk di opportunità e gap](CROSSWALK_NOTES_ANNA_2026-11-09.md) — stato verificato di repository vs proposte.
- [Protocollo delle fonti, varianti e privacy](PROTOCOLLO_FONTI_E_PRIVACY.md) — evidence ladder, regole di export e diritti.
- [Roadmap di cinque maxi-step](ROADMAP_5_MAXISTEP.md) — precondizioni, gate, owner e limiti.
- [Candidati di riuso](CANDIDATI_RIUSO.md) — estensioni a owner esistenti, non nuove CAP.

## Confini
- **Nessuna lista di acquisti, email, ID ordine, link di download, contenuti personali o ricevute** in questo repository pubblico. Un eventuale catalogo privato deve essere conservato separatamente.
- **Nessuna promessa di copertura della libreria commerciale**: le pagine pubbliche, i titoli e le anteprime non dimostrano le funzionalità delle varianti ricevute né i contenuti dei template.
- **Nessuna modifica al codice delle app, alle roadmap canoniche, al registro CAP o ai Golden** da questa ricerca. L'ammissione a prodotto richiede decisione distinta e verifiche del relativo Product Bible.
- **App Factory baseline**: `App-Factory-Core@2b3ae9e01764b7504980efca34f2543949dc7b89`, Master v27 / Golden Index v29.
- **Notes source**: `Notes-Ecosistema@2780847a0779573ab54d0d68a088e4f552e2840a`; **Anna source**: `Agenda-per-Anna@d82e2d12593683cf8bd5af8c05ee33ab19906f56`.

Questa cartella organizza **pattern**, non donor di codice Gumroad. L'eventuale codice Flutter deve essere originale o derivato da donor autorizzato con licenza e test.
