# CAP-0141 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/screens/shared_space.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/screens/shared_space.dart).
- **Nuovo comportamento NON verificato:** Una domanda condivisa con risposte private e rivelazione soltanto dopo la risposta di entrambi, senza pressione alla partecipazione.
- **Facilità di integrazione editoriale:** 65% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Catalogo locale versionato, due risposte per domanda, stato di reveal consensuale, sessione disconnessa e retry idempotente.

**Gate:** Non approvata in roadmap. Prima validare con due account/device, disclosure in cache/push/feed, revoca e privacy #215 ON HOLD; nessuna E2EE implicita.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
