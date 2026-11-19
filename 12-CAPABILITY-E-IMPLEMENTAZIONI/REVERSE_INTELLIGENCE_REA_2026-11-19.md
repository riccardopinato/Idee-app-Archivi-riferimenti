# Reverse Engineering & Software Intelligence — candidato di ricerca REA

**19/11/2026 · E1 / RESEARCH ONLY · NON CERTIFIED DONOR · NON GOLDEN**

## Fonte e diritti

- Engine: https://github.com/morluto/rea
- Pin: morluto/rea@4491c84c82140a43fa12390b727840a433875ba8
- Package: rea-agents 6.9.0, TypeScript/Node, CLI/MCP, licenza MIT
- Campo operativo: acquisizione forense/statica e analisi autorizzata di APK,
  PE/EXE, .NET, JS/Electron, siti web, file e comportamento runtime, con
  motori aggiuntivi che richiedono diritti/installazioni separati.
- Donor originario Deskland Windows:
  BLEZZ0102/Deskland@9818b577402ff476e1b59da07970c56472713126,
  licenza GPL-3.0. Codice e asset NON copiati nell'app Android indipendente.

## Contratto di riuso

| Elemento | Owner canonico | Stato |
|---|---|---|
| Ricerca/fonte OSS e diritti | Idee-app / Capability catalog | E1 pinned / proposta |
| Intake sicuro di un file locale | AppLab scripts/rea_artifact_intake.py | Codice candidato e test; CI da verificare |
| Reverse engineering REA | morluto/rea, esterno | Documentato, NON installato o eseguito qui |
| Report di ricostruzione app | Adaptive-Landscape-Android/docs/REA_DESKLAND_PILOT_2026-11-19.md | Source-side; installer assente |
| Admission e certificazione | Factory Golden OSS Reconnaissance / Single-Donor Admission | NON E3/E5, Registry invariato |

Il report AppLab è un *annesso di ricerca read-only*, non entra negli
artifact trusted di certificazione, non abilita agente, code execution,
autorepair, jailbreak, bypass di permessi o promozione automatica a Donor.
La pipeline CAP può leggere l'identità fonte/commit e link di evidenza,
ma non aggiunge oggi un ID CAP per una funzione non collaudata.
Usare la stessa evidenza per non duplicare registri E1.

## Pilota — Deskland

Upstream:
- Host C# .NET Framework / WebView2 con HTML/JS, temi locali.
- Integrazione Windows Progman/WorkerW, icone desktop lette dal sistema
  ogni ~400ms, visibilità fullscreen/tray, protocollo pagina-host.
- L'installer storico Deskland-Setup.exe della vecchia conversazione non
  è accessibile come bytes nel workspace corrente. Nessun hash, lista file,
  import PE/NSIS, decompilazione o test runtime è stato inventato.
- L'app consumer Android usa Flutter + WallpaperService, schema-2 e
  calibrazione manuale; non può replicare l'accesso alle coordinate icone
  Windows e non deve copiare codice GPL o artwork.

Repo pilota: https://github.com/riccardopinato/Adaptive-Landscape-Android
Repo QA: https://github.com/riccardopinato/AppLab
Contratto dettaglio: AppLab/integration/intelligence/REA_REVERSE_INTELLIGENCE_PILOT_2026-11-19.md

## Valore potenziale e gate

Priorità: **alta Deskland, medio-alta Factory**.
Per preferire REA a codice sorgente e strumenti esistenti servono
un artefatto autorizzato, baseline SHA-256, output tracciabile,
un delta di conoscenza misurabile e test indipendenti.
Usarlo prima per il caso sorgente-mancante; non imporlo dove il
repository contiene già sorgenti, test e CI affidabili.

**Per passare da E1 a E3:** test effettivi e CI exact-head per la
funzione circoscritta, verifiche del consumer, compatibilità legale,
nessuna promozione artificiale dello scanner. Per Golden E5:
altro consumer indipendente e percorso del Registry.
