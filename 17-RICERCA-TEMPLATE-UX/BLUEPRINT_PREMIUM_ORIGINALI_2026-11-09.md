# Blueprint commerciale e UX — 4 template originali

**Data:** 09/11/2026. **Stato:** `DESIGN CANDIDATE / RICHIEDE APPROVAZIONE UX E PRODUCT BIBLE`. Questa proposta sviluppa l'idea esistente `TPL-STORE-2026-01`, non costituisce una nuova app/CAP, un'offerta già venduta o l'autorizzazione a implementare il billing.

**Regole comuni:** proposte `research_candidate` nello standard `contracts/template_engine_v1`; ID stabili e namespaced; nessuna conversione dei modelli gratuiti in paid; prezzo **€3,99 per template** solo ipotesi di test; template originali senza account Notion, licenze/asset di terzi, URL remoti o payload eseguibile. Preview usa contenuto sintetico e rende sempre espliciti costi, confini e modifiche ai dati PRIMA della conferma. Nessuna creazione automatica di account, abbonamenti, notifiche, AI o condivisioni.

## NOTES-PACK-01 — Project Launch Studio

- **Identity candidate:** `it.riccardopinato.notes.project_launch_studio`; target `notes`; IT/EN/ES/FR/DE/PT.
- **Problema:** avviare un progetto con un processo coerente anziché copiare note e creare task disorganizzati.
- **Valore originale a pagamento (proposto):** wizard di 4 passaggi: obiettivo e criterio di successo → materiale/fonte → prossime azioni esplicite → revisione. Un'unica installazione *consapevole* crea un Project canonico (se disponibile e autorizzato), una Note guida con collegamento e una checklist Task selezionabile; niente planner parallelo, automazioni silenziose o scadenze inventate.
- **UI nativa:** card “Che cosa ottieni”, anteprima di Project/Note/Task con dati demo, scelta delle sezioni, riepilogo diff con `Crea 1 progetto / 1 nota / N task`, conferma e possibilità di annullare prima di scrivere.
- **Configurazione:** nome obbligatorio, area opzionale, task seed scelti uno per uno, date solo inserite dall'utente; nessun testo di clienti acquisiti.
- **Dipendenze:** `Note`, Task, Planner/Project Workspace canonici; permessi writer, backup e lifecycle. Il supporto ad atomicità multi-record con ricevuta idempotente è **DA IMPLEMENTARE E TESTARE**; non spacciare il Note-only Step3 per install adapter multi-record.
- **Casi bloccanti:** account cambiato in preview, limite raggiunto, Project rev non corrente, failure su secondo writer, retry stessa `installation_request_id`, backup/restore. Non cancellare record dell'utente su disinstallazione del template.
- **Criterio di ammissione:** test su staging/rollback e note/task canonici, preview fedele, origine originale, app Web e Android; diff chiaro, nessun doppio record.

## NOTES-PACK-02 — Study Sprint Studio

- **Identity candidate:** `it.riccardopinato.notes.study_sprint_studio`; target `notes`; IT/EN/ES/FR/DE/PT.
- **Problema:** organizzare studio e richiamo attivo mantenendo la provenienza delle informazioni.
- **Valore originale (proposto):** sessione guidata con `Fonte → Argomenti → Domande manuali → Ripasso`, schede di sintesi e tre checkpoint scelti, collegati a note e attività esistenti. Le domande sono inserite dall'utente o strettamente derivate da materiale verificato; nessuna AI obbligatoria né risposta allucinata.
- **UI:** catalogo → anteprima percorso studio con dati demo → scelta capitoli e slot (solo durata/dati dichiarati) → diff dei record da creare → conferma. Indicatori derivati da completamenti reali, non da conteggio approssimativo.
- **Dipendenze:** Notes Study Core, Knowledge, Note/Task e filtri privacy; riusare l'owner esistente. Futura importazione OCR/PDF solo con provenienza e permessi reali, non inclusa nel pilota.
- **Test obbligatori:** fonte rimossa/archiviata, duplicato, offline, rev stale, cancellazione task, backup e font grande; zero scritture su Annulla, nessun testo commerciale esterno.

## ANNA-PACK-01 — Atlante dei ricordi

- **Identity candidate:** `it.riccardopinato.anna.memory_chapters`; target `annas_diary`; IT/EN/ES/FR/PT.
- **Problema:** valorizzare foto e pagine di diario in capitoli personali senza duplicare Memories o riversare contenuti sensibili altrove.
- **Valore originale (proposto):** percorso di quattro capitoli personalizzabili (persone importanti, luoghi, piccoli momenti, un anno da ricordare), prompt narrativi originali, selezione **esplicita** di ricordi già posseduti e layout editoriale DS6. Un capitolo può restare una normale nota/collezione tramite gli owner esistenti; **non** creare un nuovo “album database”.
- **UI:** scelta privacy `Privato` vincolata di default, preview su dati sintetici, selezione manuale di memorie e foto autorizzate, riepilogo di cosa sarà creato/coperto, conferma e editor esistente. **Noi ♡ fuori dal primo pilota**; nessuna esposizione di Vault.
- **Rimozione:** staccare il preset dall'elenco senza eliminare DiaryBlock, media o collegamenti esistenti. Nessun accesso a Vault, password o dati ciclici.
- **Test:** media mancanti, dati non visibili, account A→B→A, vault escluso, ripristino backup, contrasto e 2× font, nessun contenuto spostato automaticamente.

## ANNA-PACK-02 — Dodici settimane che contano

- **Identity candidate:** `it.riccardopinato.anna.twelve_week_reflection`; target `annas_diary`; IT/EN/ES/FR/PT.
- **Problema:** un percorso delicato di riflessione e piccoli obiettivi senza trasformare Anna in un task manager professionale.
- **Valore originale (proposto):** 12 capitoli settimanali originali, scelta volontaria di 1 obiettivo leggero, una domanda inizio settimana e una review di fine settimana, con collegamenti ai DiaryBlock già esistenti. Ogni capitolo è modificabile e riavviabile; nessuno streak, punteggio psicologico o monitoraggio salute.
- **UI:** preview delle 12 tappe con alcuni prompt sintetici → calendario locale di partenza scelto dall'utente → conferma → apertura dell'editor privato. Nessuna notifica attivata automaticamente; eventuali promemoria tramite consenso e writer esistente dopo approvazione separata.
- **Test:** date/DST, salto settimana, interruzione/ritorno senza duplicati, account e backup, annullamento, installazione ripetuta, cinque lingue, comportamento offline. Dopo revoca pagamento i testi inseriti dall'utente restano suoi.

## Confronto e ordine pilota

| Pack | Differenza dal Free | Principale complessità | Raccomandazione |
|---|---|---|---|
| Notes Project Launch Studio | Creazione multi-record coordinata e decision log; Book Tracker Free è nota singola | staging/rollback multi-writer e ACL | **Pilota 2** dopo adapter idempotente |
| Notes Study Sprint Studio | Percorso studio multi-sessione con fonte e checkpoint, non solo testo boilerplate | provenance/stale data e task owner | **Pilota 1 Notes**, limitando v1 a Note/Task |
| Anna Atlante dei ricordi | Curatela capitoli/media e narrativa personale, non semplici rituali | ownership/media/privato, backup | **Pilota 2 Anna**, inizialmente testo e media selezionati |
| Anna Dodici settimane che contano | 12 tappe editoriali originali e review opt-in, senza vendere rituali base | date/restart/idempotenza, L10n | **Pilota 1 Anna**, preview e DiaryBlock canonici |

**Criteri di accettazione commerciale prima di SKU:** ogni pilota deve avere valore originale verificato, un manifest `research_candidate` validato e poi ammesso esplicitamente a prodotto, tre ambienti comparabili (Web/Android/iOS solo dove supportati), preview reale, test install receipt e rollback, protezione privacy/account, licenze e materiali originali, accessibilità, misurazione della soddisfazione su utenti reali (dati non ancora disponibili). Solo con UX/Product approval si progettano schermate “Acquista”, prodotti non-consumable, entitlement/sandbox, restore/refund/unknown/offline e prezzi locali forniti dallo store, senza hardcode €3,99 nei widget.

**Decisioni ancora richieste prima di sviluppo premium:** approvazione dei quattro concept o modifiche, scelta di un pilota per app, flusso interattivo UX per il pilota e autorizzazione tecnica distinta per l'eventuale adapter multi-record. Billing/provider/store NON AUTORIZZATI da questo dossier.

**Source of truth:** [Idea store esistente](IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md); [Step4](UX_STEP4_CATALOGO_NATIVO_2026_11_09.md); App Factory Core template engine v1. L'uso del termine “Notion” in una fonte di ricerca non trasferisce diritti d'autore a questo progetto.
