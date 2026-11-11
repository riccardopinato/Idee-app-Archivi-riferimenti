# Matrice riuso — ipotesi, non integrazioni
| Componente | Origin | Consumer possibili | Regola | Stato |
|---|---|---|---|---|
| Scene contract e gesture | Adaptive Landscape | Notes canvas, vision board, giochi | solo core generalizzato; benchmark e Product Bible | CANDIDATE |
| GLES shaders/animation | Adaptive Landscape | launcher, giochi | Android-specific optional; verifica licenza/performance | CANDIDATE |
| WallpaperService lifecycle | Adaptive Landscape | wallpaper/launcher | non importare in Notes | REFERENCE |
| Job scheduler/checkpoints | AppFactoryAgent Windows da acquisire | Developer/QA/Research/Finance | repo/source SHA e regression test | SOURCE NOT VERIFIED |
| Tool approval/receipts | Agent Factory prospettato | AppLab, GitHub workflow | human gate, immutable evidence | DESIGN |
| Market provider interface | Finance Agent prospettato | watchlist/portfolio | dati licenziati, timestamp e freshness | DESIGN |
| Risk analytics pure functions | Finance Agent prospettato | Finance Agent e futuri dashboard | dati sintetici, out-of-sample | DESIGN |
| Crypto arbitrage patterns | riccardopinato/btrader | NON azionario di default | review licenza e domain mismatch | REFERENCE ONLY |

| Context workflow reconciliation | [Agent Core #12](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/12) + btrader E2E #5 | Finance/Scene e ulteriori app (DA VALIDARE) | helper puro non installato nei consumer; verify repo SHA, log cron, PR/recovery e permessi prima di admission | PROCESS CANDIDATE |
| Registry 35 repo / Site | [Ideas #97](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/97) | Control Center, futuri monitor QA | read-only, redazione privati, snapshot temporale, no validazione deploy live | SOURCE + CI VERIFIED |

Nessuna riga è automaticamente CAP nuova, donor certificato o Golden. Le CAP canoniche si aggiornano solo dopo deduplicazione nel REGISTRO_CAPABILITY.json e rigenerazione del catalogo.
