# Criteri di ammissione di un provider/donor

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

Per ogni futura libreria, repository, fonte dati, POI, meteo o API creare una scheda:
- resource_id stabile, titolo, categoria (DATASET/API/LIB/REPO/CONTENT), URL canonico, proprietario;
- modello licenza (dati/code/assets separati), link a ToS, attribution, commercial_use_allowed, ODbL/CC/GPL/copyright obligations;
- mercato/copertura, granularità spaziale/temporale, aggiornamento, ultimo controllo, disponibilità SLA;
- costo: free noncommerciale, piano commerciale, query/month, limiti, egress, offline, caching, ridistribuzione;
- privacy/PII e necessità di consenso; API key in backend/restricted config;
- affidabilità e fallback; schema/versioning/dedup ID; test sample; quote e rate limit;
- app beneficiarie e uso concreto; stato CANDIDATE/VALIDATED/IMPLEMENTED/PROD VERIFIED/BLOCKED;
- prova fisica/store dove necessario; owner decision, data ultimo audit; note su aggiornamenti.

Non acquisire massivamente POI da endpoint pubblici Nominatim/Overpass per creare un mirror. Usare data extracts autorizzati.
Non usare tile OSM pubblici per download offline; configurare tile provider o self-host.
Non monetizzare un'app AdMob usando il piano API Open-Meteo dichiarato noncommerciale.
Non dare per scontata una licenza per le immagini presa dal fatto che una foto è su Wikimedia/un sito.
Non confondere il codice OSS con il contenuto servito dall'API di un provider.
Non presentare informazioni come 'aggiornato ora', 'aperto ora', 'routing confermato', 'scaricato' se non provate dai dati e dal runtime.

====================================================================
