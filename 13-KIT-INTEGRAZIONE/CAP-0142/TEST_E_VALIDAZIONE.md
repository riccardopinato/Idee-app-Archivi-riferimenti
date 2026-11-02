# Test candidati — CAP-0142

- Cambio orologio/timeout/DST, backup restore e annullamento, open in anticipo dopo consenso, coppia disconnessa e rimozione partner.
- Regressione: record vecchi/dati presenti, annulla/riprova, restore, locale, offline e accessibilità.
- Performance: footprint APK, batteria, storage e RAM solo se pertinenti al comportamento.
- Sicurezza: Nessuna garanzia crittografica del blocco temporale. QA date/fusi/offline/orologio, backup e sync due device; shared dopo Privacy #215.
- Evidenze necessarie: source SHA, test puntuali, Flutter analyze, CI exact-head, artifact e test fisico distinto da Web/CI.

**Esito al 02/11/2026:** IDEAZIONE SOLTANTO; NESSUN TEST IMPLEMENTAZIONE ESEGUITO.
