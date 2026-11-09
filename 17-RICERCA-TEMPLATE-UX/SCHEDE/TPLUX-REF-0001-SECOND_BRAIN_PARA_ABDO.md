# TPLUX-REF-0001 — Second Brain (PARA Dashboard), Abdo Karamallah

**Registrazione**: 2026-11-09
**Tipo**: pattern di UX/organizzazione — **REFERENCE-ONLY** (non donor di codice o grafica)
**Profondità**: **E1-PUBLIC-MARKETPLACE / PREVIEW IMAGE**, E2 **NON VERIFICATO**
**Product admission**: **PROPOSTA, NON APPROVATA NEI REPO APP**
**Destinazioni**: Notes-Ecosistema (principale), Anna's Diary (sottoinsieme personale, solo opt-in)
**Origine**: link condiviso per analisi, non prova di acquisto o di accesso al workspace privato

## Fonti e accessibilità
- Link originale: https://byabdo.notion.site/Second-Brain-PARA-Dashboard-f258a32233ba4b758b8f47d0ca24f7f6
- Scheda ufficiale Notion Marketplace: https://www.notion.com/templates/second-brain-para-dashboard
- Scheda ufficiale localizzata con descrizione completa: https://www.notion.com/pt/templates/second-brain-para-dashboard
- Sito del creatore / descrizione generica PARA: https://heyabdo.com/notion/notion-second-brain

**Access gate**: il link Notion originale ha restituito `object_not_found` dall'accesso Notion collegato e il browser pubblico non ha restituito la pagina; l'elenco Workspace non ha identificato la pagina condivisa. **NON** sono stati letti blocchi, database, formule, viste, proprietà o sottopagine dell'istanza originale.

**Differenza di varianti**: marketplace e sito commerciale del creatore mostrano riferimenti/canali differenti; NON inferire che prezzo, versione o funzionalità della variante commerciale coincidano con la copia del link originale.

## Evidenza E1: claim del creatore (non test di funzionamento)
Il Marketplace descrive: `Projects`, `Areas`, `Resources`, `Archive`, `Tasks`, design intuitivo e template personalizzabili.

| Elemento | Tipo di evidenza | Limite |
|---|---|---|
| PARA: Projects / Areas / Resources / Archive | DESCRIZIONE PUBBLICA | Non verificata struttura delle relazioni |
| Tasks e divisione dei progetti in azioni | DESCRIZIONE PUBBLICA | Non verificati workflow o stati |
| Template personalizzabili | DESCRIZIONE PUBBLICA | Non verificato se sono database template, pulsanti o semplici pagine |
| Pannello `Quick Action` per Area, Task, Project e Resource | SCREENSHOT MARKETPLACE | Non testata creazione reale |
| Navigazione laterale a Projects, Areas, Resources, Archives, Tasks | SCREENSHOT MARKETPLACE | Non verificati link interni, permessi, routing |
| Galleria delle aree con card e progresso dei progetti | SCREENSHOT MARKETPLACE | Non verificata formula/rollup: potrebbero essere valori dimostrativi |
| Schede Projects Active/Completed, card con date e status | SCREENSHOT MARKETPLACE | Non verificati filtri e transizioni reali |

## Lettura visuale: pattern astratti, senza copiare il design
- **Architettura informativa**: menu operativo breve a sinistra e sezioni operative/di consultazione al centro.
- **Riconoscimento**: separazione fra azioni di creazione e destinazioni di navigazione.
- **Densità**: card compatte, icone riconoscibili, percentuali/progress bar per riepilogo.
- **Palette**: anteprima prevalentemente neutra, contrasti grigio/nero e aree semplici. Riadattare con i design token delle app.
- **Rischi UX da verificare**: menu laterale su smartphone, scalabilità 100+ elementi, keyboard/screen reader, dati vuoti, differenze di permessi, significato delle percentuali, layout ridotto.

## Crosswalk con codice delle due app
Ancorato agli SHA documentati in `17-RICERCA-TEMPLATE-UX/README.md`.

| Opportunità | Notes-Ecosistema | Anna's Diary | Proposta minima senza duplicazione |
|---|---|---|---|
| Quick Actions | Capture/Planner/Project Workspace già implementati in diversi componenti | `Unified Capture` e schemi editoriali già presenti | Ricomposizione delle CTA su Home, nessun nuovo handler/source-of-truth |
| Catalogo template | `flutter_app/lib/src/domain/templates.dart` — `PersonalTemplates`, `PageTemplates` | `lib/src/daily_rituals.dart` e preset diario | Preview/categorie e preset contestuali, test rollback |
| Areas | Knowledge/Projects, relazioni esistenti | Raccolte private e temi vita, scope leggero | Notes: vista derivata Area → Projects; Anna: card private opzionali |
| Progress | Project Workspace/Planner già presenti | Week review e `realistic_day_advice.dart`; #226 aperta | Calcolare solo progress da task canonici, evitare metriche fittizie |
| Resources | Knowledge/Research Workspace già presenti | Preferire ricordi/oggetti personali, non library professionale | Notes: discovery di riferimenti esistenti; Anna: no clone PARA |
| Archive | Note/Projects stati esistenti | Diario/Ricordi, controlli privacy | Viste filtrate e recuperabili; nessun purge o migrazione implicita |
| Project board | Planner Kanban e Project Workspace | Mini-planner Noi #225 aperta, permessi stretti | Note: viste derivate; Anna: solo task/eventi autorizzati |

## Riuso e licenze
- **PATTERN_REFERENCE**: va bene studiare concetti, flussi e gerarchia, scrivendo una implementazione originale.
- **NON APPROVATO PER COPIARE**: screenshot, immagini, testi, layout puntuale, icone, formule non esaminate, codice, risorse o template stessi.
- Nulla diventa `CERTIFIED DONOR`, `COPY-READY GOLDEN` o `CAP IMPLEMENTATA` in questa fase.

## Condizioni di avanzamento da E1 a E2
1. Utente duplica il template nel workspace Notion autorizzato e scarica `Export → Markdown & CSV` con **Include subpages**; invia ZIP, oppure rende la copia disponibile nel workspace con permessi dell'integrazione Notion.
2. Ispezionare l'intera gerarchia dei file, database CSV, proprietà esportate, relazioni/loss di esportazione, media consentiti e README della variante.
3. Validare elementi visuali con screenshot delle schermate principali e viste mobile, se l'export non preserva il layout.
4. Aggiornare questa stessa scheda (senza riusare un ID diverso), distinguendo **verificato**, **parziale**, **sconosciuto**.
5. Ammettere una feature solo dopo dedup CAP, Product Bible, UX approval e test; mantenere il percorso di import staging/validate/commit.

**Esito attuale**: candidato alto per migliorare il punto di ingresso Notes e il catalogo dei template. Per Anna selezionare solo idee leggere per vita personale. Nessuna implementazione suggerita come già pronta a partire da questo template da solo.

## Aggiornamento E2 — Export autorizzato esaminato il 09/11/2026

Esaminato uno ZIP Notion con **42 file (25 Markdown, 17 CSV)** della pagina Second Brain (PARA Dashboard). Sono presenti i dataset `Projects` (6 righe), `Areas` (4), `Resources` (4), `Tasks` (6), e pagine di dettaglio con link fra progetti/aree/risorse/task. CSV con campi di status, due date, priorità, relazioni testuali, progress e timeline. **Questo conferma la struttura esportata, non le formule in Notion, la logica dei pulsanti, le viste runtime o l'esatta fidelità visuale.** Le percentuali sono valori esportati, non definizioni delle formule.

**Stato aggiornato:** `E2_EXPORT_STRUCTURE_VERIFIED` limitatamente a tali file; E3 non raggiunto. Il precedente limite di accesso al link Notion resta valido per l'istanza live. Nessun contenuto commerciale è copiato nel repository.
