# Mapping capability — Anna's Diary / NotebookLM 02/11/2026

**Stato: ricerca, non nuovo CAP canonico né autorizzazione alla roadmap.** Riferimento: [15 proposte classificate](../11-NUOVE-IDEE/ANNA_NOTEBOOKLM_2026-11-02.md). Le 140 CAP nel registro JSON non sono state cambiate; il testo NotebookLM impiegava otto codici con descrizioni diverse da quelle dell'archivio corrente.

| CAP nel documento NotebookLM | Cosa indica davvero nel catalogo |
|---|---|
| CAP-0041 (E2EE Noi ♡) | Palette da foto e golden hour |
| CAP-0052 (Lockscreen Widgets) | Meteo contestuale finestre outdoor |
| CAP-0038 (Time-Lock Storage) | PDF Pocket Tools packaging |
| CAP-0012 (QR Generator) | Year in Review deterministico |
| CAP-0015 (Stats & Charts Engine) | Ricerca globale ordinabile |
| CAP-0042 (Private Vault cifrato) | Catalogo editoriale multilingua offline |
| CAP-0022 (Unified Capture) | Localizzazione almeno cinque lingue |
| CAP-0063 (Interactive Notifications) | Momenti ideali per focus in calendario |

## Mappa di riuso vera, senza doppioni

| Idee AD-NL26 | Riuso CAP esistenti, parziale | Nuova responsabilità da validare |
|---|---|---|
| 01, 02 | CAP-0021 QR inviti; CAP-0042 editoriale (solo catalogo domande) | State machine due risposte e capsule sync |
| 03 | CAP-0012 recap; CAP-0055 reminder | Lettera futura/time-lock |
| 04 | CAP-0021 inviti; CAP-0037 PDF; CAP-0039 EXIF safe copy | Condivisione revocabile di ricordi |
| 05, 06, 11 | CAP-0014 capture; CAP-0055 notifiche | Widget privacy-safe e media opt-in |
| 12 | CAP-0055 reliability; CAP-0077 permission diagnostics | Action callbacks native idempotenti |
| 07 | CAP-0101 dashboard task; CAP-0106 heatmap riunioni (solo pattern) | Mood/activity descrittivi, statistiche senza causalità |
| 09 | CAP-0035 OCR; CAP-0037 PDF (solo pattern) | Allegati cifrati Vault, audit security |
| 13–16 | CAP-0023 design token; CAP-0024 motion; CAP-0069 visual QA | Riusare UI5, evitare doppia Home/tema |
| 17 | CAP-0072 RevenueCat entitlement | Prezzi/business test non sono una CAP runtime nuova |

**Metodo per futuro ingresso nei 140 CAP:** una proposta approvata deve prima essere confrontata con codice Anna main e Product Bible; assegnare ID monotono soltanto se responsabilità distinta e non coperta, aggiornare REGISTRO_CAPABILITY.json, rigenerare viste e kit con scripts/build_catalog.py --check in PR. Un CAP CI_VERIFIED esistente NON prova una nuova feature. Privacy #215 è ancora ON HOLD.
