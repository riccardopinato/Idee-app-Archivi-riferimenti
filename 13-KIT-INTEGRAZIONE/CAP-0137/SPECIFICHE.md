# Specifiche candidate — CAP-0137

## Scopo

3D Memory Objects: Da una foto produce un oggetto 3D ruotabile associato a una nota, con origine media preservata.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Oggetti 3D da fotografie collegati alle note** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Stable Fast 3D Space esiste, ma infrastruttura, licenze commerciali e risorse GPU necessitano gate; non promettere offline. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
