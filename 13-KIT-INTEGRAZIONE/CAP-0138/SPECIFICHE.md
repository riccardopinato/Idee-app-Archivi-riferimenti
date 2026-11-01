# Specifiche candidate — CAP-0138

## Scopo

Audio-Linked Ink: Collega ogni tratto scritto sulla canvas al timestamp della registrazione audio per navigare la lezione.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Ink sincronizzato al tempo di una registrazione** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

MOSS supporta ASR con timestamp; la sincronizzazione stroke-audio puo essere deterministica ed e proposta indipendente. Consenso registrazione obbligatorio. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
