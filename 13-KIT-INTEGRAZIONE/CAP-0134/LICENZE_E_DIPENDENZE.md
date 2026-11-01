# CAP-0134 — licensing and compatibility gate

**Source:** https://huggingface.co/vivekkaushal/DocRex — model card advertises Apache-2.0; backbone claimed Apache-2.0. Commercial suitability **still subject to file-level provenance validation** before copying weights into a shipping app.

- Recommended file `invoice_classifier_fp32.onnx`: 6.084.524 bytes, declared SHA256 `bbe9997671953145206939291c592dc937c6c523202234bba66e8a589cc643db`.
- Model card reports INT8 58.85% vs FP32 98.35% on a 243-image held-out set. **INT8 unsuitable for automatic deployment.**
- Architecture: MobileNetV3 Small, opset 18, uses ONNX Runtime as a candidate; runtime library and platform plugins require independent compatibility/license checks.
- Donor ref immutable commit: **NOT PINNED**. No donor code/payload downloaded; our Dart adapter is original (NEW_IMPLEMENTATION).
- Platform notes from `flutter_onnxruntime` package documentation: Android JNI/16KB compatibility and iOS minimum support require their own build investigation; **no plugin validated in Notes yet**.
- Privacy: model evaluates pixel content locally in its declared use; no PII redaction, no upload/no analytics by our adapter. Do not infer data residency from external inference services.
