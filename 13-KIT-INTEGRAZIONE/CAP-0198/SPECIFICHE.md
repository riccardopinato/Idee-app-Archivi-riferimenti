# CAP-0198 — Specifiche E0

## Ambito
Cattura audio di sistema e trascrizione locale consensuale

Delta circoscritto a Cattura audio di sistema e trascrizione locale consensuale. Non duplicare la responsabilita delle CAP CAP-0085, CAP-0095, CAP-0031. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0085, CAP-0095, CAP-0031, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Estende CAP-0085/0095; permessi OEM, consenso partecipanti e costo runtime
