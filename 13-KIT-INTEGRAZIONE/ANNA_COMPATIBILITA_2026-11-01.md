# Anna's Diary — compatibilita kit sorgente e contratti, 1 novembre 2026

- **Factory baseline fissata nella sessione:** `App-Factory-Core@63dd5e4f703cb23e4095a72beb253720bc1ca9a1` (Master v27, Golden Index v23).
- **App letta in sola lettura:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`, Flutter `1.0.0-rc.6+117`, Dart >=3.10.0, [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/docs/PRODUCT_BIBLE.md), [roadmap](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/docs/ROADMAP.md). **Nessun commit/PR su Agenda-per-Anna**.
- **Priorita di roadmap esistente:** C1 diagnosi permessi, C2 visual regression; nuove capability qui rimangono proposte, non approvate automaticamente.
- **Inventario reale:** `AgendaStore.items` (private), `UnifiedAgendaEntry` separa private/shared/external; `CalendarFreeSlot` deriva slot da appuntamenti autorizzati e blocca conservativamente quelli senza orario/fine; `AgendaItem` supporta task+done+recurrence ma NON una durata task canonica; `WeekData` contiene già focus/priorities/reflection; `DayJournal` e `DiaryBlock` sono canonici; MediaAssetStore conserva media con SHA-256; Vault/Password Vault/ciclo/Noi segregati.
- **Azione eseguita:** codice Dart originale preparato e test unitari per tre contratti minimi, con workflow `kit-dart-compat.yml`. Nessuna dipendenza nuova e nessun donor copiato.

| Kit | Origine fonte/compatibilità | Codice e verifiche preparate | Ease Anna precedente -> dopo | Gate reale ancora assente |
|---|---|---|---:|---|
| CAP-0102 Smart Rescheduler | `CalendarFreeSlot` + `AgendaItem`, solo task private e slot con coverage completa | [preview Dart](CAP-0102/lib/anna_reschedule_preview.dart), [test](CAP-0102/test/anna_reschedule_preview_test.dart) | 80% -> **70%** | UI, durata esplicita, revision/commit account-safe, timezone, device |
| CAP-0111 Weekly Review | `AgendaStore.items`, `AgendaItem.done`, `WeekData` | [proiezione Dart](CAP-0111/lib/anna_weekly_review.dart), [test](CAP-0111/test/anna_weekly_review_test.dart) | 90% -> **80%** | UI, permission/scope e writer `WeekData`, ricorrenze, device |
| CAP-0114 Privacy Shield | `DayJournal` e policy export privacy senza Vault/Noi | [adapter Dart](CAP-0114/lib/anna_text_privacy_gate.dart), [test](CAP-0114/test/anna_text_privacy_gate_test.dart) | 45% -> **40%** | Redazione PDF/media/metadati, privacy review, security test |
| CAP-0134 Document Auto-Sorter | DocRex runtime ONNX assente, Anna non e archivio documentale | Riutilizzabile il [contratto generico](CAP-0134/lib/document_triage.dart), nessun adattatore app-specifico | 55% -> **35%** | Business scope e runtime/model benchmark, NON prioritario |
| CAP-0138 Audio-Linked Ink | Canvas/registrazioni di Anna non hanno lo stesso contratto di Notes whiteboard | Nessuna associazione CAP/app aggiunta | n.d. | Studio nuovo feature solo se approvato nel Product Bible |

## Confini di sicurezza e correttezza

1. **Niente AI obbligatoria.** Plan My Day e un benchmark sperimentale, non un motore di planner con evidenza di efficacia reale. Il codice CAP-0102 e originale e deterministico.
2. **No mutation.** I due motori per agenda sono puri e non salvano/rischedulano alcun record né attivano notifiche, cloud o account.
3. **Dati visibili:** non usare Shared Space/E2EE, external events senza consenso, Vault/ciclo o media per le riepilogazioni. Ogni account switch o calendar coverage incompleta fa fallire la proposta.
4. **WeekData:** non inventare data di completamento dal booleano `done`; usare l'etichetta **task datate nella settimana attualmente completate**.
5. **Privacy:** il parser riconosce solo email e IBAN validi in testo; la copia mascherata NON e export sicuro, non garantisce che altri PII o metadati siano rimossi.
6. **Test gate:** verifiche Dart CLI `dart analyze`, esecuzione test su stessa PR-head, catalogue CI. Non equivale ad una app Flutter compilata o collaudata su telefono.
7. **Kit status:** source-backed contract prototype, non FULL CODE-READY INTEGRATION e non APP IN_CODICE. `app_states` resta `PROPOSTA`.

## Prossimo livello quando autorizzato in roadmap Anna

- Una piccola PR dedicata in Agenda-per-Anna per CAP-0111 per prima: adattare solo lettura al `AgendaStore`, presentare riepilogo nella vista esistente, mantenere WeekData canonico e test Flutter/widget.
- CAP-0102 in seguito: input durata esplicita, feed slot autorizzati e preview/commit con controlli ottimistici su account/revision.
- CAP-0114 come funzionalita privacy limitata solo dopo approvazione del perimetro e audit export; non usare la bozza quale sistema di oscuramento garantito.
- Per ogni futura integrazione serve controllo Product Bible, test Flutter full source, Web/Source Gate e test Android fisico sul nuovo APK firmato. L'APK +117 esistente non contiene queste feature.

**Evidence report:** i link GitHub CI di questa PR determineranno l'esito dei contratti eseguibili; un report non puo dichiarare PASS prima del completamento dei job.
