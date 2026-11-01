# Piano di verifica — CAP-0090

- Input ordinario, vuoto, grande, corrotto, duplicato; risultato specifico: **Controllo scope creep e dipendenze nelle PR**.
- Nessuna mutazione senza consenso; annulla, ripristino, rollback, dati e media originali preservati.
- Offline, autorizzazioni negate, dipendenze/modello assenti, errori runtime e riavvio.
- Traduzioni, leggibilità, accessibilità, font scaling, compatibilità con app esistente.
- Prestazioni, RAM, footprint APK, storage e batteria quando pertinenti.
- QA: `flutter analyze`, test, build, CI exact-head, smoke e dispositivo fisico dove richiesto.

## Gate specifico

Verificare se AppLab copre gia la stessa responsabilita: solo gate advisory a diff bounded confrontato con PR scope, niente agente ulteriore o trigger duplicati. Controllare licenza di ogni skill e le sue dipendenze.

**Evidenze ancora da produrre:** SHA target, tests PASS, runtime/device, licenze donor. Questa checklist NON certifica alcun test.
