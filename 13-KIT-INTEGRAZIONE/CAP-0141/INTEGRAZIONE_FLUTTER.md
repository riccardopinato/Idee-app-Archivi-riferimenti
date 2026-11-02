# Piano di integrazione Flutter — CAP-0141

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/screens/shared_space.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Catalogo locale versionato, due risposte per domanda, stato di reveal consensuale, sessione disconnessa e retry idempotente.
4. Collegare flusso ai dati e servizi canonici: Noi condiviso, catalogo domande locale, autenticazione solo per collaborazione, policy visibilità e versioning.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

Non approvata in roadmap. Prima validare con due account/device, disclosure in cache/push/feed, revoca e privacy #215 ON HOLD; nessuna E2EE implicita.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
