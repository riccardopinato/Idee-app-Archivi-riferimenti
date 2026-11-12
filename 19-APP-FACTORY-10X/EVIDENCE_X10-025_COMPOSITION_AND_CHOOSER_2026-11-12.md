# X10-025 — Flutter kit composition & dependency chooser

**Factory:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. **Predecessori:** X10-020/021/022, SOURCE+DART_CI, non Flutter device. X10-023 notification source is available but remains PLANNED for native/device testing; its use here is a Dart-only dependency boundary.

## Implementazione reale

[Package](flutter_kits/composition/) `factory_kit_composition 0.1.0` dipende tramite **path locali** dai quattro package Dart già presenti:

| Kit | Default / relazione | Necessità prima di consumer reale |
|---|---|---|
| `profile` | Core locale di preferenze, non obbliga login | Storage atomico per owner, UI/l10n, test di preferenze e migrazioni |
| `identity` | Login **opt-in**; non attivato dalla composizione | Provider OAuth/PKCE reale, verifica indipendente dei claims, session isolation e callback testate |
| `backup` | Contratto manifest/SHA e rollback; Golden **CANDIDATE** | Transaction/media adapter, safety snapshot e no-loss/crash test consumer; non copia credenziali da altri kit |
| `notifications` | Source di policy, non un receiver o OS scheduler | Android/iOS native permissions, canale, timezone, OS callbacks, receipt fisiche; non attivabile come provider web |
| `monetization` | **REFUSED** | Gate separato HUMAN, policy prodotto, Play Billing/AdMob/provider e consenso |

Il chooser non scrive alcun repository e **non abilita runtime**, pagamenti, OAuth, notifiche o backup. Il boolean dichiarativo `productBibleReviewed` segnala se il richiedente afferma di aver svolto una review, ma non prova una decisione o firma. Una scelta kit produce sempre una lista di gate di integrazione; non esiste un flag che certifica una release.

## Fixture incrociata

[Integration suite](flutter_kits/composition/test/composition_test.dart) importa **i quattro pacchetti reali** nello stesso Dart process, con adapter finti:
- preferenze profilo locali persistite, analytics opt-in inizialmente false;
- login senza azione esplicita non avvia provider, annullamento lascia dati locali intatti;
- backup costruito su allowlist dati locale, SHA/inspect e restore staged su fake port;
- notification permission denied non chiama schedule, non interrompe profilo o backup;
- monetizzazione sempre rifiutata, piattaforma web non finge un provider notifiche native;
- selezione deterministica e feature flags immutabili.

**Verifica reale del codice:** [CI Dart](../.github/workflows/app-factory-10x-dart-kits.yml) usa SDK 3.6.0 e action pin, esegue `pub get`, `analyze`, `test` su ciascun kit, ora includendo `composition`. Nessun sample è stato eseguito su emulator/telefono; un test Dart con fake provider non equivale a real auth, native delivery, backup sul filesystem o interoperabilità di due app. Non crea Product Bible, icona o build native per nuove app.

**Esito X10-025:** SOURCE+DART_CI soltanto dopo exact-head CI e merge. Richiede product admission e test consumer per ogni vera adozione.
