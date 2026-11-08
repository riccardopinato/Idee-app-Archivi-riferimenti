# CAP-0179 — Specifiche E0

## Ambito
Espansione testo a livello di sistema operativo

Delta circoscritto a Espansione testo a livello di sistema operativo. Non duplicare la responsabilita delle CAP CAP-0084. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0084, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Accessibilità/input hook per piattaforma, privacy, non installare di default
