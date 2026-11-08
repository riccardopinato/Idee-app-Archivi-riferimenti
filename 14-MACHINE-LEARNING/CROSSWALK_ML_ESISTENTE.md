# Crosswalk ML esistente — punto di partenza, non nuovo intake

Questo documento indirizza ai lavori ML **già svolti e presenti nel repository**. Non crea ID CAP nuovi, non registra repository mai ricevuti e non modifica alcuno stato implementativo.

## 1. Audit storico dei 23 algoritmi

- [Catalogo 23 tecniche](../11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md).
- [Mappa ML23/Golden](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md).
- [Grafo dei motori](../12-CAPABILITY-E-IMPLEMENTAZIONI/CATENE_MOTORI_ML_2026-11-04.json).

Nel lavoro del 04/11 sono state identificate **10 capability nuove** (CAP-0151...CAP-0160) e **13 riusi di CAP esistenti**. Famiglie individuate: lexical text, scheduling/forecast, behavioral patterns, geo geometry, sensor signal. Gli algoritmi da soli **non sono donor certificati**.

## 2. Secondo lotto delle 10 famiglie on-device

- [ML10: audit Donor/Golden](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md).
- [ML10: audit 160 CAP / 385 associazioni (snapshot storico)](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_COMPLETO_ML10_2026-11-04.md).
- [ML10: consumer Notes e TasteAI](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_CONSUMER_POSTMERGE_2026-11-04.md).
- [ML10: screening Vision/Audio](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_MODEL_SCREENING_2026-11-04.md).

Famiglie studiate: Isolation Forest / LOF; MinHash + LSH; agglomerative clustering; HMM; PCA / SVD; Naive Bayes; kNN; regressione logistica; LiteRT/Core ML Vision/Audio; smoothing Holt/Holt-Winters. **Nessuna nuova CAP in ML10**: erano tecniche alternative o approfondimenti di contratti già presenti.

## 3. Esempi di dedup da applicare ai nuovi repo

| Tecnica / modulo ritrovato | Prima ricerca CAP | Attenzione |
|---|---|---|
| Fuzzy string matching, edit distance | CAP-0152 | Verificare differenza reale da ricerca esistente |
| Tag, TF-IDF, parole chiave | CAP-0160 | Evitare secondo indicizzatore non necessario |
| Similarità/ricerca ibrida, embedding | CAP-0032 e altre CAP Search | Modelli/pesi hanno licenza indipendente |
| Duplicate review MinHash / LSH | CAP-0116 | Suggerire, non cancellare o fondere automaticamente |
| Adaptive threshold / EWMA | CAP-0158, CAP-0057 | Device/OEM e falsi allarmi da misurare |
| Markov/routine opt-in | CAP-0154 | Non inferire salute, umore o altri dati sensibili |
| Vision cibo | CAP-0046 | Non inferire allergeni sicuri da immagini |
| Classificazione audio | CAP-0132 | Microfono, latenza, modello e consenso sono gate |
| Similarità ricette e raccomandazioni | CAP-0044 | Categorie e hard constraints prima del ranking |
| Clustering spaziale | CAP-0159 | Ground truth, coordinate, precisione, privacy |

Questa mappa è orientativa. Prima di assegnare un CAP al nuovo repo aprire il **registro canonico live**, leggere il contratto e distinguere estensione da capacità veramente diversa.

## 4. Evidenza ≠ goldenizzazione

I rapporti storici documentano PR Core e consumer per motori matematici. Ciò **non certifica** automaticamente il comportamento end-to-end su ogni dispositivo né consente di chiamare GOLDEN una dipendenza esterna. Per i prossimi MLR:
- fonte/commit/file e licenza separati per codice, weights, data;
- test e benchmark verificati nello scope reale;
- adapter leggero, minore impatto possibile su APK;
- no cambi alle app o ai Golden per effetto dell'audit;
- se il contratto è nuovo, admission e kit solo tramite il workflow del registro canonico.

## 5. Stato del catalogo più recente osservato

La sezione Capability riportava al **08/11/2026 199 CAP e 441 associazioni** dopo l'ammissione E0 OSS95. I numeri degli audit ML del 04/11 (160/385) sono **snapshot storici**, non il conteggio attuale da riutilizzare senza verifica.
