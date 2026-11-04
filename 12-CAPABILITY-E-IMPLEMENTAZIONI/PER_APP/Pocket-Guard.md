# Pocket-Guard — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

**Viste operative per questa app:** [Da valutare](Pocket-Guard/DA_VALUTARE.md) · [Già integrati](Pocket-Guard/GIA_INTEGRATI.md) · [Da verificare](Pocket-Guard/DA_VERIFICARE.md) · [Tabella CSV](Pocket-Guard/TABELLA.csv). Lo storico seguente conserva tutte le associazioni ma non è la coda di nuove implementazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0158](../REGISTRO_CAPABILITY/CAP-0158.md) | Soglie adattive con isteresi per luce e prossimità | P1 | 96 | 93% | EWMA e debounce per segnali rumorosi, impossibile inferire contesto da un solo campione | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0158/README.md) | SOURCE_REPORTED | Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM. |
| [CAP-0057](../REGISTRO_CAPABILITY/CAP-0057.md) | Allarme protezione Table Pocket Bag Journey | P2 | 83 | 61% | Motore arm escalation comune con diversi sensori | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0057/README.md) | SOURCE_REPORTED | Test multi OEM FGS false-positive e batteria |
| [CAP-0081](../REGISTRO_CAPABILITY/CAP-0081.md) | Phone protection sensitivity adviser | P3 | 73 | 75% | Calibrazione sensori e diagnostics configurabili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0081/README.md) | PROPOSTA | False-positive risk e test sensori reali |
| [CAP-0157](../REGISTRO_CAPABILITY/CAP-0157.md) | Gesti volontari locali tramite Dynamic Time Warping | P3 | 72 | 72% | Distanza DTW con template scelto dall'utente; cap sensori/FGS obbligatorio | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0157/README.md) | PROPOSTA | Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita. |

**Totale associazioni:** 4. Non modificare automaticamente la roadmap del prodotto.
