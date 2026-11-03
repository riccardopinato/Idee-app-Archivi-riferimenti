# Audit incrociato Anna's Diary — aggiornamento evidenze CAP

**Data:** 2026-11-03
**Factory baseline:** [App-Factory-Core@a3c65963](https://github.com/riccardopinato/App-Factory-Core/tree/a3c65963e9f060f1a02de96ade1b0985a4adcdab), CURRENT Master 27 / Golden Index **26**.
**Sorgente verificata:** [Agenda-per-Anna@827bb616](https://github.com/riccardopinato/Agenda-per-Anna/tree/827bb61620960d8867eb03e453d142013aada786); [Development checks](https://github.com/riccardopinato/Agenda-per-Anna/actions/runs/41458618496) SUCCESS, include Flutter analyze/test.
**Ambito:** riclassificare solo prove circostanziate e preservare la distinzione tra codice, CI, device, firma e rilascio. Nessuna modifica all'app da questa PR.

## Correzioni del registro

| CAP | Prima | Dopo | Evidenza / limite |
|---|---|---|---|
| CAP-0014 | PROPOSTA | CI_VERIFIED | `event_memory_capture.dart` con `v107_a1_event_to_memory_test.dart` nella suite esatta; nessun test fisico |
| CAP-0027 | PROPOSTA | SOURCE_CONFIRMED | `share_capture_service.dart` / `v098_capture_everywhere_test.dart`; capture da Android reale non provata |
| CAP-0055 | SOURCE_REPORTED | SOURCE_CONFIRMED | `notification_service.dart` include azioni native e snooze; consegna e background su OEM da verificare |
| CAP-0069 | CI_VERIFIED | CI_VERIFIED | Comparatore `tool/compare_visual_baselines.py` realmente presente; 70 coppie screenshot reali non approvate |
| CAP-0077 | CI_VERIFIED | CI_VERIFIED | `capability_health.dart` presente; permission granted non è servizio healthy |
| CAP-0111 | CI_VERIFIED | CI_VERIFIED | `weekly_review.dart` e test esistenti; non certifica singole notifiche e restore |

Il registro conserva **147 CAP**, con **68 associate ad Anna**. I due vecchi suggerimenti NotebookLM P3 esclusi non rientrano in questo aggiornamento. Le **15 idee P1/P2** rimangono idee di prodotto distinte dallo score tecnico CAP.

## Rischi e interventi approvati

1. Widget launcher: PR [#216](https://github.com/riccardopinato/Agenda-per-Anna/pull/216) source MERGED con controllo `hideHomeDetails`, redazione sensibili e pulizia cache in cambio account; QA fisico launcher pendente. CAP-0144 resta PROPOSTA perché comprende anche countdown/foto non implementati.
2. Replanning CAP-0102: PR [#217](https://github.com/riccardopinato/Agenda-per-Anna/pull/217) source MERGED; UI propone orari, conferma, ricontrolla conflitti e account. Classificare la nuova evidenza solo dopo exact-head source verification e senza dichiarare device PASS.
3. Lettera personale CAP-0142: PR [#218](https://github.com/riccardopinato/Agenda-per-Anna/pull/218) in validazione. La modalità condivisa non è approvata e Privacy V2 #215 resta sospesa.
4. Data safety: verifiche consolidate nel percorso standard `test/v100_data_safety_v21_test.dart`, `test/v048_universal_lifecycle_audit_test.dart`, `test/v107_quick_wins2_test.dart`; restore fisico e multi-account non certificati.
5. Release: aumentare `versionCode` da 120 soltanto dopo source merge e controlli; APK firmato, artifact SHA e dispositivo restano gate distinti.

**Non sono autorizzati** merge Privacy #215, Google Calendar diretto #199, cambi Billing/AI/cloud, nuovi account o pubblicazione Play.

## Addendum post-merge #216–#219

- `CAP-0102` -> `CI_VERIFIED` for the *bounded assisted task rescheduling* implemented by PR #217, with direct deterministic slot tests. UI and provider/device certification remain distinct.
- `CAP-0142` -> `SOURCE_CONFIRMED` only for the *personal future-letter* subset from PR #218, including canonical DayJournal/Trash and optional early viewing. Shared capsules, true time-lock and automatic delivery reminders are **not implemented**.
- `CAP-0144` remains `PROPOSTA` as an **extended capability**. The existing launcher widget gained masked/account-scoped projection via PR #216; countdown and shared-photo widgets are still not implemented.
- Build `+121` from PR #219 is a separate Android release-evidence gate, not an automatic promotion to device or store.
- Evidence SHA: `Agenda-per-Anna@cb477cbecc85c1b1c415c60fd69bbd128fb82904`. Exact-head PR Development checks successful; Android device testing pending.
