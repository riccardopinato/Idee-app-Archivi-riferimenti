# CAP-0138 — executable contract and missing verification

Dart test `test/audio_ink_index_test.dart` checks session separation, time ordering, nearest earlier stroke, no negative time or duplicate IDs, schema versioning, serialization round trip and removal. Run via [CI workflow](../../.github/workflows/kit-dart-compat.yml).

Still required: plug into real Notes drawing and recording callbacks, actual audio start/pause timestamps, persistence in existing backup/sync, denied permission, crash/restore, wave seek, accessibility and physical Android device. Standalone Dart test != Notes integration compatibility.
