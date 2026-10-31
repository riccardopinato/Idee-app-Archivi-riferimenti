# Repository, librerie e donor di codice

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

Questa lista è il sottoinsieme curatoriale, NON riproduce le 632 stelle del repo separato. Tutte le licenze vanno ricontrollate PRIMA di integrare codice commerciale.

[E] scrcpy | https://github.com/Genymobile/scrcpy | mirroring/controllo Android | AppLab Physical QA, Android QA Cockpit. Apache-2.0 storico.
[E] Joplin | https://github.com/laurent22/joplin | note offline/sync/encryption/history | Notes benchmark/pattern, NON copia casuale AGPL.
[E] Smart Edge | repo storico da ricaricare dall'audit stelle | overlay/edge toolbox | EdgeDock, App Profiles, Utility Android. MIT riportata nell'audit; verifica repo preciso.
[E] Wireless ADB Switch | https://github.com/Smooth-E/wireless-adb-switch | Wireless Debugging, Shizuku, Quick Tiles | Easy Debloat/DevBridge. GPL-3.0 storico: non copiare in app closed-source senza valutare copyleft.
[E] Universal Android Debloater NG | repo da risolvere nel registro stelle | classificazione debloat e liste OEM | Easy Debloat/CleanOS, pattern di sicurezza/whitelist.
[E] PdfUnifier | repo da risolvere nel registro stelle | merger PDF | PDF Pocket Tools; audit precedente segnalava assenza licenza: NO copia codice senza licenza.
[E] tldr-pages | https://github.com/tldr-pages/tldr | esempi comandi CLI | CmdPocket e Notes developer pack; attribuzione CC-BY 4.0 per pagine.
[E] Android architecture-samples | https://github.com/android/architecture-samples | Compose/ViewModel/Room/testing | Kotlin donor architecture.
[E] LeakCanary | https://github.com/square/leakcanary | memory leak debug | Battery Guard, Tabletop, Easy Debloat, QA; debug-only.
[E] MPAndroidChart | https://github.com/PhilJay/MPAndroidChart | grafici nativi | Battery Guard, TrailPath, SleepMax, FocusSense; verificare branch/versioni effettive.
[E] Tauri | https://tauri.app/ | shell desktop Rust/Web | Android QA Cockpit, Desktop Utility Factory.
[E] Colorwaver | repository da risolvere nel registro stelle | estrazione colori | FrameLab Palette Live concetto, clean-room secondo audit.
[E] Penpot | https://github.com/penpot/penpot | canvas/visual interaction/design tokens | Notes Visual Workspace/Factory design; verify MPL obligations.
[E] raylib | https://github.com/raysan5/raylib | piccoli giochi/graphics | Game Factory.
[E] Nakama | https://github.com/heroiclabs/nakama | backend giochi multiplayer | solo giochi con multiplayer reale.
[E] Shattered Pixel Dungeon | https://github.com/00-Evan/shattered-pixel-dungeon | roguelike open game | Game Factory; GPL-3.0 obligations.
[E] browser-use | https://github.com/browser-use/browser-use | automation research agent | AppLab possibile tool/pattern.
[E] crawl4ai | https://github.com/unclecode/crawl4ai | estrazione web per fonti autorizzate | source ingestion/editorial research, non aggira copyright/ToS.
[E] addyosmani/agent-skills | https://github.com/addyosmani/agent-skills | skills di coding | App Factory process.
[E] mattpocock/skills | https://github.com/mattpocock/skills | skill modulari | App Factory process.
[E] ECC (Everything Claude Code) | repository da risolvere nell'audit stelle | pattern agents/QA | AppLab process, no framework replacement automatic.
[E] ZXing | https://github.com/zxing/zxing | barcode core | BeerClass/Professional Wallet fallback; app scanner legacy non da copiare.
[E] GraphHopper | https://github.com/graphhopper/graphhopper | routing engine | TrailPath/WEB-009.
[E] Valhalla | https://github.com/valhalla/valhalla | route/trace engine | TrailPath/WEB-009.
[E] OSRM | https://github.com/Project-OSRM/osrm-backend | routing engine | WEB-009.
[E] OvertureMaps/data | https://github.com/OvertureMaps/data | POI open dataset | Geography/POI Core.
[E] Open-Meteo source | https://github.com/open-meteo/open-meteo | weather server AGPL | eventuale self-host; distinguere backend code license e data/API terms.
[E] SunCalc | https://github.com/mourner/suncalc | sole/luna computati localmente | WEB-012 e FrameLab.
[E] Nager.Date | https://github.com/nager/Nager.Date | festive calendario | WEB-013.
[E] libphonenumber | https://github.com/google/libphonenumber | phone parsing | WEB-001.
[E] OpenTopoData | https://github.com/ajnisbet/opentopodata | elevation DEM API | TrailPath.
[E] MapLibre | https://maplibre.org/ | map render SDK | TrailPath.
[E] Geofabrik | https://download.geofabrik.de/ | OSM bulk extracts | GeoData Core.
[E] Osmium | https://osmcode.org/osmium-tool/ | processing PBF | GeoData Core.
[E] DuckDB | https://duckdb.org/ | query GeoParquet/SQL | Overture POI pipeline.

REGISTRO SEPARATO DELLE STELLE (fonte storica fornita dall'utente):
https://github.com/riccardopinato/Analisi-delle-mie-stelle-github
L'audit del 24/10/2026 dichiarava 632 repo uniche enumerabili su 645 stelle mostrate, 13 gap da chiarire. Questo registro NON pretende che tutti i 632 repo siano stati verificati qui.

====================================================================

## Donor nuovi individuati da r/BestGitHubRepos — 2026-11-01

> Ricognizione documentale; nessun codice trasferito. [Schede e commit](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_REDDIT_BESTGITHUBREPOS_2026-11-01.md).

| Repository | Licenza snapshot | Capability e target | Modalita ammissibile |
|---|---|---|---|
| [OpenWhispr](https://github.com/OpenWhispr/openwhispr) | MIT | dettatura offline, diarizzazione; Notes, Anna, Wonderlog | valutare componenti native Android separati da Electron |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | AGPL-3.0 | TTS locale, modeli on-demand; Notes, Wonderlog | pattern, non copiare in app proprietaria senza compliance |
| [disktree](https://github.com/tobi/disktree) | MIT | treemap spazio file; Omni Cleaner | adattare UI, NON scanner NTFS desktop |
| [IT Tools](https://github.com/CorentinTh/it-tools) + [fork sharevb](https://github.com/sharevb/it-tools) | GPL-3.0 | conversioni locali; DevPocket, CmdPocket | reference/clean-room salvo compatibilita copyleft |
| [Dextop](https://github.com/NarYuki/Dextop) | GPL-3.0 | compatibility probe e desktop layout; EdgeDock/App Profiles | reference, hidden API/OEM Play gate, HyperOS disabled |
| [OpenResearch](https://github.com/alphaXiv/OpenResearch) | MIT | research experiment ledger; AppLab/portfolio | adapter leggero senza secondo orchestrator |
| [God's Eye View](https://github.com/bilawalsidhu/gods-eye-view) | metadata NOASSERTION; README MIT | layer di segnali e geo scene; TrailPath/Wonderlog/CamperBoss | solo reference, feed e assets a licenze autonome |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Apache-2.0 | scope creep detector; AppLab | singoli pattern/skill con audit dipendenze |
| [free-ai-tools](https://github.com/ShaikhWarsi/free-ai-tools) | MIT | scouting provider; tutte | elenco non fonte autoritativa di prezzi o limiti |

**Non duplicare** `mattpocock/skills`: era gia stato censito. Rileggere licenza e commit prima di qualunque riuso.
