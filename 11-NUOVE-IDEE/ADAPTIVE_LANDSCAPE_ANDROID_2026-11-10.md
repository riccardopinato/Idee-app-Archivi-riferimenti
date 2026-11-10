# AL-ANDROID-2026-001 — Adaptive Landscape (Deskland concept → Android)

**Data:** 10/11/2026  
**Origine:** richiesta esplicita nuova app Android standalone, Flutter preferito, vendita una tantum ipotizzata €1,99/€2,99.  
**Stato prodotto:** `IN_ROADMAP` come obiettivo; **sorgente MVP locale preparato fuori dal repository delle idee**, **NOT VERIFIED** su Flutter/Android/CI/dispositivo/Store. Nessun nuovo repo app creato, APK non prodotto.  
**Posizionamento:** Android live wallpaper offline, senza account/AI/ads; paesaggio che lascia spazio alle icone della Home; espandibile a scenari successivi.  
**Package MVP proposto:** `it.riccardopinato.adaptivelandscape`; nome commerciale provvisorio, da distinguere nettamente da Deskland.

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
