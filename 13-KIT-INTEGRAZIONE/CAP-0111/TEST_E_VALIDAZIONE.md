# Piano di verifica — CAP-0111

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Weekly Review con proposte di pulizia e ripianificazione**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riutilizzare dashboard CAP-0101, scheduler esistente e lifecycle; nessuna cancellazione o ripianificazione automatica; Anna in forma Today/diario non PM suite.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
