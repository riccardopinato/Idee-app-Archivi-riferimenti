# CAP-0152 — Ricerca fuzzy offline per refusi e alias

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

Distanza Levenshtein/Jaro-Winkler solo su candidati autorizzati, Unicode-aware

## App candidate
- Notes-Ecosistema: PROPOSTA, facilita stimata 93%
- Agenda-per-Anna: PROPOSTA, facilita stimata 89%
- Wonderlog: PROPOSTA, facilita stimata 88%
- PDF-Unifier: PROPOSTA, facilita stimata 83%

Fattori score 96 (P1); facilità indipendente per app.

- Motore candidato: LEXICAL_TEXT
- CAP a monte: CAP-0015, CAP-0032
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Top-K bounded, grapheme, token di 1 carattere, soglie false-match, 500/5000 record e nessuna fuga da Shared Spaces.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).

## Riferimento matematico eseguibile — 04/11/2026

Il motore puro Dart corrispondente è stato integrato in App Factory Core @ `ae76e4267b67fe0e913d650d8e89a010dd235a5c`, con [sorgente](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/lib/src/on_device_algorithms.dart), [test unitari](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart) e [CI post-merge PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600). **La capability in questa app resta PROPOSTA/E0**: la sola reference library non prova una integrazione con archivio o permessi reali.

Scope concreto: LocalFuzzyReference.distance/search; bounded ID-stable code-point fuzzy token matching; cannot guarantee grapheme-aware normalization, full-text recall or ACL enforcement.

Gate di riuso: An app integration with scoped visible candidate retrieval, Shared Space ACL/revision recheck, 500/5000 notes and corrected text selection UI. Vedere [issue di certificazione Golden](https://github.com/riccardopinato/App-Factory-Core/issues/68).
