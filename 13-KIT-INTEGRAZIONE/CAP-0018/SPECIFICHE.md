# Specifiche candidate — CAP-0018

## Scopo

Ripristino validato e rollback safe

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Backup restore con staging e rollback** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Audit formati e test corrupt archive per consumer

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
