# ART-2026-001 — Atelier del Giorno
**Stato:** IN_ROADMAP / SVILUPPO ANDROID AUTORIZZATO · 21/11/2026 · **prototipo sorgente locale NON COMPILATO / NON VERIFICATO; nessun repository app, APK o pubblicazione attestato**

## Provenienza e confine
Ispirazione dell'utente: [anotherboring.day](https://anotherboring.day/), con servizio di opere d'arte curate quotidianamente e [app Mac](https://apps.apple.com/lu/app/another-boring-art-wallpaper/id6757328187?mt=12) esistente. Sito originale non letto integralmente tramite fetch, ma [pagina prodotto dell'autore](https://basalt.yevgenglukhov.com/) e listing App Store Mac documentano concept 'fine art daily', wallpaper/rotazione e raccolta. **Idea da reimplementare in modo indipendente**, NON replicare nome, asset, curatela, design, database, immagini/servizi e non assumere endpoint pubblici come contratto commerciale. Distinto da [Adaptive Landscape Android](ADAPTIVE_LANDSCAPE_ANDROID_2026-11-10.md).

## Promessa di prodotto originale
Un museo da tasca che presenta ogni giorno un'opera **con crediti e contesto**, costruisce un personale percorso d'arte e permette di usare, dove lecito, la riproduzione digitale come sfondo su smartphone. L'utente sceglie la propria esperienza: diario artistico, galleria tematica, esplorazione a sorpresa, palette di colori ispirate all'opera; mai copiare i servizi del sito sorgente. Il nome 'Atelier del Giorno' è provvisorio e richiede verifica marchi.

## Target e piattaforma
- Prima piattaforma candidata: Android Flutter, con modulo Kotlin limitato al set wallpaper/permission integration quando necessario.
- Estensione iOS solo dopo valutazione distinta: le API/permessi di gestione dello sfondo non sono equivalenti; **non promettere automatic wallpaper su iOS**.
- Categoria: arte, educazione leggera, benessere visivo / personalizzazione locale, evitando slogan salute/benefici non comprovati.
- Possibile sinergia con World Days per giornate legate all'arte (nessun riuso di storie non certificate); app indipendente per Product Bible.

## MVP candidato (non approvato)
1. **Opera del giorno**: una selezione originale verificata per fonte/diritti, descrizione breve, artista, epoca, provenienza e tecnica quando pubblicamente documentabili.
2. **Sfoglia ed esplora**: categorie, cronologia, alternative casuali; cronologia su dispositivo.
3. **Dettaglio a schermo intero**: zoom, pan, immagini non tagliate, didascalia, contrasto/tipografia accessibile.
4. **Favoriti** e raccolta locale con import/export opzionale, database leggero.
5. **Wallpaper Android**: adattamento proporzioni con crop manuale e anteprima, scelta Home/Lock quando supportata; chiedere consenso esplicito, niente cambio wallpaper senza autorizzazione.
6. **Offline**: conserva solamente file licenziati e richiesti dall'utente, cache limitata e cancellabile, backup non obbligatorio.
7. **Privacy-first**: nessun login obbligatorio; niente tracker di default; telemetria soltanto con consenso e opt-out se in futuro necessaria.

## Fuori MVP
- Clonazione pixel-to-pixel di Another Boring Day o utilizzo della sua API/feed senza permesso.
- Riproduzione indiscriminata di cataloghi, didascalie o immagini di musei.
- AI generativa di dipinti o scraping di immagini da Google.
- Wallpaper rotazione forzata su iOS, sincronizzazione cross-device, account e monetizzazione aggressiva.

## Materiali e diritti: gate obbligatorio
Fonti da verificare come candidati (non autorizzate automaticamente): [The Met Open Access](https://www.metmuseum.org/about-the-met/policies-and-documents/open-access) e [Art Institute of Chicago API](https://api.artic.edu/docs/). Per **ogni** record: source ID, licenza immagine specifica, credit line, provenienza, artista/opera, stato pubblico dominio/CC0 dove comprovato, eventuali limiti sulla riproduzione fotografica, URL persistente e date di verifica. Testi descrittivi originali, non copiati dai siti. Se diritti/dati incompleti: opera esclusa dal feed pubblico.

## Business e validazione
- Ipotesi posizionamento: alta qualità visuale + scoperta culturale, esperienza distinta da semplici wallpaper pack.
- Possibile MVP gratuito; abbonamento, lifetime e annunci da confrontare solo dopo studio della concorrenza e dei costi legali/CDN.
- Segnali da raccogliere: ricerca domanda Android Google Play; valutazione app concorrenti; interesse per contenuto quotidiano vs desiderio di wallpaper; retention D1/D7/D30 in test; fattibilità locale degli aggiornamenti e della cache.
- Rischi principali: permessi/OS restrictions, costo contenuti/autori, scarsità di differenziazione, qualità catalogo e retention.
- **Nessun potenziale commerciale numerico attestato**, nessun annuncio o prezzo approvato.

## Sviluppo: autorizzato, verifica da completare
1. Product Bible originale e mock-up indipendenti dalle schermate del concorrente; usare Design-App per componenti accessibili coerenti.
2. Proof of concept Android di wallpaper con due immagini di test con diritti verificati.
3. Pipeline editoriale per fonti/licenze e aggiornamenti controllati.
4. Test fisici di schermo intero/crop/launcher wallpaper, airplane mode, storage, privacy; dimensione APK misurata.
5. Repository consumer dedicato, CI exact-head, APK di test e firma persistente ancora da configurare. Il prototipo non equivale a una build installabile.

**Fonte Design-App:** [audit lotto 21/11/2026](https://github.com/riccardopinato/Design-App/blob/main/sources/APPLLAMA_MOTION_ART_STACK_AUDIT_2026-11-21.md). **Registro inbox:** [ART-2026-001](INBOX_IDEE.md#art-2026-001--atelier-del-giorno--arte-quotidiana-android-21112026).

## Decisione esplicita 21/11/2026 — avvio Android
- L'utente ha richiesto di **creare un'app Android come anotherboring.day**, quindi l'avvio di un'implementazione indipendente è approvato; le esclusioni su brand/feed/codice/asset del concorrente rimangono vincolanti.
- **Prima consegna nella chat**: sorgenti Flutter MVP v0.1 in ZIP + file TXT (non presenti ancora in un repository app). Funzioni implementate nel sorgente: vista giornaliera alimentata da search API AIC e selezione deterministica, esplorazione, dettaglio con zoom, metadata e credit line, preferiti locali con cache immagine best-effort, anteprima wallpaper Android e chiamata nativa Kotlin Home/Lock/Both. Nessun catalogo editoriale curato dichiarato; i contenuti giornalieri sono selezioni automatiche dal provider Open Access.
- **Stato prove**: SOURCE PREPARED LOCALLY / NOT COMPILED / NOT TESTED ON DEVICE. Flutter/Android SDK non disponibili nell'ambiente di authoring. Non attestare CI, APK, firma, installazione, Store, affidabilità provider o schedulazione automatica.
- **Provider**: Art Institute of Chicago API, `REVIEWED_FOR_PROTOTYPE` soltanto; filtro runtime `is_public_domain == true`, ID immagine limitato, credit line e link museo. La verifica per-record di diritti, termini commerciali, rate limit e provenienza editoriale rimane obbligatoria prima del feed pubblico.
- **Priorità successive**: creare repo app, integrare sorgenti, validare compilazione Android, POC wallpaper su dispositivo, approvare identità visiva, introdurre dataset editoriale 30–100 opere con rights evidence, WorkManager con opt-in e pin, test offline/cache, APK firmato dopo gate.
