# Catalogo visuale ↔ App Factory — matrice di compatibilità

**Stato: proposte UI/UX, NON approvazioni o implementazioni**. Questa vista è una fotografia di ricerca. La fonte autorevole delle associazioni tra i **99 riferimenti**, i **28 stili** e le **19 app** è [Design-App — registro relazionale](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json). Navigazione: [App → Stili](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/PER_APP_STILI_2026-11-13.md) oppure [Stile → App](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/PER_STILE_APP_2026-11-13.md). I link puntano ai file verificati nel ramo `main` di Design-App.

| App | Famiglie UI/UX compatibili | Famiglie estetiche compatibili | Reference uniche |
|---|---|---|---:|
| 180FlipCharge | BENTO UI, DESIGN SYSTEM, ILLUSTRATED CONTROLS, MINIMAL CONTROLS, NEUMORPHISM, PASTEL UI, RETRO DESKTOP, TOGGLE & SWITCH | AESTHETIC, CINEMATIC, ILLUSTRATED, PIXEL ART, Y2K RETRO | 4 |
| Anna's Diary | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, ILLUSTRATED CONTROLS, MINIMAL CONTROLS, NATURE-TECH, NAVIGATION UI, NEUMORPHISM, PALETTE, PASTEL UI, SCENIC BACKGROUND, SCENIC ILLUSTRATION, SKEUOMORPHISM, SOFT 3D, TOGGLE & SWITCH | AESTHETIC, ANIME, CINEMATIC, ILLUSTRATED, NEON, ORGANIC, VINTAGE | 29 |
| App Factory Dashboard | BENTO UI, DESIGN SYSTEM, MINIMAL CONTROLS, NAVIGATION UI, NEO-APPLE, SOFT 3D | AESTHETIC, NEON, ORGANIC, VINTAGE | 11 |
| Battery Guard | BENTO UI, DESIGN SYSTEM, GLASSMORPHISM, MINIMAL CONTROLS, NEUMORPHISM, PALETTE, SKEUOMORPHISM, TOGGLE & SWITCH | AESTHETIC, NEON, ORGANIC, VINTAGE | 20 |
| CamperBoss | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, GLASSMORPHISM, ILLUSTRATED CONTROLS, NATURE-TECH, PALETTE, PASTEL UI, SKEUOMORPHISM, SOFT 3D, TOGGLE & SWITCH | AESTHETIC, CINEMATIC, ILLUSTRATED, NEON, ORGANIC, VINTAGE | 9 |
| CashMate AI | DESIGN SYSTEM, GLASSMORPHISM, MINIMAL CONTROLS, NEO-APPLE, NEUMORPHISM, PALETTE, SKEUOMORPHISM, SOFT 3D, TOGGLE & SWITCH | AESTHETIC, NEON, ORGANIC, VINTAGE | 13 |
| Cooking Anime | BENTO UI, DESIGN SYSTEM, MINIMAL CONTROLS, PALETTE, RETRO DESKTOP, SCENIC BACKGROUND, SCENIC ILLUSTRATION, SKEUOMORPHISM, SOFT 3D | AESTHETIC, ANIME, ILLUSTRATED, NEON, PIXEL ART, VINTAGE, Y2K RETRO | 15 |
| Deskland Android | DESIGN SYSTEM, GLASSMORPHISM, MINIMAL CONTROLS, NATURE-TECH, NEUMORPHISM, PALETTE, SCENIC BACKGROUND, SCENIC ILLUSTRATION, SKEUOMORPHISM, SOFT 3D | AESTHETIC, ANIME, CINEMATIC, ILLUSTRATED, NEON, ORGANIC, VINTAGE | 22 |
| Easy Debloat | DESIGN SYSTEM, MINIMAL CONTROLS, NEUMORPHISM, TOGGLE & SWITCH | AESTHETIC, VINTAGE | 4 |
| FocusSense | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, GLASSMORPHISM, MINIMAL CONTROLS, NATURE-TECH, NEO-APPLE, NEUMORPHISM, PALETTE, PASTEL UI, SKEUOMORPHISM, SOFT 3D, TOGGLE & SWITCH | AESTHETIC, CINEMATIC, NEON, ORGANIC, VINTAGE | 25 |
| FrameLab | DESIGN SYSTEM, EDITORIAL UI, MINIMAL CONTROLS, PASTEL UI | AESTHETIC, CINEMATIC, ILLUSTRATED, NEON, POLAROID, VINTAGE | 3 |
| Notes-Ecosistema | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, MINIMAL CONTROLS, NAVIGATION UI, NEO-APPLE, NEUMORPHISM, PALETTE, PASTEL UI, RETRO DESKTOP, SCENIC BACKGROUND, SCENIC ILLUSTRATION, SOFT 3D | AESTHETIC, NEON, ORGANIC, PIXEL ART, VINTAGE, Y2K RETRO | 24 |
| Pocket Guard | BENTO UI, MINIMAL CONTROLS, NEUMORPHISM, TOGGLE & SWITCH | AESTHETIC, NEON | 6 |
| SleepMax Coach | BENTO UI, DESIGN SYSTEM, ILLUSTRATED CONTROLS, MINIMAL CONTROLS, NATURE-TECH, NEUMORPHISM, PASTEL UI, SCENIC BACKGROUND, SKEUOMORPHISM, TOGGLE & SWITCH | AESTHETIC, CINEMATIC, ILLUSTRATED, NEON, ORGANIC, VINTAGE | 14 |
| Tabletop Motion Alarm | MINIMAL CONTROLS, NEUMORPHISM, TOGGLE & SWITCH | NEON | 1 |
| The Luminous Infinite Circle | DESIGN SYSTEM, GLASSMORPHISM, MINIMAL CONTROLS, NEO-APPLE, NEUMORPHISM, SKEUOMORPHISM, TOGGLE & SWITCH | AESTHETIC, NEON | 5 |
| TrailPath | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, NATURE-TECH, PALETTE, SKEUOMORPHISM, TOGGLE & SWITCH | AESTHETIC, CINEMATIC, NEON, ORGANIC, VINTAGE | 8 |
| Wonderlog | BENTO UI, DESIGN SYSTEM, EDITORIAL UI, ILLUSTRATED CONTROLS, MINIMAL CONTROLS, NATURE-TECH, NAVIGATION UI, PALETTE, PASTEL UI, SCENIC BACKGROUND, SCENIC ILLUSTRATION, SKEUOMORPHISM, SOFT 3D, TOGGLE & SWITCH | AESTHETIC, ANIME, CINEMATIC, ILLUSTRATED, ORGANIC, POLAROID, VINTAGE | 24 |
| World Days | DESIGN SYSTEM, EDITORIAL UI, MINIMAL CONTROLS, PALETTE, PASTEL UI, SCENIC BACKGROUND, SCENIC ILLUSTRATION | AESTHETIC, CINEMATIC, ILLUSTRATED, ORGANIC, POLAROID, VINTAGE | 12 |

## Modello relazionale

- **App —(N:M)— Stile**, mediata da una o più `UIR-xxxx`. Alcuni riferimenti hanno più famiglie UI/UX e più estetiche.
- Una stessa app può adottare più stili per componenti/schermate differenti, ma mantiene un **solo design principale approvato** dalla propria Product Bible.
- Lo stato `PROPOSTA` è applicato per app; non significa feature già in source/CI, non assegna nuovi ID CAP né introduce donor o Golden.
- Adozioni, cambi di roadmap, nuove capability e catalogo implementazioni sono operazioni distinte da questa registrazione visiva.
- Le immagini risultano pubblicamente visibili secondo l'utente, ma non sono presenti informazioni sulla licenza di redistribuzione per singola opera: non caricare file protetti nei repository pubblici. Il catalogo contiene solo titoli/hash/classificazioni.

## Come usare il catalogo

Si parte dall'app o dalla famiglia stilistica; si selezionano gli ID delle reference; si valuta il componente o tema rispetto a Product Bible, fattibilità e accessibilità; si cerca una CAP già registrata (es. CAP-0023 per design tokens, CAP-0024 per motion e CAP-0069 per screenshot QA); solo dopo si propone una roadmap o una prova tecnica. Per matrice delle capability rimane valida la registry canonica del presente repository.
