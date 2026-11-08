# Audit ML — primo lotto di 10 fonti GitHub (08/11/2026)

**Factory baseline fissata:** App-Factory-Core `c709e483d40424c88b6ba316d0c8352eec5370fe`; Master 27, Golden Index 28. **Livello di prova:** E1 (README/root/commit/licenza/file pertinenti su GitHub). **Non sono stati eseguiti test di runtime su Android/iOS/Flutter, benchmark o integrazioni**. Le classificazioni P1/P2/P3 sono euristiche di esplorazione, non ordini di implementazione.

## 1. I 10 riferimenti, senza confondere codice e lista

| MLR | Risorsa | Tipo effettivo | Priorita | Potenziale riuso |
|---|---|---|---|---|
| [MLR-0001](SCHEDE/MLR-0001.md) | scikit-learn | Libreria Python/Cython | P2 | Benchmark/reference K-Means, DBSCAN e test, non package mobile |
| [MLR-0002](SCHEDE/MLR-0002.md) | mljs | Aggregatore JavaScript + 5 moduli | P1 | Naive Bayes, kNN, clustering, distance; scoped JS donor candidato |
| [MLR-0003](SCHEDE/MLR-0003.md) | River | Python/Rust online learning | P1 | Regressione online, Page-Hinkley drift; pattern Dart/Kotlin |
| [MLR-0004](SCHEDE/MLR-0004.md) | Microsoft ML-For-Beginners | Corso e notebook | P2 | Metriche, data cleaning/NLP e basi di valutazione |
| [MLR-0005](SCHEDE/MLR-0005.md) | Neural Networks Zero to Hero | Notebook educativi | P3 | Micrograd, autograd, NN; niente runtime/model pronto |
| [MLR-0006](SCHEDE/MLR-0006.md) | Homemade Machine Learning | Moduli Python NumPy | P1 | Regressione/K-Means leggibili, porting math minimo |
| [MLR-0007](SCHEDE/MLR-0007.md) | 500 AI Projects | Elenco di link | P3 | Discovery; LICENSE root non trovato, no code reuse |
| [MLR-0008](SCHEDE/MLR-0008.md) | Kaggle Solutions | Indice Astro/YAML PROVVISORIO | P2 | Competition metrics/writeup; nessun codice figli licenziato |
| [MLR-0009](SCHEDE/MLR-0009.md) | Awesome Production ML | Awesome list MLOps | P2 | Discovery di ottimizzazione, monitoraggio, deploy |
| [MLR-0010](SCHEDE/MLR-0010.md) | Awesome Machine Learning | Awesome list per linguaggio | P2 | Discovery; LICENSE ambiguo, no code reuse diretto |

**Fonte MLR-0002:** `mljs` e un'organizzazione, non un singolo repository: la libreria aggregatrice `mljs/ml` e i cinque package figli ispezionati hanno commit autonomi, documentati nella [scheda](SCHEDE/MLR-0002.md). **Fonte MLR-0008:** il nome Kaggle Solutions era senza URL; `faridrashidi/kaggle-solutions` e scelta rappresentativa PROVVISORIA, con un'alternativa documentata.

## 2. Estrazioni Donor, Golden, capability e consumer

| Proposta scoped | Fonti con codice verificato | CAP canoniche gia esistenti | Consumer / valore | Gate tecnico prima di riuso |
|---|---|---|---|---|
| **Donor candidato: classificatore testuale** | mljs/naive-bayes (MultinomialNB), moduli source MIT verificati | CAP-0160, CAP-0148 | Notes: tag suggeriti, senza cambio automatico | Tokenizzazione IT/EN, dataset etichettato, F1 e astensione; JS solo per Web o riscrittura Dart |
| **Donor candidato: K-Means/geometry** | mljs/kmeans e scikit-learn/cluster/_kmeans.py | CAP-0124, CAP-0159 | Notes: cluster note; Wonderlog/TrailPath: confronti spaziali | Convergenza, seed, cluster vuoti, N piccolo, confronto precision e CPU |
| **Donor candidato: regressione minimale** | Homemade LinearRegression e River linear_model | CAP-0153, CAP-0061 | Battery Guard/studio: stima con intervalli e fallback | Split temporale, MAE, poche osservazioni, outlier; niente port diretto NumPy |
| **Pattern candidato: sensor drift** | River drift/page_hinkley.py | CAP-0158, CAP-0057 | Pocket Guard/FocusSense: rilevare spostamento baseline sensore | Confronto con EWMA/isteresi esistenti, OEM, falsi allarmi, energia |
| **Donor candidato: kNN affinità** | mljs/knn KD-tree | CAP-0044 | TasteAI: confronto/estensione del donor ricette gia riportato; Cooking Anime dopo consenso scope | Non duplicare algoritmo gia in TasteAI; fallback con dataset piccolo, feature scaling |
| **Fixture/reference per valutazione** | scikit-learn, Microsoft, Kaggle index | CAP-0032, CAP-0160, CAP-0153 | Notes/agenda: test e metriche ripetibili | Verificare diritti sui dataset separatamente; no leakage |
| **Ottimizzazione/runtime screening** | EthicalML e Awesome ML (solo elenchi) | Nessuna nuova CAP per mera lista | Tutte: scegliere libreria/on-device runtime specifico | Audit del figlio, licenza weights/dataset, delta APK/RAM/CPU e compatibilita ABI |
| **Autodiff didattico** | Karpathy notebook Micrograd | Nessuna CAP prodotto nuova | Formazione tecnica R&D | Nessuna implementazione finche non c'e bisogno e benchmark |
| **Idee da link esterni** | 500 AI Projects (solo indice) | Nessuna CAP nuova | Ricerca di soluzioni specifiche | LICENSE root mancante; audit ogni figlio, no codice importato |

### Donor, Golden e ammissione: decisioni

- **Donor esterni:** classificati soltanto **CANDIDATE** o **PATTERN REFERENCE**. Nessun codice, package, modello o weights e stato copiato nelle nostre app.
- **Golden candidati:** (a) classificazione locale opt-in con explainability; (b) signal/online drift engine bounded; (c) fixture matematiche per regressione/clustering. **Nessun nuovo Golden creato**: prima si verifica compatibilita con Golden Hybrid Local Search, Local Rules, Explainable Recommendation, Sensor Fusion e Performance Fixture gia elencati nella Factory, e con motori math reference testati nei precedenti audit.
- **Nessuna nuova CAP**: la relazione tra queste fonti e le funzionalita e riportata nei record MLR; il [registro canonico](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json) conserva le responsabilita. Le famiglie gia censite sono in [ML23](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md) e [ML10](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md).

## 3. Priorita dei micro-step di ricerca (nessuna integrazione automatica)

1. **P1 Notes — Naive Bayes per suggerire tag.** Fase shadow con note sintetiche e test su vocaboli IT/EN, fallback TF-IDF/rule-based. Evitare classificazione diagnostica dello stato emotivo; nessun salvataggio automatico.
2. **P1 Sensor engine — Page-Hinkley vs EWMA.** Confrontare sui dispositivi e sui flussi realmente disponibili per Pocket Guard/FocusSense/Battery Guard, ma soltanto se i motori esistenti CAP-0158 non coprono gia il problema.
3. **P1 Regressione leggera.** Benchmark algoritmi Homemade e River contro fixture scikit, poi adapter minimo se un preciso consumer mostra delta positivo.
4. **P2 Ricette — kNN e ranking pesato.** Verificare prima l'implementazione esistente TasteAI CAP-0044; non dichiarare nuovo cio che e gia integrato. Per Cooking Anime serve ammissione prodotto separata.
5. **P2 Test di clustering.** Niente cluster spaziali ricalcolati a ogni frame, nessuna geo-inferenza non necessaria; precisare n e scala dati.
6. **P2 Profiling/runtime.** Da Awesome Production selezionare librerie specifiche: la lista non prova che Vision/Audio sia possibile sotto 1 MB.
7. **P3 Educazione e idea discovery.** Microsoft/Karpathy/500 AI/Kaggle per formazione e ricerca puntuale di repo figli.

## 4. Errori e limitazioni corretti nel materiale ricevuto

- **Homemade non e senza dipendenze:** gli algoritmi leggono NumPy e il requirements.txt fissa versioni obsolete, incluso `numpy==1.15.3`.
- **River non e un SDK mobile:** Python/Rust e streaming per algoritmi specifici, con costi di preprocessing e possibili falsi allarmi.
- **scikit-learn non e un import Flutter:** buona reference per contratti e test numerici, non necessariamente il codice piu piccolo per dispositivo.
- **mljs non e una libreria Dart:** web/PWA si, con bundle e licenze verificati; su Flutter Android serve un bridge giustificato o adapter nativo.
- **500 AI e Kaggle sono indici:** le soluzioni esterne non ereditano MIT, non sono codici gia testati e possono avere dataset/rules non redistribuibili.
- **Awesome list non sono pacchetti inferenza:** per ogni link figlio occorre un nuovo audit. Awesome Machine Learning ha un LICENSE root ambiguo (`Creative Commons Legal Code / No need`), code copying bloccato.
- **TextRank e CAP-0151 gia censiti:** nessuno dei 10 campioni attuali e stato verificato come donatore di TextRank; il riassunto di note resta candidato alla verifica del motore interno.
- **Nessuna promessa di pochi millisecondi o 0 batteria:** tempi, memoria, impatto APK, 90% di accelerazione PCA, classificazione audio sotto 1 MB e accuratezza sono NON MISURATI qui.
- **Sentiment testuale non e umore:** evitare inferenze sanitarie o emotive sulla persona senza un progetto privacy/consenso dedicato.

## 5. Tracciabilita, prossimo gate e confini

Le prove per ogni fonte sono collegate alla scheda individuale e al JSON [REGISTRO_FONTI_ML.json](REGISTRO_FONTI_ML.json). Ogni fonte registra SHA, licenza del contenitore, fonti, ruoli, target plausibili, stato e prossimo gate. La radice contiene risorse di sola ricerca: nessuna modifica a Flutter/Android, nessun dataset utente scaricato, nessuna promozione Golden, nessuna API/cloud o package introdotto, nessuna versione di app pubblicata.
