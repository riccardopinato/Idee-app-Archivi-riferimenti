# Piano di verifica — CAP-0105

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Prioritizzazione trasparente e matrice Eisenhower**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Controllare priorita/task preesistenti; regole deterministiche configurabili, no score opachi e drag quadranti deve aggiornare le stesse task; evitare classificazioni non richieste.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
