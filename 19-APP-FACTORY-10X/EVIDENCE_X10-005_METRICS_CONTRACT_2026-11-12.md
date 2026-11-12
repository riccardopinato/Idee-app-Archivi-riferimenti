# X10-005 — North Star e ledger KPI verificabili

**Data:** 12/11/2026 · **Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`.
**Stato reale:** contratto KPI e validatore disponibili; **nessuna baseline attiva misurata**, nessuna crescita 10x dimostrata.

## North Star
`verified_features_per_week` è la misura primaria proposta: conta solo feature di prodotto consegnate con prova al commit esatto, acceptance e gate QA. PR documentali, audit e test di solo workflow **non** sono feature rilasciate.

Altri indicatori fondamentali:
- `lead_time_hours`: dal requisito operativo alla feature verificata, separando tempo attivo misurato da attese CI/umane; il `PR opened → merged` del ledger v27 è un **proxy**, non ore lavorate.
- `manual_interventions_per_feature`: passaggi/approvazioni/copia-incolla per consegna; misura la riduzione della dipendenza da interventi umani.
- `reuse_ratio`: quote di componenti realmente integrate e provate nel consumer, non semplice presenza di donor o Golden.
- `qa_regressions_escaped`: regressioni confermate dopo release, attribuibili a commit/artifact esatto.
- `pilot_retention_d30`: utenti acquisiti e retained a D30 secondo cohort e consenso; nessun dato personale nell'archivio.
- `net_revenue_per_product`: margine dopo fee aggregato; prove fiscali/provider sono **private**, non si pubblicano.
- `agent_job_success_recovery`: tentativi agent con recovery dimostrata su run reali, non simulazioni o check CI.

## Fonte e meccanismo
- [Ledger 10x](data/METRICS_LEDGER_v1.json): 8 definizioni, unità, acceptance gate, stato `NOT_MEASURED`, nessuna osservazione numerica fittizia.
- [Validatore](../scripts/factory_10x_metrics.py): richiede ricevute GitHub con SHA/UTC/cohort/period/gate review per le osservazioni pubbliche; rifiuta ratio sopra 1, duplicazioni e metriche non provate.
- [Test negativi](../tests/factory_10x_metrics_test.py): nessuna baseline inventata, niente `VERIFIED` senza prova, niente dati revenue raw nel pubblico.
- [Ledger v27 canonico](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/evidence/v27-observability/DELIVERY_LEDGER.json): già misura il proxy temporale del ciclo PR; la sua fonte rimane autorevole, non viene copiata in questo JSON.

## Gate prima di parlare di 10x
1. Raccogliere una baseline comparabile, con perimetro di feature simile, senza attribuire tempo di attesa a lavoro umano o AI.
2. Differenziare `SOURCE_CONFIRMED`, `CI_VERIFIED`, `DEVICE_VERIFIED`, `RELEASE`. Non equiparare successo runner all'utilità utente.
3. Osservare minimo due prodotti pilota e fasi di acquisizione/retention misurabili per i KPI business.
4. Report di output significativo in rapporto al costo operativo (runner, token, euro, tempo umano) senza inferenze causali non sostenute.

**Acceptance X10-005:** definizioni, file, validator e suite CI completati; **MISURAZIONE = NOT_MEASURED** per tutte le otto metriche finché non esistano ricevute indipendenti. Il task riguarda l'installazione della strumentazione, non il raggiungimento del target.
