# Specifiche candidate — CAP-0128

## Scopo

Form-to-Card: Estrae coppie campo-valore da moduli e fatture in schede modificabili con link al file sorgente.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Estrazione campi da form in schede canoniche** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

FUNSD+ contiene annotazioni form con licenza custom; reference per layout, vietato incorporare dataset senza gate diritti. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
