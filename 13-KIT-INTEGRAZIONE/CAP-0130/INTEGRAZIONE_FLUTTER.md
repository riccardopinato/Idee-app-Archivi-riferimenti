# Piano di integrazione Flutter — CAP-0130

**NON ESEGUITO — proposta da adattare all'app.**

1. Leggere Product Bible/roadmap e fissare commit SHA del repository destinatario.
2. Cercare componenti Golden e codice equivalente già presente: riuso prima di duplicazione.
3. Definire piccolo adattatore per **Generazione di slide e figure tecniche modificabili** sui modelli e servizi canonici, senza imporre nuovo stack o un secondo database.
4. Verificare licenze e impatto di SDK, modelli, storage, rete, permessi; local-first e consenso dove previsti.
5. Creare una UI coerente con il progetto, con preview, errore comprensibile e rollback dei dati.
6. Eseguire analyze, unit/widget test, build, dimensione APK e QA device se richiesto.

## Vincoli dal registro

Paper2Any dichiara Paper2PPT e licenza Apache-2.0, ma la demo pubblica era in errore; il backend/AI non va importato automaticamente. | Paper2Any dichiara Paper2Figure e Paper2PPT nella stessa codebase; registrata come modalita dello stesso CAP di Notes-to-Slides. Verificare architettura e licensing nel Product Bible prima di integrare.

**Non dichiarare codice pronto o piattaforma supportata senza sorgente e test.**
