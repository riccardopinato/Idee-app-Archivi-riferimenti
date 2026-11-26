# Crosswalk CAP / app — audit email 8 opportunità, 26/11/2026

**Stato: RICERCA, NON AMMISSIONE CAP e NON APPROVAZIONE.** Le proposte `AUDMAIL-20261126-01…08` sono registrate nel [dossier di idee](../11-NUOVE-IDEE/AUDIT_EMAIL_PROFONDO_8_OPPORTUNITA_2026-11-26.md). Questa vista serve per deduplicare prima di qualsiasi aggiornamento al registro JSON canonico: non modifica il suo source of truth né finge CI/QA.

| ID audit | Area | CAP esistenti con cui confrontare il delta | Ipotesi di delta non certificata | Issue research |
|---|---|---|---|---|
| 01 LifeCanvas | GalleryDrift, ponte Wonderlog/Anna | CAP-0011 Life Threads, CAP-0009 mappa ricordi, CAP-0159 clustering spaziale | percorso foto private locali → momento → export album; renderer Drift Core da riusare | [GalleryDrift #17](https://github.com/riccardopinato/GalleryDrift/issues/17) |
| 02 Procedure Engine | Notes | CAP-0093 note→checklist, CAP-0097 project memory Q&A, CAP-0076 web clip con fonte | esecuzione step persistente con evidenze, dipendenze, ripresa | [Notes #108](https://github.com/riccardopinato/Notes-Ecosistema/issues/108) |
| 03 Service Passport | nuova app B2B | CAP-0080 asset passport (ambito diverso), CAP-0043 fonte asset (non work-order) | registro tecnico/rapportino intervento per macchine fisiche | [Ideas #187](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/issues/187) |
| 04 Failure Intelligence | AppLab | CAP-0070 autonomous bounded repair, CAP-0055 diagnostics truth | correlazione e dedup read-only incidenti CI: NON autonoma repair | [AppLab #245](https://github.com/riccardopinato/AppLab/issues/245) |
| 05 Decision Studio | CashMate / Finance Intelligence | nessuna CAP chiaramente equivalente nel campione 199 | simulazioni deterministiche finanza quotidiana/PAC; finanza agent senza trading | [Finance #6](https://github.com/riccardopinato/Finance-Intelligence-Agent/issues/6) |
| 06 Kitchen Conductor | TasteAI / Cooking Anime | CAP-0044 anti-spreco, CAP-0155 relazione ingredienti, non un motore tempi | timeline multi-ricetta/dipendenze/timer risorse | [TasteAI #10](https://github.com/riccardopinato/TasteAI/issues/10) |
| 07 Art-to-Shot | ArtDrift / FrameLab | CAP-0041 palette foto e golden hour; non guida compositiva | insegnamento da opere documentate + overlay camera volontario | [ArtDrift #72](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/issues/72), [FrameLab #9](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/issues/9) |
| 08 Origin Passport | ArtDrift / World Days / FrameLab | **CAP-0043** raccolta fonti e audit artwork, CAP-0076 clipping provenienza (altro ambito) | manifest item-by-item, licenze/trasformazioni e publishing preflight | [ArtDrift #73](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/issues/73), [World Days #159](https://github.com/riccardopinato/World-Days/issues/159), [FrameLab #10](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/issues/10) |

## Discipline di ammissione
- **Nessun CAP-NNNN nuovo ora**: si tratta di ipotesi e non è stata effettuata la pipeline completa `scripts/build_catalog.py` / `--check`, né preparati i sei file tecnici canonici per ogni eventuale nuovo CAP. La matrice app/issue qui è il livello corretto per la ricerca preliminare.
- Prima della decisione di introdurre una nuova CAP, risolvere duplicati su `REGISTRO_CAPABILITY.json` e catalogare il perimetro del delta; quando ammessa, generare viste e kit e superare CI exact-head.
- Issue **research-only** nei repository consumer, senza modifica di `ROADMAP.md`, `Product Bible`, applicazioni, test o policy.
- **Destinazioni non direttamente aggiornate:** CashMate e Cooking Anime non sono stati trovati fra i repository accessibili con denominazione certa durante questa sessione. Le associazioni sono salvate nel catalogo e nei consumer tecnicamente accessibili (Finance Intelligence/TasteAI), senza inventare issue o percorsi.
- Wonderlog e Anna's Diary compaiono solo come eventuali bridge futuri per LifeCanvas: il bridge già presente richiede decisione specifica per foto private/consenso. Nessun issue autonomo per non duplicare backlog senza bisogno definito.
