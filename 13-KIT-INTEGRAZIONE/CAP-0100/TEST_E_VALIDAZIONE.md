# Piano di verifica — CAP-0100

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Kanban collaborativa task e permessi per workspace**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Non anticipare il Team roadmap; design-only finche identita/ACL/sync non sono approvati; nessuna condivisione implicita di note private; WebTestBench non e donor Kanban.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
