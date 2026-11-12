# X10-028 — QA test router condiviso: integrazione source+CI

**Factory baseline**: `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29.

## Evidenza

- Owner AppLab; [PR #224](https://github.com/riccardopinato/AppLab/pull/224), exact-head `6735183a9baa78124d14a2dcdb02c643fc00b766`, **MERGED** in main `4409c77862cc83aa25bd4303a8066b6eea78b170`.
- 7/7 workflow exact-head **PASS**: AppLab CI, CodeQL, governance, canonical runtime fixture, emulator self-test, Browser WebRTC E2E, autonomous review. Il Browser E2E è eseguito sul runner Ubuntu 24.04 già integrato dalla #220; è un test infrastrutturale AppLab, non di app consumer.
- Review indipendente Codex `codex-review-state:v1`, `code_review.commit_sha=6735183a9baa78124d14a2dcdb02c643fc00b766`, `status=completed`, senza finding; thread risolti.
- Codice [`scripts/qa_test_router_x10.py`](https://github.com/riccardopinato/AppLab/blob/main/scripts/qa_test_router_x10.py) e [test](https://github.com/riccardopinato/AppLab/blob/main/backend/tests/test_x10_qa_test_router.py), contratto [X10-028 QA Router](https://github.com/riccardopinato/AppLab/blob/main/integration/agent_core/X10-028_QA_TEST_ROUTER.md).

## Scope comprovato

Adapter *reuse-first* al planner `smart_test_plan` e gate canonici AppLab; FAST selective, FULL e FAST→FULL coprono tutti i gate richiesti. Identità repo/SHA e run URL strutturale; negative test per route vuota/manomessa, downgrade, source mismatch, WARN/SKIPPED, gate obbligatori e falso PASS. I receipt rimangono `RUNNER_REPORTED_ONLY` e `independent_provenance_verified:false`.

**Stato X10-028 VERIFIED solo SOURCE+APPLAB_CI**. Non prova esecuzione su Anna's Diary/World Days/altro consumer, reale QA per-app, signed APK/AAB, release e dispositivo fisico. Questa distinzione è necessaria per non promuovere impropriamente le capability/Golden. X10-029 (visual regression), X10-030 (perf/accessibility), X10-031 (provenance firmata), X10-045 (feedback→donor) diventano candidati READY, ciascuno con PR/CI/review propri.
