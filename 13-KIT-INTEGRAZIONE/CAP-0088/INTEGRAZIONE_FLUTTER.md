# Piano di integrazione Flutter — CAP-0088

**NON ESEGUITO — proposta da adattare all'app.**

1. Leggere Product Bible/roadmap e fissare commit SHA del repository destinatario.
2. Cercare componenti Golden e codice equivalente già presente: riuso prima di duplicazione.
3. Definire piccolo adattatore per **Workspace Android desktop virtuale con capability probe** sui modelli e servizi canonici, senza imporre nuovo stack o un secondo database.
4. Verificare licenze e impatto di SDK, modelli, storage, rete, permessi; local-first e consenso dove previsti.
5. Creare una UI coerente con il progetto, con preview, errore comprensibile e rollback dei dati.
6. Eseguire analyze, unit/widget test, build, dimensione APK e QA device se richiesto.

## Vincoli dal registro

Rimandato: Dextop GPLv3, usa hidden API e runtime privilegiati; Samsung OneUI moderno prevalente, Xiaomi/HyperOS disabilitato. Vietato promettere compatibilita universale, copia solo con obblighi GPL e test Play.

**Non dichiarare codice pronto o piattaforma supportata senza sorgente e test.**
