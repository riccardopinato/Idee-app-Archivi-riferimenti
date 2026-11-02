# CAP-0144 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/home_widget_bridge.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/home_widget_bridge.dart).
- **Nuovo comportamento NON verificato:** Widget OS alimentati da proiezioni canoniche autorizzate: prossimo evento/Crea, countdown e foto opt-in con mascheratura.
- **Facilità di integrazione editoriale:** 70% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Android Home: prossimo evento e apertura Crea; countdown su data scelta. Foto partner solo fase differita con consenso per immagine e revoca cache.

**Gate:** Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
