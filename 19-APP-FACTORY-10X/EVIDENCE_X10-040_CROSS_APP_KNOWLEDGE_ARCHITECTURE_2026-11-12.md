# X10-040 — Architettura knowledge/reuse centrale, senza seconda source of truth

**Audit:** 12/11/2026 · **Ideas source:** [main@34cd92305511339036688d810e6dbe071e6548a2](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/commit/34cd92305511339036688d810e6dbe071e6548a2) · **AppLab:** [main@9bbb424929fe8916e84e2b0a9da384961c26f1e1](https://github.com/riccardopinato/AppLab/commit/9bbb424929fe8916e84e2b0a9da384961c26f1e1) · **Factory baseline:** [Core@c5adc147046beb7024629466d10eeb799c3c2619](https://github.com/riccardopinato/App-Factory-Core/commit/c5adc147046beb7024629466d10eeb799c3c2619), Master v27 / Golden Index v29.
**Classificazione:** `READ_ONLY / SOURCE_AUDITED / DESIGN_ONLY`. Nessuna scansione agentica continua, consumer code change, CI cross-repo, pubblicazione Golden o conoscenza derivata da dati privati verificata qui.

## Una sola autorità per dominio

| Dominio | Fonte primaria; prova dal codice | Vista derivata / possibile input | Divieto |
|---|---|---|---|
| Master, Golden, stati E e politica di promozione | [App-Factory-Core CURRENT](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/CURRENT.yaml), [Golden Registry](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/golden/GOLDEN_REGISTRY.yaml) | AppLab [factory_reuse_planner_v57d.py](https://github.com/riccardopinato/AppLab/blob/9bbb424929fe8916e84e2b0a9da384961c26f1e1/scripts/factory_reuse_planner_v57d.py) restituisce `ADVISORY_ONLY`, `automatic_code_change:false` | Nessuna modifica automatica a GOLDEN/CERTIFIED dal planner |
| ID CAP, score e stato per app | [REGISTRO_CAPABILITY.json](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/34cd92305511339036688d810e6dbe071e6548a2/12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json), [build_catalog.py](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/34cd92305511339036688d810e6dbe071e6548a2/scripts/build_catalog.py) | viste generate, `PER_APP`, `DA_VALUTARE` / `GIA_INTEGRATI` / `DA_VERIFICARE` | Non creare nuovi CAP dalla sola ricorrenza lessicale, non scambiare score con prova di implementazione |
| Repo/HEAD osservati e freshness | [SOURCE_INVENTORY.json](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/34cd92305511339036688d810e6dbe071e6548a2/12-CAPABILITY-E-IMPLEMENTAZIONI/SOURCE_INVENTORY.json) | snapshot + diff di commit, timestamp ultima osservazione | Snapshot HEAD del 08/11 non è lo stato GitHub di oggi; comparare source SHA esatto |
| Evidenza sorgente, test e artifact | CI/PR/commit del repository consumer; AppLab [Trusted Evidence Chain](https://github.com/riccardopinato/AppLab/blob/9bbb424929fe8916e84e2b0a9da384961c26f1e1/integration/intelligence/TRUSTED_EVIDENCE_CHAIN.md) e [Release Reality](https://github.com/riccardopinato/AppLab/blob/9bbb424929fe8916e84e2b0a9da384961c26f1e1/integration/certification/RELEASE_REALITY_V44.md) | evidence reference con status source/CI/runtime/device/release separati | Un advisory, un flag `PRESENT` o un link non deve inventare PASS/Store Ready |
| Intelligence descrittiva cross-app | AppLab [cross_app_intelligence.py](https://github.com/riccardopinato/AppLab/blob/9bbb424929fe8916e84e2b0a9da384961c26f1e1/scripts/cross_app_intelligence.py): normalizza feature signals e trova ricorrenze da report con SHA-256 | suggerimenti e anomalie da sottoporre a review | Ricorrenza o similarità non è autorizzazione ad applicare patch |
| Donor/OSS riuso | registro donor/Golden e ledger di provenance (Master/Golden pertinenti), contratti source e licenze per-file | proposta kit con `source_sha`, percorso, licenza, compatibility evidence | Nessuna copia da fonti NOASSERTION/ambigue, nessuna promozione senza consumatore indipendente |

## Architettura minima — collegare, non duplicare

```text
GitHub commit/ref (repository consumer, SHA esatto)
    -> diff scoped + changed paths + invalidation key
    -> lookup registro CAP + SOURCE_INVENTORY (snapshot con freshness esplicita)
    -> lookup Golden Registry/Donor provenance al Core SHA fissato
    -> AppLab cross_app_intelligence / factory_reuse_planner (ADVISORY_ONLY)
    -> candidate record: reason, cap_id, source/destination SHA, owner,
       license, applicability, risk, dependency/gates, confidence, evidence refs
    -> dedup/review by human or independent authorized reviewer
    -> per-consumer Product Bible + CI/QA/permissions
    -> SOLO DOPO: scoped PR; aggiorna CAP dalla vera prova del consumer
```

**Identità di dedup candidata (non già implementata):** `(producer_repo, producer_sha, CAP_ID, consumer_repo, consumer_sha, intended_action)`. SHA diversi non si sovrascrivono, ma possono rendere stale la proposta vecchia. Due record su una stessa capability non creano due CAP: il `CAP_ID` canonico resta uno, con associazioni per app separate.

**Eventual schema di proposta, non nuovo database canonico:** `proposal_id, cap_id, consumer_repo, consumer_sha, producer_repo, producer_sha, source_paths, golden_core_sha, donor_license_scope, reason_codes, evidence_links, status [PROPOSED/NEEDS_REVIEW/BLOCKED/APPROVED/REJECTED/STALE], expiry, reviewer`. Una vista JSON/Job Summary rigenerabile è sufficiente all'inizio. Non salvare sorgenti private, secrets, informazioni personali, credenziali o file finanziari nel repository pubblico.

## Task dependency e acceptance per la corsia intelligence

- **X10-041 diff-aware monitor:** solo confronto pinned SHAs e changed file scopes, timeout/rate-limit/retry bounded, idempotenza, no baseline refresh invisibile, no GitHub writes di default. Fonte: GitHub real refs, non vecchia cache di chat.
- **X10-042 dedup CAP/donor:** join a registro CAP + inventory e stato consumer; test su falso match, più repo stessi CAP, licenze e source stale. Output candidati, non stato `IN_CODICE`.
- **X10-043 semantic review:** fonte/owner/PR e evidenze verificabili, quote licenze, `USER_GATE` dove provider/perms; comportamento fail-closed su evidenza insufficiente.
- **X10-044 review cockpit:** filtrare candidate `ACTIONABLE` vs `BLOCKED` vs `STALE`, con link source commit, confidence e costo. Non inventare un nuovo Site obbligatorio.
- **X10-045 feedback failure→donor:** ingestion di failure già registrate AppLab, tracciabilità fix/consumer e verifiche; non trasformare un success unit test in Golden senza prove multi-consumer.
- **X10-050/056:** richiedono piloti reali e risultati verificati; non si sbloccano con questo audit statico.

## Rischi e anti-duplicazione

1. **Evidenza stale:** SOURCE_INVENTORY è uno snapshot datato; freschezza per repository e verifica dell'esatto SHA obbligatoria prima di qualunque decisione.
2. **False equivalenze:** `SOURCE_REPORTED` non diventa `CI_VERIFIED`; `DESIGN_ONLY` non diventa Golden; `CI_GREEN` non diventa `STORE_READY`.
3. **Conflitto consumer:** stessa capability può essere implementata diversamente per Flutter, native Android o Web SEO; servirà una matrice di compatibilità per-app, non deploy massivo.
4. **Licenze/proprietà:** annotare licenza e path di ogni origine; il riferimento pattern non autorizza incorporare codice.
5. **Doppio scheduler/costo:** AppLab ha già intelligence e infrastruttura duratura; non creare un database globale alternativo né polling continuo fuori dagli eventi autorizzati.
6. **Autorizzazione:** il programma 10x seleziona task; non conferisce diritti di mutazione/merge/certificazione ai motori di raccomandazione.

## Stato dimostrato e limite di chiusura

**X10-040 completabile solo nello scope di audit di architettura:** componenti/autorità reali individuati, wire design minimo, record candidato e successione dei gate. Nessuna pipeline `X10-041` installata, test di integrazione e proposta inter-app vera eseguiti, automazione indipendente dimostrata o percentuale 10x misurata. `X10-041` resta a sé e richiede source+CI+recovery evidence prima di `VERIFIED`.
