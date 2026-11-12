# X10-006 — Coda con evidence gates / workflow read-only

**Valutazione:** 12/11/2026 · **Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`.

## Evidence reale
- [PR #99](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/99) ha integrato i 57 task/8 ondate, `scripts/factory_10x_queue.py` e [workflow GitHub read-only](../.github/workflows/app-factory-10x-queue.yml), con [run 43121977331](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/43121977331) che esegue `--check`, test negativi e `--next` su PR. **Non** dimostra ancora un evento `schedule` della nuova Action.
- [PR #102](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/102) è merged al SHA `8fe0beb38e3c08da681e30bbbefab6248d8f95f7` e ha corretto il precedente tetto 3. La suite ha testato la selezione illimitata sul DAG e il coordinamento dei writer.
- Il validator rifiuta prerequisiti non verificati, task `VERIFIED` privi di `gate_reviewed + evidence kind/url/source_sha` e dipendenze cicliche. Il selettore espone tutti i READ_ONLY READY, coordina writer PR non isolati e libera i task BLOCKED.
- Un run Actions di sola pianificazione **non aggiunge da sé `VERIFIED`**; la registrazione avviene con branch→PR→CI→merge e source evidence.
- Un link GitHub in un JSON può essere formalmente valido ma non provare semanticamente il task; una review delle prove reali è comunque necessaria.

## Stato e limiti
**X10-006 = SOURCE+CI_VERIFIED** per la coda e il workflow read-only. NON `autonomous_code_execution`, `SCHEDULE_RUNTIME_VERIFIED` o `DEVICE_VERIFIED`. I gate del coding-agent dipendono da X10-010..016 e dall'import X10-008.

## Ultimo checkpoint
Da 2 a **7/57** task verificati con questo aggiornamento; X10-008 `BLOCKED` perché sorgenti Windows reali non ancora acquisiti; nuove attività pronte X10-010 (permission gateway), X10-017 (package Golden), X10-027 (QA matrix), X10-040 (intelligence architecture), oltre a business X10-002 e ulteriori task evidenziati dal resolver.
