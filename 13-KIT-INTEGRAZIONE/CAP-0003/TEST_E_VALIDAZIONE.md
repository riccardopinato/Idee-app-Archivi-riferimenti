# Piano di verifica — CAP-0003

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Preparazione contestuale appuntamento**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Collaudo fisico +116 V116-06…V116-10 e V116-12: note, checklist, conflitti, Trash, offline e lingue; CI e APK firmato non equivalgono a DEVICE_PASS.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
