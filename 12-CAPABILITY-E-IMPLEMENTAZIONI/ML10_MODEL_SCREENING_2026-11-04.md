# ML10 P3 — Vision / audio model due diligence (04/11/2026)

**Status:** technical model screening only — NOT shipped, NOT certified donor/Golden. Capability owners: CAP-0046 ingredient recognition and CAP-0132 acoustic-event classification.

## Verified primary sources

1. [Google MediaPipe Image Classifier](https://developers.google.com/edge/mediapipe/solutions/vision/image_classifier): default EfficientNet-Lite0 (int8/float32) trained on **ImageNet 1,000 object categories**, including broad food objects. This is NOT complete ingredient, quantity or allergen recognition. Exact model distribution and commercial rights still require verification.
2. [Google MediaPipe Audio Classifier](https://developers.google.com/edge/mediapipe/solutions/audio/audio_classifier): float32 YAMNet AudioSet event classifier; 1 x 15600 input samples. Google reports average **12.29 ms CPU** on Pixel 6 for its referenced task benchmark. This is not a battery, wake-lock or cross-OEM guarantee, nor an Italian speech-to-text model.
3. [Google AI Edge LiteRT image classification sample](https://github.com/google-ai-edge/litert-samples/blob/main/samples/litert/image_classification/README.md): demonstrates runtime, CameraX and ImageNet classification, not a validated ingredient-domain model.
4. [Google Developers Blog, October 28, 2026](https://developers.googleblog.com/smaller-apps-and-faster-gpu-inference-with-litert-in-google-play-services/): reports apps **about 8 MB smaller in its tests** when LiteRT runtime is supplied by Google Play services instead of bundling it. Device support, installation/bootstrap, iOS compatibility and the separate model footprint must still be assessed. It does NOT establish a sub-1-MB trained model.

## Portfolio decision

- CAP-0046 P3: do NOT market an ImageNet object classifier as accurate ingredient detection. Prefer manually confirmed ingredients and validated OCR/EAN where approved; ingredient/allegy data must not be invented from photographs.
- CAP-0132 P3: YAMNet may be investigated only for a product-approved, user-initiated acoustic-event surface with microphone consent; no background covert sampling, mood inference or speech transcription claims.
- Core P1-P3 mathematical references ([PR #73](https://github.com/riccardopinato/App-Factory-Core/pull/73)) are NOT model checkpoints and do not ship a Vision/Audio runtime.
- No model weights downloaded/copied into any app. No new permissions or production app changes.

## E3/E4/E5 admission gates

- [ ] Exact model card/checkpoint SHA-256, clear commercial redistribution license, attribution, task labels and quantization; assess dependencies and source provider freshness.
- [ ] Italian/English food or sound-event labeled set with precision/recall, abstention and manual correction path.
- [ ] Peak RAM/CPU, p50/p95, battery/thermal and cold start on at least two Android OEM families and iOS target hardware; quantify runtime/ABI/APK/AAB impact vs baseline.
- [ ] Explicit camera/microphone UX and no unauthorized background capture or retention.
- [ ] Product Bible-approved consumer with user confirmation/undo; tested release artifact. Distinct Golden promotion review after independent integration.

No unsupported 90% search improvement, <1 MB model assertion, or zero energy impact.
