# AppLab — Stato da verificare (4)

Derivato dal registro canonico per la **singola app**. Riuso parziale, sorgente dichiarata oppure perimetro incerto. Non proporre il lavoro da zero: prima confrontare il delta funzionale.

[Da valutare](DA_VALUTARE.md) · [Già integrati](GIA_INTEGRATI.md) · [Da verificare](DA_VERIFICARE.md) · [CSV ordinabile in Excel](TABELLA.csv) · [Scheda storica](../AppLab.md)

| CAP ID | Capability | Priorità | Facilità | Stato per app | Fonte / prova | Prossimo controllo |
| --- | --- | --- | --- | --- | --- | --- |
| [CAP-0067](../../REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | 94 | 80% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0067/README.md) | Artifact build non e device certification |
| [CAP-0068](../../REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | 90 | 65% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0068/README.md) | Mai inferire device PASS da CI |
| [CAP-0069](../../REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | 81 | 65% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0069/README.md) | Anna: acquisire e approvare 70 coppie screenshot e verificare il comparatore su baseline reali; CI del tool non equivale a visual/device PASS. |
| [CAP-0070](../../REGISTRO_CAPABILITY/CAP-0070.md) | AppLab autonomous bounded repair | 70 | 45% | SOURCE_REPORTED | [Kit tecnico](../../../13-KIT-INTEGRAZIONE/CAP-0070/README.md) | Politica fail closed P0/P1 e review |

**Totale associazioni app:** 6. Nessuna modifica alla roadmap o al codice dell'app.
