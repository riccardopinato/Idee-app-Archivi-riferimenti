# Riconciliazione stelle OSS → capability — 8 novembre 2026

**Tipologia:** evidence-backed research intake e inventario incrementale, NON nuove CAP certificate, NON approvazione di prodotto.
**Factory baseline:** `riccardopinato/App-Factory-Core@85ecbb19aeb02da1b9d04348e043f69bab77bcb9` (Master v27, Golden Index v28).
**Catalog base:** `riccardopinato/Idee-app-Archivi-riferimenti@6ed2a9b9983da45b0e1093d497d4c0ea9d0cde28`.
**Registro:** 160 CAP / 385 associazioni, Notes 88, Anna 74, 48 app/idee, prima dell'attuale PR.
**HEAD verificati nei 31 repository inventariati:** 27 invariati; 4 diversi (Anna, Notes, Factory Core, catalogo). `SOURCE_INVENTORY.json` viene aggiornato separatamente in questa PR. La comparazione di SHA NON prova runtime o completezza.

## Confini / qualità delle fonti

- Le 95 voci provengono dai **tre elenchi di repository selezionati nella chat (40 + 27 + 28)**, NON da una lettura autenticata live delle GitHub Stars. Non affermare che siano 95 stelle attuali né che siano tutte state aggiunte.
- Il catalogo storico [Analisi stelle](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github) è fermo a **632 repository pubblici enumerati il 24/10/2026**. Per confronto nominale 6/95 risultano già nello snapshot e 89/95 assenti; assente dallo snapshot NON dimostra stella appena acquisita.
- Mappatura per **ricerca/triage**: l'accostamento a un CAP è tematico, NON prova che il codice del donor soddisfi il contratto CAP. Per 16 progetti è fissato anche un HEAD esterno, che da solo non è attestazione E1/E3; il controllo di licenza, struttura, code path e test è ancora necessario.
- Alcune delle 95 voci furono risolte da descrizioni senza URL owner/repo originali; le corrispondenze meno sicure sono solo da valutare e NON donatori certificati.
- Nessun codice esterno acquisito, nessuna libreria inclusa, nessuna modifica alle app, nessuna modifica agli stati del registro per effetto del solo triage.
- [Issue catalogo #41](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/issues/41) e [roadmap Notes #60](https://github.com/riccardopinato/Notes-Ecosistema/issues/60) sono aperte; non anticipare la promozione delle 88 associazioni Notes a GIA_INTEGRATI.

## Differenze reali dagli app HEAD precedentemente inventariati

| Repository | Prima | Ora | Esito scoped |
|---|---|---|---|
| [Anna](https://github.com/riccardopinato/Agenda-per-Anna) | `cc192a59b5edf4a6ef82c4dfb45408a310f56890` | `e5b956caf7976b70afe8269fe55697f2af21c568` | 1 commit; roadmap/accettazione PWA e test responsive; [Development checks success](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/42416649963), [APK automation success](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/42417019018), senza inferire collaudo fisico |
| [Notes](https://github.com/riccardopinato/Notes-Ecosistema) | `e10b058a43e3b238e59eb946138540287756d784` | `d99a30633134e6e800e93e2a04741554d38c839b` | 18 commit, 66 file; Smart Inbox, project/dependency, PDF, restore, UI5; [Flutter Port CI success](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42418439788), [Web success](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42418439786), non prova full-scope CAP |
| [App-Factory-Core](https://github.com/riccardopinato/App-Factory-Core) | `1229d8c4d411fda76ccc58a6ed0118da1f7245e4` | `85ecbb19aeb02da1b9d04348e043f69bab77bcb9` | 8 commit, aggiornati routing e contratto capability |
| [Catalogo](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti) | `54705d4c5317e88d2a183cc5a47aa6e64ec886fc` | `6ed2a9b9983da45b0e1093d497d4c0ea9d0cde28` | 7 commit, report Anna/Notes e viste; [CI catalogo success](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/42416038027) sul main di partenza |

## Decisione di deduplicazione — match con CAP esistenti

| Ambito | Riferimenti OSS indicativi | CAP esistenti | Conseguenza |
|---|---|---|---|
| Notes: Smart Inbox/task strutturati | Joplin, Logseq, Super Productivity | CAP-0148, -0092, -0093 | completare delta degli writer canonici, nessun planner parallelo |
| Notes: dipendenze, WIP e planning | Plane, Vikunja, OpenProject | CAP-0103, -0106, -0102, -0105 | roadmap Notes #60 P1, niente promozione prima dei gate |
| Notes: ink, note collegate e mappe | Excalidraw, tldraw, Markmap | CAP-0028, -0029, -0094, -0098, -0149 | mantenere canvas/ink esistente |
| Notes: studio/documenti | AnkiDroid, Zotero, Paperless | CAP-0112, -0119, -0035, -0037 | verificare provenance, licenze, device e PDF |
| Notes: backup/privacy/collaborazione | CryptPad, Yjs, Automerge | CAP-0018, -0100, -0116 | CRDT *nuova opzione architetturale* da valutare, non autorizzare nuova sync |
| Anna: calendari e widget | Etar, Planner, Todo Agenda | CAP-0001, -0004, -0005, -0144 | mantenere agenda privata e UI5; no suite professionale |
| Anna: voice/diario | Whisper.cpp, Memos | CAP-0031, -0014, -0145 | audio locale opzionale e permessi espliciti |
| Work-Time-Keeper / FocuSense | ActivityWatch, Dayflow, Watson | CAP-0108, -0109, -0101 | candidati *per app* da valutare, niente sorveglianza implicita |
| CmdPocket / Notes | Dnote, MassCode, Espanso | CAP-0084, -0076, -0093 | nuovo possibile text-expander locale; no hook globale implicito |

Le CAP già associate ad Anna/Notes rimangono con gli **stati tecnici preesistenti** finché prova scoped, Product Bible e issue impediscono un upgrade. `CI_VERIFIED` implica il solo perimetro verificato, non esperienza mobile completa.

## Candidate nuove responsabilità (NON attribuire ID CAP senza review e sei-file kit)

1. **Editing a blocchi/Markdown con round-trip lossless**: valutare rispetto ai parser/editor e a CAP-0076/0093 (AppFlowy Editor, Milkdown, Editor.js); niente second source of truth.
2. **Convergenza CRDT per contenuti collaborativi offline**: confronto Yjs/Automerge con Shared Spaces Notes esistente, ACL, payload, test di conflitto e footprint.
3. **Viste relazionali/tabelle configurabili**: Grist, Baserow, NocoDB; valutare utilità e compatibilità Product Bible Notes, evitando un clone Notion.
4. **Text-expander locale per template contestuali**: Espanso; Notes/CmdPocket, senza cattura delle digitazioni delle altre app.
5. **Rilevamento esplicito del tempo di lavoro**: ActivityWatch/Dayflow; Work-Time-Keeper/FocuSense, consenso e retention.
6. **Snippet tecnico riusabile**: Dnote/MassCode; verificare non-duplicazione con code block e clipboard già esistenti.

**Nessuna nuova CAP-NNNN creata automaticamente:** prima serve un contratto non duplicato, ownership, decisione per ciascuna app, licenza, kit e rigenerazione delle viste. Questo è intenzionale, non una promozione falsa.

## Fonti OSS con HEAD bloccato alla data del triage

| Repo | Commit consultato | Ruolo |
|---|---|---|
| [AppFlowy-IO/appflowy-editor](https://github.com/AppFlowy-IO/appflowy-editor) | `01eccc6ee36bd07698bd80915289fe7070478cd2` | Fonte esterna di studio, **non donor certificato** |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | `69f43954f15a171b3a6edb45134d27b71560de02` | Fonte esterna di studio, **non donor certificato** |
| [yjs/yjs](https://github.com/yjs/yjs) | `db00ffdad8901900d5953e5cabc42302cf0f3756` | Fonte esterna di studio, **non donor certificato** |
| [automerge/automerge](https://github.com/automerge/automerge) | `09aeeabaa499c3aca50c48f33051a5accad0cc58` | Fonte esterna di studio, **non donor certificato** |
| [markmap/markmap](https://github.com/markmap/markmap) | `116bd2bdf1e5e428d11e5441d593969eea46451d` | Fonte esterna di studio, **non donor certificato** |
| [Etar-Group/Etar-Calendar](https://github.com/Etar-Group/Etar-Calendar) | `82ff55ea1fc035177054ce4b4aa8e0dd91059ef1` | Fonte esterna di studio, **non donor certificato** |
| [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | `e32e3a93be3aed4c9b8be024cd0e758d859547f4` | Fonte esterna di studio, **non donor certificato** |
| [baslawson/Planner](https://github.com/baslawson/Planner) | `7a9c9af3cce26e39412461fbbf8a419b90910509` | Fonte esterna di studio, **non donor certificato** |
| [super-productivity/super-productivity](https://github.com/super-productivity/super-productivity) | `08c605201890c3daf6849f8a9e20374c86bfba89` | Fonte esterna di studio, **non donor certificato** |
| [makeplane/plane](https://github.com/makeplane/plane) | `618d0eb74658329a6f6e92434ac54231422c5b96` | Fonte esterna di studio, **non donor certificato** |
| [AnkiDroid/Anki-Android](https://github.com/AnkiDroid/Anki-Android) | `67c05ca37aa340ffa4f7f6da7f0854500558345d` | Fonte esterna di studio, **non donor certificato** |
| [zotero/zotero](https://github.com/zotero/zotero) | `228f132e1a2c38745ae07bea6c1600b8bddc3b73` | Fonte esterna di studio, **non donor certificato** |
| [codex-team/editor.js](https://github.com/codex-team/editor.js) | `cfbf1daae2d722b1390c2f9a200868dd2ce8c46f` | Fonte esterna di studio, **non donor certificato** |
| [Milkdown/milkdown](https://github.com/Milkdown/milkdown) | `0655111f3bb8393e959ce3f3d107c83edce29c3a` | Fonte esterna di studio, **non donor certificato** |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | `6a8addd258eadd6563f8c582e8acc535e6325364` | Fonte esterna di studio, **non donor certificato** |
| [frappe/gantt](https://github.com/frappe/gantt) | `5c83708d300a99d9142edea0d4d52f421e3a2e68` | Fonte esterna di studio, **non donor certificato** |

## Inventario dei 95 riferimenti raggruppati per possibile riuso

> Le associazioni sono **candidature**; nessun valore è `SOURCE_CONFIRMED`, `APPROVATA`, `IN_ROADMAP` o `GIA_INTEGRATI` in virtù di questa tabella.

| # | Repository GitHub | Gruppo | Target ipotetico | Confrontare prima con |
|---:|---|---|---|---|
| 1 | [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 2 | [TriliumNext/Trilium](https://github.com/TriliumNext/Trilium) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 3 | [mattermost-community/focalboard](https://github.com/mattermost-community/focalboard) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 4 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 5 | [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 6 | [outline/outline](https://github.com/outline/outline) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 7 | [AppFlowy-IO/appflowy-editor](https://github.com/AppFlowy-IO/appflowy-editor) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 8 | [logseq/logseq](https://github.com/logseq/logseq) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 9 | [foambubble/foam](https://github.com/foambubble/foam) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 10 | [usememos/memos](https://github.com/usememos/memos) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 11 | [dendronhq/dendron](https://github.com/dendronhq/dendron) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 12 | [anyproto/anytype-ts](https://github.com/anyproto/anytype-ts) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 13 | [go-vikunja/vikunja](https://github.com/go-vikunja/vikunja) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 14 | [super-productivity/super-productivity](https://github.com/super-productivity/super-productivity) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 15 | [makeplane/plane](https://github.com/makeplane/plane) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 16 | [manuelernestog/weektodo](https://github.com/manuelernestog/weektodo) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 17 | [donetick/donetick](https://github.com/donetick/donetick) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 18 | [opf/openproject](https://github.com/opf/openproject) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 19 | [standardnotes/app](https://github.com/standardnotes/app) | Privacy e cifratura | Notes-Ecosistema; Anna solo Vault | CAP-0018, CAP-0114, CAP-0146 |
| 20 | [streetwriters/notesnook](https://github.com/streetwriters/notesnook) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 21 | [laurent22/joplin](https://github.com/laurent22/joplin) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 22 | [Laverna/laverna](https://github.com/Laverna/laverna) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 23 | [codexu/note-gen](https://github.com/codexu/note-gen) | Audio e AI locale | Notes-Ecosistema; Anna opzionale | CAP-0031, CAP-0074, CAP-0085, CAP-0095 |
| 24 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Audio e AI locale | Notes-Ecosistema; Anna opzionale | CAP-0031, CAP-0074, CAP-0085, CAP-0095 |
| 25 | [layzdonw/lazyaudio](https://github.com/layzdonw/lazyaudio) | Audio e AI locale | Notes-Ecosistema; Anna opzionale | CAP-0031, CAP-0074, CAP-0085, CAP-0095 |
| 26 | [amicalhq/prismical](https://github.com/amicalhq/prismical) | Audio e AI locale | Notes-Ecosistema; Anna opzionale | CAP-0031, CAP-0074, CAP-0085, CAP-0095 |
| 27 | [HabitRPG/habitica](https://github.com/HabitRPG/habitica) | Gamification e abitudini | Notes-Ecosistema; FocuSense | CAP-0109, CAP-0110, CAP-0145 |
| 28 | [dromse/obsidian-gamified-tasks](https://github.com/dromse/obsidian-gamified-tasks) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 29 | [appwrite/appwrite](https://github.com/appwrite/appwrite) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 30 | [taskade/taskade](https://github.com/taskade/taskade) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 31 | [OrangeCatzhang/orange-schedule](https://github.com/OrangeCatzhang/orange-schedule) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 32 | [FossifyOrg/Calendar](https://github.com/FossifyOrg/Calendar) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 33 | [vnotex/vnote](https://github.com/vnotex/vnote) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 34 | [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 35 | [linagora/twake-workplace](https://github.com/linagora/twake-workplace) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 36 | [nocodb/nocodb](https://github.com/nocodb/nocodb) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 37 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 38 | [AmmarAbouZor/tui-journal](https://github.com/AmmarAbouZor/tui-journal) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 39 | [wernerkruger/vscode-daily-planner](https://github.com/wernerkruger/vscode-daily-planner) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 40 | [shuaiplus/inkstone](https://github.com/shuaiplus/inkstone) | Snippet, strumenti e text expander | CmdPocket; Notes-Ecosistema | CAP-0076, CAP-0084, CAP-0093 |
| 41 | [LifetimeLabsHQ/PrivacyNotes.app](https://github.com/LifetimeLabsHQ/PrivacyNotes.app) | Privacy e cifratura | Notes-Ecosistema; Anna solo Vault | CAP-0018, CAP-0114, CAP-0146 |
| 42 | [regisdantas/gamify-tasks](https://github.com/regisdantas/gamify-tasks) | Gamification e abitudini | Notes-Ecosistema; FocuSense | CAP-0109, CAP-0110, CAP-0145 |
| 43 | [sharvesh1401/TaskTrail](https://github.com/sharvesh1401/TaskTrail) | Gamification e abitudini | Notes-Ecosistema; FocuSense | CAP-0109, CAP-0110, CAP-0145 |
| 44 | [FossifyOrg/Notes](https://github.com/FossifyOrg/Notes) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 45 | [baslawson/Planner](https://github.com/baslawson/Planner) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 46 | [Etar-Group/Etar-Calendar](https://github.com/Etar-Group/Etar-Calendar) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 47 | [nextcloud/calendar](https://github.com/nextcloud/calendar) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 48 | [andstatus/todoagenda](https://github.com/andstatus/todoagenda) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 49 | [jrnl-org/jrnl](https://github.com/jrnl-org/jrnl) | Calendario e diario personale | Agenda-per-Anna; Notes-Ecosistema | CAP-0001, CAP-0004, CAP-0005, CAP-0014, CAP-0144 |
| 50 | [saber-notes/saber](https://github.com/saber-notes/saber) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 51 | [tldraw/tldraw](https://github.com/tldraw/tldraw) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 52 | [xyflow/xyflow](https://github.com/xyflow/xyflow) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 53 | [sorenwacker/nodus](https://github.com/sorenwacker/nodus) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 54 | [nextcloud/notes](https://github.com/nextcloud/notes) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 55 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 56 | [Zettlr/Zettlr](https://github.com/Zettlr/Zettlr) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 57 | [pbek/QOwnNotes](https://github.com/pbek/QOwnNotes) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 58 | [docmost/docmost](https://github.com/docmost/docmost) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 59 | [BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 60 | [plankanban/planka](https://github.com/plankanban/planka) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 61 | [kanboard/kanboard](https://github.com/kanboard/kanboard) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 62 | [AnkiDroid/Anki-Android](https://github.com/AnkiDroid/Anki-Android) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 63 | [ankitects/anki](https://github.com/ankitects/anki) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 64 | [memrynote/memry](https://github.com/memrynote/memry) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 65 | [Pikos-App/pikos](https://github.com/Pikos-App/pikos) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 66 | [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Audio e AI locale | Notes-Ecosistema; Anna opzionale | CAP-0031, CAP-0074, CAP-0085, CAP-0095 |
| 67 | [cryptpad/cryptpad](https://github.com/cryptpad/cryptpad) | Privacy e cifratura | Notes-Ecosistema; Anna solo Vault | CAP-0018, CAP-0114, CAP-0146 |
| 68 | [markmap/markmap](https://github.com/markmap/markmap) | Canvas, ink e mappe | Notes-Ecosistema | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149 |
| 69 | [JerryZLiu/Dayflow](https://github.com/JerryZLiu/Dayflow) | Tempo e produttività | Work-Time-Keeper; FocuSense; Notes | CAP-0108, CAP-0109, CAP-0101 |
| 70 | [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | Tempo e produttività | Work-Time-Keeper; FocuSense; Notes | CAP-0108, CAP-0109, CAP-0101 |
| 71 | [wakatime/wakatime-cli](https://github.com/wakatime/wakatime-cli) | Tempo e produttività | Work-Time-Keeper; FocuSense; Notes | CAP-0108, CAP-0109, CAP-0101 |
| 72 | [projecthamster/hamster](https://github.com/projecthamster/hamster) | Tempo e produttività | Work-Time-Keeper; FocuSense; Notes | CAP-0108, CAP-0109, CAP-0101 |
| 73 | [jazzband/Watson](https://github.com/jazzband/Watson) | Tempo e produttività | Work-Time-Keeper; FocuSense; Notes | CAP-0108, CAP-0109, CAP-0101 |
| 74 | [todotxt/todo.txt-cli](https://github.com/todotxt/todo.txt-cli) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 75 | [GothenburgBitFactory/taskwarrior](https://github.com/GothenburgBitFactory/taskwarrior) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 76 | [mattgemmell/TaskPaperRuby](https://github.com/mattgemmell/TaskPaperRuby) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 77 | [bzg/org-mode](https://github.com/bzg/org-mode) | Task, progetti e organizzazione | Notes-Ecosistema; FocuSense | CAP-0092, CAP-0096, CAP-0100, CAP-0103, CAP-0105, CAP-0111 |
| 78 | [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 79 | [dnote/dnote](https://github.com/dnote/dnote) | Snippet, strumenti e text expander | CmdPocket; Notes-Ecosistema | CAP-0076, CAP-0084, CAP-0093 |
| 80 | [massCodeIO/massCode](https://github.com/massCodeIO/massCode) | Snippet, strumenti e text expander | CmdPocket; Notes-Ecosistema | CAP-0076, CAP-0084, CAP-0093 |
| 81 | [gristlabs/grist-core](https://github.com/gristlabs/grist-core) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 82 | [audreyt/ethercalc](https://github.com/audreyt/ethercalc) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 83 | [mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 84 | [baserow/baserow](https://github.com/baserow/baserow) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 85 | [seatable/seatable](https://github.com/seatable/seatable) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 86 | [amark/gun](https://github.com/amark/gun) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 87 | [yjs/yjs](https://github.com/yjs/yjs) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 88 | [automerge/automerge](https://github.com/automerge/automerge) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 89 | [berty/berty](https://github.com/berty/berty) | Backend, tabelle e sync | Notes-Ecosistema; infrastruttura, solo opt-in | CAP-0018, CAP-0096, CAP-0100, CAP-0118 |
| 90 | [ankicommunity/ankicommunity-sync-server](https://github.com/ankicommunity/ankicommunity-sync-server) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 91 | [zotero/zotero](https://github.com/zotero/zotero) | Documenti, OCR e studio | Notes-Ecosistema; PDF-Unifier | CAP-0035, CAP-0037, CAP-0112, CAP-0119 |
| 92 | [espanso/espanso](https://github.com/espanso/espanso) | Snippet, strumenti e text expander | CmdPocket; Notes-Ecosistema | CAP-0076, CAP-0084, CAP-0093 |
| 93 | [writefreely/writefreely](https://github.com/writefreely/writefreely) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 94 | [codex-team/editor.js](https://github.com/codex-team/editor.js) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |
| 95 | [Milkdown/milkdown](https://github.com/Milkdown/milkdown) | Note, diario, editor e knowledge | Notes-Ecosistema; Anna solo se compatibile | CAP-0013, CAP-0032, CAP-0076, CAP-0093, CAP-0148 |

## Next gate (priorità, senza implementazione)

1. **P1 Notes:** completare [#60](https://github.com/riccardopinato/Notes-Ecosistema/issues/60) (Smart Inbox #46 e Project Intelligence #51), con QA source/ACL/device separate. Poi riconciliare 88 associazioni in issue catalogo #41.
2. **P2 Notes:** interoperability/JSON Canvas e Study/PDF, con test no-loss e fonti riproducibili; evitare mutazioni automatiche.
3. **P2 Anna:** confrontare CAP-0144/0004/0005 con UI5 attuale e test reale due-device, senza nuovo store o provider.
4. **P2 Work-Time-Keeper / FocuSense:** audit prodotto per tracking consensuale e CAP-0108/0109; non promuovere sulla sola presenza di un progetto OSS.
5. **P3 CmdPocket:** verificare esistenza del repo reale e la decisione prodotto prima di associare codice, CAP o nuova app.

**Requisiti di un eventuale prossimo sync:** licenza per file, source SHA+path, test/CI del codice target, differenza funzionale, app product decision, `python3 scripts/build_catalog.py` + `--check`, `scripts/build_status_views.py` + `--check`, branch/PR/exact-head CI, device separato. Nessuna modifica a Source of Truth app, Factory, Golden o roadmap in questo step.
