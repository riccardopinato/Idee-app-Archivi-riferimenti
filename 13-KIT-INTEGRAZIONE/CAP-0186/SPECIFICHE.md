# CAP-0186 — Specifiche E0

## Ambito
Trasporto decentralizzato P2P per dati condivisi cifrati

Delta circoscritto a Trasporto decentralizzato P2P per dati condivisi cifrati. Non duplicare la responsabilita delle CAP CAP-0100, CAP-0018, CAP-0112. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0100, CAP-0018, CAP-0112, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Separare CRDT, identità e autorizzazione dal trasporto
