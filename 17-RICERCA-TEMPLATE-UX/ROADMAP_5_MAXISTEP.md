# Roadmap trasversale in 5 maxi-step — ricerca template UX

Nessuna modifica implicita alle roadmap delle app; questa è una **proposta di coordinamento** approvata come ricerca. Owner e limiti provengono dai Product Bible correnti.

| Step | Decisione / risultato | Notes-Ecosistema | Anna's Diary | Gate e prova |
|---|---|---|---|---|
| 1. Inventario fonti | Reconciliation e dedup di titoli, versioni e sottoprodotti | Filtrare casi di project/task/study | Filtrare diary/Noi/goals/vision | **BLOCKED** senza elenco Gumroad autenticato; conservare il catalogo privato, non pubblicarlo |
| 2. Audit source vs candidate | Delta per pattern con decisione esplicita | Usare `templates.dart`, `planner.dart`, `study.dart`, `visual_documents.dart`; issue #46/#51/#85 | Preservare `AgendaPreferences`, rituali e Product Bible; issue #226/#225/#224 | File/commit esatti, categoria 'in codice' separata da 'verificato Web' |
| 3. UX e prototipi | Approvazione mock-up interattivi prima del codice | Home modulare + template preview + board; non sostituire owner | Diario/Noi/vision in UI DS6, Vault invariato | Revisione visiva, accessibility, locale, explicit 10/10 se richiesto dal router |
| 4. PR integrate e testate | Estensioni minime, a release separate | Web-first, persistence scaling e preview; Smart Inbox non prod finché #46 aperta | No sync silenziosa, ACL Noi, no nuovo DB, no AI/cloud automatico | PR esatta, analyze/test/web build, AppLab e physical se richiesti |
| 5. Donor/Golden | Riuso registrato senza promozione prematura | Produrre consumer/test ed evidenze di esecuzione | Consumer distinto con UX/privacy specifiche | SHA, licenze, adattamento, tests, nessun nuovo CAP duplicato |

## Stato esecuzione Template Native — 09/11/2026

Gli Step 2–4 dei **tre piloti nativi** sono già source-integrated; l'inventario di terze parti resta un filone separato con dipendenze di acquisto/licenze. Per Step 5 è stata predisposta [la provenance per tre donor scoping](STEP5_DONOR_PROVENANCE_2026-11-09.md), senza promuovere un nuovo Golden. [QA sorgente e limiti](EXECUTION_4_PRIORITIES_2026-11-09.md) includono PR #98/#293/#27 e device ancora NON VERIFICATI. Il [blueprint premium](BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md) è progettazione futura: non significa Step 5 billing o Store READY.

## Dipendenze ad alto impatto
- **Notes Web**: lo snapshot bounded in localStorage precede grandi importazioni commerciali; migrazione/backup vanno verificati prima di un importer.
- **Smart Inbox #46**: la compensazione cross-store QA non è una transazione atomica; non attivare in production con una semplice toggle.
- **Anna / Noi #225**: condividere solo contenuto consentito al ruolo, senza usare il Vault o sincronizzare dati intimi.
- **Vision Board**: integrare con il lavoro già catalogato in `15-VISION-BOARD` invece di aprire una seconda linea di ricerca.
- **Tema**: differenziare Notes professionale e Anna editoriale, riutilizzando design token e primitivi anziché unificare l'identità.

## Uscita di questa PR
Solo **ricerca, protocollo, scheda di crosswalk e inbox proposte**. Niente sorgente app, dati di acquisto, token, CAP registry, cloud, workflow o Golden modifica. Nessun test applicativo dichiarato.
