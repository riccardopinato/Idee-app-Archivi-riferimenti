# Stelle OSS — dock Windows, widget e cross-app · 16 novembre 2026

Factory baseline `c5adc147046beb7024629466d10eeb799c3c2619` · audit research **E0 / non approvato** · input `CURATED_USER_INPUT`, stella autenticata `UNVERIFIED`.

## Fonti fissate

1. [OpenTaskbar al commit 6348d7519f83e032c31a065d72ad3b327906da15](https://github.com/alztrk/opentaskbar/tree/6348d7519f83e032c31a065d72ad3b327906da15) — MIT in `LICENSE`, C#/.NET 10 WPF per Windows. Verificati `README.md`, `Design/README.md`, `Services/DockAutoHideController.cs`, `Services/TaskbarReplacementSession.cs`, `Services/WindowThumbnailPreview.cs`.
2. [lumabar al commit 5929d128d617b7d86165f74fa74bfc3fbcfbed32](https://github.com/Acadbek/lumabar/tree/5929d128d617b7d86165f74fa74bfc3fbcfbed32) — README e assets dimostrativi, codice proprietario assente dal repository, nessuna licenza OSS; sito https://lumabar.xyz/; **no code donor**.

## Feature extract e decisioni di prima ammissione

| Feature distinguibile | Sorgente | Deduplica / classificazione | Consumer e delta reale proposto | Decisione audit |
|---|---|---|---|---|
| Dock app pinnate / reorder persistente | OpenTaskbar, README + `Models/DockApp.cs` | ESTENSIONE_SCOPED, non CAP generata | Deskland: launcher Android ancora incompleto, verificare drawer, dock, gesture e stabilità; Windows utility: dock possibile | PROPORRE_APPROVAZIONE dello studio |
| Auto-hide per overlap con trigger al bordo | OpenTaskbar, `DockAutoHideController.cs` | ESTENSIONE_SCOPED | Deskland: solo pattern Android, API Win32 non portabili; desktop dock: riusabilità MIT verificabile | ACCORPARE con shell/dock |
| Safety journal e ripristino taskbar | OpenTaskbar, `TaskbarReplacementSession.cs` | ESTENSIONE_SCOPED / invarianti runtime | Deskland: percorso sicuro per tornare alla Home predefinita, senza alterare app di sistema; Windows: ripristino stato taskbar | PRIORITA P1 di affidabilità |
| DWM live thumbnail + Jump List | OpenTaskbar, `WindowThumbnailPreview.cs` / `NativeJumpListSession.cs` | OPZIONE_ARCHITETTURALE Windows | Desktop utility; Android: non copiare Win32/DWM e non promettere anteprime senza Android API/permessi | RINVIARE_CONSIGLIATO |
| Motion fisheye e indicatori applicazioni | OpenTaskbar, `Design/README.md` | UI_UX_REFERENCE, Design-App | Desktop launcher; accessibilità/reduced-motion e hit targets prima del polish | PROPORRE_APPROVAZIONE del benchmark visivo |
| Glass adattivo con contrast fallback | OpenTaskbar XAML + lumabar README | UI_UX_REFERENCE | Design-App; Deskland UI soltanto dopo QA batteria/rendering; no asset proprietari | ACCORPARE con design system |
| Barra compatta widget con drag-and-drop | lumabar README / `assets/widgets-preview.webp` | CAP-0144 limitata a widget contestuali; **nuovo contratto desktop non automaticamente ammesso** | App Factory Control Center: stato PR/CI/release; Notes: Quick Capture, task e timer canonici; nessun database parallelo | PROPORRE_APPROVAZIONE di studio P2 |
| Monitoraggio CPU/RAM/rete/screen time | lumabar README | OPZIONE_ARCHITETTURALE; permessi/provider da validare | Eventuale utility PC; **non** aggiungere sorveglianza invasiva ad Android | RINVIARE_CONSIGLIATO |
| Widget AI plan usage / GitHub / Gmail / payments | lumabar README | EVIDENCE_GAP su implementazione/APIs | Dashboard App Factory: solo provider ufficiali, token/consenso e quote; mai scraping/session cookies senza audit | BLOCCATO fino a provider gate |
| Workspace multi-window / sticky panels | entrambi, documenti | CAP-0088 e CAP-0182 già presenti | Evitare CAP duplicata e differenziare desktop da Android | ACCORPARE |

## Matrice consumer

| Consumer | Priorità ricerca | Limite/non-implementazione |
|---|---|---|
| Adaptive-Landscape-Android (Deskland) | P1 sicurezza e correttezza launcher, P2 motion | Nessuna copia WPF. Non interrompere stabilizzazione launcher e rendering; gate device e privacy prima di qualunque nuova implementazione |
| Design-App | P1 | Catalogare come REFERENCE, non COPY_READY |
| App Factory Control Center / Desktop Utility Factory | P2 | Prima individuare prodotto canonico, data owners e connessioni; non creare nuovo repo/servizio in automatico |
| Notes-Ecosistema | P3 | Solo proiezioni di task/agenda/note esistenti, non una seconda UI permanente |
| Anna's Diary | nessuna nuova lane | CAP-0144 e progressive disclosure già presenti come direzione; non ampliare scope |

## Gate e conclusione

**0 nuove CAP**, **0 app in roadmap**, **0 donor E3/Golden**, **0 codice copiato/implementato** in questo intake documentale. Le opportunità sono registrate come estensioni o referenze da ammettere solo dopo audit su Product Bible/HEAD, deduplica semantica completa, generazione kit e validazione richieste dal comando Stelle. La presenza di due URL esplicitamente segnalati non dimostra né quante altre stelle siano cambiate né che un repo sia ancora starred.

Fonte registro stelle: https://github.com/riccardopinato/Analisi-delle-mie-stelle-github
