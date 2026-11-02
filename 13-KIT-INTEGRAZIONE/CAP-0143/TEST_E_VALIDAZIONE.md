# Test candidati — CAP-0143

- Link anonimo con/senza token, expired/revoked/rotated, accesso non autorizzato e sharing locale, EXIF, QR, export backup e cancellazione.
- Regressione: record vecchi/dati presenti, annulla/riprova, restore, locale, offline e accessibilità.
- Performance: footprint APK, batteria, storage e RAM solo se pertinenti al comportamento.
- Sicurezza: Blocco disclosure pubblica: mai pubblicare contenuto privato automaticamente. Security review token/noindex/EXIF/URL leak/revoca, termini hosting e Privacy #215.
- Evidenze necessarie: source SHA, test puntuali, Flutter analyze, CI exact-head, artifact e test fisico distinto da Web/CI.

**Esito al 02/11/2026:** IDEAZIONE SOLTANTO; NESSUN TEST IMPLEMENTAZIONE ESEGUITO.
