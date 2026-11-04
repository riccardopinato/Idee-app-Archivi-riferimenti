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

## Riferimento matematico eseguibile — 04/11/2026

Il motore puro Dart corrispondente è stato integrato in App Factory Core @ `ae76e4267b67fe0e913d650d8e89a010dd235a5c`, con [sorgente](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/lib/src/on_device_algorithms.dart), [test unitari](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart) e [CI post-merge PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600). **La capability in questa app resta PROPOSTA/E0**: la sola reference library non prova una integrazione con archivio o permessi reali.

Scope concreto: LocalTfidfReference.tokenize/keywords; sparse lexical TF-IDF with caller-supplied visible corpus and stopwords; no learned semantic embeddings.

Gate di riuso: A real Notes/Wonderlog local keyword producer with opt-in tag proposals, privacy filter, multi-locale quality fixture and canonical writer consent. Vedere [issue di certificazione Golden](https://github.com/riccardopinato/App-Factory-Core/issues/68).
