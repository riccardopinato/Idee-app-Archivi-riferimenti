# Piano di verifica — CAP-0086

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Sintesi vocale locale di note e contenuti editoriali**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Prima valutare Android TextToSpeech sistema e licenze voci; modelli scaricabili solo opt-in; VoiceStudio AGPL: pattern solo, no code copy closed-source; nessuna imitazione vocale senza consenso.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
