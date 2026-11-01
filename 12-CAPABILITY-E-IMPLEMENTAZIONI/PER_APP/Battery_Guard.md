# Battery_Guard — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0065](../REGISTRO_CAPABILITY/CAP-0065.md) | Routine wearable e battery optimization audit | P1 | 94 | 80% | Matrice dei limiti foreground service batteria sensori | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0065/README.md) | ROADMAP_STORICA | Test OEM reale multi dispositivo e Doze |
| [CAP-0067](../REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | P1 | 94 | 80% | Workflow build firma stabile SHA e manifest | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0067/README.md) | SOURCE_REPORTED | Artifact build non e device certification |
| [CAP-0077](../REGISTRO_CAPABILITY/CAP-0077.md) | Health check permessi nativi per-capability | P1 | 94 | 80% | Diagnosi degli stati di sensori accessi e notifiche | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0077/README.md) | SOURCE_REPORTED | Permesso concesso non prova capability operativa |
| [CAP-0073](../REGISTRO_CAPABILITY/CAP-0073.md) | AdMob UMP consent gating | P1 | 92 | 75% | Monetizzazione con richiesta ads soltanto quando consentita | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0073/README.md) | SOURCE_REPORTED | Test permessi consent e policy store |
| [CAP-0060](../REGISTRO_CAPABILITY/CAP-0060.md) | Protezione batteria avvisi e sessioni | P2 | 84 | 80% | Sessioni ricarica analisi comportamento batteria | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0060/README.md) | SOURCE_REPORTED | Distingue salute stimata da misure disponibili |
| [CAP-0026](../REGISTRO_CAPABILITY/CAP-0026.md) | Sound feedback semantico opzionale | P3 | 78 | 80% | Feedback sonoro minimo e disattivabile | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0026/README.md) | PROPOSTA | Controllare silent mode e opzioni accessibilita |
| [CAP-0061](../REGISTRO_CAPABILITY/CAP-0061.md) | Smart ETA e idle drain batteria | P3 | 77 | 80% | Stima contestuale tempo carica e consumi | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0061/README.md) | SOURCE_REPORTED | Verificare contro scarica reale in standby |

**Totale associazioni:** 7. Non modificare automaticamente la roadmap del prodotto.
