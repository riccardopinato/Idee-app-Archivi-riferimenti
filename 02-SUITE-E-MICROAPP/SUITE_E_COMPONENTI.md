# Suite, micro-app e moduli

> Snapshot di fonte storica al 30 ottobre 2026. Le sigle [E]/[V]/[C]/[R] riportano provenienza, non certificazione corrente. Originale preservato in 90-STORICO.

Legenda aggiornata: 🟢 codice in repo verificato; 🟡 donor storico/parziale; 🔴 non implementato in un prodotto suite verificato. Alcune sezioni restano snapshot storico, con note di audit sotto.
⚠ Una suite 🔴 può contenere donor 🟢. La verifica del 30/10/2026 ha confermato Notification Control e Phone Guard come suite realmente in codice, non Store-ready.

SUITE: NOTIFICATION CONTROL [🟢 SUITE IMPLEMENTATA — repo Notification-Control @ 664cf8c7eaaa8843711ddc99b62b547a1997fcb9; release live/Play pending]
 🟢 Notification Undo — storico notifiche cancellate; vendibile standalone.
 🟢 Pausa Ping — silenziamento temporaneo; standalone opzionale.
 🟢 Follow Up Reminder — notif→promemoria; standalone.
 🟢 Critical Message Alert — alert distinti per priorità; standalone.
 🟢 Pickup Code Pin — codice di ritiro in evidenza; principalmente modulo.
 🟢 Luminous Visual Alerts — presente come modulo in codice Notification Control; donor storico Luminous Infinite Circle.

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

SUITE: PHONE GUARD [🟢 SUITE IMPLEMENTATA — repo Phone-Guard @ ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c; v0.9.7, physical Play QA pending]
 🟢 Tabletop Motion Alarm — motion alarm con countdown/sensori; standalone.
 🟢 Pocket Guard — protezione tasca/borsa sensori; standalone.
 🟢 Journey Guard — modalità viaggio effettivamente inclusa in Phone Guard, insieme a Table/Pocket/Bag/Charging/Accessory.
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

## AUDIT REPOSITORY DEL 30/10/2026 — ULTERIORI PRODOTTI COMPOSITI E DONOR

**Android Omni Cleaner — 🟢 prodotto composito reale (v1.0.0 RC1).** Accorpa storage scanner, large-file cleaner, duplicate finder, Gallery Cleaner con undo, thumbnail/cache, app residues, Smart Categories dei download/installer/archivi/screenshot, EXIF cleaner e Safe Trash. Fonti: README, PRODUCT_BIBLE e Kotlin `cleaner/` + `exif/`. **Non è CleanOS** e non implementa Easy Debloat.

**TasteAI — 🟢 prodotto multifunzione reale (v0.13).** Ricette offline, ricerca intelligente e Anti-Waste Engine + Ispirami/Preferiti/Plus. Somiglianze con MealMate **non** costituiscono fusione formale. Possibile donor per meal planning futuro.

**PDF-Unifier — 🟢 codice reale; PDF Pocket Tools è proposta di ampliamento.** Merge, split, immagini→PDF, lock, rotate, compression, reader, OCR, bookmarking e search in Kotlin; non trattare il nuovo concept come prodotto già certificato.

**SafeShare — 🟡 donor parziale**: EXIF Cleaner è presente in Omni Cleaner ma non la suite con Clean Link/File Metadata. **Downloads Butler — 🟡 donor parziale**: Smart Categories Omni gestisce anche download vecchi, non dimostra un organizer Butler completo.
