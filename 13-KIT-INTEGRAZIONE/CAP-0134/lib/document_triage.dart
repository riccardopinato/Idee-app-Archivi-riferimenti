// Original Dart adapter, not a neural network or file manager.
// Assumes RGB pixels resized to 256x256 externally; keeps originals unchanged.
import 'dart:math' as math;
import 'dart:typed_data';

class TriageDecision {
  final String label;
  final double confidence;
  final double margin;
  final bool suggest;
  const TriageDecision(this.label, this.confidence, this.margin, this.suggest);
}

class DocRexContract {
  static const labels = ['bank_statement', 'invoice', 'other'];
  static const artifactSha256 =
      'bbe9997671953145206939291c592dc937c6c523202234bba66e8a589cc643db';

  // DocRex card: RGB 256x256 -> centered 224x224 -> float32 NCHW
  // normalized with standard ImageNet mean/std.
  static Float32List normalizeCenterCrop(Uint8List rgb) {
    if (rgb.length != 256 * 256 * 3) {
      throw ArgumentError('Requires 256x256 RGB bytes');
    }
    const means = [0.485, 0.456, 0.406];
    const deviations = [0.229, 0.224, 0.225];
    final result = Float32List(3 * 224 * 224);
    for (var c = 0; c < 3; c++) {
      for (var y = 0; y < 224; y++) {
        for (var x = 0; x < 224; x++) {
          final source = ((y + 16) * 256 + x + 16) * 3 + c;
          result[c * 224 * 224 + y * 224 + x] =
              (rgb[source] / 255.0 - means[c]) / deviations[c];
        }
      }
    }
    return result;
  }

  // The caller must run the pinned ONNX FP32 model separately and supply
  // its three logits. This function only proposes a label, never moves files.
  static TriageDecision evaluate(
    List<double> logits, {
    double minConfidence = 0.85,
    double minMargin = 0.10,
  }) {
    if (logits.length != 3 || logits.any((x) => !x.isFinite)) {
      throw ArgumentError('Three finite logits required');
    }
    if (!minConfidence.isFinite || minConfidence < 0 ||
        minConfidence > 1 || !minMargin.isFinite || minMargin < 0 ||
        minMargin > 1) {
      throw ArgumentError('Invalid confidence thresholds');
    }
    final maxLogit = logits.reduce(math.max);
    final weights = logits.map((x) => math.exp(x - maxLogit)).toList();
    final total = weights.reduce((a, b) => a + b);
    final probabilities = weights.map((x) => x / total).toList();
    var best = 0;
    for (var i = 1; i < 3; i++) {
      if (probabilities[i] > probabilities[best]) best = i;
    }
    final other = probabilities.asMap().entries
        .where((e) => e.key != best)
        .map((e) => e.value).reduce(math.max);
    final conf = probabilities[best];
    final margin = conf - other;
    return TriageDecision(labels[best], conf, margin,
        labels[best] != 'other' && conf >= minConfidence && margin >= minMargin);
  }
}
