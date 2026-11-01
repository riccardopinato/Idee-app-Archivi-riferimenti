import '../lib/privacy_preview.dart';

void check(bool value, String name) {
  if (!value) throw StateError(name);
}
void rejects(void Function() action, String name) {
  try {
    action();
  } on ArgumentError {
    return;
  }
  throw StateError('Did not reject: $name');
}
void main() {
  const source = 'Contact a@example.com and IBAN GB29 NWBK 6016 1331 9268 19.';
  final spans = PrivacyPreview.detect(source);
  check(spans.length == 2, 'two entities');
  check(spans.first.kind == 'EMAIL', 'email');
  check(spans.last.kind == 'IBAN', 'iban');
  check(PrivacyPreview.validIban('GB29 NWBK 6016 1331 9268 19'), 'valid checksum');
  check(!PrivacyPreview.validIban('GB29 NWBK 6016 1331 9268 18'), 'invalid checksum');
  check(PrivacyPreview.detect('GB29 NWBK 6016 1331 9268 18').isEmpty, 'invalid skip');
  final one = PrivacyPreview.mask(source, [spans[0]]);
  check(one.contains('[EMAIL]'), 'email hidden');
  check(one.contains('GB29 NWBK'), 'iban not selected');
  check(source.contains('a@example.com'), 'source unchanged');
  final both = PrivacyPreview.mask(source, spans);
  check(!both.contains('a@example.com') && !both.contains('GB29 NWBK'), 'both hidden');
  rejects(() => PrivacyPreview.mask('different text', spans), 'stale');
  rejects(() => PrivacyPreview.mask(source, [spans.first, spans.first]), 'duplicate');
  rejects(() => PrivacyPreview.detect('x' * 1000001), 'limit');
  print('CAP-0114 PASS - partial PII categories only');
}
