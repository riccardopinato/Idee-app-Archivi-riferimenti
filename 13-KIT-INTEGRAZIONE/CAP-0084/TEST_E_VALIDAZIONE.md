# Piano di verifica — CAP-0084

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Toolbox locale conversioni testo dati e QR**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Selezionare 5 utility davvero richieste (JSON, Base64, URL, UUID, QR) con test input sensibili offline; GPLv3: clean-room o conformita copyleft; evitare duplicazione CmdPocket e PDF-Unifier.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
