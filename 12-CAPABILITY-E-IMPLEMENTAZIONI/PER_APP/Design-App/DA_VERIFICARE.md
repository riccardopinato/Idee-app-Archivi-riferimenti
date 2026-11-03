# Design-App — Stato da verificare (5)

Derivato dal registro canonico per la **singola app**. Riuso parziale, sorgente dichiarata oppure perimetro incerto. Non proporre il lavoro da zero: prima confrontare il delta funzionale.

[Da valutare](DA_VALUTARE.md) · [Già integrati](GIA_INTEGRATI.md) · [Da verificare](DA_VERIFICARE.md) · [CSV ordinabile in Excel](TABELLA.csv) · [Scheda storica](../Design-App.md)

| CAP ID | Capability | Priorità | Facilità | Stato per app | Fonte / prova | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| [CAP-0023](../../REGISTRO_CAPABILITY/CAP-0023.md) | Design System Flutter token-first | 89 | 80% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0023/README.md) | Riuso pattern non diventa Golden automaticamente |
| [CAP-0025](../../REGISTRO_CAPABILITY/CAP-0025.md) | Schermate responsive rail e split view | 89 | 80% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0025/README.md) | No claim desktop full prima di QA multi-width |
| [CAP-0024](../../REGISTRO_CAPABILITY/CAP-0024.md) | Motion reduced-motion e microinterazioni | 87 | 80% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0024/README.md) | Verifica accessibilita e prestazioni su device |
| [CAP-0069](../../REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | 81 | 65% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0069/README.md) | Anna: acquisire e approvare 70 coppie screenshot e verificare il comparatore su baseline reali; CI del tool non equivale a visual/device PASS. |
| [CAP-0026](../../REGISTRO_CAPABILITY/CAP-0026.md) | Sound feedback semantico opzionale | 78 | 80% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0026/README.md) | Controllare silent mode e opzioni accessibilita |

**Totale associazioni app:** 5. Nessuna modifica alla roadmap o al codice dell'app.
