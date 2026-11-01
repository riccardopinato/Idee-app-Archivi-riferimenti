# CAP-0138 — Notes Flutter compatibility plan

1. Inspect `visual_documents.dart` `InkStroke.id` and `BoardStroke` ID, `whiteboard_screen.dart` drawing completion events and `editor_screen.dart` recorder lifecycle (source SHA `3fd9b0d`).
2. Expose an opt-in recording session with monotonic clock; on stroke committed, pass existing stroke ID + elapsed recording ms to `AudioInkIndex.add`. Ensure no recording without permission and UI indicator.
3. Persist versioned index sidecar with existing note/media asset references and backup/restore. Avoid mutating serialized whiteboard body without migration.
4. Handle deletions/undo, permissions, pause/resume, screen lock, app kill, sampling time drift, and per-session ownership correctly.
5. Playback seek only after known duration and source recording identity; no false timestamp equivalence to AI transcript segments.
6. Use separate widget/DB/Android physical QA for real integration. No native build or device execution has been done.
