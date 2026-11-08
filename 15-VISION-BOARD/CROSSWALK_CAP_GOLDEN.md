# Crosswalk Vision Board ↔ capability e Golden già presenti

**Baseline consultata:** `App-Factory-Core@c709e483d40424c88b6ba316d0c8352eec5370fe`, Master v27, Golden Index v28. Catalogo CAP live verificato il 08/11/2026. Questa è una **mappa di compatibilità per la ricerca**, non certificazione né attestazione di stato nell'app.

## Golden pertinenti, da riusare prima di crearne altri
| Oggetto Factory | Stato al 08/11 | Confine |
|---|---|---|
| [Infinite Canvas / Ink Engine](https://github.com/riccardopinato/App-Factory-Core/blob/c709e483d40424c88b6ba316d0c8352eec5370fe/golden/ui/GOLDEN_INFINITE_CANVAS_INK_ENGINE_v1_DRAFT.txt) | DRAFT: core viewport/ink puro Dart, consumer/widget/gestures ancora da provare | Coordinate, scene, strokes, undo/redo; NON board goals, media store o gestione diario |
| [OSS Reuse / Reconnaissance](https://github.com/riccardopinato/App-Factory-Core/blob/c709e483d40424c88b6ba316d0c8352eec5370fe/golden/governance/GOLDEN_OSS_REUSE_RECONNAISSANCE_FLUTTER_v1_DRAFT.txt) | DRAFT | Priorità reuse-first, licenze e adattamento minimo |
| [Capability Harvest / Multi-Donor](https://github.com/riccardopinato/App-Factory-Core/blob/c709e483d40424c88b6ba316d0c8352eec5370fe/golden/governance/GOLDEN_CAPABILITY_HARVEST_ASSEMBLY_v1_DRAFT.txt) | DRAFT | PRESERVE/IMPORT/REBUILD/DROP per componente, non per repo |
| [Provenance / Reuse Ledger](https://github.com/riccardopinato/App-Factory-Core/blob/c709e483d40424c88b6ba316d0c8352eec5370fe/golden/governance/GOLDEN_PROVENANCE_REUSE_LEDGER_v1_DRAFT.txt) | DRAFT | Origine, SHA, file, adattamenti, licenza e test |

## CAP canoniche da verificare come possibili match
| CAP | Contratto già catalogato | Pertinenza Vision Board |
|---|---|---|
| [CAP-0028](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0028.md) | Connettori visuali tra post-it | Link e relazioni tra elementi |
| [CAP-0029](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0029.md) | Canvas ibrida sketch sotto note | Livello disegno sotto i contenuti |
| [CAP-0094](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0094.md) | Sticky Kanban con task canoniche | Task come riferimenti, non copie |
| [CAP-0098](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0098.md) | Mind map derivata da note e documenti | Relazioni e navigazione |
| [CAP-0099](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0099.md) | Da obiettivi a checklist | Goal → azioni concrete in Notes |
| [CAP-0104](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0104.md) | Timeline obiettivi e pianificazione a ritroso | Milestone temporali |
| [CAP-0136](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0136.md) | Scontorno foto in elementi canvas | Sticker/visual compositing |
| [CAP-0149](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0149.md) | Interoperabilità JSON Canvas con perdita dichiarata | Import/export di dati editabili |
| [CAP-0027](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0027.md) | Share capture link/testo/immagine | Acquisizione di ispirazioni |
| [CAP-0075](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0075.md) | Import Center | Migrazione board / media |
| [CAP-0010](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0010.md) | Ricordi Then & Now | Contenuti comparativi per Anna |
| [CAP-0011](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0011.md) | Life Threads | Collegamenti di vita come viste derivate per Anna |

**Da non assumere:** che tutte queste CAP siano già implementate in Notes o Anna. L'esistenza nel catalogo non certifica codice, QA, né approvazione di roadmap. Per ciascuna integrazione futura leggere `app_states`, sorgenti/PR e Product Bible attuali.

## Nuove responsabilità da considerare solo dopo i repository reali
Vision Board personale/progettuale potrebbe richiedere un **contratto di composizione di visioni e obiettivi** (board→goal/reference→milestone) distinto dal puro motore canvas. Prima di proporre una CAP, provare che non sia già coperto dai contratti sopra; evitare un secondo media store, task engine, planner, sync o lifecycle. Candidate non numerate fino all'ammissione.


## Lotto 1 verificato (08/11/2026)

[20 schede](INBOX_REPOSITORY.md) / [14 estrazioni](ESTRAZIONI_CANDIDATE.md) / [audit comparativo](AUDIT_20_RIFERIMENTI_VB_2026-11-08.md). Proposta Golden Layout/Media Composition ancora NON_CERTIFIED e distinta dal core Infinite Canvas/Ink. Proposta CAP Vision Board GoalRefs+MediaRefs NON NUMERATA finché non è dimostrato il delta da CAP-0029/0099/0104/0149. Dal registro CAP: Notes CAP-0029 e 0098 SOURCE_REPORTED, CAP-0099/0104/0149 PROPOSTA. Stati di catalogo, non test runtime.


## Lotto 2 — allineamento no-duplication, 08/11/2026

[Audit](AUDIT_20_RIFERIMENTI_VB_LOTTO_2_2026-11-08.md) · [VBE-015..028](ESTRAZIONI_CANDIDATE.md). `CAP-0028`, `CAP-0029` e `CAP-0149`: Excalidraw/AFFiNE/tldraw/Fabric propongono pattern di scene e export; **Golden Infinite Canvas/Ink Draft** ha già ownership di world coords, strokes, scene. No secondo engine.

`CAP-0147`: RGL/Muuri/Masonry per layout e interazioni; confrontare con **VBE-004** ImageCanvas layout candidate. `CAP-0094/0099/0104`: AppFlowy, PLANKA, WeKan e Focalboard usati solo come sorgenti di proiezioni multi-view su task unici, non nuovi task store.

`CAP-0136` smart cutout non coincide con Easy Crop: ritaglio geometrico e media-edit vanno riconciliati con **Golden Media Asset Store Draft**, che possiede originals/derivatives. Source flags dal registro CAP live: Notes CAP-0029 e 0098 `SOURCE_REPORTED`, CAP-0094/0099/0104/0149 `PROPOSTA`; Anna CAP-0147 `PROPOSTA`. Questi non sono esiti di test runtime.
