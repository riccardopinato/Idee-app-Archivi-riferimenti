# CAP-0189 — Specifiche E0

## Ambito
Biblioteca citazioni e riferimenti bibliografici

Delta circoscritto a Biblioteca citazioni e riferimenti bibliografici. Non duplicare la responsabilita delle CAP CAP-0119, CAP-0076. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0119, CAP-0076, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
CAP-0119 copre audit fonti, non intera libreria di riferimenti
