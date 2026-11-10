# AL-ANDROID-2026-001 — Adaptive Landscape (Deskland concept → Android)

**Data:** 10/11/2026  
**Origine:** richiesta esplicita nuova app Android standalone, Flutter preferito, vendita una tantum ipotizzata €1,99/€2,99.  
**Stato prodotto (10/11/2026, aggiornamento):** `ACTIVE_REPOSITORY / v0.3.1 SOURCE_MERGED`; Flutter/Dart test e build Android/Web, incluso APK debug e release-mode per ABI, **CI VERIFIED su PR #3**. Web v0.2 confermato dall'utente come base valida. Beach v0.3 GitHub Pages deploy main SUCCESS [run #42822909836](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42822909836); v0.3.1 main pipeline/deploy IN_VERIFICA, Web visuale v0.3.x ancora non validato dall'utente. Test fisico Android, compatibilità OEM, batteria, firma stabile e Google Play **NON ATTESTATI**. Repo: https://github.com/riccardopinato/Adaptive-Landscape-Android; main source commit `72de4ff0bdd6204a9e26b0f19aa9585343e891e3`.  
**Posizionamento:** Android live wallpaper offline, senza account/AI/ads; paesaggio che lascia spazio alle icone della Home; espandibile a scenari successivi.  
**Package Android previsto da Flutter scaffold:** `it.riccardopinato.adaptive_landscape` (Activity e Service Kotlin in namespace distinto); nome commerciale provvisorio, da distinguere nettamente da Deskland.

## Correzione grafica Beach v0.3.0–v0.3.1 — SOURCE + CI

- **Brief utente:** Beach visto dall'alto, soltanto sabbia che si forma e mare in movimento; niente cielo, nuvole, sole, orizzonte o decorazioni per Beach.
- Il riferimento Deskland `prototype/flat.html` e `themes.json` è fonte UX/visuale **E1 GPL-3.0**, non risorsa da copiare in codice/assets. La nuova scena è originale e modellata in `lib/core/beach_coast.dart`, `lib/ui/beach_surface.dart`, `android/.../CoastalBeachRenderer.kt`.
- [App PR #7](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/7): merge `c220b64e5443e72987e86537009d078f45a02b45`, PR CI [#42821824304 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42821824304); GitHub Pages main [#42822909836 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42822909836).
- [App PR #8](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/8): merge `72de4ff0bdd6204a9e26b0f19aa9585343e891e3`, PR CI [#42824258762 SUCCESS](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42824258762), velocità frazionarie con fasi senza salti su Web/native. **La pipeline main v0.3.1 è in verifica**.
- La fidelity pixel-perfect e il livello "quasi reale" sono **da valutare dall'utente** sulla nuova Web. Test Android/OEM e Play restano bloccati in [issue #4](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/4), [#5](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/5), [#6](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/6). Nessuna nuova CAP/Golden o donor E3 certificata.

## Evidenza aggiornata v0.2.0 — release gates separati

- Applicazione: [Adaptive-Landscape-Android](https://github.com/riccardopinato/Adaptive-Landscape-Android), PR [#3](https://github.com/riccardopinato/Adaptive-Landscape-Android/pull/3) squash merge su `main@9538849c3c478c677bba246359c646e9fef04a11`.
- PR head `4f5d4e4df7e59cec6ed87acc2e56bb4c7fbde222`: GitHub Actions [#42812771584](https://github.com/riccardopinato/Adaptive-Landscape-Android/actions/runs/42812771584) **SUCCESS** (contratto privacy/locales, Flutter analyze, 19 tests, Kotlin build APK debug, APK ottimizzati release-mode per ABI, Web build).
- Cinque maxi-step: architettura schema V2; griglia 3–8 × 3–12 e widget zones; Meadow/Beach palette e night/animazioni; 6 lingue/profili JSON/offline; CI QA build, privacy, matrice QA Play — **implementati a livello source/CI**. La validazione fisica e Play non sono state svolte.
- APK ARM64 release-mode interno 17.762.708 byte, APK ARM32 15.262.138, APK x86_64 19.140.583; **NOT Play signed**. Conservare artefatto + hash per device QA successivo.
- Issue da collaudare: [#4 device/OEM](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/4), [#5 Store/signing](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/5), [#6 visual/energy/parity](https://github.com/riccardopinato/Adaptive-Landscape-Android/issues/6).
- Nessuna promozione **Deskland E1 → E3**, nessuna nuova capability/Golden automaticamente certificata: la certificazione richiede evidenza donor e consumer disciplinata dal Core corrente.

## Fonte OSS fissata — evidence E1

- Repository: https://github.com/BLEZZ0102/Deskland
- Source SHA (40): `9818b577402ff476e1b59da07970c56472713126` (HEAD letto 10/11/2026)
- Sorgenti studiati: `README.md`, `host/DesktopHost.cs`, `prototype/flat.html`, `prototype/meadow.html`, `prototype/themes.json`, `NOTICE`, `TRADEMARKS.md`, `THIRD_PARTY_NOTICES.md`.
- Licenza progetto + asset inclusi: **GPL-3.0**. Marchio e icona Deskland non concessi come trademark. Windows host usa WebView2; non portabile direttamente su Android.
- Classificazione: **PRODUCT/UX REFERENCE — OSS_REFERENCE_REWRITE — E1**, NON `CODE_DONOR` pronto da importare per un consumer proprietario.
- Donor certification: **E3 NON ATTESTATA**: non eseguiti test sul ref upstream esatto, nessuna CI exact-source della specifica capacità, nessun consumer Android verificato. Non promuovere a CERTIFIED DONOR né Golden.
- Se si decidesse un fork derivato reale, sarebbe necessaria compatibilità GPL-3.0 per la distribuzione, disponibilità del sorgente derivato e rispetto notice/attribuzioni; vendita GPL consentita ma non significa codice proprietario chiuso.
- Per l'app commerciale prevista: non copiare codici, asset, shader, UI e icona Deskland; implementazione originale del concetto.

## Problema Android fondamentale

Un'app ordinaria che implementa `WallpaperService` non riceve dal framework la posizione reale delle icone del launcher. Per mantenere un'app offline/privacy-safe e pubblicabile, V1 usa **calibrazione manuale della griglia occupata**. Il wallpaper non sposta le icone e non può promettere sincronizzazione automatica universale; multi-home/launcher/OEM sono test futuri. Non introdurre `AccessibilityService` / `MediaProjection` di nascosto: necessitano gate specifici di consenso/policy e non garantiscono compatibilità.

## MVP preparato fuori dal catalogo

Il sorgente fornito in chat comprende:
- Flutter Material3 con localizzazione ARB EN/IT/ES/FR/DE/PT e preview Beach/Meadow originale;
- motore di influenza locale su coordinate normalizzate 5x8 + test puri;
- Android nativo Kotlin `WallpaperService`, pausa quando non visibile, 20fps / 8fps battery saver e `MethodChannel` config;
- picker Android, scene e marchio originali (non asset GPL);
- script bootstrap PowerShell/Bash e installer singolo file .txt, roadmap e provenance.

**Evidence:** XML parsing + coerenza ARB + controllo strutturale + shell syntax Bash PASS. **Flutter analyze/test/build, runtime, firma e certificazione device: NON ESEGUITI**. Non collegare uno stato `IN_CODICE` al catalogo GitHub prima che esista un repository app verificabile.

## Reuse Golden / Factory baseline

Factory: `riccardopinato/App-Factory-Core@d4ed1185d36d419228fba6b57a979cde308bd321`; CURRENT Master v27 / Index v29 / Registry v2.

- `GOLDEN_APP_BOOTSTRAP_FLUTTER_v1_DRAFT`: manifesto e architettura minima.
- `GOLDEN_THEME_M3_FLUTTER_v1`: UI Material3 / token.
- `GOLDEN_LOCALIZATION_FLUTTER_v1`: ARB sei lingue.
- `GOLDEN_ANDROID_NATIVE_RELIABILITY_v1_DRAFT`: owner unico del wallpaper, stop rendering invisibile, battery discipline.
- `GOLDEN_CI_RELEASE_WEB_DEPLOY_FLUTTER_v2`: CI/Android signing e artifact gate (non ancora eseguiti).
- `GOLDEN_OSS_REUSE_RECONNAISSANCE_FLUTTER_v1_DRAFT`, `GOLDEN_PROVENANCE_REUSE_LEDGER_v1_DRAFT`, `GOLDEN_SINGLE_DONOR_CAPABILITY_ADMISSION_v1`: licenza e livelli E1/E3.
- `GOLDEN_RELEASE_REALITY_PHYSICAL_VALIDATION_v1_DRAFT`: distinzione build/device/store.

## 5 maxi-step

1. Aprire repo dedicato e bootstrap Flutter/Android, CI + debug APK su branch, prova WallpaperService reale.
2. Calibrazione multi-device/launcher/dock, persistenza e layout gestibili.
3. Qualità grafica, animazioni originali collision-aware, consumi e FPS testati.
4. UX premium, localizzazione nativa, preferenze/profili e test OEM.
5. Firma stabile, Play Internal Testing, pricing €1,99 vs €2,99, AAB/asset originali, release solo dopo gate.

**CAP/GOLDEN:** nessuna nuova CAP in registry senza chiaro contratto ricorrente, kit e verifica; prima confrontare catalogo esistente e implementazioni effettive. Questo dossier non è una certificazione.
