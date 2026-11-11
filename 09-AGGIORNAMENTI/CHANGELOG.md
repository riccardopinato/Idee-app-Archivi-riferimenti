# Changelog dell'archivio

## 2026-11-11 — Retry effettivi e audit di tutta la flotta di 35 repo (M1)
- Audit statico workflow su default branch 35/35, schedule/dispatch e write scopes; nessun evento `schedule` o `workflow_dispatch` del workflow di contesto risulta eseguito alla verifica. Altri schedule/manual non vanno scambiati per questo job.
- Rilanciati quattro job falliti: tre ancora bloccati dalla permission GitHub PR creation; Agent Core ha manifestato un nuovo difetto di configurazione bot identity prima del merge.
- Fix reali CI+merge nei tre originali: [App-Factory-Agent-Core #8](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/8), [Finance #4](https://github.com/riccardopinato/Finance-Intelligence-Agent/pull/4), [Interactive #4](https://github.com/riccardopinato/Interactive-Scene-Core/pull/4). [Run E2E Agent Core](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43052705998) verifica il merge e lo snapshot dopo il fix, ma non la creazione PR, bloccata dall'amministrazione. Cleanup [#10](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/10) merged.
- Esiste una sola PR bot aperta verificata, [btrader #5](https://github.com/riccardopinato/btrader/pull/5); 30 non-canary sono solo static audited. Una nuova automazione ChatGPT per ricontrollo cron è stata rifiutata perché 5 attività risultano già attive; nessuna esistente modificata.
- [Evidence completa](../18-AGENT-FACTORY/EVIDENCE_M1_35_REPO_SWEEP_AND_RETRY_2026-11-11.md) e [roadmap](../18-AGENT-FACTORY/ROADMAP_CONTEXT_AUTOMATION_35_REPOS_2026-11-11.md) restano `M1 PARTIALLY_VERIFIED`, `ADMIN_BLOCKED`, `SCHEDULE_NOT_VERIFIED`.


## 2026-11-11 — Collaudo live M1 GitHub Actions: 1 E2E PASS, 4 blocker admin
- Eseguiti **5 veri workflow di snapshot** con evento `push` temporaneo limitato al file workflow su pubblico, privato (anonimizzato nel catalogo), `master`, workflow originale e branch protetto. Cinque snapshot/branch bot verificati sui commit upstream.
- [btrader E2E run 43040885976](https://github.com/riccardopinato/btrader/actions/runs/43040885976) PASS con [PR #5](https://github.com/riccardopinato/btrader/pull/5) creata automaticamente da `github-actions[bot]`, rerun PASS e nessuna PR duplicata. La PR di metadata resta aperta per revisione.
- Quattro casi hanno fallito **solo** `gh pr create` con `GitHub Actions is not permitted to create or approve pull requests`, pur avendo scritto branch/documenti validi. Il connettore non consente la modifica dell'impostazione admin.
- Eliminati tutti i trigger `on.push` di QA con PR validate e merged. `schedule` e `workflow_dispatch` su default branch sono intatti ma **non ancora collaudati** in esecuzione reale.
  - Riconciliazione ulteriormente verificata su btrader: un nuovo commit reale di Idee ha aggiornato la PR bot #5 già aperta (`run attempt=3`, success), senza PR duplicate o altri file modificati.
- [Documento evidence](../18-AGENT-FACTORY/EVIDENCE_M1_CONTEXT_SYNC_CANARY_2026-11-11.md) e [roadmap aggiornata](../18-AGENT-FACTORY/ROADMAP_CONTEXT_AUTOMATION_35_REPOS_2026-11-11.md) marcano M1 `PARTIAL_E2E_VERIFIED / BLOCKED_ADMIN_SETTING`, senza falsa certificazione sui 35 repository.


## 2026-11-11 — Roadmap cross-repo context sync aggiornata (35/35)
- Verificato inventario dei 35 repository owner: 32 pubblici, 3 privati. Il workflow di snapshot è stato integrato nelle default branch di tutti: 32 nuovi rollout e hardening dei 3 repo Agent/Finance/Scene già inizializzati.
- Ultimi gate e merge: [CamperBoss #32](https://github.com/riccardopinato/CamperBoss/pull/32) `fe3b10d`, [World-Days #88](https://github.com/riccardopinato/World-Days/pull/88) `d06cb1d`, [AppLab #215](https://github.com/riccardopinato/AppLab/pull/215) `2d57d9c`, [Notification-Control #37](https://github.com/riccardopinato/Notification-Control/pull/37) `3a38648`.
- Aggiunta la [roadmap operativa 35 repo](../18-AGENT-FACTORY/ROADMAP_CONTEXT_AUTOMATION_35_REPOS_2026-11-11.md) con cinque maxi-step e i gate di rollout; priorità immediata al collaudo `schedule`/`workflow_dispatch` e creazione PR bot, ancora NON_VERIFICATI. CI delle PR non equivale a funzionamento schedulato.
- Nessun progresso attribuito al runtime Windows AppFactoryAgent, Finance trading, Interactive Scene renderer, device/store, Golden certification o aggiornamento semantico automatico. Factory baseline riconsultata `c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Index v29.


## 2026-11-11 — Tre repo Agent/Finance/Scene creati e documentati

- AGF, FIN e INT bootstrap #1 mergiate con CI PASS sui commit esatti: [AGF](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/1), [FIN](https://github.com/riccardopinato/Finance-Intelligence-Agent/pull/1), [INT](https://github.com/riccardopinato/Interactive-Scene-Core/pull/1).
- Documento in ciascun repo: AGENTS, Product Bible, roadmap, architecture, status/reuse/evidence/provenance, contratti design, workflow di verifica e snapshot. Nessuna importazione di codice locale Windows né nuova funzione di trading o renderer; test CI sono solo sulle utility di contesto.
- Automatismo GitHub Actions cron per osservare gli SHA upstream e aprire PR di metadata; attivazione schedulata e permessi bot PR devono ancora essere provati. Programmazione ChatGPT dedicata bloccata dal limite attuale delle cinque attività attive.


## 2026-11-11 — Agent Factory / Finance Intelligence / Interactive Scene Core, intake strutturato

- Decisione dell'utente: conservare come iniziative consistenti, preparare repo separati e mantenere documentazione/codice aggiornati incrementalmente.
- Registrati ID AGF-2026-001, FIN-2026-001, INT-2026-001 nell'Inbox e nel [dossier tecnico](../11-NUOVE-IDEE/AGENT_FACTORY_FINANCE_DESKLAND_2026-11-11.md); creati [hub](../18-AGENT-FACTORY/README.md), [bootstrap](../18-AGENT-FACTORY/BOOTSTRAP_REPOS.md) e [reuse matrix](../18-AGENT-FACTORY/REUSE_MATRIX.md).
- Riconciliato prodotto Android esistente Adaptive-Landscape-Android, senza clonarlo; Deskland GPL-3.0 reference only. btrader crypto NON identificato come Finance Agent azionario.
- Baseline Factory v27 / Golden Index 29 pin ee72dbb1b0de2cd71bc4aac42c350853c6915159. Nessun nuovo repo creato, nessun nuovo CAP/Golden o codice agente/Finance importato; stati NOT_VERIFIED dove manca evidence.


## 2026-11-10 — Android Adaptive Landscape v0.4: user real-device FAIL, PR13 test pre-merge

- User phone test v0.4 **FAIL**: sea pixelated/sbiadito, foam border harsh, motion weak, only manually placed dock creates sand. Root Android Canvas bitmap capped at 360px and generic WallpaperService no launcher icon coordinates.
- Experimental [PR13](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/13) with first-party EGL14/GLES20 full-framebuffer shader plus local screenshot-assisted manual calibration; [CI SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42903313882), head `ef6bcfd5`, **NOT MERGED pending physical acceptance**. Does not deliver automatic detection/true source 4K.
- P0 automatic icon detection [issue #14](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/14) remains open; any accessibility approach requires separate user permission, policy disclosure, OEM tests. No release certification or Golden promotion.


## 2026-11-10 — Adaptive Landscape Beach v0.4 Ultra: target realismo 4K

- Input utente: concentrare le modifiche sul realismo 4K dell'immagine del mare, non sul solo numero di pixel.
- [App PR #11](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/11) merged `main@a05bec6a`: shader GPU più ricco, palette cromatica originale campionata in atlas RGB565 24×42, preset Bilanciata/Alta/Ultra, continuità scene mare vuoto e costa condizionata da icone.
- [CI PR #42881502356 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42881502356): 42 test, Flutter analyze, APK debug/release per ABI, Web. Main Pages [#42882654064](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42882654064) **SUCCESS**.
- La texture di riferimento 2160×3840 è ricampionata e NON è fotografia ottica 4K nativa; la Web shading a risoluzione framebuffer non implica pixel fisici 4K garantiti. Realismo utente, FPS/browser e Kotlin Android restano NON CERTIFICATI; nessuna copia GPL o Golden E3.


## 2026-11-10 — Adaptive Landscape Beach v0.3.3, correzione feedback Web

- User Web v0.3.2: avvio non da mare vuoto, resa mare non realistica (**NON ACCETTATA**).
- Fix [app PR #10 merged](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/10): default Beach senza guides, comando Solo mare anche nei vecchi profili, status GPU/fallback, preview grande, shader rifinito, cache fallback doppia.
- CI [#42854917650](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42854917650) **39 test + analyze/Android/Web PASS**; main `e81907f0`, [Pages #42855928354](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42855928354) **SUCCESS**.
- Qualità/realismo 4K Web da rivalutare con l'utente; Android release/battery e Play non certificati; Deskland resta E1 reference, nessuna CAP/Golden promossa.


## 2026-11-10 — Adaptive Landscape Beach v0.3.2 GPU e dock

- User feedback: rimuovere pixelatura del mare (qualità 4K-capable Web), sabbia solo intorno a icone/cartelle/widget/dock, solo oceano quando tutto vuoto.
- [App PR #9 merged](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/9), main `6e434c0a`, [CI PR #42847066074 PASS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42847066074); [main #42848475579](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42848475579) Pages SUCCESS.
- Shader GPU per pixel Web + texture statica geometria 512×1024; dock manuale 0/3/4; fallback mesh su browser incompatibili, Android non ancora 4K/testato.
- Qualità estetica/4K reale sul browser dell'utente non attestata, QA fisica e Play rimandati, nessuna promozione E1→E3/Golden.


## 2026-11-10 — Adaptive Landscape Beach: top-down v0.3/0.3.1

- Correzione visiva richiesta dall'utente: Beach visto dall'alto, soltanto sabbia, fascia bagnata, acqua turchese/deep sea, onde/schiuma dinamiche, NO cielo/nuvole/sole; Meadow separato.
- [PR app #7](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/7) e [CI #42821824304 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42821824304), Pages [#42822909836 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42822909836), commit `c220b64e`.
- [PR app #8](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/8) e [CI #42824258762 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42824258762), speed continuity merged `72de4ff0`; main deploy v0.3.1 [run #42825324425 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42825324425).
- Nessuna prova fisica/OEM, nessuna validazione estetica utente v0.3.x, nessuna firma Play; Deskland resta reference E1 GPL, non donor E3/Golden.


## 2026-11-10 — Adaptive Landscape Android v0.2: sync stato repository

- Allineati dossier e inbox all'implementazione reale [main@9538849c](https://github.com/riccardopinato/Adaptive-Landscape-Android/commit/9538849c3c478c677bba246359c646e9fef04a11), dopo [PR #3](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/3) e [CI #42812771584 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42812771584).
- v0.2 codificata: griglie flessibili/widget zones, profili JSON locali, scene native+Flutter, 6 ARB, CI debug e APK interni ottimizzati. Device/Play/qualità premium NON attestati; issue app #4/#5/#6 aperte.
- Deskland resta riferimento E1, nessuna nuova CAP o Golden certificata. Web v0.2 su main [Actions #42813678089](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42813678089) **SUCCESS**; apertura HTTP su browser utente v0.2 non ancora confermata.


## 2026-11-10 — Nuova app Adaptive Landscape / Deskland Android, intake E1

- Creata [scheda prodotto](../11-NUOVE-IDEE/ADAPTIVE_LANDSCAPE_ANDROID_2026-11-10.md), con source SHA upstream `9818b577402ff476e1b59da07970c56472713126`, GPL-3.0, distinzione reference E1 / Donor E3 e piano Flutter + wallpaper nativo.
- Sorgenti MVP preparati in chat come file `.txt`, senza backend/AI e senza codice/asset GPL importati; build/test/Android reale e Play **non verificati**.
- Non modificati Golden Core, capability registry, repository di app, billing o pubblicazioni.


## 2026-11-09 — Chiusura sorgente delle quattro priorità template

- Notes [PR #98](https://github.com/riccardopinato/Notes-Ecosistema/pull/98) merged `cf9f9c515a87f438ab0112e7efd4a0ce0471fbd6`, test/CI PR PASS e fix controller del dialogo Book Tracker (bug riprodotto dal nuovo test). QA fisico/account non attestato.
- Anna [PR #293](https://github.com/riccardopinato/Agenda-per-Anna/pull/293) merged `260dd753a3f7d1b7cd501ce38cf6e4a78ea773b3`, check/UI5 PASS, test anteprima → annulla → conferma, riallineamento main Vision Board protetto.
- Wonderlog [PR #27](https://github.com/riccardopinato/Wonderlog/pull/27) merged `f045588dd5dbd668541fec380f184f3ebcd8bb6f`, verify/Apple/legacy PASS. Pages build+deploy **SUCCESS** sul nuovo main nella [run #42710542583](https://github.com/riccardopinato/Wonderlog/actions/runs/42710542583); due retry del precedente commit falliti per timeout, documentati in [issue #28](https://github.com/riccardopinato/Wonderlog/issues/28). La visita HTTP reale del sito resta NOT_VERIFIED.
- [Ledger donor](../17-RICERCA-TEMPLATE-UX/STEP5_DONOR_PROVENANCE_2026-11-09.md): E3 limitato con SHA/CI, senza falsa promozione E5/Golden. [Quattro blueprint premium originali](../17-RICERCA-TEMPLATE-UX/BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md): DESIGN CANDIDATE, niente SKU/billing/Store.
- [Registro completo](../17-RICERCA-TEMPLATE-UX/EXECUTION_4_PRIORITIES_2026-11-09.md). Collaudo real-device, account, backup e autorizzazione commerciale restano gate separati.

## 2026-11-09 — Template Step5: donor provenance e quattro priorità attivate

- [Registro esecuzione quattro filoni](../17-RICERCA-TEMPLATE-UX/EXECUTION_4_PRIORITIES_2026-11-09.md): retry Pages Wonderlog sullo stesso SHA, PR QA Notes #98 / Anna #293 / Wonderlog #27, ledger donor E3 limitati e blueprint quattro premium originali.
- [Provenance con SHA, codice, test e limiti](../17-RICERCA-TEMPLATE-UX/STEP5_DONOR_PROVENANCE_2026-11-09.md): TPLUX-001 allineato agli owner reali senza attribuire E5 o nuova Golden/CAP.
- [Blueprint premium](../17-RICERCA-TEMPLATE-UX/BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md): due concept per Notes e due per Anna, `DESIGN CANDIDATE`; nessun SKU, acquisto, app store, rilascio, import di materiale Notion o nuova entitlements.
- Device/backup/account reali e provider billing rimangono **NOT VERIFIED**; verificare l'esito del retry e delle nuove CI, non promuovere una PR aperta a PASS.

## 2026-11-09 — Maxi-step 4: chiusura delle due integrazioni native

- **Notes:** [PR #97](https://github.com/riccardopinato/Notes-Ecosistema/pull/97) unita a `f057c81c92532cd22b504116c14ccef8a2ad6612`; `verify`, `verify-web`, `build-web` SUCCESS sul PR head `ae93ff2a`. Catalogo gratuito / I miei, senza nuova persistenza.
- **Anna:** [PR #291](https://github.com/riccardopinato/Agenda-per-Anna/pull/291) unita a `2c77c764ecf9982817aee8fc6ecc31ee75b741f9`; `check`, UI5 source e `build-web` SUCCESS sul PR head `6316a4c`. Anteprima prima dell'editor, 5 lingue; adeguati i test storici di annullamento/errore salvataggio.
- [Matrice esatta e gate residui](../17-RICERCA-TEMPLATE-UX/UX_STEP4_CATALOGO_NATIVO_2026_11_09.md): **source/CI PR PASS, merged main**. CI post-merge, device, account/backup, billing e Store non si inferiscono dal merge. Nessun CAP/Golden, SKU, provider billing o asset Notion importato.

## 2026-11-09 — Maxi-step 4: catalogo nativo gratuito, PR aperte

- [Matrice Step4](../17-RICERCA-TEMPLATE-UX/UX_STEP4_CATALOGO_NATIVO_2026_11_09.md) e due sorgenti in PR: [Notes #97](https://github.com/riccardopinato/Notes-Ecosistema/pull/97), [Anna #291](https://github.com/riccardopinato/Agenda-per-Anna/pull/291); confermare CI e merge dai rispettivi head prima di promuovere lo stato.
- Separazione rigorosa catalogo gratuito / modelli personali / futura vendita di premium originali. Nessuna variazione al prezzo ipotetico €3,99, nessun pagamento, SKU, nuovo database, copia di asset Notion, CAP o Golden.
- Wonderlog #26 rimane nel precedente Step3, fuori da questo catalogo. Verifica fisica, account, backup e Store ancora NON VERIFICATA.

## 2026-11-09 — Chiusura integrazione sorgente Maxi-step 3

- Notes-Ecosistema [PR #96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96) merged a `42efc5b9` dopo verify, verify-web e build-web PASS. Fix della validazione titoli con emoji.
- Anna’s Diary [PR #290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290) merged a `0b49de46` dopo Development check, UI5 source e Web PASS.
- Wonderlog [PR #26](https://github.com/riccardopinato/Wonderlog/pull/26) merged a `c238afd8` dopo verify, apple-build e legacy-contract PASS. Fix date bloccate in fase di salvataggio confermato.
- [Stato per app e gate residui](../17-RICERCA-TEMPLATE-UX/UX_STEP3_IMPLEMENTAZIONE_2026_11_09.md): integrazione di codice completata; collaudo fisico, backup/account e pubblicazione Store **NON VERIFICATI**. Nessun CAP/Golden o billing introdotto.

## 2026-11-09 — Maxi-step 3: approvazione UX e implementazioni in PR

- Approvati come piloti gratuiti Book Tracker Notes, Rituali gentili Anna e Trip Planner Wonderlog; i tre prototipi di Maxi-step 2 rimangono documentazione storica.
- [Crosswalk Step3](../17-RICERCA-TEMPLATE-UX/UX_STEP3_IMPLEMENTAZIONE_2026_11_09.md) collega le PR native [Notes #96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96), [Anna #290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290), [Wonderlog #26](https://github.com/riccardopinato/Wonderlog/pull/26) e i writer canonici. Stato fonte in PR, senza dichiarare merge o test fisici non attestati.
- Nessun nuovo Store, API pagamento, database, Golden/CAP o asset Notion redistribuito. Fonte: approvazione utente nella chat del 09/11/2026; Factory baseline d4ed1185.

## 2026-11-09 — Template Engine Maxi-step 2: primi tre progetti UX

- [Matrice dei tre prototipi](../17-RICERCA-TEMPLATE-UX/UX_STEP2_PILOTI_2026_11_09.md) per Notes (#95), Anna (#286) e Wonderlog (#25), con documentazione e HTML interattivo sintetico. Stato: UX DRAFT / pending review.
- Nessun codice Flutter, database, SKU, asset Notion, licenza di terzi, CAP o Golden modificato. Il contratto Template Engine v1 è ancora static-only.

## 2026-11-09 — Catalogazione Notion trasversale a tutte le app

- 12 ZIP analizzati, **11 template unici**; Design Brief duplicato identico internamente. [Audit con E2 strutturale](../17-RICERCA-TEMPLATE-UX/LOTTO_NOTION_2026_11_09_12_ZIP.md), [protocollo routing](../17-RICERCA-TEMPLATE-UX/ROUTING_MULTI_APP.md), [registro JSON](../17-RICERCA-TEMPLATE-UX/TEMPLATE_ROUTING_REGISTRY.json).
- App primaria/secondarie e fonti non assegnabili separati; nessun dato dei ZIP o asset commerciale pubblicato. Preparazione di cataloghi locali nelle app, senza certificare app runtime o store.


## 2026-11-09 — Cinque nuovi export Notion e idea store interno

- Registrati `TPLUX-REF-0002…0006` con audit strutturale dei file forniti; aggiornato `TPLUX-REF-0001` Second Brain da E1 a E2 **solo sulla struttura Markdown/CSV**. Classificati Notes, Anna e fuori-scope CashMate; Weekly Planner marcato export landing incompleto, non planner verificato.
- Conservata in inbox `TPL-STORE-2026-01` come **IDEA VALIDA / BACKLOG**, prezzo ipotetico €3,99 a template originale, prima di alcun billing, SKU, vendita o modifica app. Book Tracker contiene divieto esplicito di redistribuzione/rivendita; nessuna copia di media o ZIP commerciali.
- Nessuna modifica a `REGISTRO_CAPABILITY.json`, Product Bible, Golden, licenze, codice app, backup, APK o Store.


## 2026-11-09 — Second Brain PARA (Abdo): prima scheda E1

- Registrata [TPLUX-REF-0001](../17-RICERCA-TEMPLATE-UX/SCHEDE/TPLUX-REF-0001-SECOND_BRAIN_PARA_ABDO.md) con evidenza E1 su Marketplace e preview pubblica, collegamento originale non accessibile in Notion, E2 non verificata. Crosswalk per Notes e Anna, no duplicazione dei motori esistenti.
- Nessuna redistribuzione degli asset del creatore, elenco acquisti, email, ID Gumroad o contenuti privati. Zero modifiche app, CAP canoniche o Golden; stato research-only.


## 2026-11-09 — Template UX — crosswalk Notes/Anna e protocollo fonti

- Creata [ricerca pubblicabile sui pattern di template](../17-RICERCA-TEMPLATE-UX/README.md): matrice del delta su file sorgente puntati Notes/Anna, protocollo privacy/varianti, roadmap di cinque maxi-step e otto candidati locali `TPLUX` in inbox. Nessun contenuto commerciale o registro personale di acquisti pubblicato.
- Baseline Factory Core `2b3ae9e` (Master 27 / Golden Index 29), Notes `2780847a`, Anna `d82e2d1`. Stato delle app distinto da ipotesi ricavate da titoli e pagine di marketing. Nessuna nuova CAP, donor/Golden, modifica app, release o test applicativo dichiarato.


## 2026-11-09 — Scansione Flutter completa e benchmark World Days CI

- Eseguiti **12 checkout completi Flutter pubblici / 1.390 Dart** e **1 checkout privato FrameLab / 77 Dart**; per ciascuno fissato SHA e registrati i conteggi. Zero match dei soli pattern API legacy cercati; 573 segnali euristici REVIEW non trasformati in bug senza triage.
- Eseguito benchmark `SavedPage` e `AroundTheWorldPage` World Days su `bb662cb2`, Flutter 3.47.3, 8 scenari 10/50/150/300 record, 7 sample ciascuno. Tempi/figli/widget nel [JSON](../12-CAPABILITY-E-IMPLEMENTAZIONI/WORLD_DAYS_LIST_BENCHMARK_2026-11-09.json); non sono frame GPU o benchmark fisici.
- Dataset distribuito: 296 record, massimo 4 per Paese. Nessuna prova di rallentamento monotono e nessun refactor lazy immediato autorizzato. Identificato un **overflow reale di 12 px a viewport 390px in AroundTheWorldPage**, [World Days issue #52](https://github.com/riccardopinato/World-Days/issues/52).
- [Report completo](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_FLUTTER_COMPLETO_WORLD_DAYS_BENCH_2026-11-09.md) e [evidenze scansione](../12-CAPABILITY-E-IMPLEMENTAZIONI/FLUTTER_FULL_SOURCE_SCAN_2026-11-09.json) aggiunti come fonti; nessuna modifica a registry CAP, app production code, App Factory Core o Golden.

## 2026-11-09 — HTML.it Flutter: 5 maxi-step catalogazione + audit mirato

- Inseriti nel catalogo [report evidence-gated](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_HTMLIT_FLUTTER_5_MAXISTEP_2026-11-09.md) e [registro JSON delle 12 estrazioni](../12-CAPABILITY-E-IMPLEMENTAZIONI/HTMLIT_FLUTTER_REFERENCE_CROSSWALK_2026-11-09.json) dalla guida HTML.it di 37 lezioni (2019–2020). Provenance: repo esempi SHA pinned, nessun LICENSE root, codice commerciale non approvato.
- Dedup contro le **199 CAP** correnti: **0 nuovi CAP**, **0 associazioni**, **0 transizioni di stato/decisione prodotto**. Fonte esterna E0 per pattern/learning, non donor né Golden.
- Audit campionato su repository e percorsi Flutter: lazy lists presenti in Anna/Notes; World Days due schermate a costruzione eager **da benchmarkare**; Anna backend IO/Web condizionale; World Days content-pack temporanei e rollback; CamperBoss geolocation service/permission health; TrailPath stack moderno documentato. Nessun bug di performance e nessun comportamento dispositivo dichiarati provati.
- Nessuna modifica a repo delle app, App Factory Core, AppLab, cloud, dati o rilasci. Zero promozioni Golden; scan completo su checkout e benchmark restano gate successivi.
- Aggiunto strumento Python read-only per segnali di API Flutter legacy (JSON file/line) e quattro unit test sintetici PASS in ambiente locale + test CI della deduplicazione crosswalk; non equivale a scansione totale dei sorgenti.

## 2026-11-08 — Vision Board lotto 2: 20 segnalazioni / 19 fonti nuove

- 13 repository con SHA e source E1, 5 directory Topics E0, 1 alias “Mymind Clone” non verificato, 1 duplicato dell'URL VBR-0001; creati VBR-0021..0039 e audit/intake/manifests.
- Corrette ownership di React Grid Layout, Muuri, React Easy Crop, PLANKA, Focalboard. Licenze: 7 MIT in LICENSE, 1 MIT README/header, 1 tldraw production license, 1 AFFiNE mixed, 1 AppFlowy AGPL, 1 PLANKA Fair Use, 1 Focalboard AGPL source (MIT compiled only).
- VBE-015..028 aggiunte, cumulative 28 opportunità candidate; confronto CAP/Golden e priorità Notes/Anna. Nessun donor/Golden certificato, nuova CAP canonica, codice app, task database, provider, roadmap o test runtime modificato.


## 2026-11-08 — Vision Board lotto 1: 20 fonti e 14 estrazioni candidate

- Registrati VBR-0001..0020: 15 repo reali E1 SHA pinned, 5 directory Topics E0; risolti Ninjafishy/Boardfish e viktorkpkn/ImageCanvas; 20 schede individuali e JSON aggiornato.
- License gate: 4 MIT LICENSE, 1 MIT in README frontend, 2 restrittive/proprietarie, 8 senza LICENSE nel tree. Boardfish blocca copia commerciale; moodboard-studio ha solo documentazione/LICENZA.
- Create 14 opportunità VBE di donor/pattern/Golden/CAP (solo candidate); collegamenti al catalogo CAP, focus Notes/Anna e audit comparativo. Nessuna CAP o Golden ufficiale promossa, nessun codice app/roadmap/Factory modificato.


## 2026-11-08 — Nuova sezione 15-VISION-BOARD

- Creata una sezione autonoma per Vision Board, separata dalla ricerca Machine Learning, con Inbox VBR, registro JSON, protocollo di audit, template repository, estrazioni candidate, matrice consumer e crosswalk CAP/Golden.
- Focus di ricerca Notes-Ecosistema e Anna's Diary; possibili riusi secondari in FrameLab e Wonderlog solo se coerenti con le rispettive Product Bible.
- Riuso-first: Golden Infinite Canvas/Ink e CAP esistenti prima di nuovi editor/registri. Nessuna fonte VBR aggiunta senza URL dell'utente; **0 repository auditati**, nessuna nuova CAP, Golden certificata, modifica alle app o roadmap.


## 2026-11-08 — Machine Learning secondo lotto: 20 riferimenti, 11 fonti nuove

- Analizzati 20 riferimenti GitHub forniti dopo il primo lotto, con dedup SHA: **11 nuovi record MLR-0011..0021**, **9 duplicati/alias** gia catalogati; totale **21 fonti uniche** in sezione 14.
- Create 11 schede E1 con URL canonico, commit, licenza codice, evidenze, classi Donor/Golden solo candidate, crosswalk CAP, consumer e gate. Aggiornati Inbox, JSON, README e audit comparativo `AUDIT_20_RIFERIMENTI_ML_LOTTO2_2026-11-08.md`.
- Corretti link GitHub: `interpret-ml/interpret` -> `interpretml/interpret`; `dvc-org/dvc` -> `treeverse/dvc`; nome abbreviato `500-AI-Machine-learning-Projects` ricondotto a MLR-0007.
- Evidenze concrete: ONNX Runtime Android Java/JNI e JS Web; tflite-micro targeting microcontroller; coremltools toolchain Python, non runtime iOS; fastText archiviato; awesome-mobile-ai loader/predict ancora placeholder; Awesome LLM Apps include esempi Ollama/Qdrant locali e altri con Qdrant Cloud.
- Nessuna promozione Donor/Golden, nessuna nuova CAP, codice app, peso modello, dataset, cloud o test su device. Licenze dei modelli e dei dataset separati; benchmark e footprint NON MISURATI.


## 2026-11-08 — Machine Learning: audit MLR-0001..0010 (primo lotto)

- Registrati 10 riferimenti nel catalogo `14-MACHINE-LEARNING`: 10 schede E1 a SHA, Inbox aggiornata, registry JSON, audit comparativo per priorita e riuso.
- Ispezionati codice e license di scikit-learn, mljs (+ 5 moduli satellite), River, Microsoft ML-For-Beginners, Karpathy, Homemade ML, 500 AI Projects, Kaggle Solutions (fonte provvisoria), EthicalML Awesome Production e Awesome Machine Learning.
- Correzioni: Homemade richiede NumPy; mljs e organizzazione, non singolo SDK Dart; 500 AI manca LICENSE in root; Awesome ML LICENSE ambiguo; Kaggle Solutions senza URL preciso, rappresentato provvisoriamente da faridrashidi/kaggle-solutions.
- Donor/Golden soltanto candidati; **zero nuove CAP, nessun test app, nessuna modifica a Golden/Factory/app**, licensing di dataset/pesi/link esterni non ereditario.


## 2026-11-08 — Creazione sezione autonoma Machine Learning

- Creata **14-MACHINE-LEARNING** con README, Inbox, registro fonti JSON, protocollo di audit, template singolo repository e crosswalk agli studi ML23 e ML10 già presenti.
- La sezione supporta nuovi link GitHub con ID MLR progressivi, audit al commit SHA, separazione codice/pesi/dataset, extraction Donor e Golden **solo candidati**, confronto anti-dup con CAP canoniche e gate E0–E5.
- **Zero nuovi repo registrati**, nessuna nuova CAP o variazione stati, nessuna modifica alle app, ad AppLab, ad App-Factory-Core o a Golden Index/Registry; il catalogo canonico resta l'unica source of truth delle capability.

## 2026-11-08 — Comando Stelle: refresh OSS95 e raccomandazioni product-admission

- Connessione GitHub autorizzata ma endpoint `user/starred` bloccato: **nuove stelle live non verificate**; usato il pacchetto curated OSS95 dichiarato, senza spacciarlo per stelle autentiche.
- 95 repository controllate per metadata `pushed_at`; 85 invariati, 10 aggiornati; tutti e 10 i blob README identici, titoli dei commit verificati solo per orientamento (non audit completo di code diff).
- Snapshot persistito in `12-CAPABILITY-E-IMPLEMENTAZIONI/OSS95_SOURCE_SNAPSHOT_2026-11-08.json`.
- Audit su 39 CAP / 56 associazioni nella matrice `AUDIT_AMMISSIONE_PRODOTTO_OSS95_39_CAP_2026-11-08.md`. Le raccomandazioni sono aggiunte come metadati separati al registro; **199 CAP/441 associazioni, stati tecnici, decisioni product owner e score invariati**.
- Nessuna CAP nuova, nessuna implementazione o approvazione automatica. Gate Notes #60 e catalogo #41 ancora aperti; Anna Calendar Direct #199 ancora draft.

## 2026-11-08 — Formalizzazione OSS95: 39 CAP E0

- CAP-0161..CAP-0199: 39 contratti E0, 56 app-associazioni in PROPOSTA / DA_VALUTARE; 199 CAP e 441 associazioni totali.
- Nessuna implementazione o donor certificato; sei file kit per ogni CAP, riscontro non duplicazione e stime euristiche.
- Rigenerate schede, ranking e code tramite scripts/build_catalog.py e status generator.


## 2026-11-08 — OSS95: license-file follow-up 26/26

- Completata la lettura documentale dei file di licenza di **26 repository GitHub** che l'API aveva classificato `NOASSERTION/UNKNOWN`; classificati 7 permissivi scoped, 8 copyleft/misti, 8 source-available restrittivi, 1 documentale, 2 indicizzatori/componenti.
- Tutti i 26 rimangono abilitati all'estrazione capability: 90 facets già presenti nel totale 329; nessuna esclusione per mancato SPDX API. Il riuso codice non viene erroneamente dichiarato MIT/libero.
- Aggiornati `AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json`, `REGISTRO_CAPABILITY.json` e report `AUDIT_LICENZE_26_OSS95_2026-11-08.md`. 160 CAP, 385 associazioni e 39 candidate E0 invariati.


## 2026-11-08 — Capability OSS95 audited intake

- Audit documentale su 95 repository GitHub (README, metadata, licenza REST; percorsi README non standard recuperati), con 329 associazioni repository-funzione, 47 CAP tematicamente corrispondenti e 39 candidate E0 con decisione prodotto DA_VALUTARE.
- Aggiornato il JSON canonico `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json` con `oss95_research_intake` e fonti per CAP già censite. **160 CAP / 385 associazioni invariati**, nessuna promozione CI/device/roadmap o copia codice OSS.
- Report e atlas: `12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_COMPLETO_OSS95_CAPABILITY_2026-11-08.md` e `AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json`; 12 batch sorgente e 6 fallback README.
- Queste 95 voci sono repository selezionati in chat; lista stelle account live non verificata. Le 39 candidate non ricevono ID permanenti senza anti-dup, scheda, kit, rigenerazione e PR/CI.


## 2026-11-07 — Anna's Diary Step 3: 74 capability con prove aggiornate
- Nuovo [crosswalk Anna 74/74](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_ANNA_STEP3_RECONCILIAZIONE_2026-11-07.md) per confrontare il registro con il main Anna `dc601002` (PWA Web-first). CAP-0152 e CAP-0160 con codice/test parziali, non con perimetro full certificato; CAP-0015 + #270, CAP-0025, CAP-0069 e CAP-0067 documentate con limiti di evidenza.
- Nessuna promozione degli stati canonici, nessuna rigenerazione delle viste, nessun cambio score/facilità o Golden. Il follow-up deve aggiornare il JSON e rigenerare con i tool di repository e check esatti.

## 2026-11-07 — Notes 88/88 crosswalk esplorativo, nessuna promozione CAP
- Aggiunta la matrice [Notes 88/88](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_NOTES_CAP_88_2026-11-07.md) e CSV correlato: 16 SOURCE_REPORTED, cinque MVP #64 parziali e audit per tutte le 88 associazioni sul main Notes `abbcab3b`.
- Nessuna modifica a REGISTRO_CAPABILITY.json o viste generate: il gate post-roadmap #41 resta valido, niente DEVICE_VERIFIED/RELEASE dedotti.

## 2026-11-04 — ML10 P1/P2/P3, consumer Notes/TasteAI e revisione 160/385
- Core #71/#73: motori numerici reference local-only con CI; Core #74/#75: evidenze e cinque Golden DRAFT con date Registry allineate, nessuna promozione E5.
- Catalogo #37: audit 160 CAP/385 app-link, quattro score, venti stime iniziali e tre prove sorgente parziali; nessuna percentuale senza motivazione.
- Notes #57: MinHash/LSH suggerimenti duplicati read-only con conferma apri-editor, non merge; TasteAI #2: kNN ricette correlate con vincolo Premium e cinque lingue.
- Aggiornamento postmerge: CAP-0116 Notes SOURCE_REPORTED e stima 83→85; TasteAI CAP-0044 evidence scoped senza alterare lo score/anti-spreco; 160 CAP e 385 associazioni conservate.
- Vision/audio: [screening tecniche e modelli](../12-CAPABILITY-E-IMPLEMENTAZIONI/ML10_MODEL_SCREENING_2026-11-04.md), licenze e test OEM restano gate aperti. Nessun nuovo peso o store release.


## 2026-11-04 — Ammissione completa ML23 a capability e Golden readiness
- Convertite 10 idee ML26 in CAP-0151...0160, 60 file kit E0, mappa 23/23 con 13 riusi CAP, cross-app score e facilità per 160 CAP e 385 associazioni.
- Cinque engine family con dipendenze a catena, contratti E0->E5, baseline Core @6cbb3449; nessun Golden o runtime app falsamente promosso.
- Vista e classifica rigenerate dal solo REGISTRO_CAPABILITY.json; catalogo storico ML conservato con collegamento.

## 2026-11-04 — Intake 23 algoritmi ML classico/on-device
- Analizzato Machine Learning.txt e verificato con documentazione ufficiale Android e scikit-learn; identificati 23 pattern, di cui 10 candidature di comportamento distinte e 13 riusi/estensioni di CAP esistenti.
- Aggiornata l'INBOX con ID ML26-001…023 e creato catalogo di fattibilità, rischi, priorità di analisi e stime per app; nessuna promozione CAP o certificazione app/Golden.
- Baseline Factory @6cbb3449… (Master 27, Golden v28). Nessuna modifica al registro canonico, ai punteggi esistenti o alle app.

## 2026-11-04 — Audit integrale Golden v28, tutte le app
- Revisione 147 CAP, 342 associazioni storiche e 31 repository reali, con 10 score e 67 valori facilita ricalibrati sulla nuova evidenza; altri valori conservati.
- Tre CAP nuove (0148 Smart Inbox, 0149 JSON Canvas, 0150 Daily Hub), un consumer parziale Wonderlog, kit e indici rigenerati.
- Provenienza SHA e delta conservati nel registro e nei CSV; nessuna nuova certificazione device/Store/Golden.

## 2026-11-04 — Notes: audit 4 fonti, crosswalk con stato codice
- Importati nell'Inbox i nove identificativi stabili NOTES-AUD4-001…009 e la mappatura CAP/issue per Notes, conservando le ricerche precedenti.
- Distinti MVP già su main, delta ancora aperti e nuove responsabilità (JSON Canvas); registrate le quattro fonti AI Valley, Hugging Face, GitHub e GitLab senza clonare codice, modelli o UX proprietarie.
- Registro canonico e viste operative lasciati invariati: necessaria una riconciliazione successiva con source SHA, scope CAP e rigenerazione `build_catalog.py --check` prima di qualsiasi promozione stato.

## 2026-11-04 — GitHub Projects: correzione collaudo live
- Creato realmente il GitHub Project personale `App Factory — Capability Dashboard` (Project #1) con campi e quattro viste, grazie al secret `APP_FACTORY_PROJECT_TOKEN`.
- Primo run live: sei record pilota creati, ma la lettura API immediata non riportava ancora l'ultima coppia `Android-Omni-Cleaner / CAP-0039`; il gate ha correttamente impedito l'import massivo.
- La verifica di lettura ora effettua tentativi con intervalli progressivi **senza effettuare nuove scritture durante la verifica**; mai dichiarare `PILOT_PASS` o `FULL_SYNC_PASS` finché il riscontro API non è positivo.
- Test di regressione per indicizzazione ritardata e fail-closed senza duplicazioni; nessuna cancellazione, modificazione del registro canonico o repo app.


## 2026-11-03 — Contenimento rate limit GitHub Projects
- Caricamento limitato a 180 coppie CAP/app per run, intervallo minimo 1,3 secondi tra mutation GraphQL, ripresa incrementale automatica nei run successivi. Distinguere `BATCH_SYNC_PASS` da `FULL_SYNC_PASS`; non promettere import completo quando il batch è ancora parziale.
- Cron ogni quattro ore, test su ripartenza batch senza duplicazioni. Il Project live resta BLOCCATO fino alla configurazione sicura del token `APP_FACTORY_PROJECT_TOKEN`.


## 2026-11-03 — GitHub Projects V2 (pilota e mirror automatico non distruttivo)
- Introdotti `scripts/projects_sync.py`, regression test e workflow manuale/push/cron per un solo Project riutilizzabile attraverso tutte le 48 app, su 342 combinazioni CAP/app.
- Creazione/ripresa Progetto V2 e 4 campi ordinabili tramite GraphQL, 4 viste; primo pilot di 6 elementi su 3 stati con rilettura, poi estensione automatica a tutte le coppie quando i gate live passano.
- Source of truth non cambia. Nessuna cancellazione, archiviazione o modifica di cartelle storiche; nessuna app toccata. `APP_FACTORY_PROJECT_TOKEN` richiesto per esecuzione live: prima dell'attivazione il sistema esegue **solo test offline/dry-run**, nessuna creazione Projects dichiarata.
- Riferimento operativo: `12-CAPABILITY-E-IMPLEMENTAZIONI/GITHUB_PROJECTS_MIRROR.md`.


## 2026-11-03 — Sottocataloghi per app con stati distinti
- Sotto `12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/` ogni app ha tre file generati: `DA_VALUTARE.md`, `GIA_INTEGRATI.md`, `DA_VERIFICARE.md`, più `TABELLA.csv` con punteggi numerici esportabili e ricercabili nell'anteprima GitHub.
- Le schede storiche `PER_APP/<app>.md` non sono eliminate e puntano alle viste operative. Indice `PER_APP/README.md` con conteggi per app.
- Una singola classificazione per coppia app/CAP, nessuna soglia arbitraria e gestione prudente di source riportate/riuso parziale. Test di regressione coprono inventario e mutua esclusione delle tre categorie.
- Nessun cambio di stato o di codice delle app: è riorganizzazione derivata dal registro canonico.


## 2026-11-03 — Correzione: nessuna soglia fissa per le idee da valutare
- La soglia **85/85** citata in precedenza era soltanto un esempio dell’utente e **non è un criterio operativo permanente**.
- `DA_VALUTARE.md` ora comprende tutte le combinazioni app-capability non integrate, ordinate per Score e facilità come due dimensioni indipendenti; esempi reali 94/80 e 90/80 non vengono più relegati in una categoria di minor interesse.
- Filtri numerici applicati solo su esplicita richiesta; preservate la separazione per app, le prove `GIA_INTEGRATI.md`, i casi di riuso parziale e l’archivio storico. Aggiunto test di regressione.


## 2026-11-03 — Classifiche operative integrate vs da valutare
- Aggiunte due viste principali: `DA_VALUTARE.md` e `GIA_INTEGRATI.md`. Lo storico CAP/IA resta completo ma non viene più interpretato come coda di nuove implementazioni.
- Classificazione **per associazione app-capability**, con spotlight iniziale Score >=85 / Facilità >=85% poi superato dalla correzione senza soglie predefinite. Separati i record `SOURCE_REPORTED` o con prova insufficiente, da verificare prima di suggerirne lo sviluppo.
- Registro `IA-2026-11-02/INTEGRATION_STATUS.json`: Phone Guard #50/#62 confermati in codice, #44 Battery Guard con source dichiarata e gate codice, #12 TasteAI e #39 Anna parziali, #37 Anna con source riportata.
- Generatore `scripts/build_status_views.py`, integrato nel normale `scripts/build_catalog.py` e nel gate CI; test per preservare tutte le 100 idee ed escludere quelle con codice verificato.
- Nessuna modifica a repository app, Product Bible, roadmap, CAP source of truth o classifiche storiche. Master corrente v27 / Golden Index v28 letto da CURRENT.yaml, 03/11/2026.



## 2026-11-03 — Anna CAP evidence audit / Golden Index 26
- Factory baseline aggiornata a `App-Factory-Core@a3c65963` (Master 27, Golden Index v26); nessuna riscrittura della fonte Factory.
- Stati di Anna verificati nel registro canonico per CAP-0014 (CI_VERIFIED), CAP-0027 e CAP-0055 (SOURCE_CONFIRMED); CAP-0069/0077/0111 mantengono CI_VERIFIED ma con path/evidenze aggiornati. 147 CAP totali.
- Viste e schede derivate rigenerate; report [AUDIT_ANNA_CAP_2026-11-03.md](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_ANNA_CAP_2026-11-03.md).
- Nessuna promozione artificiale a DEVICE_VERIFIED/RELEASE; #215 Privacy V2 resta DRAFT/ON HOLD. Le due idee P3 scartate restano fuori.


## 2026-11-02 — 15 idee Anna formalizzate come CAP, con deduplicazione
- Risolti 15 ID AD-NL26: 7 nuove capability CAP-0141…0147 e 5 ampliamenti/riusi CAP-0023, CAP-0024, CAP-0055, CAP-0069, CAP-0072. Score tecnico canonico separato da priorità editoriale idea (4 P1, 11 P2).
- Registro JSON da 140 a **147 CAP**, 7 kit livello 1 con 6 file canonici ciascuno e compatibilità Anna preliminare; rigenerate viste, matrice, ranking, schede per app e indice kit. Tutte le nuove app_states PROPOSTA; source paths esistenti non equivalgono a funzione implementata.
- Precedenti due P3 scartate non reinserite. Privacy #215 resta DRAFT/ON HOLD e nessun codice app, prodotto, licenza o prezzo modificato.


## 2026-11-02 — Esclusione delle due proposte NotebookLM P3 dal catalogo attivo
- Su richiesta dell'utente, rimosse le due idee P3 dal dossier Anna e dalle relative mappature. Classifica attiva: 15 idee, 4 P1 e 11 P2.
- Aggiornati indici, collegamenti e conteggi, senza cambiare le 140 CAP canoniche. L'importazione iniziale rimane nella cronologia Git; nessuna riscrittura della storia.
- Nessuna modifica ad Anna, roadmap, pricing o PR Privacy #215 in sospeso.


## 2026-11-02 — Valutazione proposte Anna's Diary da NotebookLM
- Fonte testuale utente SHA-256 0ac109c023523b466f71cfefe53232733d5450b7fb1164da02f560220a6c5613; 15 proposte P1/P2 con score editoriali, priorità, sovrapposizione source e gate.
- Mappati i riferimenti CAP rimasti nella fonte senza duplicare/modificare le 140 capability canoniche; riferimenti incrociati in 11 idee, 12 capability, 06 sinergie e 08 monetizzazione.
- Nessuna modifica ad Anna, roadmap, tariffari, Store o Privacy #215 ON HOLD. Fonti esterne per limitazioni widget, abbonamenti e benchmark esplicitamente distinte dal documento.


## 2026-11-02 — Valutazione strutturata lotto idee IA: 100 + 6 extra, 14 fusioni
- Recuperate e mantenute tutte le idee originali numerate #1–#100, con 100 schede individuali `IA26-001…IA26-100`. Catalogate altre sei idee autonome non numerate (`IA26-E01…E06`), e tutte le 14 fusioni successive con esito motivato.
- Ciascuna scheda include score U/D/V/M/F/S/R, formula di priorità, MVP proposto, decisione preliminare, collegamento ad app esistenti, monetizzazione, donor/link identificabili, blocchi e prossimo controllo.
- Create classifica completa, ranking tematici (facilità, monetizzazione, viralità, riuso, rischio), indice navigabile e metodologia con provenienza degli allegati/hashes e fonti esterne.
- Tutte le idee restano PROPOSTA/ANALISI NON APPROVATA; nessuna app, Product Bible, roadmap, CAP o repository codice modificato. Scoring comparativo editoriale, senza misure di domanda/fatturato.


## 2026-11-02 — Incrementale 31 repository, 8 capability Anna CI exact-head
- Inventario: 31 repository accessibili, nessun nuovo repository o default branch modificato; 3 SHA variati (Anna's Diary, App-Factory-Core, archivio stesso). Il self SHA e' volutamente pre-PR. Factory CURRENT resta Master v27 / Golden v23; commit osservato `63dd5e4f`, solo ledger di observability nel diff.
- Anna's Diary: 7 commit nuovi da `88efdfa9` a `fb476545426fb6bf290e74f53e735fa13616e4e9`. Confermati sorgenti, test e check CI exact-head per CAP-0001, CAP-0002, CAP-0003, CAP-0005, CAP-0069, CAP-0077, CAP-0111 e CAP-0113; stato Anna promosso a `CI_VERIFIED`, senza toccare gli stati delle altre app. PR sorgenti #186, #188, #191, #193, #195, #201, #203 e #204.
- Nuove quick wins Anna PR #206: duplicazione in bozza, rinvio task, recupero scaduti, anteprima domani e avvisi sovrapposizione. Riutilizzano responsabilita' gia presenti nel catalogo; non assegnati nuovi CAP e non attribuito il livello CI a capability piu' ampie non interamente coperte (CAP-0101/0102).
- Scoring: rafforzata la sola evidenza documentata per CAP-0001, CAP-0002 e CAP-0111; punteggi ricalcolati dal modello canonico. Provenienza storica conservata come `origin_source` quando la fonte primaria e' passata al codice esatto.
- Limiti: Weekly Review +118 ha accettazione generale utente ma non matrice tecnica device; C2 non ha 70 coppie screenshot approvate; C1 richiede prova permessi su telefono; Google Calendar diretto PR #199 e privacy PR #200 restano draft/bloccate. Build +120 predisposta, non certificata. Nessun `DEVICE_VERIFIED`, `RELEASE` o approvazione di nuova roadmap.

## 2026-11-01 — Audit completo delle 61 capability Anna's Diary
- Copertura 61/61 associazioni del registro Anna allo SHA `Agenda-per-Anna@88efdfa9` con percorso sorgente per CAP e scheda di compatibilità individuale; totale 62 documenti di audit.
- Classificazione: 26 sorgenti coerenti, 21 riusi parziali, 2 nuove candidate, 8 fuori scope, 2 pianificate, 2 infrastrutturali. Presenza di file ≠ test runtime.
- Ricalibrate 29 stime editoriali di facilità per Anna, senza modificare Score, evidenza app, roadmap, Product Bible o codice Flutter.
- Tabella Anna arricchita con colonne Esito sorgente e Analisi compatibilita; la CI valida catalogo e derivazioni. [Rapporto](../13-KIT-INTEGRAZIONE/ANNA_FULL_AUDIT_61_2026-11-01.md).
- Nessun APK, inferenza modello, test fisico o prova di release inventati. Tutte le 140 CAP rimangono identificate univocamente.


## 2026-11-01 — Audit Anna's Diary e 3 kit con codice Dart preparato
- Verificata in lettura `Agenda-per-Anna@88efdfa9`, Product Bible, roadmap e API `CalendarFreeSlot`, `UnifiedAgendaEntry`, `AgendaItem`, `WeekData`, `DayJournal`, `MediaAssetStore`.
- Preparati contratti puri originali e test per CAP-0102 rescheduling preview (nessun writer), CAP-0111 weekly review (soli task privati, date completamento non inventate), CAP-0114 privacy text gate (Vault/Noi/ciclo/media esclusi).
- Ricalibrate facilità stimate Anna: CAP-0102 80→70, CAP-0111 90→80, CAP-0114 45→40, CAP-0134 55→35. CAP-0134 non prioritario per Anna; CAP-0138 non associato.
- Workflow `kit-dart-compat.yml` esteso a analyze+test; nessuna modifica sorgente/roadmap Anna, stato app `PROPOSTA` invariato, nessun APK/device claim. [Audit](../13-KIT-INTEGRAZIONE/ANNA_COMPATIBILITA_2026-11-01.md).


## 2026-11-01 — Prima compatibilita mirata kit CAP-0134/0114/0138
- App Notes-Ecosistema `3fd9b0d` analizzata in lettura: Flutter 0.56.3+74, contratti documenti/media/whiteboard/audio, assenza runtime ONNX dichiarato nel pubspec.
- Tre moduli Dart originali, sei file codice/test: decoder parziale RGB/preprocessing/softmax DocRex, preview email/IBAN parziale, indice stroke-audio e codec versionato. Workflow GitHub di analyze+test; non compilati APK, non importati modelli.
- Schede dettagliate riscritte con fonte, limiti e file preparati; percentuali di integrazione stimate ricalibrate per Notes/Anna/PDF. Nessuno stato app promosso; `PROPOSTA` resta.
- [Audit](../13-KIT-INTEGRAZIONE/COMPATIBILITA_2026-11-01.md). Licenza Redact `other`; DocRex FP32 solo tre classi; MOSS 0.9B non integrato.


## 2026-11-01 — Libreria 140 kit, percentuali integrazione e descrizioni per app
- Creati 140 kit individuali in `13-KIT-INTEGRAZIONE/` con sei documenti ciascuno, note di provenienza e caveat. Stato dei kit `RIFERIMENTI_ACQUISITI`, nessun codice donor estratto e nessuna licenza automaticamente approvata.
- Aggiunti i valori `integration_ease_percent` per ogni associazione CAP/app (324): stime editoriali iniziali, memorizzate in JSON, per-app, distinte dallo Score e dalla prova reale di compatibilita.
- Aggiornato generatore `scripts/build_catalog.py` e 48 viste per app: Score, **Facilita integrazione (%)**, **Descrizione breve**, **Kit tecnico**. Classifica e tutte le schede CAP ora rimandano ai kit.
- Il check blocca percentuali mancanti/fuori range e kit incompleti; nessuna modifica agli stati di implementazione o ai repository delle app.


## 2026-11-01 — Archiviazione totale 56 idee Hugging Face Notes (ricerche #29–56)
- Salvate integralmente **16 idee #29–44** e **12 idee #45–56** in due ricerche nuove, con fonte, URL, score editoriale originale, livello di verifica, limiti e gate per futuri test Flutter/Android.
- Catalogo ora **140 capability**, 48 app/idee, 324 associazioni, 18 P1 / 72 P2 / 50 P3. Creati CAP-0114…CAP-0140 (27 nuove responsabilita), #45 e #55 sullo stesso CAP di generazione artefatti visuali modificabili.
- Collegate capability preesistenti senza cancellare o rinumerare ID; aggiornati JSON, ranking, matrice, schede per app, Inbox, README, changelog.
- Caveat delle fonti: Paper2Any e CiteAudit demo runtime error; Tadpole/Math Ink troppo pesanti per APK base; DocRex Apache-2.0/5.8MB ma 3 classi; FormStruct/FUNSD+ diritti custom; DetectiveSAM `other`; alcune fonti solo pattern di ricerca e non app eseguibili.
- Nessun codice app, Product Bible, Golden o nuova roadmap modificati; nuove associazioni sempre `PROPOSTA`. Nessun peso, dataset o codice Hugging Face incorporato.
- Schede: [terza ricerca](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md) e [quarta ricerca](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md); fonte factory `riccardopinato/App-Factory-Core@63dd5e4f703cb23e4095a72beb253720bc1ca9a1`.


## 2026-11-01 — Snapshot incrementale 31 repository e A1/A2 Anna's Diary
- Enumerati 31 repository del proprietario; nessun nuovo repository rispetto all'inventario. Registrati nome, default branch e SHA HEAD osservati, come baseline metadata per futuri diff, senza dichiarare audit sorgente dei 31 HEAD.
- CAP-0003 aggiornata da PROPOSTA a SOURCE_CONFIRMED per Agenda-per-Anna: codice `lib/src/event_preparation.dart`, test `test/v107_a2_event_preparation_test.dart` e source SHA `88efdfa9`; score evidenza 2→4 e priorita P3→P2.
- Nuova CAP-0113: conversione di appuntamento privato passato in ricordo, SOURCE_CONFIRMED per Agenda-per-Anna, PROPOSTA per Wonderlog; codice e test A1 a SHA `88efdfa9`.
- Totale 113 CAP, 48 app/idee e 275 associazioni. Viste rigenerate; nessuna Product Bible, roadmap o codice app modificato.
- APK firmato +116 documentato, ma V116-01…V116-12 sono NOT VERIFIED su dispositivo: SOURCE_CONFIRMED non significa DEVICE_VERIFIED o RELEASE.

## 2026-11-01 — Seconda ricerca Hugging Face «to do»: idee 13–28
- Conservate 16 ulteriori proposte per Notes-Ecosistema (adattamenti essenziali Anna's Diary/FocuSense) con fonti Hugging Face e distinzione tra funzionalita effettivamente documentate e proposte progettuali.
- Registro canonico da 101 a **112 CAP**: introdotti 11 nuovi ID CAP-0102…CAP-0112, riusati quelli esistenti per Backward Planning, Eisenhower Board, Alternative Plans, Focus Protection e Meeting Load Heatmap.
- Nuovo snapshot: 48 app/idee, 273 associazioni, 17 P1, 59 P2, 36 P3; aggiornati ranking, matrice, stati, schede, Inbox, indici e changelog.
- Fonti: Yuga Planner Apache-2.0 (dipendenze esterne da auditare), Plan My Day Apache-2.0 (dataset sperimentale, pesi modello sotto licenza separata), MiniAppBench (specifiche, non codice prodotto), HermesAgent release notes per flashcard.
- Ogni nuova feature resta `PROPOSTA`, senza code/device proof, merge automatico in roadmap o modifica di repository app. Nessun codice/modello/dataset esterno incorporato.
- Scheda: [Seconda ricerca Hugging Face](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md).


## 2026-11-01 — Hugging Face «to do» per Notes-Ecosistema / Anna's Diary
- Archiviate 12 proposte nella ricerca dedicata, con punteggi originali 0–10, fonti verificate vs link non probanti, licenze e impatto sull'APK.
- Aggiunte 10 capability uniche CAP-0092…CAP-0101; collegate e riusate CAP-0017/0018/0028/0029/0031/0032/0033/0055/0075 senza duplicarne la responsabilita.
- Registro ora 101 CAP (16 P1, 50 P2, 35 P3), 48 app/progetti, 257 associazioni; aggiornate viste generate, Inbox e indici.
- Tutte le nuove feature sono PROPOSTA (non IN_ROADMAP, non CODE/CI/DEVICE); nessun code/dataset OSS copiato, nessuna modifica ai repository delle app.
- Fonti: https://huggingface.co/search/full-text?q=to+do e scheda locale di ricerca.


## 2026-11-01 — Ricerca r/BestGitHubRepos e aggiornamento capability
- Esaminati post indicizzati settembre-ottobre 2026 e README/metadati GitHub di 11 donor, con commit e licenze snapshot; pagina listing Reddit non accessibile, audit dichiaratamente non esaustivo.
- Aggiornato il registro da 82 a 91 capability (nuove CAP-0083..CAP-0091), 48 app/progetti collegati, 243 associazioni, punteggi P1=15, P2=46, P3=30.
- CAP-0031, CAP-0032, CAP-0033, CAP-0077 e CAP-0078: aggiunte fonti di ricerca senza duplicare capability.
- Ampliati catalogo donor OSS, matrice riuso, inbox nuove idee (DevPocket Tools, DiskScope, GeoPulse Live, DeskPilot) e nota di ricerca con licenze e limiti.
- Nessun repository app alterato, nessun modello/code/assets copiato; GPT/LLM/API prezzi indicati da directory esterne NON assunti come verificati.

## 2026-11-01 — Capability registry multi-app e manutenzione ricorrente
- Audit documentale trasversale: 31 repository inventariati, 23 con tree/roadmap o README pertinenti campionati; fonti Project, vecchi audit, Master/Golden, Design-App e riferimenti OSS.
- Catalogate 82 capability con ID stabili, 39 app/progetti possibili consumer e 212 associazioni per app; le priorita sono P1 14, P2 42 e P3 26, indicative e distinte dalle severity dei bug.
- Inseriti catalogo canonico JSON, schede singole, viste per ogni app, matrice, classifica, stato documentale e inventario nuove repository.
- CI valida coerenza di score, ID, stati, fonti, schede e viste; il task programmato puo aggiornare il catalogo via PR dopo confronto con repo nuovi o modificati.
- Nessuna app modificata, nessuna nuova funzione implementata, nessuna certificazione fisica dedotta. Licenze esterne da riverificare prima di integrare.

## 2026-10-30 — Audit trasversale idee e innovazione (solo archivio)
- Rilette fonti Project, backlog, 16 idee Web Utility, repository OSS/Design-App e roadmap app pertinenti; evidenziata distinzione GIA IMPLEMENTATO vs GAP vs APPROVATO STORICO vs NUOVA IPOTESI.
- Registra 30 interventi di prodotto, riuso/provider e priorità con evidence scope.
- Conserva 7 nuove ipotesi in Inbox senza promuoverle a classifica né cambiare roadmap app.
- Evita duplicati: Shopping/Workout/Calendar/Map/Threads/Review già presenti in Anna; lifecycle Anna e Notes; Anti-Waste TasteAI; suite Notification/Phone.
- Verifica licensing Open-Meteo commerciale e POI/OSM/Overture; distingue 632 cataloghi stelle da deep source audit.
- Nessun codice di app o Golden modificato; nessuna certificazione/release creata.


## 2026-10-30 — Audit ChatGPT vs GitHub
- Classifica espansa a 37 voci, 7 colonne (chat, main/PR, codice, allineamento) e 37 descrizioni in elenco.
- Stato main/branch rettificato per TrailPath e Anna; contrasto Golden Wonderlog; gap README AppLab e Corpo Umano; Send-to-PC e Cozy.
- Aggiunte autonome Pockara, Tabletop, Easy Debloat e Design-App; score rivisti FocusSense, Cozy e CleanOS.
- Audit dettagliato aggiunto, classifica precedente preservata. Nessuna modifica codice app.


## 2026-10-30 — Audit fusioni già iniziate e classifica aggiornata
- Verificati su GitHub code tree e repository doc per Notification Control, Phone Guard, Android Omni Cleaner, TasteAI e PDF-Unifier, con main SHA indicati in classifica.
- La classifica cresce da 30 a 33 righe: nuovi Android Omni Cleaner, TasteAI e Downloads Butler (solo donor parziale); PDF Pocket Tools riceve evidenza concreta dal donor PDF-Unifier.
- Notification Control e Phone Guard riconosciuti come fusioni implementate (non ancora certificate Store), descrizione completa in elenco sotto classifica.
- Corretto il catalogo suite, preservando distinzione CleanOS vs Omni e MealMate vs TasteAI.
- Punteggi rimangono stime strategiche; snapshot classifica precedente conservato in 90-STORICO.


## 2026-10-30 — Nuove idee in cartella separata
- Introdotta `11-NUOVE-IDEE/` come sede canonica di proposte e inbox, separata da `01-PORTAFOGLIO/` che raccoglie i prodotti catalogati.
- Trasferite le 7 idee già presenti nell'inbox senza perdere nessuna riga; l'indirizzo precedente resta come rimando.
- Aggiornati README, guida e AGENTS; nessun codice app o repo centrale modificato.

## 2026-10-30 — Bootstrap documentale
- Repository inizialmente con solo README, ora indicizzato per portafoglio, suite, WEB, fonti, OSS, sinergie, descrizioni, monetizzazione e storico.
- Importate tutte le 383 righe del Registro Master in 90-STORICO, preservando esattamente l'originale.
- Le otto sezioni originali sono state replicate in cartelle tematiche, con indici tematici consultabili.
- Verificato App-Factory-Core: CURRENT Master 27/Golden Index 23, commit e950705...; AppLab main 46816a... linea 6.3.
- Nessuna applicazione modificata, nessuna fonte dati integrata in codice e nessuna certificazione ottenuta.

Nuove voci changelog: data, file/ID, fonte e tipo evidenza, decisione, impatto, link PR/commit.

## 2026-11-04 — Anna's Diary: audit profondo delle 58 voci da verificare
- Verificato lo stato di Anna main `ab5360b78187a643e2b101be21e6951441406059`, Product Bible, roadmap attiva/issue, App Factory Core main `8052b45b771bf3c5694fc6dd8d037bd83233b37a` e Golden/Donor per capacità.
- [Dossier con verdetto di tutte le 58 CAP](../12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_ANNA_58_DA_VERIFICARE_2026-11-04.md): promosse **solo nella coda di valutazione di prodotto** le CAP-0092, 0093, 0101, 0120, 0145, 0147, tutte con `PROPOSTA / PARTIAL_REUSE` conservato.
- Ripartizione Anna: 8→14 da valutare, 58→52 da verificare, già integrati invariati a 8; 74 associazioni Anna e 160 CAP/385 associazioni totali inalterate. Generatore e test fail-closed per distinguere valutazione e prove di codice; nessun deployment/Golden/stato prodotto implicito.
