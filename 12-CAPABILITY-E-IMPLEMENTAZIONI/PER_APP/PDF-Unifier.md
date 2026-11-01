# PDF-Unifier — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0037](../REGISTRO_CAPABILITY/CAP-0037.md) | Operazioni PDF split merge rotate lock | P1 | 98 | SOURCE_REPORTED | Verificare motore originale licenza e compatibilita Flutter |
| [CAP-0134](../REGISTRO_CAPABILITY/CAP-0134.md) | Triage e categorizzazione documenti importati | P1 | 98 | PROPOSTA | DocRex Apache-2.0, ~5,8 MB FP32, solo bank_statement/invoice/other, int8 1,7 MB non raccomandato; serve test su documenti italiani. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0035](../REGISTRO_CAPABILITY/CAP-0035.md) | OCR immagini e documenti on device | P1 | 92 | SOURCE_REPORTED | Audit licenza ML Kit e processi media originali |
| [CAP-0114](../REGISTRO_CAPABILITY/CAP-0114.md) | Redazione PII e privacy copy di note e PDF | P2 | 85 | PROPOSTA | Non certifica copertura IBAN/credenziali o privacy su tutte le lingue; regex locali e NER opzionale, redaction irreversibile sul file esportato. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0118](../REGISTRO_CAPABILITY/CAP-0118.md) | Confronto versioni documento e differenze verificabili | P2 | 85 | PROPOSTA | Il thread spiega diff testuale/semantico, non fornisce un'app donor: pattern di riferimento; attenzione a OCR e riconciliazione pagine. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0133](../REGISTRO_CAPABILITY/CAP-0133.md) | Ordine di lettura strutturato dei documenti | P2 | 83 | PROPOSTA | La doc descrive PP-DocLayoutV3; integrarlo e inferenza/progetto distinto dall'OCR. Controllare supporto linguistico e runtime mobile. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0128](../REGISTRO_CAPABILITY/CAP-0128.md) | Estrazione campi da form in schede canoniche | P2 | 81 | PROPOSTA | FUNSD+ contiene annotazioni form con licenza custom; reference per layout, vietato incorporare dataset senza gate diritti. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0122](../REGISTRO_CAPABILITY/CAP-0122.md) | Estrazione di tabelle strutturate da immagini e PDF | P2 | 79 | PROPOSTA | Paper2Any include extraction di tabelle in PPT, non un modulo Flutter pronto; integrare con CAP-0035 OCR locale e validazione cellule. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0008](../REGISTRO_CAPABILITY/CAP-0008.md) | Import foto PDF delle schede workout | P3 | 75 | DONOR_REPORTED | Verificare parser e conservazione file originale |
| [CAP-0030](../REGISTRO_CAPABILITY/CAP-0030.md) | Professional Wallet CV attestati QR vCard | P3 | 75 | PROPOSTA | Integrare Document Workspace senza wallet parallelo |
| [CAP-0038](../REGISTRO_CAPABILITY/CAP-0038.md) | PDF Pocket Tools packaging standalone | P3 | 75 | DONOR_REPORTED | Non creare secondo motore per packaging |
| [CAP-0125](../REGISTRO_CAPABILITY/CAP-0125.md) | Ricostruzione valori numerici da grafici fotografati | P3 | 72 | PROPOSTA | Dataset sintetico di grafici lineari semplici: non dimostra accuratezza su grafici reali complessi; non sostituire dati originali. Verificare architettura e licensing nel Product Bible prima di integrare. |

**Totale associazioni:** 12. Non modificare automaticamente la roadmap del prodotto.
