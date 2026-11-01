# Specifiche candidate — CAP-0140

## Scopo

Image Authenticity Inspector: Visualizza aree potenzialmente manipolate di un'immagine, con incertezza e limiti della classificazione.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Analisi forense non conclusiva delle immagini** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

DetectiveSAM ha licenza dichiarata other; non importare/copiare senza chiarimento. Le evidenze di manipolazione non certificano originalita o intenzione. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
