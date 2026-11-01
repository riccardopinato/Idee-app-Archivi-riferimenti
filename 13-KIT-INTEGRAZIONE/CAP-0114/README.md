# CAP-0114 — Privacy Shield, nucleo limitato originale

**Stato: CONTRACT_PROTOTYPE**, riconoscimento parziale email + IBAN validati, non completo rilevamento PII e **non una soluzione sicura per anonimizzare PDF**.

- [Dart source](lib/privacy_preview.dart): individuazione e anteprima mascheratura di stringhe in copia, validazione modulo-97 IBAN, selezione esplicita e rifiuto posizioni non valide.
- [Test Dart](test/privacy_preview_test.dart): checksum/negativi, nessuna mutazione del testo sorgente, selezione, duplicati e limiti input.
- [Modello di riferimento](https://huggingface.co/desert-ant-labs/redact) indica SDK Kotlin/Android e capacità più ampie; `redact-demo` usa una licenza `other` e [termini commerciali dedicati](https://license.desertant.com/1.0): **nessun codice/modello donor importato**.
- Notes `0.56.3+74@3fd9b0d`: `attachments.dart` e `documents.dart` consentono di preparare un'anteprima di testo, ma esportazione realmente redatta e pulizia metadata/immagini non sono implementate.

**Facilità ricalibrata:** Notes 55%, Anna 40%, PDF-Unifier 40%. Non usare il codice come privacy guarantee.

**Anna's Diary:** [audit di compatibilita e gate di privacy](ANNA_COMPATIBILITA.md), [filtro Dart originale](lib/anna_text_privacy_gate.dart) e [test](test/anna_text_privacy_gate_test.dart). Solo testo privato ordinario; Vault, ciclo, Noi e allegati binari esclusi.

[Specifiche](SPECIFICHE.md) · [Codice](CODICE_RIFERIMENTO.txt) · [Piano Flutter](INTEGRAZIONE_FLUTTER.md) · [Licenze](LICENZE_E_DIPENDENZE.md) · [Test](TEST_E_VALIDAZIONE.md)
