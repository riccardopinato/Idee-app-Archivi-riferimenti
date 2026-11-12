# X10-022 — Backup/recovery: bounded manifest e staging Dart

**Factory baseline:** App-Factory-Core c5adc147046beb7024629466d10eeb799c3c2619, Master v27, Golden Index v29. Relevant Golden backup_recovery is DRAFT/CANDIDATE NON COPY-READY; import_export_portability remains candidate. The package below is a testable engineering core, **not** a new certified Golden or a production backup solution.

## Source
[factory_backup_kit](flutter_kits/backup/) 0.1.0: allowlisted data.json, trash.json and media/{assetId}.bin; SHA-256 receipt per entry, original byte length, app/package identity, schema version, creation UTC, bounded total and single-entry size. Zero new cloud accounts, no synchronization or automatic archive uploads. Restricts 128 entries, 16 MiB per entry and 32 MiB total *in memory*. Requires the IO adapter to bound incoming bytes **before** reading them completely; no compression, ZIP or stream implementation has been supplied here.

The recovery path is inspect -> safety snapshot -> private staging -> commit. Any checksum, unexpected path, missing media or wrong schema/app mismatch blocks restore *before* mutation; stage/commit failure calls rollback, and rollback failure returns RECOVERY_REQUIRED instead of a false success. Duplicate concurrent restore is denied. Original data is not deleted by a failed validation. Real consumer storage must implement transactional state changes and stage media safely, including crash consistency.

## Tests and independent gates
Pinned Dart 3.6.0 CI runs unit tests with fake transaction ports (tampered bytes, missing media, unsafe paths, case duplicates, oversized entries, future schema, failure of stage/commit/rollback/snapshot and duplicate restore). Using crypto ^3.0.3 for SHA-256 is integrity **only**, not a digital signature or encryption. A hostile editor could recompute the unkeyed hash; authenticity requires a separate trust/encryption scheme if product policy needs one.

**NOT VERIFIED**: actual native file picker/ZIP handling, multi-GB streaming archive, data/user-owned field filtering, real SQLite/Drift Room transaction recovery, media references, emulator/device failure mid-commit, app migrations, secure encryption, cloud backup, cross-app restoration, real consumer integrations. In particular, no consumer has tested no data loss after a process crash. Never represent these Dart unit tests as a physical restore certification.
