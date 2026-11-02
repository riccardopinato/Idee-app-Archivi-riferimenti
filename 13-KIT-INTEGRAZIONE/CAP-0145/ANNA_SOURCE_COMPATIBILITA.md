# CAP-0145 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/planner_views.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/planner_views.dart).
- **Nuovo comportamento NON verificato:** Vista aggregata calendar-heatmap delle attività realmente annotate, con dati mancanti distinti da zeri e senza inferenze psicologiche.
- **Facilità di integrazione editoriale:** 70% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Griglia locale per eventi/diario/task esistenti; eventuale mood/gratitudine solo con input esplicito e consenso.

**Gate:** No health/diagnostic claims, no dati ciclo/Vault in UI ordinaria, no esempi +40% spacciati per risultati; test missingness e permessi.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
