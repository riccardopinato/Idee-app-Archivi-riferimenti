# CAP-0192 — Specifiche E0

## Ambito
Recupero account cifrato con frase mnemonica senza email

Delta circoscritto a Recupero account cifrato con frase mnemonica senza email. Non duplicare la responsabilita delle CAP CAP-0018, CAP-0146. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0018, CAP-0146, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Nessuna modifica al Vault Anna; threat model e restore test prima di valutare
