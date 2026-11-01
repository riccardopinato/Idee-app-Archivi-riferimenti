# Specifiche candidate — CAP-0106

## Scopo

Confrontare ore disponibili, task stimate e riunioni per giorno/settimana, evidenziando collisioni e intensita in heatmap.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Rilevamento sovraccarico e heatmap riunioni** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Audit calendar provider, permessi, CAP-0001 e CAP-0101; calcolare solo su dati disponibili e consenso, evitare falsa precisione su durata task e false promesse di sync.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
