# Piano di verifica — CAP-0101

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Dashboard produttivita locale da task canoniche**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Verificare report gia esistenti; calcolare su task non cestinate; metriche semplici e leggibili con limiti e no analytics privacy-invasive.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
