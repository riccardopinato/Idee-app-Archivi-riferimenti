# CAP-0157 — Gesti volontari locali tramite Dynamic Time Warping — gate QA

- Invarianti: input finiti e validati, risultati riproducibili/tie-break, permessi e source revision, zero write implicit.
- Negativi: empty/one element, dati raddoppiati, unicode/locale, stale/deleted/archived, device capability absent, no model, no network.
- Eseguire piccoli + 500/5000 synthetic fixtures, misurare correctness prima di p50/p95, dimensione apk diff e RAM/batteria su device distinto.
- Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita.
- Solo evidence a commit SHA e CI exact-head puo portare a donor E3; consumer indipendente E5 resta futuro.

ESITO: NOT TESTED IN THIS AUDIT / NOT COPY READY.
