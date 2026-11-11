# Context Sync — processo candidato a riuso (M5)

**Data:** 11/11/2026 · **Source of truth:** Master v27 / Golden Index v29 a `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`.

**Classe:** `PROCESS_CANDIDATE`. Non aggiunge CAP, Donor, Golden al registry. Non sostituisce il Golden esistente Event-Driven Reconciliation (`COPY-READY PROCESS`).

## Evidenze osservate
- Rollout documentale su 35 repository e check di workflow/CI; 32 v2, 3 originali.
- Cinque reali `push` canary di snapshot. Uno (btrader) ha generato PR bot reale [#5](https://github.com/riccardopinato/btrader/pull/5), retry idempotente e aggiornamento upstream.
- Quattro canary sono bloccati in fase create PR per repository Actions permission; la correzione Git identity su Agent Core è stata verificata in [run #43052705998](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43052705998).
- [PR #12 Agent Core](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/12) implementa helper offline per retry, conflitti, privacy e semantic-review. Non è collegato nei workflow dei 35 progetti.
- [PR #97 Ideas](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/97) introduce registro 35/35 con private redaction e vista Site sorgente, non deployment verificato.

## Matrice di admission

| Gate | Stato |
|---|---|
| Fonte e commit pinnati | PASS |
| Provenienza e limiti / privacy documentati | PASS |
| Test offline negativi del helper | CI PASS su Agent Core PR #12 |
| Run snapshot reale | PASS su 5 canary in scope `push` |
| Bot PR reale con recovery | PASS **solo btrader** |
| Due consumer indipendenti con cron+PR+recovery | NOT VERIFIED |
| Recupero dopo admin PR permission fix | BLOCKED |
| Fault injection runtime/retry rate-limit e conflitti | NOT VERIFIED |
| Allineamento per-app Product Bible + test consumer | NOT VERIFIED |
| Golden admission / certification PR nel Core | NOT ATTEMPTED |

## Controlli, dipendenze e prossima ammissione
- Prima completare la verifica dei quattro repository bloccati, senza bypass dei ruleset.
- Poi testare `workflow_dispatch` e `schedule` effettivi su almeno due consumer indipendenti e una failure/recovery; raccogliere URLs Actions e PR bot, HEAD esatto.
- Rilevare costi/minuti, quota API e fallimenti GitHub Actions, non inferirli dal solo numero di repository.
- Con validazione e Product Bible consultate, proporre una nuova admission nel Core tramite PR dedicata e reviewer, **senza** dichiarare Certified Golden in anticipo.
- In caso di fallimento: mantenere ultimo snapshot, disabilitare il solo workflow per-repo, rollback attraverso PR con CI, preservare cronologia e branch evidence. [Playbook](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/docs/CONTEXT_SYNC_RECOVERY_PLAYBOOK.md).

**Verdetto:** avanzamento progettuale/documentale M5, **non** promozione Golden completata.
