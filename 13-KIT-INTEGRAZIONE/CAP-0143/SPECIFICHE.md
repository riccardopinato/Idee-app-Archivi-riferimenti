# Specifiche candidate — CAP-0143

## Responsabilità distinta

Esportazione di un ricordo sotto forma di biglietto stampabile e, solo su scelta, link Web con QR, scadenza e revoca.

## MVP delimitato

Prima fase offline: PNG/PDF derivato da elemento selezionato. Seconda fase Web/PWA richiede token opaco revocabile e revisione destinatario.

## Vincoli architetturali

- Export safe-copy, QR esistenti per inviti (non equivalenti), eventuale servizio token con scadenza e autorizzazione.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

Blocco disclosure pubblica: mai pubblicare contenuto privato automaticamente. Security review token/noindex/EXIF/URL leak/revoca, termini hosting e Privacy #215.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
