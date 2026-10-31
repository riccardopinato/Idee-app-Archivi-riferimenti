# CamperBoss — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0017](../REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | P1 | 94 | PROPOSTA | Regression entita-per-entita e file orfani; niente duplicazione lifecycle |
| [CAP-0053](../REGISTRO_CAPABILITY/CAP-0053.md) | Sun Moon calcolo locale | P1 | 93 | PROPOSTA | Calcolo locale SunCalc con timezone corretto |
| [CAP-0018](../REGISTRO_CAPABILITY/CAP-0018.md) | Backup restore con staging e rollback | P2 | 90 | SOURCE_REPORTED | Audit formati e test corrupt archive per consumer |
| [CAP-0068](../REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | P2 | 90 | SOURCE_REPORTED | Mai inferire device PASS da CI |
| [CAP-0071](../REGISTRO_CAPABILITY/CAP-0071.md) | Offline content packs incremental sync | P2 | 90 | SOURCE_REPORTED | Licenze e hashing versioni pack |
| [CAP-0047](../REGISTRO_CAPABILITY/CAP-0047.md) | POI offline versionati e provenienza | P2 | 88 | ROADMAP_STORICA | Licenze ODbL provider e freshness; non scaricare tile pubblici |
| [CAP-0050](../REGISTRO_CAPABILITY/CAP-0050.md) | Riorganizzazione tappe e tempi itinerario | P2 | 85 | PROPOSTA | Tempi da routing verificato e controllo manuale ordine |
| [CAP-0052](../REGISTRO_CAPABILITY/CAP-0052.md) | Meteo contestuale finestre outdoor | P2 | 85 | PROPOSTA | API gratuita meteo non commerciale non usare con Ads |
| [CAP-0060](../REGISTRO_CAPABILITY/CAP-0060.md) | Protezione batteria avvisi e sessioni | P2 | 84 | PROPOSTA | Distingue salute stimata da misure disponibili |
| [CAP-0019](../REGISTRO_CAPABILITY/CAP-0019.md) | Store media content addressed e GC | P2 | 81 | PROPOSTA | Non uniformare database privacy separati |
| [CAP-0048](../REGISTRO_CAPABILITY/CAP-0048.md) | Routing sentieri trace snap affidabile | P2 | 79 | PROPOSTA | Test fisico snap a vari zoom e reti |
| [CAP-0049](../REGISTRO_CAPABILITY/CAP-0049.md) | Offline map engine e routing camper | P2 | 79 | ROADMAP_STORICA | Validare routing camper reale e non dichiarare vera navigazione offline senza mappe |
| [CAP-0087](../REGISTRO_CAPABILITY/CAP-0087.md) | Layer geografici pubblici con freshness e fallback | P2 | 79 | PROPOSTA | Per ogni feed dichiarare API, diritti commerciali, refresh, intervalli, limiti, simulazioni e disponibilita; nessuna navigazione operativa o allerta emergenza da data feed incompleti. Repo metadata NOASSERTION: verify license per file. |
| [CAP-0080](../REGISTRO_CAPABILITY/CAP-0080.md) | Document expiry and asset passport | P3 | 78 | SOURCE_REPORTED | Non includere segreti/identita in archivio condiviso |
| [CAP-0091](../REGISTRO_CAPABILITY/CAP-0091.md) | Snapshot condivisibile della vista mappa senza dati privati | P3 | 78 | PROPOSTA | Distinguere view state (camera, zoom, layers) da percorso/ricordi privati; share URL/file su azione volontaria, nessuna chiave API, token o posizione personale inclusa. |
| [CAP-0054](../REGISTRO_CAPABILITY/CAP-0054.md) | Prezzi carburanti ufficiali | P3 | 76 | PROPOSTA | Dati nazionali diritti timestamp e valuta |

**Totale associazioni:** 16. Non modificare automaticamente la roadmap del prodotto.
