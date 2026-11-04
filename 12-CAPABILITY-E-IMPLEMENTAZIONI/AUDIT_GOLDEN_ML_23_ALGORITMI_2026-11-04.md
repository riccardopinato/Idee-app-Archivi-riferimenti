# Audit completo 23 algoritmi ML e motori candidati Golden — 04/11/2026

**Core baseline SHA** riccardopinato/App-Factory-Core@6cbb3449ba375496029bee93b45bc9f939dcd794 (Master v27; Golden Index v28). **Ideas baseline** 150 CAP / 346 associazioni. **Dopo** 160 CAP / 385 associazioni / 48 app.

Audit source: [Machine Learning.txt riportato nell'intake](../11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md). 23 tecniche analizzate; 10 nuovi comportamenti ammessi CAP-0151…0160, 13 riusi di capability già esistenti, senza duplicare funzioni.

### Stato Golden e metodo probatorio

E0 idea/specifica -> E1 sorgente SHA + file -> E2 test presenti (non necessariamente eseguiti) -> **E3** direct tests + exact-head CI per scope donor -> **E4** test piattaforma fisica/provider se applicabili -> **E5** consumer indipendente provato. Nessuna nuova CAP acquisisce E3/E5 semplicemente entrando nel catalogo.

Goldens esistenti pertinenti: Hybrid Search (DRAFT, limited independent consumer), Local Rules (DRAFT), Explainable Recommendation (DRAFT), GPX (DRAFT, limited read-only consumer), Spatial (DRAFT), Sensor Fusion Android (DRAFT), Performance Fixture (DRAFT). **Non dichiararli universalmente COPY-READY.**

Android limita sensor sampling e background activity: https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview. BatteryManager current/capacity dipende dal fuel gauge: https://developer.android.com/reference/android/os/BatteryManager. Per K-Means e TF-IDF sparse la stabilità del clustering va misurata: https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html.

### Mappa 23/23: algoritmo → capability canonica

| Intake | Algoritmo | CAP canoniche | Esito | Priorità di approfondimento |
| --- | --- | --- | --- | --- |
| ML26-001 | Levenshtein / Jaro-Winkler | CAP-0152 | NUOVA CAP E0 | P1 |
| ML26-002 | TF-IDF + coseno sparse | CAP-0160 | NUOVA CAP E0 | P1 |
| ML26-003 | K-Means testo | CAP-0124 | RIUSO CAP ESISTENTE | P2 |
| ML26-004 | TextRank estrattivo | CAP-0151 | NUOVA CAP E0 | P2 |
| ML26-005 | Regex / dizionario / NER | CAP-0002, CAP-0092, CAP-0148 | RIUSO CAP ESISTENTE | P1 |
| ML26-006 | Greedy / interval scheduling | CAP-0001, CAP-0102 | RIUSO CAP ESISTENTE | P1 |
| ML26-007 | Algoritmi genetici / euristici | CAP-0102, CAP-0050 | RIUSO CAP ESISTENTE | P3 |
| ML26-008 | Regressione lineare robusta | CAP-0153 | NUOVA CAP E0 | P2 |
| ML26-009 | Markov / frequenze temporali | CAP-0154 | NUOVA CAP E0 | P3 |
| ML26-010 | K-Means utenti / Random Forest | CAP-0057, CAP-0062 | RIUSO CAP ESISTENTE | P3 |
| ML26-011 | Color histogram matching | CAP-0041 | RIUSO CAP ESISTENTE | P2 |
| ML26-012 | Coseno / collaborative filtering / SVD | CAP-0032, CAP-0044 | RIUSO CAP ESISTENTE | P3 |
| ML26-013 | Apriori / frequent itemsets | CAP-0155 | NUOVA CAP E0 | P2 |
| ML26-014 | Dijkstra / A* | CAP-0048, CAP-0049 | RIUSO CAP ESISTENTE | P1 |
| ML26-015 | DBSCAN / clustering spaziale | CAP-0159 | NUOVA CAP E0 | P2 |
| ML26-016 | Ramer-Douglas-Peucker | CAP-0156 | NUOVA CAP E0 | P2 |
| ML26-017 | Kalman / filtro complementare | CAP-0057 | RIUSO CAP ESISTENTE | P2 |
| ML26-018 | Dynamic Time Warping / DTW | CAP-0157 | NUOVA CAP E0 | P3 |
| ML26-019 | EWMA / soglie adattive / isteresi | CAP-0158 | NUOVA CAP E0 | P1 |
| ML26-020 | Regressione lineare batteria | CAP-0061 | RIUSO CAP ESISTENTE | P2 |
| ML26-021 | Embedding vettoriali e coseno | CAP-0032 | RIUSO CAP ESISTENTE | P3 |
| ML26-022 | TFLite / Core ML audio classifier | CAP-0132 | RIUSO CAP ESISTENTE | P3 |
| ML26-023 | Apriori sequenze / regole locali | CAP-0148, CAP-0111 | RIUSO CAP ESISTENTE | P2 |

### Nuove 10 capability e facilità per tutte le app candidate

| CAP | Motore | Score globale | Facilità per app (euristica) | Dipendenze di ingresso |
| --- | --- | ---: | --- | --- |
| CAP-0151 Riassunti estrattivi di note con TextRank e citazioni | LEXICAL_TEXT | 85 (P2) | Notes-Ecosistema 84%, Agenda-per-Anna 72%, Wonderlog 73%, PDF-Unifier 64% | CAP-0032, CAP-0097, CAP-0148 |
| CAP-0152 Ricerca fuzzy offline per refusi e alias | LEXICAL_TEXT | 96 (P1) | Notes-Ecosistema 93%, Agenda-per-Anna 89%, Wonderlog 88%, PDF-Unifier 83% | CAP-0015, CAP-0032 |
| CAP-0153 Previsione prudente di completamento studio e progetti | SCHEDULING_FORECAST | 78 (P3) | Notes-Ecosistema 74%, Agenda-per-Anna 71%, FocuSense 66% | CAP-0108, CAP-0104, CAP-0102 |
| CAP-0154 Routine predittive con Markov solo opt-in | BEHAVIORAL_PATTERNS | 71 (P3) | Agenda-per-Anna 71%, Notes-Ecosistema 69%, SleepMax-Coach 63%, FocuSense 68% | CAP-0111, CAP-0148 |
| CAP-0155 Associazioni ingredienti e ricette offline con Apriori | BEHAVIORAL_PATTERNS | 89 (P2) | TasteAI 84%, In-Cucina-con-gli-Anime 82%, MealMate 77% | CAP-0044, CAP-0045 |
| CAP-0156 Semplificazione reversibile di tracce e polilinee GPX | GEO_GEOMETRY | 89 (P2) | TrailPath 82%, Wonderlog 89%, CamperBoss 86% | CAP-0048, CAP-0049, CAP-0050 |
| CAP-0157 Gesti volontari locali tramite Dynamic Time Warping | SENSOR_SIGNAL | 72 (P3) | Phone-Guard 61%, Pocket-Guard 72%, Tabletop-Motion-Alarm 67%, FocuSense 65% | CAP-0057, CAP-0062 |
| CAP-0158 Soglie adattive con isteresi per luce e prossimità | SENSOR_SIGNAL | 96 (P1) | Pocket-Guard 91%, Phone-Guard 86%, FocuSense 89%, Tabletop-Motion-Alarm 84% | CAP-0057, CAP-0062 |
| CAP-0159 Clustering spaziale privacy-safe per ricordi e POI | GEO_GEOMETRY | 85 (P2) | Wonderlog 88%, TrailPath 79%, CamperBoss 82%, Agenda-per-Anna 70% | CAP-0009, CAP-0051, CAP-0048 |
| CAP-0160 Estrazione TF-IDF di parole chiave e tag suggeriti | LEXICAL_TEXT | 91 (P2) | Notes-Ecosistema 91%, Agenda-per-Anna 80%, Wonderlog 84%, PDF-Unifier 74% | CAP-0124, CAP-0148, CAP-0032 |

### Cinque famiglie di motori e cascata abilitata

| Famiglia | Golden esistente o nuova candidatura | Port puramente algoritmico | CAP a valle |
| --- | --- | --- | --- |
| LEXICAL_TEXT | NEW GOLDEN CANDIDATE: GOLDEN_HYBRID_LOCAL_SEARCH_ENGINE_v1_DRAFT | Pure Dart tokenizer/TF-IDF, bounded fuzzy and cited extractive summaries | CAP-0015, CAP-0032, CAP-0093, CAP-0097, CAP-0124, CAP-0148 |
| SCHEDULING_FORECAST | EXTEND EXISTING GOLDEN RULES DRAFT: GOLDEN_LOCAL_RULES_AUTOMATION_ENGINE_v1_DRAFT | Greedy bounded slots + robust forecast separated from canonical calendar writes | CAP-0001, CAP-0102, CAP-0104, CAP-0106, CAP-0108, CAP-0111 |
| BEHAVIORAL_PATTERNS | NEW GOLDEN CANDIDATE: GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT | Explainable Markov/Apriori with support and minimum observations | CAP-0044, CAP-0045, CAP-0111, CAP-0148 |
| GEO_GEOMETRY | EXTEND EXISTING GPX/SPATIAL GOLDENS: GOLDEN_GPX_INTEROPERABILITY_ENGINE_v1_DRAFT + GOLDEN_SPATIAL_CLUSTERING_ENGINE_v1_DRAFT | Bounded reversible simplifier and meter-scale density clustering | CAP-0009, CAP-0048, CAP-0049, CAP-0050, CAP-0051 |
| SENSOR_SIGNAL | EXTEND SENSOR FUSION GOLDEN DRAFT: GOLDEN_SENSOR_FUSION_ANDROID_v1_DRAFT | Portable EWMA/hysteresis core + optional DTW bounded gestures; OEM adapters separate | CAP-0057, CAP-0061, CAP-0062 |

### Priorità di realizzazione, non approvazione prodotto

1. **A — motore testo**: tokenizer multilingua, TF-IDF, fuzzy bounded; tests provenance / Unicode / retrieval privacy. E3 probabile con zero modelli; E5 da Notes o Wonderlog.
2. **B — motore sensor signal**: EWMA/hysteresis pure; Physical/OEM required for E4. CAP-0158 sblocca qualità CAP-0057 e CAP-0062; non utilizzare sensor service background senza check OS.
3. **C — scheduling & forecast**: riusare CAP-0001/0102 e Local Rules; regressione con campione minimo, opt-in. Nessun evento spostato automaticamente.
4. **D — recommender / associations**: Apriori per catalogo ricette e Markov routine (solo consenso); l'output dev'essere spiegabile e privo di write impliciti.
5. **E — geospatial**: RDP sopra GPX, DBSCAN/grid sopra Spatial Clustering, con coordinate valide, antimeridiano e origine inalterata.
6. **F — DTW / embedding / modelli**: data collection etichettata e hardware baseline prima; non introdurre pacchetti pesanti nella base.

### Metriche di certificazione (e non metriche inventate)

- Correttezza: golden input-output vectors, proprietà determinate, tie-break stabile, output null su input non sufficienti, test negativi per ciclo/ACL/stale data.
- CPU: median/p95 su N=0/1/100/500/5000, budget e memoria registrati; non assumere complessità lineare per TextRank/DBSCAN/DTW.
- APK: baseline vs engine size diff, pacchetti transitivi, nessun file modello di default; Web e Android toolchain se usati come consumer.
- Sicurezza: no data export, source-scoped permission filtering, cancellazione/undo e Privacy-by-design per suggerimenti. False positive/negative test sui sensori reali.
- Prove: SHA 40 caratteri, file donor e test, URL CI exact SHA, licenza, compatibilità, data di revisione e successivo consumer indipendente.

### Cosa NON è stato fatto da questa ammissione

- Nessuna delle 10 CAP implementata nelle app, nessun nuovo Golden certificato o registro centrale promosso, nessun LLM/model download/API e nessun rilascio.
- Non modificare gli score delle 150 capability esistenti per il semplice fatto di aver proposto un algoritmo. I 2 nuovi collegamenti CAP-0041 alle app ricette sono solo PROPOSTA.
- I 10 kit sono al livello E0 (specifica e piano), non source-extracted. L'inventario di nuove implementazioni vive nel registro canonico e la vista è generata.

Grafo machine-readable: [CATENE_MOTORI_ML_2026-11-04.json](CATENE_MOTORI_ML_2026-11-04.json).
