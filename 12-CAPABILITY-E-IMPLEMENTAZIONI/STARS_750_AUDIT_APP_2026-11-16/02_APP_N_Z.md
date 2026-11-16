# Audit specifico per app — blocco N–Z, 16 novembre 2026

**P** priorità e urgenza sulla scala 0–100; **F** fattibilità tecnica 0–100. Non probabilità né stime di test superati. `GATE` indica affidabilità, QA o release da chiudere; `RIUSO` usa fonti OSS come benchmark/concept prima di un eventuale license gate; `NUOVA` è funzionalità proposta. Distinguere `main`, PR draft, CI, dispositivo e Store.

Fonte stelle: [classifica 110](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/main/research/CLASSIFICA_CURATA_110_2026-11-16.md). Source of truth delle capability: [REGISTRO_CAPABILITY](../REGISTRO_CAPABILITY.json). Non sono stati eseguiti tutti i test/analisi su dispositivo in questa ricognizione.

## Notes — Ecosistema
Source: [Notes-Ecosistema@22892b336e4587dc2daa1e8df970b873e72e41d7](https://github.com/riccardopinato/Notes-Ecosistema/tree/22892b336e4587dc2daa1e8df970b873e72e41d7) · [README.md](https://github.com/riccardopinato/Notes-Ecosistema/blob/22892b336e4587dc2daa1e8df970b873e72e41d7/README.md).
**Stato documentale:** Flutter local-first 0.56.3; Needle runtime in base e modello circa 35,3 MB on-demand; browser usa shared_preferences_web/localStorage e non replica tutti i moduli; CAP ricche già presenti..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Rendere Web durabile per dataset grandi: migrazione versionata localStorage → IndexedDB/SQLite Web, backup e rollback | **98** | **58** | CAP-0149/0167 | Limitazione esplicita README; non perdere dati browser già salvati |
| GATE | Audit full journey Smart Inbox suggerimento → preview → writer canonico con permessi, undo e account switch | **98** | **74** | CAP-0148 | Verificare il codice finale e test; non generare un secondo inbox/writer |
| RIUSO | Editor Flutter a blocchi e round-trip Markdown da AppFlowy Editor (dual AGPL/MPL) come benchmark | **91** | **66** | CAP-0161 | Adattare editor esistente; gate licensing per-file |
| RIUSO | Canvas note/oggetti vivi e graph relations con AFFiNE, Nodus, tldraw, Excalidraw | **90** | **67** | CAP-0028/0029/0149 | Una sola source of truth; non creare un secondo canvas o store |
| GATE | Needle Plus real-device: sandbox, precisione intents, RAM/latency e recupero pack on-demand | **94** | **64** | CAP-0032 | Distinguere implementazione source dalla validazione su device, billing e AI model delivery |
| NUOVA | Audio-to-note offline opt-in via whisper.cpp con testo editabile e segmentazione | **74** | **53** | CAP-0031/0085 | Modulo scaricabile, consenso microfono, dimensioni APK e protezione privacy |

## Notification Control
Source: [Notification-Control@3a38648f730fff591a85e48b5f4757073adc4663](https://github.com/riccardopinato/Notification-Control/tree/3a38648f730fff591a85e48b5f4757073adc4663) · [README.md](https://github.com/riccardopinato/Notification-Control/blob/3a38648f730fff591a85e48b5f4757073adc4663/README.md).
**Stato documentale:** Android Kotlin; single capture/vault, FTS/Paging3, recovery point cifrato, Rules, Luminous; lane release e AppLab documentate..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Matrix Android/OEM NotificationListenerService: kill, reboot, DND, permessi, process death, dati duplicati | **99** | **63** | CAP-0068 | Cattura notifiche è sensibile e dipende da permessi speciali |
| GATE | Validazione Store e privacy: restricted settings, permessi, retention e recovery di media con limiti Play | **98** | **61** | CAP-0114 | Non passare a broad MediaStore in prod senza policy |
| MIGLIORIA | Audit restore/rollback crittografato dei backup e switching profilo, revisioni Vault e indicatori affidabilità | **94** | **75** | CAP-0068 | Non introdurre una seconda cifratura/DB |
| RIUSO | Riepiloghi locali delle notifiche archiviabili in Notes solo tramite export volontario | **70** | **79** | CAP-0027/0148 | Niente cattura invisibile o condivisione automatica |

## PDF Unifier
Source: [PDF-Unifier@03acc73ad8122a8aac4ee1c728f9875791bb4c49](https://github.com/riccardopinato/PDF-Unifier/tree/03acc73ad8122a8aac4ee1c728f9875791bb4c49) · [README.md](https://github.com/riccardopinato/PDF-Unifier/blob/03acc73ad8122a8aac4ee1c728f9875791bb4c49/README.md).
**Stato documentale:** Utility Android per unione PDF; README minimale: non documenta tutte le funzioni di modifica, quindi proposte da verificare sul codice..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Test PDF uniti: ordine pagine, orientamento, bookmark, dimensioni, password, input malformato e recovery | **97** | **82** | CAP-0068 | Garantire output non corrotto e atomicità |
| MIGLIORIA | Flusso anteprima/riordino/split e conferma prima di sovrascrivere documenti | **87** | **76** | CAP-0023 | Verificare se già presente prima di programmare il nuovo editor |
| RIUSO | Motore redazione dati personali e metadati PDF con copia sicura, non modifica distruttiva | **82** | **57** | CAP-0114 | Risk privacy e librerie PDF da valutare |
| NUOVA | Ricerca/OCR PDF e citazioni collegabili a Notes con export volontario | **70** | **52** | CAP-0122/0119 | Toolchain più pesante; non imporre upload cloud |

## Phone Guard
Source: [Phone-Guard@0586b41ef439b4ac20a834ac74c9c3d8186fa82a](https://github.com/riccardopinato/Phone-Guard/tree/0586b41ef439b4ac20a834ac74c9c3d8186fa82a) · [ROADMAP.md](https://github.com/riccardopinato/Phone-Guard/blob/0586b41ef439b4ac20a834ac74c9c3d8186fa82a/ROADMAP.md).
**Stato documentale:** Kotlin 0.9.7, sei modalità Table/Pocket/Bag/Charging/Accessory/Journey, service owner unico, auto-arm opt-in e sicurezza PIN; physical/OEM gates rimasti..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Collaudo fisico multipiattaforma FGS, screen-off, sensori, vibrazione/sirena e recovery | **99** | **64** | CAP-0068 | No falso positivo o falsa protezione e battery drain |
| GATE | Tuning grace, calibrazione e protezione da allarmi errati quando viene recuperato il telefono | **97** | **71** | CAP-0157 | La UX di owner-check deve restare non bypassabile |
| MIGLIORIA | Health dashboard per profilo e diagnostica locale a semaforo senza controlli aggressivi | **83** | **80** | CAP-0088 | Mostrare capability reali non promesse generiche |
| RIUSO | Differenziare funzioni da Pocket-Guard e Tabletop: estrarre donor solo quando prove E3 | **85** | **79** | CAP-0068 | Evitare tripla manutenzione della stessa detection |

## Pocket Guard / Pockara
Source: [Pocket-Guard@fbe2dbdabe4f6b7c90c12c906b8a48d41dbef6fd](https://github.com/riccardopinato/Pocket-Guard/tree/fbe2dbdabe4f6b7c90c12c906b8a48d41dbef6fd) · [README.md](https://github.com/riccardopinato/Pocket-Guard/blob/fbe2dbdabe4f6b7c90c12c906b8a48d41dbef6fd/README.md).
**Stato documentale:** Android 0.5.2 code 8; Pocket/Bag e Journey Guard con PIN/biometria; commerciale Free/Pro e pacchetto storico compatibile..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | False positives e veri furti simulati: movimento tasca/borsa, trasporto, dispositivi diversi, Doze | **98** | **70** | CAP-0157 | Taratura per dispositivo, test ripetibili con sensibilità e consumo |
| GATE | Aggiornamento firmato da versioni precedenti, Play Billing lifetime e restore senza perdere storia | **96** | **69** | CAP-0068 | Package com.riccardopinato.pocketguard da preservare |
| MIGLIORIA | Scelta modalità assistita con test rapido sensori e diagnostica permission-health | **84** | **81** | CAP-0157 | Valorizzare percorso quotidiano già incluso |
| RIUSO | Consolidare eventuale core detection in Phone Guard come donor verificato, non fusione dei prodotti | **82** | **65** | CAP-0068 | Prodotti diversi, componenti condivisibili ma policy/branding distinti |

## Send to PC
Source: [Send-to-pc@723a13dfc144669589e0a9127d3577433a61677e](https://github.com/riccardopinato/Send-to-pc/tree/723a13dfc144669589e0a9127d3577433a61677e) · [ROADMAP.md](https://github.com/riccardopinato/Send-to-pc/blob/723a13dfc144669589e0a9127d3577433a61677e/ROADMAP.md).
**Stato documentale:** Android rete locale, TLS self-signed con fingerprint, file/text/link bidirezionali, upload resumable e localizzazione sei lingue; production AdMob/physical ancora pendenti..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Collaudo Android ↔ browser su reti reali, router isolati, hotspot, IP change e recovery download grandi | **99** | **67** | CAP-0068 | Non confondere CI HTTP con interoperabilità TLS reale |
| GATE | UX sicurezza TLS: fingerprint leggibile, QR/PIN e warning self-signed spiegati senza bypass silenzioso | **98** | **72** | CAP-0068 | Evita downgrade HTTP o accettazione certificato cieca |
| MIGLIORIA | Batch/clipboard drag-and-drop su PC con recupero progress e checksum visibile | **87** | **75** | CAP-0020 | Estendere sessione esistente, non creare altro server |
| RICERCA | Streaming desktop da Sunshine solo in una nuova categoria prodotto, non nella release trasferimento | **28** | **28** | — | GPU/encoding latenza e licenza molto fuori scope |

## Tabletop Motion Alarm
Source: [Tabletop-Motion-Alarm@04bb247a736289eb85de7506ae7abdd315a72a7b](https://github.com/riccardopinato/Tabletop-Motion-Alarm/tree/04bb247a736289eb85de7506ae7abdd315a72a7b) · [ROADMAP.md](https://github.com/riccardopinato/Tabletop-Motion-Alarm/blob/04bb247a736289eb85de7506ae7abdd315a72a7b/ROADMAP.md).
**Stato documentale:** Kotlin utility premium local-first v1.0.0 code 4, no billing interno; reliability e lean build implementati; locali/release e physical non conclusi..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Test allarme screen-off, movimento e recovery dopo kill/reboot su Pixel/Samsung/Xiaomi | **99** | **69** | CAP-0068 | FGS e sirena devono rispondere su hardware reale |
| GATE | Step7 localizzazione completa IT/EN/ES/DE/FR/PT, notifiche ed errori | **89** | **88** | CAP-0022 | Roadmap indica step non fatto |
| MIGLIORIA | Onboarding e preset sensibilità per tavoli instabili con modalità test | **87** | **79** | CAP-0157 | Separare vibrazioni fisiologiche da tentativi di furto |
| GATE | Store paid app: firma, privacy, FGS specialUse, screenshot e update regression | **94** | **75** | CAP-0068 | Nessun in-app Pro/Billing da duplicare |

## TasteAI
Source: [TasteAI@2e6cb127a081365efe565d5f0b8ad1435c2fe4ba](https://github.com/riccardopinato/TasteAI/tree/2e6cb127a081365efe565d5f0b8ad1435c2fe4ba) · [README.md](https://github.com/riccardopinato/TasteAI/blob/2e6cb127a081365efe565d5f0b8ad1435c2fe4ba/README.md).
**Stato documentale:** Flutter 111 ricette canoniche offline, Anti-Waste grounded, FTS e Google Drive backup opzionale; Needle 3 non incluso in base e provider reali non certificati..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Pipeline PDF ricette: estrazione, normalizzazione, dedup e verifica ingredienti/allergeni/manuale | **97** | **80** | CAP-0042/0155 | Nessuna ricetta generata fuori catalogo verificato |
| MIGLIORIA | Lista della spesa generata da ricette presenti e quantità/porzioni con edit esplicito | **88** | **82** | CAP-0155 | Valore frequenza uso senza cloud |
| MIGLIORIA | Anti-Waste con spiegazione degli ingredienti effettivamente usati, senza presunte scadenze | **85** | **83** | CAP-0155 | Estendere grounded retrieval esistente |
| GATE | Firma/store, Google OAuth, RevenueCat e backup/restore su device; non imporre provider | **94** | **65** | CAP-0068 | Gates produttivi esplicitamente pending |
| RICERCA | Needle 3 intent locale opzionale se supera benchmark e dimensioni app | **62** | **48** | CAP-0032 | Non duplicare AI fallback già deterministico |

## TrailPath
Source: [TrailPath@74a5cf87d0be55900d9be318af53972643eebd32](https://github.com/riccardopinato/TrailPath/tree/74a5cf87d0be55900d9be318af53972643eebd32) · [README.md](https://github.com/riccardopinato/TrailPath/blob/74a5cf87d0be55900d9be318af53972643eebd32/README.md).
**Stato documentale:** Flutter 0.9.15 build 27, planner route/GPS/offline; dichiarati fallimenti routing espliciti; vari rami Pro/Sync v1.x ancora draft o non main..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Rilevare e correggere cause routing fallito e percorsi deviati: provider, snap, percorso breve, trace | **100** | **53** | CAP-0048 | P0 core prodotto, provare su tracce e dati stradali reali |
| GATE | GPS fisico e persistenza track/GPX con Doze, background, riavvio e rete intermittente | **99** | **61** | CAP-0048 | CI emulator non prova accuratezza di percorso |
| GATE | Download offline region e versionamento tile: verifica integrità, progress, resume e recupero spazio | **96** | **67** | CAP-0048 | No linee rette silenziose in fallback |
| MIGLIORIA | Riorganizzare i cinque controlli circolari, layout 320–390px, safe area e gesture accessibili | **94** | **90** | CAP-0023 | Feedback layout noto: fix circoscritto |
| GATE | Verificare SKU Pro e entitlement solo quando PR/branch è confluito e source freeze è chiusa | **91** | **66** | CAP-0068 | Non dichiarare Pro attivo dal draft |

## Wonderlog
Source: [Wonderlog@85a6fbcc914224b6753d9e405cc8fbc2e4d40cc6](https://github.com/riccardopinato/Wonderlog/tree/85a6fbcc914224b6753d9e405cc8fbc2e4d40cc6) · [ROADMAP.md](https://github.com/riccardopinato/Wonderlog/blob/85a6fbcc914224b6753d9e405cc8fbc2e4d40cc6/ROADMAP.md).
**Stato documentale:** Flutter nuovo baseline, legacy Kotlin donor; Life Bridge COPY/LINK provato fisicamente, ma cutover/mappa offline/cloud non dichiarati Store-certified..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Parità Flutter rispetto legacy: import/upgrade, media, mappe, note e lossless sync con dati reali | **99** | **64** | CAP-0020 | Non chiudere la migrazione per sola CI |
| GATE | Offline map caching/routing e ripresa dopo background senza rete su dispositivo | **96** | **65** | CAP-0048 | La roadmap segnala implementazione runtime, non certificazione totale |
| MIGLIORIA | Diario/ricordi condivisibili con Anna tramite il Bridge già certificato, con review visibile | **83** | **80** | CAP-0020 | COPY/LINK già provati: estendere la UX e non il protocollo |
| MIGLIORIA | Timeline viaggio con foto, posizione e fonti, offline editing e navigazione immediata | **77** | **84** | CAP-0013 | Riusare gli entity id e media già presenti |

## World Days
Source: [World-Days@f6b70fc2298176c950d0cda9f0d6919c66267c13](https://github.com/riccardopinato/World-Days/tree/f6b70fc2298176c950d0cda9f0d6919c66267c13) · [README.md](https://github.com/riccardopinato/World-Days/blob/f6b70fc2298176c950d0cda9f0d6919c66267c13/README.md).
**Stato documentale:** Flutter: 1.111 IDs canonici, 502 articoli ricchi in sei lingue da CI AI, 485 dossier storici distinti; 626 ID restano senza ricerca storica primaria, 7 hold filippini, 0 signoff umani indipendenti..

| Tipo | Intervento specifico | P | F | CAP | Ragione/gate |
|---|---|---:|---:|---|---|
| GATE | Wave editoriali sulle 626 ricorrenze senza dossier originale: fonti istituzionali e 6 lingue con checkpoint | **100** | **70** | CAP-0042 | Mai confondere 502 Rich Editorial con 502 dossier originali distinti |
| GATE | Chiudere 7 hold filippini con fonti legali ufficiali, date mobili e controllo lingua | **99** | **48** | CAP-0042 | Fail closed se fonte non sufficiente; non inventare anni |
| GATE | Review umana qualificata di storie/6 lingue prima di dichiarare certificazione integrale | **97** | **57** | CAP-0042 | AI certification ≠ approvazione editoriale umana |
| MIGLIORIA | Feed quotidiano, preferiti/letture salvate, serie tematiche e ricerca incrociata per retention | **85** | **83** | CAP-0013/0144 | Niente nuove fonti non verificate nel contenuto |
| GATE | Verifica contenuti runtime, deploy Web e Play (APK/AAB), distinguendo CI da pubblicazione | **94** | **73** | CAP-0068 | README esclude esplicitamente deploy nel lotto #138 |

