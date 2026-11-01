// Original narrow proof of concept, NOT a complete data redaction engine.
// Detects email and validated IBAN only; PDFs, metadata and OCR out of scope.
class RedactionSpan {
  final int start;
  final int end;
  final String kind;
  final String original;
  const RedactionSpan(this.start, this.end, this.kind, this.original);
}

class PrivacyPreview {
  static final email = RegExp(
    r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
    caseSensitive: false,
  );
  static final iban = RegExp(
    r'\b[A-Z]{2}\d{2}(?:[ ]?[A-Z0-9]){11,30}\b',
    caseSensitive: false,
  );

  static bool validIban(String input) {
    final text = input.replaceAll(' ', '').toUpperCase();
    if (text.length < 15 || text.length > 34 ||
        !RegExp(r'^[A-Z]{2}\d{2}[A-Z0-9]+$').hasMatch(text)) return false;
    final rotated = text.substring(4) + text.substring(0, 4);
    var rest = 0;
    for (final rune in rotated.codeUnits) {
      if (rune >= 48 && rune <= 57) {
        rest = (rest * 10 + rune - 48) % 97;
      } else if (rune >= 65 && rune <= 90) {
        rest = (rest * 100 + rune - 55) % 97;
      } else {
        return false;
      }
    }
    return rest == 1;
  }

  static List<RedactionSpan> detect(String text) {
    if (text.length > 1000000) throw ArgumentError('Input exceeds limit');
    final found = <RedactionSpan>[
      ...email.allMatches(text).map(
          (m) => RedactionSpan(m.start, m.end, 'EMAIL', m.group(0)!)),
      ...iban.allMatches(text).where((m) => validIban(m.group(0)!)).map(
          (m) => RedactionSpan(m.start, m.end, 'IBAN', m.group(0)!)),
    ]..sort((a, b) => a.start.compareTo(b.start));
    final result = <RedactionSpan>[];
    for (final item in found) {
      if (result.isEmpty || result.last.end <= item.start) result.add(item);
    }
    return List.unmodifiable(result);
  }

  // Caller explicitly selects which detected spans to hide. The output is
  // a new string; the original text and any source files are not modified.
  static String mask(String text, List<RedactionSpan> selected) {
    final detected = detect(text);
    for (final item in selected) {
      if (!detected.any((d) => d.start == item.start &&
          d.end == item.end && d.kind == item.kind &&
          d.original == item.original)) {
        throw ArgumentError('Stale or forged span');
      }
    }
    final ordered = [...selected]..sort((a, b) => b.start.compareTo(a.start));
    var boundary = text.length;
    var result = text;
    for (final item in ordered) {
      if (item.end > boundary) throw ArgumentError('Overlapping selection');
      result = result.replaceRange(item.start, item.end, '[' + item.kind + ']');
      boundary = item.start;
    }
    return result;
  }
}
