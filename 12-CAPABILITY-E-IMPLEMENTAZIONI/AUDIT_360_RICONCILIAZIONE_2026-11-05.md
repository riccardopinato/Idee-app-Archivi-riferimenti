# Audit 360° App Factory — riconciliazione repository, ChatGPT e capability
Data: 2026-11-05 · Tipo: **audit documentale e source-sampling**, non certificazione runtime.
Sorgente primaria: GitHub. Il contesto ChatGPT e gli allegati storici sono segnali di ricerca e decisioni da verificare, non prove di codice aggiornato.

## 0. Gerarchia e baseline fissata
- Factory: `riccardopinato/App-Factory-Core@42ad47a9ebacc55ae901ea55a01a6855e320377d`.
- `CURRENT.yaml`: Master **v27** (`v27/candidate/MASTER_CORE_v27_CANDIDATE.txt`), Golden Index **v28** (`golden/GOLDEN_INDEX_CURRENT.txt`), Registry **v2** (`golden/GOLDEN_REGISTRY.yaml`).
- Archive: `riccardopinato/Idee-app-Archivi-riferimenti@15a81a233df6778c39cd339ba0dcb03c19508085`, prima di questa PR.
- Snapshot capability 2026-11-04: **160 CAP, 385 associazioni, 48 app/idee**. Non significa 48 repository attivi o 385 implementazioni.
- Policy: Product Bible e roadmap app definiscono scope, codice/test dimostrano comportamento, certificazioni device/provider/Play sono ulteriori gate. Nessun merge/feature/Golden promotion implicita da questo audit.

## 1. Copertura e limiti effettivi
- Enumerati **31/31 repository dell'affiliazione owner** collegata e letta la struttura root di ciascuno.
- Letti, per campionamento mirato, README, ROADMAP e documenti di release/feature dei progetti maggiori; ricontrollati esempi di sorgente di Notes PDF, ricerca fuzzy, Word/Editorial, EXIF e altri.
- Acquisiti SHA live di tutti i 31 branch default il 5 novembre; non sono stati eseguiti qui Flutter/Gradle, CI, APK, test hardware o Play/AdMob.
- Le **17 differenze 48–31** sono nomi di app/idee nel catalogo *non rappresentati uno-a-uno nel set owner visibile*. Non vanno etichettati «mai sviluppati»: possono essere idee, nomi storici, progetti accorpati o codice non accessibile tramite questa installazione.
- `APP_FACTORY_CORE` contiene anche Golden con stati DRAFT, COPY-READY, CERTIFIED DONOR/PROCESS: `present in registry` != libreria installata nel consumer.
- Questo audit **non sostituisce** l'audit codice-file-per-file, la verifica transitive licenses, l'esecuzione test o la policy Play attuale.

## 2. Snapshot dei repository osservati
Tutti gli SHA sono testate reali lette da GitHub; per `btrader` il default è `master`, per gli altri `main`.

| Repository | SHA osservato | Classificazione operativa |
|---|---|---|
| 1000-AI-collection-tools | `3fec0fc008894f364cdef0f18419b5b575c24d55` | archivio esterno/ricerca, non app consumer |
| 180FlipCharge | `1d4a9f3492afab2c4486738c466ce2acc38719c0` | utility Kotlin, firma/QA separati |
| Agenda-per-Anna | `0587993047dcc3fa06732477e5c145ee520cc04c` | Anna's Diary, prodotto maturo; release e sicurezza non deducibili dal solo merge |
| Analisi-delle-mie-stelle-github | `493db7d438f530957ddae03a4fe1777548c5f4f6` | ricerca/donor |
| Android-Omni-Cleaner | `a753baa8ad0b647be747050ac7e2f6d1fde85465` | prodotto Kotlin; Step 9.7 physical primary PASS, Step 10 provider/Store aperto |
| App-corpo-umano | `0a0cdbd2564e2e6db20f6aab9f6c07eba6722556` | app educativa Flutter, README 0.18.0+18 |
| App-Factory-Core | `42ad47a9ebacc55ae901ea55a01a6855e320377d` | baseline centrale |
| app-fotografia | `e7538d7dfc484f81f37a8e4363cd56a5b742e804` | app fotografia/FrameLab, contenuti/archivio editoriali |
| AppLab | `58cb25070b80673f1e9d12593bceb496b83bc6f0` | QA agentico, release evidence, non app consumer |
| Battery_Guard | `d8cf237ab2df2daf427b87ca057871e3143bccc7` | Flutter 1.8.1+27, device/Play/AdMob gate aperti |
| btrader (master) | `59721c9ca1601f29bfa382e0a3131b9dfc02cc2d` | progetto Rust distinto; non assumere consumer App Factory |
| CamperBoss | `ae30d08f23aa7e8c835927bc98127f25662d2f6a` | Flutter, Step 16 release core ancora BLOCKED |
| Cozy-game-nome-da-scegliere- | `433ffe98cd2f658a2e15b2b6029336b5487e881d` | repository root solo README; non qualificare runtime completo |
| Design-App | `546a1c187824a416b5caf3b841c8f143b373aae1` | design donor, token, pack; diversi scope di maturità |
| desktop-tutorial | `ce1383559996b0e0d447a4208b78431da23ff49b` | tool/web/prototipo, fuori quota app native |
| FocuSense | `bdc8becfff1b1a5f629456deb34170f0d905d8b7` | Kotlin 1.0 RC1; device/signing/prod aperti |
| FrameLab-Google-AI-Studio | `239995759e2b56f5315a061a169404c591d77f39` | possibile mirror FrameLab: README, ROADMAP, pubspec e lib/main.dart con blob SHA identici ad app-fotografia |
| Idee-app-Archivi-riferimenti | `15a81a233df6778c39cd339ba0dcb03c19508085` | ricerca/capability authoritative portfolio, non codice app |
| In-Cucina-con-gli-Anime | `478f6db6d6cdcfe9adcbddacfe834cb7fbc345e7` | Cooking Anime, code/quality lanes e food-safety/content gate |
| Neon-arcade-runner | `ecb79f6fc2ed24513cc04dab5a44ca4606b5ab59` | gioco Capacitor/Web; device gameplay repair monitorare |
| Notes-Ecosistema | `3cd9062601e58ee4ad8bfb7bb6eb2c96a24b890f` | Flutter notes; funzioni molte, physical/billing/PDF exposure separati |
| Notification-Control | `664cf8c7eaaa8843711ddc99b62b547a1997fcb9` | Kotlin suite; Play/OEM QA aperti |
| PDF-Unifier | `3aacb3e2ac4822db4601fe5c217c016cecc6cbf4` | Kotlin PDF donor; non equivale a PDF Pocket Tools già distribuita |
| Phone-Guard | `ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c` | suite Kotlin Tabletop/Pocket/Bag, OEM physical pending |
| Pocket-Guard | `dcec7d82e374e955f1e06c2c8d0a9143c418b6d7` | donor Kotlin per Phone Guard; entità prodotto autonoma |
| Send-to-pc | `bd271cb96b565e4b937f0e7cfe14058759f830b3` | Kotlin LAN; RC 1.27.1 startup hotfix da provare fisicamente |
| Tabletop-Motion-Alarm | `9e67bcbd84e8add7d183349644d3f6f6bbe9ffe0` | donor Kotlin, firma/hardware gate separati |
| TasteAI | `fc2f80e43f91b441863f8e3a77ae7196251979cf` | Flutter ricette, core anti-spreco; QA prod esterno |
| TrailPath | `3f44ab37c0881e4315033797c451cec723e23cd2` | Flutter routing/outdoor; device routing/OEM/Store da certificare |
| Wonderlog | `b4840e845336fb6df6f823986b8cf0a731e66a35` | Flutter primario, Kotlin legacy donor; ponte e cutover evidence da contestualizzare |
| World-Days | `bb662cb21506b6157658f43070c2059c960637b5` | Flutter editorial/ad/Play; storie complete e release ancora aperte |

Nota duplicati: i **quattro blob identici** fra `app-fotografia` e `FrameLab-Google-AI-Studio` costituiscono prova di duplicazione di questi file, NON prova di identità integrale dell'intero repository. Definire owner canonico e politica mirror prima di fare sviluppi in entrambe.

## 3. Stato numerico del registro, non del prodotto
Fonte: `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json` aggiornato 2026-11-04.

| Stato registrato | Associazioni | Interpretazione |
|---|---:|---|
| PROPOSTA | 258 | opportunità catalogata; non implicita approvazione |
| ROADMAP_STORICA | 15 | una roadmap storica la cita, corrente da ricontrollare |
| SOURCE_REPORTED | 98 | codice/documento dichiarato, non certificazione indipendente |
| DONOR_REPORTED | 2 | donor dichiarato, riuso da verificare |
| SOURCE_CONFIRMED | 2 | codice identificato con prova scoped |
| CI_VERIFIED | 10 | CI specifica verificata nella precedente registrazione |
| DEVICE_VERIFIED | 0 | nessuna attestazione classificata nel *registro*; non assenza di test fisici nei repo |
| RELEASE | 0 | nessuna prova di release classificata nel *registro*; non prova di mancata distribuzione |
| **Totale** | **385** | **160 capability, 48 consumer/idee** |

**Distribuzione del catalogo:** Notes 88 associazioni (0 SOURCE_CONFIRMED/CI nel registro), Anna 74 (12), Wonderlog 35 (0), CamperBoss 19, app-fotografia 16, PDF-Unifier 15, TrailPath 14, FocuSense 13, Cooking Anime 12, World Days 10. Questo mostra un **gap di registrazione evidence**, non che Notes sia priva di funzioni.

## 4. Riscontri già implementati / da non ricostruire
- **Anna**: agenda/slot liberi `CAP-0001`, natural event parser `CAP-0002`, preparazione appuntamenti `CAP-0003`, export calendario `CAP-0005` parziale in termini di prodotto, weekly review `CAP-0111`, health native `CAP-0077`, capture memory `CAP-0113`; prove puntuali nel registro. La roadmap **5 novembre** documenta anche `CAP-0160` tag TF-IDF privati, con PR #245 merged: non trattarlo come greenfield. La release +125 e la PR mockup #251 hanno identità diverse.
- **Notes**: Smart Inbox, Next Action, Knowledge Graph, canvas/digital ink, P2.5 import provenance, backup, Study, local retrieval e Needle optional sono già domini in codice; non sostituirli con nuovi datastore. `flutter_app/lib/src/domain/note_local_signals.dart` implementa fuzzy fallback locale `CAP-0152`: stato registro SOURCE_REPORTED è prudentemente conservativo ma questa fonte va allegata. `flutter_app/android_overrides/PdfToolkitBridge.kt` implementa merge/extract/rotate/reorder PDF (`CAP-0037` **parzialmente implementata**, non semplicemente PROPOSTA); `NOTES_ENABLE_PDF_TOOLBOX=false` nelle build ordinarie. Password lock/redaction/iOS/Web non implementati e QA-PDF-01..12 NOT RUN; issue #70.
- **World Days**: catalogo offline multilingua e editorial pipeline, localization e release identity esistono. Story completeness **non** è conclusa: issue aperta per 296 storie source-reviewed e anni di istituzione nelle sei lingue; release Play/Billing/QA resta distinta.
- **Android Omni Cleaner**: inventario/storage, EXIF JPEG, index persistente e hashing bounded sono donor candidati; non introdurre una seconda pulizia o una nuova gestione backup solo per `CAP-0039`. Test primario fisico documentato, non piena Store readiness.
- **Phone Guard**: convergenza Tabletop/Pocket/Bag e attivazioni rapide già sviluppate; `CAP-0158` va verificata come integrazione di policy/soglie, non un altro servizio di allarme.
- **Send-to-pc**: HTTPS LAN, identità Keystore, transfer recovery e signing esistono; il blocco più importante è startup/physical RC, non aggiungere EXIF prima della stabilizzazione.
- **Wonderlog**: Flutter è il consumer attuale; Kotlin legacy è donor. Producer Life Bridge documentato; la roadmap dice round-trip Xiaomi fisico 2026-10-05, mentre il Golden Bridge centrale resta `cross-app physical NOT VERIFIED`. **Divergenza di perimetro/evidence** da riconciliare con SHA artifact, verso del trasferimento e matrice 7 casi, senza annullare l'evidence storica.
- **FrameLab**: Drift/archivio, import editoriale e localizzazioni sono esistenti. `CAP-0039` EXIF-safe copy e `CAP-0053` Sun/Moon non provate come feature in release; non confondere con semplici metadati o palette di design.
- **Cooking Anime**: authoring, localizzazione ed editorial pipeline sono reali. Food-safety e false friend FR/DE/PT hanno issue aperte; sicurezza editoriale prima di nuovi sistemi AI/anti-spreco.
- **AppLab/Factory Core/Design-App**: QA/evidence, regole Golden e asset UI sono tre authority diverse, non tre librerie da copiare per intero.

## 5. Disallineamenti documentali immediati
1. README root archive: **«147 capability»** e **«150 kit»** sono obsoleti rispetto a JSON **160/385** e `13-KIT-INTEGRAZIONE/CAP-0001..0160`. Aggiornare solo l'indice, preservare i file storici.
2. README root presenta snapshot **Golden Index v23 del 30 ottobre**: deve restare esplicitamente marcato come **storico** e accompagnato dal nuovo collegamento all'audit v28; non alterare lo snapshot.
3. `GIA_INTEGRATI.md` e `DA_VALUTARE.md` sono file **generati**: non modificarli a mano. Prima reconciliamo evidence/stati nel JSON, poi `python3 scripts/build_catalog.py` e `--check` su PR dedicata.
4. `CAP-0037/Notes`: nuova proposta originale **superata dal source dark-launch**. Non promuovere l'intera CAP a CI_VERIFIED/DEVICE: contiene anche il lock PDF non presente.
5. `CAP-0160/Anna`: proposta nell'archivio 04/11, implementazione sorgente descritta il 05/11; aggiornamento di app_state e prove solo dopo audit scoped exact-head.
6. `CAP-0152/Notes`: fuzzy fallback presente nel source corrente; registrare path, test, ACL/save-time gate senza chiamarla semantic neural search certificata.
7. `app-fotografia` e `FrameLab-Google-AI-Studio`: quattro file importanti condividono blob SHA; evitare roadmap duplicate divergenti.
8. README principale Anna ancora parla di v1.05.x/+111 mentre `docs/ROADMAP.md` del 05/11 segue RC +124/+125 e PR #251: distinguere storico README vs stato operativo. NON riscrivere release identity senza source/artifact verification.
9. Alcune roadmap dichiarano `SOURCE COMPLETE` o `DONE` e separatamente `PHYSICAL QA PENDING`. Conservare due colonne: implementazione vs certificazione/distribuzione.

## 6. Shortlist non implementata / residua (priorità ed ease stimate)
I punteggi 0–100 e la facilità sono **euristiche presenti nel registro** e non probabilità di riuscita; la priorità release blocco/QA può superare quella feature.

| Priorità pratica | CAP / app | Score / facilità archivio | Reality check / prossima azione |
|---|---|---|---|
| P0 qualità | Send-to-pc v1.27.1 | fuori CAP | collaudo in-place/startup reale prima di altro prodotto |
| P0 distribuzione | World Days release | fuori CAP | Play Billing sandbox, physical QA, 296 storie/anni fonte: blocchi separati |
| P0 affidabilità | Anna/Notes/Phone/Battery | vari | signing, restore, notifica, permessi, sicurezza e test device prima di store claim |
| P1 evidence | CAP-0037 Notes | 98 / 90 | **parziale dark launch**, 12 test QA-PDF NOT RUN; non rifare engine |
| P1 nuova integrazione | CAP-0039 FrameLab | 98 / 95 | riuso mirato EXIF-safe copy donor Omni Cleaner; consenso e copie, licenza/adattamento |
| P1 nuova integrazione | CAP-0039 Send-to-pc | 98 / 90 | solo dopo RC fisica; copia separata senza mutare originali |
| P1 nuova integrazione | CAP-0152 Anna | 96 / 89 | riuso bounded fuzzy del donor Notes con account/privacy e test refusi |
| P1 nuova integrazione | CAP-0152 Wonderlog | 96 / 88 | stessa policy, senza importare index/storage Notes |
| P1 proposta prodotto | CAP-0044 Cooking Anime | 95 / 97 | differenziare nettamente dal core anti-spreco TasteAI, non clonare |
| P1 QA orizzontale | CAP-0017 Anna/Notes/Wonderlog/CamperBoss | 94 / 80 (ultimi due) | matrice entity lifecycle, cancellazioni a cascata, media orfani, undo/sync |
| P1 basso costo | CAP-0053 FrameLab/CamperBoss/TrailPath | 93 / 95 | Sun/Moon locale, timezone/DST/location explicit, offline tests |
| P1 complessità OEM | CAP-0158 FocuSense | 96 / 89 | calibrazione sensori/isteresi; test hardware prima del riuso |
| P1 complessità OEM | CAP-0158 Phone Guard | 96 / 86 | integrare policy esistente, non nuova protezione |
| P1 evoluzione Notes | CAP-0102 | 92 / 85 | ripianificazione assistita solo previa preview e consenso, senza mutazione automatica |
| P2 portabilità | CAP-0042 FrameLab/World Days/Cooking Anime | 94 / 82–85 | contratto donor editoriale con fonti, rights e package integrity; engine già presente, non rifare |

**Non universalizzare** AI, sensori, AdMob, login, cloud, billing, PDF, push e permessi: applicabilità condizionata al prodotto. Reuse-first per core puri/contratti con consumer adapters diversi.

## 7. Roadmap trasversale proposta, 5 maxi-step

### M1 — Verità di release e blocchi realmente urgenti
Aggiornare per i consumer critici un `Release Reality ledger`: HEAD SHA, package/versionCode, artifact SHA/signing, CI, Android device, Web/iOS, provider/Play, verdict, owner del gate. Primo gruppo Anna, World Days, Send-to-pc, Notes, Battery Guard, Phone Guard, TrailPath e CamperBoss. Niente falsi `CERTIFIED`.

### M2 — Reconciliation evidence di 385 associazioni
Non richiedere 385 nuovi test subito. Selezionare prima 100 `SOURCE_REPORTED`/`DONOR_REPORTED`, verificare prove E1–E3 ad alto valore e cambiare solo le associazioni supportate: `CAP-0037/Notes`, `CAP-0160/Anna`, `CAP-0152/Notes`, `CAP-0042`, `CAP-0039`, `CAP-0017`. Aggiornare JSON canonico e rigenerare tutte le viste derivate; differenziare `PARTIAL_SOURCE` da `PROPOSED_ONLY` nei commenti di evidence, senza inventare nuovo enum non supportato dallo script.

### M3 — Safety-first reuse, senza duplicazioni
Donor scoped esistenti: backup/restore, entity lifecycle/trash, media CAS, permission health, sensor admission, signing, evidence. Consumatori selezionati in base al bisogno reale; regression suite per entità, network-offline, OEM, profile/account switching, no file orfani, backup/restore. Golden DRAFT non sono automaticamente COPY-READY.

### M4 — Quick wins per prodotto e donor
Primo lotto: EXIF-safe sharing/FrameLab, fuzzy offline Anna+Wonderlog, Sun/Moon FrameLab+CamperBoss+TrailPath, TF-IDF tag dove manca e serve; mantenere workflow editoriale riusabile per World Days/FrameLab/Cooking Anime. Nuovo motore o package condiviso solo quando i consumer convergono sullo stesso contratto stabile.

### M5 — Allineamento continuativo e riduzione duplicati
Un report machine-readable per app `repo, canonical app id, default HEAD, Product Bible, roadmap, release gates, CAP state, donor source SHA, last verified date`. Check CI `build_catalog.py --check` ed evidence link test; singolo repo canonico/mirror policy FrameLab; nessuna riscrittura indiscriminata di AGENTS/ROADMAP/Golden.

## 8. Decisioni e sicurezza di esecuzione
- Il presente file propone correzioni e priorità; **non** dichiara cambi di `REGISTRO_CAPABILITY.json`, merge, implementazioni, Play/test device o promozioni Golden.
- `GIA_INTEGRATI` non può crescere da 12 a 100 perché la roadmap «dice fatto». Ogni promozione richiede riferimento scoped e livello di prova.
- Branch/PR documentale dedicato; `main` e tutti i repo app restano invariati finché il relativo gate/PR non è verificato.
- `PROPOSTA` non implica scope approvato: Product Bible e roadmap di ciascun prodotto controllano l'adozione.
- Per i mirror/donor preservare licenze, attribution, identità/ownership, tests, privacy e asset rights.
- Aggiornamento futuro: nuova baseline solo a inizio nuova sessione o dopo aggiornamento centrale, non durante questa sequenza.

## 9. Link autorevoli
- [Factory CURRENT](https://github.com/riccardopinato/App-Factory-Core/blob/main/CURRENT.yaml)
- [Golden Registry](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/GOLDEN_REGISTRY.yaml)
- [Registro CAP JSON](REGISTRO_CAPABILITY.json)
- [Stato implementazioni](STATO_IMPLEMENTAZIONI.md)
- [Già integrati](../GIA_INTEGRATI.md) · [Da valutare](../DA_VALUTARE.md)
- [Audit ML10 04/11](AUDIT_COMPLETO_ML10_2026-11-04.md)
- [Anna roadmap reale](https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md)
- [Notes roadmap reale](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/ROADMAP.md)
- [Notes PDF source/gates](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/flutter_app/PDF_TOOLBOX_SOURCE_AND_GATES.md) · [Notes PDF device QA](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/flutter_app/PDF_TOOLBOX_DEVICE_QA.md)
- [World Days roadmap](https://github.com/riccardopinato/World-Days/blob/main/ROADMAP.md)
- [Send-to-pc roadmap](https://github.com/riccardopinato/Send-to-pc/blob/main/ROADMAP.md)
