# Piano di verifica — CAP-0097

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Project Memory con Q&A circoscritto e provenance**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Partire da filtri e FTS locale esistenti; ricerca semantica solo opt-in/on-device se giustificata; citazioni verificabili e isolamento tra progetti.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
