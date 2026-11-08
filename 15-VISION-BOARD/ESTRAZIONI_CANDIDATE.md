# Vision Board — 28 estrazioni candidate (non certificate)

**Lotto 1:** VBE-001..014. **Lotto 2:** VBE-015..028. Nessuna nuova CAP ufficiale, Donor verificato o Golden certificato.

Le righe VBE sono **candidature**, non nuove CAP ufficiali, Donor VERIFIED o Golden certificati. Riuso-first della Factory.

| ID | Fonte/i | Ruolo | Contratto utile | Consumer | CAP correlate | Gate |
|---|---|---|---|---|---|---|
| VBE-001 | VBR-0003,VBR-0005 | UX_REFERENCE | Onboarding domande→obiettivi→immagini | Anna/Notes | CAP-0099 | Prototipo autonomo senza codice non licenziato |
| VBE-002 | VBR-0002 | PATTERN_DONOR | Tracking consistenza/frequenza obiettivi | Notes/Anna | CAP-0099,CAP-0104 | Algoritmo locale senza Neon |
| VBE-003 | VBR-0005 | PATTERN_DONOR | Board→goal ID, stato CRUD e lifecycle | Notes/Anna | CAP-0099 | Niente nuovo DB, sanificazione input e verifica Rails separata |
| VBE-004 | VBR-0013 | GOLDEN_CANDIDATE | Collage packer geometrico multi-layout | Notes/Anna | CAP-0029 | Port Dart + fixture + device benchmark |
| VBE-005 | VBR-0013 | CODE_DONOR_CANDIDATE | Media references/persistenza senza toccare originali | Notes/Anna | CAP-0075 | SAF Android, media missing, backup/restore |
| VBE-006 | VBR-0017 | CODE_DONOR_CANDIDATE | Document/viewport serializzazione .drawnix e plugin | Notes | CAP-0028,CAP-0029,CAP-0149 | Non confondere .drawnix e JSON Canvas |
| VBE-007 | VBR-0018 | CODE_DONOR_CANDIDATE | Web scene graph drag/pointer/touch | Notes Web | CAP-0029 | Valutare solo editor Web, non Flutter nativo |
| VBE-008 | VBR-0012 | PATTERN_DONOR | Portable imageStore board document .bf | Notes/Anna | CAP-0075,CAP-0149 | Solo pattern: codice non commerciale vietato |
| VBE-009 | VBR-0009 | PATTERN_DONOR | Collaboration presence + history opzionale | Notes (futuro) | CAP-0028 | Cloud auth/Liveblocks e license gate, non default Anna |
| VBE-010 | VBR-0015 | PATTERN_DONOR | Cluster cards e suggestion accept/reject | Notes | CAP-0098,CAP-0148 | Versione locale senza Gemini/CDP |
| VBE-011 | VBR-0020 | PATTERN_DONOR | Board protocol seq/idempotency/agent trace | Dev tools/Notes | CAP-0149 | Scope separato e licenze sottoprogetti |
| VBE-012 | VBR-0011 | UX_REFERENCE | Offline PDF proportional export UX | Notes/Anna | CAP-0075 | Solo descrizione: codice proprietario non pubblicato |
| VBE-013 | VBR-0006,VBR-0014 | UX_REFERENCE | Search images via provider, captions/attribution | Notes/Anna | CAP-0027 | ToS media, evitare secret lato client |
| VBE-014 | VBR-0016,VBR-0019 | DISCOVERY_ONLY | Nuovi motori o template da directory | Notes/Anna | — | Catalogare solo nuovi URL repository reali |

## Candidati da approfondire

**Golden candidato: Visual Board Layout / Media Composition.** Input: immagini e dimensioni; output: collages/tiled/cascading con bounding box; donor di riferimento [ImageCanvas](SCHEDE/VBR-0013.md), licenza MIT, ma Swift/macOS. Verificare che non duplichi il Golden Infinite Canvas/Ink già Draft: il vecchio Golden possiede viewport/ink, non un packer di layout dimostrato.

**CAP candidata non numerata: Vision Board come vista di goal, media reference e milestone canonici.** Confrontare con CAP-0099, CAP-0104, CAP-0029 e CAP-0075, impedendo un altro media store/DB/planner. Nessuna proposta di ID finché il delta non è approvato.

**Portabilità visiva:** codec .drawnix e .bf non equivalgono a JSON Canvas v1; import/export richiede mappatura, lossiness, fixture e test.


## Lotto 2 — VBE-015..028, solo candidate

| ID | Fonti VBR | Tipo | Contratto proposto | Consumer | CAP match | Gate |
|---|---|---|---|---|---|---|
| VBE-015 | VBR-0021 | PATTERN_DONOR | React infinite canvas custom shape and binding graph | Notes | CAP-0028,CAP-0029 | tldraw production license required; only reference without rights |
| VBE-016 | VBR-0022 | CODE_DONOR_CANDIDATE | Ordered .excalidraw scene IDs and export adapter | Notes,Anna | CAP-0028,CAP-0149 | MIT; Dart adapter, codec lossiness, no second engine |
| VBE-017 | VBR-0023 | PATTERN_DONOR | Unified notes/doc blocks↔edgeless graphical projections | Notes | CAP-0029,CAP-0098 | AFFiNE MIT/MPL/EE mixed; per-file license scope |
| VBE-018 | VBR-0025 | CODE_DONOR_CANDIDATE | Pure grid compaction/collision and responsive constraints | Notes,Anna | CAP-0147,CAP-0029 | MIT; Dart fixture tests vs existing VBE-004 |
| VBE-019 | VBR-0026 | PATTERN_DONOR | Multi-grid sort/filter/move with responsive layout | Notes | CAP-0147,CAP-0094 | MIT DOM, Flutter geometry + hit-testing required |
| VBE-020 | VBR-0028 | PATTERN_DONOR | Flutter Kanban as a canonical view layout | Notes,Anna | CAP-0094,CAP-0099 | AppFlowy AGPL; code reuse gated; one DB owner |
| VBE-021 | VBR-0033 | CODE_DONOR_CANDIDATE | Masonry waterfall media tile packing | Notes,Anna | CAP-0029,CAP-0147 | MIT README/source header; Outlayer/get-size dependencies |
| VBE-022 | VBR-0034 | CODE_DONOR_CANDIDATE | Canvas transforms/group and scene serialization/export | Notes,Anna | CAP-0029,CAP-0149 | Fabric MIT; Web-only or Dart port, not smart segmentation |
| VBE-023 | VBR-0035 | CODE_DONOR_CANDIDATE | Image crop and rotation geometry | Anna,Notes | CAP-0136 (ADJACENT) | Crop != cutout; immutable originals, EXIF and pinch QA |
| VBE-024 | VBR-0036 | PATTERN_DONOR | Minimum image editor tool lifecycle and non-destructive export | Anna,Notes | CAP-0075,CAP-0029 | MIT source, but Web/React size/privacy benchmark |
| VBE-025 | VBR-0037 | PATTERN_DONOR | Card/list/project IDs, order, due-date and attachments | Notes | CAP-0094,CAP-0099 | PLANKA Fair Use/Pro restriction; reference only |
| VBE-026 | VBR-0038 | PATTERN_DONOR | Recurring Kanban card and import/export contracts | Notes | CAP-0094,CAP-0075 | WeKan MIT; selective domain tests, no Meteor |
| VBE-027 | VBR-0039 | PATTERN_DONOR | Same block data shown as board/table/gallery/calendar views | Notes,Anna | CAP-0094,CAP-0147 | Focalboard AGPL source and maintenance notice |
| VBE-028 | VBR-0034, VBR-0035, VBR-0036 | GOLDEN_CANDIDATE | Reversible image edit derivatives referencing canonical originals | Anna,Notes | CAP-0136 (ADJACENT),CAP-0075 | Reconcile Golden Media Asset Store, Dart device tests |

**Antiduplicazione:** VBE-018 (React Grid Layout) e VBE-021 (Masonry) ampliano il confronto del **candidato Golden layout VBE-004**, non generano due Golden. VBE-020/025/026/027 vanno confrontate con `CAP-0094` e i task canonici, senza app proprietaria seconda. VBE-028 va sottoposto prima al Golden Media Asset Store: geometric crop/edits non equivalgono a ML cutout CAP-0136.
