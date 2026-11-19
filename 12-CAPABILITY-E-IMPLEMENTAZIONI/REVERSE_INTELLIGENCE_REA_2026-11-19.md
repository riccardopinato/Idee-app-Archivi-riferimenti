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
| Intake sicuro di un file locale | AppLab scripts/rea_artifact_intake.py | Integrato con test e CI; identità statica, non decompila |
| REA CLI statico (imports/certificates) | AppLab scripts/rea_cli_bridge.py, [PR #236](https://github.com/riccardopinato/AppLab/pull/236) | [REA invocato davvero: smoke PASS](https://github.com/riccardopinato/AppLab/actions/runs/44604806371) su PE sintetico; PR #236 **merged** |
| Dossier pilota Deskland | [AppLab report binario pubblico](https://github.com/riccardopinato/AppLab/blob/main/integration/intelligence/REA_DESKLAND_PREVIEW_BINARY_REPORT_2026-11-19.md) + Adaptive-Landscape-Android/docs/REA_DESKLAND_PILOT_2026-11-19.md | **REAL PUBLIC PREVIEW BINARY PASS**; installer storico assente |
| Admission e certificazione | Factory Golden OSS Reconnaissance / Single-Donor Admission | NON E3/E5, Registry invariato |

Il bridge AppLab invoca la CLI REA 6.9.0 in modo esplicito (senza MCP o server); conserva evidenze JSON e rifiuta automaticamente input non ammessi. **Non** è stato eseguito sul vecchio installer Deskland e il test sintetico non ne certifica la ricostruzione.

Il report AppLab è un *annesso di ricerca read-only*, non entra negli
artifact trusted di certificazione, non abilita agente, code execution,
autorepair, jailbreak, bypass di permessi o promozione automatica a Donor.
La pipeline CAP può leggere l'identità fonte/commit e link di evidenza,
ma non aggiunge oggi un ID CAP per una funzione non collaudata.
Usare la stessa evidenza per non duplicare registri E1.

## Prova reale di reverse engineering (release pubblica, non file storico)

REA CLI v6.9.0 ha ispezionato il pacchetto ufficiale Deskland Preview v0.1.3 sul runner GitHub, [run #44615407360](https://github.com/riccardopinato/AppLab/actions/runs/44615407360). SHA-256 ufficiale dell'installer `e253cad56f1ea0ee2fb9d13ebe8a44f7dbe7232a506ba752cbe54c939c17bf44`; **43/43** contenuti pubblicati estratti e validati per SHA-256, più 5 file NSIS di supporto. Outer installer x86 PE32 con 7 DLL/163 importazioni; vero host `Deskland.exe` 94.208 byte, .NET x64 IL-only, assembly v0.1.3.0, 200 metodi, 40 mapping P/Invoke e WebView2 1.0.4191.47. **Nessuna nuova capability Android trasferibile** trovata rispetto ai sorgenti; l'adozione generalizzata di REA rimane opzionale. Il vecchio `Deskland-Setup.exe` fornito dall'utente **non è stato analizzato**; non usarne i riferimenti per inferire stessi bytes/versione.

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
