# Piano di verifica — CAP-0103

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Grafo delle dipendenze e blocker delle task**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Audit CAP-0096 e canvas CAP-0028; relazioni no-cicli, cancellazione/ripristino, undo, accessibilita e filtri; il donor Yuga modella dipendenze in forma sequenziale.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
