# Notes-Ecosistema — Riconciliazione esplorativa 88/88 CAP (Cantiere D)

**Data:** 2026-11-07 · **Repository app:** `riccardopinato/Notes-Ecosistema@abbcab3b59bb67462238ad047fd619935a9acc0b` · **Catalogo:** `riccardopinato/Idee-app-Archivi-riferimenti@b99c87bbd302a09244f8d9c91d748595545c5445` · **Core:** `3481a8190a5db5965bb22f84832094268d05be98`.

## Vincoli dell'audit
- **88 associazioni Notes-CAP / 88 ID unici** riletti da `PER_APP/Notes-Ecosistema/TABELLA.csv`: **16 SOURCE_REPORTED** e **72 proposte/roadmap storiche**, zero promozioni in `GIA_INTEGRATI` nel catalogo.
- Questo è un **crosswalk di audit non canonico**. Non cambia `REGISTRO_CAPABILITY.json`, score, `app_states` o viste generate, in accordo con issue [catalogo #41](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/issues/41) che ne prescrive l'aggiornamento **post-roadmap #60**, con gate completi e rigenerazione delle viste.
- `CODICE_CANDIDATO_DA_VERIFICARE` = esiste indizio puntuale nel source, **non** CAP integrata. `MVP_PARZIALE_PR_MERGED` = PR #65/#66/#67/#68/#69 citate da Notes issue #64, **non** contratto CAP completo. `INDIZIO_CODICE_SCOPE_DA_VERIFICARE` = riuso o funzione analoga, ma comportamento richiesto non provato. `NESSUNA_PROVA_PUNTUALE_AUDIT` = non censita da questa verifica mirata, **non** assente dal progetto.
- Nessun `DEVICE_VERIFIED` o `RELEASE` attribuito. La CI e la review del codice non attestano QA fisica, firma production, licenze o copertura integrale del contratto CAP.
- Le proporzioni sono inventario di stati, non uno score percentuale di completamento reale.

## Contatori verificati
| Classe | Numero |
| --- | ---: |
| Associazioni Notes con indizio codice/test individuato in questo audit | 46 |
| Di cui 5 MVP #64 con PR mergiate ma scope residuo | 5 |
| SOURCE_REPORTED originali | 16 |
| PROPOSTA o ROADMAP_STORICA originali | 72 |
| Associazioni senza evidenza puntuale attribuita in questo audit | 42 |
| **Totale associazioni** | **88** |

## Priorità operative e dipendenze
A: build/release/restore (#72/#75/#70/#71). B: spec UI5 mobile Home/nav, nessun tocco a writer C. C: Smart Inbox #46 poi Project Intelligence #51, portability #48/#49, document/study #47. D: questa matrice, monitorata ma **nessuna promozione canonica** prima del gate issue #41.

### 16 SOURCE_REPORTED — source-review mirata
| CAP | Funzione | Indizio sorgente Notes | Delta / test mancante |
| --- | --- | --- | --- |
| CAP-0093 | Da note a checklist strutturate | `flutter_app/lib/src/domain/note_to_checklist.dart` | Parser+task canonico: verificare flusso sorgente/ACL e cap completo |
| CAP-0152 | Ricerca fuzzy offline per refusi e alias | `flutter_app/lib/src/domain/note_local_signals.dart` | Fallback fuzzy Unicode: recall/false-positive, ricerca 1 carattere, 500/5000 |
| CAP-0017 | Universal Delete Trash e lifecycle audit | `flutter_app/test/lifecycle_test.dart` | Trash esistente: regressioni cross-sidecar/GC e test Android |
| CAP-0160 | Estrazione TF-IDF di parole chiave e tag suggeriti | `flutter_app/lib/src/domain/note_local_signals.dart` | TF-IDF proposte tag: 6 locale, source/ACL, nessuna scrittura automatica |
| CAP-0071 | Offline content packs incremental sync | `flutter_app/lib/src/data/needle_runtime_service.dart` | Pack AI on-demand non equivale al content-pack sync generico; hashing e licenze |
| CAP-0018 | Backup restore con staging e rollback | `flutter_app/lib/src/domain/recovery_journal.dart` | Journal Step 2C merged: process-kill/SAF/low storage device |
| CAP-0103 | Grafo delle dipendenze e blocker delle task | `flutter_app/lib/src/domain/project_dependency_actions.dart` | Dipendenze canoniche parziali: ciclo/ACL/stadi e UX blocker |
| CAP-0106 | Rilevamento sovraccarico e heatmap riunioni | `flutter_app/lib/src/domain/project_workload_guard.dart` | Workload read-only: heatmap riunioni e durate da verificare |
| CAP-0029 | Canvas ibrida sketch sotto note | `flutter_app/lib/src/screens/whiteboard_screen.dart` | Canvas ink+post-it presente; test penna/restore fisico |
| CAP-0116 | Deduplicazione semantica note con merge reversibile | `flutter_app/lib/src/domain/note_duplicate_review.dart` | Pilot read-only; KEEP/VARIANT/merge reversibile non completo |
| CAP-0019 | Store media content addressed e GC | `flutter_app/lib/src/domain/attachments.dart` | CAS e GC: test cleanup crash, integrity SHA, restore su device |
| CAP-0096 | Gerarchie task ricorrenze e relazioni alle note | `flutter_app/lib/src/domain/planner.dart` | Task/subtask e relazioni: ricorrenze, edit/save/lifecycle da verificare |
| CAP-0032 | Indicizzazione ricerca semantica locale | `flutter_app/lib/src/data/semantic_index_store.dart` | Indice vettori hash 192 dimensioni, non LLM; qualità e device |
| CAP-0098 | Mind map navigabile derivata da note e documenti | `flutter_app/lib/src/screens/whiteboard_screen.dart` | Mind Map editabile presente; derivazione autonoma da note/PDF da provare |
| CAP-0033 | Modello Needle 3 on demand Plus | `flutter_app/lib/src/data/needle_runtime_service.dart` | Needle opzionale Plus; Play-pack/runtime device e entitlement reali |
| CAP-0112 | Flashcard e ripasso dilazionato collegati alle note | `flutter_app/lib/src/domain/study.dart` | Flashcard e scheduling presenti; provenance/QA completa |

### Cinque MVP già mergiate ma non complete (issue Notes #64)
| CAP | PR Notes | Indizio | Gate residuo |
| --- | --- | --- | --- |
| CAP-0092 | [#65](https://github.com/riccardopinato/Notes-Ecosistema/pull/65) | `flutter_app/lib/src/domain/natural_language_task.dart` | PR #65 parser IT/EN MVP: reminder/ACL/6 lingue restano |
| CAP-0037 | [#69](https://github.com/riccardopinato/Notes-Ecosistema/pull/69) | `flutter_app/android_overrides/PdfToolkitBridge.kt` | PR #69 PDF Toolbox dark-launched; dispositivo/licenze e operazioni restano |
| CAP-0104 | [#66](https://github.com/riccardopinato/Notes-Ecosistema/pull/66) | `flutter_app/lib/src/domain/project_goal_timeline.dart` | PR #66 timeline retrograda read-only: persist/milestone/conflitti restano |
| CAP-0118 | [#67](https://github.com/riccardopinato/Notes-Ecosistema/pull/67) | `flutter_app/lib/src/domain/document_delta.dart` | PR #67 diff testuale: PDF visual/side by side avanzato restano |
| CAP-0114 | [#68](https://github.com/riccardopinato/Notes-Ecosistema/pull/68) | `flutter_app/lib/src/domain/privacy_copy.dart` | PR #68 privacy copy testuale: PDF redaction reale assente |

### Indice completo 88/88, in ordine di priorità del catalogo
| CAP | Score | Facilità | Stato catalogo | Verifica nello source review | Delta / nuovo gate |
| --- | ---: | ---: | --- | --- | --- |
| CAP-0037 | 98 | 90% | PROPOSTA | MVP_PARZIALE_PR_MERGED | PR #69 PDF Toolbox dark-launched; dispositivo/licenze e operazioni restano |
| CAP-0015 | 95 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Ricerca e sort presenti: token singolo/edge-case device |
| CAP-0102 | 92 | 85% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0035 | 92 | 80% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | OCR MLKit local: fonte/revisione e test fisico |
| CAP-0028 | 91 | 97% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Connettori fra nodi presenti: roundtrip edge e stress device |
| CAP-0109 | 91 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Focus presente: Pomodoro/permessi DND/attribuzione task da verificare |
| CAP-0111 | 91 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Weekly Review proiezione presente: CTA/azioni e storico mancanti |
| CAP-0027 | 90 | 85% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Android share capture: scope/data provenance e test intents |
| CAP-0092 | 90 | 85% | PROPOSTA | MVP_PARZIALE_PR_MERGED | PR #65 parser IT/EN MVP: reminder/ACL/6 lingue restano |
| CAP-0084 | 89 | 90% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0002 | 88 | 95% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0013 | 88 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Raccolte e ricerca presenti: scala/performance e smoke |
| CAP-0016 | 88 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Raccolte già presenti: categoria editabile equivalenza funzionale da stabilire |
| CAP-0020 | 88 | 58% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0104 | 87 | 85% | PROPOSTA | MVP_PARZIALE_PR_MERGED | PR #66 timeline retrograda read-only: persist/milestone/conflitti restano |
| CAP-0107 | 87 | 85% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Markdown intake exists; blueprint to confirmed tasks not demonstrated |
| CAP-0004 | 87 | 80% | ROADMAP_STORICA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Overlay calendari esterni non dimostrato; roadmap storica |
| CAP-0005 | 87 | 80% | ROADMAP_STORICA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Export eventi calendario esterno non dimostrato; roadmap storica |
| CAP-0148 | 87 | 80% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Smart Inbox preview/task presente: writer completo tag/progetto e Undo |
| CAP-0138 | 87 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0031 | 86 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0094 | 85 | 87% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Canvas e task esistono separati; ID unico sticky Kanban non provato |
| CAP-0105 | 85 | 85% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Matrice Eisenhower presente: azione canone e campi espliciti |
| CAP-0118 | 85 | 85% | PROPOSTA | MVP_PARZIALE_PR_MERGED | PR #67 diff testuale: PDF visual/side by side avanzato restano |
| CAP-0151 | 85 | 84% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | No extractive TextRank with citations verified; may reuse lexical signals |
| CAP-0114 | 85 | 55% | PROPOSTA | MVP_PARZIALE_PR_MERGED | PR #68 privacy copy testuale: PDF redaction reale assente |
| CAP-0101 | 84 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Indicatori task presenti: dashboard intervalli completa non provata |
| CAP-0108 | 84 | 95% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0134 | 84 | 58% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0133 | 83 | 70% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0066 | 83 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0110 | 82 | 95% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Focus esistente: micro-step guidato separato non dimostrato |
| CAP-0003 | 81 | 95% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0149 | 81 | 67% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Visual-doc engine found; JSON Canvas v1 import/export not proven |
| CAP-0121 | 81 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0128 | 81 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0129 | 81 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0145 | 81 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0120 | 81 | 60% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Immagini in note presenti; testo alternativo accessibile da valutare |
| CAP-0130 | 81 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0147 | 81 | 60% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Home attuale non modulare; blueprint UI5 separato |
| CAP-0153 | 80 | 77% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0122 | 79 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0095 | 79 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0076 | 78 | 85% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Importer con provenance; Web Clip sicuro non dimostrato |
| CAP-0080 | 78 | 85% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0126 | 78 | 85% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Relazioni sono base utile; glossario contestuale non provato |
| CAP-0127 | 78 | 75% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0136 | 76 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0030 | 75 | 85% | ROADMAP_STORICA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0124 | 74 | 72% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Embedding locale disponibile; topic cluster non dimostrato |
| CAP-0075 | 74 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0115 | 74 | 65% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Relazioni fonte disponibili; contradiction check con provenance non provato |
| CAP-0123 | 74 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0099 | 73 | 85% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0097 | 72 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0125 | 72 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0086 | 72 | 60% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0131 | 72 | 35% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0135 | 71 | 85% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0150 | 71 | 82% | PROPOSTA | INDIZIO_CODICE_SCOPE_DA_VERIFICARE | Home briefing esistente; Daily Note Hub read-only distinta da definire |
| CAP-0154 | 71 | 69% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0085 | 70 | 50% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0117 | 70 | 35% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0146 | 69 | 20% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0074 | 67 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0119 | 67 | 65% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0132 | 65 | 50% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0139 | 63 | 50% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0140 | 63 | 35% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0100 | 61 | 45% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0137 | 52 | 15% | PROPOSTA | NESSUNA_PROVA_PUNTUALE_AUDIT | Non valutato puntualmente nel source review: non inferire assenza o implementazione. |
| CAP-0093 | 96 | 97% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Parser+task canonico: verificare flusso sorgente/ACL e cap completo |
| CAP-0152 | 96 | 95% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Fallback fuzzy Unicode: recall/false-positive, ricerca 1 carattere, 500/5000 |
| CAP-0017 | 94 | 82% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Trash esistente: regressioni cross-sidecar/GC e test Android |
| CAP-0160 | 91 | 93% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | TF-IDF proposte tag: 6 locale, source/ACL, nessuna scrittura automatica |
| CAP-0071 | 90 | 67% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Pack AI on-demand non equivale al content-pack sync generico; hashing e licenze |
| CAP-0018 | 90 | 65% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Journal Step 2C merged: process-kill/SAF/low storage device |
| CAP-0103 | 87 | 91% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Dipendenze canoniche parziali: ciclo/ACL/stadi e UX blocker |
| CAP-0106 | 87 | 91% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Workload read-only: heatmap riunioni e durate da verificare |
| CAP-0029 | 84 | 76% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Canvas ink+post-it presente; test penna/restore fisico |
| CAP-0116 | 83 | 85% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Pilot read-only; KEEP/VARIANT/merge reversibile non completo |
| CAP-0019 | 81 | 65% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | CAS e GC: test cleanup crash, integrity SHA, restore su device |
| CAP-0096 | 80 | 89% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Task/subtask e relazioni: ricorrenze, edit/save/lifecycle da verificare |
| CAP-0032 | 79 | 63% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Indice vettori hash 192 dimensioni, non LLM; qualità e device |
| CAP-0098 | 78 | 70% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Mind Map editabile presente; derivazione autonoma da note/PDF da provare |
| CAP-0033 | 76 | 60% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Needle opzionale Plus; Play-pack/runtime device e entitlement reali |
| CAP-0112 | 75 | 91% | SOURCE_REPORTED | CODICE_CANDIDATO_DA_VERIFICARE | Flashcard e scheduling presenti; provenance/QA completa |

## Procedura al gate di issue #41
1. Read full individual CAP contract, source exact SHA, test and approval proof; distinguish partial from full per-app implementation.
2. Only then amend canonical `REGISTRO_CAPABILITY.json`, preserving old evidence and per-app states.
3. Run `python3 scripts/build_catalog.py` then `python3 scripts/build_catalog.py --check`, repository CI exact-head and code review.
4. Merge only if required checks green. The CSV companion provides all 88 rows for exact evidence triage, **not** a second source of truth.

**File dati di audit:** [AUDIT_NOTES_CAP_88_2026-11-07.csv](AUDIT_NOTES_CAP_88_2026-11-07.csv). 
