// Original Dart-only private task review projection.
// Does not read any Vault, shared-space, or encrypted-domain record.
class AnnaReviewTask {
  final String id;
  final DateTime date;
  final bool completed;
  final bool isTask;
  final bool privateOwned;
  const AnnaReviewTask(this.id, this.date, {
    required this.completed,
    required this.isTask,
    required this.privateOwned,
  });
}

class AnnaWeekReview {
  final DateTime start;
  final DateTime end;
  final List<String> overdueTaskIds;
  final List<String> pendingDatedThisWeekIds;
  final int completedDatedThisWeek;
  final int totalTasksDatedThisWeek;

  const AnnaWeekReview(this.start, this.end, this.overdueTaskIds,
      this.pendingDatedThisWeekIds, this.completedDatedThisWeek,
      this.totalTasksDatedThisWeek);
}

abstract final class AnnaWeeklyReview {
  static AnnaWeekReview fromPrivateTasks({
    required DateTime weekOf,
    required Iterable<AnnaReviewTask> entries,
    bool accountUnchanged = true,
    int maximumTasks = 10000,
  }) {
    if (maximumTasks < 1 || maximumTasks > 50000) {
      throw ArgumentError('Invalid task ceiling');
    }
    final week = DateTime(
      weekOf.year, weekOf.month, weekOf.day - (weekOf.weekday - DateTime.monday),
    );
    final end = DateTime(week.year, week.month, week.day + 7);
    if (!accountUnchanged) {
      return AnnaWeekReview(week, end, const [], const [], 0, 0);
    }
    final seen = <String>{};
    final overdue = <String>[];
    final pending = <String>[];
    var done = 0;
    var dated = 0;
    var included = 0;
    for (final task in entries) {
      if (!task.privateOwned || !task.isTask || task.id.isEmpty ||
          !seen.add(task.id)) continue;
      included++;
      if (included > maximumTasks) throw StateError('Too many tasks to review');
      final day = DateTime(task.date.year, task.date.month, task.date.day);
      if (day.isBefore(week) && !task.completed) {
        overdue.add(task.id);
      } else if (!day.isBefore(week) && day.isBefore(end)) {
        dated++;
        if (task.completed) {
          done++;
        } else {
          pending.add(task.id);
        }
      }
    }
    overdue.sort();
    pending.sort();
    return AnnaWeekReview(
      week, end, List.unmodifiable(overdue), List.unmodifiable(pending), done, dated,
    );
  }
}
