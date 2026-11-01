import '../lib/anna_weekly_review.dart';

void check(bool value, String name) {
  if (!value) throw StateError(name);
}
void rejects(void Function() run, String name) {
  try {
    run();
  } on ArgumentError {
    return;
  } on StateError {
    return;
  }
  throw StateError('Expected error: $name');
}

void main() {
  final monday = DateTime(2026, 11, 2);
  final records = <AnnaReviewTask>[
    AnnaReviewTask('late', DateTime(2026, 10, 30),
        completed: false, isTask: true, privateOwned: true),
    AnnaReviewTask('pending', DateTime(2026, 11, 3),
        completed: false, isTask: true, privateOwned: true),
    AnnaReviewTask('done', DateTime(2026, 11, 5),
        completed: true, isTask: true, privateOwned: true),
    AnnaReviewTask('shared', DateTime(2026, 11, 4),
        completed: false, isTask: true, privateOwned: false),
    AnnaReviewTask('meeting', DateTime(2026, 11, 4),
        completed: false, isTask: false, privateOwned: true),
    AnnaReviewTask('future', DateTime(2026, 11, 9),
        completed: false, isTask: true, privateOwned: true),
    AnnaReviewTask('pending', DateTime(2026, 11, 3),
        completed: false, isTask: true, privateOwned: true),
  ];
  final review = AnnaWeeklyReview.fromPrivateTasks(
      weekOf: DateTime(2026, 11, 5), entries: records);
  check(review.start == monday, 'Monday window');
  check(review.end == DateTime(2026, 11, 9), 'exclusive next week');
  check(review.overdueTaskIds.length == 1, 'overdue private task');
  check(review.overdueTaskIds.first == 'late', 'overdue identity');
  check(review.pendingDatedThisWeekIds.length == 1, 'pending distinct');
  check(review.pendingDatedThisWeekIds.first == 'pending', 'pending identity');
  check(review.completedDatedThisWeek == 1, 'completed dated task');
  check(review.totalTasksDatedThisWeek == 2, 'weekly total');
  check(!review.pendingDatedThisWeekIds.contains('shared'), 'shared excluded');
  final none = AnnaWeeklyReview.fromPrivateTasks(
      weekOf: monday, entries: records, accountUnchanged: false);
  check(none.pendingDatedThisWeekIds.isEmpty, 'changed account fail closed');
  rejects(() => AnnaWeeklyReview.fromPrivateTasks(
      weekOf: monday, entries: records, maximumTasks: 1), 'limit');
  rejects(() => AnnaWeeklyReview.fromPrivateTasks(
      weekOf: monday, entries: [], maximumTasks: 0), 'invalid ceiling');
  check(records.length == 7, 'input untouched');
  print('ANNA CAP-0111 PASS');
}
