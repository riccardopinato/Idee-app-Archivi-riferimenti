# Vision Board — audit tecnico lotto 2 / 08-11-2026

## Scope
20 input: 13 repository E1 con commit immutabile e source file, 5 directory GitHub Topics, 1 alias di topic non verificato, 1 duplicato (input 17 -> VBR-0001). 19 nuove schede. Nessun test runtime, CI, porting, licenza estesa, build o release svolto in questo lavoro.

## Licenze ad alto impatto
- **tldraw VBR-0021:** custom license vieta produzione ordinaria senza licenza commerciale/trial valida, con enforcement/telemetria; non trattare come MIT.
- **AFFiNE VBR-0023:** sorgenti MIT fuori aree escluse, backend/server EE e carveout MPL CE/client; audit per singolo file prima di copie.
- **AppFlowy VBR-0028:** AGPL-3.0; non è divieto assoluto commerciale ma obbliga a verifica copyleft/network-source.
- **PLANKA VBR-0037:** Community Fair Use e Pro/Enterprise separati; il README classifica calendar/timeline/map/templates e PDF Pro, non code donor libero.
- **Focalboard VBR-0039:** LICENSE.txt è AGPL per sorgenti di norma con eccezioni Apache2; MIT per binari prodotti da Mattermost, non automaticamente per sorgenti. README: not maintained.
- **MIT file:** VBR-0022 Excalidraw, 0025 React Grid Layout, 0026 Muuri, 0034 Fabric, 0035 EasyCrop, 0036 Filerobot, 0038 WeKan (7). **MIT README+header:** VBR-0033 Masonry (1). Asset/SDK/package chain indipendente da verificare.

## Source-backed technical audit
1. `VBR-0021` tldraw: Editor.ts object record graph, shape binding, scene operations; React with commercial SDK license gate.
2. `VBR-0022` Excalidraw: Scene.ts object ordering, deletion and selection, .excalidraw JSON separate from JSON Canvas v1.
3. `VBR-0023` AFFiNE: mindmap store.ts registers plain text/Markdown adapters, docs+edgeless model; mixed licensing.
4. `VBR-0025` React Grid Layout: compactor.ts pluggable collision and layout geometric code; TS core can be ported to Dart.
5. `VBR-0026` Muuri: Item.js grid item geometry, sorting/drag; DOM-heavy web only without port.
6. `VBR-0028` AppFlowy: board.dart Flutter BoardPluginBuilder maps ViewPB to Board layout, integrated with Rust/domain.
7. `VBR-0033` Masonry: masonry.js colYs waterfall; photographic grid, not freeform canvas.
8. `VBR-0034` Fabric: StaticCanvas.ts object scene and transform/zoom/JSON/SVG support, not ML background cutout.
9. `VBR-0035` EasyCrop: helpers.ts cropSize/zoom/rotation/restrictPosition; crop geometry ≠ CAP-0136 scontorno.
10. `VBR-0036` Filerobot: browser editor index.js React mount/getCurrentImgData/updateState, large editor scope.
11. `VBR-0037` PLANKA: Card.js redux-orm card/list/board/attachment relations; Pro claims cannot become Community guarantees.
12. `VBR-0038` WeKan: cards.js recurrence, dependencies and metadata; Meteor server/app model large.
13. `VBR-0039` Focalboard: boardView.ts projects same blocks into board/table/gallery/calendar filtered views.

## Donor / Golden / CAP extraction
[14 candidate nuove VBE-015..028](ESTRAZIONI_CANDIDATE.md). Un Golden Visual Board Layout già ipotizzato come VBE-004 non va duplicato: candidati ImageCanvas, React Grid Layout, Muuri e Masonry sono **alternative da confrontare**. Golden Media Asset Store Draft è owner di originals/derivatives, non importare un secondo media DB.

Notes P1: AFFiNE hybrid doc+board reference, Excalidraw ordering, RGL pure compactor, AppFlowy Flutter board projection; Fabric per Web/edit quando necessario; tldraw *solo reference licenza-gated*. Anna P1: EasyCrop crop geometry, Masonry photo waterfall, Filerobot minimal edit UX, Fabric object compositing; no generico editor enterprise o seconda architettura.

CAP crosswalk: `CAP-0029` canvas ibrida; `CAP-0028` connectors; `CAP-0094` Kanban canonico; `CAP-0099` goals; `CAP-0104` timeline; `CAP-0147` modular Home; `CAP-0149` JSON Canvas; `CAP-0136` smart cutout **non** coperto da crop. Nessuna modifica CAP/Golden ufficiale.

## Gate
- Flutter port fixture tests on scene/layout/pinch/undo/redo and canonical goal/media references.
- Media original/derivative, missing file, EXIF, privacy, storage/backup, memory and APK size.
- .excalidraw/.bf/.drawnix/JSON Canvas adapters require staging and lossiness reporting.
- Per-file OSS license/SBOM and legal gate before any paid commercial reuse.
- No consumer code changed or verified in this audit; roadmap scope pending Product Bible decision.
