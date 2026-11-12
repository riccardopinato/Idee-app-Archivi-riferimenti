# X10-035 — Decisione prodotti e budget: proposta pronta, approvazione assente

Factory baseline: Core@c5adc147046beb7024629466d10eeb799c3c2619 (Master v27, Golden Index v29).

**Precondizioni soddisfatte:** X10-002 shortlist, X10-034 competitor audit, basati sulle evidenze già presenti in archivio. Nessun dato Play privato o misura di willingness-to-pay è stato usato come fatto.

## Decisione da registrare (HUMAN_GATE)

- **Battery Guard**: primo esperimento di prodotto, soggetto a OEM/device QA e token purchase/refund lifecycle
- **Rotate 180°**: secondo esperimento di confronto con upfront price, soggetto a verifica compatibilità/sistema
- **World Days**: candidato condizionale, non confermato per advertising; contenuti verificati e costo editoriale prima del via libera

Il file [X10-035 decision proposal](X10-035_OWNER_DECISION_PROPOSAL.json) codifica esattamente `owner_approved: false` e `approved_budget_eur: null`. Nessun budget è impegnato, nessun prezzo lanciato e nessun prodotto è dichiarato approvato. Per avanzare il gate X10-035 occorre una conferma esplicita del proprietario che indichi 2–3 prodotti, budget totale e go/no-go di ciascuno, seguita da PR di registrazione e controlli.

## X10-036 — Dipendenza non aggirabile

Il [kit privacy_metrics](flutter_kits/privacy_metrics/README.md) è solo un componente educativo/testabile per contatori aggregate in memoria senza rete o storage, non un sistema analytics di prodotto. Non misura retention unica o attribuzione; non viene integrato nelle app prima di approvazione prodotto, disclosure, consent e policy di conservazione.
