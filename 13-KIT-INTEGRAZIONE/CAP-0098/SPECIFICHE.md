# Specifiche candidate — CAP-0098

## Scopo

Mappa mentale interattiva da nodi estratti da note/fonti, con zoom pan e tap che torna all'entita originale senza duplicare lo storage.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Mind map navigabile derivata da note e documenti** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riutilizzare canvas e connettori, audit licenza Vertical.ai; evitare dipendenze RAG cloud o Neo4j introdotte solo per il concept.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
