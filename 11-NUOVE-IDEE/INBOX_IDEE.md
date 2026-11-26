# Inbox nuove idee — da valutare e conservare

## AUDMAIL-20261126-01…08 — Audit email: otto opportunità registrate (26/11/2026)

**Decisione utente:** registrare tutte le opportunità dell'audit e, dove utile, i miglioramenti nei repository delle app. **IDEA / DA_VALUTARE / NON APPROVATA**; le priorità sotto sono *di ricerca*, non di sviluppo. Le email private **non** sono state pubblicate. [Dossier approfondito con MVP, differenziale, privacy e gate](AUDIT_EMAIL_PROFONDO_8_OPPORTUNITA_2026-11-26.md) · [crosswalk CAP e issues](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_EMAIL_8_CAP_CROSSWALK_20261126.md).

| ID stabile | Opportunità | Tipo | Collocazione | Ricerca |
|---|---|---|---|---|
| AUDMAIL-20261126-01 | LifeCanvas | evoluzione | GalleryDrift, futuro ponte Wonderlog/Anna | P1 |
| AUDMAIL-20261126-02 | Procedure Engine | evoluzione | Notes-Ecosistema | P1 |
| AUDMAIL-20261126-03 | **Service Passport** | **NUOVA APP B2B candidata** | tecnici sul campo, non esiste ancora repo | P1 |
| AUDMAIL-20261126-04 | Failure Intelligence | evoluzione interna | AppLab / App Factory | P1 interna |
| AUDMAIL-20261126-05 | Decision Studio | evoluzione proposta | [CashMateAI #1](https://github.com/riccardopinato/CashMateAI/issues/1) (repo vuoto) / [Finance Intelligence #6](https://github.com/riccardopinato/Finance-Intelligence-Agent/issues/6) | P2 |
| AUDMAIL-20261126-06 | Kitchen Conductor | evoluzione proposta | [CookingAnime #79](https://github.com/riccardopinato/CookingAnime/issues/79) / [TasteAI #10](https://github.com/riccardopinato/TasteAI/issues/10) | P2 |
| AUDMAIL-20261126-07 | Art-to-Shot | evoluzione | ArtDrift / FrameLab | P2 |
| AUDMAIL-20261126-08 | Origin Passport | capability editoriale | ArtDrift / World Days / FrameLab, CAP-0043 da verificare | P2 interna |

**Escluse come nuovi prodotti**: screenshot organizer AI, generatore fotolibri standalone, quiz AI da PDF, ETF overlap tracker standalone, timer ricette semplice, task manager email generico: già diffusi o sovrapposti. Gli issue app collegati nel dossier sono **solo ricerca**, non scope implementativo. Nessuna nuova CAP assegnata senza pipeline completa.

## UTIL-20261126-01…03 — Tre utility pratiche salvate su richiesta dell'utente (26/11/2026)

**Decisione:** **SALVARE COME IDEE DA VALUTARE**, senza iniziare lo sviluppo. Rispetto alle dieci ipotesi email non convincenti, queste tre proposte sono state selezionate esplicitamente dall'utente come esempi più concreti. [Dossier con problema, azione principale, MVP e deduplicazione](UTIL-2026-11-26_TRE_UTILITY_PRATICHE.md).

| ID stabile | Proposta | Funzione essenziale | Collocazione | Stato |
|---|---|---|---|---|
| UTIL-20261126-01 | **L'ultima volta che…** | Registro interventi e **«Fatto oggi»**, prossima scadenza | Candidata nuova utility, verificare overlap HomeFix/reminder | IDEA / DA_VALUTARE |
| UTIL-20261126-02 | **File pronto da inviare** | Condividi file, converti/comprimi al limite richiesto, restituisci copia pronta | **Estensione candidata** PDF-Unifier / Omni Cleaner / FileFlow Kit | IDEA FUNZIONE / DA_VALUTARE |
| UTIL-20261126-03 | **Dov'è finito?** | Foto/etichette oggetto e ricerca della scatola o del cassetto | **Riuso/variante** di BoxFinder e Home Assets Passport, non clone | IDEA VARIANTE / DA_VALUTARE |

**Gate:** nessuna nuova app, modifica ai consumer, CAP, roadmap o promessa economica prima di un'ulteriore approvazione.

## MAIL-2026-001…010 — 10 ipotesi da email, conservate ma NON approvate (26/11/2026)

**Decisione utente: REGISTRARE SOLTANTO; LE IDEE NON CONVINCONO.** Stato di tutte le voci **RINVIATA / NON APPROVATA / PRIORITÀ BASSA**, senza attività pianificata. Fonte: osservazioni tematiche da corrispondenza privata, riportate **solo in forma astratta**, senza dati identificativi o copie delle email. Nessuna nuova app, capability, roadmap o valutazione commerciale verificata. [Dossier completo con problemi, MVP, riuso e ostacoli](MAIL-2026-11-26_OPPORTUNITA_DA_EMAIL.md).

| ID | Idea | Instradamento ipotetico (NON autorizzato) | Stato |
|---|---|---|---|
| MAIL-2026-001 | Deadline Radar | Notes/task o nuova app, da validare | RINVIATA |
| MAIL-2026-002 | RefundGuard | possibile CashMate | RINVIATA |
| MAIL-2026-003 | DevPulse | preferire App Factory/AppLab | RINVIATA |
| MAIL-2026-004 | GameShelf | solo ipotesi standalone | RINVIATA |
| MAIL-2026-005 | SellerDeadline | possibile micro-B2B | RINVIATA |
| MAIL-2026-006 | Backup Guardian | possibile Notes/Omni Cleaner | RINVIATA |
| MAIL-2026-007 | Subscription Map | possibile CashMate | RINVIATA |
| MAIL-2026-008 | TripChange | possibile Wonderlog | RINVIATA |
| MAIL-2026-009 | Access Watch | utility di sicurezza da verificare | RINVIATA |
| MAIL-2026-010 | Coupon Vault | micro-utility secondaria | RINVIATA |

**Gate di riapertura:** proposta migliorata + domanda esterna, concorrenza, differenziazione, diritti/permesse privacy e fattibilità. **Nessuna priorità ai prossimi step**.

## ART-2026-001 — Atelier del Giorno / arte quotidiana Android (21/11/2026)

**IN_CODICE / SOURCE_MERGED 21/11/2026** — app Flutter Android nel [repository ArtDrift](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery) (PR #1 merged, main `d329161c`). Flutter analyze, test e APK debug GitHub Actions [PASS su commit esatto](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/actions/runs/44858976559); **APK ARM64 v0.2 di test da 17,2 MB con **72 opere reali / ~302 KB di asset incorporati** [CI PASS](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/actions/runs/44861566087); nessun collaudo fisico, store, firma produzione o update-in-place certificati**. Origine: interesse espresso dall'utente per [anotherboring.day](https://anotherboring.day/) il 21/11/2026, verificato come servizio di opere d'arte scelte ogni giorno e wallpaper con app Mac esistente ([pagina prodotto](https://basalt.yevgenglukhov.com/), [Mac App Store](https://apps.apple.com/lu/app/another-boring-art-wallpaper/id6757328187?mt=12)). **Scope rettificato su indicazione esplicita dell'utente:** app Android Flutter **canvas infinito 2D in tutte le direzioni**, gesture drag/pan/pinch e opere visibili che compaiono durante l'esplorazione; layout posizionale stabile, lazy loading e dettaglio artwork a tap. Opera del giorno, ricerca/archivio/favoriti, palette e wallpaper restano secondari. Il vecchio ZIP Atelier v0.1 con liste/griglie era fuori scope ed è stato sostituito nel nuovo consumer da un vero canvas; il catalogo è ancora finito e può ripetersi nelle regioni lontane. Nome commerciale ancora da scegliere. **Non copiare** brand, grafica, feed, selezioni, download o testi del concorrente; servono diritti dell'opera, della riproduzione digitale e degli eventuali crediti per ogni immagine. Fonti candidata Met Open Access / Art Institute of Chicago API, da validare prima dell'import; catalogo indipendente curato. Diversa da `AL-ANDROID-2026-001` Adaptive Landscape (sfondi contestuali/lanciatori, non diario di opere d'arte). Monetizzazione da valutare, nessun prezzo approvato. [Dossier ART-2026-001](ART-2026-001_ATELIER_DEL_GIORNO.md) · [design audit](https://github.com/riccardopinato/Design-App/blob/main/sources/APPLLAMA_MOTION_ART_STACK_AUDIT_2026-11-21.md) (link del ramo da riconciliare dopo merge). **Gate:** sorgenti MVP locali non equivalgono ad APK; creare repo dedicato, catalogo editoriale originale con diritti per record, build/test Android, wallpaper su dispositivo reale, Product Bible e design distinti, modello economico e approvazione della pubblicazione.

**Aggiornamento 21/11 ArtDrift v0.3:** [PR #5 merged](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/pull/5), [CI esatta Flutter/test/ARM64 PASS](https://github.com/riccardopinato/ArtDrift-Infinite-Art-Gallery/actions/runs/44894034979); ricerca barra 1/3 avorio/pennello, pergamena con autocomplete autore/titolo/soggetto, Met+Cleveland *solo ricerca su richiesta*, 6 lingue UI e impostazioni/privacy/Pro informativo. **NON ancora** riconoscimento visivo, Rijksmuseum/catalogo internazionale permanente nel canvas, pagamenti o AdMob, né Play/QA fisica.

## GAME-2026-001 — Zombie Pixel Survival / precision shooter (21/11/2026)

**IDEA / DA_VALUTARE · nuovo gioco mobile standalone, non in roadmap.** Fonte: screenshot condiviso dall'utente il 20/11/2026 e analisi commerciale in chat. Pixel art post-apocalittica panoramica, shooter a munizioni limitate con possibile mira touch; MVP candidato Android landscape (15 livelli, 3 armi, 4 nemici e 2 ambienti). Potenziale commerciale preliminare **7,5/10** (stima, non ricavi misurati); priorità esplorativa medio-alta. **Nessuna identificazione dell'originale o licenza accertata: solo riferimento visivo, niente copia di codice/asset.** [Scheda completa GAME-2026-001](GAME-2026-001_ZOMBIE_PIXEL_SURVIVAL.md). Prima dello sviluppo: acquisire fonte originale, verificare diritti e validare una demo touch su Android.

## Anna's Diary — idee congelate dall'audit di consolidamento (19/11/2026)

**Decisione esplicita del titolare:** CONSERVARE PER RIVALUTAZIONE, **NON SVILUPPARE ORA**. Fonte: audit Anna's Diary del 19/11/2026 e sua sezione conclusiva ("consolidamento, collaudo ed effettiva finalizzazione del prodotto"). App source al censimento: [Agenda-per-Anna@adbab7d](https://github.com/riccardopinato/Agenda-per-Anna/commit/adbab7db67a1262a5255a64e4aa34da376d6d051); App Factory baseline per l'esecuzione: `6dfde2d6b6a5be6cbc898cea137f87803701814d` (Master v27 / Index v29). I sette ID qui sotto sono **ID di inbox / proposte**, non nuovi ID CAP. Non creare database/servizi, non duplicare CAP o promuovere nella Product Bible senza valutazione separata.

| ID inbox stabile | Opportunità | Valore / riuso possibile | Prima di rivalutare | Perché NON svilupparla ora | Stato |
|---|---|---|---|---|---|
| AD-OPP-20261119-01 | Ricordi del giorno con controlli espliciti | Valorizzare On This Day e Life Threads canonici; utilità personale, opt-in, snooze, preferenza mai suggerire | [Anna #224](https://github.com/riccardopinato/Agenda-per-Anna/issues/224), privacy/filter/locale/feedback su dati autorizzati | Prima QA Ricordi/Privacy e nessun algoritmo emotivo opaco | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-02 | Indicatore di ultima verifica cloud verificata | Riutilizzo cross-app del confine *cache disponibile* ≠ *server confermato*; candidato donor dal [fix Anna #365](https://github.com/riccardopinato/Agenda-per-Anna/pull/365) | Distinguere per-app ultima ricevuta, pendenti, offline, errore; niente "synced" senza ricevuta; verifica indipendente su secondo consumer | Il primo donor non basta per Golden certificata e nessuna nuova sync UI senza evidenza | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-03 | Backup guidato con prova del file | Wizard non distruttivo per rilettura archivio, checksum e ripristino isolato senza dati personali | Chiudere [Anna #329](https://github.com/riccardopinato/Agenda-per-Anna/issues/329) Android provider, rollback, ZIP/JSON, foto, incomplete media; rispettare Golden Backup DRAFT | Il backup esistente è già implementato: prima provarlo, non costruire un secondo motore | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-04 | Guide locali delle sottosezioni più difficili | Riutilizzare `AnnaContextHelpButton`, 5 lingue, a11y; guida su Account/Backup/Calendario/Color Picker | [Anna #355](https://github.com/riccardopinato/Agenda-per-Anna/issues/355) con priorità basata su percorsi realmente difficili e screenshot | Le guide principali esistono già; evitare assistenza invadente o duplicata | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-05 | Album media a proporzione naturale e fruizione migliorata | Estendere l'esistente viewer Ricordi senza ridimensionare o duplicare il file canonico | [Anna #327](https://github.com/riccardopinato/Agenda-per-Anna/issues/327), golden foto/testo vuoto, fixture reali autorizzate, memoria e scorrimento Android | Prima accettazione estetica attuale e misure di fluidità; non cambiare MediaAssetStore | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-06 | Mini-planner contestuale in Insieme (sola lettura) | Riepilogo weekend/preparazione da record condivisi già autorizzati | [Anna #225](https://github.com/riccardopinato/Agenda-per-Anna/issues/225), ACL server, revoche, due account e due dispositivi | Rischio esposizione privata e duplicazione task; Insieme va certificato prima | DA_VALUTARE / DEFERRED |
| AD-OPP-20261119-07 | Semplificazione moduli e percorsi poco utilizzati | Ridurre attrito e densità senza perdere strumenti o dati; telemetria solo aggregata/consensuale oppure osservazione QA manuale | Verificare uso effettivo con test sintetici e feedback; confronto N18 e configurazione moduli | Nessuna autorizzazione a nascondere/eliminare feature già approvate; prima consolidare | DA_VALUTARE / DEFERRED |

**Regole di riapertura:** la rivalutazione è una decisione futura distinta. Controllare prima capacità esistenti e `DA_VALUTARE.md`, evitare nuovi CAP per responsabilità già registrate; fissare fonte, beneficio, costo manutenzione, rischio dati, privacy, accessibilità, riuso, licenze e prove test. Nessuna di queste voci significa *feature mancante confermata* o *scope approvato*. Nel frattempo la priorità reale di Anna è chiudere 20 interventi di audit con livelli di evidenza distinti: codice, CI, PWA, Android fisico e Store.


## STARS-2026-11-16 — 17 fonti nuove e crosswalk trasversale da 110 stelle

**RESEARCH / NON APPROVATE**. Censimento pubblico GitHub: 737 su 750 stelle indicate; 110 nuove rispetto alle 632 storiche, di cui 89 già OSS95 e quattro già note. Le **17 fonti senza precedente dossier** suggeriscono soprattutto sicurezza per AppLab, Agent Canvas con OpenHands, widget desktop per App Factory Control Center; gli spunti Notes/Anna rimandano principalmente alle CAP già catalogate. [Scheda idee](STELLE_750_OPPORTUNITA_2026-11-16.md) · [Audit CAP e licenze](../12-CAPABILITY-E-IMPLEMENTAZIONI/STELLE_750_DELTA_110_OSS95_AUDIT_2026-11-16.md). Nessun nuovo prodotto, provider, CAP o codice approvato.


## DOCK-2026-001 — Dock desktop modulare e widget contestuali (16/11/2026)

**Stato: IDEA DI RICERCA / NON APPROVATA.** Due fonti fornite dall'utente: [OpenTaskbar (MIT, codice Windows)](https://github.com/alztrk/opentaskbar) e [lumabar (commerciale, source non pubblico)](https://github.com/Acadbek/lumabar). Non creare automaticamente un terzo launcher o duplicare Deskland: il prodotto autonomo avrebbe senso solo come piccola utility Windows molto diversa da un clone, con dock leggero, workflow app e widget opzionali utili (es. stato App Factory PR/CI). Prima verificare domanda, concorrenza, differenziazione, accessibilità, policy e coste di sviluppo. **Nessuna stella confermata dall'API autenticata; nessuna roadmap app modificata.** [Scheda tecnica con crosswalk CAP-0088, CAP-0144, CAP-0182 e source-pin](../12-CAPABILITY-E-IMPLEMENTAZIONI/STELLE_DOCK_WIDGET_INTAKE_2026-11-16.md).


## AGF-2026-001 / FIN-2026-001 / INT-2026-001 — Agent Factory, Finance Agent, Interactive Scene Core (11/11/2026)

**Decisione utente: CONSERVARE E STRUTTURARE** con repo dedicati e aggiornamenti progressivi. [Dossier completo](AGENT_FACTORY_FINANCE_DESKLAND_2026-11-11.md) · [Hub e bootstrap](../18-AGENT-FACTORY/README.md). Agent Factory Core per automazione cross-app, Finance Intelligence Agent per azioni/portafoglio read-only e paper trading, Interactive Scene Core ricavabile soltanto dal codice effettivamente testato di Adaptive Landscape. Il prodotto Android esiste già: [Adaptive-Landscape-Android](https://github.com/riccardopinato/Adaptive-Landscape-Android); l'upstream Deskland è GPL-3.0, **solo reference**, non copiare codice/asset nel progetto proprietario. I tre nuovi repo sono **CREATI, DOCUMENTATI e MERGED con CI PASS**: [Agent](https://github.com/riccardopinato/App-Factory-Agent-Core), [Finance](https://github.com/riccardopinato/Finance-Intelligence-Agent), [Scene](https://github.com/riccardopinato/Interactive-Scene-Core). Il codice agente Windows/WSL non è stato ancora importato su GitHub. Nessun trading live, nessuna nuova CAP o Golden promossa automaticamente.


## AL-ANDROID-2026-001 — Adaptive Landscape, wallpaper Android adattivo (10/11/2026)

**APP ATTIVA / SOURCE_MERGED v0.4.0 — ANDROID USER FAIL** nel [repo dedicato](https://github.com/riccardopinato/Adaptive-Landscape-Android) a `main@a05bec6a`; [PR #3](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/3) CI Flutter analyze/19 tests/Kotlin Android + APK ottimizzato/Web e GitHub Pages main [#42813678089](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42813678089) PASS. **Beach v0.3** corretta in [PR #7](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/7), Pages [#42822909836 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42822909836); **v0.3.1** speed fix [PR #8](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/8) merge su `main@72de4ff0`, deploy main [run #42825324425 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42825324425). [Beach v0.3.2 PR #9](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/9) GPU per-pixel, mare vuoto e dock manuale: [CI PR PASS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42847066074), main Pages SUCCESS. **v0.3.2 RESPINTA dal feedback visivo utente**; [v0.3.3 PR #10 merged](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/10), [39 test CI PR SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42854917650), [main Pages SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42855928354). [v0.4.0 PR #11 merged](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/11), [42 tests CI PR SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42881502356), [main Pages #42882654064 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42882654064). **Android v0.4 primo test: USER FAIL** per raster 360px, qualità visiva e assenza di lettura automatica Home. [PR sperimentale #13](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/13) con [CI SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42903313882), non merged; nuova APK fisica ancora da verificare. Auto-detection [issue #14](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/14) ancora mancante. Store/Play ancora NON VERIFICATI. Fonte [Deskland GPL-3.0](https://github.com/BLEZZ0102/Deskland) bloccata al commit `9818b577402ff476e1b59da07970c56472713126`: solo **reference E1**, nessun Donor E3 certificato, nessuna copia codice/asset. Flutter UI + WallpaperService Kotlin; griglia di calibrazione manuale perché Android non fornisce coordinate universali delle icone. Vendita standalone ipotizzata **€1,99–€2,99**, niente abbonamenti o ads. [Scheda tecnica, licenze, Golden e cinque maxi-step](ADAPTIVE_LANDSCAPE_ANDROID_2026-11-10.md).


## Template Notion — catalogazione per tutte le app (09/11/2026)

Nuovo [protocollo multi-app](../17-RICERCA-TEMPLATE-UX/ROUTING_MULTI_APP.md) per la sezione `docs/TEMPLATE_NOTION` in ogni app, alimentata da un [registro unico di 11 fonti](../17-RICERCA-TEMPLATE-UX/TEMPLATE_ROUTING_REGISTRY.json) ricavate da 12 ZIP (Design Brief duplicato). Nessuna CAP/Golden, integrazione Flutter, store o acquisto automatico; l'[idea template premium originale](../17-RICERCA-TEMPLATE-UX/IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md) resta backlog.


## TPL-STORE-2026-01 — Store interno di template originali (IDEA VALIDA, 09/11/2026)

**Decisione dell'utente:** conservare come **idea valida** lo store di template acquistabili separatamente all'interno di Notes e Anna's Diary; **€3,99 per template** è un'ipotesi di prezzo, non un prezzo approvato/attivato. La [scheda tecnica e commerciale](../17-RICERCA-TEMPLATE-UX/IDEA_STORE_TEMPLATE_INTERNO_2026-11-09.md) definisce catalogo, anteprime, acquisti una tantum, diritti, ripristino, compatibilità e gate. **Non autorizza** oggi sviluppo, nuove API/cloud, billing o release.

**Progettazione quattro pack originali (09/11):** [blueprint Notes/Anna](../17-RICERCA-TEMPLATE-UX/BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md), con due ipotesi Notes (Project Launch Studio e Study Sprint Studio) e due Anna (Atlante dei ricordi e Dodici settimane che contano). **DESIGN CANDIDATE / nessuna approvazione dello sviluppo premium**: non sono SKU, prodotti acquistabili, contenuti già realizzati o entitlement. \n\nLa vendita deve riguardare **template originali per le app**. Gli ZIP Notion di terzi sono fonti di ricerca, **non merce rivendibile**. Second Brain, Book Tracker e quattro altri export hanno [schede E2 o incompleto](../17-RICERCA-TEMPLATE-UX/README.md) con assegnazione primaria specifica.


## Ricerca template UX (09/11/2026) — TPLUX-001…008

Otto candidati di miglioramento, NON nuove app e NON nuove CAP, deduplicabili nella [scheda di riuso](../17-RICERCA-TEMPLATE-UX/CANDIDATI_RIUSO.md). Area di ricerca: template guidati, vision board sui canvas esistenti, home modulare, goal/review, mini-planner Noi, Second Brain read-only, Study Web e giornata realistica. [Matrice sorgente per Notes e Anna](../17-RICERCA-TEMPLATE-UX/CROSSWALK_NOTES_ANNA_2026-11-09.md). **PROPOSTA**: nessuna modifica a Product Bible, runtime, roadmap delle app o CAP registry; dati privati delle ricevute esclusi.


## Algoritmi ML leggeri, zero API e on-device — 04/11/2026

[Catalogo decisionale di 23 tecniche, 10 candidature nuove e mappa verso CAP/Golden](./CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md). Fonte: Machine Learning.txt dell'utente. ID stabili ML26-001…023. Nessun modello o codice integrato. Le 10 idee sono ora ammesse come CAP proposte, senza mutare le app.
**Aggiornamento di ammissione 04/11:** le dieci candidature ML26-001/002/004/008/009/013/015/016/018/019 sono state registrate rispettivamente come CAP-0152/0160/0151/0153/0154/0155/0159/0156/0157/0158, tutte PROPOSTA/E0. Le altre 13 restano riferite a CAP gia esistenti. [Audit Golden completo](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md).


## Notes-Ecosistema — audit 4 fonti e delta implementativi (04/11/2026)

Origine: audit condiviso dall'utente su **AI Valley, Hugging Face, GitHub/JSON Canvas e GitLab**. Le proposte **NOTES-AUD4-001…009** sono state ricondotte alle CAP canoniche esistenti quando pertinente; Smart Inbox action flow, JSON Canvas e Daily Note Hub non vanno assimilati a CAP solo simili. [Crosswalk con evidenze GitHub e roadmap ancora aperta](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_QUATTRO_FONTI_NOTES_2026-11-04.md).

**Stato:** audit/intake e delta di funzioni parziali; nessuna nuova app. Non promuove il registro CAP né cambia gli stati generati. Priorità operative: Smart Inbox #46, Project blockers #51, quindi Study #47, Duplicate Review #48 e JSON Canvas #49.

## Anna's Diary — 15 proposte NotebookLM (02/11/2026)

**Analizzate e mappate su 7 nuove CAP + 5 estensioni, non approvate in roadmap.** [Classifica e valutazioni](ANNA_NOTEBOOKLM_2026-11-02.md); [correzione CAP](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_ANNA_NOTEBOOKLM_2026-11-02.md); [offerta commerciale](../08-MONETIZZAZIONE/ANNA_DIARY_FREEMIUM_IPOTESI_2026-11-02.md). P1: domanda Noi, lettera futura, capsula, widget Oggi. Privacy #215 congelata.


| Nome | Categoria | Stato | Prossimo controllo |
|---|---|---|---|
| PDF Pocket Tools | utility | candidato con donor `PDF-Unifier` in codice | valutare estensione commerciale e licenze PDF, non partire da zero |
| EdgeDock / SideHub | Android launcher/overlay | candidato | permessi, policy |
| CmdPocket / TLDR Offline | developer | candidato | attribuzione dataset |
| Android QA Cockpit | desktop/B2B | candidato | rapporto con AppLab |
| DevBridge | dev/native | donor/candidato | GPL, Shizuku |
| Palette Lens | fotografia | feature FrameLab prima | algoritmo clean-room |
| ComicShelf | reader | backlog | licenza e mercato |

| Home Assets Passport | Suite consumer | NUOVA IPOTESI NON APPROVATA | BoxFinder + Purchase Guard + manuali/garanzie; verificare differenziazione |
| ShootWindow | foto / meteo / luce | NUOVA IPOTESI NON APPROVATA | prima funzione FrameLab, poi validare standalone |
| Pocket POI Offline | offline / geodata | NUOVA IPOTESI NON APPROVATA | licenze, qualità e freschezza POI, non clonare CamperBoss |
| DriveDay | auto / dati pubblici | NUOVA IPOTESI NON APPROVATA | combinare Parking Buddy, Fuel, Trip Cost, Vehicle Check |
| Trip Ready | travel checklist | NUOVA IPOTESI NON APPROVATA | testare prima in Wonderlog/CamperBoss/TrailPath |
| FileFlow Kit | file / privacy / transfer | NUOVA IPOTESI NON APPROVATA | non duplicare Send to PC, Foto→Chiavetta, SafeShare |
| Local Data Health Cockpit | B2B / AppLab | NUOVA IPOTESI NON APPROVATA | verificare adapter e copertura provider |

Prima di assegnare nuovi ID controllare i [cataloghi esistenti](../01-PORTAFOGLIO/CATALOGO_APP.md). Per una scheda dettagliata usare il [modello app](../10-MODELLI/SCHEDA_APP.md). Le proposte restano qui anche dopo promozione o rinvio, con stato e link aggiornati.

## Nuove candidate da r/BestGitHubRepos — 01/11/2026 (non promosse)

| Nome | Tipo | Decisione | Collegamento / prossimo gate |
|---|---|---|---|
| **DevPocket Tools** | mini suite web/Android | **NUOVA IDEA da valutare**, distinta da CmdPocket | CAP-0084; testare conversioni locali JSON/Base64/QR e differenza rispetto a WEB-001…016, licenza GPL reference-only |
| **DiskScope** | storage visualizer standalone | **FEATURE-FIRST / RINVIATA** | CAP-0083: introdurre treemap in Android Omni Cleaner prima di validare nuova app a pagamento |
| **GeoPulse Live** | esploratore di layer pubblici | **IPOTESI NON APPROVATA / RINVIATA** | CAP-0087; provider/ToS/meteo/earthquake; no allerta di sicurezza o navigazione operativa |
| **DeskPilot** | Android desktop workspace | **BASSA PRIORITA / BLOCCO OEM** | CAP-0088, Dextop GPL e HyperOS non supportato; non sovrapporre a EdgeDock/App Profiles |

Le idee restano in 11; i singoli comportamenti sono in 12 con ID CAP. Nessuna apertura app repo o promozione al portafoglio senza approvazione distinta.

## Hugging Face «to do» — 12 proposte funzionali, 01/11/2026 (NON nuove app)

Tutte **PROPOSTA**; destinazione principale Notes-Ecosistema, subset essenziale Anna's Diary. Scheda completa con punteggi, fonti, licensing e gate: [RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md).

| # | Idea conservata | Stato |
| --- | --- | --- |
| 1 | **01 Smart Task Capture** — CAP-0092 | PROPOSTA / non in roadmap |
| 2 | **02 Note → Checklist** — CAP-0093 | PROPOSTA / non in roadmap |
| 3 | **03 Sticky Kanban** — CAP-0094 | PROPOSTA / non in roadmap |
| 4 | **04 Voice → Actions** — CAP-0031/0092/0095 | PROPOSTA / non in roadmap |
| 5 | **05 Meeting Intelligence** — CAP-0095 | PROPOSTA / non in roadmap |
| 6 | **06 Task collegate/ricorrenti** — CAP-0096 | PROPOSTA / non in roadmap |
| 7 | **07 Project Memory** — CAP-0097 | PROPOSTA / non in roadmap |
| 8 | **08 Mind Map** — CAP-0098 | PROPOSTA / non in roadmap |
| 9 | **09 Planner studio** — CAP-0099 | PROPOSTA / non in roadmap |
| 10 | **10 Kanban collaborativa** — CAP-0100 | PROPOSTA / non in roadmap |
| 11 | **11 Productivity Dashboard** — CAP-0101 | PROPOSTA / non in roadmap |
| 12 | **12 Task Recovery** — CAP-0017/0018/0075 | PROPOSTA / non in roadmap |

Nessun progetto standalone o migrazione AI approvato; i CAP nuovi sono CAP-0092…CAP-0101. I CAP esistenti restano canonici per backup, lifecycle, voce e ricerca.

## Hugging Face «to do» — seconda ricerca, idee 13–28, 01/11/2026

Tutte **PROPOSTA** (funzioni, non nuove app). Approfondimento con punteggi, fonti dirette/distinte da inferenze, licenze e gate: [Seconda ricerca Hugging Face «to do»](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md).

| # | Idea | CAP collegati | Stato |
| --- | --- | --- | --- |
| 13 | **Smart Rescheduler** | CAP-0102, CAP-0001 | PROPOSTA — non in roadmap |
| 14 | **Dependency Map** | CAP-0103, CAP-0096, CAP-0028 | PROPOSTA — non in roadmap |
| 15 | **Goal Timeline** | CAP-0104, CAP-0099 | PROPOSTA — non in roadmap |
| 16 | **Smart Priority Engine** | CAP-0105 | PROPOSTA — non in roadmap |
| 17 | **Workload Guard** | CAP-0106, CAP-0001 | PROPOSTA — non in roadmap |
| 18 | **Project Blueprint Import** | CAP-0107, CAP-0093, CAP-0075 | PROPOSTA — non in roadmap |
| 19 | **Backward Planning** | CAP-0104, CAP-0001 | PROPOSTA — non in roadmap |
| 20 | **Task Time Accuracy** | CAP-0108, CAP-0101 | PROPOSTA — non in roadmap |
| 21 | **Focus Notes** | CAP-0109 | PROPOSTA — non in roadmap |
| 22 | **Eisenhower Visual Board** | CAP-0105, CAP-0094 | PROPOSTA — non in roadmap |
| 23 | **Quick Start Mode** | CAP-0110, CAP-0109 | PROPOSTA — non in roadmap |
| 24 | **Weekly Review** | CAP-0111, CAP-0101 | PROPOSTA — non in roadmap |
| 25 | **Learning Recall** | CAP-0112, CAP-0099 | PROPOSTA — non in roadmap |
| 26 | **Alternative Plans** | CAP-0102, CAP-0001 | PROPOSTA — non in roadmap |
| 27 | **Focus Protection** | CAP-0109, CAP-0077 | PROPOSTA — non in roadmap |
| 28 | **Meeting Load Heatmap** | CAP-0106, CAP-0101 | PROPOSTA — non in roadmap |

Le 16 idee si traducono in 11 nuovi CAP (CAP-0102…CAP-0112) e collegamenti a CAP preesistenti, evitando doppioni. La ricerca originale 1–12 resta nel documento precedente.

## Hugging Face Notes — terza e quarta ricerca: idee #29–56, 01/11/2026

**28 proposte funzionali archiviate, nessuna nuova app approvata.** Schede dettagliate: [idee #29–44](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md) e [idee #45–56](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md); originali #1–28 preservate.

| # | Idea conservata | Stima editoriale | Capability | Stato |
| --- | --- | --- | --- | --- |
| 29 | Privacy Shield | 9,9/10 | [CAP-0114](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0114.md) | PROPOSTA / non in roadmap |
| 30 | Contradiction Finder | 9,8/10 | [CAP-0115](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0115.md) | PROPOSTA / non in roadmap |
| 31 | Duplicate Notes Cleaner | 9,7/10 | [CAP-0116](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0116.md) | PROPOSTA / non in roadmap |
| 32 | Sketch-to-Diagram | 9,7/10 | [CAP-0117](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0117.md) | PROPOSTA / non in roadmap |
| 33 | Document Delta | 9,6/10 | [CAP-0118](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0118.md) | PROPOSTA / non in roadmap |
| 34 | Citation Integrity Checker | 9,5/10 | [CAP-0119](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0119.md) | PROPOSTA / non in roadmap |
| 35 | Accessible Image Notes | 9,4/10 | [CAP-0120](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0120.md) | PROPOSTA / non in roadmap |
| 36 | Easy Reading Mode | 9,4/10 | [CAP-0121](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0121.md) | PROPOSTA / non in roadmap |
| 37 | Table Capture | 9,3/10 | [CAP-0122](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0122.md) | PROPOSTA / non in roadmap |
| 38 | Bilingual Notes Reader | 9,2/10 | [CAP-0123](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0123.md) | PROPOSTA / non in roadmap |
| 39 | Topic Discovery | 9,2/10 | [CAP-0124](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0124.md) | PROPOSTA / non in roadmap |
| 40 | Chart-to-Data | 9,1/10 | [CAP-0125](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0125.md) | PROPOSTA / non in roadmap |
| 41 | Living Glossary | 9,0/10 | [CAP-0126](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0126.md) | PROPOSTA / non in roadmap |
| 42 | Video Chapter Notes | 9,0/10 | [CAP-0127](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0127.md) | PROPOSTA / non in roadmap |
| 43 | Form-to-Card | 8,9/10 | [CAP-0128](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0128.md) | PROPOSTA / non in roadmap |
| 44 | Knowledge Freshness | 8,9/10 | [CAP-0129](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0129.md) | PROPOSTA / non in roadmap |
| 45 | Notes to Slides | 9,8/10 | [CAP-0130](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0130.md) | PROPOSTA / non in roadmap |
| 46 | Math Ink | 9,7/10 | [CAP-0131](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0131.md) | PROPOSTA / non in roadmap |
| 47 | Soundscape Journal | 9,6/10 | [CAP-0132](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0132.md) | PROPOSTA / non in roadmap |
| 48 | Smart Reading Flow | 9,6/10 | [CAP-0133](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0133.md) | PROPOSTA / non in roadmap |
| 49 | Document Auto-Sorter | 9,5/10 | [CAP-0134](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0134.md) | PROPOSTA / non in roadmap |
| 50 | Evidence Board | 9,5/10 | [CAP-0135](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0135.md) | PROPOSTA / non in roadmap |
| 51 | Smart Cutout Canvas | 9,4/10 | [CAP-0136](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0136.md) | PROPOSTA / non in roadmap |
| 52 | 3D Memory Objects | 9,3/10 | [CAP-0137](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0137.md) | PROPOSTA / non in roadmap |
| 53 | Audio-Linked Ink | 9,3/10 | [CAP-0138](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0138.md) | PROPOSTA / non in roadmap |
| 54 | Motion Study Notes | 9,2/10 | [CAP-0139](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0139.md) | PROPOSTA / non in roadmap |
| 55 | Scientific Figure Studio | 9,1/10 | [CAP-0130](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0130.md) | PROPOSTA / non in roadmap |
| 56 | Image Authenticity Inspector | 9,0/10 | [CAP-0140](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0140.md) | PROPOSTA / non in roadmap |

Il caso #55 e #45 condivide una sola capability; nessuna delle due idee e stata scartata. Link, licensing, demo offline e impatto APK sono documentati nelle schede di ricerca.

## Importazione IA 02/11/2026 — idee in analisi (non promosse)

| Lotto | Natura | Stato | Schede e ranking | Prossimo gate |
|---|---|---|---|---|
| IA26-001…IA26-100 | 100 idee originali #1–#100; nessun ID app nuovo | ANALISI / NON APPROVATE | [Indice 100](IA-2026-11-02/INDICE_100_SCHEDE.md) · [ranking](IA-2026-11-02/RANKING_100_COMPLETO.md) | concorrenza, review codice, licenze, policy |
| IA26-E01…E06 | 6 idee non numerate, conservate separatamente | ANALISI / NON APPROVATE | [Indice extra](IA-2026-11-02/INDICE_IDEE_EXTRA_NON_NUMERATE.md) | prototipi tecnici, target, domanda |
| 14 fusioni della fonte | valutazione combinazioni, nessun prodotto fuso approvato | ANALISI | [Fusioni e reuse](IA-2026-11-02/FUSIONI_E_RIUSO.md) | gate di coerenza prodotto e donor |

## Secondo lotto ML10 on-device — 04/11/2026

Fonte: messaggio utente 04/11 con elenchi ripetuti. Dieci famiglie distinte: Isolation Forest/LOF, MinHash+LSH, agglomerative clustering, HMM, PCA/TruncatedSVD, Naive Bayes, kNN, logistic regression, visione/audio LiteRT/Core ML, exponential smoothing/Holt-Winters. Tutte mappate a CAP esistenti, senza nuova app o duplicazione CAP. [Audit approfondito e scelte](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md). Due reference engine puri integrati da [Core PR #71](https://github.com/riccardopinato/App-Factory-Core/pull/71), [CI main SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497699); zero modifiche ai prodotti. Certificazione donor consumer / Golden ancora da dimostrare ([gate #72](https://github.com/riccardopinato/App-Factory-Core/issues/72)).

## ML10 — esecuzione P1/P2/P3 e revisione generale (04/11/2026)

I motori puramente matematici ora esistono come reference implementation in [Core #71](https://github.com/riccardopinato/App-Factory-Core/pull/71) e [Core #73](https://github.com/riccardopinato/App-Factory-Core/pull/73), con CI Dart/Factory verde; **non** significa modelli ML addestrati né motori certificati sul dispositivo. Il classificatore Vision/Audio resta bloccato per mancanza di checkpoint/licenze/benchmark. [Audit completo 160 CAP / 385 associazioni](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_COMPLETO_ML10_2026-11-04.md) ricalcola le priorità e la facilità per app soltanto dove nuove prove giustificano la modifica; nessuna nuova CAP duplicata.

## ML10 consumer delta verificato — 04/11/2026

App Factory Core resta source of truth delle Golden Rules; Ideas mantiene il registro a 160 CAP e le 385 associazioni. [Notes #57](https://github.com/riccardopinato/Notes-Ecosistema/pull/57) è un consumer MinHash/LSH read-only, non merge reversibile; [TasteAI #2](https://github.com/riccardopinato/TasteAI/pull/2) un consumer P2 kNN ricette correlate, non prova di migliori risultati anti-spreco. [Registro con delta app e sorgenti](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_CONSUMER_POSTMERGE_2026-11-04.md), [screening modelli P3](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_MODEL_SCREENING_2026-11-04.md). Nessuna nuova CAP, nessuna promozione Golden/Store.
