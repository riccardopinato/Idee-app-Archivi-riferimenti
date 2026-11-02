# Specifiche candidate — CAP-0142

## Responsabilità distinta

Creazione volontaria di lettere/ricordi personali o condivisi con data di apertura e regole recuperabili.

## MVP delimitato

Modalità personale testo e reminder; estensione successiva coppia testo+foto con data/fuso e apertura esplicita dopo prova privacy.

## Vincoli architetturali

- Diario/ricordi e media canonici, reminder; backend solo per condivisione esplicita e autorizzata.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

Nessuna garanzia crittografica del blocco temporale. QA date/fusi/offline/orologio, backup e sync due device; shared dopo Privacy #215.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
