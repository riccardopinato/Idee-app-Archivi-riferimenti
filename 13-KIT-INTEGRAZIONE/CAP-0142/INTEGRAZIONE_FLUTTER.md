# Piano di integrazione Flutter — CAP-0142

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/shared_memories.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Modalità personale testo e reminder; estensione successiva coppia testo+foto con data/fuso e apertura esplicita dopo prova privacy.
4. Collegare flusso ai dati e servizi canonici: Diario/ricordi e media canonici, reminder; backend solo per condivisione esplicita e autorizzata.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

Nessuna garanzia crittografica del blocco temporale. QA date/fusi/offline/orologio, backup e sync due device; shared dopo Privacy #215.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
