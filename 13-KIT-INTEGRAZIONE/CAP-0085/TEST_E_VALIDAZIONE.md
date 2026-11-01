# Piano di verifica — CAP-0085

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Diarizzazione vocale locale per appunti riunioni**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
