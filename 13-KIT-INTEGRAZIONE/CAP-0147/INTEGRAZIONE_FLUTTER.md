# Piano di integrazione Flutter — CAP-0147

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/app_shell.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Riordino opzionale 2-3 card già esistenti, fallback per preferenze vecchie, reset e keyboard-accessible controls.
4. Collegare flusso ai dati e servizi canonici: App shell e preferenze canoniche, design tokens e module-visibility semantics; non duplica CAP-0023 theme.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

No secondo dashboard/data store; screenshot matrix su UI5, contrasto, semantica, performance, account switch e fallback small screen.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
