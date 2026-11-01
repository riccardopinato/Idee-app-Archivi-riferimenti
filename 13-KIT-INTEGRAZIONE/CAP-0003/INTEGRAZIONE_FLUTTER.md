# Piano di integrazione Flutter — CAP-0003

**NON ESEGUITO — proposta da adattare all'app.**

1. Leggere Product Bible/roadmap e fissare commit SHA del repository destinatario.
2. Cercare componenti Golden e codice equivalente già presente: riuso prima di duplicazione.
3. Definire piccolo adattatore per **Preparazione contestuale appuntamento** sui modelli e servizi canonici, senza imporre nuovo stack o un secondo database.
4. Verificare licenze e impatto di SDK, modelli, storage, rete, permessi; local-first e consenso dove previsti.
5. Creare una UI coerente con il progetto, con preview, errore comprensibile e rollback dei dati.
6. Eseguire analyze, unit/widget test, build, dimensione APK e QA device se richiesto.

## Vincoli dal registro

Collaudo fisico +116 V116-06…V116-10 e V116-12: note, checklist, conflitti, Trash, offline e lingue; CI e APK firmato non equivalgono a DEVICE_PASS.

**Non dichiarare codice pronto o piattaforma supportata senza sorgente e test.**
