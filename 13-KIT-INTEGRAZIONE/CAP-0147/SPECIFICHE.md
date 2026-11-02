# Specifiche candidate — CAP-0147

## Responsabilità distinta

Riordino e visibilità di card esistenti in una Home, rispettando preferenze persistenti e navigazione accessibile.

## MVP delimitato

Riordino opzionale 2-3 card già esistenti, fallback per preferenze vecchie, reset e keyboard-accessible controls.

## Vincoli architetturali

- App shell e preferenze canoniche, design tokens e module-visibility semantics; non duplica CAP-0023 theme.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

No secondo dashboard/data store; screenshot matrix su UI5, contrasto, semantica, performance, account switch e fallback small screen.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
