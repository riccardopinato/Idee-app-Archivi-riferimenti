# Piano di verifica — CAP-0113

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Da appuntamento passato a ricordo privato**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Collaudo fisico APK +116 V116-03…V116-05: annulla senza scrivere, anti-duplicato, Trash/restore e privacy; valutare riuso Wonderlog senza duplicare il diario.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
