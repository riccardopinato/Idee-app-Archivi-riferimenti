# Audit trasversale capability — 1 novembre 2026

## Perimetro

- Factory Core baseline confermata al commit `632a66dce4aa00e8e1700b0a3e4dfc7ea008197c` (Master v27, Golden Index v23, registry v2).
- **31 repository** elencati dal connettore GitHub dell'account in questa sessione; **23 repository** con tree e roadmap/README pertinenti letti in modo mirato (non source-code audit integrale). Repository non letti in profondita NON equivalgono a prodotti assenti.
- Fonti interne: `01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md`, `06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md`, catalogo OSS, Design-App registry, Web Utility, Golden Core; allegati Project `Backlog idee app.txt`, `Idee che mi vengono in mente per le app.txt`, `Classifica idee app.txt`, `Anna's Diary.txt`, `Analisi stelle GitHub.txt`.
- Ricerca esterna precedente: Hugging Face / AI Valley, **idee candidate** con licenza/benchmark ancora da riconfermare prima della realizzazione.
- Principali roadmap lette: Agenda-per-Anna, Notes, Wonderlog, TrailPath, CamperBoss, World Days, Cooking Anime, TasteAI, Omni Cleaner, FocuSense, Phone Guard, Battery Guard, Send to PC, FrameLab, Design-App, AppLab e altri progetti utility.
- Copertura: audit documentale/matrice di opportunita; NON test Flutter/Android, review integrale del codice, Play, device fisico o licenze in tempo reale di ogni libreria.

## Duplicati importanti evitati

1. Anna shopping list, workout core, external calendar overlay, Life Threads, Collections, Year Review e Memories Map hanno evidenza documentale di implementazione esistente; le proposte nuove riguardano differenze di prodotto, UX o import foto/PDF, non rifacimenti.
2. Anna e Notes hanno lifecycle/cestino di base; occorrono test di cascata, backup, allegati, account e permessi, non nuove persistenze.
3. TasteAI possiede l'anti-waste engine; Cooking Anime e MealMate non devono diventare cloni prima di un caso d'uso differenziato.
4. PDF-Unifier e un donor interno per PDF Pocket Tools e Notes, non un progetto da ricostruire da zero.
5. Omni Cleaner dispone di un percorso EXIF/media cleanup; SafeShare/FrameLab/Wonderlog sono consumer candidati, non nuovi motori duplicati.
6. Phone Guard integra gia piu protezioni dai donor Tabletop/Pocket; gli stati fisici OEM restano separati.
7. Wonderlog ↔ Anna: ponte ecosystem con evidenza in roadmap; verificare revisioni e device QA prima di promuovere altri consumer.
8. Capability design di Design-App e Golden in App-Factory-Core hanno stati diversi; COPY_READY o SOURCE_REPORTED non certificano una nuova app automaticamente.

## Gap di verifica

- Ogni stato `SOURCE_REPORTED` richiede un gate source-level mirato per arrivare a `SOURCE_CONFIRMED`; non si promuove automaticamente.
- CashMate AI, BeerClass AI, SleepMax e altri prodotti storici hanno alcune fonti da Project/archivio e repository non individuati tra i 31 accessibili: mappatura `PROPOSTA` o storico, NON falso `non implementato`.
- Modelli locali (Whisper Tiny, Needle, embeddings) richiedono benchmark memoria, dimensioni APK e 5 lingue; i provider non commerciali richiedono termini compatibili col modello d'affari.
- Privacy: Anna/Notes/Travel NON condividono automaticamente storage/DB, account o vault; bridge COPY/LINK esplicito.

## Priorita operativa

- Prima: release/device/quality gates che bloccano promesse esistenti nelle app piu mature, a carico delle rispettive roadmap.
- Poi: miglioramenti a forte utilita e basso costo come parser evento, OCR con conferma, riuso PDF/EXIF, slot di agenda.
- Poi: motori multi-app riutilizzabili (visual connections, voice offline pack, geodata), con benchmark.
- Infine: funzionalita per nuove app consumer e web con provider e mercato da validare.

Catalogazione non equivale ad approvazione di implementazione. La fonte autorevole di una release resta sempre il repository della singola app.
