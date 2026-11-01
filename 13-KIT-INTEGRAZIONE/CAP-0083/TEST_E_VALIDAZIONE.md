# Piano di verifica — CAP-0083

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Treemap interattiva dello spazio e selezione sicura**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Scansione progressiva read-only, treemap per dimensione, selezione esplicita, conferma eliminazione o esportazione e rollback ove disponibile. Non replicare accesso MFT/NTFS nel sandbox Android.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
