# Specifiche candidate — CAP-0114

## Scopo

Privacy Shield: Individua PII nel testo di note/PDF e propone oscuramenti in una copia esportata, conservando l'originale e la scelta per campo.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Redazione PII e privacy copy di note e PDF** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Non certifica copertura IBAN/credenziali o privacy su tutte le lingue; regex locali e NER opzionale, redaction irreversibile sul file esportato. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
