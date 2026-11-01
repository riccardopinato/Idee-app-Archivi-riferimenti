# CAP-0138 — Audio-Linked Ink, indice temporale deterministico

**Stato: CONTRACT_PROTOTYPE — Dart originale**, senza AI e senza acquisizione audio.

- [Dart source](lib/audio_ink_index.dart): mappa `recordingId + strokeId -> elapsedMs`, ricerca del tratto precedente, rimozione idempotente, serializzazione JSON versionata con limiti.
- [Test Dart](test/audio_ink_index_test.dart): sessioni isolate, posizioni temporali, chiavi duplicate, persist/recovery, input invalidi.
- Notes `3fd9b0d`: `flutter_app/lib/src/domain/visual_documents.dart` espone `InkStroke.id` e `BoardStroke` identificati, `whiteboard_screen.dart` scrive un documento visuale, `editor_screen.dart` usa `record: ^7.1.1`. **Nessun collegamento audio/whiteboard e stato inserito nell'app**.
- [MOSS Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) e un modello 0.9B Apache-2.0 per trascrizione e timestamp; *non serve* per collegare gli eventi al clock del registratore. Nessun download.

**Facilità aggiornata:** Notes 65%. Serve progettare persistenza dei collegamenti, UI e clock monotono dopo l'audit del prodotto.

[Specifiche](SPECIFICHE.md) · [Codice](CODICE_RIFERIMENTO.txt) · [Piano Flutter](INTEGRAZIONE_FLUTTER.md) · [Licenze](LICENZE_E_DIPENDENZE.md) · [Test](TEST_E_VALIDAZIONE.md)
