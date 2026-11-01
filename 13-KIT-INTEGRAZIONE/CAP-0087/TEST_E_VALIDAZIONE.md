# Piano di verifica — CAP-0087

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Layer geografici pubblici con freshness e fallback**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Per ogni feed dichiarare API, diritti commerciali, refresh, intervalli, limiti, simulazioni e disponibilita; nessuna navigazione operativa o allerta emergenza da data feed incompleti. Repo metadata NOASSERTION: verify license per file.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
