# Protocollo di audit per repository Machine Learning — v1

## 0. Ambito e governance

L'utente fornisce uno o più URL GitHub ML. Per ogni URL, eseguire l'audit **incrementale** e aggiornare solo la sezione di ricerca del repo Idee. In assenza di una richiesta specifica, non installare dipendenze, eseguire modelli di terze parti sui dati dell'utente, modificare app/Factory, scaricare pesi, aprire nuove infrastrutture né promettere performance non misurate.

Applicare nell'ordine: App-Factory-Core/CURRENT.yaml > Master selezionato > Golden Index/Registry > Golden pertinenti > questo AGENTS.md > questo protocollo. Il registro canonico CAP è 12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json. Qui non nasce un secondo catalogo CAP.

## 1. Acquisizione e controllo qualità della fonte

- Concretizzare URL, repository owner/name, tipologia originale/fork, branch, **SHA completo fissato**, data acquisizione, linguaggio, dimensione e stato maintenance.
- Leggere LICENSE e file/asset specifici: il codice può avere termini diversi da dataset, pesi pretrained, tokenizer, immagini, checkpoint e modelli derivati. Cercare NOTICE, commercial restrictions, attribution, redistribution, copyleft e access conditions.
- Verificare README, directory funzionali, API, dipendenze, demo, test, workflow CI, release, issue critiche; distinguere claim di marketing da feature code.
- Se il repository non è accessibile, mantenere URL e stato BLOCCATO / NON_VERIFICATO senza inventare file, SHA o licenze.
- Per repository aggiornato: confrontare commit e diff con ultimo SHA già documentato; non ripetere inutilmente audit invariati.

## 2. Scomposizione ML (molti moduli, non una singola feature)

Per ogni estrazione indicare **che cosa fa** e che cosa non fa, ruolo e input/output:
- Algoritmo puro o statistico: normalizzazione, ranking, clustering, regressione, filtri, detection, recommender.
- Training: dataset richiesto, labeling, train/test split, leakage, parametrizzazione, retraining e versionamento.
- Inference: target Android/iOS/Web/PC, CPU/GPU/NPU, runtime e ABI, preprocessing/postprocessing, offline, inferenza deterministica o probabilistica.
- Modello/weights: file esatto, checksum, licenza, model card, lingue/classi, metriche su benchmark, quantizzazione, compatibilità e versione.
- Dati: provenienza, autorizzazione d'uso, consenso, durata conservazione, rischi privacy, rappresentatività e fair use.
- UX: trigger visibile, suggerimento reversibile, spiegazione, confidence **calibrata** o astensione quando mancano dati.

Non confondere un motore rule-based con un modello addestrato; entrambi possono essere candidati utili, ma vanno classificati correttamente.

## 3. Crosswalk e deduplicazione

1. Cercare responsabilità equivalente tra le CAP canoniche **alla versione live**, quindi tra i relativi kit e Golden/donor.
2. Se equivalenza esiste, collegare MLR -> CAP esistente (e specificare delta rispetto all'implementato).
3. Se la tecnica cambia soltanto la strategia interna (es. kNN vs similarità coseno), **non creare CAP** separata senza nuovo contratto di prodotto.
4. Se emerge una responsabilità veramente nuova, registrare **PROPOSTA CAP NON ANCORA AMMESSA**, con definizione, consumer e anti-dup; numerazione monotona, sei file kit, generazione delle viste e CI solo attraverso il workflow canonico autorizzato.
5. Un'idea di app standalone segue 11-NUOVE-IDEE; il singolo repository ML non approva Product Bible né roadmap.

## 4. Catalogazione dell'opportunità

Per ogni proposta registrare:
- Categoria tecnica, utilità App Factory e consumer plausibili con motivazione **per app**.
- Classificazione: CODE DONOR / PATTERN REFERENCE / MODEL / DATASET / RUNTIME TOOL / APP IDEA.
- Tipo di riuso: libreria compatibile, estrazione minima, clean-room rewrite, benchmark soltanto, scarto.
- Baseline già in app/Golden, delta esatto, dipendenze aggiunte, costo CPU/RAM/batteria, impatto APK/AAB e Web.
- Licenze e condizioni di uso commerciale, costi API/cloud, download on-demand, lingua/mercato e compatibilità dei target.
- Rischi: privacy, inferenza sensibile, permessi, bias, falsi positivi/negativi, drift, hallucination se generativo, prompt-injection/poisoning/data-leakage, sicurezza supply chain.
- Score comparativo (valore, riuso, facilità, evidence, rischio), **segnalato come euristico** e mai come percentuale di successo.
- Giudizio finale e **next gate** verificabile.

## 5. Qualità delle evidenze e promozioni

| Livello | Dimostrazione | Cosa NON dimostra |
|---|---|---|
| E0 | Link, idea, metadati e possibile CAP | Esistenza di codice utile o permesso di copia |
| E1 | SHA esatto, file rilevanti, contratto e licenza controllata | Test eseguiti |
| E2 | Test o benchmark documentati nel repo | PASS nel nostro ambiente |
| E3 | Adattamento/donor scoped, test mirati realmente eseguiti e CI exact-head | Device, provider o Store |
| E4 | Test fisico/provider su target e artifact reale quando richiesto | Riutilizzabilità in seconda app |
| E5 | Riuso indipendente in consumer con test di contratto | Qualsiasi altra capability non testata |

I repository esterni partono da E0/E1: **mai** Golden certificati per sola notorietà, licenza permissiva o README. Una goldenizzazione richiede un artefatto interno adattato, prove, Registry/Index via processo Factory e, per certificazione multi-consumer, E5.

## 6. Benchmark e gate ML specifici

- Confrontare contro baseline deterministica o soluzione in uso; documentare corpus, versioni e campioni reali/sintetici.
- NLP/search: precision@k/recall@k, falsi duplicati, Unicode/IT/EN e citazioni/provenance.
- Classificazione: precision, recall, F1, matrice di confusione, soglia di astensione; probabilità solo se calibrate.
- Regressione/forecast: MAE/MAPE dove adatti, split temporale e no leakage, errore sui casi rari.
- Vision/audio: classi e test-set, permessi, condizioni reali, false alarm, consenso esplicito.
- Sensori: false positive/negative, OEM/OS, background restrictions, battery drain; niente dati segreti/sensibili in logs.
- Performance: startup, inferenza p50/p95, memoria picco, download, runtime + model bytes, batteria, CPU; misure con modello, device e ABI espliciti.
- Distribuzione: licenza verificata per weights/dataset, checksum, on-demand vs bundle, offline, fallback manuale, aggiornabilità/revoca.
- Qualità UX: nessun salvataggio/cancellazione automatica irreversibile; suggestions con spiegazione, anteprima e conferma quando modificano dati.

Se non ci sono misure, segnare **NON MISURATO**; non sostituire con numeri teorici.

## 7. Output obbligatorio per ogni link

1. ID MLR, identità e stato di accesso, SHA e licenze.
2. Tabella moduli reali -> responsabilità -> CAP esistente/novità proposta.
3. Donor candidati, Golden candidati (nessuna promozione implicita), pattern e modelli separati.
4. Consumer per app, compatibilità, stima di complessità e costo/footprint.
5. Verdetto, next gate e link alla scheda/evidenze.
6. Delta su Inbox/Registro e README se serve; changelog per ogni aggiornamento sostanziale.

**Validazione catalogo:** se si modifica solo documentazione/registro di questa sezione, controllare Markdown, link relativi e JSON valido. Se in futuro si modifica il REGISTRO_CAPABILITY.json, eseguire gli script canonici build_catalog.py e --check, kit obbligatori, test e CI exact-head prima del merge.
