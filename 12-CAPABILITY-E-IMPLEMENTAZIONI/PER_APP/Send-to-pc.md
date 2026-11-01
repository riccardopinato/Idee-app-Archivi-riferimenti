# Send-to-pc — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0039](../REGISTRO_CAPABILITY/CAP-0039.md) | EXIF privacy safe copy | P1 | 98 | 90% | Esportazione copia foto senza GPS e dati sensibili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0039/README.md) | PROPOSTA | Niente modifica di originali e UI attributi rimossi |
| [CAP-0083](../REGISTRO_CAPABILITY/CAP-0083.md) | Treemap interattiva dello spazio e selezione sicura | P2 | 87 | 80% | Usare visualizzazione a rettangoli proporzionali per mostrare cosa occupa lo storage senza cancellazioni implicite. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0083/README.md) | PROPOSTA | Scansione progressiva read-only, treemap per dimensione, selezione esplicita, conferma eliminazione o esportazione e rollback ove disponibile. Non replicare accesso MFT/NTFS nel sandbox Android. |
| [CAP-0066](../REGISTRO_CAPABILITY/CAP-0066.md) | Trasferimento LAN QR HTTPS fidato | P2 | 83 | 60% | Condivisione file locale senza cloud obbligatorio | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0066/README.md) | SOURCE_REPORTED | Pairing fingerprint HTTPS e test rete locale |

**Totale associazioni:** 3. Non modificare automaticamente la roadmap del prodotto.
