# Piano di integrazione Flutter — CAP-0085

**NON ESEGUITO — proposta da adattare all'app.**

1. Leggere Product Bible/roadmap e fissare commit SHA del repository destinatario.
2. Cercare componenti Golden e codice equivalente già presente: riuso prima di duplicazione.
3. Definire piccolo adattatore per **Diarizzazione vocale locale per appunti riunioni** sui modelli e servizi canonici, senza imporre nuovo stack o un secondo database.
4. Verificare licenze e impatto di SDK, modelli, storage, rete, permessi; local-first e consenso dove previsti.
5. Creare una UI coerente con il progetto, con preview, errore comprensibile e rollback dei dati.
6. Eseguire analyze, unit/widget test, build, dimensione APK e QA device se richiesto.

## Vincoli dal registro

Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base.

**Non dichiarare codice pronto o piattaforma supportata senza sorgente e test.**
