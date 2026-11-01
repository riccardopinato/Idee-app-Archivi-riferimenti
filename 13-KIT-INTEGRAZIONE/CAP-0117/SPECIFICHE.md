# Specifiche candidate — CAP-0117

## Scopo

Sketch-to-Diagram: Converte un diagramma disegnato a mano in box, etichette e frecce editabili dentro la canvas.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Da diagramma a grafo editabile sulla canvas** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Q4 circa 529 MB + vision encoder circa 205 MB, quindi non nell'APK base; proof su diagrammi italiani e licensing. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
