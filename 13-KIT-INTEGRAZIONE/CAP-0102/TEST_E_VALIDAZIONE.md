# Piano di verifica — CAP-0102

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Ripianificazione assistita e confronto piani alternativi**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Verificare task e calendario canonici; strategia locale con vincoli hard/soft e preview delle modifiche, nessuno spostamento o evento scritto senza conferma; fallback no-AI.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
