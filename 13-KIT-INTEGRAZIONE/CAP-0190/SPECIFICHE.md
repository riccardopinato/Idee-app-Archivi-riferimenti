# CAP-0190 — Specifiche E0

## Ambito
Da evidenziazioni PDF a note collegate e storylines

Delta circoscritto a Da evidenziazioni PDF a note collegate e storylines. Non duplicare la responsabilita delle CAP CAP-0098, CAP-0119. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0098, CAP-0119, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Riusare CAP-0035/0098/0119; preservare pagina e provenance
