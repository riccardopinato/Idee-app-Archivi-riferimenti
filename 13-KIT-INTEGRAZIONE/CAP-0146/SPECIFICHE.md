# Specifiche candidate — CAP-0146

## Responsabilità distinta

Estensione opzionale del Vault cifrato a PDF/scansioni, con cifratura dei contenuti e gestione robusta della recovery.

## MVP delimitato

Nessun codice fino a threat model. Solo dopo: singolo PDF limitato, stream cifrato, preview temporanea protetta e recupero verificato.

## Vincoli architetturali

- Vault canonico/Keystore Android, envelope encryption, file store protetto; non importare PDF engine come percorso plaintext.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

Security HIGH: plaintext temporanei/thumbnail/indici, backup/cloud, perdita chiavi, iOS/Web, memoria; Privacy #215 ON HOLD; no claim Keystore universale.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
