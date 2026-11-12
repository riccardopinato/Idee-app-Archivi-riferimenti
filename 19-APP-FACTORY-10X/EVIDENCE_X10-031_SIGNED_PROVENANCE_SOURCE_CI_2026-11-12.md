# X10-031 — Signed release provenance gate (SOURCE + CI)

**Factory baseline:** App-Factory-Core@`c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29.

- Repository: `riccardopinato/AppLab`, [PR #225](https://github.com/riccardopinato/AppLab/pull/225) MERGED; main squash SHA `a1ddbbe4be15b8cadd7f3614f4ec7a33e12e6658`.
- Exact PR head tested and reviewed: `107e005d2d6ee5a3d389b50f3fc9321e091d4edb`.
- All seven workflows **SUCCESS** on exact head: Repository Governance Audit, AppLab True Autonomous App Review v5.3.5, Canonical Runtime Fixture Build, AppLab CodeQL, AppLab CI, Live Emulator Browser E2E, Emulator Self Test.
- Independent Codex `code_review.status=completed`, `has_any_findings=false`, `has_unresolved_findings=false`; the three P2 review threads on earlier head were documented and resolved before merge.

## Implementazione

- `scripts/x10_signed_release_provenance.py` riusa l'autorità dei package-build contracts e degli inspector AppLab esistenti. Controlla hash SHA-256 e size dei byte, source Git SHA, AppLab SHA, manifest package/versionName/versionCode, certificato signer, scope ABI APK attraverso contenuti ZIP, contratto AAB vincolato all'hash della build, repository workflow distinto dal consumer e forma degli artifact URL.
- `backend/tests/test_x10_signed_release_provenance.py`: test negativi sintetici per manomissione, firma mancante, mismatch source/version/ABI/AAB, symlink e URL incongruenti.
- `integration/agent_core/X10-031_SIGNED_RELEASE_PROVENANCE.md`: limiti dell'adapter e provenienza.

**Stato canonico: VERIFIED SOURCE+CI soltanto.** Il modulo non esegue un vero inspector AAB, non prova l'esistenza di un artifact upload e non certifica che un consumer abbia ricevuto un APK/AAB firmato. Device, upgrade senza perdita dati, Play Internal Testing, Store e release restano separati. Nessuna chiave di firma creata o letta. Il successore X10-032 è HUMAN_GATE per test effettivi; X10-033 attende X10-029 e X10-030.
