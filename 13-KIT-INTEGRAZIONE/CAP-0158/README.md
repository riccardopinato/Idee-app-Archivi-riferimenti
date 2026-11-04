# CAP-0158 — Soglie adattive con isteresi per luce e prossimità

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

EWMA e debounce per segnali rumorosi, impossibile inferire contesto da un solo campione

## App candidate
- Pocket-Guard: PROPOSTA, facilita stimata 91%
- Phone-Guard: PROPOSTA, facilita stimata 86%
- FocuSense: PROPOSTA, facilita stimata 89%
- Tabletop-Motion-Alarm: PROPOSTA, facilita stimata 84%

Fattori score 96 (P1); facilità indipendente per app.

- Motore candidato: SENSOR_SIGNAL
- CAP a monte: CAP-0057, CAP-0062
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
