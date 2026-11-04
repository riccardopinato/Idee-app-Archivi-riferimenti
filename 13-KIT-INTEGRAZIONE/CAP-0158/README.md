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

## Riferimento matematico eseguibile — 04/11/2026

Il motore puro Dart corrispondente è stato integrato in App Factory Core @ `ae76e4267b67fe0e913d650d8e89a010dd235a5c`, con [sorgente](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/lib/src/on_device_algorithms.dart), [test unitari](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart) e [CI post-merge PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600). **La capability in questa app resta PROPOSTA/E0**: la sola reference library non prova una integrazione con archivio o permessi reali.

Scope concreto: LocalAdaptiveSignalReference.step; deterministic EWMA, consecutive threshold and hysteresis state; pure numeric samples only.

Gate di riuso: Kotlin/Flutter-native sensor adapter with hardware health/foreground compliance, multi-OEM false alarms, energy and persistence tests. Vedere [issue di certificazione Golden](https://github.com/riccardopinato/App-Factory-Core/issues/68).
