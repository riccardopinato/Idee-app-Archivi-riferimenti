# Catalogo algoritmi ML leggeri e on-device — 4 novembre 2026

**Origine:** file utente Machine Learning.txt (156 righe). Questo documento è un intake di ricerca, non una modifica di prodotto o l'avvio di modelli.
**Factory baseline letta:** App-Factory-Core@6cbb3449ba375496029bee93b45bc9f939dcd794; Master 27, Golden Index 28, Registry v2. Per l'archivio capability baseline: 150 CAP e 346 associazioni prima di questo intake.

## Presupposti rigorosi

- OFFLINE E API: tutti gli algoritmi deterministici possono essere implementati localmente; questo non certifica il bundle, i permessi, il consumo o la latenza. Un modello pretrained può avere costi di manutenzione/distribuzione e licenze da controllare.
- RICERCA SEMANTICA: embedding linguistici addestrati possono cogliere relazioni semantiche. TF-IDF e feature hashing da soli sono principalmente segnali lessicali; l'algoritmo non garantisce pertinenza né veridicità di una fonte recuperata.
- NER: email/date/ore possono emergere da regex e dizionari; POS tagging e riconoscimento affidabile di nomi e frasi complesse richiedono NLP, spesso risorse aggiuntive. Una proposta non crea task o appuntamenti senza consenso.
- K-MEANS: i cluster di testo sparso sono sensibili a inizializzazione/numero K; l'utente conferma sempre tag/cartelle. Random Forest richiede dati etichettati e verifica out-of-sample.
- GENETICI: tempi di calcolo e ottimalità non sono garantiti. Prima baseline greedy e regole di constraint scheduling.
- TRACCE: Douglas–Peucker non garantisce alcun 90% di riduzione universale; preservare originale e misurare errore di semplificazione.
- SENSORI: presenza sensore e health/permessi sono distinti. Android 9+ limita eventi sensore in background; registrare listeners solo per il tempo necessario; test fisici e batteria separati da unit test.
- BATTERIA: BatteryManager espone proprietà come current now/average/capacity, ma disponibilità, precisione e finestre di misura dipendono dal dispositivo; evitare previsione garantita.
- COLLABORATIVE FILTERING: utilizzare dati comportamentali di altri utenti contraddice una architettura esclusivamente personale/offline se quei dati non sono stati raccolti e distribuiti con consenso. Preferire content-based su corpus locale.

## Mappatura completa delle 23 proposte

| ID intake | Algoritmo | Funzionalità | Catalogo | App e facilità di partenza | Priorità | Gate principale |
| --- | --- | --- | --- | --- | --- | --- |
| ML26-001 | Levenshtein / Jaro-Winkler | Ricerca fuzzy con correzione typo | NUOVA CANDIDATA | Notes-Ecosistema 92%; Agenda-per-Anna 88%; Wonderlog 85% | P1 | Edit distance Unicode; limitarla ai migliori risultati autorizzati; fallback ricerca esatta |
| ML26-002 | TF-IDF + coseno sparse | Suggerimenti tag/keyword per singola nota | NUOVA CANDIDATA; collegata CAP-0124 / CAP-0148 | Notes-Ecosistema 90%; Agenda-per-Anna 78%; Wonderlog 83% | P1 | No comprensione semantica addestrata; topic cluster e writer di tag restano separati |
| ML26-003 | K-Means testo | Cluster tematici proposti | GIÀ CAP-0124 | Notes-Ecosistema 70% | P2 | Instabilità piccoli corpus, scelta K, niente cartelle persistenti senza conferma |
| ML26-004 | TextRank estrattivo | Riassunto da frasi originali con offset | NUOVA CANDIDATA; adiacente CAP-0097 | Notes-Ecosistema 80%; Agenda-per-Anna 70%; Wonderlog 68% | P2 | Non generativo: omette contesto, negazioni e date; citare frasi e fonte |
| ML26-005 | Regex / dizionario / NER | Bozze evento o task da testi | GIÀ CAP-0002 / CAP-0092 / CAP-0148 | Agenda-per-Anna 85%; Notes-Ecosistema 78% | P1 | Il POS tagging può richiedere modello, nomi persona non deducibili da sole regex; preview e consenso |
| ML26-006 | Greedy / interval scheduling | Incastrare task in slot liberi | GIÀ CAP-0001 / CAP-0102 | Agenda-per-Anna 85%; Notes-Ecosistema 78% | P1 | Vincoli hard/soft, durata, timezone, ricorrenze; mai scrittura automatica |
| ML26-007 | Algoritmi genetici / euristici | Varianti di calendario complesso | ESTENSIONE CAP-0102 / CAP-0050 | Agenda-per-Anna 55%; Notes-Ecosistema 56% | P3 | Non garantiscono ottimo né milioni di varianti in millisecondi; baseline greedy prima |
| ML26-008 | Regressione lineare robusta | Forecast avanzamento studio e progetto | NUOVA CANDIDATA; collegata CAP-0108 / CAP-0104 | Notes-Ecosistema 72%; Agenda-per-Anna 68%; FocuSense 66% | P2 | Campione minimo, outlier, pause, intervallo e output nessuna stima |
| ML26-009 | Markov / frequenze temporali | Suggerimenti routine opt-in | NUOVA CANDIDATA; adiacente CAP-0111 | Agenda-per-Anna 70%; Notes-Ecosistema 65%; SleepMax-Coach 63% | P3 | Consenso revocabile, non inferire dati sensibili, nessun reminder automatico |
| ML26-010 | K-Means utenti / Random Forest | Personalizzazione/classificazione | ESTENSIONE CAP-0062 / CAP-0057 | FocuSense 55%; Phone-Guard 50% | P3 | Necessari dati etichettati/validazione; per 1 utente no profilo cross-user |
| ML26-011 | Color histogram matching | Cercare ricette/foto per palette | ESTENSIONE CAP-0041 | In-Cucina-con-gli-Anime 82%; TasteAI 78%; app-fotografia 91% | P2 | Il colore non riconosce ingrediente o qualità |
| ML26-012 | Coseno / collaborative filtering / SVD | Suggerimenti ricette e contenuti | CAP-0032 + Golden Explainable Recommendations | TasteAI 66%; In-Cucina-con-gli-Anime 74% | P3 | Collaborativo cross-user richiede dati di terzi: fallback content-based locale |
| ML26-013 | Apriori / frequent itemsets | Ingredienti correlati da catalogo locale | NUOVA CANDIDATA; adiacente CAP-0044 / CAP-0045 | TasteAI 84%; In-Cucina-con-gli-Anime 80%; MealMate 73% | P2 | Dati sufficienti e support/confidence; allergeni/diete non inferiti |
| ML26-014 | Dijkstra / A* | Routing mappe offline | GIÀ CAP-0048 / CAP-0049 | TrailPath 50%; CamperBoss 50% | P1 | Senza grafo/mappa locale non esiste routing offline; percorsi e vincoli da validare |
| ML26-015 | DBSCAN / clustering spaziale | Hotspots locali di ricordi e POI | NUOVA CANDIDATA; adiacente CAP-0009 / CAP-0051 + Golden Spatial | Wonderlog 84%; TrailPath 76%; CamperBoss 78% | P2 | Raggio in metri, antimeridiano, privacy location/Shared Spaces, nessuna pubblicazione |
| ML26-016 | Ramer-Douglas-Peucker | Compressione geometrica GPX reversibile | NUOVA CANDIDATA; adiacente CAP-0048 | Wonderlog 88%; TrailPath 82%; CamperBoss 84% | P2 | Originale immutato, errore misurato, unità metri e coordinate non valide |
| ML26-017 | Kalman / filtro complementare | Sensor fusion movimento/giroscopio | GIÀ CAP-0057 + GOLDEN_SENSOR_FUSION_ANDROID_DRAFT | Pocket-Guard 75%; Phone-Guard 65%; Tabletop-Motion-Alarm 72% | P2 | Riduce rumore ma non garantisce precisione; calibrazione e OEM |
| ML26-018 | Dynamic Time Warping / DTW | Gesture deliberate con template locale | NUOVA CANDIDATA; adiacente CAP-0057 | Pocket-Guard 69%; Phone-Guard 59%; Tabletop-Motion-Alarm 64% | P3 | Sampling, variabilità device, false positive; Android foreground/FGS e permessi |
| ML26-019 | EWMA / soglie adattive / isteresi | Sensori luce e prossimità stabili | NUOVA CANDIDATA; adiacente CAP-0057 / CAP-0062 | Pocket-Guard 90%; Phone-Guard 85%; FocuSense 88% | P1 | Device availability, sensori binari/continuativi, debounce, consumi e QA OEM |
| ML26-020 | Regressione lineare batteria | ETA carica e scarica prudente | GIÀ CAP-0061 | Battery_Guard 80% | P2 | Current/average non sempre disponibili, stima non certa, no autospegnimento opaco |
| ML26-021 | Embedding vettoriali e coseno | Ricerca basata su significato | GIÀ CAP-0032 + Golden Hybrid Search DRAFT | Notes-Ecosistema 62%; Wonderlog 64%; Agenda-per-Anna 42% | P3 | Embedding addestrati ≠ TF-IDF; modello opzionale, licenza, benchmark IT |
| ML26-022 | TFLite / Core ML audio classifier | Classificazione micro-eventi sonori | GIÀ CAP-0132 | Notes-Ecosistema 47%; Wonderlog 48% | P3 | Nessuna garanzia modello inferiore 1MB, microfono e privacy |
| ML26-023 | Apriori sequenze / regole locali | Consigli azioni ripetute e automazioni | CAP-0148 + Golden Local Rules Automation DRAFT | Notes-Ecosistema 70%; Agenda-per-Anna 63% | P2 | Regole esplicabili; non dedurre causalità né applicare scritture silenziose |

**Legenda:** le percentuali sono ipotesi di facilità implementativa, non probabilità di successo né score delle CAP. P1/P2/P3 sono priorità di approfondimento **dell'intake**, da riconciliare con Product Bible e ranking canonico in caso di promozione.

## Dieci candidature distinte, NON ancora promosse a CAP

- 1. ML26-001 — Ricerca fuzzy con correzione typo. Levenshtein / Jaro-Winkler. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 2. ML26-002 — Suggerimenti tag/keyword per singola nota. TF-IDF + coseno sparse. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 3. ML26-004 — Riassunto da frasi originali con offset. TextRank estrattivo. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 4. ML26-008 — Forecast avanzamento studio e progetto. Regressione lineare robusta. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 5. ML26-009 — Suggerimenti routine opt-in. Markov / frequenze temporali. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 6. ML26-013 — Ingredienti correlati da catalogo locale. Apriori / frequent itemsets. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 7. ML26-015 — Hotspots locali di ricordi e POI. DBSCAN / clustering spaziale. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 8. ML26-016 — Compressione geometrica GPX reversibile. Ramer-Douglas-Peucker. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 9. ML26-018 — Gesture deliberate con template locale. Dynamic Time Warping / DTW. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.
- 10. ML26-019 — Sensori luce e prossimità stabili. EWMA / soglie adattive / isteresi. Collegare ai contratti canonici prima di assegnare un CAP ID definitivo.

## Ordine consigliato

**Wave 1 (basso rischio e riuso immediato):** ML26-001 fuzzy search, ML26-002 TF-IDF tag suggeriti, ML26-019 soglie adattive. Scheduling e parsing si estendono nelle CAP già esistenti, non in nuovi componenti duplicati.
**Wave 2 (funzioni visibili):** ML26-004 TextRank citabile, ML26-013 Apriori ricette, ML26-016 GPX semplificazione.
**Wave 3 (dati e consenso):** ML26-008 previsione fine progetto, ML26-009 Markov opzionale, ML26-015 cluster spaziali.
**Wave 4 (misure fisiche/complessità):** ML26-018 DTW; modelli/embedding o combinazioni genetiche solo dopo analisi corpus/licenza, peso APK e test hardware.

## Prossimi gate per eventuale promozione

- Un solo CAP per responsabilità, non un CAP per ogni formula matematica. Cercare prima delta funzionale rispetto a CAP-0001/0002/0032/0041/0048/0049/0057/0061/0062/0092/0102/0108/0124/0132/0148 e relativi Golden.
- La promozione richiede scelta prodotto, compatibilità app-specifica, kit di 6 file e aggiornamento REGISTRO_CAPABILITY.json, poi build_catalog.py + --check e CI exact-head.
- Stati iniziali PROPOSTA, non CODE_READY/CI_VERIFIED/DEVICE_VERIFIED. Nessuna scrittura, background tracking, API o modello integrati per effetto di questo audit.

## Fonti esterne (verifica concettuale, non donor di codice)

- [scikit-learn: clustering documenti TF-IDF e K-Means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)
- [Android Developers: Sensors overview, disponibilità e foreground](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview)
- [Android Developers: BatteryManager, proprietà di corrente](https://developer.android.com/reference/android/os/BatteryManager)
- [App Factory: Golden Hybrid Search v28](https://github.com/riccardopinato/App-Factory-Core/blob/6cbb3449ba375496029bee93b45bc9f939dcd794/golden/data/GOLDEN_HYBRID_LOCAL_SEARCH_ENGINE_v1_DRAFT.txt)
- [App Factory: Golden Sensor Fusion Android v28](https://github.com/riccardopinato/App-Factory-Core/blob/6cbb3449ba375496029bee93b45bc9f939dcd794/golden/native/GOLDEN_SENSOR_FUSION_ANDROID_v1_DRAFT.txt)
