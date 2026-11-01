# Specifiche candidate — CAP-0122

## Scopo

Table Capture: Estrae griglie e valori da tabella fotografata o PDF in celle modificabili con evidenza dei campi incerti.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Estrazione di tabelle strutturate da immagini e PDF** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Paper2Any include extraction di tabelle in PPT, non un modulo Flutter pronto; integrare con CAP-0035 OCR locale e validazione cellule. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
