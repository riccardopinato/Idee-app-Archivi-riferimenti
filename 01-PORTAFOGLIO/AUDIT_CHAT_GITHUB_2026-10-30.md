# Audit ChatGPT ↔ GitHub — 30 ottobre 2026

Perimetro: **31 repo accessibili** e **37 prodotti** nel portafoglio. Ho controllato main/README per le app principali, sorgenti e manifest mirati, roadmap, PR aperte/merged e main check-run di Anna, World Days, TrailPath, Battery Guard, AppLab, Phone Guard, Notification Control, Omni Cleaner, TasteAI e Cooking Anime. Le chat sono ricostruite dalle informazioni conversazionali disponibili: non è garantita la copertura di ogni chat archiviata.

| Priorità | Progetto | Gap | Azione successiva (non eseguita) |
|---|---|---|---|
| P0 | TrailPath | v1.5 solo feature, non main; PR #27 aperta | riconciliare merge verso release e QA |
| P0 | Wonderlog vs Core | Bridge dichiarato Certified nel repo, Candidate nel Golden Registry | confrontare evidence fisiche e aggiornare autorità tramite PR |
| P1 | Anna | UI5 #154 open | gate/merge; non segnare UI5 live |
| P1 | AppLab | README v6.2 vs main v6.3B; #213 open | allineamento docs |
| P1 | Send-to-PC | chat 1.28 vs main 1.27.3 | individuare artifact/branch |
| P1 | Corpo Umano | README 0.18 vs pubspec 0.32 | aggiornare README |
| P1 | FrameLab | due repo, PR #15 in app-fotografia | scegliere canonical source |
| P1 | Cooking Anime | catalog/quality e store billing separati | completare F4B e prove Play |
| P2 | Cozy Days | solo README | recuperare sorgente o cambiare stato |
| P2 | prodotti solo-chat | repo non individuati per GrillBoss, CashMate, BeerClass, SleepMax, Easy Debloat | localizzare progetti/artifact senza inventare conclusioni |

## Commit campionati
- App Factory Core `e9507056601c4a6751510da4c5d1f61601a5dc25` (Master v27).
- AppLab `46816a1786820eb7c0edab7500ca950b10c7718c`.
- Anna `f9a3593a6629085a8ac58ccd81a958a4d3018e20`.
- TrailPath `3f44ab37c0881e4315033797c451cec723e23cd2`; feature PR #40 verso `feature/v1.1-v1.5`.
- World Days `622e5c2f00c08b0905207c6765c9b51e199e706f`.
- Notes `3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c`.
- Battery `d8cf237ab2df2daf427b87ca057871e3143bccc7`.
- Notification `664cf8c7eaaa8843711ddc99b62b547a1997fcb9`.
- Phone Guard `ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c`.
- Omni Cleaner `a753baa8ad0b647be747050ac7e2f6d1fde85465`.
- TasteAI `99e93784db403c9da65c8753c6bbcc802d01180e`.
- Cooking Anime `7225d9e9a58bc1b5a01a54e2b20af9503e1731e2`.
- FocuSense `bdc8becfff1b1a5f629456deb34170f0d905d8b7`.

**Limiti:** nessuna nuova build/test fisico/Play, niente audit di sicurezza profondo su ogni repository. Mancanza del repo non equivale a progetto non sviluppato. I punteggi non sono performance di mercato misurate.
