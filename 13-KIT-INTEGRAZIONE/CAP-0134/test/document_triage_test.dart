import 'dart:typed_data';
import '../lib/document_triage.dart';

void check(bool condition, String name) {
  if (!condition) throw StateError(name);
}
void rejects(void Function() call, String name) {
  try {
    call();
  } on ArgumentError {
    return;
  }
  throw StateError('Did not reject: $name');
}
void main() {
  final pixels = Uint8List(256 * 256 * 3);
  var tensor = DocRexContract.normalizeCenterCrop(pixels);
  check(tensor.length == 3 * 224 * 224, 'shape');
  check((tensor[0] + 0.485 / 0.229).abs() < 0.0001, 'red normalize');
  check((tensor[224 * 224] + 0.456 / 0.224).abs() < 0.0001, 'green normalize');
  check((tensor[2 * 224 * 224] + 0.406 / 0.225).abs() < 0.0001, 'blue normalize');
  pixels[((16 * 256) + 16) * 3] = 255;
  tensor = DocRexContract.normalizeCenterCrop(pixels);
  check((tensor[0] - (1 - 0.485) / 0.229).abs() < 0.0001, 'crop origin');
  rejects(() => DocRexContract.normalizeCenterCrop(Uint8List(7)), 'size');
  final invoice = DocRexContract.evaluate([0, 8, -2]);
  check(invoice.label == 'invoice' && invoice.suggest, 'invoice');
  final other = DocRexContract.evaluate([-2, 0, 9]);
  check(other.label == 'other' && !other.suggest, 'no other route');
  check(!DocRexContract.evaluate([0, 0, 0]).suggest, 'uncertain');
  check(DocRexContract.evaluate([10000, 9999, -10000]).confidence.isFinite,
      'stable softmax');
  rejects(() => DocRexContract.evaluate([1]), 'logit length');
  rejects(() => DocRexContract.evaluate([1, double.nan, 3]), 'NaN');
  rejects(() => DocRexContract.evaluate([0, 2, 3], minMargin: -1), 'margin');
  print('CAP-0134 PASS');
}
