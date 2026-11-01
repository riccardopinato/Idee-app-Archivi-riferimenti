# CAP-0114 — Anna's Diary: filtro di sicurezza testuale

**Sorgente app:** riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2, [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/docs/PRODUCT_BIBLE.md), [AgendaStore](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/agenda_store.dart), [DayJournal / DiaryBlock](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/domain_models.dart), [MediaAssetStore](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/media_asset_store.dart).

Il Product Bible esclude Vault, Password Vault, ciclo ed E2EE Noi dai percorsi ordinari di export, backup e ricerca. L'adattatore **non entra in quei domini**: ammette solo `AnnaTextOrigin.ordinaryPrivate` e testo senza media binari, e fallisce per shared/vault/ciclo/unknown/account changed. L'oggetto restituito e **solo una bozza** con `productionSafeRedaction=false`.

- [lib/anna_text_privacy_gate.dart](lib/anna_text_privacy_gate.dart) riutilizza il parser limitato [privacy_preview.dart](lib/privacy_preview.dart); nessun modello donor copiato.
- [test/anna_text_privacy_gate_test.dart](test/anna_text_privacy_gate_test.dart): testo mascherato in copia, perimetri proibiti, media e account switch.
- Non copre indirizzi/nominativi/telefono, metadati, immagini, PDF, allegati, OCR, testo annidato in export o verifiche anti-recovery. **Non e una redazione sicura da esportare o condividere.**
- Licenza riferimento [Redact](https://huggingface.co/desert-ant-labs/redact): source-available / `other`, condizioni commerciali separate; non importare SDK/weights senza revisione.

**Compatibilita:** solo adapter Dart testabile. Flutter UI e integrazione al writer/export NON eseguite. Facilita stimata Anna 40%, non probabilita di superamento di test.
