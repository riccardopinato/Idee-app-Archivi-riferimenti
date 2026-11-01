# Piano di verifica — CAP-0109

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Sessioni Focus/Pomodoro collegate a note e protezione opzionale**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riutilizzare eventuali timer FocusSense prima del codice; persistenza dopo app pause, gestione lifecycle e background Android, DND soltanto con permesso/azione esplicita; non promettere blocco siti.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
