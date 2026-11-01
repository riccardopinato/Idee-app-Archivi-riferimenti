# CAP-0134 — test plan and evidence

## Automated standalone contract tests

- [test/document_triage_test.dart](test/document_triage_test.dart) (Dart SDK only).
- Cases: 3-channel normalization, center crop, input shape, label order, stable softmax, unknown/low confidence, NaN, out-of-range threshold.
- [Workflow](../../.github/workflows/kit-dart-compat.yml) must pass exact PR head before a merge.

## NOT tested

- ONNX graph load or binary checksum of actual downloaded model; PDF and camera decoding; GPU/CPU throughput; device RAM and APK size; compatibility with Notes build; Italian-language invoices; model privacy/accessibility; no Android/iOS runtime or real-device QA.

**Status:** Dart contract test result is only whatever the linked CI proves; donor-level claimed 98.35% is not our measurement. Integration state in app: `PROPOSTA`.
