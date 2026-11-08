# CAP-0173 — Specifiche E0

## Ambito
Sprint, cicli e retrospettive di progetto

Delta circoscritto a Sprint, cicli e retrospettive di progetto. Non duplicare la responsabilita delle CAP CAP-0103, CAP-0111, CAP-0148. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0103, CAP-0111, CAP-0148, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Non sovrascrivere il planner esistente
