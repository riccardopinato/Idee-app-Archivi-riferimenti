# Piano di verifica — CAP-0099

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Planner studio e progetto da obiettivi in checklist**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riusare note-to-checklist CAP-0093 e planner; niente copia dataset CC BY-NC; generazione sempre come bozza e conferma degli impegni.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
