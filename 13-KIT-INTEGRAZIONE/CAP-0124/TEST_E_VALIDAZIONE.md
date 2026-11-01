# Piano di verifica — CAP-0124

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Scoperta di temi e cluster nell'archivio note**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

BERTopic/UMAP del progetto riguarda progetti UE, non note personali; modelli e footprint da valutare, fallback tag manuali. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
