# Specifiche candidate — CAP-0118

## Scopo

Document Delta: Confronta due versioni dello stesso PDF/testo mettendo in evidenza modifiche puntuali e, se disponibile, differenze di layout.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Confronto versioni documento e differenze verificabili** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Il thread spiega diff testuale/semantico, non fornisce un'app donor: pattern di riferimento; attenzione a OCR e riconciliazione pagine. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
