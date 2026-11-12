# X10-043 — Revisione semantica supervisionata di capability/Golden

**Baseline:** App-Factory-Core `c5adc147046beb7024629466d10eeb799c3c2619`; Golden Index v29. **Input canonico:** X10-041 evento+diff autenticato, X10-042 join CAP-source/consumer; `REGISTRO_CAPABILITY.json` e `SOURCE_INVENTORY.json` rimangono le uniche fonti per IDs e stato, non vengono alterati.

## Implementazione
[Modulo](../scripts/factory_10x_semantic_review.py) `factory_10x_semantic_review.prepare()`: produce proposta versionata `X10_043_SUPERVISED_REUSE_PROPOSAL` con:
- identità immutabile `producer_repo`, `producer_sha`, `consumer_repo`, `consumer_sha`, `cap_id` e *hash* del percorso sorgente, non contenuti o nomi file potenzialmente sensibili;
- descrizione semantica della capability e assessment di compatibilità del consumer richiesti e bounded;
- evidenza test pin alla **stessa SHA donor** e run CI; il testo/URL del run non è indipendentemente attendibile finché il controllo esterno non lo verifica;
- decisione licenza `INTERNAL_APPROVED` o `SPDX_VERIFIED` con prova per *quel file* e URL, e Product Bible consumer con ref che contiene `consumer_sha`, policy `REVIEW_REQUIRED`;
- approvazione umana `APPROVED`, `REJECTED` o `DEFERRED`, identità e scope review con **donor e consumer SHA** espliciti;
- callback `trusted_receipt_verifier` da componente indipendente: senza attestazione reale lo stato è **BLOCKED_PENDING_REVIEW**, anche se in input compare la scritta APPROVED; con attestazione positiva solo `SCOPED_REVIEW_RECORDED`, mai esecuzione automatica o pubblicazione Golden.

Il modulo è una **projection ADVISORY_ONLY**, non un sistema di firma né una fonte di approvazioni. Il verifier deve controllare ACL/autenticazione reviewer, Product Bible vera al commit, licenza per-file, provenienza CI/run source, capability scope ed eventuali permessi/prodotti. Un callback finto usato in test **non** autorizza azioni reali.

## Test e confini
[`tests/factory_10x_semantic_review_test.py`](../tests/factory_10x_semantic_review_test.py) controlla source/target mismatch, licenze mancanti, Product Bible stale, firma/review falsa, candidate stale/blocked, rifiuto/defer e non-promozione. Python CI exact-head dimostra soltanto l'algoritmo del gate.

**NON PROVATO:** due consumer reali, legal review licenze, vera approvazione owner, CI del consumer, codice integrato, device/Store, reale processo di autorizzazione presso GitHub. Prima di una scoped PR per-app serve la review indipendente, e dopo la PR servono QA e product gates consumer. Non modificare stati ufficiali CAP/Golden in assenza di prove nuove.
