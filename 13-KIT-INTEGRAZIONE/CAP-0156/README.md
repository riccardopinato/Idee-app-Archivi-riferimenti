# CAP-0156 — Semplificazione reversibile di tracce e polilinee GPX

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

Ramer–Douglas–Peucker parametrizzato in metri, originale immutato

## App candidate
- TrailPath: PROPOSTA, facilita stimata 82%
- Wonderlog: PROPOSTA, facilita stimata 89%
- CamperBoss: PROPOSTA, facilita stimata 86%

Fattori score 89 (P2); facilità indipendente per app.

- Motore candidato: GEO_GEOMETRY
- CAP a monte: CAP-0048, CAP-0049, CAP-0050
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Lat/lon finiti, antimeridiano e poli, endpoint/waypoint protetti, errore massimo verificato, nessuna mutazione dello storico.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
