# Piano di verifica — CAP-0135

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Raccolta delle prove a favore e contro una tesi**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Dataset ClaimReview2025Q4 non risolto nel controllo: conservare il riferimento originale e cercare alternative verificabili prima di donorship. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
