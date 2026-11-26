# Tre utility pratiche da conservare — 26/11/2026

**Origine:** selezione esplicita dell'utente in chat del 26/11/2026 fra esempi di app a uso concreto.
**Decisione:** **SALVATE / IDEA / DA_VALUTARE**. Non equivalgono a sviluppo approvato, roadmap, nuova CAP, repository, prototipo o mercato validato.
**Obiettivo di selezione:** utilità verificabile nell'uso reale, azione chiave rapida, preferibilmente locale/offline e senza login.
**ID stabili di inbox:** UTIL-20261126-01…03. I nomi sono provvisori.
**Nota deduplicazione:** una sola candidata standalone chiaramente distinta; le altre sono evoluzioni/delta di idee e prodotti già registrati.

## UTIL-20261126-01 — «L'ultima volta che…»
- **Problema:** ricordare l'ultima volta che si è eseguita una manutenzione o controllo domestico/personale periodico (es. pulizia macchina del caffè, filtro cappa, pressione pneumatici).
- **Azione di valore:** apri una scheda e premi **«Fatto oggi»**; l'app registra il completamento, mostra quando è stato fatto e quando farlo ancora.
- **MVP:** schede attività create a mano o da pochi modelli originali; data ultima esecuzione; intervallo giorni/settimane/mesi; prossima scadenza; cronologia minimale; notifiche locali e widget opzionale.
- **Offline-first:** DB locale, backup/esportazione facoltativa; nessun accesso a email, account o contatti.
- **Posizionamento:** **nuova app consumer possibile**, ma prima verificare catalogo HomeFix, Home Assets Passport e reminder già esistenti; non confonderla con agenda generica.
- **Misura di utilità:** completare un'attività in 1 tap; reminder puntuale, senza falsi positivi; prova d'uso per manutenzioni ripetute.
- **Rischi:** poco differenziante da habit tracker; concorrenza, retention, intervalli stagionali e qualità delle notifiche Android da verificare.
- **Stato:** IDEA / DA_VALUTARE, **NON APPROVATA PER LO SVILUPPO**.

## UTIL-20261126-02 — «File pronto da inviare»
- **Problema:** portali, moduli o siti richiedono foto/documenti in formato e dimensione specifici (es. JPG massimo 2 MB); l'utente deve cercare diversi strumenti.
- **Azione di valore:** dal menu **Condividi** Android, scegli file → tipo e limite → genera copia pronta da caricare/condividere senza alterare originale.
- **MVP:** target JPG/PNG (quando compatibile), limite dimensione in MB, ricompressione/downscale progressivo con anteprima dimensione e qualità, output locale e condivisione tramite Android Sharesheet; gestione di errori e metadati.
- **Limiti da esplicitare:** nessuna promessa di rispettare qualsiasi limite senza compromettere leggibilità; trasparenza su EXIF, privacy e su conversione PDF se in scope futuro.
- **Posizionamento:** **prima valutare come funzione per PDF-Unifier o Android Omni Cleaner** / possibile evoluzione del candidato FileFlow Kit, evitando un prodotto duplicato.
- **Misura di utilità:** da file ricevuto a file idoneo in meno di 30 secondi, con nessuna perdita dell'originale.
- **Rischi:** differenziazione vs converter esistenti, elaborazione grandi file, qualità, Android URI permissions, gestione errori.
- **Stato:** IDEA DI FUNZIONE / DA_VALUTARE, **NON APPROVATA PER L'IMPLEMENTAZIONE**.

## UTIL-20261126-03 — «Dov'è finito?»
- **Problema:** oggetti piccoli e accessori in scatole/cassetti si ritrovano con difficoltà dopo mesi.
- **Azione di valore:** fotografa o registra una scatola, assegna collocazione e parole chiave, cerca poi l'oggetto per trovare la posizione.
- **MVP:** contenitori + luoghi, una o più foto, elenco/etichette manuali di oggetti, ricerca offline per nome/alias, vista rapida posizione; QR fisico opzionale e successivo.
- **Posizionamento:** **NON creare subito nuova app**: è forte sovrapposizione di **BoxFinder** (inventario scatole e QR) e **Home Assets Passport** (suite oggetti/garanzie/manuali). Va annotata come proposta di UX e scope mirato per tali idee, con enfasi su foto + ricerca semplice.
- **Misura di utilità:** identificare un oggetto in pochi secondi senza scandagliare scatole; minimo tempo di inserimento.
- **Rischi:** costo di inventariazione elevato, abbandono dopo setup iniziale, foto senza tag insufficienti per ricerca e OCR/AI non necessari nell'MVP.
- **Stato:** VARIANTE / DA_VALUTARE, **NESSUN NUOVO PRODOTTO APPROVATO**.

## Criteri di una successiva rivalutazione
1. Per ogni candidata dimostrare il caso pratico dall'apertura all'azione finale su Android; applicazione fluida, poca frizione e nessun account per l'uso base.
2. Confrontare prodotti esistenti e **funzioni già registrate** per non ricostruire BoxFinder/FileFlow/Reminder.
3. Definire differenza vendibile, test con utenti esterni e limiti delle API/permessi Android.
4. Solo dopo decisione esplicita dell'utente creare issue, roadmap, nuove CAP o codice.
