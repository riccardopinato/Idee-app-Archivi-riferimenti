# Specifiche candidate — CAP-0085

## Scopo

Separare gli interventi di piu persone nelle trascrizioni locali con correzione manuale.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Diarizzazione vocale locale per appunti riunioni** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
