# Agenda-per-Anna — Da valutare (8)

Derivato dal registro canonico per la **singola app**. Candidate ancora aperte, senza soglie di score. Non comprende integrazioni parziali, dichiarate o verificate.

[Da valutare](DA_VALUTARE.md) · [Già integrati](GIA_INTEGRATI.md) · [Da verificare](DA_VERIFICARE.md) · [CSV ordinabile in Excel](TABELLA.csv) · [Scheda storica](../Agenda-per-Anna.md)

| CAP ID | Capability | Priorità | Facilità | Stato per app | Fonte / prova | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| [CAP-0152](../../REGISTRO_CAPABILITY/CAP-0152.md) | Ricerca fuzzy offline per refusi e alias | 96 | 89% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0152/README.md) | Top-K bounded, grapheme, token di 1 carattere, soglie false-match, 500/5000 record e nessuna fuga da Shared Spaces. |
| [CAP-0160](../../REGISTRO_CAPABILITY/CAP-0160.md) | Estrazione TF-IDF di parole chiave e tag suggeriti | 91 | 80% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0160/README.md) | Tokenizzazione IT/EN/ES/FR/DE/PT, stopwords, IDF stabile, shared ACL, gestione corpus piccolo, preview prima di tag writer. |
| [CAP-0031](../../REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | 86 | 35% | PROPOSTA | [Audit di sorgente](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/13-KIT-INTEGRAZIONE/CAP-0031/ANNA_SOURCE_COMPATIBILITA.md) | Licenza modello footprint benchmark 5 lingue e download opt-in |
| [CAP-0151](../../REGISTRO_CAPABILITY/CAP-0151.md) | Riassunti estrattivi di note con TextRank e citazioni | 85 | 72% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0151/README.md) | Segmentazione multilingua, citazioni/negazioni, source-revision, test di frasi non inventate, fallback a estratto lineare. |
| [CAP-0159](../../REGISTRO_CAPABILITY/CAP-0159.md) | Clustering spaziale privacy-safe per ricordi e POI | 85 | 70% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0159/README.md) | Antimeridiano/poli, GPS nullo/non finito, raggio geodesico, permesso luoghi condivisi, dati privati non esportabili per default. |
| [CAP-0121](../../REGISTRO_CAPABILITY/CAP-0121.md) | Lettura semplificata con originale affiancato | 81 | 35% | PROPOSTA | [Audit di sorgente](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/13-KIT-INTEGRAZIONE/CAP-0121/ANNA_SOURCE_COMPATIBILITA.md) | Dataset multilingue Easy-Language come riferimento; rischio di cambiare significato, soprattutto testi legali/medici. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0153](../../REGISTRO_CAPABILITY/CAP-0153.md) | Previsione prudente di completamento studio e progetti | 80 | 73% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0153/README.md) | Minimo storico, anomalie, weekend e pause, intervallo di confidenza onesto, mai date certe da campioni scarsi. |
| [CAP-0154](../../REGISTRO_CAPABILITY/CAP-0154.md) | Routine predittive con Markov solo opt-in | 71 | 72% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0154/README.md) | Opt-in, minimal retention, cancellazione, min-sample, divieto inferenze sensibili e zero notifiche automatiche. |

**Totale associazioni app:** 74. Nessuna modifica alla roadmap o al codice dell'app.
