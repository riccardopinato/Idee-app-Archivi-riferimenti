# TasteAI — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

**Viste operative per questa app:** [Da valutare](TasteAI/DA_VALUTARE.md) · [Già integrati](TasteAI/GIA_INTEGRATI.md) · [Da verificare](TasteAI/DA_VERIFICARE.md) · [Tabella CSV](TasteAI/TABELLA.csv). Lo storico seguente conserva tutte le associazioni ma non è la coda di nuove implementazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0044](../REGISTRO_CAPABILITY/CAP-0044.md) | Ricette anti-spreco da ingredienti | P1 | 95 | 95% | Suggerire ricette fattibili usando ingredienti disponibili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0044/README.md) | SOURCE_REPORTED | Non clonare TasteAI; validare differenziazione |
| [CAP-0155](../REGISTRO_CAPABILITY/CAP-0155.md) | Associazioni ingredienti e ricette offline con Apriori | P2 | 89 | 84% | Frequent itemset e regole con supporto/confidenza, mai dedurre allergeni o causalità | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0155/README.md) | PROPOSTA | Corpus minimo, support/confidence/lift, ingredienti canonici, lingua, allergeni, nessuna aggiunta automatica a spesa. |
| [CAP-0072](../REGISTRO_CAPABILITY/CAP-0072.md) | Entitlement RevenueCat provider truth | P2 | 88 | 60% | Servizio entitlement con stato verificato e fallback | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0072/README.md) | SOURCE_REPORTED | IAP compliance e no premium unlocked falsely |
| [CAP-0041](../REGISTRO_CAPABILITY/CAP-0041.md) | Palette da foto e golden hour | P2 | 86 | 78% | Estrarre palette e pianificare sessioni fotografiche | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0041/README.md) | PROPOSTA | SunCalc locale e colori originali con file donor verificato |
| [CAP-0006](../REGISTRO_CAPABILITY/CAP-0006.md) | Lista della spesa privata e condivisa | P2 | 83 | 95% | Quantità categorie e condivisione selettiva tra membri | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0006/README.md) | PROPOSTA | Verificare test v0.71 e riuso senza database condiviso |
| [CAP-0045](../REGISTRO_CAPABILITY/CAP-0045.md) | Meal plan e spesa derivata | P2 | 82 | 80% | Pianificazione pasti collegata a ingredienti e lista spesa | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0045/README.md) | PROPOSTA | Lista derivata con consenso e separazione proprieta dati |
| [CAP-0032](../REGISTRO_CAPABILITY/CAP-0032.md) | Indicizzazione ricerca semantica locale | P2 | 79 | 52% | Ricerca per significato on device solo se migliora FTS | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0032/README.md) | PROPOSTA | Modello multilingue licenza footprint e benchmark; non inserire pack base |
| [CAP-0046](../REGISTRO_CAPABILITY/CAP-0046.md) | Ingredienti da foto e confezioni | P3 | 78 | 80% | Scansione lista o confezione per scegliere ricetta | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0046/README.md) | PROPOSTA | OCR poi conferma attributi e nessuna promessa nutrizionale |
| [CAP-0033](../REGISTRO_CAPABILITY/CAP-0033.md) | Modello Needle 3 on demand Plus | P3 | 76 | 60% | Pacchetto AI opzionale con fallback e non requisito del core | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0033/README.md) | ROADMAP_STORICA | Play delivery benchmark e entitlement non auto concesso |

**Totale associazioni:** 9. Non modificare automaticamente la roadmap del prodotto.
