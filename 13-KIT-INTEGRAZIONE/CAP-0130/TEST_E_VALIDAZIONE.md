# Piano di verifica — CAP-0130

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Generazione di slide e figure tecniche modificabili**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Paper2Any dichiara Paper2PPT e licenza Apache-2.0, ma la demo pubblica era in errore; il backend/AI non va importato automaticamente. | Paper2Any dichiara Paper2Figure e Paper2PPT nella stessa codebase; registrata come modalita dello stesso CAP di Notes-to-Slides. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
