# X10-017 — Contratto operativo per pacchetti Golden Flutter

**Data:** 12/11/2026 · **Factory:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27 / Golden Index v29.  
**Fonte:** [X10-003 Golden/donor inventory](../EVIDENCE_X10-003_GOLDEN_DONOR_2026-11-12.md). **Stato:** `SOURCE+CI CONTRACT`, nessun package Flutter realmente estratto/installato.

## Output tangibile
- [Schema JSON](golden_package_v1.schema.json): campi versione, tipo di origine, Golden exact-SHA, donor/file SHA, licenza, SDK Flutter/Dart, dependency pin, donor/consumer CI, artifact/rollback e consenso pubblicazione.
- [Manifesto iniziale Profile Standard](PROFILE_STANDARD_CANDIDATE.json): `app_factory_profile_standard 0.0.0` **DESIGN_ONLY**; la fonte Golden è COPY-READY **come documento**, ma non c'è ancora una libreria testata. Licenza, versione runtime, SDK, CI consumer e artifact non sono inventati.
- [Validatore fail-closed](../../scripts/factory_10x_package_contract.py): blocca versioni e dipendenze mobili, provenance assente, package senza file, test senza matrice SDK, certificazione senza due consumer, rilascio senza SHA256/rollback.
- [Test negativi](../../tests/factory_10x_package_contract_test.py) in CI; comando: `python3 scripts/factory_10x_package_contract.py --check`.

## Ordine dei gate
1. `DESIGN_ONLY`: solo progetto del package, nessun codice copiabile.
2. `SOURCE_EXTRACTED`: file reali + origine SHA + licenza verificata + versione semver non-placeholder.
3. `PACKAGE_TESTED`: test donor e compatibilità effettiva Flutter/Dart, dipendenze fissate e reproducible CI.
4. `CONSUMER_VERIFIED`: almeno un consumer approvato nella sua Product Bible e CI exact-head.
5. `CERTIFIED_MULTI_CONSUMER`: due consumer indipendenti, test/admission, governance Golden Core e review separata. La stringa nello schema non certifica da sola il Registry.
6. Pubblicazione/download richiedono decisione per-artifact e rollback: lo schema può bloccare un manifesto incompleto ma non sostituisce l'autorizzazione reale di Store o dell'owner.

## Prossimi task
- `X10-018`: AppLab compatibility harness su versioni pinned.
- `X10-019`: starter kit Flutter minimale, componenti da combinare soltanto quando file/licenza/test sono disponibili.
- `X10-020–026`: provider identity, theme, backup e notifiche in consumer specifici, con gate separati.
- **Non** registrare questo schema come nuova CAP o Golden certificata automaticamente.

**Rischio neutralizzato:** non accettare più “Golden copy-ready” come prova di package installabile o di compatibilità universale.
