# X10-022 — Manifest + staged restore contract

Pure Dart 0.1.0; crypto is used only for SHA-256 integrity, not
authenticity, confidentiality or encryption. No ZIP/tar/streaming and
no external file picker is implemented. The app must allowlist user-owned
fields and exclude OAuth/service tokens, ephemeral caches and derived data.

Accepts data.json, trash.json, and bounded media/<assetId>.bin entries.
Limits: max 128 entries, max 16 MiB each, max 32 MiB total.
The IO adapter must enforce size ceilings before full allocation.
Both stored entry hashes and byte lengths are checked before stage.

Restore is inspect -> safety snapshot -> private stage -> commit.
If stage/commit fails, rollback is attempted; if rollback fails,
the return value is recoveryRequired, never "data safe".

Integration requires a true atomic or rollback-safe domain database and
media storage adapter; unit tests use a fake transaction only. Backup
Golden is DRAFT/CANDIDATE and must not be promoted on these tests.
No consumer app integration/device crash/reboot test or export format
certification is implied. Run dart pub get && dart analyze && dart test.
