# Anna's Diary ↔ App Factory 10x — riconciliazione dei 57 task

**Data:** 13 novembre 2026. **Natura:** audit documentale, non certificazione di telefono, Store o Golden.
**SSOT dei 57:** [PROGRAM_QUEUE.json](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/19-APP-FACTORY-10X/PROGRAM_QUEUE.json) su Idee-app-Archivi-riferimenti main `9a7aedfcffdfbd77db420159968882d166ee423f`.
**Anna main osservato:** `c9da767a14eae5ef0f82ee39e61853f2e24f0057` (PR #312 merged).
**Factory baseline:** App-Factory-Core `c5adc147046beb7024629466d10eeb799c3c2619` / Master v27 / Golden Index v29.

## Correzione di perimetro

Questi sono **57 task del programma trasversale App Factory 10x, non 57 issue o 57 task di Anna's Diary**. Ogni riga qui sotto conserva l'ID e lo stato della coda; la colonna Collegamento Anna e' una classificazione di audit, non un cambiamento di stato nel JSON. Gli stati della coda riflettono gate eterogenei SOURCE/CI/PR; `VERIFIED` non implica Android fisico.

**Conteggio canonico:** 35 VERIFIED, 21 PLANNED, 1 BLOCKED; totale 57.

## Stato verificato del percorso Android Anna

- **Maxi-step 1 — APK originali firmati**: [Anna PR #311](https://github.com/riccardopinato/Agenda-per-Anna/pull/311) MERGED; [audit identita'](https://github.com/riccardopinato/Agenda-per-Anna/blob/c9da767a14eae5ef0f82ee39e61853f2e24f0057/docs/release_evidence/ANDROID_SIGNED_PAIR_127_128_AUDIT.md). Due originali ARM64 +127/+128, Android versionCode effettivi 2127/2128, stesso package e impronta firma; SOLO identita' APK.
- **Maxi-step 2 — Emulator runtime**: [Anna PR #312](https://github.com/riccardopinato/Agenda-per-Anna/pull/312) MERGED in `c9da767a14eae5ef0f82ee39e61853f2e24f0057`; [Actions 43425287812](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43425287812) SUCCESS; [main post-merge 43426938558](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/43426938558) SUCCESS. Verificata **una sola categoria sintetica Inbox** su originali +127→+128, force-stop, downgrade ordinario rifiutato e repair stessa versione; nessuna nota, media, Vault, archivio completo, telefono o Play testati.
- **Maxi-step 3 — physical/data matrix**: **NOT VERIFIED**, non avviato ne' chiuso da questo audit. Checklist di riferimento [DS6 +129 physical acceptance](https://github.com/riccardopinato/Agenda-per-Anna/blob/c9da767a14eae5ef0f82ee39e61853f2e24f0057/docs/DS6_129_PHYSICAL_ACCEPTANCE.md). La +129 e' a livello SOURCE+CI, **non** identificata come APK firmato; testare solo artefatti autentici ed esatti con identita' comparabile.
- **X10-032** resta `PLANNED/HUMAN_GATE` nella coda 10x: il PASS emulator di Anna non e' prova fisica ne' Play. Anche `X10-031` e `X10-033` sono VERIFIED solo per i rispettivi adattatori generali SOURCE+CI.

## Matrice uno-a-uno: 57 ID senza rinumerazione

| ID | Wave | Stato 10x | Task originale | Collegamento effettivo con Anna | Prima prova 10x |
|---|---|---|---|---|---|
| X10-001 | W0 | VERIFIED | Baseline multi-repo fonte verità e gap analysis | Factory baseline multi-repo: include Anna come progetto osservato; non e' un gate Android. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/100) |
| X10-002 | W0 | VERIFIED | Selezione shortlist 2–3 app commerciali | Shortlist prodotti commerciali: Anna non risulta selezionata automaticamente. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/108) |
| X10-003 | W0 | VERIFIED | Inventario Golden/donor e consumatori | Inventario Golden/donor: possibile sorgente di riuso; non modifica l'APK Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/103) |
| X10-004 | W0 | VERIFIED | Audit capability AppLab riusabili | Capability AppLab: prerequisito infrastrutturale, non collaudo dell'app. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/100) |
| X10-005 | W0 | VERIFIED | North Star KPI e ledger tempi/costi/ricavi | Metriche Factory: tempi/costi/ricavi non equivalgono al collaudo Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/104) |
| X10-006 | W0 | VERIFIED | Coda esecuzione con evidence gates | Registro DAG globale: traccia il programma 10x, separato dalla roadmap Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/102) |
| X10-007 | W0 | VERIFIED | Inventario agente Windows locale richiesto | Inventario sorgenti agent Windows: nessuna prova Android. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/14) |
| X10-008 | W1 | BLOCKED | Acquisizione codice Windows verificato | Blocco sorgenti Windows: NON e' bloccante per il test fisico Anna; gate diverso. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/14) |
| X10-009 | W1 | VERIFIED | Selezione adapter AppLab esistente | Adapter AppLab selezionato: specifica, non esecuzione su Anna. | [evidenza](https://github.com/riccardopinato/AppLab/pull/216) |
| X10-010 | W1 | VERIFIED | Contract API job e permission gateway | Gateway permessi agente: nessuna esecuzione su Anna. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/15) |
| X10-011 | W1 | VERIFIED | Coda durevole / retry/idempotency | Retry/idempotency agente: source/CI, non recovery dati Anna. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/16) |
| X10-012 | W1 | VERIFIED | Workspace isolato con source SHA | Workspace isolamento agente: non backup/restore app Anna. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/17) |
| X10-013 | W1 | VERIFIED | Orchestrazione bounded con adapter | Orchestrazione adapter source/CI: no worker Windows o QA Anna. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/20) |
| X10-014 | W1 | VERIFIED | PR agent con CI exact-head | PR agent exact-head: meccanismo generale, non PR #312 stessa feature. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/21) |
| X10-015 | W1 | PLANNED | Test end-to-end agente locale | Test agente locale attende X10-008: indipendente da Android fisico Anna. | assenza di receipt finale |
| X10-016 | W1 | VERIFIED | Adapter agenti ricerca/QA | Adapter ricerca/QA agent: non collaudo Anna. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/22) |
| X10-017 | W2 | VERIFIED | Contratto package Golden e versioning | Contratti package Golden: riuso potenziale, non adozione automatica. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/106) |
| X10-018 | W2 | VERIFIED | Harness compatibility per Golden | Compatibility harness: test source-bound, non aggiornamento APK reale. | [evidenza](https://github.com/riccardopinato/AppLab/pull/223) |
| X10-019 | W2 | VERIFIED | Flutter starter kit minimale | Flutter starter: nuovo prodotto, non rifare la base Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/112) |
| X10-020 | W2 | VERIFIED | Kit identity/login opt-in | Kit identity/login: adozione consumer separata; non test account-switch fisico. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/121) |
| X10-021 | W2 | VERIFIED | Kit profilo/impostazioni | Kit profilo/impostazioni: Anna adotta profile-kit 0.1.1 nella PR #310; soltanto source+CI. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/119) |
| X10-022 | W2 | VERIFIED | Kit backup/recovery | Kit backup/recovery: SOURCE+DART_CI, non prova archivio/media su telefono Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/124) |
| X10-023 | W2 | PLANNED | Kit notifiche/health | Kit notifiche: PLANNED; test native API29 non dimostra delivery/OEM Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/43336767350) |
| X10-024 | W2 | PLANNED | Kit monetizzazione modulare | Kit monetizzazione: PLANNED e provider/owner gate; nessuna prova Play Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/actions/runs/43338039970) |
| X10-025 | W2 | VERIFIED | Kit composizione e dependency chooser | Kit composizione/dependency chooser: riuso proposto, non runtime Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/131) |
| X10-026 | W2 | VERIFIED | Due consumer Flutter certificati per kit | Anna e TasteAI sono consumer source+CI di factory_profile_kit 0.1.1; Anna PR #310, non dati fisici. | [evidenza](https://github.com/riccardopinato/AppLab/actions/runs/43331970619) |
| X10-027 | W3 | VERIFIED | Matrice QA esistente e gap release | Matrice livelli di QA AppLab: applicabile al Maxi-step 3; documentale. | [evidenza](https://github.com/riccardopinato/AppLab/pull/217) |
| X10-028 | W3 | VERIFIED | QA test router condiviso | Test router AppLab: supporto teorico alla campagna QA Anna; non run fisico. | [evidenza](https://github.com/riccardopinato/AppLab/pull/224) |
| X10-029 | W3 | VERIFIED | Visual regression automation | Visual regression AppLab: adapter source+CI; baseline visiva Anna da collaudare. | [evidenza](https://github.com/riccardopinato/AppLab/pull/226) |
| X10-030 | W3 | VERIFIED | Performance e accessibilità gate | Performance/accessibilita' AppLab: adapter source+CI; manca benchmark su telefono Anna. | [evidenza](https://github.com/riccardopinato/AppLab/pull/227) |
| X10-031 | W3 | VERIFIED | Signed release provenance pipeline | Provenance pipeline AppLab: compatibile con Maxi-step 1, ma la prova specifica Anna e' PR #311. | [evidenza](https://github.com/riccardopinato/AppLab/pull/225) |
| X10-032 | W3 | PLANNED | Physical QA e Play internal testing | Gate fisico e Play: corrispondenza PRINCIPALE con Maxi-step 3; rimane PLANNED/HUMAN_GATE. | [evidenza](https://github.com/riccardopinato/AppLab/actions/runs/43343304828) |
| X10-033 | W3 | VERIFIED | Gate CI->QA->release decision | Release decision AppLab: infrastruttura source+CI, non promozione Anna a Store-ready. | [evidenza](https://github.com/riccardopinato/AppLab/pull/228) |
| X10-034 | W4 | VERIFIED | Validazione ricerca domanda/competitor | Analisi domanda mercato: nessun test fisico Anna o vendita dimostrata. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/114) |
| X10-035 | W4 | PLANNED | Decisione 2–3 prodotti e budget | Budget e selezione 2-3 prodotti: approvazione umana globale separata dal Maxi-step 3. | assenza di receipt finale |
| X10-036 | W4 | PLANNED | Sistema privacy-first product analytics | Analytics product privacy-first: futuro opt-in per prodotto, non abilitato in Anna da questo task. | assenza di receipt finale |
| X10-037 | W4 | PLANNED | Pricing e monetization experiment plan | Esperimenti pricing e monetizzazione: nessun billing Anna autorizzato. | assenza di receipt finale |
| X10-038 | W4 | PLANNED | Pilot acquisition e release approval | Acquisizione e release pilota: non autorizza Play/Store Anna. | assenza di receipt finale |
| X10-039 | W4 | PLANNED | Decisioni basate su coorti reali | Decisioni coorti: richiedono dati utenti reali, assenti per questo gate. | assenza di receipt finale |
| X10-040 | W5 | VERIFIED | Architettura knowledge/reuse centrale | Architettura conoscenza/riuso centrale: nessun writer sul diario Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/110) |
| X10-041 | W5 | VERIFIED | Diff-aware monitor repository | Monitor differenze repo: Anna potra' essere monitorata, non certificata. | [evidenza](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/19) |
| X10-042 | W5 | VERIFIED | Dedup capability/donor hypotheses | Dedup capability/donor: suggerimenti di riuso, non applicazione al progetto. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/117) |
| X10-043 | W5 | VERIFIED | Semantic review workflow supervisionato | Revisione semantica supervisionata: non prova Android reale. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/122) |
| X10-044 | W5 | VERIFIED | Riuso recommendation cockpit | Cockpit raccomandazioni riuso: non modifica/valida dati utenti Anna. | [evidenza](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/129) |
| X10-045 | W5 | VERIFIED | Feedback loop failure→donor | Feedback failure verso donor: errori Anna possono essere proposti, senza autoregolazione automatica. | [evidenza](https://github.com/riccardopinato/AppLab/pull/229) |
| X10-046 | W6 | PLANNED | Pilota sviluppo feature A | Pilota agente feature A: repo/feature non selezionati, non considerare Anna implicita. | assenza di receipt finale |
| X10-047 | W6 | PLANNED | Pilota feature B su repo diverso | Pilota agente feature B: altro consumer, non collaudo Anna. | assenza di receipt finale |
| X10-048 | W6 | PLANNED | Compatibilità kit nel secondo consumer | Secondo consumer kit: ulteriore requisito Factory, distinto dalla PR #310. | assenza di receipt finale |
| X10-049 | W6 | PLANNED | Campaign regressioni cross-app | Regressioni cross-app: programma futuro; non chiude singoli casi di Anna. | assenza di receipt finale |
| X10-050 | W6 | PLANNED | Knowledge feedback su due consumer | Feedback conoscenza due consumer: non QA fisico. | assenza di receipt finale |
| X10-051 | W7 | PLANNED | Portfolio queue continua con recovery | Queue continua/recovery orchestrazione: progresso 10x, non backup Anna. | assenza di receipt finale |
| X10-052 | W7 | PLANNED | Cost/performance benchmark rispetto al baseline | Benchmark tempi e costi 10x: non confondere con tempi startup/scroll Anna. | assenza di receipt finale |
| X10-053 | W7 | PLANNED | Scoped donor/process admission | Golden admission scoped: no promozione per PR #311/#312 da sole. | assenza di receipt finale |
| X10-054 | W7 | PLANNED | Release train per 2–3 app | Release train 2-3 app: non conferma pubblicazione Play di Anna. | assenza di receipt finale |
| X10-055 | W7 | PLANNED | Conferma scaling prodotti | Decisione scaling commerciale: basata su dati reali, non risolta dall'emulatore. | assenza di receipt finale |
| X10-056 | W7 | PLANNED | Reprioritizzazione cross-app basata su dati | Reprioritizzazione portafoglio: non sostituisce Product Bible Anna. | assenza di receipt finale |
| X10-057 | W7 | PLANNED | Nuova ondata mantenendo storico | Nuova ondata W8+: attivita' futura di governo, non Maxi-step 3. | assenza di receipt finale |

## Gap effettivi di Anna prima di affermare collaudo fisico

1. **Backup indipendente verificato e inventario ante update**: identita' installato, account, journal/ricordi, Inbox categorie e note, archive/Trash, persone, agenda, foto/audio/sketch, reminder, preferenze; includere dati reali solo con consenso e protezione, senza trasmetterli alla CI.
2. **Artifact identity sul telefono**: medesimo package e certificate SHA256, Android versionCode crescente, SHA256 APK fisico, modello/Android, assenza uninstall/clear. `+127/+128` originali sono gli unici firmati coperti dai Maxi-step 1–2; non chiamare `+129` release firmata.
3. **Matrice persist-after-upgrade e restart**: verifica elemento per elemento e backup/restore con rollback sicuro, niente downgrade forzato o distruzione dati personali.
4. **Permessi e sicurezza**: Vault/PIN/biometria, ricerca privata, account switching, notifiche, sincronizzazione offline e isolamenti corretti.
5. **Shared-space**: su due telefoni/account distinti, scenari codice/QR/membership, privacy e recovery; separare da prove solo locali.
6. **UX/performance/accessibilita'**: dieci journey DS6, 5 lingue IT/EN/ES/FR/PT, schermi piccoli/testo grande, foto reali, startup/scroll, error logs, no jank osservato.
7. **Play**: internal testing e billing richiedono autorizzazione, account/track e receipt separati; non dedurli da sideload o emulatore.

**Regola di chiusura:** per ogni scenario registrare `PASS / FAIL / BLOCKED / NOT VERIFIED` con artifact/source SHA, dispositivo, test osservato e link alla prova, senza dati sensibili. La matrice supporta un futuro task X10-032, ma **non** muta automaticamente PROGRAM_QUEUE.json o Product Bible. Nessun nuovo apk, release, patch all'app o modifica del JSON canonico con questa PR.

## Disallineamenti corretti in questa riconciliazione

- Il numero 57 non appartiene alla roadmap Android di Anna; il programma globale 10x ne e' la source of truth.
- `VERIFIED` Factory e' relativo ai gate di ogni task, non prova di dispositivo o risultato commerciale.
- L'assenza di 52 issue aperte in Anna non prova che 52/57 siano stati implementati: non sono lo stesso namespace.
- La PR #312 non completa X10-032 ne' una matrice di archivio completo; la modifica in Main riguarda un collaudo emulatore circoscritto.
- Il blocco X10-008 (sorgenti agente Windows) e' indipendente dal Maxi-step 3 Android.
