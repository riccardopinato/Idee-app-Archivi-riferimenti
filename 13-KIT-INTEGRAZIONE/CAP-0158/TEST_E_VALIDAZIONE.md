# CAP-0158 — Soglie adattive con isteresi per luce e prossimità — gate QA

- Invarianti: input finiti e validati, risultati riproducibili/tie-break, permessi e source revision, zero write implicit.
- Negativi: empty/one element, dati raddoppiati, unicode/locale, stale/deleted/archived, device capability absent, no model, no network.
- Eseguire piccoli + 500/5000 synthetic fixtures, misurare correctness prima di p50/p95, dimensione apk diff e RAM/batteria su device distinto.
- Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM.
- Solo evidence a commit SHA e CI exact-head puo portare a donor E3; consumer indipendente E5 resta futuro.

ESITO: NOT TESTED IN THIS AUDIT / NOT COPY READY.
