# CAP-0152 — Ricerca fuzzy offline per refusi e alias — gate QA

- Invarianti: input finiti e validati, risultati riproducibili/tie-break, permessi e source revision, zero write implicit.
- Negativi: empty/one element, dati raddoppiati, unicode/locale, stale/deleted/archived, device capability absent, no model, no network.
- Eseguire piccoli + 500/5000 synthetic fixtures, misurare correctness prima di p50/p95, dimensione apk diff e RAM/batteria su device distinto.
- Top-K bounded, grapheme, token di 1 carattere, soglie false-match, 500/5000 record e nessuna fuga da Shared Spaces.
- Solo evidence a commit SHA e CI exact-head puo portare a donor E3; consumer indipendente E5 resta futuro.

ESITO: NOT TESTED IN THIS AUDIT / NOT COPY READY.

## Evidenza parziale su package di riferimento

- Dart test per motore puro su Core `ae76e4267b67fe0e913d650d8e89a010dd235a5c`: [CI PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600); [test code](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart).
- Non eseguiti test sulle app beneficiarie, nessun hardware/OEM per i sensori, nessuna firma Play.
- Prossimo gate: An app integration with scoped visible candidate retrieval, Shared Space ACL/revision recheck, 500/5000 notes and corrected text selection UI.
