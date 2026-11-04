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
