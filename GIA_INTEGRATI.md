# Già integrati — archivio delle implementazioni confermate

> Esclusi automaticamente da DA_VALUTARE per la stessa app. CI verificata non significa prova fisica né pubblicazione Play. La stessa capability può essere integrata in un'app e ancora proposta in un'altra.

## Capability con prova di codice puntuale (8)

| App | Capability | Priorità | Facilità | Stato | Prova |
| --- | --- | --- | --- | --- | --- |
| Agenda-per-Anna | [CAP-0077](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0077.md) Health check permessi nativi per-capability | 94 | 70% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/capability_health.dart) |
| Agenda-per-Anna | [CAP-0001](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0001.md) Pianificazione di slot liberi | 93 | 95% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/calendar_free_slots.dart) |
| Agenda-per-Anna | [CAP-0111](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0111.md) Weekly Review con proposte di pulizia e ripianificazione | 91 | 80% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/weekly_review.dart) |
| Agenda-per-Anna | [CAP-0002](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0002.md) Creazione eventi da linguaggio naturale | 88 | 95% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/natural_event_parser.dart) |
| Agenda-per-Anna | [CAP-0005](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0005.md) Esportazione esplicita eventi verso calendario | 87 | 75% | CI_VERIFIED / PARTIAL_REUSE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/android_calendar_sync.dart) |
| Agenda-per-Anna | [CAP-0003](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0003.md) Preparazione contestuale appuntamento | 81 | 95% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/event_preparation.dart) |
| Agenda-per-Anna | [CAP-0113](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0113.md) Da appuntamento passato a ricordo privato | 81 | 95% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/lib/src/event_memory_capture.dart) |
| Agenda-per-Anna | [CAP-0069](12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0069.md) Automated screenshot visual regression | 81 | 65% | CI_VERIFIED / EXISTING_SOURCE | [codice](https://github.com/riccardopinato/Agenda-per-Anna/blob/fb476545426fb6bf290e74f53e735fa13616e4e9/tool/compare_visual_baselines.py) |

## Idee IA26 con funzione equivalente già in codice (2)

| Idea | Priorità | Facilità | App correlata | Stato | Prova |
| --- | --- | --- | --- | --- | --- |
| [#62](11-NUOVE-IDEE/IA-2026-11-02/SCHEDE/IA26-062.md) Allarme Telefono Toccato | 80 | 80% | Phone-Guard | INTEGRATED | [codice](https://github.com/riccardopinato/Phone-Guard/blob/ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c/app/src/main/java/com/riccardopinato/phoneguard/service/ProtectionForegroundService.kt) |
| [#50](11-NUOVE-IDEE/IA-2026-11-02/SCHEDE/IA26-050.md) Allarme Anti-Borseggio | 78 | 60% | Phone-Guard | INTEGRATED | [codice](https://github.com/riccardopinato/Phone-Guard/blob/ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c/app/src/main/java/com/riccardopinato/phoneguard/protection/PocketProtectionController.kt) |

Le integrazioni **parziali** non sono conteggiate come completate: sono riportate in [Da valutare, sezione verifica](DA_VALUTARE.md).

[Da valutare](DA_VALUTARE.md) · [Stato tecnico originario](12-CAPABILITY-E-IMPLEMENTAZIONI/STATO_IMPLEMENTAZIONI.md)
