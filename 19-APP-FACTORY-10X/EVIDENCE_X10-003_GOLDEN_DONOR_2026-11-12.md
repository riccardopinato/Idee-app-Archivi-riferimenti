# X10-003 — Inventario Golden/donor e consumer candidati

**Data:** 12/11/2026 · **Scope:** ricognizione statica e registrazione di evidence, **non** estrazione/importazione codice.
**Factory baseline verificata:** [App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619](https://github.com/riccardopinato/App-Factory-Core/commit/c5adc147046beb7024629466d10eeb799c3c2619), Master v27 / Golden Index v29. Fonte Golden: [Registry](https://github.com/riccardopinato/App-Factory-Core/blob/c5adc147046beb7024629466d10eeb799c3c2619/golden/GOLDEN_REGISTRY.yaml). Donor: [snapshot Site](../16-APP-FACTORY-SITE/data/snapshot.json) (dataset del 08/11, potenzialmente meno fresco dei singoli repo).

## Inventario reale
- **61** Golden/Process registrati; di cui **2** `CERTIFIED GOLDEN` scoped; **9** `COPY-READY GOLDEN` secondo l'admission esatta; **4** `COPY-READY PROCESS`; i restanti hanno stati diversi di candidato/draft/donor/deprecated.
- **20** passport donor in snapshot su **17** progetti; **15** sono `E3_EXACT_HEAD_TESTS`, altri **4** E3 di altra categoria storica e **1** E2. E3 non significa artefatto universalmente integrabile, compatibilità futura o QA fisico.
- Il [JSON normalizzato](data/reuse_inventory_v1.json) registra *tutti* i 61 status esatti, data/freshness, fonte SHA e tutti i 20 passport col relativo SHA/CI. È un **inventario derivato**, non un secondo Registry e non certifica alcun codice nuovo.

## Selezione concreta per i futuri kit Flutter

| Priorità | Modulo Golden | Condizione attuale | Consumer sperimentali *da approvare* | Gate prima dell'uso |
|---|---|---|---|---|
| 1 | `profile_standard` | COPY-READY / freshness CURRENT | Battery Guard, World Days | Estrarre API pura, test profilo/nomi/null, no doppia auth |
| 1 | `ci_release_web_deploy` | COPY-READY / CURRENT | Battery Guard, World Days | Pin Action, firma persistente, source/artifact identity, device separato |
| 1 | `entitlement_contract` | COPY-READY provider-agnostic / CURRENT | World Days, Battery Guard se approvato | Test access state offline/fail-closed; **no** billing reale implicito |
| 2 | `theme_m3` | COPY-READY / NEEDS_REVIEW | Utility Flutter nuove | Flutter SDK/versioni, light/dark/system, contrasto, screenshot |
| 2 | `localization` | COPY-READY / NEEDS_REVIEW | World Days, Notes | ARB/toolchain attuale, plurali, fallback, RTL se pertinente |
| 2 | `google_auth_supabase` | COPY-READY / NEEDS_REVIEW | Consumer con login richiesto | Provider/OAuth auth-callback staging, privacy, session lifecycle |
| 2 | `secure_storage_android_keystore` | COPY-READY / NEEDS_REVIEW | App con segreti cifrati | Android keystore, backup/restore e migration, secure defaults |
| 2 | `notification_reliability` | COPY-READY / NEEDS_REVIEW | World Days e utility promemoria | Runtime permissions, Android SDK, lifecycle e notifica effettiva |
| 3 | `civil_date_recurrence_engine` | COPY-READY pure Dart reference | Calendari/World Days se prodotto autorizza | API/versione, timezone e test consumer secondo Golden |
| NON ORA | `backup_recovery` | **DRAFT / CANDIDATE** | Anna/Notes/CamperBoss | Corruzione file, atomic restore, safety snapshot e test fisico |
| NON ORA | `play_billing_lifetime_entitlement` | **DRAFT**, Store sandbox NOT_VERIFIED | Utility commerciale | Provider test in Play sandbox + policy/review, budget approvato |

## Donor Passport — relazioni utili
- `anna_media` → Anna's Diary (media), `notes_links` → Notes (link/graph), `camper_backup` → CamperBoss (backup); *questi passport non certificano una libreria Flutter installabile*.
- `world_content_pack` → World Days, `notification_dedup` e `notification_quiet_hours` → Notification-Control, `battery_estimation` → Battery Guard; riuso di dominio solo dietro verifica licenza + consumer.
- `trail_geo` → TrailPath, `taste_retrieval` → TasteAI, `phone_security_policy` → Phone Guard; strumenti e codice Android possono essere platform-specific.
- La classificazione `E3_SOURCE_PINNED_TESTS` è diversa da `E3_EXACT_HEAD_TESTS`. `send_upload_bounds` è E2 storico: non promuovere per inferenza.

## Architettura di selezione 10x
1. Resolve `CURRENT.yaml` una volta e usa Golden exact-SHA, non latest remembered docs.
2. `X10-017`: definire un contratto di package con API, licenza, semver, matrix Flutter/Dart/provider, provenienza, policy aggiornamento e rollback.
3. `X10-018`: AppLab harness con test lato donor + due consumer.
4. `X10-019`: starter Flutter **minimale**: tema, localizzazione, profilo opzionali, nessuna auth/paywall auto-abilitata.
5. `X10-020..026`: integrazione per consumer con Product Bible + CI exact-head + device quando richiesto. Due consumer prima di ogni promozione Golden.

**Decisione:** X10-003 è un inventario evidence-backed e riproducibile, **non** una nuova certificazione. Aggiornare l'inventario solo a una nuova Factory baseline dichiarata; nessun modifica al Golden Core effettuata.
