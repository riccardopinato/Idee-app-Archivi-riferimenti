# X10-028 — QA Test Router condiviso: closure SOURCE + CI

**Data:** 2026-11-12  
**Baseline:** App-Factory-Core@`c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29.

## Prove verificabili

- Repository: `riccardopinato/AppLab`.
- PR [#224](https://github.com/riccardopinato/AppLab/pull/224) MERGED in `main`; merge SHA `4409c77862cc83aa25bd4303a8066b6eea78b170`.
- Head revisionata/testata: `6735183a9baa78124d14a2dcdb02c643fc00b766`.
- Workflow exact-head tutti conclusi SUCCESS (7/7): Canonical Runtime Fixture Build; AppLab CI; AppLab True Autonomous App Review v5.3.5; AppLab CodeQL; Emulator Self Test; Live Emulator Browser E2E; Repository Governance Audit.
- Review Codex: `chatgpt-codex-connector[bot]` review `code_review.status=completed`, `commit_sha=6735183a9baa78124d14a2dcdb02c643fc00b766`, `has_any_findings=false`, `has_unresolved_findings=false`; [commenti PR](https://github.com/riccardopinato/AppLab/pull/224#issuecomment-6827145692).

## Perimetro attestato

- `scripts/qa_test_router_x10.py` e `backend/tests/test_x10_qa_test_router.py` aggiunti ad AppLab.
- Selezione test per app e modalità FAST / FULL, con STRICT_GATES e receipts vincolati alla fonte.
- WARN, SKIPPED, risultati vuoti o privi di prova non vengono promossi a PASS; nessuna attribuzione di certificazione automatica sulla sola base della CI.

## Limitazioni e successori

**VERIFIED SOURCE+CI, non runtime consumer/device/Store.** Non sono stati collaudati tutti i singoli prodotti, non è certificata la firma degli APK/AAB e non risulta un'autonomia live dell'agente Windows.

Sblocca gli interventi separati X10-029 (regressione visuale), X10-030 (performance e accessibilità), X10-031 (provenienza firmata release), X10-045 (feedback failure→donor), subordinati ai loro gate di sviluppo e review.
