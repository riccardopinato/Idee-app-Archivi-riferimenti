# X10-026 — Two real Flutter consumers + independent rollback *source* evidence

**13 November 2026. Factory** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. **Task state remains PLANNED** because the X10-018 compatibility harness requires a real lower-semver package rollback receipt before full closure. This document records actual bounded implementation and tests, not hypothetical success.

## Verified source and pipeline, exact SHAs

| Source | Actual tested code | Evidence |
|---|---|---|
| Factory donor | `factory_profile_kit 0.1.0` from `Idee-app-Archivi-riferimenti@1d1a8628e25f58b788b013cf6955763d00363cdc` | [AppLab independent matrix](https://github.com/riccardopinato/AppLab/actions/runs/43331970619) SUCCESS |
| Anna's Diary | `Agenda-per-Anna@984a34462ba527b2ea98dbc3a337bdd8614b88d4` | [Source+CI PR #307](https://github.com/riccardopinato/Agenda-per-Anna/pull/307), [#308](https://github.com/riccardopinato/Agenda-per-Anna/pull/308), [main Development checks](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43328842284) SUCCESS; [signed ARM64 build](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43329448204) SUCCESS |
| TasteAI | `TasteAI@61a83aa638654f4e885d503e024408d2dcddebc2` | [Profile adoption #6](https://github.com/riccardopinato/TasteAI/pull/6), [pin Flutter/toolchain CI #7](https://github.com/riccardopinato/TasteAI/pull/7), [full main Flutter CI](https://github.com/riccardopinato/TasteAI/actions/runs/43330930127) SUCCESS |
| AppLab source runner | `AppLab@d1ec6f94198b0ef9ddd2e520ec39b71df6887e23` merge of [PR #231](https://github.com/riccardopinato/AppLab/pull/231) | Exact PR source head `f2a70d1ce7eb96a34f3077fbc40a696e3e8061a9`; **7/7** workflow SUCCESS, Codex review no findings, threads resolved |

AppLab #231 tests the actual public-source repositories at the specified SHAs rather than fixtures. Both consumer `pubspec.yaml` and `pubspec.lock` pin the SAME immutable donor commit. The runner executes the donor Dart contract tests, both real source-consumer tests, existing Anna preferences and TasteAI restore tests, then checks out the **pre-adoption SHAs** `8fbfe14f7a21d41af274cf259c462df2eab9dc69` and `8e880be68d74686c6c6b7e6a992a5fdc6fa6c384` and reruns the existing tests there. All source tests passed on the 3.47.5 Flutter toolchain. No consumer app's stored bytes are changed by the profile adapter or test campaign.

## What this *does not* prove

- No Android device was downgraded from a newer installed APK to an older APK while preserving private user data. Only **source rollback** was executed; no device/Play verdict can be inherited.
- There is no verified package-version rollback from `factory_profile_kit 0.1.0` to a real earlier semver release. A fabricated `0.0.0` would be invalid. Consequently the existing [X10-018 Golden compatibility harness](https://github.com/riccardopinato/AppLab/blob/main/scripts/golden_compat_harness_x10.py) has not produced a complete real multi-consumer admission result.
- No OAuth, backup migration, native notification provider or billing integration was added to these users by the profile experiment.
- No Golden admission, release certification, proof of cross-app account behavior or independent installed-data migration proof.

## Remaining X10-026 gate

When there is a **real** next version of the shared kit (not an artificial bump just to satisfy the checklist), verify semver downgrade to the pre-existing version, acquire a genuine independently reviewed rollback CI receipt for the X10-018 harness, then complete scoped review/queue promotion. Downstream Golden X10-053 is a separate human gate and cannot be auto-activated.

Authoritative queue: [PROGRAM_QUEUE.json](PROGRAM_QUEUE.json). **34 VERIFIED / 22 PLANNED / 1 BLOCKED** remains the truth after this source campaign; source-only merge does not automatically close X10-026.
