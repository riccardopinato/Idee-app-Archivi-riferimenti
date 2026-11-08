# Audit comparativo — 20 riferimenti Vision Board, 2026-11-08

## Perimetro ed evidence
- **20 input**, nell'ordine ricevuto; 15 repository reali con SHA 40 caratteri, README, albero e file sorgente mirato (E1). VBR-0011 ha soltanto README e LICENSE: analisi documentale, non code audit. Cinque directory GitHub Topics E0 senza commit, license o code donor.
- Nessuna build, test unitario indipendente, benchmark, device/Play/Web runtime o certificazione. Test esistenti nei repo non sono test eseguiti qui. La selezione dei sorgenti è mirata, non un audit security completo delle codebase.
- **Factory baseline** App-Factory-Core@c709e483d40424c88b6ba316d0c8352eec5370fe; Master v27, Golden Index v28. Capability registry verificato a 199 record, senza modifiche.

## Correzioni documentate alle descrizioni ricevute
- **VisionBoard-Vanilla (VBR-0004):** static HTML/CSS; upload/drag/save risultano roadmap, non funzioni disponibili nel sorgente.
- **Moodboard Studio (VBR-0011):** solo README + LICENSE, senza app/source; license proprietaria all-rights-reserved. PDF export descrittivo, non codice auditabile.
- **Boardfish (VBR-0012):** codice e molti test presenti, formato .bf/imageStore; LICENSE vieta business/paid redistribution senza permesso. Pattern sì, codice commerciale no.
- **ImageCanvas (VBR-0013):** MIT; algoritmi verificabili in LayoutEngine.swift (tiled/cascading/picasa), board locale con refs in BoardStore.swift; Swift/macOS soltanto, pen drawings session-only.
- **Drawnix (VBR-0017):** MIT e sistema plugin, serializzazione `.drawnix`; non è automaticamente JSON Canvas v1.
- **Konva (VBR-0018):** MIT e HTML5 Canvas Web/JS; non è Flutter nativo.
- **dev.fast Whiteboard (VBR-0020):** MIT root, protocolli versioned per board agentica e sottoprogetti/licenze separate; non è dreamboard consumer.
- **Envision (VBR-0006):** Pixabay API key nel codice frontend; non riusare secret e non considerare Pixabay asset free by default.
- **niral28 (VBR-0015):** Canvas cluster/suggestions, ma pipeline agentica Gemini cloud+Chrome CDP; non etichettare on-device.
- **sbendimerad (VBR-0002):** goal behavior tracker Streamlit/Neon, non editor di immagini.
- **ckaiser (VBR-0005) e jeanarose (VBR-0003):** fork con upstream fissati nel registro; backend Rails del primo separato dal frontend auditato.
- **xgicmt (VBR-0008):** Rails 2015, shared_link generato before_save; richiede token lifecycle/threat model.
- **khalid (VBR-0009):** Liveblocks/Clerk/Neon collaborative cloud; non default raccomandato per Anna.
- **irisyann (VBR-0014):** Gallery React dipendente da Pexels e suoi termini.

## Licensing dei 15 repository (Topic esclusi)
| Scope verificato | N | Fonti |
|---|---:|---|
| MIT in file LICENSE | 4 | VBR-0013 ImageCanvas, VBR-0017 Drawnix, VBR-0018 Konva, VBR-0020 dev.fast |
| MIT nel README frontend | 1 | VBR-0005 ckaiser (backend fuori scope) |
| Restrizione commerciale / proprietaria | 2 | VBR-0012 Boardfish, VBR-0011 Moodboard Studio |
| Nessuna licenza nel tree ispezionato | 8 | VBR-0002, 0003, 0004, 0006, 0008, 0009, 0014, 0015 |

Asset, font, immagini, foto da Pexels/Pixabay/GIPHY, dipendenze e servizi richiedono ToS/clearance separati. Niente copia in app commerciali senza compatibilità del file.

## Sintesi per consumer
**Notes, ricerca P1:** layout da ImageCanvas (port Flutter), interfacce/documenti Drawnix, Konva **solo se** serve specifica superficie Web JS; Boardfish **solo come riferimento non copiato**. P2: goal tracker sbendimerad, relazioni board→goal ckaiser, cluster niral riscritto local-first senza Gemini/CDP. dev.fast per tool di progettazione/software, non Notes consumer.

**Anna, ricerca P1:** collage e layout ImageCanvas, UX guidata jeanarose, concetti portabili Boardfish in implementazione autonoma. P2: progress visuale goal/ricordi, export PDF e schede vision come funzioni opzionali. Nessuna migrazione al sistema Notes, nessun contenuto condiviso in Noi ♡ senza consenso esplicito.

## Crosswalk con CAP e Golden correnti
CAP-0028 connettori post-it; CAP-0029 canvas ibrida (Notes `SOURCE_REPORTED`); CAP-0098 mind map (Notes `SOURCE_REPORTED`); CAP-0099 planner goal (Notes `PROPOSTA`); CAP-0104 timeline milestone (Notes `PROPOSTA`); CAP-0075 Import Center; CAP-0149 JSON Canvas (Notes `PROPOSTA`). Fonte Factory: Infinite Canvas/Ink Engine **Draft**, core implementato ma widget/gestures/consumer non interamente certificati. Nessun matching implica funzione già operativa.

## 14 estrazioni, priorità e gate
[Tabella dettagliata VBE-001..014](ESTRAZIONI_CANDIDATE.md). Una eventuale nuova CAP «Vision Board come vista GoalRefs+MediaRefs» richiede anti-duplicazione e normale processo CAP. Un Golden Layout/Media Pack richiede contratto Dart, license gate, fixture, benchmark Android/Web e riuso indipendente. Nessuna nuova Golden o CAP creata.

## Test raccomandati prima dell'adozione
Viewport zoom/pinch, move/rotate, undo/redo, griglie multi-aspect, export/import round-trip, immagini mancanti, corrupted JSON, 1k media low-end, account switch, privacy/sync offline, font scale, rights attribution, footprint APK e responsive Web. Solo a valle di Product Bible e roadmap autorizzate.
