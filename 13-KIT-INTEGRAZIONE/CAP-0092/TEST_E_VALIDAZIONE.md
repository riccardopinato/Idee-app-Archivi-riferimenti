# Piano di verifica — CAP-0092

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Cattura task da linguaggio naturale e note**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Verificare capture/task canonici prima di aggiungere parser IT/EN locale; preview, timezone, consenso prima di scheduler, AI solo pack opzionale e niente download automatici.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
