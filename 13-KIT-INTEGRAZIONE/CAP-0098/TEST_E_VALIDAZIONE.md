# Piano di verifica — CAP-0098

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Mind map navigabile derivata da note e documenti**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riutilizzare canvas e connettori, audit licenza Vertical.ai; evitare dipendenze RAG cloud o Neo4j introdotte solo per il concept.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
