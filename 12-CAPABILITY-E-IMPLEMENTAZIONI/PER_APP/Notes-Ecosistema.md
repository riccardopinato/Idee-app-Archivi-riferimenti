# Notes-Ecosistema — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0037](../REGISTRO_CAPABILITY/CAP-0037.md) | Operazioni PDF split merge rotate lock | P1 | 98 | PROPOSTA | Verificare motore originale licenza e compatibilita Flutter |
| [CAP-0015](../REGISTRO_CAPABILITY/CAP-0015.md) | Ricerca globale ordinabile e un carattere | P1 | 95 | PROPOSTA | Source gate riportati PASS ma verificare smoke Android |
| [CAP-0017](../REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | P1 | 94 | SOURCE_REPORTED | Regression entita-per-entita e file orfani; niente duplicazione lifecycle |
| [CAP-0093](../REGISTRO_CAPABILITY/CAP-0093.md) | Da note a checklist strutturate | P1 | 94 | PROPOSTA | Audit note/task esistenti, implementare parsing deterministico e preview multi-selezione; dataset NC reference only, test su ambiguita e nessuna creazione implicita. |
| [CAP-0035](../REGISTRO_CAPABILITY/CAP-0035.md) | OCR immagini e documenti on device | P1 | 92 | PROPOSTA | Audit licenza ML Kit e processi media originali |
| [CAP-0028](../REGISTRO_CAPABILITY/CAP-0028.md) | Connettori visuali tra post-it | P2 | 91 | PROPOSTA | Riutilizzare canvas esistente e salvare soli edge |
| [CAP-0018](../REGISTRO_CAPABILITY/CAP-0018.md) | Backup restore con staging e rollback | P2 | 90 | SOURCE_REPORTED | Audit formati e test corrupt archive per consumer |
| [CAP-0027](../REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | P2 | 90 | PROPOSTA | Android share intent e consenso senza import occulto |
| [CAP-0071](../REGISTRO_CAPABILITY/CAP-0071.md) | Offline content packs incremental sync | P2 | 90 | SOURCE_REPORTED | Licenze e hashing versioni pack |
| [CAP-0092](../REGISTRO_CAPABILITY/CAP-0092.md) | Cattura task da linguaggio naturale e note | P2 | 90 | PROPOSTA | Verificare capture/task canonici prima di aggiungere parser IT/EN locale; preview, timezone, consenso prima di scheduler, AI solo pack opzionale e niente download automatici. |
| [CAP-0084](../REGISTRO_CAPABILITY/CAP-0084.md) | Toolbox locale conversioni testo dati e QR | P2 | 89 | PROPOSTA | Selezionare 5 utility davvero richieste (JSON, Base64, URL, UUID, QR) con test input sensibili offline; GPLv3: clean-room o conformita copyleft; evitare duplicazione CmdPocket e PDF-Unifier. |
| [CAP-0013](../REGISTRO_CAPABILITY/CAP-0013.md) | Collection e ricerca locale | P2 | 88 | PROPOSTA | Verificare performance e origine dei risultati |
| [CAP-0016](../REGISTRO_CAPABILITY/CAP-0016.md) | Inbox con categorie modificabili | P2 | 88 | PROPOSTA | Smoke fisico categoria vuota riavvio e sync |
| [CAP-0020](../REGISTRO_CAPABILITY/CAP-0020.md) | Shared Ecosystem Bridge COPY LINK | P2 | 88 | PROPOSTA | Verificare roundtrip reale e contratti consumer per versione |
| [CAP-0004](../REGISTRO_CAPABILITY/CAP-0004.md) | Overlay calendari esterni read-only | P2 | 87 | ROADMAP_STORICA | Verificare Android Calendar Provider e disponibilità Notes |
| [CAP-0005](../REGISTRO_CAPABILITY/CAP-0005.md) | Esportazione esplicita eventi verso calendario | P2 | 87 | ROADMAP_STORICA | Verificare provider permessi e intent senza sync bidirezionale |
| [CAP-0002](../REGISTRO_CAPABILITY/CAP-0002.md) | Creazione eventi da linguaggio naturale | P2 | 86 | PROPOSTA | Parser EN IT ES FR PT con conferma e timezone |
| [CAP-0031](../REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | P2 | 86 | PROPOSTA | Licenza modello footprint benchmark 5 lingue e download opt-in |
| [CAP-0094](../REGISTRO_CAPABILITY/CAP-0094.md) | Sticky Kanban con task canoniche su canvas e planner | P2 | 85 | PROPOSTA | Verificare modelli e canvas attuali, riusare post-it/task, garantire update unico, undo e sync; non usare come donor il link MiniMax-M1 non pertinente. |
| [CAP-0101](../REGISTRO_CAPABILITY/CAP-0101.md) | Dashboard produttivita locale da task canoniche | P2 | 84 | PROPOSTA | Verificare report gia esistenti; calcolare su task non cestinate; metriche semplici e leggibili con limiti e no analytics privacy-invasive. |
| [CAP-0066](../REGISTRO_CAPABILITY/CAP-0066.md) | Trasferimento LAN QR HTTPS fidato | P2 | 83 | PROPOSTA | Pairing fingerprint HTTPS e test rete locale |
| [CAP-0019](../REGISTRO_CAPABILITY/CAP-0019.md) | Store media content addressed e GC | P2 | 81 | SOURCE_REPORTED | Non uniformare database privacy separati |
| [CAP-0029](../REGISTRO_CAPABILITY/CAP-0029.md) | Canvas ibrida sketch sotto note | P2 | 80 | SOURCE_REPORTED | Verificare gesto pennello undo save e restore device |
| [CAP-0095](../REGISTRO_CAPABILITY/CAP-0095.md) | Estrazione decisioni e action items da riunioni | P2 | 79 | PROPOSTA | Conferma umana, privacy meeting/consensi, diarizzazione opzionale, test IT/EN, footprint offline e riferimento Sherlock solo progettuale CC BY-NC-SA. |
| [CAP-0076](../REGISTRO_CAPABILITY/CAP-0076.md) | Web Clip sicuro con provenienza | P3 | 78 | PROPOSTA | Permissions share sheet e URL originale |
| [CAP-0080](../REGISTRO_CAPABILITY/CAP-0080.md) | Document expiry and asset passport | P3 | 78 | PROPOSTA | Non includere segreti/identita in archivio condiviso |
| [CAP-0096](../REGISTRO_CAPABILITY/CAP-0096.md) | Gerarchie task ricorrenze e relazioni alle note | P3 | 78 | PROPOSTA | Audit funzioni task e recurrence gia presenti; non introdurre secondo scheduler o storage; test eccezioni ricorrenza, delete e restore. |
| [CAP-0003](../REGISTRO_CAPABILITY/CAP-0003.md) | Preparazione contestuale appuntamento | P3 | 77 | PROPOSTA | Riutilizzare reminder e note senza nuovo scheduler |
| [CAP-0033](../REGISTRO_CAPABILITY/CAP-0033.md) | Modello Needle 3 on demand Plus | P3 | 76 | SOURCE_REPORTED | Play delivery benchmark e entitlement non auto concesso |
| [CAP-0030](../REGISTRO_CAPABILITY/CAP-0030.md) | Professional Wallet CV attestati QR vCard | P3 | 75 | ROADMAP_STORICA | Integrare Document Workspace senza wallet parallelo |
| [CAP-0075](../REGISTRO_CAPABILITY/CAP-0075.md) | Import Center per migrazioni utenti | P3 | 74 | PROPOSTA | Import validato e non perdere storico |
| [CAP-0098](../REGISTRO_CAPABILITY/CAP-0098.md) | Mind map navigabile derivata da note e documenti | P3 | 74 | PROPOSTA | Riutilizzare canvas e connettori, audit licenza Vertical.ai; evitare dipendenze RAG cloud o Neo4j introdotte solo per il concept. |
| [CAP-0032](../REGISTRO_CAPABILITY/CAP-0032.md) | Indicizzazione ricerca semantica locale | P3 | 73 | PROPOSTA | Modello multilingue licenza footprint e benchmark; non inserire pack base |
| [CAP-0099](../REGISTRO_CAPABILITY/CAP-0099.md) | Planner studio e progetto da obiettivi in checklist | P3 | 73 | PROPOSTA | Riusare note-to-checklist CAP-0093 e planner; niente copia dataset CC BY-NC; generazione sempre come bozza e conferma degli impegni. |
| [CAP-0086](../REGISTRO_CAPABILITY/CAP-0086.md) | Sintesi vocale locale di note e contenuti editoriali | P3 | 72 | PROPOSTA | Prima valutare Android TextToSpeech sistema e licenze voci; modelli scaricabili solo opt-in; VoiceStudio AGPL: pattern solo, no code copy closed-source; nessuna imitazione vocale senza consenso. |
| [CAP-0097](../REGISTRO_CAPABILITY/CAP-0097.md) | Project Memory con Q&A circoscritto e provenance | P3 | 72 | PROPOSTA | Partire da filtri e FTS locale esistenti; ricerca semantica solo opt-in/on-device se giustificata; citazioni verificabili e isolamento tra progetti. |
| [CAP-0085](../REGISTRO_CAPABILITY/CAP-0085.md) | Diarizzazione vocale locale per appunti riunioni | P3 | 70 | PROPOSTA | Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base. |
| [CAP-0074](../REGISTRO_CAPABILITY/CAP-0074.md) | Companion voice note organizer | P3 | 67 | PROPOSTA | No duplicare trascrizione vocale offline |
| [CAP-0100](../REGISTRO_CAPABILITY/CAP-0100.md) | Kanban collaborativa task e permessi per workspace | P3 | 61 | PROPOSTA | Non anticipare il Team roadmap; design-only finche identita/ACL/sync non sono approvati; nessuna condivisione implicita di note private; WebTestBench non e donor Kanban. |

**Totale associazioni:** 39. Non modificare automaticamente la roadmap del prodotto.
