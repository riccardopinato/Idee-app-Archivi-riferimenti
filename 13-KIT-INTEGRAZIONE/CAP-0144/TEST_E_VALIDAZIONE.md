# Test candidati — CAP-0144

- Tap deep-link idempotente, sync aggiornamenti/differenza OS, widget scaduto e offline, redazione contenuti riservati, revoca foto, reinstall/backup, small widgets.
- Regressione: record vecchi/dati presenti, annulla/riprova, restore, locale, offline e accessibilità.
- Performance: footprint APK, batteria, storage e RAM solo se pertinenti al comportamento.
- Sicurezza: Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata.
- Evidenze necessarie: source SHA, test puntuali, Flutter analyze, CI exact-head, artifact e test fisico distinto da Web/CI.

**Esito al 02/11/2026:** IDEAZIONE SOLTANTO; NESSUN TEST IMPLEMENTAZIONE ESEGUITO.
