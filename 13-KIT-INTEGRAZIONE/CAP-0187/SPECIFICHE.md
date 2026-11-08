# CAP-0187 — Specifiche E0

## Ambito
Editing Typst/matematica con anteprima verificabile

Delta circoscritto a Editing Typst/matematica con anteprima verificabile. Non duplicare la responsabilita delle CAP CAP-0098, CAP-0119, CAP-0018. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0098, CAP-0119, CAP-0018, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Limitare a modalità studio ed export, valutare peso
