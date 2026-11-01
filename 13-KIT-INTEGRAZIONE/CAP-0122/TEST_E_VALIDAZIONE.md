# Piano di verifica — CAP-0122

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Estrazione di tabelle strutturate da immagini e PDF**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Paper2Any include extraction di tabelle in PPT, non un modulo Flutter pronto; integrare con CAP-0035 OCR locale e validazione cellule. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
