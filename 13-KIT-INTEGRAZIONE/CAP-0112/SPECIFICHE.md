# Specifiche candidate — CAP-0112

## Scopo

Creare domande/flashcard dalle note di studio e pianificare ripassi a intervalli con fonte originale e statistiche locali.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Flashcard e ripasso dilazionato collegati alle note** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riusare note e pianificatore CAP-0099; SRS deterministico, contenuti modificabili, licenza delle skill esterne da verificare; nessun modello AI pesante bundled.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
