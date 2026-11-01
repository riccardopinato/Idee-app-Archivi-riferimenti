# app-fotografia — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0039](../REGISTRO_CAPABILITY/CAP-0039.md) | EXIF privacy safe copy | P1 | 98 | PROPOSTA | Niente modifica di originali e UI attributi rimossi |
| [CAP-0022](../REGISTRO_CAPABILITY/CAP-0022.md) | Localizzazione cinque o piu lingue | P1 | 94 | SOURCE_REPORTED | Controllare parita lingua in native notifications |
| [CAP-0042](../REGISTRO_CAPABILITY/CAP-0042.md) | Catalogo editoriale multilingua offline | P1 | 94 | SOURCE_REPORTED | Riusare pattern non mescolare dati editoriali di prodotti differenti |
| [CAP-0053](../REGISTRO_CAPABILITY/CAP-0053.md) | Sun Moon calcolo locale | P1 | 93 | PROPOSTA | Calcolo locale SunCalc con timezone corretto |
| [CAP-0025](../REGISTRO_CAPABILITY/CAP-0025.md) | Schermate responsive rail e split view | P2 | 89 | SOURCE_REPORTED | No claim desktop full prima di QA multi-width |
| [CAP-0040](../REGISTRO_CAPABILITY/CAP-0040.md) | Deduplicazione foto per hash percettivo | P2 | 87 | PROPOSTA | Verificare algoritmo reale e precisione duplicati quasi identici |
| [CAP-0089](../REGISTRO_CAPABILITY/CAP-0089.md) | Registro locale esperimenti con ipotesi e risultato | P2 | 87 | PROPOSTA | Riutilizzare evidence/versioning AppLab e Git; nuovi record solo per ipotesi, misura, input baseline, output e decisione, senza seconda authority CI o agent runtime. |
| [CAP-0041](../REGISTRO_CAPABILITY/CAP-0041.md) | Palette da foto e golden hour | P2 | 86 | ROADMAP_STORICA | SunCalc locale e colori originali con file donor verificato |
| [CAP-0043](../REGISTRO_CAPABILITY/CAP-0043.md) | Raccolta fonti contenuti e audit artwork | P2 | 85 | SOURCE_REPORTED | Rispettare copyright e revisioni umane obbligatorie |
| [CAP-0052](../REGISTRO_CAPABILITY/CAP-0052.md) | Meteo contestuale finestre outdoor | P2 | 85 | PROPOSTA | API gratuita meteo non commerciale non usare con Ads |
| [CAP-0130](../REGISTRO_CAPABILITY/CAP-0130.md) | Generazione di slide e figure tecniche modificabili | P2 | 81 | PROPOSTA | Paper2Any dichiara Paper2PPT e licenza Apache-2.0, ma la demo pubblica era in errore; il backend/AI non va importato automaticamente. / Paper2Any dichiara Paper2Figure e Paper2PPT nella stessa codebase; registrata come modalita dello stesso CAP di Notes-to-Slides. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0082](../REGISTRO_CAPABILITY/CAP-0082.md) | Deterministic UI design artwork | P2 | 79 | PROPOSTA | Non generare asset coperti da diritti |
| [CAP-0091](../REGISTRO_CAPABILITY/CAP-0091.md) | Snapshot condivisibile della vista mappa senza dati privati | P3 | 78 | PROPOSTA | Distinguere view state (camera, zoom, layers) da percorso/ricordi privati; share URL/file su azione volontaria, nessuna chiave API, token o posizione personale inclusa. |
| [CAP-0136](../REGISTRO_CAPABILITY/CAP-0136.md) | Scontorno foto in elementi canvas riutilizzabili | P3 | 76 | PROPOSTA | Segment Anything WebGPU demo esiste; runtime Android/offline, peso del modello e licenza degli asset da verificare. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0140](../REGISTRO_CAPABILITY/CAP-0140.md) | Analisi forense non conclusiva delle immagini | P3 | 63 | PROPOSTA | DetectiveSAM ha licenza dichiarata other; non importare/copiare senza chiarimento. Le evidenze di manipolazione non certificano originalita o intenzione. Verificare architettura e licensing nel Product Bible prima di integrare. |

**Totale associazioni:** 15. Non modificare automaticamente la roadmap del prodotto.
