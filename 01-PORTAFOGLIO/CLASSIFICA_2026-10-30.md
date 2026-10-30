# Classifica portafoglio — audit degli accorpamenti verificati su GitHub (30/10/2026)

> **Aggiornamento della classifica precedente, senza cancellarla dallo storico.** Score /100 = valutazione strategica **stimata**, non previsione di ricavi o certificazione tecnica. I punteggi dei prodotti con nuova evidenza sono stati ricalibrati secondo maturità reale e possibilità di commercializzazione; gli altri conservano i valori storici. Le informazioni sono perimetro **main** dei repository indicati, verificato il 30/10/2026; niente test fisici o Play eseguiti durante questo audit.

**Legenda evidenze:** 🟢 repository/sorgenti **ispezionati in questa verifica**; 🔵 repository individuato nell'account ma **non sottoposto ad audit puntuale ora**; 🟡 solo evidenza storica o donor parziale, **non** prova di suite corrente; 🔴 concept o nessun repository prodotto corrispondente individuato. Il colore non attesta store readiness.

## Classifica aggiornata — 33 prodotti / progetti

| # | App / progetto | Score /100 | Evidenza | Commercializzazione / stato |
|---:|---|---:|:---:|---|
|1|Anna's Diary|93|🔵|Standalone o progetto autonomo|
|2|World Days|92|🔵|Contenuti/ads|
|3|Send to PC|91|🔵|Standalone o progetto autonomo|
|4|Notes-Ecosistema|90|🔵|Standalone o progetto autonomo|
|5|Battery Guard|89|🔵|Standalone o progetto autonomo|
|6|Notification Control|89|🟢|Suite in codice|
|7|Android Omni Cleaner|89|🟢|Prodotto composito in codice|
|8|Phone Guard|88|🟢|Suite in codice|
|9|AppLab|88|🔵|Infrastruttura/B2B|
|10|TrailPath|87|🔵|Standalone o progetto autonomo|
|11|CleanOS / Easy Debloat|86|🟡|Fusione da completare|
|12|GrillBoss|85|🟡|Standalone o progetto autonomo|
|13|TasteAI|85|🟢|Prodotto multifunzione in codice|
|14|Wonderlog|84|🔵|Standalone o progetto autonomo|
|15|BeerClass AI|83|🟡|Standalone o progetto autonomo|
|16|Cooking Anime|82|🔵|Contenuti/ads|
|17|PDF-Unifier → PDF Pocket Tools|82|🟢|Donor PDF in codice; suite proposta|
|18|Human Zoom|81|🔵|Standalone o progetto autonomo|
|19|FrameLab|79|🔵|Standalone o progetto autonomo|
|20|Snack Empire Tycoon|79|🟡|Standalone o progetto autonomo|
|21|CashMate AI|79|🟡|Standalone o progetto autonomo|
|22|App Profiles|78|🟡|Fusione da completare|
|23|EdgeDock / SideHub|78|🔴|Standalone o progetto autonomo|
|24|SafeShare|78|🟡|Fusione da completare|
|25|Purchase Guard|77|🔴|Fusione da completare|
|26|SleepMax|75|🟡|Standalone o progetto autonomo|
|27|FocusSense|74|🔵|Standalone o progetto autonomo|
|28|CamperBoss|73|🔵|Standalone o progetto autonomo|
|29|Downloads Butler|73|🟡|Fusione da completare|
|30|180FlipCharge / Rotate 180°|72|🔵|Standalone o progetto autonomo|
|31|CmdPocket|72|🔴|Standalone o progetto autonomo|
|32|Cozy Days|72|🔵|Standalone o progetto autonomo|
|33|Neon Arcade Runner|71|🔵|Standalone o progetto autonomo|

## Descrizione di ogni app e progetto accorpato

1. **Anna's Diary** — Agenda, diario e timeline privata con Today, Calendar, Ricordi e Capture. Prodotto autonomo, collegabile a Notes/Wonderlog/TrailPath senza fusioni.
2. **World Days** — Calendario visuale di giornate e settimane mondiali, quiz, curiosità, share cards e ritorno quotidiano. Non è una suite; modello contenuti + AdMob.
3. **Send to PC** — Invio locale di file telefono↔PC tramite rete e browser/QR. Utility standalone, da distinguere dai moduli Downloads.
4. **Notes-Ecosistema** — Workspace di note, canvas, ricerca e contenuti locali. Autonomo, con bridge espliciti verso Anna e altri prodotti.
5. **Battery Guard** — Controllo indicatori, sessioni e avvisi batteria. App standalone; non incorporarla in CleanOS o Omni Cleaner.
6. **Notification Control** — **Accorpamento REALIZZATO:** Notification Undo + Pausa Ping + Follow Up Reminder + Critical Alert + Pickup Code Pin + Luminous Visual Alerts, tutti sul medesimo Notification Listener e Vault. Rules Engine, backup e premium; Play Internal/live da validare. Repo `riccardopinato/Notification-Control` @ `664cf8c7eaaa8843711ddc99b62b547a1997fcb9`.
7. **Android Omni Cleaner** — **Prodotto composito REALIZZATO:** pulizia file grandi e duplicati + galleria/undo + cache/thumbnail + residui app + download vecchi + EXIF privacy + Safe Trash. **Non** include il debloat di CleanOS. Kotlin RC1, test e performance su Xiaomi; release Play/provider ancora aperta. Repo @ `a753baa8ad0b647be747050ac7e2f6d1fde85465`.
8. **Phone Guard** — **Accorpamento REALIZZATO:** Tabletop Motion Alarm + Pocket Guard/Pockara; evoluto in sei modalità Table, Pocket, Bag, Charging, Accessory e Journey. Smart Arm, Auto Guard e allarmi condividono un servizio. v0.9.7; QA fisica multi-OEM/Play ancora richiesta. Repo @ `ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c`.
9. **AppLab** — Piattaforma interna di QA, certificazione, ottimizzazione e assistenza allo sviluppo. Linea v6.3; eventuale B2B distinto dalle app consumer.
10. **TrailPath** — App outdoor per sentieri, percorsi, mappe e routing. Autonoma da Wonderlog/Anna; possibile riuso motori POI/route.
11. **CleanOS / Easy Debloat** — **Accorpamento PROPOSTO, non ancora suite verificata su GitHub:** Easy Debloat (donor storico Shizuku) + OEM Ad Shield + App Control/Freeze + eventuale Wireless ADB integrato. È controllo delle app di sistema, non pulizia file.
12. **GrillBoss** — Assistente BBQ per tagli, quantità, cottura e timer. Possibile riuso di catalogo ricette, ma non fusione con TasteAI/Cooking Anime.
13. **TasteAI** — **Prodotto multi-funzione già IN CODICE:** catalogo di 111 ricette offline, ricerca intelligente senza cloud AI, 'Ispirami', preferiti e Anti-Waste Engine; profilo e Plus. Condivide idee con MealMate, **senza fusione formalmente documentata**. Repo @ `99e93784db403c9da65c8753c6bbcc802d01180e` (v0.13).
14. **Wonderlog** — Diario e pianificazione viaggi con luoghi, media e collegamenti espliciti ad Anna/TrailPath. Non fonderlo nella stessa app.
15. **BeerClass AI** — Diario birre, gusti, valutazioni e scansione barcode; app di nicchia indipendente.
16. **Cooking Anime** — Ricette ispirate agli anime, ricerca per opere e catalogo editoriale. Possibile riuso cataloghi/timer, non fusione con TasteAI.
17. **PDF-Unifier → PDF Pocket Tools** — **Motore già REALIZZATO:** merge PDF, immagini→PDF, split, protezione password, rotazione, lettore, ricerca, segnalibri, compressione, OCR ed export testo. `PDF Pocket Tools` resta **evoluzione commerciale proposta**, non suite già completata. Repo `riccardopinato/PDF-Unifier` @ `3aacb3e2ac4822db4601fe5c217c016cecc6cbf4`.
18. **Human Zoom** — Atlante di anatomia e quiz. Educativa standalone; roadmap di contenuto/ottimizzazione separata.
19. **FrameLab** — Utility e cataloghi creativi per fotografi; possibili funzioni golden hour/palette e contenuti multilingua.
20. **Snack Empire Tycoon** — Idle/tycoon game con progressione e monetizzazione F2P; sviluppato in lane giochi indipendente.
21. **CashMate AI** — Gestione delle finanze personali, budget e obiettivi; privacy e abbonamenti/Plus come modelli distinti.
22. **App Profiles** — **Accorpamento PROPOSTO:** Brightness Profiles + Rotation Profiles + Screen Awake + Bluetooth Volume Memory + DisplayPilot/SoundPilot, con 180FlipCharge come donor reale. Suite non ancora assemblata.
23. **EdgeDock / SideHub** — Barra laterale Android con scorciatoie e comandi; candidato da donor Smart Edge, non progetto prodotto verificato.
24. **SafeShare** — **Accorpamento PROPOSTO:** Clean Link + Photo EXIF/GPS Cleaner + File/PDF Metadata Cleaner + ShareSafe. **Esiste un donor EXIF in Android Omni Cleaner**, non una suite SafeShare verificata.
25. **Purchase Guard** — **Accorpamento PROPOSTO:** Subscription Guard + Receipt/Warranty Guard + Trial Reminder + Return Reminder; gestione dell'acquisto dopo il pagamento. Nessun repo suite trovato.
26. **SleepMax** — Coach routine e qualità percepita del sonno con reminder e statistiche; non necessariamente parte di FocusSense.
27. **FocusSense** — Misura condizioni di rumore, luce e movimento per Focus Score e abitudini; riuso sensori possibile, senza fusione obbligatoria.
28. **CamperBoss** — Strumenti per camper, soste, viaggio, POI/offline content e pianificazione. Prodotto autonomo, provider geografici condivisibili.
29. **Downloads Butler** — **Accorpamento PROPOSTO con donor parziale:** Download Organizer + Downloads Cleaner + TempBox. Android Omni Cleaner implementa discovery/pulizia guidata di download vecchi, ma non prova una suite Butler né l'organizer completo.
30. **180FlipCharge / Rotate 180°** — Rotazione verticale invertita con attivazione manuale, ricarica, Quick Tile e per-app exceptions. Standalone e motore riusabile in App Profiles.
31. **CmdPocket** — Manuale offline rapido per comandi terminale ispirato a tldr-pages; progetto candidato e attribuzione dataset da verificare.
32. **Cozy Days** — Gioco cozy con progressione; separato dalle utility.
33. **Neon Arcade Runner** — Gioco arcade leggero con monetizzazione giochi; separato dalle utility.

## Decisioni dell'audit: non confondere i prodotti

- **Notification Control** e **Phone Guard**: le righe storiche le descrivevano come suite da assemblare, ma i rispettivi repository dimostrano **fusioni già eseguite in codice**. La pubblicazione resta separata dalla conferma software.
- **Android Omni Cleaner vs CleanOS**: il primo pulisce **file e media**, con funzioni EXIF e download; il secondo è un progetto diverso basato su **debloat e controllo app OEM**. Non trattarli come alias.
- **TasteAI vs MealMate**: TasteAI ha già ricerca ricette, ispirazione e anti-spreco, ma non risulta una delibera di fusione canonica con il concept MealMate. Valutare riuso e sovrapposizioni prima di creare due esperienze identiche.
- **PDF-Unifier vs PDF Pocket Tools**: PDF-Unifier ha già motori Kotlin in codice, quindi PDF Pocket Tools **non parte da zero**. Restano aperte scelte di naming, architettura, QA e packaging; non segnare la suite proposta come già pronta.
- **SafeShare/Downloads Butler**: alcune capability hanno donor in Omni Cleaner; questo **non** significa che le due suite separate siano state sviluppate.
- **App Profiles**: 180FlipCharge esiste come prodotto autonomo e possibile donor, ma gli altri profili e la suite non risultano integrati nel repository corrispondente.

## Repository verificati nell'audit

| Progetto | Repository | Commit main verificato | Prova di sviluppo |
|---|---|---|---|
| Notification Control | https://github.com/riccardopinato/Notification-Control | `664cf8c7eaaa8843711ddc99b62b547a1997fcb9` | README, Product Bible, service capture/Vault, schedulers, Luminous, billing |
| Phone Guard | https://github.com/riccardopinato/Phone-Guard | `ba377aa0fadbe2d7e5ec603f5abd4b69d411ed3c` | README, DONOR_PROVENANCE, roadmap, detector e servizio comuni |
| Android Omni Cleaner | https://github.com/riccardopinato/Android-Omni-Cleaner | `a753baa8ad0b647be747050ac7e2f6d1fde85465` | README, Product Bible, parity matrix, cleaner/EXIF/SQL index |
| TasteAI | https://github.com/riccardopinato/TasteAI | `99e93784db403c9da65c8753c6bbcc802d01180e` | README, roadmap, search/recipe/antiwaste Dart |
| PDF-Unifier | https://github.com/riccardopinato/PDF-Unifier | `3aacb3e2ac4822db4601fe5c217c016cecc6cbf4` | `PdfEngine.kt`, OCR, reader, compression, bookmarks |
