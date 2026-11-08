# Machine Learning — registro e laboratorio di riuso App Factory

Sezione dedicata esclusivamente alla **ricerca, analisi ed estrazione di repository, algoritmi, modelli e strumenti Machine Learning**. È un **catalogo di intake**: non è una seconda source of truth delle capability e **non autorizza** nuove integrazioni, API, costi o promozioni Golden.

**Stato iniziale (08/11/2026):** sezione creata; nessun nuovo repository fornito in questo lotto. Sono già presenti due audit ML storici (23 algoritmi + 10 famiglie), collegati nel crosswalk. La registrazione del primo repo avverrà quando verrà fornito un link concreto.

## Navigazione

- [Inbox link da esaminare](INBOX_REPOSITORY.md) — ordine di arrivo, ID stabili, stato.
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
