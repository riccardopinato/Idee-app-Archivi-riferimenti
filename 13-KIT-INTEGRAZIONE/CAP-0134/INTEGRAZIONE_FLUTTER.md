# CAP-0134 — Notes adapter plan after source inspection

Repo audit: `riccardopinato/Notes-Ecosistema@3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c`.

1. Attach to existing `flutter_app/lib/src/domain/documents.dart` + `data/document_store.dart` with a read-only proposal service. For images use existing `attachments.dart` SHA-256 media store; PDF render as local page preview. Do not edit originals.
2. The `pubspec.yaml` has no ONNX dependency. Compare a maintained ONNX Runtime Flutter adapter (and native ARM64/16KB-page/AGP/iOS compatibility) **before** adding it. No new dependency is installed in the kit.
3. Keep optional model with checksum `bbe9997671953145206939291c592dc937c6c523202234bba66e8a589cc643db` and explicit user action; do not silently download. FP32 size ~5.8 MiB plus unknown runtime overhead.
4. Decode/resize selected document to 256 RGB, use `DocRexContract.normalizeCenterCrop`, pass NCHW float32 into the ONNX model, evaluate logits and create `TriageDecision`.
5. Propose only invoice or statement if confident; `other` produces **no automatic folder/category**. Never move files, write category, trigger cloud or OCR based on uncertain output without user confirmation.
6. Tests: contract CI; then instrumentation using Italian samples, PDF pages, memory/size profiling and physical device. **No claim of end-to-end runtime testing**.
