# CAP-0155 — Associazioni ingredienti e ricette offline con Apriori

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

Frequent itemset e regole con supporto/confidenza, mai dedurre allergeni o causalità

## App candidate
- TasteAI: PROPOSTA, facilita stimata 84%
- In-Cucina-con-gli-Anime: PROPOSTA, facilita stimata 82%
- MealMate: PROPOSTA, facilita stimata 77%

Fattori score 89 (P2); facilità indipendente per app.

- Motore candidato: BEHAVIORAL_PATTERNS
- CAP a monte: CAP-0044, CAP-0045
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Corpus minimo, support/confidence/lift, ingredienti canonici, lingua, allergeni, nessuna aggiunta automatica a spesa.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
