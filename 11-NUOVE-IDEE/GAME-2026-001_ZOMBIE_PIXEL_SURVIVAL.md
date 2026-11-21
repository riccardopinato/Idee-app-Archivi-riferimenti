# GAME-2026-001 — Zombie Pixel Survival (titolo provvisorio)

- **ID stabile:** GAME-2026-001
- **Nome e alias:** Zombie Pixel Survival / Atmospheric Zombie Precision Shooter (working title, non nome di gioco originale identificato).
- **Categoria / mercato:** gaming mobile, shooter 2D di precisione, zombie/survival, pixel art; Android e iOS.
- **Stato:** IDEA / DA_VALUTARE — **non approvata per sviluppo**, nessun repository app creato, nessuna release.
- **Fonte e data:** screenshot fornito dall'utente nella conversazione del 20/11/2026; valutazione commerciale nella stessa conversazione. Registrazione 21/11/2026.
- **Riferimento grafico:** immagine utente in chat, non copiata o pubblicata nel repository. Autore del gioco, URL originale e licenze non identificati.
- **Priorità esplorativa:** medio-alta, condizionata alla prova del gameplay.
- **App Factory baseline della registrazione:** `riccardopinato/App-Factory-Core@4df94ac3b3ea22a2323634fe83c3c7770fe3b835` (CURRENT.yaml: Master v27, Golden Index v31).

## Concept e proposta di valore

Sparatutto mobile panoramico a livelli brevi: atmosfera post-apocalittica, pixel art ricca, mira e rilascio touch, munizioni limitate e precisione. Differenziarsi con **ambientazione cinematografica + meccanica immediata**, non con la sola presenza degli zombie.

**Osservazioni direttamente visibili nello screenshot:** paesaggio al tramonto, grattacieli in rovina, vegetazione e specchio d'acqua con riflessi; interfaccia `RUN 2`, `5 infected left` e `BULLETS 5/5`; istruzioni `drag back from vincent to shoot · right-drag to look`. Non è verificato come funzioni realmente il tiro, l'IA dei nemici, la fisica o la progressione.

**Problema UX da affrontare:** personaggi e contatori molto piccoli rispetto alla scena. Su schermi telefonici preservare il paesaggio ma ingrandire target, feedback d'impatto e HUD; ottimizzare visuale orizzontale e touch.

## Valutazione preliminare (euristica, non dati di mercato)

| Dimensione | Punteggio |
|---|---:|
| Potenziale commerciale del concept | **7,5/10** |
| Qualità visiva percepita | **9/10** |
| Adattabilità mobile | **7/10** |
| Differenziazione nel genere | **6,5/10** |

Concorrenti da confrontare: *Stupid Zombies 3* (mira/livelli), *Dead Ahead: Zombie Warfare* (pixel art e progressione), *Mr Bullet* (gesto breve) e *Huntdown* (qualità visuale/premium). Sono riferimenti di design, **non comparabili diretti per vendite**; nessuna previsione di ricavi/installazioni.

## MVP da valutare

1. Demo Android landscape con **15 livelli**, due ambienti, **3 armi**, **4 tipologie di nemici**.
2. Loop: osserva scena → mira/trascina → rilascia/spara → completa obiettivo → stelle/ricompensa.
3. Livelli indicativamente da **30–90 secondi**, replay volontario, conteggio munizioni e feedback di tiro.
4. Progressione locale semplice e modalità Endless **solo in seconda fase**, se i test confermano divertimento.
5. Accessibilità: target leggibili, drag regolabile, HUD scalabile, suono/vibrazione disattivabili, comportamento su display compatti.
6. Benchmark su Android reali per frame pacing, input latency, memoria, consumi e stabilità dei riflessi/parallax.

**Stack candidato:** Godot 2D (prima scelta da verificare), alternativa Flutter + Flame se il gameplay rimane molto semplice. Evitare un'architettura eccessiva per l'MVP.

## Commercializzazione ipotetica

- Free-to-play con **rewarded ads volontarie**, interstitial rari fra livelli, acquisto unico "Rimuovi annunci" indicativamente **€3,99**, skin cosmetiche eventuali.
- **Niente banner durante il combattimento**; prezzi, AdMob, billing e creatività pubblicitaria non approvati né implementati.
- Alternativa premium/demo + sblocco se il prodotto evolve in campagna narrativa rifinita.

## Gate e rischi

- **Origine e diritti da verificare:** screenshot e gameplay osservabili sono una reference; non copiare sprite, musica, codice o asset senza titolarità e licenza compatibile. La ricreazione deve produrre asset originali o autorizzati.
- **Convalida domanda:** testare una demo con persone reali (campione esplorativo suggerito 100–300) e misurare completamento tutorial/primi livelli, tentativi spontanei, D1, feedback su mira e leggibilità. Obiettivo D1 30–35% **indicativo**, non dato garantito.
- **Rischi principali:** gameplay monotono, scarsa leggibilità su telefono, acquisizione utenti onerosa, costi della produzione artistica e licenze sconosciute.
- **Nessuna modifica ai repository delle app, nessun codice, CAP/Golden, monetizzazione o pubblicazione autorizzati da questa scheda.**

## Prossimo passo

Recuperare link/demo/repository del gioco mostrato, identificare l'autore e le condizioni d'uso; quindi progettare un prototipo **originale** del gesto di mira e farlo provare su Android prima di investire in una campagna completa.
