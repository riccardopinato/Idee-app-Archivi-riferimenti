# X10-042 — Join CAP/donor: nessun duplicato, nessuna promozione

**Factory:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`. **Precondizione:** X10-041 [Agent-Core PR #19](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/19), merge `f6b4d6fd022e34c1784e2915733b89bf5ee24d74`. Source of truth CAP: [REGISTRO_CAPABILITY.json](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json); snapshot GitHub: [SOURCE_INVENTORY.json](../12-CAPABILITY-E-IMPLEMENTAZIONI/SOURCE_INVENTORY.json).

## Contratto source implementato

[`scripts/factory_10x_cap_dedup.py`](../scripts/factory_10x_cap_dedup.py) esegue join **deterministico** dei segnali X10-041 `path_sha256` con le sole associazioni `implementation_evidence.{producer}.source_path/source_sha` in record `CAP-NNNN` già presenti nel REGISTRO, quindi con i consumer esplicitamente censiti nel rispettivo `app_states`. Non ricostruisce il nome file originale dagli hash e non inventa ID CAP, repo consumer o codice donor.

Ogni candidato è identificato con hash della tupla `(producer_repo, producer_sha, CAP_ID, consumer_repo, consumer_inventory_sha, REUSE_REVIEW)` e include `requires_license_review:true`, `requires_product_owner_approval:true`, `automatic_adoption:false`, `ci_verified_this_run:false`. Le app già `SOURCE_CONFIRMED`, `CI_VERIFIED`, `DEVICE_VERIFIED`, `RELEASE` **non** ricevono una proposta duplicata per lo stesso CAP. Non equivale a certificare un CAP in un'altra app.

Se sorgente, HEAD della snapshot, vecchia evidence CAP, baseline Factory o osservazione inventory non sono sincronizzate, lo stato è `STALE`, non `ACTIONABLE`. Anche in presenza di tutti i match lo stato massimo è `NEEDS_REVIEW`.

## Limiti e verifica
- L'inventory canonica è uno **snapshot 08/11**; non riflette automaticamente gli HEAD attuali. Il Registry contiene riferimenti storici Factory: possono essere stale e non vengono riscritti da questa funzione.
- Gli input devono provenire da checkout/commit GitHub già autenticati e fissati al relativo SHA; la funzione non accede alla rete né verifica materialmente l'esistenza dei file/copyright/licenze. Il caller deve controllare source/head e ACL.
- [Test di regressione](../tests/factory_10x_cap_dedup_test.py) su match positivo, duplicati, CAP origin, licenza/owner gate, inventory stale, evidence SHA non allineata, consumer già implementato e no leak del nome sorgente. Nessun codice o PR consumer modificato; nessuna Golden promossa.
- Per la successiva X10-043 un reviewer deve controllare corrispondenza semantica dei consumer, Product Bible, licenza donor *per-file* e prove CI esatte; il risultato di X10-042 è sempre ADVISORY_ONLY.

**Scope della verifica:** source+CI del join, **non** monitor GitHub realmente in esecuzione, CAP aggiornato da nuovo source, pipeline di riuso live o riduzione dei costi misurata.
