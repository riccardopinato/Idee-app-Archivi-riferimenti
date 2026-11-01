# Changelog dell'archivio

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
