# Idee-app-Archivi-riferimenti — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0090](../REGISTRO_CAPABILITY/CAP-0090.md) | Controllo scope creep e dipendenze nelle PR | P1 | 92 | 80% | Segnalare file e comportamenti fuori dallo scope autorizzato prima del merge. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0090/README.md) | PROPOSTA | Verificare se AppLab copre gia la stessa responsabilita: solo gate advisory a diff bounded confrontato con PR scope, niente agente ulteriore o trigger duplicati. Controllare licenza di ogni skill e le sue dipendenze. |
| [CAP-0089](../REGISTRO_CAPABILITY/CAP-0089.md) | Registro locale esperimenti con ipotesi e risultato | P2 | 87 | 80% | Tracciare prove e tentativi per decidere se una nuova capability migliora un prodotto. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0089/README.md) | PROPOSTA | Riutilizzare evidence/versioning AppLab e Git; nuovi record solo per ipotesi, misura, input baseline, output e decisione, senza seconda authority CI o agent runtime. |

**Totale associazioni:** 2. Non modificare automaticamente la roadmap del prodotto.
