# Suite, micro-app e moduli

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

Legenda: 🟢 donor o codice segnalato; 🔴 nessuno sviluppo dimostrato in questa revisione.
⚠ Una suite 🔴 può contenere donor 🟢. Stato dichiarato come promemoria storico, da verificare su repo alla prossima attivazione.

SUITE: NOTIFICATION CONTROL [🔴 suite da assemblare]
 🔴 Notification Undo — storico notifiche cancellate; vendibile standalone.
 🔴 Pausa Ping — silenziamento temporaneo; standalone opzionale.
 🔴 Follow Up Reminder — notif→promemoria; standalone.
 🔴 Critical Message Alert — alert distinti per priorità; standalone.
 🔴 Pickup Code Pin — codice di ritiro in evidenza; principalmente modulo.
 🟢? Luminous Infinite Circle — visual alert donor/progetto definito; verificare codice prima di considerarlo realmente riusabile.

SUITE: APP PROFILES [🔴 suite da assemblare]
 🔴 App Brightness / Brightness Profiles — luminosità per app; standalone.
 🔴 Rotation Profiles — orientamento per app; standalone.
 🔴 Screen Awake Profiles — schermo sempre acceso per app; standalone.
 🔴 Bluetooth Volume Memory — volume per device; standalone.
 🔴 Public Audio Guard — prevenzione suoni inattesi; modulo.
 🔴 Music Focus — profili media/focus; modulo.
 🔴 Calendar Auto-Mute — silenzioso da calendario; valutare standalone.
 🔴 Silent Timer — temporizzazione silenzioso; valutare standalone.
 🔴 DisplayPilot — fusione nella suite, NON terza implementazione.
 🔴 SoundPilot — fusione nella suite, NON terza implementazione.
 🟢 180FlipCharge engine — codice in progetto dedicato; donor, standalone autonomo.

SUITE: CLEANOS [🔴 suite da assemblare]
 🟢 Easy Debloat — debloat/disabilita app OEM, donor Kotlin/Compose, Shizuku già testato storicamente; standalone forte.
 🔴 OEM Ad Shield — ridurre raccomandazioni/pubblicità OEM per modelli supportati.
 🔴 App Control — stop, freeze/disable con privilegi disponibili.
 🔴 Kill Current App — microcomando, solo modulo.
 🔴 Local Wireless ADB bridge/pairing — candidato senza app Shizuku obbligatoria; Android 11+, pairing utente, mai asserire funzionamento già realizzato.

SUITE: SAFESHARE [🔴]
 🔴 Clean Link — elimina parametri tracking URL; standalone.
 🔴 ShareSafe — flusso condivisione protetta; possibile standalone.
 🔴 Photo Metadata Cleaner — elimina EXIF/GPS foto; standalone.
 🔴 File/PDF Metadata Cleaner — metadati documenti; possibile standalone.

SUITE: PHONE GUARD [🔴]
 🟢 Tabletop Motion Alarm — motion alarm con countdown/sensori; standalone.
 🟢 Pocket Guard — protezione tasca/borsa sensori; standalone.
 🔴 Journey Guard — modalità viaggio, attenzione possibili componenti nel donor Pocket: verificare prima di dichiararla assente.
 🔴 Pocket Drop Alarm — rilevamento caduta/estrazione; possibile standalone.

SUITE: DOWNLOADS BUTLER [🔴]
 🔴 Download Organizer — organizza file per categoria; standalone.
 🔴 Downloads Cleaner — pulizia file download; standalone.
 🔴 TempBox — file temporanei ed expiry; modulo o standalone.

SUITE: PURCHASE GUARD [🔴]
 🔴 Receipt & Warranty Guard — ricevute/garanzie; standalone.
 🔴 Subscription Guard — rinnovi/abbonamenti; standalone.
 🔴 Trial Reminder — prova gratuita in scadenza; modulo.
 🔴 Return Reminder — termine resi; modulo.

SUITE: RESOURCE WATCH [🔴]
 🔴 Storage Growth Watch — quale app cresce nello storage; standalone condizionata a permessi Android.
 🔴 Data Hog Guard — traffico dati per app; standalone condizionata a visibilità Android.
 🔴 App Usage Snapshot — uso app; principalmente modulo.

SUITE: SENIOR SAFE HOME [🔴]
 🔴 Senior Home — launcher accessibile.
 🔴 Big Contacts — chiamate/contatti con foto e pulsanti grandi; standalone.
 🔴 Sono Arrivato — avvisa contatto di arrivo; modulo.
 🔴 Scam Call Warning — segnala rischio call center/truffa; standalone possibile e policy sensibile.
 🔴 Call Me Back — richiamo/promemoria; modulo condiviso con Call Companion.

SUITE: HANDOFF MODE [🔴]
 🔴 Single Photo Lock — mostra una sola foto, non galleria; standalone.
 🔴 Touch Lock — blocco tocchi/gesture; standalone.
 🔴 Temporary HandOff — prestito controllato dispositivo; core suite.

SUITE: KID MODE [🔴]
 🔴 Kids App Lock — limita accesso a specifiche app.
 🔴 Screen Time Traffic Light — semaforo tempo schermo.
 🔴 Touch Lock — RIUSO unico motore dalla famiglia HandOff.
 🔴 Chore Button — checklist compiti.
 🔴 School Bag Check — checklist zaino.
 🔴 Wake Up Routine Kids — routine mattutina.

SUITE: CALL COMPANION [🔴]
 🔴 Missed Call Reminder — richiamare chiamata persa; standalone possibile.
 🔴 Post-call Notes — nota dopo chiamata; modulo.
 🔴 Follow-up Call — richiamo in data futura; modulo.

SUITE: CURAVESTITI [🔴]
 🔴 SmacchiaFacile — trattamento macchie per tessuto.
 🔴 Lavatrice Facile — programma/cura lavaggio.
 🔴 Care Symbols — spiegazione simboli etichette.

SUITE: HOMEFIX [🔴]
 🔴 Casa SOS — checklist primo controllo problema domestico.
 🔴 Pronto Casa — identificare quando serve professionista.
 🔴 Papà Fai Da Te — manutenzione base, con limiti di sicurezza.

SUITE: MEALMATE [🔴]
 🔴 Cosa cucino stasera? — suggerimenti con ingredienti disponibili.
 🔴 Anti-Spreco — priorità alimenti vicini a scadenza.
 🔴 Quantity Calculator — porzioni/quantità.
 🔴 Random Dinner — scelta pasto casuale.
 🔴 Weekly Meal Planner — pianificazione settimana.

PRINCIPIO DI PACKAGING
- Un solo package di librerie/core per ciascuna famiglia; N shell/app distinte con propri package name, signing, store listing, analytics e billing.
- Acquisti di una standalone NON sbloccano automaticamente la suite: eventuale cross-upgrade richiede contratto commerciale e verifica billing/store.
- Se un modulo introduce permessi invasivi, non includerli automaticamente nelle altre standalone.
- Store listing non duplicati: ogni app deve avere funzione principale e valore completi, non una facciata del medesimo prodotto.

====================================================================
