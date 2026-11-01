// Original Dart-only proposal engine for Anna's Diary; no persistent writes.
// The host passes only explicitly permitted visible calendar free intervals.
class AnnaFreeWindow {
  final DateTime start;
  final DateTime end;
  const AnnaFreeWindow(this.start, this.end);
}

class AnnaMoveProposal {
  final String taskId;
  final DateTime start;
  final DateTime end;
  const AnnaMoveProposal(this.taskId, this.start, this.end);
}

abstract final class AnnaReschedulePreview {
  static List<AnnaMoveProposal> suggest({
    required String taskId,
    required int requestedMinutes,
    required DateTime now,
    required Iterable<AnnaFreeWindow> freeWindows,
    required bool isPrivateTask,
    required bool completed,
    required bool recurring,
    required bool fixedAppointment,
    required bool calendarCoverageComplete,
    required bool accountUnchanged,
    DateTime? deadline,
    DateTime? previousStart,
    int maxSuggestions = 3,
  }) {
    if (taskId.trim().isEmpty || requestedMinutes < 1 ||
        requestedMinutes > 720 || maxSuggestions < 1 ||
        maxSuggestions > 10) {
      throw ArgumentError('Invalid task or scheduling parameters');
    }
    if (!isPrivateTask || completed || recurring || fixedAppointment ||
        !calendarCoverageComplete || !accountUnchanged ||
        (deadline != null && !deadline.isAfter(now))) {
      return const [];
    }
    final candidates = <AnnaMoveProposal>[];
    for (final window in freeWindows) {
      if (!window.end.isAfter(window.start)) continue;
      final start = window.start.isAfter(now) ? window.start : now;
      final end = start.add(Duration(minutes: requestedMinutes));
      if (end.isAfter(window.end) ||
          (deadline != null && end.isAfter(deadline)) ||
          (previousStart != null && start.isAtSameMomentAs(previousStart))) {
        continue;
      }
      candidates.add(AnnaMoveProposal(taskId, start, end));
    }
    candidates.sort((a, b) {
      final start = a.start.compareTo(b.start);
      return start != 0 ? start : a.end.compareTo(b.end);
    });
    final result = <AnnaMoveProposal>[];
    for (final option in candidates) {
      if (result.any((existing) => existing.start.isAtSameMomentAs(option.start))) {
        continue;
      }
      result.add(option);
      if (result.length >= maxSuggestions) break;
    }
    return List.unmodifiable(result);
  }
}
