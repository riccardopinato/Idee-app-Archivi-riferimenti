# Specifiche candidate — CAP-0141

## Responsabilità distinta

Una domanda condivisa con risposte private e rivelazione soltanto dopo la risposta di entrambi, senza pressione alla partecipazione.

## MVP delimitato

Catalogo locale versionato, due risposte per domanda, stato di reveal consensuale, sessione disconnessa e retry idempotente.

## Vincoli architetturali

- Noi condiviso, catalogo domande locale, autenticazione solo per collaborazione, policy visibilità e versioning.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

Non approvata in roadmap. Prima validare con due account/device, disclosure in cache/push/feed, revoca e privacy #215 ON HOLD; nessuna E2EE implicita.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
