# Machine Learning — registro e laboratorio di riuso App Factory

Sezione dedicata esclusivamente alla **ricerca, analisi ed estrazione di repository, algoritmi, modelli e strumenti Machine Learning**. È un **catalogo di intake**: non è una seconda source of truth delle capability e **non autorizza** nuove integrazioni, API, costi o promozioni Golden.

**Stato (08/11/2026):** **21 fonti ML uniche, MLR-0001...MLR-0021**, due lotti elaborati (10 + 20 riferimenti; 9 ripetizioni/alias deduplicate nel secondo). Livello verificato **E1** con SHA e licenze del repository principale; NESSUN test di inferenza su device, modello scaricato o Golden/Donor certificato. Rimangono collegati gli audit ML23 e ML10 storici.

## Navigazione

- [Inbox 21 fonti GitHub](INBOX_REPOSITORY.md) — ID stabili, SHA, dedup e stato degli audit.
- [Secondo lotto: crosswalk completo 20 riferimenti](AUDIT_20_RIFERIMENTI_ML_LOTTO2_2026-11-08.md) — 11 fonti nuove, 9 duplicate, target e priorita.
- [Schede nuove MLR-0011...0021](SCHEDE/MLR-0011.md) — accessibili singolarmente dall'Inbox.
- [Audit comparativo e priorita](AUDIT_10_REPOSITORY_ML_2026-11-08.md) — Donor, Golden candidati, CAP e consumer.
- [Schede lotto 1 MLR-0001...MLR-0010](SCHEDE/MLR-0001.md) — link individuali disponibili dall'Inbox.
- [Registro machine-readable](REGISTRO_FONTI_ML.json) — inventario dei repository esaminati e collegamenti alle CAP.
- [Protocollo di analisi](PROTOCOLLO_AUDIT_ML.md) — verifiche, dedup, licenze, test e gate.
- [Template di scheda](TEMPLATE_SCHEDA_REPOSITORY.md) — output obbligatorio per ciascuna fonte.
- [Crosswalk iniziale](CROSSWALK_ML_ESISTENTE.md) — mappa verso il lavoro ML già catalogato.

## Per ogni repository ML inviato

1. **Identificazione:** URL canonico, owner, default branch, commit SHA fissato, data, manutenzione, stack e licenza.
2. **Audit reale:** README, sorgenti pertinenti, modelli/weights, dataset, esempi, test, CI, dipendenze e comportamento dimostrabile. Dichiarare il livello effettivo della verifica.
3. **Estrazione selettiva:** capability implementabili, algoritmi e pattern, moduli riusabili, Donor candidati, Golden candidati, eventuali idee per app autonome; evitare estrazione non pertinente.
4. **Crosswalk:** cercare prima le CAP esistenti in [registro canonico](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json); collegare la tecnica a uno o più ID solo se il contratto funzionale corrisponde. Una tecnica nuova **non implica** una nuova CAP.
5. **Ammissione:** distinguere utilità, facilità per ogni app, rischio, costo, privacy, licenza e qualità della prova; non cambiare automaticamente decisioni prodotto o stati app.
6. **Provenienza:** salvare scheda, fonte, SHA/file, verdict, limitazioni e next gate; aggiornare inbox e registro in modo incrementale e senza duplicati.
7. **Promozione separata:** Donor/Golden richiedono estrazione, test e prove secondo App Factory; questo repository conserva la **candidatura**, non rilascia certificazioni.

## Tipi da classificare distintamente

- **CODE DONOR CANDIDATE:** implementazione con possibile riuso di codice (solo dopo licenza verificata, adaptation e test).
- **PATTERN / ALGORITHM REFERENCE:** architettura, algoritmo o tecnica da reimplementare con contratto minimo.
- **MODEL / WEIGHTS CANDIDATE:** pesi/versione, model card, input-output, licenza e prestazioni da verificare separatamente dal codice.
- **DATASET / BENCHMARK SOURCE:** dati, termini, provenance e rappresentatività; nessuna redistribuzione implicita.
- **TOOL / RUNTIME / MLOPS:** tooling di training, inferenza, conversione, quantizzazione, profiling o monitoraggio.
- **APP IDEA CANDIDATE:** prodotto standalone da registrare in 11-NUOVE-IDEE prima di eventuale promozione.

Un repository può avere più ruoli; lo stato di licenza vale **per codice, pesi, dati e asset separatamente**. Non chiamare Golden un repository esterno semplicemente perché è interessante.

## Ambiti di ricerca

ML classico e statistico; NLP, ricerca ed embedding; Vision/OCR; audio; recommender; previsione e serie temporali; clustering; sensori e anomaly detection; on-device/edge inference; ottimizzazione e quantizzazione; privacy, sicurezza e MLOps.

Regola preferenziale: **motore locale leggero, spiegabile, opzionale** quando equivalente per il prodotto. Non introdurre modelli grandi, download o inferenze personali senza Product Bible, privacy e misure reali.

## Source of truth e limiti

- Policy/GOLDEN: [App-Factory-Core](https://github.com/riccardopinato/App-Factory-Core) tramite CURRENT.yaml (baseline di questa creazione: Master v27, Golden Index v28, Core main c709e483d40424c88b6ba316d0c8352eec5370fe).
- Capability canoniche e stati per app: [12-CAPABILITY-E-IMPLEMENTAZIONI](../12-CAPABILITY-E-IMPLEMENTAZIONI/README.md).
- Kit effettivi: [13-KIT-INTEGRAZIONE](../13-KIT-INTEGRAZIONE/README.md), solo dopo ammissione CAP.
- Nuove idee-prodotto: [11-NUOVE-IDEE](../11-NUOVE-IDEE/README.md).
- I test di Core, un README esterno, un download di modello e una CI verde **non** provano autonomamente runtime su device, compatibilità commerciale né Golden certificato.

**Workflow operativo:** ogni nuovo URL entra nell'Inbox con MLR progressivo, viene verificato al commit e poi genera una scheda di analisi; il JSON conserva provenienza e associazioni, senza duplicare REGISTRO_CAPABILITY.json. Gli esiti possono essere ADOTTABILE/DA STUDIARE/SOLO REFERENCE/BLOCCATO/SCARTATO con motivazione e prossimo gate.

## Conclusione operativa del secondo lotto

- **Runtime on-device:** ONNX Runtime (MLR-0011) candidato condizionato a modello e benchmark; TFLite Micro (MLR-0012) mirato a microcontrollori, non runtime telefono; Core ML Tools (MLR-0013) serve alla conversione per iOS, non e runtime app.
- **Codice NLP classico:** fastText (MLR-0015) offre classifier/vector/quantization ma GitHub lo segnala come archiviato; modelli, weights e corpus hanno condizioni distinte.
- **Governance ML:** DVC (MLR-0019) e MLflow (MLR-0020) appartengono a sviluppo/esperimenti, non all'APK; si adotta tooling solo se il beneficio misurato giustifica il costo operativo.
- **Raccolte e formazione:** risorse GenAI, LLM, Awesome LLM Apps non equivalgono a inferenza mobile offline: alcuni progetti usano Ollama locale su PC, altri servizi cloud e API.
- **Nessun falso donor:** awesome-mobile-ai (MLR-0014) contiene un loader Python segnaposto; non e un engine iOS/Android implementato.

Il secondo lotto ha inoltre risolto URL obsoleti di InterpretML e DVC e il nome ridotto della raccolta 500 AI. Prossimo ID disponibile: **MLR-0022**.
