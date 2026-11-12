# X10-044 — Recommendation cockpit delle opportunità di riuso

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. **Prerequisito:** X10-043 merge [PR #122](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/122), che genera proposte consultive vincolate a CAP, producer/consumer SHA e review supervisionata.

## Componente reale

[Script](../scripts/factory_10x_reuse_cockpit.py): `rank(proposals, estimates, inventory, *, factory_sha, observed_on)` ordina fino a 100 proposte `X10_043_SUPERVISED_REUSE_PROPOSAL` verificate **solo strutturalmente** e combinate con stime tecniche esplicite. Richiede identità pinned, review state consistente, campi obbligatori `automatic_merge:false`, `automatic_code_change:false`, `golden_promotion:false`, `independent_consumer_ci_required:true`. Gli input devono provenire da fonti GitHub autenticate e da giudizi espliciti: lo script *non* autentica da solo il provider né verifica le approvazioni.

I fattori di ordinamento, ciascuno 0–5, sono **impatto**, **riuso cross-app**, **forza dell'evidenza stimata**, **rischio** e **sforzo**. Le dipendenze introducono una penalità; il calcolo è `4×impatto + 3×riuso + 2×evidenza - 3×rischio - 2×sforzo - 2×n_dipendenze`. Si tratta di un indice **relativo e non validato**, non di una probabilità, ROI, ore risparmiate o previsione di conversione.

Confronta inoltre l'HEAD immutabile di producer e consumer e la data di osservazione con l'inventario canonico `SOURCE_INVENTORY.json`; un consumer assente o HEAD vecchio produce `STALE_RECHECK` e **non può arrivare davanti a proposte fresche** solo per punteggio alto. Ciascun risultato ha reason code per review mancante, dipendenze, rischio elevato e freshness. Le ipotesi testuali sono riportate solo come SHA-256 per evitare che il report riversi contenuto non verificato potenzialmente sensibile; i fattori numerici restano ispezionabili.

## Confini di autorità e verifica

- Il risultato è **ADVISORY_ONLY**; nessun consumer viene scritto, nessuna PR è aperta, nessun CAP ID è creato, nessuna Golden viene promossa. Anche `SCOPED_REVIEW_RECORDED` indica solo presa visione della review, non implementazione certificata.
- Una stima `impact=5` non dimostra domanda reale o compatibilità delle licenze.
- L'input X10-043 non garantisce approvazioni autentiche né la provenienza della CI; i caller devono verificare i receipt attraverso una control plane indipendente.
- L'inventario canonico precedente risulta osservato il **2026-11-08**. Non generare artificiosamente proposte `READY` dalla sua staleness. Un cockpit vuoto è un risultato corretto finché non sono disponibili vere proposte X10-043 e stime approvate.
- Nessuna dashboard web interattiva, scansione live webhook, sistema di autorizzazione GitHub, consumer CI o risparmio 10x reale è stato realizzato in X10-044.

[Regression suite](../tests/factory_10x_reuse_cockpit_test.py) esercita ranking, input incompleti, staleness, falsi claim di review, blocchi e immutabilità del perimetro. Eseguita nella [CI queue](../.github/workflows/app-factory-10x-queue.yml) con verifica exact-head. **Stato di evidenza:** SOURCE+PYTHON_CI soltanto dopo la CI e il merge effettivi.
