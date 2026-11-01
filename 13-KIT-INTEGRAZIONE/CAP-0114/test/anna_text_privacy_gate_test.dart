import '../lib/anna_text_privacy_gate.dart';

void check(bool good, String name) {
  if (!good) throw StateError(name);
}
void blocked(void Function() action, String name) {
  try {
    action();
  } on StateError {
    return;
  }
  throw StateError('Expected block: $name');
}

void main() {
  const input = 'Email: anna@example.com, altro testo privato.';
  final selected = AnnaTextPrivacyGate.inspect(
    source: input, origin: AnnaTextOrigin.ordinaryPrivate,
    containsBinaryMedia: false, accountUnchanged: true,
  );
  check(selected.length == 1, 'limited email inspection');
  final draft = AnnaTextPrivacyGate.createPreview(
    source: input, origin: AnnaTextOrigin.ordinaryPrivate,
    containsBinaryMedia: false, accountUnchanged: true, selected: selected,
  );
  check(draft.text.contains('[EMAIL]'), 'preview');
  check(!draft.text.contains('anna@example.com'), 'masked field');
  check(draft.maskedFields == 1, 'count');
  check(!draft.productionSafeRedaction, 'not production certified');
  check(input.contains('anna@example.com'), 'original unchanged');
  for (final origin in [
    AnnaTextOrigin.sharedSpace,
    AnnaTextOrigin.privateVault,
    AnnaTextOrigin.passwordVault,
    AnnaTextOrigin.cycleTracker,
    AnnaTextOrigin.unknown,
  ]) {
    blocked(() => AnnaTextPrivacyGate.inspect(
      source: input, origin: origin, containsBinaryMedia: false,
      accountUnchanged: true,
    ), 'privacy boundary');
  }
  blocked(() => AnnaTextPrivacyGate.inspect(
    source: input, origin: AnnaTextOrigin.ordinaryPrivate,
    containsBinaryMedia: true, accountUnchanged: true,
  ), 'binary media');
  blocked(() => AnnaTextPrivacyGate.inspect(
    source: input, origin: AnnaTextOrigin.ordinaryPrivate,
    containsBinaryMedia: false, accountUnchanged: false,
  ), 'account changed');
  blocked(() => AnnaTextPrivacyGate.createPreview(
    source: input, origin: AnnaTextOrigin.ordinaryPrivate,
    containsBinaryMedia: false, accountUnchanged: true, selected: const [],
  ), 'no selection');
  print('ANNA CAP-0114 PASS');
}
