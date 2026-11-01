# Specifiche candidate — CAP-0102

## Scopo

Proporre slot alternativi per task spostabili dopo un imprevisto, conservando eventi fissi, preferenze e possibilita di confrontare due soluzioni.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Ripianificazione assistita e confronto piani alternativi** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Verificare task e calendario canonici; strategia locale con vincoli hard/soft e preview delle modifiche, nessuno spostamento o evento scritto senza conferma; fallback no-AI.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
