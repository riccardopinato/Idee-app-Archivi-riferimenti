# Audit completo Flutter e benchmark liste World Days — 09/11/2026

**Modalità:** QA read-only su checkout GitHub Actions, sorgenti Flutter reali; benchmark su widget effettivi di World Days in runner Linux.  
**Baseline Factory:** `riccardopinato/App-Factory-Core@a6d7ff36db7f70b03ccfdf02fa265049d31ae2f1` (Master v27 / Golden Index v29).  
**Scansione pubblica:** [GitHub Actions run 42538515322](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/42538515322) · [run finale 42538824133](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/42538824133).  
**FrameLab privato:** [run privato 42538883595](https://github.com/riccardopinato/FrameLab-Google-AI-Studio/actions/runs/42538883595) · dettagli rimangono in un artifact del repository privato.  
**Metriche JSON:** [13 repo](FLUTTER_FULL_SOURCE_SCAN_2026-11-09.json) · [8 scenari di World Days](WORLD_DAYS_LIST_BENCHMARK_2026-11-09.json).

## 1. Risultato scanner su checkout completi

- Inventario owner verificato: **31 repository**. **12** repository Flutter pubblici analizzati da cloni completi; **1** Flutter privato analizzato in proprio runner con checkout privato. Altri repo sono Kotlin/non Flutter oppure infrastruttura.
- **1.467 file Dart** effettivamente analizzati (**1.390 pubblici + 77 privati**). Il filtro esclude generati e path non pertinenti; per ogni repo SHA e raggruppamento dei pattern sono nel JSON.
- **0 match di API LEGACY_API nel set circoscritto** (tra cui `RaisedButton`, `FlatButton`, `OutlineButton`, `Scaffold.of(...).showSnackBar`, istanza storica `Geolocator()`). Non significa assenza di tutte le API deprecate in Flutter, né certificazione `flutter analyze`.
- I `REVIEW` sono **indicatori euristici, non bug**: `ListView(children:...)` può essere appropriato, `dart:io` può essere isolato per piattaforma e `SharedPreferences.getInstance()` è una API legacy ancora supportata. **Nessun refactor automatico**.
- Indicatori puntuali da ispezionare se si apre uno step futuro: Anna `async_void_handler` 1, Cooking Anime `legacy_theme_field` 6; entrambi classificati REVIEW e **non dimostrati difetti**.

| Repository | SHA sorgente | Dart letti | Pattern legacy | Segnali REVIEW |
|---|---|---:|---:|---:|
| Agenda-per-Anna | `9f2c308099` | 300 | 0 | 245 |
| App-corpo-umano | `0a0cdbd256` | 10 | 0 | 37 |
| app-fotografia | `e7538d7dfc` | 75 | 0 | 14 |
| Battery_Guard | `d8cf237ab2` | 62 | 0 | 12 |
| CamperBoss | `ae30d08f23` | 213 | 0 | 34 |
| Design-App | `546a1c1878` | 24 | 0 | 6 |
| In-Cucina-con-gli-Anime | `478f6db6d6` | 56 | 0 | 11 |
| Notes-Ecosistema | `2780847a07` | 223 | 0 | 110 |
| TasteAI | `fc2f80e43f` | 59 | 0 | 14 |
| TrailPath | `3f44ab37c0` | 69 | 0 | 15 |
| Wonderlog | `b4840e8453` | 213 | 0 | 39 |
| World-Days | `bb662cb215` | 86 | 0 | 20 |
| FrameLab-Google-AI-Studio (privato) | `7104ecc847` | 77 | 0 | 16 |

**Nota copertura:** `Cozy-game-nome-da-scegliere-` e `desktop-tutorial` sono privati ma gli alberi GitHub consultati riportano 0 sorgenti Dart/0 pubspec Flutter; FrameLab-Google-AI-Studio è invece Flutter ed è stato scansionato in ambiente privato. Il totale 13 deriva dalla detection del framework nel sorgente, non dalla memoria storica della chat.

## 2. Benchmark World Days — sorgente pinned

**Repo:** `riccardopinato/World-Days@bb662cb21506b6157658f43070c2059c960637b5`  
**Flutter SDK CI:** 3.47.3 · **viewport:** 480×844 px logici · **2 warmup e 7 sample per scenario**.  
**Che cosa si misura:** wall-clock intorno a `tester.pumpWidget` + `tester.pump` su `SavedPage` e `AroundTheWorldPage` reali; **non** frame budget GPU, jank reale, tempo di scrolling o memoria su smartphone.

| Record sintetici | Salvati mediana ms | Salvati P95 ms | Figli ListView | In giro mediana ms | In giro P95 ms | Figli ListView |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 71.043 | 79.334 | 32 | 39.846 | 44.643 | 24 |
| 50 | 55.101 | 73.993 | 112 | 35.731 | 37.49 | 104 |
| 150 | 48.502 | 51.461 | 312 | 33.681 | 38.296 | 304 |
| 300 | 47.447 | 55.477 | 612 | 35.048 | 41.431 | 604 |

**Contesto del dataset generato dall'app:** 296 giornate totali; massimo **4** associate a un singolo paese (US) e **2** per l'Italia. Il numero reale di righe di `AroundTheWorldPage` è quindi piccolo, perché la pagina filtra per nazione. Gli stress test 50/150/300 sono volutamente fuori dalla densità attuale di una schermata per Paese. La vista `Salvati` può invece teoricamente avere fino a 296 preferiti.

**Conclusione performance:** la lista delle card viene costruita eager nel delegate (a 300 record: 612 figli in Salvati, 604 in In giro), ma i mounted `ObservanceCard` nella viewport sono rispettivamente solo ~6 e ~4; i dati non dimostrano peggioramento monotono di mediana con N. Il run ha effetto di warmup/ordine di esecuzione (dimensioni crescenti): **non stimare un miglioramento percentuale** con `ListView.builder` dai numeri raccolti. Non raccomandare refactor immediato in `AroundTheWorldPage`; per Salvati un eventuale test su dispositivo con dataset favoriti molto ampio può giustificare un change mirato.

## 3. Bug UI riprodotto separatamente a 390px

Nel primo run widget test a **390×844** con locale `it`, `AroundTheWorldPage` ha lanciato **RenderFlex overflowed by 12 pixels on the right** nel `DropdownButtonFormField<String?>` di `lib/features/discover/around_the_world_page.dart:57`. Il secondo run ha confermato il medesimo difetto con un test UI separato che registra una eccezione: `renderflex_overflow_detected=true`. Il benchmark prestazionale è stato quindi eseguito a 480px senza nascondere il bug 390px.

**Issue operativa:** [World Days #52 — P2 overflow selettore Paese](https://github.com/riccardopinato/World-Days/issues/52). Intervento candidato: testare `isExpanded`/vincoli del dropdown e truncation delle opzioni, regressioni a 320/360/390/480, testo scalato, IT/EN/DE. Non è stata apportata alcuna correzione production.

## 4. Decisioni e gate

| Elemento | Decisione |
|---|---|
| Modernizzazione generica API Flutter | **NON NECESSARIA ORA** per i pattern legacy cercati |
| World Days In giro — lazy list | **RINVIARE** (massimo 4 record attuali per Paese) |
| World Days Salvati — lazy list | **P2 VERIFICA** su dataset 250–296 preferiti e dispositivo, non bug provato |
| World Days Dropdown 390px | **P2 BUG CONFERMATO**; issue #52, prossimo fix test-driven |
| Dart IO e SharedPreferences | **REVIEW**; mantenere adapter/migrazioni finché non emerge un difetto concreto |
| Nuovi Donor / Golden / CAP | **0 promozioni**, richiedono contratti e prove per consumer |
| App code, release, cloud, dati | **nessuna modifica** |

**Metodo:** `scripts/run_portfolio_flutter_source_scan.py` clona i repository pubblici e chiama il scanner read-only versionato `scripts/audit_flutter_antipatterns.py`; FrameLab privato usa il medesimo scanner (pinned SHA) nel proprio runner; `benchmark/world_days_lists_perf_test.dart` viene copiato *solo nel checkout temporaneo CI* di World Days e cronometra i widget effettivi; `scripts/parse_world_days_widget_bench.py` conserva raw sample in JSON. Niente dati reali utenti, secrets o attività background nelle app.

**Stato:** 13/13 Flutter identificati da inventario disponibili scansionati a livello di sorgenti, benchmark widget 8/8 + un test overflow riprodotto, evidenze GitHub Actions PASS. **Non** equivalgono a `flutter analyze` totale, prestazioni device/profile, QA fisico o validazione Store.
