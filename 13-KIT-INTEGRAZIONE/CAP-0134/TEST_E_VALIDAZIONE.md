# Piano di verifica — CAP-0134

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Triage e categorizzazione documenti importati**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

DocRex Apache-2.0, ~5,8 MB FP32, solo bank_statement/invoice/other, int8 1,7 MB non raccomandato; serve test su documenti italiani. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
