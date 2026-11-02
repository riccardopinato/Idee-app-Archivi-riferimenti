# CAP-0142 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/shared_memories.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/shared_memories.dart).
- **Nuovo comportamento NON verificato:** Creazione volontaria di lettere/ricordi personali o condivisi con data di apertura e regole recuperabili.
- **Facilità di integrazione editoriale:** 70% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Modalità personale testo e reminder; estensione successiva coppia testo+foto con data/fuso e apertura esplicita dopo prova privacy.

**Gate:** Nessuna garanzia crittografica del blocco temporale. QA date/fusi/offline/orologio, backup e sync due device; shared dopo Privacy #215.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
