# CAP-0111 — test standalone

`dart 13-KIT-INTEGRAZIONE/CAP-0111/test/anna_weekly_review_test.dart`. Copre limiti settimana, status attuale `done`, filtro su private task, dedup ID, appuntamenti esclusi, account changed e limiti di iterazione. `dart analyze` eseguito in CI su sorgente e test.

Non testato: mapping vivo `AgendaItem`, `AgendaStore` real-time, UI, blocchi di ricorrenza nel runtime, migrazioni/export, Android physical. Stato app `PROPOSTA`.
