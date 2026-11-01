# Piano di verifica — CAP-0110

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Avvio guidato micro-passo e focus breve**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Usare CAP-0109 e CAP-0096; template locali senza AI obbligatoria, scelta editabile e nessuna sovrascrittura della nota; test accessibilita e interruzione.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
