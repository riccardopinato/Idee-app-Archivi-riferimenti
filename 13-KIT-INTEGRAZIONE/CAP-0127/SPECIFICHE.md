# Specifiche candidate — CAP-0127

## Scopo

Video Chapter Notes: Importa link video e crea note con timestamp e capitoli editabili che rinviano a punti specifici.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Note video navigabili per capitoli e timestamp** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Fonte descrive tutorial YouTube -> guida con timestamp; accesso a transcript, copyright/ToS e disponibilita offline da verificare. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
