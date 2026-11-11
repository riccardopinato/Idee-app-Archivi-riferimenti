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

Nessuna riga è automaticamente CAP nuova, donor certificato o Golden. Le CAP canoniche si aggiornano solo dopo deduplicazione nel REGISTRO_CAPABILITY.json e rigenerazione del catalogo.
