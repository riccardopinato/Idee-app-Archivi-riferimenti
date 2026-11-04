# CAP-0160 — Estrazione TF-IDF di parole chiave e tag suggeriti

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

TF-IDF sparse per keyword e ranking, distinto da embeddings semantici

## App candidate
- Notes-Ecosistema: PROPOSTA, facilita stimata 91%
- Agenda-per-Anna: PROPOSTA, facilita stimata 80%
- Wonderlog: PROPOSTA, facilita stimata 84%
- PDF-Unifier: PROPOSTA, facilita stimata 74%

Fattori score 91 (P2); facilità indipendente per app.

- Motore candidato: LEXICAL_TEXT
- CAP a monte: CAP-0124, CAP-0148, CAP-0032
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Tokenizzazione IT/EN/ES/FR/DE/PT, stopwords, IDF stabile, shared ACL, gestione corpus piccolo, preview prima di tag writer.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
