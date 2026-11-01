# Piano di verifica — CAP-0120

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Testi alternativi accessibili per immagini delle note**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Il demo usa modelli BLIP/servizi che possono essere pesanti; l'accessibilita non equivale a certificazione WCAG. Test con screen reader. Verificare architettura e licensing nel Product Bible prima di integrare.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
