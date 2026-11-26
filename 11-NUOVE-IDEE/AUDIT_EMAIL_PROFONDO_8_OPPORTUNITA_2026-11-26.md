# Audit profondo email → 8 opportunità per App Factory (26/11/2026)

> **Decisione utente:** registrare tutte le opportunità in `11-NUOVE-IDEE` e, dove pertinente, annotare miglioramenti alle app già esistenti. **NON equivale ad approvare sviluppo/roadmap, modificare Product Bible o creare nuovi prodotti.**
>
> **Privacy:** analisi originale di corrispondenza personale, ma questo repository conserva esclusivamente categorie astratte, nessuna email, indirizzo, messaggio, ordine, cifra o circostanza riconducibile alla persona. La selezione è editoriale e non prova un bisogno di mercato.

## Ambito e metodologia
- Fonti tematiche private campionate: newsletter fotografia e fotolibri, creator/workflow B2B, produttività e AI, strumenti finanziari, design/contenuti, viaggi e gaming. **Non è stata analizzata esaustivamente l'intera casella.**
- Cross-check: portafoglio `01-PORTAFOGLIO/CATALOGO_APP.md`, `INBOX_IDEE.md`, catalogo CAP (199 record al campionamento), README e sorgenti pertinenti dei repository pubblici. I livelli SOURCE/CI/device non sono qui ricertificati.
- Mercato: ci sono alternative note per photo memories, workflow/task, field service, portfolio analytics, recipe cooking mode, image coaching e content provenance; l'innovazione qui è una **ipotesi differenziante da testare**, non unicità dimostrata.
- Criterio di utilità: passaggio **input → azione → risultato verificabile**, poco attrito, dati locali quando possibile, beneficio misurato e confini di prodotto.
- Classificazione: **IDEA / DA_VALUTARE / NOT_APPROVED**, priorità di ricerca qualitativa P1/P2, non priorità esecutiva né score CAP.

## Matrice canonica di otto idee

| ID stabile | Titolo | Tipo / destinazione di ricerca | Priorità ricerca | Stato |
|---|---|---|---|---|
| AUDMAIL-20261126-01 | **LifeCanvas — archivio fotografico che diventa esperienza** | Evoluzione GalleryDrift; handoff opzionale Wonderlog / Anna's Diary | P1 | DA_VALUTARE |
| AUDMAIL-20261126-02 | **Procedure Engine — informazioni in procedure eseguibili** | Evoluzione Notes-Ecosistema, delta sulla Smart Inbox e CAP-0093 | P1 | DA_VALUTARE |
| AUDMAIL-20261126-03 | **Service Passport — rapportini per tecnici sul campo** | **Nuova app B2B standalone candidata** | P1 | DA_VALUTARE |
| AUDMAIL-20261126-04 | **Failure Intelligence — da log a diagnosi di incidente** | Evoluzione AppLab/App Factory, riuso CAP-0070 da verificare | P1 **interna** | DA_VALUTARE |
| AUDMAIL-20261126-05 | **Decision Studio — simulatori economici concreti** | Evoluzione CashMate + Finance Intelligence Agent (solo simulazioni) | P2 | DA_VALUTARE |
| AUDMAIL-20261126-06 | **Kitchen Conductor — coordinatore di cotture** | Evoluzione TasteAI/Cooking Anime | P2 | DA_VALUTARE |
| AUDMAIL-20261126-07 | **Art-to-Shot — esercizi di composizione da arte** | Evoluzione ArtDrift + FrameLab, ambiti separati | P2 | DA_VALUTARE |
| AUDMAIL-20261126-08 | **Origin Passport — tracciabilità contenuti e licenze** | Capability editoriale ArtDrift / World Days / FrameLab, delta CAP-0043 | P2 **interna** | DA_VALUTARE |

### AUDMAIL-20261126-01 — LifeCanvas
**Problema:** foto ordinate ma mai ritrovate o trasformate in ricordi utilizzabili.
**Azione 1 minuto:** apri cartella selezionata → vedi raggruppamenti locali per data/cartella → scegli un momento → produci mini-album o pagina ricordo esportabile.
**MVP:** gestione foto senza upload, raggruppamento deterministico, selezione esplicita, layout visivo, export PDF; handoff opzionale in futuro, mai lettura implicita di dati Anna.
**Differenziale da validare:** continuità fra canvas spaziale, esplorazione e produzione di un artefatto; NON inventare nuovo motore canvas se Drift Core esiste.
**Gate:** audit ArtDrift+GalleryDrift Core pin esatti; privacy MediaStore, prestazioni ampie raccolte, confronto con foto-memory app; verifica con utenti che l'album sia realmente utile.
**Collocazione:** GALLERY_ONLY per accesso a libreria privata, SHARED_CORE solo per renderer/gesture dimostrate, bridge explicit-consent per Wonderlog/Anna. Nessuna nuova app.

### AUDMAIL-20261126-02 — Procedure Engine
**Problema:** leggere guide, documenti o note non garantisce di portare a termine un'attività.
**Azione:** importa testo/PDF volontariamente → revisione dei passaggi → checklist con stato e prova → riprendi da ultimo passaggio.
**MVP:** editor manuale della procedura, identificazione fonte vs suggerimento, step, dipendenze di base, allegati facoltativi, stato persistente, export; AI solo suggerimenti confermati.
**Differenziale da validare:** esecuzione e tracciabilità, NON ennesimo riassunto o duplicato Smart Inbox/CAP-0093.
**Gate:** verificare delta nei moduli Notes attuali, non costruire secondo DB/task, privacy fonti, concorrenza e acceptance su procedura reale.

### AUDMAIL-20261126-03 — Service Passport
**Problema:** piccoli tecnici ricopiano macchina, guasto, intervento e cliente fra chat, tabelle, calendario e rapportino.
**Azione:** fotografa targhetta → verifica manuale marca/modello/matricola → apre scheda macchina → registra guasto, attività, ricambi e firma → esporta rapportino PDF.
**MVP B2B:** anagrafica clienti/macchine, storico interventi, foto, note, firma cliente, export PDF, backup locale; no OCR obbligatorio per v1.
**Nicchia/ICP candidata:** ditte piccole di assistenza installazione e riparazione attrezzature professionali; mercato generale field-service già competitivo.
**Gate commerciale:** 5–10 colloqui con tecnici, rilevazione minuti risparmiati sul ciclo intervento, GDPR e custodia firma, quote/legalità licenze; verificare software concorrente, willingness-to-pay e costi di supporto prima di aprire repo.
**Stato:** nuova app proposta; **nessun repository o prodotto creato**.

### AUDMAIL-20261126-04 — Failure Intelligence
**Problema:** notifiche CI ridondanti nascondono causa radice; build ripetute vengono trattate come incidenti separati.
**Azione:** commit SHA e log esatti → clustering deterministico errori → confronto ultima build verde → causa probabile verificabile e link ai log.
**MVP:** import GitHub Actions read-only, fingerprint dell'errore, raggruppamento, regressione-vs-infrastruttura, report evidence-first.
**Differenziale:** spiegazione verificabile e dedup; non ricostruire scheduler, repair agent, verifier o Golden esistenti in AppLab/CAP-0070.
**Gate:** dati sintetici e failure fixture; accuratezza/falsi raggruppamenti, audit log, nessuna riparazione autonoma autorizzata. Feature interna, non nuovo prodotto consumer.

### AUDMAIL-20261126-05 — Decision Studio
**Problema:** rendimento percentuale, costo di finanziamento o nuovo salario spesso non indicano conseguenze economiche reali.
**Azione:** scegli scenario (finanziamento/cambio lavoro/PAC) → imposta ipotesi e vincoli → confronta risultati trasparenti in euro/periodi.
**MVP:** tre simulatori deterministici indipendenti, formule visibili, range/sensitivity, note su ipotesi e esportazione; niente broker credentials.
**Distinzione:** CashMate per decisioni di finanza quotidiana; Finance Intelligence Agent per PAC, portafogli e rendimenti con fonti/tempi dichiarati.
**Gate:** formule certificate con esempi verificabili, no advice/trading reale, normative, confronto con portfolio tracker e calcolatori esistenti. Nessuna automazione di acquisti.

### AUDMAIL-20261126-06 — Kitchen Conductor
**Problema:** ricette separate non coordinano piatti con tempi diversi per farli arrivare pronti insieme.
**Azione:** seleziona 2–3 ricette canoniche → indica ora servizio → genera sequenza di preparazione, cottura, riposo e timer paralleli.
**MVP:** dipendenze e durate editorialmente validate, timeline calcolata in modo deterministico, timer multipli, pausa/sostituzioni controllate, schermata hands-busy a testo grande.
**Gate:** ingredienti/temperature sicurezza alimentare, compatibilità TasteAI e Cooking Anime senza ricette duplicate, collisioni risorse (fornelli/forno) e QA con preparazioni vere; differenziale rispetto a cook modes/timer già diffusi.
**Stato:** proposta funzionale per app esistenti, non terza app ricette.

### AUDMAIL-20261126-07 — Art-to-Shot
**Problema:** vedere dipinti e leggere guide fotografiche sono attività separate; manca un passaggio didattico concreto.
**Azione:** da opera ArtDrift seleziona 'Prova questa composizione' → ottieni griglia compositiva spiegata → prova volontariamente con fotocamera e confronta.
**MVP:** 10 opere open-access con composizioni descritte/validate, overlay guide manuali, confronto prima/dopo locale; niente valutazione automatica spacciata per oggettiva.
**Gate:** copyright/diritti di riproduzione, consenso camera, adattamento a rapporto d'aspetto, indipendenza ArtDrift/FrameLab e test su telefono. **ART_ONLY** per opere e API musei; eventuale UI/coach fotografico FrameLab separato.

### AUDMAIL-20261126-08 — Origin Passport
**Problema:** per contenuti editoriali, immagini e asset creativi servono provenienza, licenze, modifiche e prove prima della pubblicazione.
**Azione:** seleziona asset → registra origine/licenza/uso commerciale/attribuzione/edit → preflight report con stati PASS/REVIEW/BLOCKED basati su evidenze.
**MVP:** manifest asset per record, fonti/versione, proof links, esito di revisione, export audit; import metadata C2PA quando esistono, senza dedurre autenticità dalla loro assenza.
**Gate:** distinzione copyright opera e riproduzione, audit comparato con CAP-0043 (workflow fonti e artwork) e registri World Days/FrameLab; niente 'autenticità garantita'. Preferire capacità editoriale interna.

## Esclusioni / non nuove idee
Le seguenti categorie erano emerse ma **non** ricevono nuovi ID/prodotti perché già diffuse o sovrapposte: screenshot AI organizer; photobook generator standalone; AI quiz da PDF; ETF overlap tracker standalone; timer ricette semplice; task manager da email. Non creare questi cloni senza nuovo delta dimostrato.

## Matrice destinazioni e stato
| Destinazione | Idee | Tipo di annotazione | Trattamento |
|---|---|---|---|
| GalleryDrift | 01 | esperienza galleria e export | backlog di ricerca, non attivare |
| Wonderlog / Agenda-per-Anna | 01 | handoff opt-in, non integrare senza decisione privacy | solo cross-reference, no duplicazione del bridge |
| Notes-Ecosistema | 02 | procedure con prova e stato | ricerca funzionale, non riscrivere Smart Inbox |
| AppLab / App-Factory-Core | 04 | diagnosi CI evidence-first | candidato AppLab, Core invariato |
| CashMate + Finance Intelligence Agent | 05 | simulazioni bounded | backlog separato dai dati finanziari reali |
| TasteAI / Cooking Anime | 06 | scheduler ricette | test di coordinamento multipiatto, no modifica ricette ora |
| ArtDrift / FrameLab | 07 | apprendimento fotografico | diritti e UX separati |
| ArtDrift / World Days / FrameLab | 08 | source/provenance per contenuti | delta da CAP-0043, no falsa certificazione |
| App Factory catalogo | 01–08 | un solo set di ID e nota esclusioni | ricerca, nessuna implementazione |

## Criterio per promuovere
- Test assistito con compito concreto, baseline di tempo/errori, criterio di successo e almeno 5 utenti esterni per prodotto consumer o 5–10 operatori per B2B.
- Confronto testato con alternative esistenti; differenziale non basato solo su AI.
- No merge di codice, billing o permessi senza approvazione specifica di Product Bible, roadmap e gate.
- Crosswalk CAP: **CAP-0011, CAP-0043, CAP-0070, CAP-0093** sono potenzialmente pertinenti ma non provano equivalenza. Per nuovi contratti canonici occorrono audit e generazione verificata del registro: **qui non si assegnano CAP fittizie né si sovrascrivono gli stati tecnici**.

## Registro di follow-up nei repository (ricerca, non sviluppo)

- **01 LifeCanvas** — [GalleryDrift #17](https://github.com/riccardopinato/GalleryDrift/issues/17). Wonderlog/Anna soltanto bridge futuro previa decisione privacy.
- **02 Procedure Engine** — [Notes #108](https://github.com/riccardopinato/Notes-Ecosistema/issues/108).
- **03 Service Passport** — [issue del catalogo #187](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/issues/187); **nuovo repo non creato**.
- **04 Failure Intelligence** — [AppLab #245](https://github.com/riccardopinato/AppLab/issues/245).
- **05 Decision Studio** — [Finance Intelligence #6](https://github.com/riccardopinato/Finance-Intelligence-Agent/issues/6); CashMate solo mappata in catalogo.
- **06 Kitchen Conductor** — [TasteAI #10](https://github.com/riccardopinato/TasteAI/issues/10); Cooking Anime solo mappata in catalogo.
- **07 Art-to-Shot** — [ArtDrift #72](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/issues/72), [FrameLab #9](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/issues/9).
- **08 Origin Passport** — [ArtDrift #73](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/issues/73), [World Days #159](https://github.com/riccardopinato/World-Days/issues/159), [FrameLab #10](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/issues/10).

[Crosswalk CAP e anticollisione](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_EMAIL_8_CAP_CROSSWALK_20261126.md). Gli issue conservano solo brief di ricerca: nessuna implementazione dichiarata.
