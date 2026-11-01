# CAP-0114 — compatibility plan for Notes/Anna/PDF

Notes at `3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c` stores notes/media via `lib/src/domain/attachments.dart` and PDF annotations in `lib/src/domain/documents.dart`. Reuse these, keeping original data immutable; only preview a new text export after explicit selection. No automatic share.

To achieve production privacy: verify all required PII types and PDF raster/text/metadata, add robust and reversible-prevention tests, fail closed when unsupported, consider vetted SDK only after explicit commercial license clearance and native Android/iOS smoke. Do NOT reuse demo code with ambiguous licensing. Flutter package integration not attempted.
