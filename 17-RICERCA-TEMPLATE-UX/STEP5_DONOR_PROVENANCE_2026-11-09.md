# Maxi-step 5 — Donor scoped / Golden candidate: Template Native Preview

**Data:** 2026-11-09. **Factory baseline:** `App-Factory-Core@d4ed1185d36d419228fba6b57a979cde308bd321` (CURRENT Master v27, Golden Index v29). **Stato decisionale: HARVEST DOCUMENTATO / GOLDEN NON PROMOSSO**.

## Perimetro e deduplicazione

Il pattern TPLUX-001 (catalogo / anteprima / configurazione / conferma / writer canonico) è integrato come **tre implementazioni app-specifiche**, non come pacchetto Flutter unico e non come nuovo Store. Il contratto centrale già esistente è `App-Factory-Core/contracts/template_engine_v1` (schema e validatore statici, NON SDK runtime). Il Golden `GOLDEN_PROVENANCE_REUSE_LEDGER_v1_DRAFT` disciplina questi record; `GOLDEN_SINGLE_DONOR_CAPABILITY_ADMISSION_v1` distingue E3 donor, E5 consumer e certificazione Golden.

**Dedup:** nel registro centrale CAP (199 record esaminati, 2026-11-09) non è stata promossa una nuova CAP per una seconda implementazione del catalogo; gli ID di ricerca `TPLUX-001` e lo standard `contracts/template_engine_v1` restano la chiave di coordinamento. Non equiparare il nome del pattern alla prova di portabilità di codice.

## Evidence ledger — componenti delimitati

| ID di ricerca | Donor e fonte immutabile | Code / test / prova CI | Evidenza ammessa e restrizione |
|---|---|---|---|
| TPLUX-E3-NOTES-01 | `riccardopinato/Notes-Ecosistema@f057c81c92532cd22b504116c14ccef8a2ad6612` | `flutter_app/lib/src/domain/templates.dart` (`PageTemplates.bookTracker`, `PersonalTemplates`); `flutter_app/lib/src/screens/templates_screen.dart`; `flutter_app/test/templates_backup_knowledge_test.dart`; `flutter_app/test/template_step4_catalog_widget_test.dart`; [PR #96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96), [PR #97](https://github.com/riccardopinato/Notes-Ecosistema/pull/97); [Web QA main run](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42705714341) | **E3 SCOPED / CI** per nota singola e gallery in Notes, non per writer multi-entità, account fisici, dati grandi o vendita. [QA supplementare #98](https://github.com/riccardopinato/Notes-Ecosistema/pull/98) in verifica separata |
| TPLUX-E3-ANNA-01 | `riccardopinato/Agenda-per-Anna@2c77c764ecf9982817aee8fc6ecc31ee75b741f9` | `lib/src/diary/diary_templates.dart`, `lib/src/daily_rituals.dart`; `test/v104_daily_rituals_test.dart`, `test/v105x_audit_maintenance_test.dart`, `test/template_step4_free_gallery_test.dart`; [PR #290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290), [PR #291](https://github.com/riccardopinato/Agenda-per-Anna/pull/291); [Development main run](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/42705284412) | **E3 SCOPED / CI** per preview testuale → editor privato e rituali quotidiani sequenziali, NON per Vault, ACL Noi, notifica fisica, store. [QA supplementare #293](https://github.com/riccardopinato/Agenda-per-Anna/pull/293) separata |
| TPLUX-E3-WONDER-01 | `riccardopinato/Wonderlog@c238afd82ca93699d0e0d5d4e3e3a9a0d6d1d9ee` | `flutter/lib/features/journeys/domain/trip_planner_template.dart`, `flutter/lib/features/journeys/presentation/journey_widgets.dart`; `flutter/test/trip_planner_template_test.dart`; [PR #26](https://github.com/riccardopinato/Wonderlog/pull/26), [Flutter Foundation main run](https://github.com/riccardopinato/Wonderlog/actions/runs/42701619424) | **E3 SCOPED / CI** per sezione `Journey.description` e writer esistente, NON per packing strutturato, prenotazioni o QA premium reali. Pages deployment [attempt 1 FAILED](https://github.com/riccardopinato/Wonderlog/actions/runs/42701619452) per timeout `syncing_files`; retry dell'**identico SHA** avviato, risultato da verificare. [QA supplementare #27](https://github.com/riccardopinato/Wonderlog/pull/27) separata |

**License / origin:** `INTERNAL_DONOR` per tutte e tre le implementazioni originali dei repository dell'owner. Non dichiarare una licenza SPDX che non è stata verificata nel singolo file; `INTERNAL / COPYING OUTSIDE OWNED REPOS NOT AUTHORIZED`. Nessun ZIP Notion, asset Mindful Setups, formule commerciali o testo protetto importati come donor. I `TPLUX-REF` restano riferimenti di ricerca, non provenienza di codice.

**Adattamento:** Notes usa `Note`/tags/personal templates e Material UI; Anna usa `DiaryTemplatePreset` + `DiaryBlock` privato + DS6/5 lingue e limiti Vault/Noi; Wonderlog usa `Journey` + Premium limit pre-write e 6 lingue. I tre writer non hanno un owner condiviso, né è stato copiato un adapter universale.

## Golden promotion: NO

E3 è limitato ai comportamenti diretti provati nei singoli donor; il **riuso cross-app E5 NON È PROVATO**: l'implementazione indipendente di tre schermate simili non equivale a consumer dello stesso codice estratto. Non creare `GOLDEN_TEMPLATE_STORE`, non modificare `App-Factory-Core/golden/GOLDEN_INDEX_CURRENT.txt` o `GOLDEN_REGISTRY.yaml`, non creare CAP nuova.

Per una promozione futura servono: owner e contratto di estrazione generalizzato, test unitari del riferimento, consumer realmente separato che lo utilizza (con SHA+CI), version/compat test, diritti verificati e QA nativo quando l'azione coinvolge account, file, notifiche o billing. Le evidenze physical/device, purchase/refund/restore e Web cross-account restano **NOT VERIFIED**.

## Checklist di handoff

1. Completare le tre PR QA #98/#293/#27 sul rispettivo exact-head senza presumere il loro merge.
2. Eseguire le matrici `docs/TEMPLATE_NOTION/QA_PHYSICAL_MATRIX_20261109.md` con identità di browser/device/versione e output osservati.
3. Rivalutare TPLUX-001 come candidato di **processo** (non SDK) solo dopo almeno un consumer indipendente; riusare il template manifest standard centrale senza clonare parser.
4. Per premium originali distinguere `CatalogManifest` vs `StoreProduct` vs `EntitlementSnapshot` vs `InstallReceipt`. Nessuna certificazione provider dai test statici.

## Aggiunta evidence dei consumer QA nativi — 09/11/2026

Il catalogo è aggiornato *senza modificare le baseline donor storiche* (immutabilità della fonte):

| Consumer/QA | Nuovo main merge SHA | Esito PR head | Ambito |
|---|---|---|---|
| Notes QA [#98](https://github.com/riccardopinato/Notes-Ecosistema/pull/98) | `cf9f9c515a87f438ab0112e7efd4a0ce0471fbd6` | `verify`, `verify-web`, `build-web` PASS | Fixed dialog controller lifetime, tests canceled/invalid title/backup round trip |
| Anna QA [#293](https://github.com/riccardopinato/Agenda-per-Anna/pull/293) | `260dd753a3f7d1b7cd501ce38cf6e4a78ea773b3` | `check` e `UI5 source and visual-flow contracts` PASS | Dialog preview cancel vs confirm in existing Diary, no new writer |
| Wonderlog QA [#27](https://github.com/riccardopinato/Wonderlog/pull/27) | `f045588dd5dbd668541fec380f184f3ebcd8bb6f` | `verify`, `apple-build`, `legacy-contract` PASS | Header validation and explicit Premium gate order; new Pages run SUCCESS |

**E5 remains NOT VERIFIED**: non sono consumer indipendenti dello stesso package/generalized code. No Store READY or hardware proof. The E3 historical donor source identities above remain valid at their pinned commits, while new QA adds evidence under separate commits.
