# CAP-0138 — contract extraction and invariants

Source app `riccardopinato/Notes-Ecosistema@3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c`: `InkStroke.id` is stable, `Note.id` identifies the owning entity, `editor_screen.dart` manages `AudioRecorder` via `record`. Existing whiteboard and sketch bodies are canonical; this feature must not replace them.

## Original candidate model

- `recordingId`: reference to an existing audio media asset/recording, no invented cross-app URI.
- `strokeId`: stable ID from existing `InkStroke`/whiteboard stroke; prohibit duplicates within one recording.
- `elapsedMs`: integer elapsed from **monotonic recording start**, 0...86,400,000 (24h ceiling in prototype), never wall-clock epoch.
- `AudioInkIndex.atOrBefore(recording, offsetMs)`: time-navigation reference; ties broken stably by stroke ID, no cross-session lookup.
- JSON `schema:1` with bounded anchor count; source note/canvas and audio are not modified.

## Missing product integration

Persist companion index as versioned sidecar linked to note/media and include in backup/restore, enforce deletion and access-scopes and clip duration, implement event callbacks in whiteboard + recorder and playback seek in UI. Do not claim full recording synchronization from the index alone.
