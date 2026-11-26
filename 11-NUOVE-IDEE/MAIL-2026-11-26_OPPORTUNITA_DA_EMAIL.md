# MAIL-2026-001…010 — Idee ricavate da problemi descritti in email (26/11/2026)

**Stato decisionale: ARCHIVIATE / RINVIATE / NON APPROVATE / PRIORITÀ BASSA.**
**Feedback utente (26/11/2026):** le proposte non convincono molto. Richiesta esclusivamente la conservazione nel catalogo, **non** lo sviluppo, la creazione di nuovi repository o la promozione in roadmap.
**Origine:** analisi tematica, condotta in chat su corrispondenza privata; archiviate soltanto **categorie astratte di problemi**, senza contenuti delle email, indirizzi, dati personali, dettagli di servizi/account riconducibili a una persona, allegati o date di eventi privati.
**Evidenza:** un messaggio commerciale non prova una domanda diffusa. Le comunicazioni operative segnalano scenari reali ma **non** validano mercato, unicità o disponibilità a pagare. Nessuna intervista utente, benchmark di mercato, test su dispositivo, API audit, codice o CAP certificata.
**Naming:** etichette provvisorie, non marchi verificati.

| ID stabile | Nome provvisorio | Bisogno/ipotesi sintetica | MVP ipotetico | Collocazione preferibile | Ostacolo / gate di eventuale rivalutazione |
|---|---|---|---|---|---|
| MAIL-2026-001 | Deadline Radar | Comunicazioni operative con scadenze importanti vengono disperse fra newsletter e messaggi non urgenti | Import volontario di comunicazioni, estrazione data/azione/conseguenza, conferma manuale e reminder locale | Valutare delta rispetto a Notes/task; standalone solo se differenziante | Accesso email e privacy/GDPR, qualità estrazione, falsi positivi, concorrenti già presenti |
| MAIL-2026-002 | RefundGuard | Un reso può avere scadenze, stati e metodi di rimborso difficili da seguire | Registro manuale/ricevuta selezionata, date, stato, metodo di accredito e conferma rimborso | Possibile modulo CashMate | Dati non standard, nessuna integrazione e-commerce garantita, confermare domanda reale |
| MAIL-2026-003 | DevPulse | CI e deployment possono generare notifiche ripetute che nascondono la causa iniziale | Aggregazione read-only di failure, dedup per commit/workflow, deep link ai log | Prima capability App Factory / AppLab, non necessariamente app | Non clonare dashboard esistenti, autenticazione provider, verificare differenziale reale |
| MAIL-2026-004 | GameShelf | Librerie gaming disperse, giochi riscattati e spese difficili da ricostruire | Catalogo manuale/import ricevute, costo per piattaforma, duplicati e backlog | Candidata standalone solo dopo analisi | Competizione elevata, API/disponibilità dati e import parziali, protezione dati acquisto |
| MAIL-2026-005 | SellerDeadline | Piccoli venditori ricevono verifiche, documenti e scadenze su vari canali | Registro scadenze e checklist manuali per venditore, alert local-first | Micro-B2B candidato | Dominio normativo variabile, autenticità degli avvisi, gestione informazioni sensibili |
| MAIL-2026-006 | Backup Guardian | Gli avvisi di cancellazione o indisponibilità dati sono facili da perdere | Inventario backup con data ultimo controllo, test di rilettura, promemoria | Prima valutare riuso Notes / Android Omni Cleaner | Non promettere backup validi senza verifiche, sistemi e permessi differenti |
| MAIL-2026-007 | Subscription Map | Rinnovi e servizi ricorrenti possono essere dimenticati | Elenco abbonamenti, costo annualizzato, promemoria e cancellazione manuale guidata | Preferire estensione CashMate | Categoria affollata; no accesso bancario automatico senza valore e permessi |
| MAIL-2026-008 | TripChange | Conferme, modifiche prenotazione e regole di viaggio sono distribuite fra email | Scheda viaggio, confronto conferme importate, checklist e scadenze | Prima estensione Wonderlog | Evitare duplicazione con app di viaggio esistenti, parsing non affidabile, privacy |
| MAIL-2026-009 | Access Watch | Avvisi di accesso anomalo e incidenti sicurezza richiedono verifiche su siti diversi | Archivio manuale avvisi e checklist di verifica tramite link ufficiali | Ipotesi di utility separata solo dopo threat model | Alto rischio fiducia e phishing; nessuna diagnosi di compromissione basata su email |
| MAIL-2026-010 | Coupon Vault | Codici e buoni promozionali possono scadere inutilizzati | Archivio codici con validità, condizioni inserite manualmente e reminder | Backlog minore, eventuale micro-utility | Valore marginale e saturazione; distinguere offerte reali da marketing |

## Decisione di catalogo
- Tutte le 10 idee sono **RINVIATE / NON APPROVATE** e **priorità bassa**, a prescindere da un precedente giudizio preliminare favorevole in chat.
- Non inserirle nella classifica operativa `DA_VALUTARE.md` delle capability come lavoro immediato: sono ipotesi non ancora ammesse e spesso sovrapposte a prodotti esistenti.
- Non aggiungere CAP, issue di sviluppo, Golden, donor, repo, codice, deploy, Google OAuth o proposte di monetizzazione come impegno.
- Le possibili integrazioni in CashMate, Notes, AppLab, Wonderlog e Android Omni Cleaner sono **solo associazioni da verificare**, non funzionalità mancanti certe.
- Riaprire solo su richiesta dell'utente o con nuove prove: problema ripetuto da utenti terzi, concorrenza, willingness to pay, unicità, perimetro tecnico e requisiti di privacy.

## Tracciabilità
- Fonte primaria non pubblicabile: conversazione utente–assistente del 26/11/2026 e rassegna **privata** di email, non riprodotte.
- Fonte editoriale: ipotesi dell'assistente, non dichiarazioni dei mittenti o autorizzazioni commerciali dei provider.
- Nuovo ingresso: [INBOX_IDEE.md](INBOX_IDEE.md). Non promossa in `01-PORTAFOGLIO`.
