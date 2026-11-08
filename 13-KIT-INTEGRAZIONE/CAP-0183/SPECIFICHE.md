# CAP-0183 — Specifiche E0

## Ambito
Punti, ricompense e progressione volontaria delle task

Delta circoscritto a Punti, ricompense e progressione volontaria delle task. Non duplicare la responsabilita delle CAP CAP-0145, CAP-0096, CAP-0101. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0145, CAP-0096, CAP-0101, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Opt-in, nessuna pressione/comportamento patologizzante
