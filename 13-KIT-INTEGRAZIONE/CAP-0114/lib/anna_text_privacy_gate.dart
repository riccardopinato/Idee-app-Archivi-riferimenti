// Anna's Diary adapter around the narrow original PrivacyPreview parser.
// This produces a draft preview, not a complete safe export or PII guarantee.
import 'privacy_preview.dart';

enum AnnaTextOrigin {
  ordinaryPrivate,
  sharedSpace,
  privateVault,
  passwordVault,
  cycleTracker,
  unknown,
}

class AnnaMaskedDraft {
  final String text;
  final int maskedFields;
  final bool productionSafeRedaction = false;
  const AnnaMaskedDraft(this.text, this.maskedFields);
}

abstract final class AnnaTextPrivacyGate {
  static List<RedactionSpan> inspect({
    required String source,
    required AnnaTextOrigin origin,
    required bool containsBinaryMedia,
    required bool accountUnchanged,
  }) {
    _ensureAllowed(origin, containsBinaryMedia, accountUnchanged);
    return PrivacyPreview.detect(source);
  }

  static AnnaMaskedDraft createPreview({
    required String source,
    required AnnaTextOrigin origin,
    required bool containsBinaryMedia,
    required bool accountUnchanged,
    required List<RedactionSpan> selected,
  }) {
    _ensureAllowed(origin, containsBinaryMedia, accountUnchanged);
    if (selected.isEmpty) throw StateError('Explicit selection required');
    final copy = PrivacyPreview.mask(source, selected);
    return AnnaMaskedDraft(copy, selected.length);
  }

  static void _ensureAllowed(
      AnnaTextOrigin origin, bool containsBinaryMedia, bool accountUnchanged) {
    if (origin != AnnaTextOrigin.ordinaryPrivate ||
        containsBinaryMedia || !accountUnchanged) {
      throw StateError('Source not eligible for text-only preview');
    }
  }
}
