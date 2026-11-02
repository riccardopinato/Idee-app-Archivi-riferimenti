# Piano di integrazione Flutter — CAP-0144

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/home_widget_bridge.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Android Home: prossimo evento e apertura Crea; countdown su data scelta. Foto partner solo fase differita con consenso per immagine e revoca cache.
4. Collegare flusso ai dati e servizi canonici: Existing home_widget_bridge, Agenda store, shared media privacy gate, native Android AppWidget e iOS WidgetKit separati.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
