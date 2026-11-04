# CAP-0159 — Clustering spaziale privacy-safe per ricordi e POI

**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.

DBSCAN in metri o griglia geospaziale con source visibility

## App candidate
- Wonderlog: PROPOSTA, facilita stimata 88%
- TrailPath: PROPOSTA, facilita stimata 79%
- CamperBoss: PROPOSTA, facilita stimata 82%
- Agenda-per-Anna: PROPOSTA, facilita stimata 70%

Fattori score 85 (P2); facilità indipendente per app.

- Motore candidato: GEO_GEOMETRY
- CAP a monte: CAP-0009, CAP-0051, CAP-0048
- Fonte: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md
- Gate: Antimeridiano/poli, GPS nullo/non finito, raggio geodesico, permesso luoghi condivisi, dati privati non esportabili per default.

Altri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).
