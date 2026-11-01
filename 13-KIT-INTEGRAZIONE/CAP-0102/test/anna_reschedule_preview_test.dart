import '../lib/anna_reschedule_preview.dart';

void check(bool ok, String caseName) {
  if (!ok) throw StateError(caseName);
}

void rejects(void Function() call, String caseName) {
  try {
    call();
  } on ArgumentError {
    return;
  }
  throw StateError('Expected ArgumentError: $caseName');
}

void main() {
  final today = DateTime(2026, 11, 2, 9);
  final ten = DateTime(2026, 11, 2, 10);
  final windows = [
    AnnaFreeWindow(DateTime(2026, 11, 2, 8), DateTime(2026, 11, 2, 9, 30)),
    AnnaFreeWindow(ten, DateTime(2026, 11, 2, 11)),
    AnnaFreeWindow(DateTime(2026, 11, 2, 13), DateTime(2026, 11, 2, 14)),
    AnnaFreeWindow(ten, DateTime(2026, 11, 2, 11)),
  ];
  List<AnnaMoveProposal> run({
    bool private = true,
    bool done = false,
    bool recurring = false,
    bool fixed = false,
    bool coverage = true,
    bool account = true,
    DateTime? deadline,
    int minutes = 45,
    DateTime? previous,
  }) => AnnaReschedulePreview.suggest(
    taskId: 'private-task-1',
    requestedMinutes: minutes,
    now: today,
    freeWindows: windows,
    isPrivateTask: private,
    completed: done,
    recurring: recurring,
    fixedAppointment: fixed,
    calendarCoverageComplete: coverage,
    accountUnchanged: account,
    deadline: deadline,
    previousStart: previous,
  );

  check(run().length == 2, 'only two 45m windows');
  check(run().first.start == ten, 'sorted next slot');
  check(run()[1].start.hour == 13, 'second slot');
  check(run(deadline: DateTime(2026, 11, 2, 11)).length == 1, 'deadline');
  check(run(private: false).isEmpty, 'shared/private boundary');
  check(run(done: true).isEmpty, 'completed excluded');
  check(run(recurring: true).isEmpty, 'recurrence excluded');
  check(run(fixed: true).isEmpty, 'fixed excluded');
  check(run(coverage: false).isEmpty, 'partial coverage fail closed');
  check(run(account: false).isEmpty, 'account changed');
  check(run(minutes: 120).isEmpty, 'no fit');
  check(run(previous: ten).length == 1, 'original slot excluded');
  rejects(() => run(minutes: 0), 'zero duration');
  rejects(() => AnnaReschedulePreview.suggest(
      taskId: 'x', requestedMinutes: 20, now: today,
      freeWindows: [], isPrivateTask: true, completed: false,
      recurring: false, fixedAppointment: false,
      calendarCoverageComplete: true, accountUnchanged: true,
      maxSuggestions: 0), 'invalid limit');
  check(run().first.taskId == 'private-task-1', 'source identity');
  print('ANNA CAP-0102 PASS');
}
