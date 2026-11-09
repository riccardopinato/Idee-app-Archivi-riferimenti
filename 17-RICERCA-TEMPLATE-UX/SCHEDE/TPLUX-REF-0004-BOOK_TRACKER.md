# TPLUX-REF-0004 — Book Tracker (Mindful Setups)

**Evidenza:** E2-EXPORT-STRUCTURE per pagine, colonne e valori esportati, **non per formule/button action interne**. **Consumer principale:** Notes-Ecosistema. **Secondario:** Anna's Diary solo come raccolta/diario letture personali. **Decisione:** RIFERIMENTO UX VALIDO; riuso di pattern con codice e asset originali.

## Struttura effettivamente esaminata
**61 file: 24 Markdown, 14 CSV, 21 JPG, 2 PNG.** Pagine principali: Book Tracker, biblioteca/lista lettura, libri in lettura, librerie/Bookshelves, schede di libri. CSV con Books, Bookshelves, Reading List e Library. Nei campi dei libri compaiono autore, genere, stato, progress, rating, pagina corrente/totale, date di inizio/fine, formato, copertina e collegamento alla libreria; gli scaffali hanno descrizione, conteggio e stato archivio.

La guida incorporata **afferma** che una formula calcola il progresso di lettura e un pulsante 'Mark as Finished' registra fine lettura/stato. Il CSV esportato conferma campi/valori di progresso, **non esporta una prova eseguibile della formula né la configurazione del pulsante**.

## Adattamento proposto
- Notes: template di reading/knowledge library, fonti/annotazioni collegate a note canoniche, statistiche derivate e viste filtered per libri e categorie. Prima verificare `library.dart`, Knowledge/Research Workspace e nessun nuovo catalogo duplicato.
- Anna: solo un futuro diario di letture personale con ricordi collegabili, senza work-management o seconda libreria.

## Licenza BLOCCANTE PER LA RIVENDITA
La pagina del creatore nell'export dichiara **uso personale e divieto di redistribuzione/rivendita non autorizzata**. Non si può inserire questo ZIP, le copertine, il layout identico, le formule o i media originali in uno store commerciale. Ammesso **solo riferimento concettuale / implementazione clean-room originale**, previa verifica di eventuali diritti sulle immagini inserite.

Nessun asset o libro/citazione del template viene caricato nel repository.
