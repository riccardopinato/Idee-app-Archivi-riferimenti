# CAP-0157 — Gesti volontari locali tramite Dynamic Time Warping

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

Distanza DTW con template scelto dall'utente; cap sensori/FGS obbligatorio

## App candidate
- Phone-Guard: PROPOSTA, facilita stimata 61%
- Pocket-Guard: PROPOSTA, facilita stimata 72%
- Tabletop-Motion-Alarm: PROPOSTA, facilita stimata 67%
- FocuSense: PROPOSTA, facilita stimata 65%

Fattori score 72 (P3); facilità indipendente per app.

- Motore candidato: SENSOR_SIGNAL
- CAP a monte: CAP-0057, CAP-0062
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
