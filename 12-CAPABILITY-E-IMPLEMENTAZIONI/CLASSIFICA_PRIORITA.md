# Classifica capability — snapshot 2026-11-01

**Ranking tecnico-editoriale relativo, NON approvazione di roadmap.** P1: >=92, P2: 79–91, P3: <79. P0 e riservato ai veri incidenti di sicurezza/dati, non alla ricerca di idee.

| # | ID | Capability | Ambito | Score | Classe | App interessate | Prossima verifica |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [CAP-0037](REGISTRO_CAPABILITY/CAP-0037.md) | Operazioni PDF split merge rotate lock | pdf | 98 | P1 | PDF-Unifier, Notes-Ecosistema, PDF-Pocket-Tools | Verificare motore originale licenza e compatibilita Flutter |
| 2 | [CAP-0039](REGISTRO_CAPABILITY/CAP-0039.md) | EXIF privacy safe copy | privacy | 98 | P1 | Android-Omni-Cleaner, app-fotografia, Send-to-pc, SafeShare | Niente modifica di originali e UI attributi rimossi |
| 3 | [CAP-0015](REGISTRO_CAPABILITY/CAP-0015.md) | Ricerca globale ordinabile e un carattere | ricerca | 95 | P1 | Agenda-per-Anna, Notes-Ecosistema | Source gate riportati PASS ma verificare smoke Android |
| 4 | [CAP-0044](REGISTRO_CAPABILITY/CAP-0044.md) | Ricette anti-spreco da ingredienti | ricette | 95 | P1 | TasteAI, In-Cucina-con-gli-Anime, MealMate | Non clonare TasteAI; validare differenziazione |
| 5 | [CAP-0017](REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | data-safety | 94 | P1 | Agenda-per-Anna, Notes-Ecosistema, Wonderlog, CamperBoss | Regression entita-per-entita e file orfani; niente duplicazione lifecycle |
| 6 | [CAP-0022](REGISTRO_CAPABILITY/CAP-0022.md) | Localizzazione cinque o piu lingue | fondazione | 94 | P1 | Agenda-per-Anna, World-Days, app-fotografia, In-Cucina-con-gli-Anime | Controllare parita lingua in native notifications |
| 7 | [CAP-0042](REGISTRO_CAPABILITY/CAP-0042.md) | Catalogo editoriale multilingua offline | editoriale | 94 | P1 | app-fotografia, World-Days, In-Cucina-con-gli-Anime | Riusare pattern non mescolare dati editoriali di prodotti differenti |
| 8 | [CAP-0055](REGISTRO_CAPABILITY/CAP-0055.md) | Notifiche affidabili e diagnostics truth | notifiche | 94 | P1 | Agenda-per-Anna, World-Days, Notification-Control | Permesso non equivale consegna reale |
| 9 | [CAP-0065](REGISTRO_CAPABILITY/CAP-0065.md) | Routine wearable e battery optimization audit | qualita | 94 | P1 | Phone-Guard, Battery_Guard, FocuSense | Test OEM reale multi dispositivo e Doze |
| 10 | [CAP-0067](REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | devops | 94 | P1 | Agenda-per-Anna, AppLab, Battery_Guard | Artifact build non e device certification |
| 11 | [CAP-0077](REGISTRO_CAPABILITY/CAP-0077.md) | Health check permessi nativi per-capability | devops | 94 | P1 | Phone-Guard, TrailPath, Battery_Guard, Agenda-per-Anna | Permesso concesso non prova capability operativa |
| 12 | [CAP-0053](REGISTRO_CAPABILITY/CAP-0053.md) | Sun Moon calcolo locale | geografia | 93 | P1 | app-fotografia, TrailPath, CamperBoss, WEB-012 | Calcolo locale SunCalc con timezone corretto |
| 13 | [CAP-0035](REGISTRO_CAPABILITY/CAP-0035.md) | OCR immagini e documenti on device | ocr | 92 | P1 | PDF-Unifier, Notes-Ecosistema, Agenda-per-Anna, BeerClass-AI | Audit licenza ML Kit e processi media originali |
| 14 | [CAP-0073](REGISTRO_CAPABILITY/CAP-0073.md) | AdMob UMP consent gating | monetizzazione | 92 | P1 | World-Days, In-Cucina-con-gli-Anime, Battery_Guard | Test permessi consent e policy store |
| 15 | [CAP-0001](REGISTRO_CAPABILITY/CAP-0001.md) | Pianificazione di slot liberi | agenda | 91 | P2 | Agenda-per-Anna, FocuSense | Verificare conflitti e non spostare eventi fissi |
| 16 | [CAP-0028](REGISTRO_CAPABILITY/CAP-0028.md) | Connettori visuali tra post-it | canvas | 91 | P2 | Notes-Ecosistema | Riutilizzare canvas esistente e salvare soli edge |
| 17 | [CAP-0018](REGISTRO_CAPABILITY/CAP-0018.md) | Backup restore con staging e rollback | data-safety | 90 | P2 | Agenda-per-Anna, Notes-Ecosistema, CamperBoss | Audit formati e test corrupt archive per consumer |
| 18 | [CAP-0027](REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | organizzazione | 90 | P2 | Notes-Ecosistema, Agenda-per-Anna, Wonderlog | Android share intent e consenso senza import occulto |
| 19 | [CAP-0034](REGISTRO_CAPABILITY/CAP-0034.md) | OCR scontrino e parsing spese | ocr | 90 | P2 | CashMate-AI, In-Cucina-con-gli-Anime, BeerClass-AI | OCR locale poi conferma prima di transazione |
| 20 | [CAP-0068](REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | devops | 90 | P2 | AppLab, Agenda-per-Anna, CamperBoss | Mai inferire device PASS da CI |
| 21 | [CAP-0071](REGISTRO_CAPABILITY/CAP-0071.md) | Offline content packs incremental sync | fondazione | 90 | P2 | World-Days, CamperBoss, Notes-Ecosistema | Licenze e hashing versioni pack |
| 22 | [CAP-0023](REGISTRO_CAPABILITY/CAP-0023.md) | Design System Flutter token-first | design | 89 | P2 | Design-App, Agenda-per-Anna, Wonderlog | Riuso pattern non diventa Golden automaticamente |
| 23 | [CAP-0025](REGISTRO_CAPABILITY/CAP-0025.md) | Schermate responsive rail e split view | design | 89 | P2 | Design-App, Agenda-per-Anna, app-fotografia | No claim desktop full prima di QA multi-width |
| 24 | [CAP-0013](REGISTRO_CAPABILITY/CAP-0013.md) | Collection e ricerca locale | memorie | 88 | P2 | Agenda-per-Anna, Notes-Ecosistema | Verificare performance e origine dei risultati |
| 25 | [CAP-0016](REGISTRO_CAPABILITY/CAP-0016.md) | Inbox con categorie modificabili | organizzazione | 88 | P2 | Agenda-per-Anna, Notes-Ecosistema | Smoke fisico categoria vuota riavvio e sync |
| 26 | [CAP-0020](REGISTRO_CAPABILITY/CAP-0020.md) | Shared Ecosystem Bridge COPY LINK | integrazione | 88 | P2 | Agenda-per-Anna, Wonderlog, Notes-Ecosistema, TrailPath | Verificare roundtrip reale e contratti consumer per versione |
| 27 | [CAP-0047](REGISTRO_CAPABILITY/CAP-0047.md) | POI offline versionati e provenienza | geografia | 88 | P2 | CamperBoss, TrailPath, Wonderlog | Licenze ODbL provider e freshness; non scaricare tile pubblici |
| 28 | [CAP-0072](REGISTRO_CAPABILITY/CAP-0072.md) | Entitlement RevenueCat provider truth | monetizzazione | 88 | P2 | Agenda-per-Anna, TasteAI, In-Cucina-con-gli-Anime | IAP compliance e no premium unlocked falsely |
| 29 | [CAP-0004](REGISTRO_CAPABILITY/CAP-0004.md) | Overlay calendari esterni read-only | agenda | 87 | P2 | Agenda-per-Anna, Notes-Ecosistema | Verificare Android Calendar Provider e disponibilità Notes |
| 30 | [CAP-0005](REGISTRO_CAPABILITY/CAP-0005.md) | Esportazione esplicita eventi verso calendario | agenda | 87 | P2 | Agenda-per-Anna, Notes-Ecosistema | Verificare provider permessi e intent senza sync bidirezionale |
| 31 | [CAP-0024](REGISTRO_CAPABILITY/CAP-0024.md) | Motion reduced-motion e microinterazioni | design | 87 | P2 | Design-App, Agenda-per-Anna, World-Days | Verifica accessibilita e prestazioni su device |
| 32 | [CAP-0040](REGISTRO_CAPABILITY/CAP-0040.md) | Deduplicazione foto per hash percettivo | foto | 87 | P2 | Android-Omni-Cleaner, Wonderlog, app-fotografia | Verificare algoritmo reale e precisione duplicati quasi identici |
| 33 | [CAP-0002](REGISTRO_CAPABILITY/CAP-0002.md) | Creazione eventi da linguaggio naturale | agenda | 86 | P2 | Agenda-per-Anna, Notes-Ecosistema | Parser EN IT ES FR PT con conferma e timezone |
| 34 | [CAP-0031](REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | voce | 86 | P2 | Agenda-per-Anna, Notes-Ecosistema, Wonderlog | Licenza modello footprint benchmark 5 lingue e download opt-in |
| 35 | [CAP-0041](REGISTRO_CAPABILITY/CAP-0041.md) | Palette da foto e golden hour | foto | 86 | P2 | app-fotografia, World-Days, TrailPath | SunCalc locale e colori originali con file donor verificato |
| 36 | [CAP-0043](REGISTRO_CAPABILITY/CAP-0043.md) | Raccolta fonti contenuti e audit artwork | editoriale | 85 | P2 | In-Cucina-con-gli-Anime, World-Days, app-fotografia | Rispettare copyright e revisioni umane obbligatorie |
| 37 | [CAP-0050](REGISTRO_CAPABILITY/CAP-0050.md) | Riorganizzazione tappe e tempi itinerario | geografia | 85 | P2 | Wonderlog, CamperBoss, TrailPath | Tempi da routing verificato e controllo manuale ordine |
| 38 | [CAP-0052](REGISTRO_CAPABILITY/CAP-0052.md) | Meteo contestuale finestre outdoor | geografia | 85 | P2 | CamperBoss, TrailPath, app-fotografia, GrillBoss | API gratuita meteo non commerciale non usare con Ads |
| 39 | [CAP-0060](REGISTRO_CAPABILITY/CAP-0060.md) | Protezione batteria avvisi e sessioni | batteria | 84 | P2 | Battery_Guard, CamperBoss | Distingue salute stimata da misure disponibili |
| 40 | [CAP-0006](REGISTRO_CAPABILITY/CAP-0006.md) | Lista della spesa privata e condivisa | agenda | 83 | P2 | Agenda-per-Anna, TasteAI | Verificare test v0.71 e riuso senza database condiviso |
| 41 | [CAP-0010](REGISTRO_CAPABILITY/CAP-0010.md) | Ricordi Then and Now | memorie | 83 | P2 | Agenda-per-Anna, Wonderlog | Usare media canonici e consenso foto |
| 42 | [CAP-0057](REGISTRO_CAPABILITY/CAP-0057.md) | Allarme protezione Table Pocket Bag Journey | sicurezza | 83 | P2 | Phone-Guard, Pocket-Guard, Tabletop-Motion-Alarm | Test multi OEM FGS false-positive e batteria |
| 43 | [CAP-0066](REGISTRO_CAPABILITY/CAP-0066.md) | Trasferimento LAN QR HTTPS fidato | file | 83 | P2 | Send-to-pc, Notes-Ecosistema, Wonderlog | Pairing fingerprint HTTPS e test rete locale |
| 44 | [CAP-0011](REGISTRO_CAPABILITY/CAP-0011.md) | Life Threads narrativi | memorie | 82 | P2 | Agenda-per-Anna, Wonderlog | Non introdurre archivio parallelo |
| 45 | [CAP-0045](REGISTRO_CAPABILITY/CAP-0045.md) | Meal plan e spesa derivata | ricette | 82 | P2 | TasteAI, MealMate, Agenda-per-Anna | Lista derivata con consenso e separazione proprieta dati |
| 46 | [CAP-0019](REGISTRO_CAPABILITY/CAP-0019.md) | Store media content addressed e GC | data-safety | 81 | P2 | Agenda-per-Anna, Notes-Ecosistema, CamperBoss | Non uniformare database privacy separati |
| 47 | [CAP-0069](REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | devops | 81 | P2 | Design-App, AppLab, Agenda-per-Anna | Baseline screen e variant certi |
| 48 | [CAP-0078](REGISTRO_CAPABILITY/CAP-0078.md) | Web utility location market provider adapter | web | 81 | P2 | WEB-008, WEB-012, WEB-014, WEB-009 | Lingua diversa dal mercato e diritti provider |
| 49 | [CAP-0029](REGISTRO_CAPABILITY/CAP-0029.md) | Canvas ibrida sketch sotto note | canvas | 80 | P2 | Notes-Ecosistema | Verificare gesto pennello undo save e restore device |
| 50 | [CAP-0051](REGISTRO_CAPABILITY/CAP-0051.md) | Mappe luoghi ricordi condivisi con ponte | geografia | 80 | P2 | Wonderlog, Agenda-per-Anna, TrailPath | Trasporto COPY LINK esplicito e autorizzato |
| 51 | [CAP-0062](REGISTRO_CAPABILITY/CAP-0062.md) | Best Conditions Engine sensori | focus | 80 | P2 | FocuSense, Agenda-per-Anna, SleepMax-Coach | Score sensori non diagnosi e test runtime |
| 52 | [CAP-0063](REGISTRO_CAPABILITY/CAP-0063.md) | Momenti ideali per focus in calendario | focus | 80 | P2 | FocuSense, Agenda-per-Anna | Consenso e niente spostamento eventi involontario |
| 53 | [CAP-0012](REGISTRO_CAPABILITY/CAP-0012.md) | Year in Review deterministico | memorie | 79 | P2 | Agenda-per-Anna, Wonderlog | Non ricostruire funzione gia integrata |
| 54 | [CAP-0048](REGISTRO_CAPABILITY/CAP-0048.md) | Routing sentieri trace snap affidabile | geografia | 79 | P2 | TrailPath, CamperBoss | Test fisico snap a vari zoom e reti |
| 55 | [CAP-0049](REGISTRO_CAPABILITY/CAP-0049.md) | Offline map engine e routing camper | geografia | 79 | P2 | CamperBoss, TrailPath | Validare routing camper reale e non dichiarare vera navigazione offline senza mappe |
| 56 | [CAP-0082](REGISTRO_CAPABILITY/CAP-0082.md) | Deterministic UI design artwork | design | 79 | P2 | World-Days, app-fotografia, Agenda-per-Anna | Non generare asset coperti da diritti |
| 57 | [CAP-0026](REGISTRO_CAPABILITY/CAP-0026.md) | Sound feedback semantico opzionale | design | 78 | P3 | Design-App, FocuSense, Battery_Guard | Controllare silent mode e opzioni accessibilita |
| 58 | [CAP-0036](REGISTRO_CAPABILITY/CAP-0036.md) | Riconoscimento etichette senza barcode | ocr | 78 | P3 | BeerClass-AI, In-Cucina-con-gli-Anime | Conferma manuale prodotto gradazione ingredienti |
| 59 | [CAP-0046](REGISTRO_CAPABILITY/CAP-0046.md) | Ingredienti da foto e confezioni | ricette | 78 | P3 | In-Cucina-con-gli-Anime, TasteAI | OCR poi conferma attributi e nessuna promessa nutrizionale |
| 60 | [CAP-0076](REGISTRO_CAPABILITY/CAP-0076.md) | Web Clip sicuro con provenienza | organizzazione | 78 | P3 | Notes-Ecosistema, Agenda-per-Anna | Permissions share sheet e URL originale |
| 61 | [CAP-0080](REGISTRO_CAPABILITY/CAP-0080.md) | Document expiry and asset passport | documenti | 78 | P3 | CamperBoss, Notes-Ecosistema, Home-Assets-Passport | Non includere segreti/identita in archivio condiviso |
| 62 | [CAP-0003](REGISTRO_CAPABILITY/CAP-0003.md) | Preparazione contestuale appuntamento | agenda | 77 | P3 | Agenda-per-Anna, Notes-Ecosistema | Riutilizzare reminder e note senza nuovo scheduler |
| 63 | [CAP-0007](REGISTRO_CAPABILITY/CAP-0007.md) | Scheda workout e storico multisport | agenda | 77 | P3 | Agenda-per-Anna, FocuSense | Non creare doppio diario allenamenti |
| 64 | [CAP-0009](REGISTRO_CAPABILITY/CAP-0009.md) | Ricordi mappa geolocalizzata | memorie | 77 | P3 | Agenda-per-Anna, Wonderlog | Verificare permessi e nessuna condivisione GPS implicita |
| 65 | [CAP-0061](REGISTRO_CAPABILITY/CAP-0061.md) | Smart ETA e idle drain batteria | batteria | 77 | P3 | Battery_Guard | Verificare contro scarica reale in standby |
| 66 | [CAP-0033](REGISTRO_CAPABILITY/CAP-0033.md) | Modello Needle 3 on demand Plus | ai-locale | 76 | P3 | Notes-Ecosistema, TasteAI | Play delivery benchmark e entitlement non auto concesso |
| 67 | [CAP-0054](REGISTRO_CAPABILITY/CAP-0054.md) | Prezzi carburanti ufficiali | geografia | 76 | P3 | CamperBoss, WEB-002, WEB-009 | Dati nazionali diritti timestamp e valuta |
| 68 | [CAP-0056](REGISTRO_CAPABILITY/CAP-0056.md) | Notification listener multi-modulo | notifiche | 76 | P3 | Notification-Control, Phone-Guard | Non accedere a messaggi privati fuori scopo |
| 69 | [CAP-0008](REGISTRO_CAPABILITY/CAP-0008.md) | Import foto PDF delle schede workout | documenti | 75 | P3 | Agenda-per-Anna, PDF-Unifier | Verificare parser e conservazione file originale |
| 70 | [CAP-0014](REGISTRO_CAPABILITY/CAP-0014.md) | Cattura rapida contestuale da calendario | memorie | 75 | P3 | Agenda-per-Anna, Wonderlog | Conversione evento a ricordo sempre esplicita |
| 71 | [CAP-0021](REGISTRO_CAPABILITY/CAP-0021.md) | QR inviti condivisi 24 ore | condivisione | 75 | P3 | Agenda-per-Anna, Wonderlog | Serve prova camera e 2 account su device distinti |
| 72 | [CAP-0030](REGISTRO_CAPABILITY/CAP-0030.md) | Professional Wallet CV attestati QR vCard | documenti | 75 | P3 | Notes-Ecosistema, PDF-Unifier | Integrare Document Workspace senza wallet parallelo |
| 73 | [CAP-0038](REGISTRO_CAPABILITY/CAP-0038.md) | PDF Pocket Tools packaging standalone | pdf | 75 | P3 | PDF-Pocket-Tools, PDF-Unifier | Non creare secondo motore per packaging |
| 74 | [CAP-0075](REGISTRO_CAPABILITY/CAP-0075.md) | Import Center per migrazioni utenti | data-safety | 74 | P3 | Agenda-per-Anna, Notes-Ecosistema | Import validato e non perdere storico |
| 75 | [CAP-0032](REGISTRO_CAPABILITY/CAP-0032.md) | Indicizzazione ricerca semantica locale | ricerca | 73 | P3 | Notes-Ecosistema, TasteAI, Agenda-per-Anna | Modello multilingue licenza footprint e benchmark; non inserire pack base |
| 76 | [CAP-0064](REGISTRO_CAPABILITY/CAP-0064.md) | Sonno routine e reminder adattivi | benessere | 73 | P3 | SleepMax-Coach, Agenda-per-Anna | Non formulare diagnosi mediche |
| 77 | [CAP-0081](REGISTRO_CAPABILITY/CAP-0081.md) | Phone protection sensitivity adviser | sicurezza | 73 | P3 | Phone-Guard, Pocket-Guard | False-positive risk e test sensori reali |
| 78 | [CAP-0059](REGISTRO_CAPABILITY/CAP-0059.md) | ADB Shizuku debloat reversibile | android | 72 | P3 | Easy-Debloat, CleanOS | Conferma dispositivo e backup package actions no root claim |
| 79 | [CAP-0058](REGISTRO_CAPABILITY/CAP-0058.md) | Quick settings overlay rotazione 180 | android | 71 | P3 | 180FlipCharge, App-Profiles | Permessi overlay e specialUse Play policy |
| 80 | [CAP-0070](REGISTRO_CAPABILITY/CAP-0070.md) | AppLab autonomous bounded repair | devops | 70 | P3 | AppLab | Politica fail closed P0/P1 e review |
| 81 | [CAP-0074](REGISTRO_CAPABILITY/CAP-0074.md) | Companion voice note organizer | voce | 67 | P3 | Notes-Ecosistema, Agenda-per-Anna | No duplicare trascrizione vocale offline |
| 82 | [CAP-0079](REGISTRO_CAPABILITY/CAP-0079.md) | Report fiscale stipendi mercati separati | web | 67 | P3 | WEB-004, Work-Time-Keeper | Fonte fiscale ufficiale e data annuale |

Il ranking NON usa metriche economiche reali; la priorita finale spetta alla roadmap della singola app.
