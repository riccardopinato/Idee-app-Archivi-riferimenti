# Specifiche candidate — CAP-0133

## Scopo

Smart Reading Flow: Ricostruisce ordine di lettura, titoli e sezioni da PDF a piu colonne conservando geometrie e origine.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Ordine di lettura strutturato dei documenti** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

La doc descrive PP-DocLayoutV3; integrarlo e inferenza/progetto distinto dall'OCR. Controllare supporto linguistico e runtime mobile. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
