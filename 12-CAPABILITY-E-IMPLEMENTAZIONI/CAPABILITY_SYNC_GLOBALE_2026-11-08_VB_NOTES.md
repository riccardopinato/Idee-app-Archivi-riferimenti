# Capability globale — riconciliazione incrementale 08/11/2026

**Decisione operativa:** applicare un *research crosswalk* agli ID esistenti e aggiornare l'inventario HEAD/CI; **nessuna nuova CAP**, nessuna promotion, nessuna decisione prodotto inventata.

## Baseline e controllo
- Factory: `riccardopinato/App-Factory-Core@c709e483d40424c88b6ba316d0c8352eec5370fe` (Master v27, Golden Index v28).
- Catalogo prima/dopo: **199 CAP / 441 associazioni / 48 nomi app**.
- Repository account owner: **31/31 visibili, 31/31 HEAD letti**, 28 invariati, 3 variati. Dei 3, **1 app (Notes)** e **2 infrastrutture (Factory + archivio)**.
- Non presume che altri repository fuori dall'account collegato siano accessibili. Riconoscere i 48 nomi app/idee del registro, senza convertirli automaticamente in 48 repo reali.
- I 28 progetti HEAD invariati preservano stati. Verifiche provider/device, review Product Bible e source gaps precedenti rimangono aperti.

## Delta Notes-Ecosistema
- Prima `d99a30633134e6e800e93e2a04741554d38c839b`, dopo **`f11ca0bee1594ccf95ca2876a1df0c658459aeb4`**; un commit merged [PR #84](https://github.com/riccardopinato/Notes-Ecosistema/pull/84).
- `flutter_app/lib/src/domain/mobile_navigation_ui5.dart`, `flutter_app/lib/src/app.dart`, `flutter_app/test/mobile_navigation_ui5_test.dart`, `flutter_app/UI5_NAV_B4_2026_11_07.md`: preview **five tabs Home/Notes/Tasks/Diary/Spaces** per mobile, canonical Search 5 stays reachable and rail 6 destinations retained on desktop. Flag `NOTES_UI5_NAV_PREVIEW` default **false**.
- [CI verify exact-head](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42439836027) PASS: analyze, Flutter tests, debug APK build. [Build web](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42439836033) PASS. **No physical UI5 validation, no default-on proof**.
- CAP-0025 (responsive rail/split) is an **overlap to investigate**, not proven full contract: no new Notes CAP association or CI_VERIFIED promotion. CAP-0147 concerns **Home modular reordering**, not five-tab navigation; state unchanged.

## Vision Board: research matching, non ammissione
- [Registry fonti Vision Board alla SHA](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/b57b6bee09528457e7e920216b8bc907b596e508/15-VISION-BOARD/REGISTRO_FONTI_VB.json) contains 39 unique refs, 28 repos SHA-pinned, 10 topics with URL, 1 unverified alias, 28 extractions candidate. One duplicate intake URL was already VBR-0001.
- **12 CAP esistenti, 60 VBR↔CAP links; no new CAP or product status change.** Source references E1 are read-only technical snapshots; Topics E0 are discovery, no donor proof.

| CAP | Titolo | VBR links | E1 repo refs | Gate specifico |
|---|---|---:|---:|---|
| [CAP-0027](REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | 4 | 4 | Capture patterns only; external source does not certify private media import into app. |
| [CAP-0028](REGISTRO_CAPABILITY/CAP-0028.md) | Connettori visuali tra post-it | 4 | 4 | Scene connectors and bindings are external research, not proof of Notes connector end-to-end. |
| [CAP-0029](REGISTRO_CAPABILITY/CAP-0029.md) | Canvas ibrida sketch sotto note | 12 | 12 | Canvas research extends existing Notes Visual Workspace; prevent a second editor/storage. |
| [CAP-0075](REGISTRO_CAPABILITY/CAP-0075.md) | Import Center per migrazioni utenti | 6 | 6 | Import/export ideas only; migrations require staging/validation and permission gates. |
| [CAP-0094](REGISTRO_CAPABILITY/CAP-0094.md) | Sticky Kanban con task canoniche su canvas e planner | 6 | 6 | All Kanban examples must project canonical task IDs; no second task store. |
| [CAP-0098](REGISTRO_CAPABILITY/CAP-0098.md) | Mind map navigabile derivata da note e documenti | 4 | 4 | Mind-map/graph sources do not prove an implemented Notes consumer. |
| [CAP-0099](REGISTRO_CAPABILITY/CAP-0099.md) | Planner studio e progetto da obiettivi in checklist | 7 | 7 | Goal planning patterns are optional and do not approve automatic task creation. |
| [CAP-0104](REGISTRO_CAPABILITY/CAP-0104.md) | Timeline obiettivi e pianificazione a ritroso | 4 | 4 | Milestone and reverse planning remain proposal; no event writing without confirmation. |
| [CAP-0136](REGISTRO_CAPABILITY/CAP-0136.md) | Scontorno foto in elementi canvas riutilizzabili | 2 | 2 | NEGATIVE CONTRACT MATCH: Easy Crop / Fabric geometry does not perform image segmentation or cutout. |
| [CAP-0147](REGISTRO_CAPABILITY/CAP-0147.md) | Home modulare riordinabile con preferenze locali | 4 | 4 | Responsive layout/drag patterns are not evidence that personalized Home already runs. |
| [CAP-0148](REGISTRO_CAPABILITY/CAP-0148.md) | Smart Inbox verificabile da fonte ad azione canonica | 1 | 1 | Related to visual intake only; not proof of a verified Smart Inbox workflow. |
| [CAP-0149](REGISTRO_CAPABILITY/CAP-0149.md) | Interoperabilita JSON Canvas v1 con report di perdita | 6 | 6 | Excalidraw/Fabric/.drawnix formats do NOT equal JSON Canvas v1; require adapters and lossiness reporting. |

**Fonti con licenze commerciali da chiarire**: tldraw SDK custom production-license; AFFiNE mixed MIT/MPL/EE per file; AppFlowy AGPLv3; PLANKA Community Fair Use/Pro; Focalboard source AGPL/compiled binary MIT only. Progetti senza LICENSE non autorizzano copia. Biblioteche MIT richiedono comunque notice/dipendenze/asset check. Non copiare né attribuire risultati runtime agli OSS.

## Tre assi per app — vincoli conservati
- **Tecnico:** `app_states` di tutti e 441 rapporti invariati; Notes CAP-0029/0098 `SOURCE_REPORTED` restano DA_VERIFICARE. Le CAP 0028/0094/0099/0104/0149 Notes e 0147 Anna sono `PROPOSTA`; la CI di Notes UI5 non promuove quelle CAP.
- **Decisioni prodotto:** tutte le `app_product_decisions` documentate invariati, inclusi i 56 entry E0 OSS95. Non inventate APPROVATA/IN_ROADMAP/RINVIATA/SCARTATA.
- **Completamento:** nessun dispositivo o scenario Vision Board testato. Estrazioni VBE-001..028 e possibili Golden restano candidate.

## Coda istruttoria, non roadmap né task già autorizzati
Ordine qualitativo per scenario VB/Notes/Anna. Score e facilità sono **stime già presenti nel JSON**, non metriche misurate; le voci `PROPOSTA` non diventano eseguibili senza ammissione prodotto.

| Ordine | CAP / app | Score | Facilità | Stato tecnico | Blocco/next gate |
|---:|---|---:|---:|---|---|
| 1 | [CAP-0028](REGISTRO_CAPABILITY/CAP-0028.md) / Notes-Ecosistema | 91 | 97% | `PROPOSTA` | Conferma Product Bible; test edge lifecycle, undo, hit test e ID unici. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0028/README.md) |
| 2 | [CAP-0094](REGISTRO_CAPABILITY/CAP-0094.md) / Notes-Ecosistema | 85 | 87% | `PROPOSTA` | Conferma scope; dimostrare una sola ownership task e drag/undo. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0094/README.md) |
| 3 | [CAP-0104](REGISTRO_CAPABILITY/CAP-0104.md) / Notes-Ecosistema | 87 | 85% | `PROPOSTA` | Dipende da planner/task canonici; date confermate; no auto-write. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0104/README.md) |
| 4 | [CAP-0149](REGISTRO_CAPABILITY/CAP-0149.md) / Notes-Ecosistema | 81 | 67% | `PROPOSTA` | Staging/import export test; formati Excalidraw != JSON Canvas. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0149/README.md) |
| 5 | [CAP-0147](REGISTRO_CAPABILITY/CAP-0147.md) / Agenda-per-Anna | 81 | 65% | `PROPOSTA` | Product Bible Anna, UI5 responsive/screenshots, accessibilità. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0147/README.md) |
| 6 | [CAP-0099](REGISTRO_CAPABILITY/CAP-0099.md) / Notes-Ecosistema | 73 | 85% | `PROPOSTA` | Conferma; riuso CAP-0093 checklist e planner. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0099/README.md) |
| 7 | [CAP-0029](REGISTRO_CAPABILITY/CAP-0029.md) / Notes-Ecosistema | 84 | 76% | `SOURCE_REPORTED` | Source/CI/device whiteboard, save/reload e export; no reimplementazione. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0029/README.md) |
| 8 | [CAP-0098](REGISTRO_CAPABILITY/CAP-0098.md) / Notes-Ecosistema | 78 | 70% | `SOURCE_REPORTED` | Source/CI binding a note, reconnect, migrazioni. [Kit](../../13-KIT-INTEGRAZIONE/CAP-0098/README.md) |

**Candidate non numerata da riesaminare:** VisualBoard GoalRefs+MediaRefs (composizione obiettivi, ricordi, immagini con ownership canonica, progresso e privacy). Valutare se davvero distinta da CAP-0029/0094/0099/0104 prima di qualsiasi CAP-0200; richiede Product Bible target e test di non duplicazione. **Non ammessa** in questo run.

## Gate di qualità e metriche
- 31 HEAD verificate; 28 invariati; 3 mutati: 1 app source diff + 2 infrastruttura. Nuove app trovate: **0** fra 31/31 repo collegati.
- 12 CAP existing con nuovi pointer a fonti; 60 matching; 0 nuove CAP; 0 nuove associazioni; 0 promozioni CI/device/release; 0 nuove decisioni prodotto; 0 regression di rating o score.
- Aggiornati *solo* registro dei riferimenti nella CAP registry (metadata non consumati dal generatore), SOURCE_INVENTORY, questo report e README catalogo. Output derivati dal generatore devono rimanere byte-identici perché non sono mutati score, states, source principale, reviewed_at, app association o `updated_at`.
- **Build gate:** `scripts/build_catalog.py --check`, `scripts/validate_ml_intake.py`, `capability_registry_test.py`, `status_views_test.py`, `projects_sync_test.py`, `projects_sync.py --mode dry-run` eseguiti nel workflow PR (verificare il risultato e exact SHA prima del merge); il comando Python `build_catalog.py` senza `--check` non è stato eseguito in questo ambiente.

## Prossima capability consigliata
**CAP-0028, connettori visuali tra post-it per Notes**, **solo dopo ammissione in Product Bible**. Il rischio di duplicare core è basso se si aggiungono soltanto edge con ID canonici; priorità editoriale 91/100, facilità stimata 97%. In alternativa, primo gate a basso rischio già in corso: verifica fisica della UI5 Notes (flag ON) prima di nuove funzionalità.
