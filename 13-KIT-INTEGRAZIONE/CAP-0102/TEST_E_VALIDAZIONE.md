# CAP-0102 — test contract Anna

`dart 13-KIT-INTEGRAZIONE/CAP-0102/test/anna_reschedule_preview_test.dart` in GitHub CI verifica: slot liberi che rispettano durata, due proposte, ordine stabile, deadline, blocco shared/fixed/recurring/completed, coverage parziale, account cambiato, dedup, duration input invalida.

**Non testati:** import nella Flutter app, connessione all'AgendaStore e all'editor, vere revisioni DB, DST/fusi reali, reminder/sync e contesto dispositivo. `dart analyze` e CLI test non equivalgono a build APK.
