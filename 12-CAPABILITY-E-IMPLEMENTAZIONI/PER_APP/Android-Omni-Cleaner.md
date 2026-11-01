# Android-Omni-Cleaner — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0039](../REGISTRO_CAPABILITY/CAP-0039.md) | EXIF privacy safe copy | P1 | 98 | 90% | Esportazione copia foto senza GPS e dati sensibili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0039/README.md) | SOURCE_REPORTED | Niente modifica di originali e UI attributi rimossi |
| [CAP-0040](../REGISTRO_CAPABILITY/CAP-0040.md) | Deduplicazione foto per hash percettivo | P2 | 87 | 80% | Raggruppare file media simili senza cancellazione automatica | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0040/README.md) | SOURCE_REPORTED | Verificare algoritmo reale e precisione duplicati quasi identici |
| [CAP-0083](../REGISTRO_CAPABILITY/CAP-0083.md) | Treemap interattiva dello spazio e selezione sicura | P2 | 87 | 80% | Usare visualizzazione a rettangoli proporzionali per mostrare cosa occupa lo storage senza cancellazioni implicite. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0083/README.md) | PROPOSTA | Scansione progressiva read-only, treemap per dimensione, selezione esplicita, conferma eliminazione o esportazione e rollback ove disponibile. Non replicare accesso MFT/NTFS nel sandbox Android. |

**Totale associazioni:** 3. Non modificare automaticamente la roadmap del prodotto.
