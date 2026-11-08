# CAP-0163 — Specifiche E0

## Ambito
Note gerarchiche, alias e transclusioni controllate

Delta circoscritto a Note gerarchiche, alias e transclusioni controllate. Non duplicare la responsabilita delle CAP CAP-0013. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0013, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
No cicli e duplicazioni di proprietario; link non equivalgono a copia
