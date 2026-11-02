# CAP-0143 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/shared_invite_qr.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/shared_invite_qr.dart).
- **Nuovo comportamento NON verificato:** Esportazione di un ricordo sotto forma di biglietto stampabile e, solo su scelta, link Web con QR, scadenza e revoca.
- **Facilità di integrazione editoriale:** 40% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Prima fase offline: PNG/PDF derivato da elemento selezionato. Seconda fase Web/PWA richiede token opaco revocabile e revisione destinatario.

**Gate:** Blocco disclosure pubblica: mai pubblicare contenuto privato automaticamente. Security review token/noindex/EXIF/URL leak/revoca, termini hosting e Privacy #215.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
