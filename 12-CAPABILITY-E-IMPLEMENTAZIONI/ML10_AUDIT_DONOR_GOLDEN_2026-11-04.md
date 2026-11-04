# ML10 — Audit profondo del secondo lotto on-device (04/11/2026)

**Stato:** intake tecnico, crosswalk, audit dei rischi e candidati scoped donor; NON certificazione Golden né autorizzazione a cambiare il comportamento delle app.
**Origine:** messaggio utente del 04/11/2026, che ripete tre volte due liste equivalenti. Il lotto deduplicato conta **10 famiglie**, con varianti metodologiche non equivalenti.
**Factory baseline fissata:** `riccardopinato/App-Factory-Core@21afcd78606dfcf49a0f43886d8a6f5bbc1858cf`, CURRENT.yaml Master 27 / Golden Index 28 / Registry 2.
**Catalogo corrente:** 160 CAP e 385 associazioni. Nessuna nuova CAP canonica in questo audit: per ogni scenario si individua un owner funzionale già registrato. Il numero di algoritmi non corrisponde al numero di capability di prodotto.
**Code track E3 matematico verificato:** [App-Factory-Core PR #71](https://github.com/riccardopinato/App-Factory-Core/pull/71) **MERGED**, source `f5dad948dcc1096864cd4b9db84b9f0d86c9cb03`; [Dart full tests e analyze main SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497699), [Factory validation main SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497896). Sono **reference engine testati in Core**, non donor applicativi E3 né Golden o consumer E5. [Issue E5/Golden #72](https://github.com/riccardopinato/App-Factory-Core/issues/72).

## Correzione delle premesse e provenienza

1. **On-device/offline:** il calcolo di un algoritmo puro può funzionare senza rete o API a pagamento; questo non rende nullo il costo CPU, RAM, batteria, manutenzione, crash o licenze delle librerie/modelli.
2. **Nessun impatto sulla UX:** non verificabile senza p50/p95 e profiling su device. N² distance matrix, scansioni dense, preprocessing, retraining, import foto e microfono possono essere onerosi. Non invocare routine pesanti sul thread UI o a ogni frame.
3. **TFLite/Core ML <1 MB:** premessa non generale. Runtime, preprocessing e modello possono essere diversi MB; modelli image-classification benchmark ufficiali LiteRT mostrano già 5, 10, 14 MB. Confermare specifico artifact/quantizzazione/ops/ABIs e licenza, non solo nome della piattaforma.
4. **«Ricerca visiva 90% più veloce»:** stima non supportata. PCA centra input; TruncatedSVD è adatto anche a matrice sparse non centrata; non assicura accuratezza o guadagno prestazionale. Serve misura e recall/precision.
5. **«Sentiment = umore personale»:** classificare lessico in positivo/negativo non è una misura affidabile dello stato emotivo. Nessun avviso o inferenza psicologica in Anna's Diary senza scelta esplicita, set etichettato valido e privacy review.
6. **Fonti:** il testo utente cita 1–14 ma non contiene la bibliografia originaria. Non trattare questi numeri come fonti verificabili.

Documentazione esterna per metodologia:
- Outlier e differenza LOF novelty/outlier detection: https://scikit-learn.org/stable/modules/outlier_detection.html
- Definizione e limiti Local Outlier Factor: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html
- MinHash/LSH: https://ekzhu.com/datasketch/documentation.html
- Agglomerative clustering e connettività: https://scikit-learn.org/stable/modules/clustering.html
- TruncatedSVD: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html
- PCA: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
- LiteRT framework: https://developers.google.com/edge/litert
- Modelli, footprint e hardware misurati: https://google-ai-edge.github.io/litert-samples/benchmark/leaderboard/
- Android sensor power/lifecycle: https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview

## Crosswalk 10/10 — decisione architetturale e app consumer

| ID intake | Tecnica/variante | Capability esistente | Priorità | Decisione e contesto |
|---|---|---|---|---|
| ML10-01 | Isolation Forest / LOF | CAP-0057 sensor fusion, CAP-0154 routine opt-in | P3 | **RICERCA/SHADOW:** non sostituisce calibrazione, isteresi CAP-0158 o alarm owner-check. Per diario non dedurre malessere da comportamenti anomali; preferire robust MAD/quantili baseline. |
| ML10-02 | MinHash + banded LSH | CAP-0116 duplicate review, CAP-0032 ricerca | P1 | **DONOR CANDIDATE:** brevi shingles, shortlist LSH e Jaccard esatto; preview diff, revisione e merge esplicito con undo in Notes. Misurare recall vs full scan. |
| ML10-03 | Agglomerative clustering | CAP-0159 map POI, CAP-0124 topic discovery | P3 | **ESTENDERE SOLO SE SERVE:** su mappa i grid/zoom già esistenti sono più adatti per POI numerosi; gerarchia topic per 50–200 note massimo e consenso dell'utente. |
| ML10-04 | Hidden Markov Model | CAP-0154 routine/Markov opt-in, CAP-0057 sensori | P3 | **POC ETICHETTATO:** HMM include probabilità d'emissione e stato latente; non è equivalente alla catena di Markov già proposta. Riconoscimento attività richiede ground truth e benchmark OEM. |
| ML10-05 | PCA / Truncated SVD | CAP-0032 locale/embedding, CAP-0041 palette foto | P3 | **OTTIMIZZAZIONE OPZIONALE:** per TF-IDF sparse preferire SVD senza centering; con pochi dati più sensato vettore diretto. Nessun nuovo engine per sole promesse di -90%. |
| ML10-06 | Multinomial / Gaussian Naive Bayes | CAP-0092 task extraction, CAP-0160 tag suggeriti, CAP-0148 regole | P1 scoped / P3 mood | **DONOR CANDIDATE:** categorie esplicite e reversibili. Multinomial per token; Gaussian solo per feature continue; mood inference non autorizzata e distinta. |
| ML10-07 | kNN | CAP-0044 ricette, CAP-0041 somiglianza foto, CAP-0057 sensori | P2 | **ESTENSIONE:** cosine/metriche ponderate su feature normalizzate; permessi GPS/WiFi/microfono non concessi dal classificatore. Baseline esatta su piccoli cataloghi. |
| ML10-08 | Regressione logistica | CAP-0153 forecast prudente, CAP-0105 priorità, CAP-0104 goal timeline | P2 | **PROPOSTA MODELLO:** diverso da regressione lineare; richiede outcome etichettati, base rate e calibrazione, nessuna `probability` credibile senza training/validazione. |
| ML10-09 | Vision/audio pretrained via LiteRT/Core ML | CAP-0046 ingredienti da foto, CAP-0132 eventi acustici | P3 | **BLOCCO MODEL-GATE:** nessun download o bundle automatico. Servono licenza commerciale, modello/file versionati, footprint runtime, test su target e consenso microphone. |
| ML10-10 | Smoothing exp / Holt / Holt-Winters | CAP-0158 EWMA/hysteresis, CAP-0061 battery ETA | P1 riuso / P3 stagionale | **RIUSO PRIMA:** EWMA CAP-0158 già in Core e Pocket shadow; Holt trend e Winters stagionalità solo con serie stazionarie e sufficiente stagionalità, baseline monotona e device measurement. |

### Decisione CAP

- **0 nuove CAP canoniche al momento:** tutte le responsabilità consumer sono già rappresentate. La novità metodologica va annotata in submotori/adattatori, non spalmata su nuovi titoli CAP.
- La deduplicazione testuale **CAP-0116** è distinta dall'hash percettivo foto **CAP-0040**. Non convertire suggerimento di duplicato in hard-delete/merge automatico.
- LSH ha rischi di **falsi negativi** perché la shortlist è probabilistica. Anche Jaccard alto tra boilerplate comuni non garantisce duplicazione semantica; usare evidenze testuali nel confronto.
- Naive Bayes **non** è sentiment analysis affidabile. Lo score logaritmico non equivale a «85% sicuro». Un classificatore di etichette user-approved non autorizza classificazioni di salute o umore.
- HAC non equivale a grid clustering già implementato: semantiche differenti. HMM non equivale a frequenze Markov senza emissioni.
- Il test del core puramente matematico **non** modifica lo stato app `PROPOSTA` né la Golden Index.

## Audit profondo per famiglia

### ML10-01 Anomaly Detection: Isolation Forest vs LOF

**Meccanismo.** IF costruisce alberi con partizioni casuali e usa path length; LOF confronta densità locale rispetto ai k vicini. Entrambi richiedono un campione storico rappresentativo; la sequenza temporale, i trend e la stagionalità non sono modellati automaticamente. LOF outlier fit e novelty scoring su nuove osservazioni hanno contratti differenti. Non equiparare outlier a sensore difettoso: un urto può essere l'evento rilevante da proteggere.

**Costo/rischio.** Training, memoria e nearest-neighbor LOF dipendono da N/d e implementazione; conservare solo statistiche consentite, non telemetria di diario. Evitare train su <30 casi e drift incontrollato; per campioni rarissimi preferire median absolute deviation (MAD), soglie calibrate, EWMA e isteresi. Per anti-furto un filtro non deve scartare il singolo spike prima della state machine se quello spike potrebbe segnalare rimozione.

**Gate.** Baseline false negatives/positives, dati temporali con ground truth, OEM e lifecycle, opt-in per routine, nessuna notifica «psicologica».

### ML10-02 MinHash + LSH

**Meccanismo.** n-gram/shingle testuali -> firme di hash minimo -> banding per selezione approssimata -> Jaccard *esatto* di conferma. È un algoritmo lessicale: sinonimi/parafrasi distanti possono sfuggire. Per 100–300 note, scan diretto Jaccard o FTS candidate set potrebbe essere più economico di ricostruire firme e indici.

**Progetto donor.** Pure Dart senza librerie terze in Core PR #71, cap rigidi, 64 hash/16 band da 4, tie-break ID, condizioni hidden/deleted; delega ad app i veri ACL, revision, account switch, hash index persistente e scelta del merge. Un unico documento con testo molto breve produce nessun suggerimento.

**Gate.** Test di precisione/recall vs baseline `O(N^2)` full-pair per corpus 100/500/5000; benchmark p95 con indicizzazione incrementale; Unicode NFC/NFD, italiano/inglese, stopword/boilerplate, date e account. Review diff side-by-side, undo, soft-delete, lock stale revision, zero merge implicito. Consumer target Notes #48.

### ML10-03 Agglomerative Clustering

**Meccanismo.** Linkage single/complete/average/Ward crea dendrogramma; distanze e connettività sono scelte di modello. Pairwise distance dense ha footprint quadratico e linkage naive può essere oneroso. Non fare recompute sull'intera mappa a ogni pinch zoom.

**App.** Per POI 10k preferire `GOLDEN_SPATIAL_CLUSTERING_ENGINE_v1_DRAFT` gridZoom con anti-meridiano; per topic 50–200 note, provare clustering su feature sparse autorizzate con limite di cluster/tag suggeriti, senza spostare note o perdere categorie manuali.

### ML10-04 Hidden Markov Model

**Meccanismo.** Stati latenti, matrice di transizione, emission likelihood, decodifica Viterbi; `O(T*K²)` per passaggio base, con K stati e T campioni. Il training supervisionato/EM e la scelta dei sensori non sono «gratis». Serve set locale etichettato e un valore reale vs regole di soglia.

**App.** Solo shadow in Pocket Guard/FocusSense inizialmente; Agenda solo modalità opt-in, no inferenza «in auto» basata su posizione o rete senza consenso e permessi minimi. Misurare confusione tra cammino/corsa/auto e costi sampling.

### ML10-05 PCA / SVD

**Meccanismo.** Fit/proiezione dimensionalità; PCA centra caratteristiche, TruncatedSVD non necessariamente. TruncatedSVD su sparse TF-IDF è distinto dalla semplice riduzione dei colori di immagini. Le componenti cambiano a ogni refit se non versionate.

**App.** Assumere prima piccola feature table tipizzata; se >1000 vettori di >64 dimensioni e benchmark dimostra vantaggio, versionare modello/proiezione, controllare drift e recall@k. Non usare riduzione semantica per «riconoscimento ingredienti da foto» senza un encoder di visione.

### ML10-06 Naive Bayes

**Meccanismo.** Multinomial su conteggi/TF, Gaussian su vettori numerici continui. Richiede dati etichettati rappresentativi; soglie di rifiuto e calibrazione; il class prior può catturare squilibri non desiderati.

**Progetto donor.** Pure Dart in Core PR #71 con etichette esplicitamente fornite, 2+ classi con minimo campioni, unknown-vocabulary abstention, max 300 righe, e log-score margin non calibrato. Non scrive tag. Per Note/Anna richiedere UX in cui l'utente accetta ogni tag, archivia il consenso e può disattivare la classificazione. L'analisi dell'umore non è un semplice alias della categorizzazione dei task.

**Gate.** Matrice di confusione per italiano/EN/ES, class imbalance, false suggestions, negazione/sarcasmo, 6+ documenti per etichetta e qualità in cold start; ACL per esempi di training; nessuna applicazione automatica.

### ML10-07 kNN

**Meccanismo.** Confronta l'osservazione con K esempi etichettati/similari; fase di fit minimale, query lineare `O(N*d)` salvo indice. Normalizzare numeriche e codificare categorie; pesare allergeni e ingredienti proibiti come *hard constraints*, non somiglianza.

**App.** CAP-0044 ricette (catalogo esclusivamente approvato), ricerca visuale solo con descrittori validi, sensori solo con osservazioni realmente campionate. Geolocalizzazione e reti visibili comportano permessi/privacy/batteria: KNN non li elimina. Preferire cosine baseline quando piccola matrice.

### ML10-08 Regressione logistica

**Meccanismo.** Classificatore binario con sigmoid, non regressione lineare del tempo rimanente. I coefficienti devono essere appresi su dati etichettati e verificati senza data leakage da scadenze future.

**App.** Previsione di posticipo in agenda solo con opt-in, sufficiente storico, soglia trasparente, controlli fairness e calibration (Brier score / reliability curve). Se dati insufficienti, proporre un task split su regola esplicita invece di probabilità inventata. Nessuna schedulazione automatica.

### ML10-09 LiteRT / Core ML Vision-Audio

**Meccanismo.** Framework runtime, **non** singolo algoritmo né singolo file modello. Dimensione/latency dipendono da architettura, quantizzazione, ops, device/acceleratore, frequenza dei fotogrammi e pre/postprocessing.

**App.** CAP-0046 estrazione ingrediente richiede model card, precision per classe/dataset food locale, fallback manuale, attributi allergeni mai dedotti dalla foto. CAP-0132 audio richiede microfono con indicatore/consenso e no background covert recording. Se modello manca o license/toS non consentono distribuzione commerciale: BLOCKED. Preferire pack opt-in con checksum/licenza e revoca.

### ML10-10 EWMA, Holt, Holt-Winters

**Meccanismo.** EWMA liscia un livello; Holt modella livello+trend; Winters aggiunge stagionalità additiva/moltiplicativa. Questi non riconoscono «anomalia» senza logica separata e non sempre prevedono bene cambi improvvisi di regime.

**App.** Estendere prima `LocalAdaptiveSignalReference` CAP-0158 e Smart ETA CAP-0061; tenere lontano dall'active alarm path senza test. In batteria il segnale corrente/capacità dipende da qualità fuel-gauge; stime devono esporre affidabilità e cold-start, non cifre false.

## Donor e Golden admission — piano con gate riproducibili

| Lane | Source/protocollo | Evidenza minima E3 | Consumer E5 + Golden gate |
|---|---|---|---|
| **A** CAP-0116 MinHash LSH | Core PR #71, `reference_engines/lib/src/local_ml_candidates.dart` e `test/local_ml_candidates_test.dart` | exact-head static analysis, full Dart test, fixture equivalence, failure vectors, immutabile SHA | Notes-Ecosistema #48: source-backed read-only preview, ACL, revision, undo, user Save; confronto p95/recall e seconda app/harness se Golden generalizzato |
| **B** Tag Naive Bayes (CAP-0160 / CAP-0092) | stesso Pure Dart, nessun package | log-score deterministico, abstain, multilabel? **no** (un label); CV per token e classi | Notes editor: suggerimento esplicito, niente write auto, test data leakage; nessun mood tracking Golden |
| **C** CAP-0158 EWMA | Core pure source già presente; Pocket Guard shadow con CI documentata | già registrata nel ledger ML23; non duplicare | Pocket hardware QA multi OEM, drain, false positive/negative, lifecycle prima di decision path |
| **D** Geo/HMM/LOF/SVD/Modelli | nessun donor creato qui | richiede fixture, scelte dei parametri, footprint e prova di convenienza | consumer/physical/legale e consenso prima di qualunque promozione |

**Distinzioni E0/E1/E2/E3/E4/E5:** E0 specifica; E1 source SHA immutabile; E2 test presenti; E3 test effettivamente eseguiti con CI exact-source -> **CERTIFIED DONOR limitato al comportamento matematico**; E4 hardware/provider; E5 consumer indipendente provato. **COPY-READY / CERTIFIED GOLDEN non derivano automaticamente da un donor matematico.** Applicare [Single-Donor Admission](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/governance/GOLDEN_SINGLE_DONOR_CAPABILITY_ADMISSION_v1.txt).

**Golden esistenti da estendere, non duplicare:** `GOLDEN_HYBRID_LOCAL_SEARCH_ENGINE_v1_DRAFT`, `GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT`, `GOLDEN_SPATIAL_CLUSTERING_ENGINE_v1_DRAFT`, `GOLDEN_SENSOR_FUSION_ANDROID_v1_DRAFT`; tutti con scope limitato. Non toccare `CURRENT.yaml`, Golden Index o Registry fino a PR separata con prove.

## Benchmark e criteri di adozione nelle app

- Misurare 0/1/100/500/5000 fonti quando l'algoritmo lo supporta, p50/p95, RAM, output digest, durata on main isolate vs isolate, dimensione APK delta e device thermal/battery.
- Per MinHash usare corpus autorizzato, recall rispetto a Jaccard esaustivo, precision dei suggerimenti reali, false negatives di LSH e test di edit/reindex. 5000 non è automaticamente consentito dal donor da 500; misurare un algoritmo comparabile con budget esplicito.
- Per NB/logit/HMM usare validation set separato, confusion matrix, macro F1, class imbalance, dataset freshness e abstention; niente «accuracy» da pochi esempi costruiti.
- Per sensori usare p95 e consumi in background su due famiglie OEM; sampling/lifecycle e comportamento allarme prima della promozione.
- Per LiteRT includere licenza commerciale del singolo checkpoint, data, checksum, footprint per ABI, memoria runtime e benchmark fisico; senza questi, nessun model pack distribuito.
- **Privacy e UX:** account isolation, trasparenza, opt-in, visualizzazione della causa, correzione/undo, eliminazione degli indici alla cancellazione dati, no inferenze emotive automatiche.

## Stato finale e prossime decisioni

- Intake **10/10 catalogato** come crosswalk; nessun CAP ID riutilizzato o inventato. Linkare questa scheda dall'Inbox e dal README della capability.
- Due motori nel Core PR #71 **in implementazione/validazione separata**, non ancora `CERTIFIED DONOR` al momento di questo documento. I file e i test proposti non sono certificazione runtime.
- App da integrare **solo con PR separate** e secondo Product Bible: Notes #48 per duplicati, editor tag per NB, Pocket/FocusSense in shadow se realmente utile, Cooking Anime ingredient catalog solo dopo ricerca QA.
- Nuova CAP soltanto se una responsabilità consumer non risulta già coperta, con aggiornamento del JSON canonico, kit a 6 file, generator e `--check`; non creare capability per ciascun nome di algoritmo.

## Aggiornamento esecuzione motori P1/P2/P3 e catalogo — 04/11/2026

- [Core PR #73 merged](https://github.com/riccardopinato/App-Factory-Core/pull/73), main `02f3cd94f0ee6f19bc06fc0cb329fdf5398a739b`, [reference-Dart main CI SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41838055370) e [Factory validation SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41838055475). Implementazioni **reference math** per EWMA/Holt/Winters, kNN, regressione logistica, LOF, isolation-path proxy, HMM Viterbi, HAC bounded e PCA/TruncatedSVD approssimate. Nessuna inferenza personalizzata certificata.
- Precedente [Core PR #71](https://github.com/riccardopinato/App-Factory-Core/pull/71) e [CI main](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497699): MinHash/LSH e Naive Bayes pure-Dart. EWMA+hysteresis resta donor math nel precedente ML23, senza nuovo alarm decision path.
- [Notes PR #57](https://github.com/riccardopinato/Notes-Ecosistema/pull/57): candidato consumer solo **read-only** CAP-0116; non equivalente al merge reversibile richiesto dall'issue #48, stato e main CI da verificare separatamente.
- Vision/audio LiteRT/CoreML: **NON IMPLEMENTATO**; mancano modello/versione/license/footprint e precision-device test. Tutti gli algoritmi matematici restano senza dipendenze ML esterne.
- [Audit quantitative full-scope 160/385](AUDIT_COMPLETO_ML10_2026-11-04.md) usa HEAD dei 31 repo censiti; 17 app/idee fuori inventario non sono dichiarate source-verified.
