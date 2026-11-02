# Piano di integrazione Flutter — CAP-0143

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/shared_invite_qr.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Prima fase offline: PNG/PDF derivato da elemento selezionato. Seconda fase Web/PWA richiede token opaco revocabile e revisione destinatario.
4. Collegare flusso ai dati e servizi canonici: Export safe-copy, QR esistenti per inviti (non equivalenti), eventuale servizio token con scadenza e autorizzazione.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

Blocco disclosure pubblica: mai pubblicare contenuto privato automaticamente. Security review token/noindex/EXIF/URL leak/revoca, termini hosting e Privacy #215.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
