// Original Dart-only index that connects saved strokes to offsets in an
// existing recording. It does not record sound, handle consent or open files.
import 'dart:convert';

class StrokeTime {
  final String recordingId;
  final String strokeId;
  final int elapsedMs;
  const StrokeTime(this.recordingId, this.strokeId, this.elapsedMs);

  Map<String, Object> toJson() => {
    'recordingId': recordingId,
    'strokeId': strokeId,
    'elapsedMs': elapsedMs,
  };

  static StrokeTime fromJson(Map<String, dynamic> value) {
    final recording = value['recordingId'];
    final stroke = value['strokeId'];
    final offset = value['elapsedMs'];
    if (recording is! String || recording.isEmpty ||
        stroke is! String || stroke.isEmpty ||
        offset is! int || offset < 0 || offset > 86400000) {
      throw FormatException('Invalid anchor');
    }
    return StrokeTime(recording, stroke, offset);
  }
}

class AudioInkIndex {
  final Map<String, Map<String, StrokeTime>> _byRecording = {};

  int get length => _byRecording.values.fold(0, (n, m) => n + m.length);

  void add(String recording, String stroke, int timeMs) {
    if (recording.isEmpty || stroke.isEmpty ||
        timeMs < 0 || timeMs > 86400000) {
      throw ArgumentError('Invalid event');
    }
    final strokes = _byRecording.putIfAbsent(recording, () => {});
    if (strokes.containsKey(stroke)) throw StateError('Duplicate stroke');
    strokes[stroke] = StrokeTime(recording, stroke, timeMs);
  }

  StrokeTime? stroke(String recording, String id) => _byRecording[recording]?[id];

  StrokeTime? atOrBefore(String recording, int positionMs) {
    if (positionMs < 0) throw ArgumentError('Invalid playback time');
    final values = _byRecording[recording]?.values.toList() ?? [];
    values.sort((a, b) {
      final cmp = a.elapsedMs.compareTo(b.elapsedMs);
      return cmp != 0 ? cmp : a.strokeId.compareTo(b.strokeId);
    });
    StrokeTime? previous;
    for (final item in values) {
      if (item.elapsedMs > positionMs) break;
      previous = item;
    }
    return previous;
  }

  bool remove(String recording, String id) {
    final existed = _byRecording[recording]?.remove(id) != null;
    if (_byRecording[recording]?.isEmpty == true) _byRecording.remove(recording);
    return existed;
  }

  String encode() {
    final values = _byRecording.values.expand((m) => m.values).toList();
    values.sort((a, b) {
      final session = a.recordingId.compareTo(b.recordingId);
      if (session != 0) return session;
      final time = a.elapsedMs.compareTo(b.elapsedMs);
      return time != 0 ? time : a.strokeId.compareTo(b.strokeId);
    });
    return jsonEncode({'schema': 1, 'anchors': values.map((a) => a.toJson()).toList()});
  }

  static AudioInkIndex decode(String raw) {
    final json = jsonDecode(raw);
    if (json is! Map<String, dynamic> ||
        json['schema'] != 1 || json['anchors'] is! List) {
      throw FormatException('Unknown audio-ink schema');
    }
    final records = json['anchors'] as List;
    if (records.length > 100000) throw FormatException('Too many anchors');
    final index = AudioInkIndex();
    for (final record in records) {
      if (record is! Map<String, dynamic>) throw FormatException('Invalid record');
      final value = StrokeTime.fromJson(record);
      index.add(value.recordingId, value.strokeId, value.elapsedMs);
    }
    return index;
  }
}
