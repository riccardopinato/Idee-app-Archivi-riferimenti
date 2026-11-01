# Piano di verifica — CAP-0106

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Rilevamento sovraccarico e heatmap riunioni**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Audit calendar provider, permessi, CAP-0001 e CAP-0101; calcolare solo su dati disponibili e consenso, evitare falsa precisione su durata task e false promesse di sync.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
