# CAP-0114 — test matrix and scope

Dart CLI contract test: `test/privacy_preview_test.dart`, invoked in CI. Covers email, valid/invalid IBAN modulo97, explicit selection, source unchanged, stale spans, duplicate spans and max size.

**Not verified:** personal names, addresses, phones, EU national IDs, OCR/PDF, metadata, alternative text, annotations, attachments, redaction of binary files, screen capture, Android/iOS, security review, comprehensive false negatives. The contract test result is NOT production privacy certification.

Integration state per-app: PROPOSTA. Test of third-party native SDK requires license review before attempting in a commercial app.

## Gate aggiuntivo Anna

- [Test perimetro Anna](test/anna_text_privacy_gate_test.dart): consenso/ambito private, esclusione Vault/ciclo/Noi, binary media, cambio account, copia originale immutata.
- [Analisi](ANNA_COMPATIBILITA.md). Non equivale a export sicuro o QA Android, parser comprende solo email e IBAN con checksum.
