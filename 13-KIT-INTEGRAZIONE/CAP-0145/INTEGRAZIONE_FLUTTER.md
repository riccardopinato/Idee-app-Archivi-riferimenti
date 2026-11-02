# Piano di integrazione Flutter — CAP-0145

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/planner_views.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Griglia locale per eventi/diario/task esistenti; eventuale mood/gratitudine solo con input esplicito e consenso.
4. Collegare flusso ai dati e servizi canonici: Derived view su store canonico di diario e task, nessun nuovo profiler né IA e nessuna telemetria obbligatoria.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

No health/diagnostic claims, no dati ciclo/Vault in UI ordinaria, no esempi +40% spacciati per risultati; test missingness e permessi.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
