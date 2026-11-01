# Piano di verifica — CAP-0104

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Timeline obiettivi e pianificazione a ritroso**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riutilizzare planner CAP-0099 e task canoniche; date e durate esplicite, vincoli per milestone e opzione backwards come modalita della stessa timeline, non secondo motore.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
