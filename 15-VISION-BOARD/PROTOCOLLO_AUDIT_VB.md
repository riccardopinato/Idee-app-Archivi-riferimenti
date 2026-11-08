# Protocollo di audit Vision Board — v1

## 0. Vincolo e gerarchia
Task tipico: l'utente invia uno o più repository relativi a Vision Board / moodboard / goal visualization. Aggiornare **soltanto** il repository Idee, se non è espressamente richiesta una implementazione nelle singole app. Rispettare l'ordine: Factory CURRENT > Master > Golden Index/Registry > Golden pertinenti > AGENTS di questo repo > presente protocollo. Risolvere Factory una sola volta per sessione e fissare SHA. Nessun lavoro cloud, download, copia o modifica app implicita.

## 1. Identità e verifica E0–E5
- **E0 / URL:** input ricevuto; nessuna asserzione su codice o licenza.
- **E1 / fonte fissata:** `owner/repo`, upstream, branch, SHA 40 char, LICENSE/README e file pertinenti verificati; descrivere copertura esatta.
- **E2 / architettura:** componenti, API, modelli dati, dipendenze, test/CI, edge cases e compatibilità target ispezionati; un test *presente nel repo* non è un test *eseguito*.
- **E3 / donor verificato nel proprio scope:** adattamento/esecuzione e test esatti documentati secondo Factory; non promuovere da un'analisi documentale.
- **E5 / riuso indipendente:** consumer aggiuntivo e prove richieste per la classe Golden. Device/Play/Web production sono gate separati.
- Per repo variati rispetto all'ultimo SHA: audit del delta e confronto file/commit; preservare le evidenze storiche.

## 2. Lettura tecnica mirata
Verificare, quando pertinenti:
- **Board model:** ID stabili, ordine/layer, frame/group, coordinate world/screen, layout libero/griglia, relazioni e tipi di oggetto.
- **Interazione:** drag/resize/rotate, pan/zoom/pinch, touch/stylus, hit testing, snapping, keyboard, selezione multipla, lasso, undo/redo, collisioni e motion.
- **Contenuti:** immagini, testo, post-it, sticker, colori, palette, link e media; storage canonico, dedup, reference counting, permessi e originali preservati.
- **Vision-specific:** goal cards, intenzioni, milestone, progress, timeline, rituali/promemoria, set tematici, template, wallpaper/collage, review annuale — separare feature reale da mockup.
- **Persistenza:** offline-first, salvataggio automatico, recoverability, import/export PNG/PDF/editabile, formato versione, migrazione, backup, sincronizzazione e conflitti.
- **Qualità:** tests, gestione corruzioni, immagini mancanti, grandi board, RAM, FPS, APK/bundle size, accessibilità, font scale, dark mode, localizzazione e Web/PWA.
- **Sicurezza e privacy:** immagini personali, metadati EXIF, contenuti intimi, share/permessi, revoca, accesso a media, eventuali endpoint AI e trasmissioni reali.
- **Licenze separate:** codice, package, foto di esempio, illustrazioni, template, font, icone e dataset. Repository pubblico **non** equivale a codice riusabile commercialmente. Niente copia di asset proprietari.

## 3. Estrazione a livello componente
Per ogni elemento estratto registrare:
`source_sha + source_path + original_contract + target_contract + candidate_kind + license_scope + existing_CAP + relevant_Golden + consumer + adaptation_delta + tests_required + evidence + next_gate`.

Classi:
- `CODE_DONOR_CANDIDATE`: porzione di codice potenzialmente adattabile, solo previo license gate.
- `PATTERN_DONOR`: algoritmo/interazione/document design; implementazione autonoma.
- `UX_REFERENCE`: gerarchia visuale o flusso, senza copiare branding o asset.
- `GOLDEN_CANDIDATE`: contratto **trasversale** non già coperto da Golden validi; soltanto proposta.
- `CAPABILITY_MATCH`: collega a `CAP-NNNN` esistente, con delta dichiarato.
- `NEW_CAP_PROPOSAL`: responsabilità prodotto realmente nuova, **senza assegnare ID ufficiale** finché non passa dal registro CAP canonico + kit + build catalog + CI.
- `APP_IDEA`: eventuale standalone da registrare in `11-NUOVE-IDEE`, non automaticamente in roadmap.
- `REJECTED`: incompatibilità, duplicazione, licenza o costo sproporzionato.

Scegliere `PRESERVE / IMPORT / REBUILD / DROP` rispetto ai donor alternativi, senza accumulare editor, controller o storage paralleli.

## 4. Crosswalk obbligatorio
1. Cercare contratto equivalente fra **199 CAP** attualmente presenti nel registro live (numero snapshot al 08/11, non costante).
2. Verificare per ogni app `app_states` e codice alla SHA reale, distinguendo `DA_VALUTARE`, `DA_VERIFICARE` e implementato.
3. Riusare Golden Infinite Canvas/Ink dove compatibile. Non certificare widget/gesture/consumer per la sola presenza del core Dart.
4. Creare nuove CAP solo attraverso il normale workflow del catalogo, mai come effetto automatico del link.
5. Non inserire nelle roadmap Anna/Notes senza verifica Product Bible, benefici e approvazione.

## 5. Matrice d'ammissione per app
- **Notes:** Goal/Project Vision Board come vista/estensione del Visual Workspace già posseduto; link a note, task e progetti, niente copia di documenti o sistemi di sincronizzazione paralleli.
- **Anna's Diary:** Dreams/Life Board leggera, visiva e privata, con eventuali collegamenti *espliciti* a ricordi, persone, eventi e piani. Le immagini non diventano automaticamente ricordi, le board non devono apparire a membri di Noi ♡ per default.
- **Altre:** valutare solo un caso di prodotto concreto e un consumer canonico; niente diffusione a tutte le app indiscriminatamente.

Per ogni consumer valutare `valore`, `riuso`, `facilità`, `maturità prova`, `rischi` e `footprint`. Gli score sono **euristici**; non sono risultati di test. Specificare i costi API/servizi (default nessuno), implicazioni licenze e install size.

## 6. Test candidati, non presunti
Smoke test di board vuota/piena; centro viewport; 2x zoom + drag; input penna vs pinch; selezione ed editing di oggetti; undo/redo; salvataggio/riapertura; import/export e roundtrip; file corrotti; migrazione formato; media mancanti; duplicazione ID; offline e account switch; privacy su share/collaborazione; permission revoke; accessibility/reduced motion; stress su dispositivi reali. `flutter analyze`, tests, CI exact-head e AppLab solo quando si passa a integrazione autorizzata.

## 7. Output e registri
Ogni batch con URL reali deve produrre (nella stessa PR):
1. Inbox `VBR-NNNN` unica e deduplicata;
2. scheda individuale con URL/SHA/file/license/evidence;
3. JSON `REGISTRO_FONTI_VB.json` aggiornato in append/merge coerente;
4. vista `ESTRAZIONI_CANDIDATE.md` e crosswalk CAP/Golden;
5. eventuale integrazione con 11-NUOVE-IDEE o catalogo canonico **solo se autorizzata** e rispettando i relativi gate;
6. changelog, PR, eventuali check/merge exact-head.

**Esiti:** ADOTTABILE COME CANDIDATO / DA STUDIARE / SOLO REFERENCE / BLOCCATO / SCARTATO. Non dichiarare `GOLDEN CERTIFIED`, `DONOR VERIFIED` o `DEVICE PASS` sulla base di README, stelle o screenshot.
