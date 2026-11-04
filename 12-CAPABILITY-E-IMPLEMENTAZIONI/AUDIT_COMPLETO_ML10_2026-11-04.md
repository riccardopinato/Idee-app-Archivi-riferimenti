# Audit completo capability / ML10 — 4 novembre 2026

**Baseline:** `riccardopinato/App-Factory-Core@02f3cd94f0ee6f19bc06fc0cb329fdf5398a739b`; Master v27 / Golden Index v28 / Registry v2.
**Scope:** tutte le 160 CAP e 385 associazioni riferite alle 48 app/idee;
31 repository GitHub confrontati per HEAD prima del presente pass.
**Importante:** 160/385 e un audit completo **del registro e delle evidenze note**;
non sono 160 implementazioni ispezionate end-to-end ne 48 test hardware.
Le 17 app senza repo nell'inventario mantengono SOURCE NON VERIFICATA.

- Ricalcolate e controllate: **160/160 score**, **385/385 stime app**.
- Score modificati con motivazione: **4**; invariati: **156**.
- Facilita modificate con motivazione: **20**; invariati: **365**.
- Stati per app modificati con evidenza scoped: **3**.
- Nuove CAP: 0. Golden certificati: 0. Nessuna modifica al Product Bible.
- Numeri di facilità: stime relative, NON probabilità empiriche.

## Score modificati

| CAP | Prima | Dopo | Motivo / fonte |
| --- | ---: | ---: | --- |
| CAP-0046 | 78 | 74 | No validated licensed vision checkpoint, runtime/model footprint or Italian ingredient-dataset accuracy; reduce feasibility. (https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md) |
| CAP-0116 | 79 | 83 | Small read-only MinHash/LSH source and guarded consumer pilot reduce narrow technical implementation cost; reversible canonical merge is NOT proven. (https://github.com/riccardopinato/App-Factory-Core/pull/71) |
| CAP-0132 | 69 | 65 | Audio model pack, rights, microphone UX and on-device profiling remain unverified; reference ML math does not implement an audio classifier. (https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md) |
| CAP-0153 | 78 | 80 | Exact-main test of bounded logistic/Holt numerical reference increases math evidence only; no personal task-delay calibration. (https://github.com/riccardopinato/App-Factory-Core/pull/73) |

## Facilità app modificate

| CAP / app | Prima | Dopo | Motivo |
| --- | ---: | ---: | --- |
| CAP-0032 / Notes-Ecosistema | 62 | 63 | Core bounded PCA/SVD projection provides optional math; no actual semantic model recall uplift claimed. |
| CAP-0044 / TasteAI | 95 | 96 | Core bounded kNN can rank user-visible recipe features; allergy, rights and canonical ingredient constraints external. |
| CAP-0044 / In-Cucina-con-gli-Anime | 95 | 97 | Core bounded kNN can rank user-visible recipe features; allergy, rights and canonical ingredient constraints external. |
| CAP-0046 / In-Cucina-con-gli-Anime | 80 | 74 | No licensed, benchmarked offline image classifier model and preprocessing/ABI contract. |
| CAP-0046 / TasteAI | 80 | 74 | No licensed, benchmarked offline image classifier model and preprocessing/ABI contract. |
| CAP-0057 / Pocket-Guard | 60 | 61 | Core LOF/isolation math does not supplant Android real-world sensor truth or alarm state policy. |
| CAP-0061 / Battery_Guard | 80 | 83 | Core EWMA/Holt additive seasonality reference only; phone fuel-gauge ETA accuracy unmeasured. |
| CAP-0116 / Notes-Ecosistema | 77 | 83 | Core ML10 MinHash reference and candidate preview reduce lexical implementation effort; source permissions and merge/undo remain unproven. |
| CAP-0124 / Notes-Ecosistema | 70 | 72 | Core HAC small-N reference; no topical structure changes or personal-note grouping validated. |
| CAP-0132 / Notes-Ecosistema | 55 | 50 | No licensed, benchmarked offline audio classifier model and microphone/privacy permission validation. |
| CAP-0132 / Wonderlog | 55 | 50 | No licensed, benchmarked offline audio classifier model and microphone/privacy permission validation. |
| CAP-0132 / Agenda-per-Anna | 25 | 20 | No licensed, benchmarked offline audio classifier model and microphone/privacy permission validation. |
| CAP-0152 / Notes-Ecosistema | 93 | 95 | Notes existing local bounded fuzzy fallback merged in PR #56; account ACL/save-time gate remains. |
| CAP-0153 / Notes-Ecosistema | 74 | 77 | Core numerical logistic/Holt tested; no trained, calibrated user-forecast predictor in any app. |
| CAP-0153 / Agenda-per-Anna | 71 | 73 | Core numerical logistic/Holt tested; no trained, calibrated user-forecast predictor in any app. |
| CAP-0153 / FocuSense | 66 | 67 | Core numerical logistic/Holt tested; no trained, calibrated user-forecast predictor in any app. |
| CAP-0154 / Agenda-per-Anna | 71 | 72 | Core Viterbi math available; labeled emissions and opt-in behavioral model missing. |
| CAP-0158 / Pocket-Guard | 91 | 93 | Pocket Guard live-session EWMA shadow sample observer merged #6; hardware/OEM and alarm-decision gate remain. |
| CAP-0159 / Wonderlog | 88 | 89 | Existing grid and radius geospatial reference remains preferable to bounded HAC on thousands of map POIs. |
| CAP-0160 / Notes-Ecosistema | 91 | 93 | Notes editor local TF-IDF suggestions merged in PR #56; human Save and ACL remain app duties. |

## Scoring and validation limits

I cinque fattori originali hanno pesi 35% valore, 25% riuso, 20% fattibilità,
10% evidenza, 10% rischio. Non si alterano score non corroborati.
CAP-0116 include esplicitamente merge reversibile: un read-only reviewer non completa il CAP.
CAP-0158 Pocket osserva i sensori in SHADOW, non pilota allarmi.
LiteRT/Core ML image/audio mancano di checkpoint licenziati e test dispositivi.
Core Dart numerics CI: https://github.com/riccardopinato/App-Factory-Core/actions/runs/41838055370
Notes verified historical fuzzy + TF-IDF main CI: https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41822558551
Pocket shadow postmerge: https://github.com/riccardopinato/Pocket-Guard/actions/runs/41822147632
ML10 audit and architecture: https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md

## 160/385 machine-readable full audit

- [Full CAP before/after and evidence CSV](AUDIT_COMPLETO_CAP_ML10_2026-11-04.csv)
- [Full app-CAP before/after and state CSV](AUDIT_COMPLETO_APP_ML10_2026-11-04.csv)
- [Canonical registry and per-record rationale](REGISTRO_CAPABILITY.json)
- Per-app generated operational views: `PER_APP/<app>/`.

## Remaining physical/quality gates

Notes Duplicate Review: source ACL, account switch, revision at merge-time,
attachment diff, explicit reversible merge and real precision/recall.
Pocket Guard: OEM, false positives, battery/lifecycle multi-device.
HMM / LOF / logistic: labeled independent validation, opt-in and power budgets.
Vision/audio: rights, model checksum, preprocessing, ABI and on-device tests.
Golden promotion needs its own reviewed, validated Core PR and E5 proof.
