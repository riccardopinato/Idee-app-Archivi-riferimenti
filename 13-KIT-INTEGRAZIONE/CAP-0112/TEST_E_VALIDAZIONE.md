# Piano di verifica — CAP-0112

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Flashcard e ripasso dilazionato collegati alle note**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Riusare note e pianificatore CAP-0099; SRS deterministico, contenuti modificabili, licenza delle skill esterne da verificare; nessun modello AI pesante bundled.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
