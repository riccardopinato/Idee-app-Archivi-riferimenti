# CAP-0160 — Estrazione TF-IDF di parole chiave e tag suggeriti — gate QA

- Invarianti: input finiti e validati, risultati riproducibili/tie-break, permessi e source revision, zero write implicit.
- Negativi: empty/one element, dati raddoppiati, unicode/locale, stale/deleted/archived, device capability absent, no model, no network.
- Eseguire piccoli + 500/5000 synthetic fixtures, misurare correctness prima di p50/p95, dimensione apk diff e RAM/batteria su device distinto.
- Tokenizzazione IT/EN/ES/FR/DE/PT, stopwords, IDF stabile, shared ACL, gestione corpus piccolo, preview prima di tag writer.
- Solo evidence a commit SHA e CI exact-head puo portare a donor E3; consumer indipendente E5 resta futuro.

ESITO: NOT TESTED IN THIS AUDIT / NOT COPY READY.
