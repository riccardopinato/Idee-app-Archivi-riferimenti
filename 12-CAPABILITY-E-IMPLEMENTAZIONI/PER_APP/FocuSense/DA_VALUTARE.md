# FocuSense — Da valutare (12)

Derivato dal registro canonico per la **singola app**. Candidate ancora aperte, senza soglie di score. Non comprende integrazioni parziali, dichiarate o verificate.

[Da valutare](DA_VALUTARE.md) · [Già integrati](GIA_INTEGRATI.md) · [Da verificare](DA_VERIFICARE.md) · [CSV ordinabile in Excel](TABELLA.csv) · [Scheda storica](../FocuSense.md)

| CAP ID | Capability | Priorità | Facilità | Stato per app | Fonte / prova | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| [CAP-0158](../../REGISTRO_CAPABILITY/CAP-0158.md) | Soglie adattive con isteresi per luce e prossimità | 96 | 89% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0158/README.md) | Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM. |
| [CAP-0065](../../REGISTRO_CAPABILITY/CAP-0065.md) | Routine wearable e battery optimization audit | 94 | 80% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0065/README.md) | Test OEM reale multi dispositivo e Doze |
| [CAP-0001](../../REGISTRO_CAPABILITY/CAP-0001.md) | Pianificazione di slot liberi | 93 | 95% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0001/README.md) | Anna: test fisici suggerimenti slot e avvisi sovrapposizione; dati esterni solo se autorizzati, nessuna scrittura automatica. Altre app: integrazione ancora proposta. |
| [CAP-0109](../../REGISTRO_CAPABILITY/CAP-0109.md) | Sessioni Focus/Pomodoro collegate a note e protezione opzionale | 91 | 95% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0109/README.md) | Riutilizzare eventuali timer FocusSense prima del codice; persistenza dopo app pause, gestione lifecycle e background Android, DND soltanto con permesso/azione esplicita; non promettere blocco siti. |
| [CAP-0145](../../REGISTRO_CAPABILITY/CAP-0145.md) | Heatmap locale di ricordi, attività e abitudini volontarie | 81 | 55% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0145/README.md) | No health/diagnostic claims, no dati ciclo/Vault in UI ordinaria, no esempi +40% spacciati per risultati; test missingness e permessi. |
| [CAP-0063](../../REGISTRO_CAPABILITY/CAP-0063.md) | Momenti ideali per focus in calendario | 80 | 90% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0063/README.md) | Consenso e niente spostamento eventi involontario |
| [CAP-0153](../../REGISTRO_CAPABILITY/CAP-0153.md) | Previsione prudente di completamento studio e progetti | 80 | 67% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0153/README.md) | Minimo storico, anomalie, weekend e pause, intervallo di confidenza onesto, mai date certe da campioni scarsi. |
| [CAP-0026](../../REGISTRO_CAPABILITY/CAP-0026.md) | Sound feedback semantico opzionale | 78 | 80% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0026/README.md) | Controllare silent mode e opzioni accessibilita |
| [CAP-0007](../../REGISTRO_CAPABILITY/CAP-0007.md) | Scheda workout e storico multisport | 77 | 80% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0007/README.md) | Non creare doppio diario allenamenti |
| [CAP-0157](../../REGISTRO_CAPABILITY/CAP-0157.md) | Gesti volontari locali tramite Dynamic Time Warping | 72 | 65% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0157/README.md) | Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita. |
| [CAP-0154](../../REGISTRO_CAPABILITY/CAP-0154.md) | Routine predittive con Markov solo opt-in | 71 | 68% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0154/README.md) | Opt-in, minimal retention, cancellazione, min-sample, divieto inferenze sensibili e zero notifiche automatiche. |
| [CAP-0139](../../REGISTRO_CAPABILITY/CAP-0139.md) | Studio del movimento da video con pose annotate | 63 | 45% | PROPOSTA | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0139/README.md) | AIMoCap demo esiste; accuratezza tecnica e scientifica, privacy dei soggetti e permessi video da testare; non diagnosi medica. Verificare architettura e licensing nel Product Bible prima di integrare. |

**Totale associazioni app:** 13. Nessuna modifica alla roadmap o al codice dell'app.
