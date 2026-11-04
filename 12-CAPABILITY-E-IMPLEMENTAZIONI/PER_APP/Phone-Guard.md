# Phone-Guard — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

**Viste operative per questa app:** [Da valutare](Phone-Guard/DA_VALUTARE.md) · [Già integrati](Phone-Guard/GIA_INTEGRATI.md) · [Da verificare](Phone-Guard/DA_VERIFICARE.md) · [Tabella CSV](Phone-Guard/TABELLA.csv). Lo storico seguente conserva tutte le associazioni ma non è la coda di nuove implementazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0158](../REGISTRO_CAPABILITY/CAP-0158.md) | Soglie adattive con isteresi per luce e prossimità | P1 | 96 | 86% | EWMA e debounce per segnali rumorosi, impossibile inferire contesto da un solo campione | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0158/README.md) | PROPOSTA | Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM. |
| [CAP-0065](../REGISTRO_CAPABILITY/CAP-0065.md) | Routine wearable e battery optimization audit | P1 | 94 | 80% | Matrice dei limiti foreground service batteria sensori | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0065/README.md) | ROADMAP_STORICA | Test OEM reale multi dispositivo e Doze |
| [CAP-0077](../REGISTRO_CAPABILITY/CAP-0077.md) | Health check permessi nativi per-capability | P1 | 94 | 80% | Diagnosi degli stati di sensori accessi e notifiche | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0077/README.md) | SOURCE_REPORTED | Anna: QA Android reale per revoca permessi, canali, OEM exact alarm, calendario e push; stato AVAILABLE non dimostra consegna. |
| [CAP-0057](../REGISTRO_CAPABILITY/CAP-0057.md) | Allarme protezione Table Pocket Bag Journey | P2 | 83 | 60% | Motore arm escalation comune con diversi sensori | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0057/README.md) | SOURCE_REPORTED | Test multi OEM FGS false-positive e batteria |
| [CAP-0056](../REGISTRO_CAPABILITY/CAP-0056.md) | Notification listener multi-modulo | P3 | 76 | 60% | Undo pausa follow-up e critical rules su listener unico | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0056/README.md) | PROPOSTA | Non accedere a messaggi privati fuori scopo |
| [CAP-0081](../REGISTRO_CAPABILITY/CAP-0081.md) | Phone protection sensitivity adviser | P3 | 73 | 75% | Calibrazione sensori e diagnostics configurabili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0081/README.md) | SOURCE_REPORTED | False-positive risk e test sensori reali |
| [CAP-0157](../REGISTRO_CAPABILITY/CAP-0157.md) | Gesti volontari locali tramite Dynamic Time Warping | P3 | 72 | 61% | Distanza DTW con template scelto dall'utente; cap sensori/FGS obbligatorio | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0157/README.md) | PROPOSTA | Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita. |

**Totale associazioni:** 7. Non modificare automaticamente la roadmap del prodotto.
