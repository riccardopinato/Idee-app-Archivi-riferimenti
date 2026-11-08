# Vision Board — 14 estrazioni candidate (non certificate)

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
