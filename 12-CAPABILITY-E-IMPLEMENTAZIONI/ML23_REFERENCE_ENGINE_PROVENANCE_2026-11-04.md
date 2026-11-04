# ML23 — source ledger dei tre motori riusabili (4 novembre 2026)

- App Factory Core versione fonte: [`ae76e4267b67fe0e913d650d8e89a010dd235a5c`](https://github.com/riccardopinato/App-Factory-Core/commit/ae76e4267b67fe0e913d650d8e89a010dd235a5c)
- Libreria: [`reference_engines/lib/src/on_device_algorithms.dart`](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/lib/src/on_device_algorithms.dart)
- Vettori di test: [`reference_engines/test/on_device_algorithms_test.dart`](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart)
- Verifica eseguita: [reference-dart post-merge PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600) + [Factory validate PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145585)
- Governance: [issue #68 — Golden admission / E5](https://github.com/riccardopinato/App-Factory-Core/issues/68)

| CAP | Motore verificato in Core | Cosa resta da dimostrare |
| --- | --- | --- |
| CAP-0152 | Levenshtein, ricerca fuzzy limitata e filtraggio visible/deleted su input | Tokeni Unicode grapheme, ACL reale, shortlist Notes/Wonderlog e nuove revisioni |
| CAP-0160 | Tokenizzazione Unicode e TF-IDF lessicale sparse | Corpus e stopword 6 locale, ACL app, writer tag confermato e prova consumer |
| CAP-0158 | EWMA con isteresi e debounce su sequenze sintetiche | Adattatore sensori, foreground/lifecycle, batteria e test multi-OEM |

**Regola:** il CI dimostra un *source reference testato*, non E5 su un'app consumatrice, non hardware e non release. Queste tre CAP restano `PROPOSTA` a livello applicativo, il Golden Index v28 rimane la baseline letta dell'audit precedente. Nessun pacchetto ML, API esterna o permesso nativo è stato introdotto da questo aggiornamento.
