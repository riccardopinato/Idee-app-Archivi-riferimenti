# Opportunità di riuso e integrazioni — audit 30/10/2026

La stessa fonte può alimentare più prodotti solo se **licenze, località, origine, versione e copertura** sono tracciate. Non creare database condiviso che mescola ownership privata di Anna/Notes/Wonderlog.

| Capability canonica candidata | Donor / fonte | Possibili consumer | Rischio e prossimo gate |
|---|---|---|---|
| Lifecycle audit harness | Anna v0.48/0.74 + Notes v0.32 | Anna, Notes, Wonderlog, CamperBoss | test a matrice per domini nuovi, non motore DB comune |
| PDF Ops | PDF-Unifier | PDF Pocket Tools, Notes Documents, Omni Cleaner exports | estrarre motore senza refactoring inutile; test input corrupt/encrypted |
| EXIF safe-copy | Android Omni Cleaner | SafeShare, FrameLab, Send to PC optional | preserving originals, embedded metadata/license check |
| Map POI Pack | OSM/Geofabrik/Overture | CamperBoss, TrailPath, Wonderlog, Pocket POI Offline | attribution, schema, region size, expiry, source revision |
| Weather/Daylight | Open-Meteo commercial + SunCalc | CamperBoss, TrailPath, ShootWindow, GrillBoss, WEB-008 | status/data age, NO commercial Free API |
| Official holidays/observances | Nager.Date + UN/UNESCO/WHO | World Days + WEB-013 | officiality rules, movable recurrences, locale ≠ market |
| Fuel data market | MIMIT et al. | WEB-002, WEB-009, DriveDay, CamperBoss | fuel price freshness, market adapter, no invented deals |
| User-owned sharing bridge | Shared Ecosystem Core v1 | Anna, Wonderlog, Notes later | COPY/LINK only, consent, no implicit cross-app sync |
| UI motion and semantics | Design-App Motion/Icon/Sound packs | Anna, FrameLab, World Days, FocuSense | library proof != app integration proof |
| Physical testing | AppLab + scrcpy/LeakCanary | all native/Flutter apps | exact device/artifact, trusted evidence |
| Local content catalog | World Days/FrameLab/Cooking Anime | editorial apps | source-backed edits, data licenses, distinct schema per subject |
| ADB/OEM packages | Easy Debloat + UAD NG reference | CleanOS standalone, DevBridge | rootless claims, privileges, policy, restore and audit log |

## Esclusioni importanti
- **Non** unire Battery Guard al motore di clean storage: le promesse cliente differiscono.
- **Non** unire Notes/Anna/Wonderlog/TrailPath in un unico archivio/DB privato.
- **Non** associare automaticamente acquisti standalone a una suite: entitlement diverso.
- **Non** copiare documentazione o immagini pubbliche senza licenza verificata.
- **Non** confondere renderer MapLibre con dataset cartografico/POI.
