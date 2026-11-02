# CAP-0147 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/app_shell.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/app_shell.dart).
- **Nuovo comportamento NON verificato:** Riordino e visibilità di card esistenti in una Home, rispettando preferenze persistenti e navigazione accessibile.
- **Facilità di integrazione editoriale:** 65% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Riordino opzionale 2-3 card già esistenti, fallback per preferenze vecchie, reset e keyboard-accessible controls.

**Gate:** No secondo dashboard/data store; screenshot matrix su UI5, contrasto, semantica, performance, account switch e fallback small screen.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
