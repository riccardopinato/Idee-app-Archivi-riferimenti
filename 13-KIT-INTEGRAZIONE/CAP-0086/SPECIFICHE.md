# Specifiche candidate — CAP-0086

## Scopo

Leggere ad alta voce ricordi, guide e ricette con controlli di velocita e ascolto offline.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Sintesi vocale locale di note e contenuti editoriali** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Prima valutare Android TextToSpeech sistema e licenze voci; modelli scaricabili solo opt-in; VoiceStudio AGPL: pattern solo, no code copy closed-source; nessuna imitazione vocale senza consenso.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
