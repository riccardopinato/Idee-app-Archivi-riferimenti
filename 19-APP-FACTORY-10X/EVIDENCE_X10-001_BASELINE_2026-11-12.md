# X10-001 — Baseline multi-repo e gap analysis (coorte iniziale 10x)

**Data audit:** 12/11/2026 · **Stato:** `READ_ONLY / SOURCE_AUDITED`. Non è una certificazione runtime dei prodotti.
**Factory baseline canonica:** [App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619](https://github.com/riccardopinato/App-Factory-Core/commit/c5adc147046beb7024629466d10eeb799c3c2619) (Master v27, Golden Index v29).
**Autorità:** la Product Bible locale governa il prodotto; AGENTS e roadmaps decidono il processo; codice+test effettivi prevalgono sullo storico chat.

## Commit HEAD osservati e documentazione di ingresso
`Presente` indica che il file è apparso nell'inventario del default branch; `non visto in root` non significa che non esistano documenti analoghi in altre cartelle.

| Repository | SHA osservato | Entry-point visibili nel root | Delta operativo |
|---|---|---|---|
| [AppLab](https://github.com/riccardopinato/AppLab/commit/2d57d9cea85ac03016b24e103046e47b6f02acb5) | `2d57d9cea85a` | AGENTS, ROADMAP, scripts/, integration/, tests/ | Esiste già closed-loop v6; verificare integration e prove `SELF_CANARY`, non riscrivere un worker equivalente |
| [Agent Core](https://github.com/riccardopinato/App-Factory-Agent-Core/commit/78dc19318b5905fd83b52b8840e082c5fec51b45) | `78dc19318b59` | AGENTS, PRODUCT_BIBLE, ROADMAP, docs/, scripts/, tests/ | Codice Windows originale non importato; la helper metadata non è un coding agent |
| [Archivio Idee](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/commit/9212bf3cd4eea51639a8ab6bdbf312719db1a075) | `9212bf3cd4ee` | AGENTS, 19-APP-FACTORY-10X, 18-AGENT-FACTORY, scripts/, tests/ | Source della coda e dei dati osservati, non delle applicazioni o del Golden Core |
| [Anna's Diary](https://github.com/riccardopinato/Agenda-per-Anna/commit/8fbfe14f7a21d41af274cf259c462df2eab9dc69) | `8fbfe14f7a21` | AGENTS, APP_FACTORY_ADOPTION, `lib/`, `test/`, `integration_test/` | Candidato Flutter consumer, ma decisioni UI/OAuth e QA fisico restano prodotto-local |
| [Notes](https://github.com/riccardopinato/Notes-Ecosistema/commit/22892b336e4587dc2daa1e8df970b873e72e41d7) | `22892b336e45` | ROADMAP, docs/, flutter_app/ | Candidato per riuso canvas e DS; verificare Product Bible e fonte app effettiva prima di upgrade |
| [World Days](https://github.com/riccardopinato/World-Days/commit/988aef2c89ab7503253950c06ccc8deadb22d367) | `988aef2c89ab` | AGENTS, ROADMAP, docs/, lib/, test/, integration_test/ | Forte consumer Flutter, ma download APK/editorial coverage/store QA da verificare |
| [TrailPath](https://github.com/riccardopinato/TrailPath/commit/74a5cf87d0be55900d9be318af53972643eebd32) | `74a5cf87d0be` | docs/, lib/, test/ | Consumer nativo/Flutter solo se Product Bible e routing gates compatibili |
| [Battery Guard](https://github.com/riccardopinato/Battery_Guard/commit/1343f09d21ace8adf3976b3fd347183f38e5ab68) | `1343f09d21ac` | PRODUCT_BIBLE, ROADMAP, docs/, lib/, test/ | Possibile utility Flutter per kit/release; signing e APK reale restano non attestati qui |

**Lettura allineamento:** non viene dedotto uno stato `CI_VERIFIED` o `DEVICE_VERIFIED` dal solo HEAD. HEAD è evidenza di versionamento, non conformità al prodotto. Il root è stato ispezionato per ciascun repository e i file di policy canonica sono stati letti per AppLab e Agent Core.

## Gap strategici a massima priorità
1. **Integration gap:** [AppLab v6](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/integration/roadmap/APPLAB_V6_CLOSED_LOOP_AGENTIC_ENGINEERING.md) ha già queue/investigation/worker/PR, mentre Agent Core contiene helper di contesto, non il runner Windows né adapter. Decisione: creare un boundary adapter, non un nuovo motore orchestration.
2. **Runtime evidence gap:** AppLab v6.2 dichiara 0/3 prove reali di repair per rollout oltre `SELF_CANARY`; l'integrazione deve mantenere il gate [operational proof](https://github.com/riccardopinato/AppLab/blob/2d57d9cea85ac03016b24e103046e47b6f02acb5/integration/roadmap/APPLAB_V62_OPERATIONAL_PROOF.md).
3. **Product shortlist gap:** la Factory ha molti repository ma nessuna selezione commerciale 2–3 prodotti dimostrata da domanda, retention o ricavi nella presente verifica; task `X10-002` non completato.
4. **Reusable Flutter kit gap:** Golden disponibili e documentati, ma l'applicabilità richiede test per consumer e packaging/compatibilità; `X10-003` e `X10-017` restano separati.
5. **Distribution gap:** non assumere che un CI green sia APK firmato/installato o Play. AppLab QA e validazione fisica separati.
6. **Autonomy gap:** un cron GitHub read-only o un task Chat pianificato non sono un agente continuamente attivo; il runner locale va importato/collaudato prima.

## Decisione operativa
- Sbloccare in parallelo `X10-004` (audit del motore AppLab), `X10-002` (selezione candidati commerciali) e `X10-003` (Golden/Donor inventory) in scope separato.
- Non scegliere subito Anna/Notes/World Days per il business: sono solo *candidati tecnici*; shortlist e market diligence richiedono prove e decisione del prodotto.
- Questo documento è l'artefatto di accettazione `X10-001`, **scoped static/read-only**. Nessuna modifica al codice prodotto.
