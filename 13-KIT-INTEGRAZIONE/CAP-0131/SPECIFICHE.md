# Specifiche candidate — CAP-0131

## Scopo

Math Ink: Riconosce formule manoscritte o fotografate e le converte in LaTeX modificabile e verificabile.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Riconoscimento formule a mano e conversione LaTeX** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Re-host MIT di RapidLatexOCR, circa 179 MB ONNX: modello on-demand eventuale, non nell'APK; audit peso e accuratezza. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
