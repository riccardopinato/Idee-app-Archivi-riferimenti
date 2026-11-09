# Protocollo ricerca, evidenza e privacy

## 1. Fonti ammissibili
- **E0 / titolo o descrizione commerciale**: serve per *candidate UX*, mai per dichiarare implementazione o disponibilità in una versione free.
- **E1 / pagina pubblica attribuita e verificata**: permette di discutere solo ciò che è pubblicizzato, distinguendo varianti, date e limitazioni.
- **E2 / file realmente autorizzato ed esaminato**: export Markdown/CSV, screenshot o manuale ottenuto dal legittimo titolare; documentare struttura reale, elementi grafici, formule, relazione e variante.
- **E3 / codice sorgente di un donor con licenza verificata**: solo qui può nascere un donor di codice, con SHA, file, test e gate; per i template commerciali normalmente si resta in reference-only.

## 2. Procedura completa per ogni fonte
1. Registrare ID stabile nel **catalogo privato**, nome/variante, data, origine, prova e revisioni.
2. Confrontare il prodotto con tutti i record e bundle: distinguere duplicato, nuova variante o prodotto differente.
3. Esaminare contenuto consentito: blocchi, database, relazioni, proprietà/formule, navigazione, colori, responsive, iconografia, accessibilità, stati empty/error.
4. Tracciare separatamente funzionalità dichiarate, osservate in screenshot, verificate dentro l'export e testate nel consumer.
5. Collegare alle classi e ai file esistenti di Notes/Anna; classificare: **ESISTE**, **PARZIALE**, **NON VERIFICATO**, **MANCANTE CON PROVA**, **FUORI PRODUCT BIBLE**.
6. Proporre **REUSE FIRST**: singola capability con due adapter UX, oppure NO-OP/RINVIA/SCARTA.
7. Prima di una futura PR applicativa: specifica, migrazione e contratto dati, test di permessi, test web e review esatta, quindi eventuale gate prodotto.
8. Non trasformare contenuto recuperato per ricerca in asset redistribuibile.

## 3. Acquisizione autorizzata
- Usare ricevute possedute, esportazioni ufficiali richieste al provider, download normali permessi dalla licenza e manuali/file forniti dall'utente.
- Per i template Notion duplicati in un workspace autorizzato: `••• → Export → Markdown & CSV` o `HTML`; impostare **Include subpages** quando appropriato. I database esportano CSV, e alcune strutture (es. callout) hanno conversioni non lossless: [guida ufficiale Notion](https://www.notion.com/help/export-your-content).
- I [termini Gumroad](https://gumroad.com/terms), sezione 14, proibiscono l'uso di software o processi manuali/automatici per effettuare scraping delle pagine del servizio, salvo l'eccezione descritta per i motori di ricerca pubblici. Non automatizzare il crawling della libreria o il download attraverso scraping.
- Nessuna password, cookie sessione, URL con token, dati di pagamento o download riservato in issue o repo pubblico.

## 4. Privacy e proprietà intellettuale
Il repository pubblico può contenere SOLO **pattern generici, link pubblici, benchmark consentiti e proposte astratte**. Non pubblicare liste personali di acquisti, email, ricevute, ordini, prezzi individuali o asset dei template. Per fonti commerciali: **REFERENCE / CLEAN-ROOM IMPLEMENTATION**; disegni, font, foto, formule proprietarie e testi non sono automaticamente riutilizzabili.

## 5. Condizioni di chiusura
La fase di *inventario completo* richiede confronto con un export/lista ufficiale della libreria reale. Il numero di prodotti rilevati in ricevute non è prova di copertura al 100%. L'audit delle **grafiche vere** richiede immagini/export dei template specifici. Segnare sempre gli elementi non accessibili senza saltarli.
