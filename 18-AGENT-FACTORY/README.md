# Agent Factory — hub di riuso e repository
Data 2026-11-11. Baseline Core ee72dbb1b0de2cd71bc4aac42c350853c6915159.
Questa cartella è un hub di registrazione e scaffold DOCUMENTALE, non un repository eseguibile.
Dossier: [Agent Factory / Finance / Deskland](../11-NUOVE-IDEE/AGENT_FACTORY_FINANCE_DESKLAND_2026-11-11.md).

## Destinazioni e stato attuale
| ID | Repo destinazione proposto | Stato |
|---|---|---|
| AGF-2026-001 | riccardopinato/App-Factory-Agent-Core | DA CREARE; codice locale agente Windows ancora da acquisire |
| FIN-2026-001 | riccardopinato/Finance-Intelligence-Agent | DA CREARE; MVP azionario read-only |
| INT-2026-001 | riccardopinato/Interactive-Scene-Core | DA CREARE solo quando extraction seam dimostrato |
| DESK-EXISTING | riccardopinato/Adaptive-Landscape-Android | ESISTE; code owner del prodotto Android |
| REF-CRYPTO | riccardopinato/btrader | ESISTE; arbitraggio crypto, diverso prodotto |

## Source of truth
- Policies: riccardopinato/App-Factory-Core/CURRENT.yaml (Master 27, Golden Index 29 al 11/11).
- AGENTS.md locale per ciascun nuovo repo; Product Bible per ciascun prodotto; ROADMAP e IMPLEMENTATION_LOG; CODE_PROVENANCE con SHA/licenze; TEST_EVIDENCE con tool/date/result; CHANGELOG; decision records.
- Mai creare una copia del Master o dei Golden in questi repo; solo link/pin commit.
- Originale Deskland BLEZZ0102/Deskland GPL-3.0: prodotto/UX reference; non importare code/assets direttamente in Adaptive Landscape commerciale.

## Convezioni di stato per aggiornamenti
IDEA -> IN_ROADMAP -> IN_CODICE -> CI_VERIFIED -> DEVICE_VERIFIED -> RELEASE; status e freshness distinti.
AGF: schemi job, adapter strumenti e gating indipendenti.
FIN: dati/licenze, timestamp, paper-only e divieto trading reale come default.
INT: interoperabilità Flutter/Kotlin, permessi Android, FPS/batteria e doppio consumer prima di Golden.
Ogni modifica: task/issue -> branch -> commit -> PR -> exact-head tests -> merge condizionale -> changelog e aggiornamento link qui. Nessuna esecuzione in background implicita.

## Bootstrap minimo per nuovi repo
1. Crea repository separato con visibilità valutata (per Agent e Finance preferibilmente privato).
2. Introduci README.md, AGENTS.md, PRODUCT_BIBLE.md, ROADMAP.md, CHANGELOG.md, docs/ARCHITECTURE.md, docs/SECURITY.md, docs/PROVENANCE.md, evidence/README.md.
3. Per AGF migra il codice esistente solo dal path locale verificato, con commit e licenza; nessun codice fittizio.
4. Per FIN importa solo modelli dati anonimi/sintetici, nessuna chiave né posizioni personali.
5. Per INT estrai dal repo Adaptive Landscape soltanto dopo benchmark, review licenze e test di consumer.
6. Collegamento reciproco con il presente hub e con il dossier principale. Non sovrascrivere repository preesistenti.
