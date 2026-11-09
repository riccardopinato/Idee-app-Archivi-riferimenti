# TPLUX-REF-0005 — Subscription Tracker

**Evidenza:** E2-EXPORT-STRUCTURE (non funzionalità live). **Destinazione primaria suggerita:** CashMate AI / famiglia finanza personale, **non forzare nei cataloghi Notes o Anna**. **Decisione:** UTILE MA FUORI SCOPE CONSUMER ATTUALI.

## Struttura riscontrata
**14 file: 10 Markdown, 3 CSV, 1 MP4.** Database di abbonamenti con sei righe dimostrative; campi di costo, valuta da verificare, cadenza (mensile/settimanale), data prossima scadenza, inizio/cancellazione, auto-rinnovo, stato, fornitore e metodo di pagamento. Pagina Analytics con grafici/indicatori **incorporati via servizio esterno NotionStats**.

Il template stesso richiede campi specifici compilati per corretta analisi, compresa la prossima scadenza e la data di avvio. Le integrazioni grafici esterne, calcoli ricorrenti, reminder e accessibilità non sono stati testati.

## Riusi possibili
**CashMate:** candidato per una vista abbonamenti ricorrenti con previsioni e costo annualizzato, da istruire separatamente nel repository prodotto. Notes può usare solo idea generica di scadenzario se coerente; Anna non deve diventare un gestore finanziario.

## Rischi / limiti
- No dipendenze obbligatorie da NotionStats; nessuna incorporazione dei suoi URL embed o video nel prodotto.
- La struttura esportata non prova il funzionamento del servizio remoto, né la correttezza di calcolo con fusi orari, date non valide e cadenze.
- I dati di pagamento e gli esempi del file non sono riportati nel repository. Nessuna licenza di redistribuzione verificata, solo reference.
