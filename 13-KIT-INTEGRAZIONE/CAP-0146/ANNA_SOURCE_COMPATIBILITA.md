# CAP-0146 — Compatibilità preliminare Anna's Diary

- **Ambito:** `PARTIAL_REUSE` (presenza di struttura affine, nuova capability NON verificata).
- **Snapshot di audit storicizzato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`.
- **File sorgente osservato esistente:** [`lib/src/screens/private_vault.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/screens/private_vault.dart).
- **Nuovo comportamento NON verificato:** Estensione opzionale del Vault cifrato a PDF/scansioni, con cifratura dei contenuti e gestione robusta della recovery.
- **Facilità di integrazione editoriale:** 30% (stima, non percentuale di test superati).
- **Stato CAP per Anna:** PROPOSTA; non approvato in Product Bible/roadmap.

## Approccio

Nessun codice fino a threat model. Solo dopo: singolo PDF limitato, stream cifrato, preview temporanea protetta e recupero verificato.

**Gate:** Security HIGH: plaintext temporanei/thumbnail/indici, backup/cloud, perdita chiavi, iOS/Web, memoria; Privacy #215 ON HOLD; no claim Keystore universale.

## Evidence ladder

- Esistenza file donor: VERIFICATA allo SHA di audit.
- Implementazione del nuovo comportamento: NON VERIFICATA / PROPOSTA.
- Flutter test/analyze, build APK, prova Android/iOS, QA due account e Play: NON ESEGUITI per questa CAP.
- Privacy #215: DRAFT / ON HOLD su richiesta del proprietario; questa ricerca non la modifica.
