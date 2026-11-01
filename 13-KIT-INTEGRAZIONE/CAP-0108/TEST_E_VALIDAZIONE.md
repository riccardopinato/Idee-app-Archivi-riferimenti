# Piano di verifica — CAP-0108

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Confronto durata prevista e reale per task**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Provenienza dei tempi, pause e interruzioni, import da focus timer opzionale, no raccolta in background e niente telemetria remota; integrazione CAP-0101.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
