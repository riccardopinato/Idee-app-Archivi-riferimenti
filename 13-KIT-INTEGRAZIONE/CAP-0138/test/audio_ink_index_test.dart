import '../lib/audio_ink_index.dart';

void check(bool good, String name) {
  if (!good) throw StateError(name);
}
void rejects(void Function() call, String name) {
  try {
    call();
  } on ArgumentError {
    return;
  } on FormatException {
    return;
  } on StateError {
    return;
  }
  throw StateError('Did not reject: $name');
}
void main() {
  final i = AudioInkIndex();
  i.add('session-1', 'stroke-b', 4000);
  i.add('session-1', 'stroke-a', 1000);
  i.add('session-2', 'stroke-c', 1000);
  check(i.length == 3, 'size');
  check(i.stroke('session-1', 'stroke-a')?.elapsedMs == 1000, 'lookup');
  check(i.atOrBefore('session-1', 999) == null, 'before start');
  check(i.atOrBefore('session-1', 1000)?.strokeId == 'stroke-a', 'seek');
  check(i.atOrBefore('session-1', 9000)?.strokeId == 'stroke-b', 'latest');
  check(i.atOrBefore('session-2', 9000)?.strokeId == 'stroke-c', 'session');
  check(i.atOrBefore('session-3', 9000) == null, 'unknown session');
  rejects(() => i.add('session-1', 'stroke-a', 7), 'duplicate');
  rejects(() => i.add('session-1', 'bad', -1), 'time');
  final revived = AudioInkIndex.decode(i.encode());
  check(revived.length == 3, 'persist round-trip');
  check(revived.atOrBefore('session-1', 9000)?.strokeId == 'stroke-b', 'restored seek');
  rejects(() => AudioInkIndex.decode('{"schema":2,"anchors":[]}'), 'schema');
  rejects(() => AudioInkIndex.decode('{"schema":1,"anchors":[{}]}'), 'invalid data');
  check(revived.remove('session-1', 'stroke-a'), 'remove');
  check(!revived.remove('session-1', 'stroke-a'), 'repeat remove');
  print('CAP-0138 PASS');
}
