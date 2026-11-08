# Stelle — audit incrementale OSS95 e ammissione al prodotto · 8 novembre 2026

**Input:** 95 repository già curate e fornite in chat; **NON** un nuovo elenco autenticato di stelle GitHub. L'endpoint `user/starred` non è disponibile nella connessione. Nessun nuovo repository starred può essere confermato.

**Baseline Factory:** `App-Factory-Core@c709e483d40424c88b6ba316d0c8352eec5370fe`. **Registro:** 199 CAP / 441 associazioni, invariati. 39 CAP OSS95 E0 / 56 associazioni valutate, tutte con stato tecnico `PROPOSTA` e decisione del product owner `DA_VALUTARE`.

**Confronto sorgenti:** [snapshot 95 repo](OSS95_SOURCE_SNAPSHOT_2026-11-08.json). 95 metadati repository controllati; 85 date `pushed_at` invariate; 10 mutate; SHA blob dei README di tutte le dieci invariato. I titoli degli ultimi commit sono stati esaminati, **non** tutti i diff di codice. Non è provata alcuna capability nuova da questa scansione; non significa che tutto il codice sia invariato.

**Consumer controllati:** Notes `d99a30633134e6e800e93e2a04741554d38c839b`, Anna `e5b956caf7976b70afe8269fe55697f2af21c568`, FocuSense `bdc8becfff1b1a5f629456deb34170f0d905d8b7`, PDF-Unifier `3aacb3e2ac4822db4601fe5c217c016cecc6cbf4`. CmdPocket e Work-Time-Keeper 404 ai nomi censiti.

## Raccomandazioni per CAP (non decisioni approvate)

| Esito audit | CAP |
| --- | ---: |
| PROPORRE_APPROVAZIONE | 7 |
| ACCORPARE | 10 |
| RINVIARE_CONSIGLIATO | 11 |
| BLOCCATO | 3 |
| FUORI_SCOPE_CONSIGLIATO | 8 |
| **Totale** | **39** |

| ID | Descrizione | Esito prevalente | Motivazione |
| --- | --- | --- | --- |
| CAP-0161 | Editor ricco a blocchi con round-trip Markdown reversibile | ACCORPARE | Editor a blocchi e Markdown già esistenti in Notes; fare soltanto un test mirato sul round-trip senza perdita. |
| CAP-0162 | Wikilink, backlink e rinomina dei link con riparazione | PROPORRE_APPROVAZIONE | Knowledge Graph/wikilink già presenti: valore incrementale nella rinomina e riparazione sicura dei backlink. |
| CAP-0163 | Note gerarchiche, alias e transclusioni controllate | ACCORPARE | Knowledge Graph e Synced Blocks già coprono buona parte della semantica di alias/transclusione. |
| CAP-0164 | Query e scripting locale su note e knowledge base | RINVIARE_CONSIGLIATO | Script/query locali richiedono sandbox, controllo permessi e domanda utente concreta. |
| CAP-0165 | Tabelle relazionali e campi calcolati/formule | RINVIARE_CONSIGLIATO | Properties e viste Tabella già esistono; formule/relazioni introducono elevata complessità di schema. |
| CAP-0166 | Viste salvate con filtri, raggruppamenti e permessi | ACCORPARE | Viste Lista/Board/Tabella/Calendario/Timeline esistenti; aggiungere filtri salvati come delta. |
| CAP-0167 | Convergenza CRDT per modifiche concorrenti offline | FUORI_SCOPE_CONSIGLIATO | Roadmap Notes non autorizza un secondo sync CRDT. |
| CAP-0168 | Condivisione cifrata selettiva e revoca per documento | RINVIARE_CONSIGLIATO | Revoca cifrata per documento richiede threat model, ACL e key rotation. |
| CAP-0169 | Sincronizzazione CalDAV bidirezionale opt-in | BLOCCATO | Google Calendar Direct #199 è DRAFT e il calendario esterno Anna è attualmente read-only. |
| CAP-0170 | Conversione esplicita evento↔attività senza duplicati | PROPORRE_APPROVAZIONE | Conversione task-evento utile, ma ID, owner e reminder devono restare canonici. |
| CAP-0171 | Ricorrenza calcolata da scadenza o completamento | PROPORRE_APPROVAZIONE | Ricorrenza dalla data di completamento è un caso distinto; verificare DST, timezone e idempotenza. |
| CAP-0172 | Rotazione equa degli assegnatari nelle attività condivise | RINVIARE_CONSIGLIATO | Assegnazione a rotazione utile solo per task condivisi leggeri, non una suite di project management. |
| CAP-0173 | Sprint, cicli e retrospettive di progetto | RINVIARE_CONSIGLIATO | Sprint/retrospettive allargano lo scope Notes prima della chiusura dei P1. |
| CAP-0174 | Limiti WIP e swimlane Kanban configurabili | ACCORPARE | Workload Guard e vista Board già trattano WIP/blocked reasons: evitare motore parallelo. |
| CAP-0175 | Timeboxing drag-and-drop sul calendario | PROPORRE_APPROVAZIONE | Timeboxing nelle viste Calendario/Timeline Notes aumenta utilità con costo limitato. |
| CAP-0176 | Timeline attività automatica con AFK e consenso | FUORI_SCOPE_CONSIGLIATO | Activity tracking/AFK introduce raccolta comportamentale fuori dalle funzioni focus correnti. |
| CAP-0177 | Tracciamento attività IDE tramite plugin opt-in | BLOCCATO | I consumer Work-Time-Keeper e CmdPocket non sono accessibili ai nomi di repository censiti. |
| CAP-0178 | Espansione abbreviazioni solo nell'editor corrente | ACCORPARE | Template in-editor Notes già esistenti; usare una estensione reversibile. |
| CAP-0179 | Espansione testo a livello di sistema operativo | BLOCCATO | Text expander globale comporta hook sistema/accessibilità, consumer CmdPocket non verificato. |
| CAP-0180 | Archivio snippet di codice con linguaggi e frammenti | RINVIARE_CONSIGLIATO | Snippet riutilizzabili potrebbero derivare da code block, tag e template senza nuovo vault. |
| CAP-0181 | Import/export lossless di todo.txt, Org e TaskPaper | PROPORRE_APPROVAZIONE | todo.txt/Org/TaskPaper migliora portabilità, previa analisi lossiness e conflitti. |
| CAP-0182 | Finestre sticky giornaliere/settimanali per desktop | RINVIARE_CONSIGLIATO | Widget desktop sticky non prioritario rispetto a rilascio/QA Android Anna. |
| CAP-0183 | Punti, ricompense e progressione volontaria delle task | ACCORPARE | FocuSense possiede già XP, badge e progressione; Notes non ha una decisione prodotto analoga. |
| CAP-0184 | Serie abitudini e obiettivi di continuità con storico | ACCORPARE | FocuSense possiede già streak; per Anna manca un mandato su habit tracking. |
| CAP-0185 | Regole di automazione tipizzate trigger→azione con preview | ACCORPARE | Workflow automations evento→azione già presenti in Notes: isolare soltanto preview tipizzate mancanti. |
| CAP-0186 | Trasporto decentralizzato P2P per dati condivisi cifrati | FUORI_SCOPE_CONSIGLIATO | P2P cifrato introdurrebbe un secondo trasporto di sync e maggiore superficie di rischio. |
| CAP-0187 | Editing Typst/matematica con anteprima verificabile | RINVIARE_CONSIGLIATO | Typst/matematica richiede domanda Studio verificata e footprint misurato. |
| CAP-0188 | Pubblicazione controllata Markdown/wiki con redazione | FUORI_SCOPE_CONSIGLIATO | Pubblicazione wiki pubblica comporta hosting e privacy esterni allo scope Notes corrente. |
| CAP-0189 | Biblioteca citazioni e riferimenti bibliografici | PROPORRE_APPROVAZIONE | Libreria bibliografica supera l'attuale audit di provenienza e migliora il workflow Studio. |
| CAP-0190 | Da evidenziazioni PDF a note collegate e storylines | PROPORRE_APPROVAZIONE | Evidenziazioni PDF collegate a note e pagine migliorano Study/Documents con provenance. |
| CAP-0191 | Editor multipannello con due note e split sincronizzato | RINVIARE_CONSIGLIATO | Split editor comporta complessità responsive; rimandare dopo flussi e QA prioritari. |
| CAP-0192 | Recupero account cifrato con frase mnemonica senza email | FUORI_SCOPE_CONSIGLIATO | Frase di recupero crittografica richiede architettura e threat model non approvati. |
| CAP-0193 | Diario testuale portable e operazioni CLI per data | FUORI_SCOPE_CONSIGLIATO | CLI per diario personale è incoerente con Anna mobile-first; CmdPocket non verificato. |
| CAP-0194 | Command palette e scorciatoie tastiera contestuali | ACCORPARE | Quick Switcher e scorciatoie Notes esistono; estendere invece di ricostruire. |
| CAP-0195 | Timesheet esportabili e report settimanali per progetto | RINVIARE_CONSIGLIATO | Timesheet derivabili da Focus, ma reporting professionale non è una priorità verificata. |
| CAP-0196 | Archivio documenti indicizzato con classificazione e retention | ACCORPARE | Documents/indicizzazione presenti in Notes; la retention avanzata va definita nello stesso layer. |
| CAP-0197 | Marcatura attività tramite NFC volontario | RINVIARE_CONSIGLIATO | NFC introduce hardware e permessi per un caso d'uso non ancora validato. |
| CAP-0198 | Cattura audio di sistema e trascrizione locale consensuale | FUORI_SCOPE_CONSIGLIATO | Cattura audio di sistema richiede permessi, consenso terzi e verifiche Android/OEM. |
| CAP-0199 | Interfaccia MCP/API locale per lettura controllata di agenda e task | FUORI_SCOPE_CONSIGLIATO | API/MCP locale introduce una nuova superficie di accesso a dati personali. |

## Matrice delle 56 associazioni per app

| CAP | App | Raccomandazione | Motivazione |
| --- | --- | --- | --- |
| CAP-0161 | Notes-Ecosistema | ACCORPARE | Editor a blocchi e Markdown già esistenti in Notes; fare soltanto un test mirato sul round-trip senza perdita. |
| CAP-0162 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Knowledge Graph/wikilink già presenti: valore incrementale nella rinomina e riparazione sicura dei backlink. |
| CAP-0163 | Notes-Ecosistema | ACCORPARE | Knowledge Graph e Synced Blocks già coprono buona parte della semantica di alias/transclusione. |
| CAP-0164 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Script/query locali richiedono sandbox, controllo permessi e domanda utente concreta. |
| CAP-0165 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Properties e viste Tabella già esistono; formule/relazioni introducono elevata complessità di schema. |
| CAP-0166 | Notes-Ecosistema | ACCORPARE | Viste Lista/Board/Tabella/Calendario/Timeline esistenti; aggiungere filtri salvati come delta. |
| CAP-0167 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | Roadmap Notes non autorizza un secondo sync CRDT. |
| CAP-0168 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Revoca cifrata per documento richiede threat model, ACL e key rotation. |
| CAP-0169 | Agenda-per-Anna | BLOCCATO | Google Calendar Direct #199 è DRAFT e il calendario esterno Anna è attualmente read-only. |
| CAP-0170 | Agenda-per-Anna | PROPORRE_APPROVAZIONE | Conversione task-evento utile, ma ID, owner e reminder devono restare canonici. |
| CAP-0170 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Conversione task-evento utile, ma ID, owner e reminder devono restare canonici. |
| CAP-0171 | Agenda-per-Anna | PROPORRE_APPROVAZIONE | Ricorrenza dalla data di completamento è un caso distinto; verificare DST, timezone e idempotenza. |
| CAP-0171 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Ricorrenza dalla data di completamento è un caso distinto; verificare DST, timezone e idempotenza. |
| CAP-0172 | Agenda-per-Anna | RINVIARE_CONSIGLIATO | Assegnazione a rotazione utile solo per task condivisi leggeri, non una suite di project management. |
| CAP-0172 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Assegnazione a rotazione utile solo per task condivisi leggeri, non una suite di project management. |
| CAP-0173 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Sprint/retrospettive allargano lo scope Notes prima della chiusura dei P1. |
| CAP-0174 | Notes-Ecosistema | ACCORPARE | Workload Guard e vista Board già trattano WIP/blocked reasons: evitare motore parallelo. |
| CAP-0175 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Timeboxing nelle viste Calendario/Timeline Notes aumenta utilità con costo limitato. |
| CAP-0175 | Agenda-per-Anna | ACCORPARE | Timeboxing nelle viste Calendario/Timeline Notes aumenta utilità con costo limitato. |
| CAP-0176 | Work-Time-Keeper | BLOCCATO | Activity tracking/AFK introduce raccolta comportamentale fuori dalle funzioni focus correnti. |
| CAP-0176 | FocuSense | FUORI_SCOPE_CONSIGLIATO | Activity tracking/AFK introduce raccolta comportamentale fuori dalle funzioni focus correnti. |
| CAP-0177 | Work-Time-Keeper | BLOCCATO | I consumer Work-Time-Keeper e CmdPocket non sono accessibili ai nomi di repository censiti. |
| CAP-0177 | CmdPocket | BLOCCATO | I consumer Work-Time-Keeper e CmdPocket non sono accessibili ai nomi di repository censiti. |
| CAP-0178 | Notes-Ecosistema | ACCORPARE | Template in-editor Notes già esistenti; usare una estensione reversibile. |
| CAP-0178 | CmdPocket | BLOCCATO | Template in-editor Notes già esistenti; usare una estensione reversibile. |
| CAP-0179 | CmdPocket | BLOCCATO | Text expander globale comporta hook sistema/accessibilità, consumer CmdPocket non verificato. |
| CAP-0180 | CmdPocket | BLOCCATO | Snippet riutilizzabili potrebbero derivare da code block, tag e template senza nuovo vault. |
| CAP-0180 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Snippet riutilizzabili potrebbero derivare da code block, tag e template senza nuovo vault. |
| CAP-0181 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | todo.txt/Org/TaskPaper migliora portabilità, previa analisi lossiness e conflitti. |
| CAP-0182 | Agenda-per-Anna | RINVIARE_CONSIGLIATO | Widget desktop sticky non prioritario rispetto a rilascio/QA Android Anna. |
| CAP-0183 | FocuSense | ACCORPARE | FocuSense possiede già XP, badge e progressione; Notes non ha una decisione prodotto analoga. |
| CAP-0183 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | FocuSense possiede già XP, badge e progressione; Notes non ha una decisione prodotto analoga. |
| CAP-0184 | FocuSense | ACCORPARE | FocuSense possiede già streak; per Anna manca un mandato su habit tracking. |
| CAP-0184 | Agenda-per-Anna | RINVIARE_CONSIGLIATO | FocuSense possiede già streak; per Anna manca un mandato su habit tracking. |
| CAP-0185 | Notes-Ecosistema | ACCORPARE | Workflow automations evento→azione già presenti in Notes: isolare soltanto preview tipizzate mancanti. |
| CAP-0186 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | P2P cifrato introdurrebbe un secondo trasporto di sync e maggiore superficie di rischio. |
| CAP-0187 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Typst/matematica richiede domanda Studio verificata e footprint misurato. |
| CAP-0188 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | Pubblicazione wiki pubblica comporta hosting e privacy esterni allo scope Notes corrente. |
| CAP-0189 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Libreria bibliografica supera l'attuale audit di provenienza e migliora il workflow Studio. |
| CAP-0190 | Notes-Ecosistema | PROPORRE_APPROVAZIONE | Evidenziazioni PDF collegate a note e pagine migliorano Study/Documents con provenance. |
| CAP-0191 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Split editor comporta complessità responsive; rimandare dopo flussi e QA prioritari. |
| CAP-0192 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | Frase di recupero crittografica richiede architettura e threat model non approvati. |
| CAP-0192 | Agenda-per-Anna | FUORI_SCOPE_CONSIGLIATO | Frase di recupero crittografica richiede architettura e threat model non approvati. |
| CAP-0193 | Agenda-per-Anna | FUORI_SCOPE_CONSIGLIATO | CLI per diario personale è incoerente con Anna mobile-first; CmdPocket non verificato. |
| CAP-0193 | CmdPocket | BLOCCATO | CLI per diario personale è incoerente con Anna mobile-first; CmdPocket non verificato. |
| CAP-0194 | Notes-Ecosistema | ACCORPARE | Quick Switcher e scorciatoie Notes esistono; estendere invece di ricostruire. |
| CAP-0194 | CmdPocket | BLOCCATO | Quick Switcher e scorciatoie Notes esistono; estendere invece di ricostruire. |
| CAP-0195 | Work-Time-Keeper | BLOCCATO | Timesheet derivabili da Focus, ma reporting professionale non è una priorità verificata. |
| CAP-0195 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | Timesheet derivabili da Focus, ma reporting professionale non è una priorità verificata. |
| CAP-0196 | Notes-Ecosistema | ACCORPARE | Documents/indicizzazione presenti in Notes; la retention avanzata va definita nello stesso layer. |
| CAP-0196 | PDF-Unifier | RINVIARE_CONSIGLIATO | Documents/indicizzazione presenti in Notes; la retention avanzata va definita nello stesso layer. |
| CAP-0197 | Agenda-per-Anna | RINVIARE_CONSIGLIATO | NFC introduce hardware e permessi per un caso d'uso non ancora validato. |
| CAP-0197 | Notes-Ecosistema | RINVIARE_CONSIGLIATO | NFC introduce hardware e permessi per un caso d'uso non ancora validato. |
| CAP-0198 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | Cattura audio di sistema richiede permessi, consenso terzi e verifiche Android/OEM. |
| CAP-0199 | Notes-Ecosistema | FUORI_SCOPE_CONSIGLIATO | API/MCP locale introduce una nuova superficie di accesso a dati personali. |
| CAP-0199 | CmdPocket | BLOCCATO | API/MCP locale introduce una nuova superficie di accesso a dati personali. |

## Gate di ammissione

- **Notes:** [roadmap #60](https://github.com/riccardopinato/Notes-Ecosistema/issues/60), [Smart Inbox #46](https://github.com/riccardopinato/Notes-Ecosistema/issues/46), [Project Intelligence #51](https://github.com/riccardopinato/Notes-Ecosistema/issues/51) restano aperte. Evitare CRDT, secondo planner, cloud/AI non approvati.
- **Anna:** [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/e5b956caf7976b70afe8269fe55697f2af21c568/docs/PRODUCT_BIBLE.md) definisce diario/agenda e calendario esterno read-only; [Google Calendar Direct PR #199](https://github.com/riccardopinato/Agenda-per-Anna/pull/199) ancora DRAFT/DO NOT MERGE.
- **FocuSense:** [Product Bible](https://github.com/riccardopinato/FocuSense/blob/bdc8becfff1b1a5f629456deb34170f0d905d8b7/PRODUCT_BIBLE.md) già include XP, badge e streak. Niente tracking passivo automatico.
- **PDF-Unifier:** consumer repo verificato, Product Bible per espansione archivio non verificata; **CmdPocket/Work-Time-Keeper:** consumer repo non accessibili.
- **Licenze OSS:** tutte le fonti possono essere studiate per la funzionalità; import del codice richiede diritti per-file, compatibilità commerciale e test.
- Le sette CAP proposte per approvazione sono **0162, 0170, 0171, 0175, 0181, 0189, 0190**. Sono raccomandazioni e NON `APPROVATA` né `IN_ROADMAP`.

## Bilancio

0 nuove stelle autenticate; 0 nuove CAP; 0 nuovi kit; 0 associazioni create. **39 raccomandazioni per CAP e 56 per-app** da rispecchiare nel JSON senza alterare decisioni del product owner, roadmap, app, Golden o test di implementazione.

**Criterio per il prossimo ciclo:** usare il checkpoint `OSS95_SOURCE_SNAPSHOT_2026-11-08.json`, confrontare prima la fonte stelle accessibile e fare audit mirato solo di differenze riproducibili. Il `pushed_at` non è un HEAD SHA né una prova funzionale.
