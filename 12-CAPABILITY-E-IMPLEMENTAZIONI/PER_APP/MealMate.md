# MealMate — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

**Viste operative per questa app:** [Da valutare](MealMate/DA_VALUTARE.md) · [Già integrati](MealMate/GIA_INTEGRATI.md) · [Da verificare](MealMate/DA_VERIFICARE.md) · [Tabella CSV](MealMate/TABELLA.csv). Lo storico seguente conserva tutte le associazioni ma non è la coda di nuove implementazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0044](../REGISTRO_CAPABILITY/CAP-0044.md) | Ricette anti-spreco da ingredienti | P1 | 95 | 91% | Suggerire ricette fattibili usando ingredienti disponibili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0044/README.md) | PROPOSTA | Non clonare TasteAI; validare differenziazione |
| [CAP-0155](../REGISTRO_CAPABILITY/CAP-0155.md) | Associazioni ingredienti e ricette offline con Apriori | P2 | 89 | 77% | Frequent itemset e regole con supporto/confidenza, mai dedurre allergeni o causalità | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0155/README.md) | PROPOSTA | Corpus minimo, support/confidence/lift, ingredienti canonici, lingua, allergeni, nessuna aggiunta automatica a spesa. |
| [CAP-0045](../REGISTRO_CAPABILITY/CAP-0045.md) | Meal plan e spesa derivata | P2 | 82 | 76% | Pianificazione pasti collegata a ingredienti e lista spesa | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0045/README.md) | PROPOSTA | Lista derivata con consenso e separazione proprieta dati |

**Totale associazioni:** 3. Non modificare automaticamente la roadmap del prodotto.
