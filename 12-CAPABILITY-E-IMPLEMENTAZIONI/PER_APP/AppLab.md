# AppLab — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0067](../REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | P1 | 94 | SOURCE_REPORTED | Artifact build non e device certification |
| [CAP-0090](../REGISTRO_CAPABILITY/CAP-0090.md) | Controllo scope creep e dipendenze nelle PR | P1 | 92 | PROPOSTA | Verificare se AppLab copre gia la stessa responsabilita: solo gate advisory a diff bounded confrontato con PR scope, niente agente ulteriore o trigger duplicati. Controllare licenza di ogni skill e le sue dipendenze. |
| [CAP-0068](../REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | P2 | 90 | SOURCE_REPORTED | Mai inferire device PASS da CI |
| [CAP-0089](../REGISTRO_CAPABILITY/CAP-0089.md) | Registro locale esperimenti con ipotesi e risultato | P2 | 87 | PROPOSTA | Riutilizzare evidence/versioning AppLab e Git; nuovi record solo per ipotesi, misura, input baseline, output e decisione, senza seconda authority CI o agent runtime. |
| [CAP-0069](../REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | P2 | 81 | SOURCE_REPORTED | Baseline screen e variant certi |
| [CAP-0070](../REGISTRO_CAPABILITY/CAP-0070.md) | AppLab autonomous bounded repair | P3 | 70 | SOURCE_REPORTED | Politica fail closed P0/P1 e review |

**Totale associazioni:** 6. Non modificare automaticamente la roadmap del prodotto.
