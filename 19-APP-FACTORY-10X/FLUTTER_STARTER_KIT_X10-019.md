# X10-019 — Flutter Starter Kit minimale

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` · Master v27 · Golden Index v29. **Classificazione:** SOURCE_GENERATOR / PYTHON_TESTED (Flutter toolchain non installata in questa CI).

## Sorgente realmente aggiunto
- [Generatore idempotente per directory nuove](../../scripts/factory_10x_flutter_starter.py): `python3 scripts/factory_10x_flutter_starter.py --name demo_starter --output /tmp/demo_starter`.
- [Test Python](../../tests/factory_10x_flutter_starter_test.py): generazione delle 8 risorse, campi ARB IT/EN, Material 3, token, rifiuto nomi insicuri/symlink e sovrascrittura.
- File risultanti: `pubspec.yaml`, `l10n.yaml`, `lib/main.dart`, `lib/src/theme/app_tokens.dart`, `lib/l10n/app_en.arb`, `lib/l10n/app_it.arb`, `test/widget_test.dart`, `README.md`.

Il generatore emette solo sorgenti, **non** esegue Flutter né genera platform runners nativi. Dopo la generazione, creare i file Android/iOS/Web con `flutter create` nella destinazione senza sovrascrivere quanto generato; eseguire `flutter pub get`, `flutter gen-l10n`, `flutter analyze`, `flutter test` e `flutter build web --release` in una toolchain Flutter compatibile e fissata.

## Boundaries
- Theme seed e testi IT/EN sono **valori dimostrativi** da adattare alla Product Bible di ogni app.
- Nessun pacchetto Golden, donor, identity, backup, monetizzazione, API, telemetry o AI è automaticamente incluso o approvato.
- Nessuna copia di codice esterno/no licenza non verificata. Il codice generato è nuovo.
- **Non provati**: compilation/build Flutter in CI, collaudo Android/iOS, app connessa a repo consumer, produzione APK/AAB, due consumer o risparmio 10x. Il test Python prova soltanto la correttezza strutturale del bootstrap.
- Successori X10-020/021/022/023 dipendono dal consolidamento del kit, revisione Product Bible e test consumer separati.

## Definition of Done per X10-019
Sorgente generatore + scaffold + token design + IT/EN l10n + docs e regressioni offline in una PR con CI exact-head, **scope limitato SOURCE**. La validazione Dart/Flutter reale è successiva e rimane `NOT_VERIFIED` finché non esiste il suo run.
