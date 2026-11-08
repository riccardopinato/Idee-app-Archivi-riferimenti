# HTML.it Flutter — esecuzione dei 5 maxi-step (09/11/2026)

**Tipo:** audit sorgenti + catalogazione evidence-gated, senza modifiche ai consumer.  
**Fonte:** https://www.html.it/guide/flutter-creare-app-mobile-multipiattaforma/ (37 lezioni, pubblicazione 2019–2020, audit documentale di origine 09/11/2026).  
**Repository esempi:** https://github.com/antedesk/flutter_tutorial_htmlit/tree/2bf59b6d712eef4e85648b08c22a3203cd1799ce  
**Diritti:** GitHub metadata `license:null`; LICENSE non presente nel root esaminato. **COPY CODE = BLOCKED** fino a clearance per il singolo file; consentita analisi di pattern e reimplementazione indipendente.  
**Factory:** riccardopinato/App-Factory-Core@`a6d7ff36db7f70b03ccfdf02fa265049d31ae2f1`, CURRENT Master v27 / Golden Index v29 / Registry v2.  
**Registro:** archivio main precedente `b3ca5c6911ab12a292025d5c82abb4b5571c6b3a`, **199 CAP / 441 associazioni / 48 app-idee**.  
**Esito:** 12 estrazioni **HTMLIT-01..12**, tutte riferimenti E0 e non nuove CAP numeriche. Nessuna nuova associazione app, stato tecnico, priorità o decisione Product Bible. Non si dichiarano test/build runtime.  
**Raccolta codice:** GitHub fetch_file di percorsi puntuali + code search indicizzato con limite di risultati; **non un grep completo di tutti i file**. Gli 0 risultati non provano assenza assoluta.  
**Legenda:** V = evidenza di codice puntuale; I = indicazione/inferenza da struttura o ricerca; NV = non verificato; P1/P2/P3 = urgenza di *verifica*, non severità bug né approvazione feature.

## 1. Registro delle 12 estrazioni e deduplicazione

| ID fonte | Responsabilità studiata | CAP esistenti più vicini | Esito dedup | Prossimo gate |
|---|---|---|---|---|
| HTMLIT-01 | Liste lazy e build cost | CAP-0025, CAP-0069 | Pattern trasversale, nessuna CAP prodotto autonoma | benchmark su lista lunga |
| HTMLIT-02 | Tema Flutter moderno | CAP-0023 | Copertura diretta; Golden Theme M3 COPY-READY prioritario | coerenza tema consumer |
| HTMLIT-03 | Navigazione tipizzata/deep link | CAP-0025, CAP-0027 | Sovrapposizione parziale, non duplicare router | test Web back/deep link |
| HTMLIT-04 | Preferenze locali e async safety | CAP-0018, CAP-0023 | Requisito di qualità trasversale, non nuovo store | audit await/migrazione |
| HTMLIT-05 | File I/O adapter Android/Web | CAP-0018, CAP-0019, CAP-0075 | Copertura tramite data safety; no `dart:io` indiscriminato | parity test native/web |
| HTMLIT-06 | SQLite/repository/migration QA | CAP-0018, CAP-0075 | Parte del data lifecycle, non database parallelo | restart/migration/rollback |
| HTMLIT-07 | Location permission health | CAP-0077 | Copertura diretta; Golden native health DRAFT | service+permission+accuracy+fallback |
| HTMLIT-08 | Scelta provider mappe | CAP-0047, CAP-0048, CAP-0049 | Già sotto map/offline/routing; Google Maps non obbligatorio | privacy/costi/termini |
| HTMLIT-09 | Image loading/failure/memory | CAP-0019, CAP-0120 | Media Asset Store + accessibility | placeholder/error/cache benchmark |
| HTMLIT-10 | SnackBar/dialog/semantica delete | CAP-0017, CAP-0024 | Lifecycle + feedback condiviso | conferma distruttiva + undo |
| HTMLIT-11 | Widget constraints/adaptive shell | CAP-0025, CAP-0023 | Copertura diretta; shell Golden DRAFT | text scale/viewport/rail |
| HTMLIT-12 | Migrazione API e lint gate | CAP-0068, CAP-0070 | Estensione di QA/AppLab, non nuovo runtime | scan read-only + triage |

Non assegnare ID `CAP-0200+` alle 12 estrazioni didattiche: un ID CAP richiede responsabilità distinta e ammissione canonica. I match sopra **non certificano** che ogni comportamento sia implementato nelle app indicate. Priorità Golden interno, donor interno, documentazione ufficiale, poi reference esterno.

## 2. Anti-pattern Flutter — audit campionato

**Target HEAD esatti 09/11/2026:**

| Repository | HEAD |
|---|---|
| Agenda-per-Anna | `869d48ca651bd85e9ee4952264c87a9e33904606` |
| Notes-Ecosistema | `6e8510c721308d0acceeda12d0b4090268118cdd` |
| World-Days | `bb662cb21506b6157658f43070c2059c960637b5` |
| TrailPath | `3f44ab37c0881e4315033797c451cec723e23cd2` |
| app-fotografia (FrameLab) | `e7538d7dfc484f81f37a8e4363cd56a5b742e804` |
| CamperBoss | `ae30d08f23aa7e8c835927bc98127f25662d2f6a` |
| Wonderlog | `b4840e845336fb6df6f823986b8cf0a731e66a35` |
| Battery_Guard | `d8cf237ab2df2daf427b87ca057871e3143bccc7` |

**Ricerca indicizzata campionata (Anna, Notes, World Days):** `RaisedButton`, `FlatButton`, `accentColor`, `Scaffold.of(context).showSnackBar`, `Navigator.pushNamed` hanno restituito 0 hit nel campione interrogato. **Stato: NON TROVATO NEL CAMPIONE, non assenza garantita.**

**Asincronia:** il search `async void` restituisce anche `Future<void>`; conteggi non utilizzabili per affermare che ci siano handler `void ... async` pericolosi. **Nessun bug async-void accertato** su questi risultati. Ricercare in futuro signature sintattiche vere, verificare writes non attesi e propagazione errori.

**Preferenze (V):**
- [Anna `lib/local_state_store.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/869d48ca651bd85e9ee4952264c87a9e33904606/lib/local_state_store.dart): store Sembast con checksum, fallback sul precedente valore, migrazione da SharedPreferences e operazioni `Future` attese. **Preservare**, nessun refactor obbligatorio.
- [Notes `flutter_app/lib/src/app.dart`](https://github.com/riccardopinato/Notes-Ecosistema/blob/6e8510c721308d0acceeda12d0b4090268118cdd/flutter_app/lib/src/app.dart): `SharedPreferences.getInstance()` legacy per lingua/tema ma scritture attese; **P2 valutare** modernizzazione solo con test di compatibilità/migrazione, non presupporre perdita dati.
- [World Days `lib/data/preferences_repository.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/data/preferences_repository.dart): modelli preferenze tipizzati, parsing difensivo e compatibilità categorie legacy; la presenza del package non prova un difetto.

**Dart 3 / migrazione:** l'esempio HTML.it `async void` per persistence non va copiato; anche la guida usa API storiche `RaisedButton`, tema pre-M3, geolocator istanziato e rotte nominali. Lo stack push/pop è **LIFO**, non FIFO come descritto nell'articolo. Verifica prioritaria solo quando una di queste forme sia davvero presente nel codice consumer.

## 3. UI, performance e responsive — audit campionato

- **Anna (V):** `ListView.builder` compare in `lib/src/unified_capture.dart`, `lib/src/diary/diary_memories.dart`, `lib/src/screens/shopping_list_screen.dart`; **lazy-list già presente**. Non imporre un secondo componente generico. Restano NV misure startup, scroll/jank, image decode, regressione visiva e grandi dimensioni testo.
- **Notes (V):** `ListView.builder` compare in `flutter_app/lib/src/screens/notes_screen.dart`, `planner_screen.dart` e altri widget. [`notes_screen.dart`](https://github.com/riccardopinato/Notes-Ecosistema/blob/6e8510c721308d0acceeda12d0b4090268118cdd/flutter_app/lib/src/screens/notes_screen.dart) preserva `dispose()` del debounce e `mounted` dopo async; non etichettare automaticamente state lifecycle come carente. Performance fisica/browser NV.
- **World Days (V):** [`calendar_page.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/features/calendar/calendar_page.dart) usa `ListView(children: ...)` per schermata composta principalmente da sezioni UI e griglia del mese: nessun bug provato. [`saved_page.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/features/saved/saved_page.dart) e [`around_the_world_page.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/features/discover/around_the_world_page.dart) costruiscono `ObservanceCard` tramite loop dentro `ListView(children: ...)`: **P2 benchmark** con centinaia di elementi, possibile costo eager; non modificare senza misure. Questo è il delta più specifico emerso.
- **FrameLab, Wonderlog, Battery Guard (NV):** HEAD fissati ma nessun benchmark UI completo. Non assumere né assenza né presenza delle 12 opportunità solo da storici.
- **Responsive/Web (NV):** servono screenshot alle larghezze 320/375/768/1280, text scaling ≥200%, keyboard, focus e system dark. Solo audit statico non basta a misurare frame budget.

## 4. Storage, Web/native e geolocalizzazione — audit campionato

- **Anna (V):** [`local_state_backend.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/869d48ca651bd85e9ee4952264c87a9e33904606/lib/local_state_backend.dart) usa import condizionale per IO/Web; [backend IO](https://github.com/riccardopinato/Agenda-per-Anna/blob/869d48ca651bd85e9ee4952264c87a9e33904606/lib/local_state_backend_io.dart) usa directory applicativa + Sembast. **Adapter già presente**, test Web/native di restore non eseguito qui.
- **World Days (V):** [`content_pack_runtime.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/core/content_pack/content_pack_runtime.dart) seleziona implementation mobile via import condizionale; [`file_content_pack_storage.dart`](https://github.com/riccardopinato/World-Days/blob/bb662cb21506b6157658f43070c2059c960637b5/lib/core/content_pack/file_content_pack_storage.dart) usa file temporanei, pointer backup, previous version e rollback. **Preservare**, non riprendere i semplici File IO della guida. Physical recovery e crash injection NV.
- **Notes (V/I):** `flutter_app/lib/src/app.dart` importa `dart:io` e alcune parti piattaforma usano bridge. **P2 verificare il percorso Web reale** su build/source target; la sola importazione non dimostra un errore runtime, né un test Web PASS.
- **CamperBoss (V):** [`location_service.dart`](https://github.com/riccardopinato/CamperBoss/blob/ae30d08f23aa7e8c835927bc98127f25662d2f6a/lib/core/services/location_service.dart) controlla GPS service, permesso negato/negato per sempre, timeout 12 s, e presenta fallback ricerca manuale. Questo è un **riferimento donor scoped candidato** per permission health; non certificato qui perché manca test specifico su device.
- **TrailPath (I/V):** [README corrente](https://github.com/riccardopinato/TrailPath/blob/3f44ab37c0881e4315033797c451cec723e23cd2/README.md) descrive Riverpod, GoRouter, Drift, MapLibre, GPS health, routing ed error state; [pubspec](https://github.com/riccardopinato/TrailPath/blob/3f44ab37c0881e4315033797c451cec723e23cd2/pubspec.yaml) usa stack Flutter moderno e geolocator recente. README **non** dimostra fisicamente precisione GPS/routing. Nessuna proposta Google Maps sostitutiva.
- **Platform parity NV:** test di backup/restore, ciclo offline/restart, account switch, permessi disabilitati, mappe offline, web fallback, consumo batteria e costo provider rimangono gate separati; nessuna modifica live a location/background/cloud.

## 5. Valutazione Golden, adattamenti minimi e promozione

| Golden/Process interno | Stato Index v29 | Azione derivata dall'audit |
|---|---|---|
| Theme Material 3 | COPY-READY GOLDEN; provider freshness NEEDS_REVIEW | usa come prima scelta, non copiarne uno da HTML.it |
| Profile Standard | COPY-READY GOLDEN | preferenze/tema; proteggere migration |
| App Shell / Responsive / Visual QA | DRAFT | aggiungere casi benchmark World Days, non promuovere |
| Media Asset Store | DRAFT | riuso asset/immagini, nessun secondo store |
| Backup / Recovery | DRAFT | estendere test e recovery, non sostituire adapter |
| Capability / Permission / Health | DRAFT; NEEDS_REVIEW | confrontare CamperBoss e TrailPath con hardware |
| Import / Export / Portability | DRAFT | test file Web/native |
| OSS Reuse / Reconnaissance | DRAFT / PROCESS CANDIDATE; NEEDS_REVIEW | blocco codice HTML.it per licenza |
| Provenance / Reuse Ledger | DRAFT / PROCESS CANDIDATE | questa ricerca è pattern reference non donor |

**Decisione maxi-step 5:** non si è materializzato un gap che richieda un adapter nuovo senza duplicare un'implementazione già esistente. **0 patch app, 0 test Flutter/Android/Web eseguiti, 0 donor/Golden promossi, 0 claim certificazione**. Priorità successiva è un benchmark mirato `World-Days/SavedPage` e `AroundTheWorldPage` con dataset realistici, poi read-only static scan per tutte le repo Flutter su checkout locali. Una eventuale correzione si farà nel repository dell'app, con propria Product Bible, branch, test `flutter analyze`/`flutter test`, Web e CI exact-head; non attraverso modifiche alla Factory o alle app motivate dalla sola guida.

## Strumento QA riutilizzabile (non un Golden)

Aggiunti [`scripts/audit_flutter_antipatterns.py`](../../scripts/audit_flutter_antipatterns.py) e [`tests/flutter_antipatterns_test.py`](../../tests/flutter_antipatterns_test.py). È uno **scanner locale read-only** senza network, senza dipendenze extra: processa directory `*.dart`, esclude file generati, produce JSON di candidati `LEGACY_API`/ `REVIEW` con path e linea, e non modifica il checkout. Esempi: `RaisedButton` => `LEGACY_API`; `ListView(children:...)`, `dart:io`, `SharedPreferences.getInstance()` => solo `REVIEW`, **non errori automatici**.

```bash
python3 scripts/audit_flutter_antipatterns.py /percorso/repo-flutter > flutter-audit.json
python3 scripts/audit_flutter_antipatterns.py --fail-on-legacy-api /percorso/repo-flutter
python3 -m unittest discover -s tests -p 'flutter_antipatterns_test.py'
```

**Prova locale:** 2/2 test sintetici PASS su versione identica dello script; copertura di segnalazione API legacy, esclusione generati e no false-positive di `Future<void>` / `ListView.builder`. **Non è stata eseguita la scansione sui checkout completi delle app** né `flutter analyze` dei consumer. La PR GitHub ha un gate separato per questa modifica.

## Criteri di chiusura per riuso futuro

1. Il gap è dimostrato da file+linea e un comportamento misurabile (non solo da grep o HTML.it).
2. Golden/donor interno esistente controllato per quell'esatto problema e consumer.
3. Codice esterno solo con licenza verificata del singolo file oppure reimplementazione indipendente.
4. Test funzionale di success/error/offline/restart, Web/native e accessibilità dove pertinenti.
5. Provenance con SHA, plugin/toolchain, dipendenze, regressioni, dimensione e risultati CI.
6. Nessun `CERTIFIED GOLDEN` senza la ladder centrale completa e consumer/harness indipendente.

## Riferimenti aggiornati

- https://docs.flutter.dev/perf/best-practices
- https://docs.flutter.dev/ui/adaptive-responsive
- https://docs.flutter.dev/ui/navigation
- https://docs.flutter.dev/release/breaking-changes/buttons
- https://docs.flutter.dev/release/breaking-changes/scaffold-messenger
- https://pub.dev/packages/shared_preferences
- https://pub.dev/packages/geolocator
- https://dart.dev/null-safety

**Chiusura:** maxi-step 1 catalogazione di ricerca; step 2/3/4 *audit campionati con evidence* e gap/non-gap distinti; step 5 valutazione riuso completata con decisione **NO PROMOTION / NO CODE CHANGE**. **Non** è un audit 360° file-per-file di ogni repository, né build/performance test su hardware.