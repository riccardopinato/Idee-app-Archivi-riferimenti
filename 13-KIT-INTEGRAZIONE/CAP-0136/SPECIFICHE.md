# Specifiche candidate — CAP-0136

## Scopo

Smart Cutout Canvas: Scontorna oggetti da una foto creando sticker/soggetti mobili per composizioni sulla canvas.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Scontorno foto in elementi canvas riutilizzabili** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Segment Anything WebGPU demo esiste; runtime Android/offline, peso del modello e licenza degli asset da verificare. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
