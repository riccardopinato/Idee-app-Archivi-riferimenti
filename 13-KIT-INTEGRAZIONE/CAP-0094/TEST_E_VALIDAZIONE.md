# Piano di verifica — CAP-0094

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Sticky Kanban con task canoniche su canvas e planner**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Verificare modelli e canvas attuali, riusare post-it/task, garantire update unico, undo e sync; non usare come donor il link MiniMax-M1 non pertinente.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
