# Audit funzionale trasversale — 95 repository GitHub — 08/11/2026

**Factory baseline:** [App-Factory-Core@85ecbb19](https://github.com/riccardopinato/App-Factory-Core/tree/85ecbb19aeb02da1b9d04348e043f69bab77bcb9) (Master v27, Golden Index v28).  
**Catalogo sorgente:** [REGISTRO_CAPABILITY.json](REGISTRO_CAPABILITY.json) — 160 CAP/385 associazioni al momento dell'avvio.  
**Atlas machine-readable:** [AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json](AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json).  
**Evidenze:** [12 batch JSON](AUDIT_OSS95_EVIDENZE_BATCH_01.json) più [6 README con path non standard](AUDIT_OSS95_README_VARIANTS_2026-11-08.json).  

## Risultati del censimento

- **95/95 repository** confrontate per identità, descrizione, licenza REST e README (89 a nome standard, 6 con path alternativo; tutti e 95 recuperati).
- **329 associazioni repository–feature**: uno stesso concetto compare in più repository, quindi **non** sono 329 CAP distinte.
- **47 CAP esistenti** riutilizzabili come match di ricerca (non automaticamente implementate) e **39 famiglie candidate** distinte nei casi d'uso/scope. I 39 ID `OSS95-Nxx` sono provvisori e non occupano CAP-0161 o successivi.
- **26/95** repository con licenza REST `NOASSERTION`/`UNKNOWN`: non significa necessariamente assenza di LICENSE nel repository, ma richiede audit file-per-file prima di qualsiasi copia. Per altre repository, licenza dichiarata dal metadato REST non è autorizzazione a copiare indiscriminatamente.
- **4 riferimenti di attenzione particolare**: taskade/taskade (DOCUMENTATION_ONLY); BookStackApp/BookStack (SOURCE_MOVED); bzg/org-mode (MIRROR_ONLY); ankicommunity/ankicommunity-sync-server (OLD_PROTOCOL_WARNING).
- Le 95 provengono dalle tre liste selezionate in chat (40+27+28). **Non è stata verificata la lista privata/autenticata delle stelle attuali**.
- **Livello di prova:** E0/E1 documentale del repository e del README; nessun build/CI device/commit donor E3 svolto su tutte le repository. Gli HEAD esterni precedentemente pinnati sono riferimenti, non certificazioni.

## Criteri di classificazione

1. Una repository può mostrare più funzioni: ciascuna appare nella matrice, con match `CAP-NNNN` esistente oppure nuova famiglia `OSS95-Nxx`.
2. Le `CAP-NNNN` indicano **sovrapposizione tematica** da validare contro il contratto della singola CAP, non identità di codice.
3. Le `OSS95-Nxx` sono candidature di responsabilità funzionale: alcune sono nuove, altre ESTENSIONE di codice già esistente (es. editor Flutter e workflow Notes). **Non attribuire automaticamente un ID CAP canonico** finché non sono superati il controllo anti-duplicato, le schede/kit e i gate di prodotto.
4. Le dimensioni `app_states`, decisione prodotto e completamento restano distinte. Nessuna roadmap/AGENTS/app source modificata.
5. Anna deve restare diario/agenda personale, non CRM/Notion; per Notes i gate roadmap [#60](https://github.com/riccardopinato/Notes-Ecosistema/issues/60) e catalogo [#41](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/issues/41) restano vincolanti.

## 39 famiglie candidate deduplicate

| ID provvisorio | Capability | App target (proposte) | Fonti OSS | Valutazione | Gate prioritario |
|---|---|---|---:|---|---|
| OSS95-N01 | Editor ricco a blocchi con round-trip Markdown reversibile | Notes-Ecosistema | 7 | ESTENSIONE_CON_SORGENTE_APP | Mantenere una sola sorgente canonica e regression sui blocchi non serializzabili |
| OSS95-N02 | Wikilink, backlink e rinomina dei link con riparazione | Notes-Ecosistema | 8 | NUOVA_DA_CONFRONTARE | Riconciliare con Knowledge Graph e link stabili già implementati |
| OSS95-N03 | Note gerarchiche, alias e transclusioni controllate | Notes-Ecosistema | 3 | NUOVA_DA_CONFRONTARE | No cicli e duplicazioni di proprietario; link non equivalgono a copia |
| OSS95-N04 | Query e scripting locale su note e knowledge base | Notes-Ecosistema | 4 | NUOVA_PROPOSTA | Sandbox, privacy, limiti di esecuzione e tipizzazione |
| OSS95-N05 | Tabelle relazionali e campi calcolati/formule | Notes-Ecosistema | 9 | NUOVA_PROPOSTA | Distinguere da proprietà tipizzate e viste tabellari già esistenti |
| OSS95-N06 | Viste salvate con filtri, raggruppamenti e permessi | Notes-Ecosistema | 10 | ESTENSIONE_DA_VERIFICARE | Usare ProjectWorkspace canonico, mai duplicare Note/Task |
| OSS95-N07 | Convergenza CRDT per modifiche concorrenti offline | Notes-Ecosistema | 6 | OPZIONE_ARCHITETTURALE | Prototipo isolato; nessuna sostituzione di Shared Spaces autorizzata |
| OSS95-N08 | Condivisione cifrata selettiva e revoca per documento | Notes-Ecosistema | 9 | ESTENSIONE_CON_RISCHI | Threat model, ACL server, chiavi e revoca effettiva |
| OSS95-N09 | Sincronizzazione CalDAV bidirezionale opt-in | Agenda-per-Anna | 5 | NUOVA_PROPOSTA_CON_GATE | Google Calendar Direct issue #199 resta DRAFT; account e conflitti vanno verificati |
| OSS95-N10 | Conversione esplicita evento↔attività senza duplicati | Agenda-per-Anna; Notes-Ecosistema | 1 | NUOVA_PROPOSTA | Preservare identità, reminder e ripristino |
| OSS95-N11 | Ricorrenza calcolata da scadenza o completamento | Agenda-per-Anna; Notes-Ecosistema | 2 | NUOVA_PROPOSTA | DST e salti calendario; nessun reminder doppio |
| OSS95-N12 | Rotazione equa degli assegnatari nelle attività condivise | Agenda-per-Anna; Notes-Ecosistema | 1 | NUOVA_PROPOSTA | Per Anna solo Noi ♡, consenso e ownership espliciti |
| OSS95-N13 | Sprint, cicli e retrospettive di progetto | Notes-Ecosistema | 2 | NUOVA_PROPOSTA | Non sovrascrivere il planner esistente |
| OSS95-N14 | Limiti WIP e swimlane Kanban configurabili | Notes-Ecosistema | 3 | ESTENSIONE_DA_VERIFICARE | Prima confrontare CAP-0103, -0105, -0096 |
| OSS95-N15 | Timeboxing drag-and-drop sul calendario | Notes-Ecosistema; Agenda-per-Anna | 6 | ESTENSIONE_DA_VERIFICARE | Conferma esplicita e nessun duplicato nelle date |
| OSS95-N16 | Timeline attività automatica con AFK e consenso | Work-Time-Keeper; FocuSense | 2 | NUOVA_CONSENSO_OBBLIGATORIO | No cattura schermo nascosta; retention e minimizzazione |
| OSS95-N17 | Tracciamento attività IDE tramite plugin opt-in | Work-Time-Keeper; CmdPocket | 1 | NUOVA_PROPOSTA | Solo eventi editor autorizzati e aggregati |
| OSS95-N18 | Espansione abbreviazioni solo nell'editor corrente | Notes-Ecosistema; CmdPocket | 1 | ESTENSIONE_DA_VERIFICARE | Riusa i template esistenti e permette undo |
| OSS95-N19 | Espansione testo a livello di sistema operativo | CmdPocket | 1 | NUOVA_ALTO_RISCHIO | Accessibilità/input hook per piattaforma, privacy, non installare di default |
| OSS95-N20 | Archivio snippet di codice con linguaggi e frammenti | CmdPocket; Notes-Ecosistema | 3 | NUOVA_DA_CONFRONTARE | Riutilizzare note/tag/code block senza un secondo vault |
| OSS95-N21 | Import/export lossless di todo.txt, Org e TaskPaper | Notes-Ecosistema | 5 | NUOVA_PROPOSTA | Parser delimitato, anteprima, semantica recurrence e rollback |
| OSS95-N22 | Finestre sticky giornaliere/settimanali per desktop | Agenda-per-Anna | 2 | ESTENSIONE_MULTIPIATTAFORMA | Separare dal widget Android CAP-0144 |
| OSS95-N23 | Punti, ricompense e progressione volontaria delle task | FocuSense; Notes-Ecosistema | 4 | NUOVA_PROPOSTA | Opt-in, nessuna pressione/comportamento patologizzante |
| OSS95-N24 | Serie abitudini e obiettivi di continuità con storico | FocuSense; Agenda-per-Anna | 6 | NUOVA_DA_CONFRONTARE | Distinguere dalla heatmap CAP-0145 |
| OSS95-N25 | Regole di automazione tipizzate trigger→azione con preview | Notes-Ecosistema | 7 | ESTENSIONE_CON_SORGENTE_APP | Notes 0.54 ha Workflow Automations; evitare doppio motore |
| OSS95-N26 | Trasporto decentralizzato P2P per dati condivisi cifrati | Notes-Ecosistema | 6 | OPZIONE_ARCHITETTURALE | Separare CRDT, identità e autorizzazione dal trasporto |
| OSS95-N27 | Editing Typst/matematica con anteprima verificabile | Notes-Ecosistema | 5 | NUOVA_PROPOSTA | Limitare a modalità studio ed export, valutare peso |
| OSS95-N28 | Pubblicazione controllata Markdown/wiki con redazione | Notes-Ecosistema | 5 | NUOVA_PROPOSTA | Mai esporre contenuti privati o condivisi per default |
| OSS95-N29 | Biblioteca citazioni e riferimenti bibliografici | Notes-Ecosistema | 1 | ESTENSIONE_DA_VERIFICARE | CAP-0119 copre audit fonti, non intera libreria di riferimenti |
| OSS95-N30 | Da evidenziazioni PDF a note collegate e storylines | Notes-Ecosistema | 1 | ESTENSIONE_DA_VERIFICARE | Riusare CAP-0035/0098/0119; preservare pagina e provenance |
| OSS95-N31 | Editor multipannello con due note e split sincronizzato | Notes-Ecosistema | 1 | ESTENSIONE_UX | Non duplicare i writer e testare gestione conflitti |
| OSS95-N32 | Recupero account cifrato con frase mnemonica senza email | Notes-Ecosistema; Agenda-per-Anna | 1 | NUOVA_ALTO_RISCHIO | Nessuna modifica al Vault Anna; threat model e restore test prima di valutare |
| OSS95-N33 | Diario testuale portable e operazioni CLI per data | Agenda-per-Anna; CmdPocket | 3 | ESTENSIONE_DA_VERIFICARE | Per Anna prodotto UI-first; CLI solo interop opzionale |
| OSS95-N34 | Command palette e scorciatoie tastiera contestuali | Notes-Ecosistema; CmdPocket | 8 | NUOVA_PROPOSTA | Ricerca e azioni limitate ai permessi correnti |
| OSS95-N35 | Timesheet esportabili e report settimanali per progetto | Work-Time-Keeper; Notes-Ecosistema | 9 | ESTENSIONE_DA_VERIFICARE | Misure da sessioni reali, timezone e no inventare lavoro |
| OSS95-N36 | Archivio documenti indicizzato con classificazione e retention | Notes-Ecosistema; PDF-Unifier | 1 | ESTENSIONE_DA_VERIFICARE | Distinguere OCR CAP-0035, triage CAP-0134 e vault documenti |
| OSS95-N37 | Marcatura attività tramite NFC volontario | Agenda-per-Anna; Notes-Ecosistema | 1 | NUOVA_PROPOSTA | Richiede NFC, conferma o revoca in shared-space |
| OSS95-N38 | Cattura audio di sistema e trascrizione locale consensuale | Notes-Ecosistema | 4 | NUOVA_POTENZIALE | Estende CAP-0085/0095; permessi OEM, consenso partecipanti e costo runtime |
| OSS95-N40 | Interfaccia MCP/API locale per lettura controllata di agenda e task | Notes-Ecosistema; CmdPocket | 1 | NUOVA_CONSENSO_OBBLIGATORIO | Sandbox, autorizzazioni, no accesso al Vault o chiavi |

## Destinazioni e opportunità trasversali

- **Notes-Ecosistema**: 32 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N01, OSS95-N02, OSS95-N03, OSS95-N04, OSS95-N05, OSS95-N06, OSS95-N07, OSS95-N08, OSS95-N10, OSS95-N11, OSS95-N12, OSS95-N13, OSS95-N14, OSS95-N15, OSS95-N18, OSS95-N20, OSS95-N21, OSS95-N23, OSS95-N25, OSS95-N26, OSS95-N27, OSS95-N28, OSS95-N29, OSS95-N30, OSS95-N31, OSS95-N32, OSS95-N34, OSS95-N35, OSS95-N36, OSS95-N37, OSS95-N38, OSS95-N40. Associazione di ricerca, non roadmap approvata.
- **Agenda-per-Anna**: 10 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N09, OSS95-N10, OSS95-N11, OSS95-N12, OSS95-N15, OSS95-N22, OSS95-N24, OSS95-N32, OSS95-N33, OSS95-N37. Associazione di ricerca, non roadmap approvata.
- **Work-Time-Keeper**: 3 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N16, OSS95-N17, OSS95-N35. Associazione di ricerca, non roadmap approvata.
- **FocuSense**: 3 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N16, OSS95-N23, OSS95-N24. Associazione di ricerca, non roadmap approvata.
- **CmdPocket**: 7 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N17, OSS95-N18, OSS95-N19, OSS95-N20, OSS95-N33, OSS95-N34, OSS95-N40. Associazione di ricerca, non roadmap approvata.
- **PDF-Unifier**: 1 famiglie candidate pertinenti (incluse estensioni e opzioni), IDs OSS95-N36. Associazione di ricerca, non roadmap approvata.

### Riscontro di codice interno già presente

- **Notes Editor:** [BlockEditorCodec](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/domain/blocks.dart), [UniversalBlockEditor](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/widgets/universal_block_editor.dart), [test round-trip](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/test/visual_blocks_compatibility_test.dart): N01 è **estensione**, non un editor da ricostruire.
- **Notes database/views:** [properties.dart](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/domain/properties.dart), [project_workspace.dart](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/domain/project_workspace.dart): esistono tipi e viste; nuove formule/relazioni e viste salvate richiedono una specifica non duplicante.
- **Notes Sync:** [shared_spaces_live_sync.dart](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/sync/shared_spaces_live_sync.dart): verifica merge/conflitto, ma **non** un CRDT; non introdurre Yjs/Automerge senza compatibilità, ACL e performance.
- **Notes Focus:** [focus.dart](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/lib/src/domain/focus.dart) e [test](https://github.com/riccardopinato/Notes-Ecosistema/blob/d99a30633134e6e800e93e2a04741554d38c839b/flutter_app/test/focus_productivity_test.dart): timer/sessioni già presenti; nuovo tempo passivo è separato per consenso.
- **FocuSense:** [Product Bible](https://github.com/riccardopinato/FocuSense/blob/bdc8becfff1b1a5f629456deb34170f0d905d8b7/PRODUCT_BIBLE.md) documenta sessioni focus e core; nessuna inferenza di session tracking universale.
- **Anna:** [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/e5b956caf7976b70afe8269fe55697f2af21c568/docs/PRODUCT_BIBLE.md) limita l'ambito a vita personale, privacy e dati canonici.

## Matrice repository-by-repository (95/95)

| # | Repository | Facet | CAP già censite da confrontare | Candidate nuove/estensioni | Licenza REST | Fonte |
|---:|---|---:|---|---|---|---|
| 1 | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 5 | CAP-0096, CAP-0100 | OSS95-N01, OSS95-N05, OSS95-N06 | AGPL-3.0 | Riferimento |
| 2 | [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) | 4 | CAP-0013 | OSS95-N02, OSS95-N03, OSS95-N04 | AGPL-3.0 | Riferimento |
| 3 | [mattermost-community/focalboard](https://github.com/mattermost-community/focalboard) | 4 | CAP-0100, CAP-0096 | OSS95-N06, OSS95-N14 | NOASSERTION | Riferimento |
| 4 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | 5 | CAP-0029, CAP-0094, CAP-0100 | OSS95-N01, OSS95-N05 | NOASSERTION | Riferimento |
| 5 | [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 4 | CAP-0032, CAP-0112 | OSS95-N02, OSS95-N04 | AGPL-3.0 | Riferimento |
| 6 | [outline/outline](https://github.com/outline/outline) | 4 | CAP-0013, CAP-0100 | OSS95-N08, OSS95-N28 | NOASSERTION | Riferimento |
| 7 | [AppFlowy-IO/appflowy-editor](https://github.com/AppFlowy-IO/appflowy-editor) | 3 | CAP-0023 | OSS95-N01, OSS95-N34 | NOASSERTION | Riferimento |
| 8 | [logseq/logseq](https://github.com/logseq/logseq) | 4 | CAP-0098, CAP-0112, CAP-0150 | OSS95-N02 | AGPL-3.0 | Riferimento |
| 9 | [foambubble/foam](https://github.com/foambubble/foam) | 3 | CAP-0098 | OSS95-N02, OSS95-N34 | NOASSERTION | Riferimento |
| 10 | [usememos/memos](https://github.com/usememos/memos) | 4 | CAP-0014, CAP-0150, CAP-0013 | OSS95-N28 | MIT | Riferimento |
| 11 | [dendronhq/dendron](https://github.com/dendronhq/dendron) | 4 | — | OSS95-N03, OSS95-N02, OSS95-N27, OSS95-N34 | Apache-2.0 | Riferimento |
| 12 | [anyproto/anytype-ts](https://github.com/anyproto/anytype-ts) | 5 | CAP-0100, CAP-0018 | OSS95-N05, OSS95-N07, OSS95-N26 | NOASSERTION | Riferimento |
| 13 | [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) | 4 | CAP-0096, CAP-0100, CAP-0004 | OSS95-N09 | AGPL-3.0 | Riferimento |
| 14 | [super-productivity/super-productivity](https://github.com/super-productivity/super-productivity) | 5 | CAP-0108, CAP-0109, CAP-0105 | OSS95-N15, OSS95-N35 | MIT | Riferimento |
| 15 | [makeplane/plane](https://github.com/makeplane/plane) | 5 | CAP-0103, CAP-0111, CAP-0148 | OSS95-N06, OSS95-N13 | AGPL-3.0 | Riferimento |
| 16 | [manuelernestog/weektodo](https://github.com/manuelernestog/weektodo) | 3 | CAP-0096, CAP-0144 | OSS95-N15 | GPL-3.0 | Riferimento |
| 17 | [donetick/donetick](https://github.com/donetick/donetick) | 5 | CAP-0096 | OSS95-N11, OSS95-N12, OSS95-N35, OSS95-N37 | AGPL-3.0 | Riferimento |
| 18 | [opf/openproject](https://github.com/opf/openproject) | 4 | CAP-0103, CAP-0104 | OSS95-N13, OSS95-N35 | GPL-3.0 | Riferimento |
| 19 | [standardnotes/app](https://github.com/standardnotes/app) | 3 | CAP-0018, CAP-0114 | OSS95-N08 | AGPL-3.0 | Riferimento |
| 20 | [streetwriters/notesnook](https://github.com/streetwriters/notesnook) | 4 | CAP-0018, CAP-0075, CAP-0013 | OSS95-N08 | GPL-3.0 | Riferimento |
| 21 | [laurent22/joplin](https://github.com/laurent22/joplin) | 4 | CAP-0076, CAP-0018, CAP-0013, CAP-0118 | — | NOASSERTION | Riferimento |
| 22 | [Laverna/laverna](https://github.com/Laverna/laverna) | 4 | CAP-0018, CAP-0032 | OSS95-N01, OSS95-N27 | MPL-2.0 | Riferimento |
| 23 | [codexu/note-gen](https://github.com/codexu/note-gen) | 4 | CAP-0148, CAP-0151, CAP-0076, CAP-0093 | — | GPL-3.0 | Riferimento |
| 24 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 4 | CAP-0085, CAP-0095, CAP-0031 | OSS95-N38 | MIT | Riferimento |
| 25 | [layzdonw/lazyaudio](https://github.com/layzdonw/lazyaudio) | 4 | CAP-0085, CAP-0095, CAP-0098 | OSS95-N38 | Apache-2.0 | Riferimento |
| 26 | [amicalhq/prismical](https://github.com/amicalhq/prismical) | 4 | CAP-0085, CAP-0095, CAP-0031 | OSS95-N38 | MIT | Riferimento |
| 27 | [HabitRPG/habitica](https://github.com/HabitRPG/habitica) | 3 | CAP-0145 | OSS95-N23, OSS95-N24 | NOASSERTION | Riferimento |
| 28 | [dromse/obsidian-gamified-tasks](https://github.com/dromse/obsidian-gamified-tasks) | 3 | CAP-0096, CAP-0145 | OSS95-N23 | MIT | Riferimento |
| 29 | [appwrite/appwrite](https://github.com/appwrite/appwrite) | 4 | CAP-0018, CAP-0100 | OSS95-N25, OSS95-N26 | BSD-3-Clause | Riferimento |
| 30 | [taskade/taskade](https://github.com/taskade/taskade) | 4 | CAP-0148, CAP-0100 | OSS95-N25, OSS95-N04 | NOASSERTION | DOCUMENTATION_ONLY |
| 31 | [OrangeCatzhang/orange-schedule](https://github.com/OrangeCatzhang/orange-schedule) | 4 | CAP-0144, CAP-0001 | OSS95-N22, OSS95-N15 | MIT | Riferimento |
| 32 | [FossifyOrg/Calendar](https://github.com/FossifyOrg/Calendar) | 4 | CAP-0004, CAP-0005, CAP-0144 | OSS95-N09 | GPL-3.0 | Riferimento |
| 33 | [vnotex/vnote](https://github.com/vnotex/vnote) | 4 | CAP-0098, CAP-0037 | OSS95-N27, OSS95-N01 | LGPL-3.0 | Riferimento |
| 34 | [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | 4 | CAP-0013 | OSS95-N04, OSS95-N25, OSS95-N02 | MIT | Riferimento |
| 35 | [linagora/twake-workplace](https://github.com/linagora/twake-workplace) | 2 | CAP-0100 | OSS95-N26 | UNKNOWN | Riferimento |
| 36 | [nocodb/nocodb](https://github.com/nocodb/nocodb) | 4 | CAP-0100 | OSS95-N05, OSS95-N06, OSS95-N08 | NOASSERTION | Riferimento |
| 37 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 4 | CAP-0029, CAP-0028, CAP-0149, CAP-0100 | — | MIT | Riferimento |
| 38 | [AmmarAbouZor/tui-journal](https://github.com/AmmarAbouZor/tui-journal) | 3 | CAP-0014, CAP-0150 | OSS95-N33 | MIT | Riferimento |
| 39 | [wernerkruger/vscode-daily-planner](https://github.com/wernerkruger/vscode-daily-planner) | 3 | CAP-0108, CAP-0109 | OSS95-N35 | MIT | Riferimento |
| 40 | [shuaiplus/inkstone](https://github.com/shuaiplus/inkstone) | 4 | CAP-0018, CAP-0032 | OSS95-N31, OSS95-N34 | NOASSERTION | Riferimento |
| 41 | [LifetimeLabsHQ/PrivacyNotes.app](https://github.com/LifetimeLabsHQ/PrivacyNotes.app) | 4 | CAP-0018, CAP-0146 | OSS95-N32, OSS95-N08 | AGPL-3.0 | Riferimento |
| 42 | [regisdantas/gamify-tasks](https://github.com/regisdantas/gamify-tasks) | 2 | — | OSS95-N23, OSS95-N24 | NOASSERTION | Riferimento |
| 43 | [sharvesh1401/TaskTrail](https://github.com/sharvesh1401/TaskTrail) | 3 | CAP-0101 | OSS95-N24, OSS95-N23 | MIT | Riferimento |
| 44 | [FossifyOrg/Notes](https://github.com/FossifyOrg/Notes) | 2 | CAP-0093, CAP-0014 | — | GPL-3.0 | Riferimento |
| 45 | [baslawson/Planner](https://github.com/baslawson/Planner) | 6 | CAP-0004, CAP-0144 | OSS95-N09, OSS95-N10, OSS95-N11, OSS95-N15 | GPL-3.0 | Riferimento |
| 46 | [Etar-Group/Etar-Calendar](https://github.com/Etar-Group/Etar-Calendar) | 4 | CAP-0004, CAP-0005, CAP-0144 | OSS95-N09 | GPL-3.0 | Riferimento |
| 47 | [nextcloud/calendar](https://github.com/nextcloud/calendar) | 4 | CAP-0004, CAP-0100, CAP-0003 | OSS95-N09 | AGPL-3.0 | Riferimento |
| 48 | [andstatus/todoagenda](https://github.com/andstatus/todoagenda) | 3 | CAP-0144, CAP-0004 | OSS95-N22 | Apache-2.0 | Riferimento |
| 49 | [jrnl-org/jrnl](https://github.com/jrnl-org/jrnl) | 3 | CAP-0014, CAP-0018 | OSS95-N33 | GPL-3.0 | Riferimento |
| 50 | [saber-notes/saber](https://github.com/saber-notes/saber) | 3 | CAP-0029, CAP-0118, CAP-0018 | — | GPL-3.0 | Riferimento |
| 51 | [tldraw/tldraw](https://github.com/tldraw/tldraw) | 4 | CAP-0029, CAP-0028, CAP-0149 | OSS95-N25 | NOASSERTION | Riferimento |
| 52 | [xyflow/xyflow](https://github.com/xyflow/xyflow) | 3 | CAP-0028, CAP-0117 | OSS95-N25 | MIT | Riferimento |
| 53 | [sorenwacker/nodus](https://github.com/sorenwacker/nodus) | 4 | CAP-0098, CAP-0119 | OSS95-N27, OSS95-N30 | NOASSERTION | Riferimento |
| 54 | [nextcloud/notes](https://github.com/nextcloud/notes) | 3 | CAP-0013, CAP-0004, CAP-0018 | — | AGPL-3.0 | Riferimento |
| 55 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | 3 | CAP-0035, CAP-0134 | OSS95-N36 | GPL-3.0 | Riferimento |
| 56 | [Zettlr/Zettlr](https://github.com/Zettlr/Zettlr) | 3 | CAP-0119 | OSS95-N27, OSS95-N28 | GPL-3.0 | Riferimento |
| 57 | [pbek/QOwnNotes](https://github.com/pbek/QOwnNotes) | 3 | CAP-0018, CAP-0075, CAP-0013 | — | GPL-2.0 | Riferimento |
| 58 | [docmost/docmost](https://github.com/docmost/docmost) | 4 | CAP-0100, CAP-0118 | OSS95-N02, OSS95-N08 | AGPL-3.0 | Riferimento |
| 59 | [BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) | 3 | CAP-0013 | OSS95-N03, OSS95-N28 | MIT | SOURCE_MOVED |
| 60 | [plankanban/planka](https://github.com/plankanban/planka) | 3 | CAP-0100 | OSS95-N14, OSS95-N06 | NOASSERTION | Riferimento |
| 61 | [kanboard/kanboard](https://github.com/kanboard/kanboard) | 3 | CAP-0105, CAP-0100 | OSS95-N14 | MIT | Riferimento |
| 62 | [AnkiDroid/Anki-Android](https://github.com/AnkiDroid/Anki-Android) | 3 | CAP-0112, CAP-0144 | OSS95-N24 | GPL-3.0 | Riferimento |
| 63 | [ankitects/anki](https://github.com/ankitects/anki) | 2 | CAP-0112 | OSS95-N24 | NOASSERTION | Riferimento |
| 64 | [memrynote/memry](https://github.com/memrynote/memry) | 5 | CAP-0029, CAP-0148 | OSS95-N07, OSS95-N24, OSS95-N15 | AGPL-3.0 | Riferimento |
| 65 | [Pikos-App/pikos](https://github.com/Pikos-App/pikos) | 5 | CAP-0004, CAP-0002 | OSS95-N15, OSS95-N34, OSS95-N40 | NOASSERTION | Riferimento |
| 66 | [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 3 | CAP-0031, CAP-0085 | OSS95-N38 | MIT | Riferimento |
| 67 | [cryptpad/cryptpad](https://github.com/cryptpad/cryptpad) | 3 | CAP-0100 | OSS95-N08, OSS95-N07 | AGPL-3.0 | Riferimento |
| 68 | [markmap/markmap](https://github.com/markmap/markmap) | 3 | CAP-0098, CAP-0149, CAP-0120 | — | MIT | Riferimento |
| 69 | [JerryZLiu/Dayflow](https://github.com/JerryZLiu/Dayflow) | 3 | CAP-0101 | OSS95-N16, OSS95-N35 | MIT | Riferimento |
| 70 | [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | 3 | CAP-0108 | OSS95-N16, OSS95-N35 | MPL-2.0 | Riferimento |
| 71 | [wakatime/wakatime-cli](https://github.com/wakatime/wakatime-cli) | 2 | — | OSS95-N17, OSS95-N35 | BSD-3-Clause | Riferimento |
| 72 | [projecthamster/hamster](https://github.com/projecthamster/hamster) | 2 | CAP-0108 | OSS95-N35 | GPL-3.0 | Riferimento |
| 73 | [jazzband/Watson](https://github.com/jazzband/Watson) | 2 | CAP-0108 | OSS95-N35 | MIT | Riferimento |
| 74 | [todotxt/todo.txt-cli](https://github.com/todotxt/todo.txt-cli) | 3 | CAP-0075, CAP-0096 | OSS95-N21 | GPL-3.0 | Riferimento |
| 75 | [GothenburgBitFactory/taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior) | 3 | CAP-0096, CAP-0105 | OSS95-N21 | MIT | Riferimento |
| 76 | [mattgemmell/TaskPaperRuby](https://github.com/mattgemmell/TaskPaperRuby) | 3 | CAP-0075, CAP-0096 | OSS95-N21 | MIT | Riferimento |
| 77 | [bzg/org-mode](https://github.com/bzg/org-mode) | 3 | CAP-0096, CAP-0150 | OSS95-N21 | GPL-3.0 | MIRROR_ONLY |
| 78 | [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki) | 3 | CAP-0013 | OSS95-N02, OSS95-N33 | NOASSERTION | Riferimento |
| 79 | [dnote/dnote](https://github.com/dnote/dnote) | 3 | CAP-0013 | OSS95-N20, OSS95-N21 | Apache-2.0 | Riferimento |
| 80 | [massCodeIO/massCode](https://github.com/massCodeIO/massCode) | 4 | CAP-0084, CAP-0013 | OSS95-N20, OSS95-N34 | AGPL-3.0 | Riferimento |
| 81 | [gristlabs/grist-core](https://github.com/gristlabs/grist-core) | 3 | CAP-0122 | OSS95-N05, OSS95-N06 | Apache-2.0 | Riferimento |
| 82 | [audreyt/ethercalc](https://github.com/audreyt/ethercalc) | 3 | CAP-0100 | OSS95-N05, OSS95-N06 | NOASSERTION | Riferimento |
| 83 | [mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar) | 3 | CAP-0100 | OSS95-N05, OSS95-N06 | GPL-3.0 | Riferimento |
| 84 | [baserow/baserow](https://github.com/baserow/baserow) | 4 | CAP-0100 | OSS95-N05, OSS95-N06, OSS95-N25 | NOASSERTION | Riferimento |
| 85 | [seatable/seatable](https://github.com/seatable/seatable) | 3 | — | OSS95-N05, OSS95-N06, OSS95-N25 | UNKNOWN | Riferimento |
| 86 | [amark/gun](https://github.com/amark/gun) | 3 | CAP-0100 | OSS95-N26, OSS95-N07 | NOASSERTION | Riferimento |
| 87 | [yjs/yjs](https://github.com/yjs/yjs) | 3 | CAP-0100, CAP-0118 | OSS95-N07 | NOASSERTION | Riferimento |
| 88 | [automerge/automerge](https://github.com/automerge/automerge) | 3 | CAP-0100, CAP-0118 | OSS95-N07 | MIT | Riferimento |
| 89 | [berty/berty](https://github.com/berty/berty) | 3 | CAP-0100 | OSS95-N26, OSS95-N08 | NOASSERTION | Riferimento |
| 90 | [ankicommunity/ankicommunity-sync-server](https://github.com/ankicommunity/ankicommunity-sync-server) | 2 | CAP-0112 | OSS95-N26 | AGPL-3.0 | OLD_PROTOCOL_WARNING |
| 91 | [zotero/zotero](https://github.com/zotero/zotero) | 3 | CAP-0119, CAP-0076 | OSS95-N29 | NOASSERTION | Riferimento |
| 92 | [espanso/espanso](https://github.com/espanso/espanso) | 3 | — | OSS95-N19, OSS95-N18, OSS95-N20 | GPL-3.0 | Riferimento |
| 93 | [writefreely/writefreely](https://github.com/writefreely/writefreely) | 3 | CAP-0013 | OSS95-N28, OSS95-N08 | AGPL-3.0 | Riferimento |
| 94 | [codex-team/editor.js](https://github.com/codex-team/editor.js) | 3 | CAP-0118 | OSS95-N01, OSS95-N34 | Apache-2.0 | Riferimento |
| 95 | [Milkdown/milkdown](https://github.com/Milkdown/milkdown) | 3 | CAP-0118 | OSS95-N01, OSS95-N34 | MIT | Riferimento |

## Conclusioni operative e priorità

- **P1 — completare contratti approvati:** Notes CAP-0148 Smart Inbox e CAP-0103/0106 Project Intelligence, senza saltare le issue/QA.
- **P2 — promuovere solo responsabilità E0 realmente distinte:** N02 wikilink backlink, N05 formule relazionali, N10 conversione task↔evento, N11 ricorrenza su completamento, N13 sprint, N21 task plain-text. Scelta per-app dopo verifica Product Bible.
- **P2 — contenere lo scope:** N01 editor, N06 viste, N15 timeboxing, N25 automazioni, N35 timesheet come estensioni già parzialmente supportate.
- **P2 con gate architetturali obbligatori:** N07 CRDT, N08 condivisione cifrata, N09 CalDAV, N16 tracking attività, N19 espansione globale, N26 P2P, N32 frase di recupero, N38 audio di sistema. Nessun provider/permesso aggiunto per questa ricerca.
- **P3 — interesse per altre app:** N20 snippet per CmdPocket; N23/N24 gamification/serie per FocuSense; N34 command palette; N37 NFC opzionale.
- I livelli reali di licenza, test, runtime, consumo RAM/APK e supporto Flutter non sono dimostrati dai README. Un donor richiede path/commit, limiti, license review, E2/E3 e gate consumer.

**Prossimo ingresso CAP ufficiale:** proporre N02 o N01 dopo deduplicazione contrattuale, fissare evidenze esatte e costruire 6 file del kit tecnico; non “promuovere” automaticamente tutte le 39 idee. Il catalogo resta la fonte autorevole per contare le CAP numeriche.
