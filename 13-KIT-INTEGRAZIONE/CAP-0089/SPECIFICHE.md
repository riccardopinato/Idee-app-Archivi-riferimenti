# Specifiche candidate — CAP-0089

## Scopo

Tracciare prove e tentativi per decidere se una nuova capability migliora un prodotto.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Registro locale esperimenti con ipotesi e risultato** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riutilizzare evidence/versioning AppLab e Git; nuovi record solo per ipotesi, misura, input baseline, output e decisione, senza seconda authority CI o agent runtime.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
