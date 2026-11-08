# Audit secondo lotto Machine Learning: 20 riferimenti (08/11/2026)

Factory baseline: App-Factory-Core c709e483d40424c88b6ba316d0c8352eec5370fe (Master 27, Golden Index 28). Le priorita P1/P2/P3 sono euristiche di RICERCA. Evidence E1 (README, licenze, commit e file/codice pertinenti consultati), non test mobile o certificazione Donor/Golden.

## Crosswalk integrale 20/20

| # | Scheda | Repository verificato | Dedup | Priorita |
|---:|---|---|---|---|
| 1 | [MLR-0011](SCHEDE/MLR-0011.md) | [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | NUOVO | P1 |
| 2 | [MLR-0012](SCHEDE/MLR-0012.md) | [tensorflow/tflite-micro](https://github.com/tensorflow/tflite-micro) | NUOVO | P3 |
| 3 | [MLR-0013](SCHEDE/MLR-0013.md) | [apple/coremltools](https://github.com/apple/coremltools) | NUOVO | P2 |
| 4 | [MLR-0014](SCHEDE/MLR-0014.md) | [umitkacar/awesome-mobile-ai](https://github.com/umitkacar/awesome-mobile-ai) | NUOVO | P3 |
| 5 | [MLR-0015](SCHEDE/MLR-0015.md) | [facebookresearch/fastText](https://github.com/facebookresearch/fastText) | NUOVO | P2 |
| 6 | [MLR-0001](SCHEDE/MLR-0001.md) | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | GIA PRESENTE | P2 |
| 7 | [MLR-0002](SCHEDE/MLR-0002.md) | [mljs/ml](https://github.com/mljs/ml) | GIA PRESENTE | P1 |
| 8 | [MLR-0003](SCHEDE/MLR-0003.md) | [online-ml/river](https://github.com/online-ml/river) | GIA PRESENTE | P1 |
| 9 | [MLR-0016](SCHEDE/MLR-0016.md) | [interpretml/interpret](https://github.com/interpretml/interpret) | NUOVO; URL CORRETTO | P2 |
| 10 | [MLR-0004](SCHEDE/MLR-0004.md) | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | GIA PRESENTE | P2 |
| 11 | [MLR-0005](SCHEDE/MLR-0005.md) | [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | GIA PRESENTE | P3 |
| 12 | [MLR-0006](SCHEDE/MLR-0006.md) | [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) | GIA PRESENTE | P1 |
| 13 | [MLR-0017](SCHEDE/MLR-0017.md) | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | NUOVO | P3 |
| 14 | [MLR-0018](SCHEDE/MLR-0018.md) | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | NUOVO | P3 |
| 15 | [MLR-0007](SCHEDE/MLR-0007.md) | [ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) | GIA PRESENTE; ALIAS | P3 |
| 16 | [MLR-0010](SCHEDE/MLR-0010.md) | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | GIA PRESENTE | P2 |
| 17 | [MLR-0009](SCHEDE/MLR-0009.md) | [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | GIA PRESENTE | P2 |
| 18 | [MLR-0019](SCHEDE/MLR-0019.md) | [treeverse/dvc](https://github.com/treeverse/dvc) | NUOVO; OWNER AGGIORNATO | P2 |
| 19 | [MLR-0020](SCHEDE/MLR-0020.md) | [mlflow/mlflow](https://github.com/mlflow/mlflow) | NUOVO | P3 |
| 20 | [MLR-0021](SCHEDE/MLR-0021.md) | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | NUOVO | P3 |

**Totali:** 20 voci ricevute, **11 nuove MLR-0011..0021**, 9 duplicati/alias a MLR precedenti, **21 fonti uniche** nel catalogo. Gli 8 duplicati con indirizzo canonico preesistente hanno HEAD verificato invariato, quindi nessuna duplicazione di scheda. Nessuna CAP nuova ammessa.

## Identita, errori di nomenclatura e scope

- Voce #9: interpret-ml/interpret non esiste (404): il progetto verificato e interpretml/interpret (MLR-0016).
- Voce #18: dvc-org/dvc non esiste (404); iterative/dvc rimanda al repository treeverse/dvc (MLR-0019).
- Voce #15: il nome abbreviato ashishpatel26/500-AI-Machine-learning-Projects non esiste; la risorsa gia catalogata e MLR-0007 (indice di collegamenti, senza LICENSE root verificato).
- MLR-0018: GitHub API dice NOASSERTION, ma il file LICENSE.txt letto contiene Apache License 2.0; non vale per pesi/modelli/dataset terzi.

## Donor, Golden candidati e CAP canoniche da riusare

| Priorita | Modulo/pattern | Fonte | CAP esistenti | Consumer e next gate |
|---|---|---|---|---|
| P1 condizionata | ONNX Runtime, native Android/Web, model load | MLR-0011 | CAP-0032, CAP-0033, CAP-0132 | Notes: modello licenziato, CPU/RAM, ABI, APK delta, p95 su device |
| P2 | fastText C++ con classificazione e compressione .ftz | MLR-0015 | CAP-0160, CAP-0134 | Notes: F1 corpus italiano, confronto TF-IDF/Naive Bayes, repo archived |
| P2 | Core ML conversion per iOS, NON runtime mobile | MLR-0013 | CAP-0032, CAP-0132 | iPhone: model conversion e test, compare accuracy/latency |
| P2 | Explainable ML / EBM | MLR-0016 | CAP-0153, CAP-0134 | Battery Guard/studio: dataset tabulare autorizzato, baseline semplice e spiegazioni affidabili |
| P2 tooling | DVC experiment/dataset versioning (locale possibile) | MLR-0019 | Nessuna CAP app | R&D App Factory: provare riproducibilita fixture sintetiche senza remotes |
| P3 tooling | MLflow experiment tracking e tracing | MLR-0020 | Nessuna CAP app | Confrontare log JSON locale vs servizio MLflow; proteggere dati/segreti |
| P3 | RAG, SLM, agenti, attenzione/LLM educativi | MLR-0017, MLR-0018, MLR-0021 | CAP-0032, CAP-0033, CAP-0097 | Notes: pattern local-first con provenance, nessuna API obbligatoria |
| P3 | Embedded TinyML con micro-interpreter | MLR-0012 | CAP-0057, CAP-0132 (relazione solo tecnica) | Hardware microcontroller futuro, NON Android/iOS default |
| P3 | Mobile AI resource index e scaffold Python | MLR-0014 | Nessuna CAP | Source scaffold _load_model e placeholder; NON donor funzionale |

## Limiti riscontrati nel codice e licensing

- ONNX Runtime contiene Java JNI e SDK JavaScript (Web/React Native); la dimensione runtime, l'integrazione Flutter, gli operatori e un MODELLO concreto sono ancora da verificare.
- TensorFlow Lite Micro e specifico per sistemi bare-metal/microcontroller e DSP; non va confuso con il normale runtime mobile LiteRT/TFLite.
- coremltools e toolkit Python di conversione: l'inferenza su iPhone usa il framework Core ML, non il package Python.
- awesome-mobile-ai: src/mobile_ai/core.py ha _load_model non implementato e predict con placeholder; la presenza di test/README non prova inferenza reale.
- fastText e ARCHIVED su GitHub: C++ e quantization esistono, ma manutenzione/sicurezza e licenze modelli sono gate aperti.
- Microsoft GenAI course include servizi Azure/OpenAI, oltre ad esempi Foundry Local; non ogni lezione e offline o priva di costi API.
- rasbt/LLMs-from-scratch e una guida PyTorch di training, non un modello leggero gia pronto per l'APK.
- DVC e MLflow sono tool di sviluppo e controllo, non librerie da incorporare automaticamente nelle app; DVC puo tenere esperimenti locali, MLflow puo coinvolgere un servizio.
- awesome-llm-apps: il local_rag_agent usa Ollama, Qdrant locale e Llama 3.2 scaricato; il deepseek_local_rag_agent descrive Qdrant Cloud e opzione Exa API. Niente garanzia di offline universale o footprint mobile.
- LICENSE del codice principale non autorizza automaticamente modelli/pesi, tokenizer, dataset, immagini, third-party packages. Le misure CPU, RAM, AAB/APK, battery, p50/p95, F1 e qualità sono NON MISURATE.

## Decisione

Catalogazione E1 di fonti/ruoli/possibili consumer, non autorizzazione Product Bible o app code. Nessun download di modelli, copia di codice terzo, Golden certificato, Donor certificato, CAP aggiunta o piattaforma cloud abilitata. Prima di qualsiasi adozione: baseline interna, una feature concreta, licenze per tutti gli asset, test exact-SHA, benchmark mobile e fallback.

Prossimo ingresso: MLR-0022.
