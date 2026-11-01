# Specifiche candidate — CAP-0103

## Scopo

Visualizzare task con prerequisiti, segnalare cosa le blocca e riconciliare archi con relazioni canoniche.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Grafo delle dipendenze e blocker delle task** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Audit CAP-0096 e canvas CAP-0028; relazioni no-cicli, cancellazione/ripristino, undo, accessibilita e filtri; il donor Yuga modella dipendenze in forma sequenziale.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
