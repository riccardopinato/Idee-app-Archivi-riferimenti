# Specifiche candidate — CAP-0091

## Scopo

Ricreare una vista di mappa con gli stessi layer e posizione di camera su un altro dispositivo.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Snapshot condivisibile della vista mappa senza dati privati** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Distinguere view state (camera, zoom, layers) da percorso/ricordi privati; share URL/file su azione volontaria, nessuna chiave API, token o posizione personale inclusa.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
