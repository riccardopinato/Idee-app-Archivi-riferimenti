# Ricerca r/BestGitHubRepos — 1 novembre 2026

## Metodo, fonti e limiti
- Subreddit: https://www.reddit.com/r/BestGitHubRepos/
- La pagina listing/top e i feed JSON non erano accessibili dal browser di ricerca (cache miss). Sono stati esaminati **post indicizzati raggiungibili** (settembre-ottobre 2026) e le pagine GitHub canoniche di 11 repository. Non dichiarare censimento completo di tutti i post o repository del subreddit.
- Reddit rappresenta lo spunto di discovery, non la fonte della licenza. Le licenze indicate derivano dai metadati GitHub/README al 2026-11-01, pinned SHA sotto; la licenza di file, asset, pesi modello e API va verificata al momento dell'integrazione.
- Ogni proposta e research-only. Nessun codice, metodo di accesso privilegiato, modello o dataset e stato copiato nelle app.

## Repository analizzati, decisione e destinazioni

| Donor | Commit verificato | Licenza snapshot | Decisione | App / capability |
|---|---|---|---|---|
| [tobi/disktree](https://github.com/tobi/disktree) | `9b18b272` | MIT | ADATTARE PATTERN, nessun Rust desktop transplant in Android | CAP-0083, Omni Cleaner, Downloads Butler |
| [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools) | `d505845f` | GPL-3.0 | REFERENCE_ONLY / clean-room per utility chiusa | CAP-0084, DevPocket Tools, CmdPocket |
| [sharevb/it-tools](https://github.com/sharevb/it-tools) | branch `chore/all-my-stuffs` non pinned | GPL-3.0 fork | SECONDARY_REFERENCE, non donor indipendente | CAP-0084 |
| [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) | `b9e9ebef` | MIT | PATTERN/SDK EVAL, desktop Electron non adatto come dipendenza Flutter | CAP-0031 e CAP-0085, Notes/Anna/Wonderlog |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | `13a5ef77` | AGPL-3.0 | REFERENCE_ONLY in prodotti closed-source; mobile solo preview, modelli con diritti propri | CAP-0086, CAP-0033 |
| [NarYuki/Dextop](https://github.com/NarYuki/Dextop) | `5402d091` | GPL-3.0 | DEFER, hidden Android APIs/OEM, HyperOS disabled | CAP-0088 / EdgeDock / App Profiles / DeskPilot |
| [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) | `a92fd471` | MIT | PATTERN for local experiment trace, no new orchestration engine | CAP-0089 / AppLab |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | `8978801d` | GitHub NOASSERTION; README mentions MIT; verify scope | REFERENCE_ONLY, data/API/3D licensed independently | CAP-0087, CAP-0091 / travel |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | `6c16b23f` | Apache-2.0 repository; templates/deps separately | PATTERN selective, no agent stack adoption | CAP-0090 / AppLab |
| [ShaikhWarsi/free-ai-tools](https://github.com/ShaikhWarsi/free-ai-tools) | `4e2c00c3` | MIT list | DIRECTORY ONLY, pricing/model/API claims need official verification | Research/app provider scouting |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `4ae2317d` | MIT | ALREADY CATALOGUED: no duplicate donor | AppLab skills process |

## Post Reddit verificabili e rilievi
- [IT Tools 27/10](https://www.reddit.com/r/BestGitHubRepos/comments/1xgpvro/) — commento segnala il fork sharevb, utile come reference; i numeri di star e i dettagli license del post non sostituiscono GitHub.
- [Dextop 30/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wu5tcb/) — interazione Android desktop. README ufficiale indica Xiaomi HyperOS **disabled**, comportamento diverso per OEM.
- [VoiceStudio 26/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wqvy29/) — voce locale, dubbing/narration, mobile preview; AGPL e pesi modello da verificare.
- [OpenWhispr 26/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wqltx4/) — dictation locale, whisper.cpp/sherpa-onnx e speaker labels; il nostro CAP-0031 esiste gia.
- [disktree 30/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wud3go/) — visual treemap e scanning, con limiti Windows/NTFS non trasferibili in Android.
- [OpenResearch 29/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wt62lb/) — ricerca locale riproducibile; evitare un secondo AppLab.
- [God's Eye View 19/09](https://www.reddit.com/r/BestGitHubRepos/comments/1wkt8qz/) — live public signal, ma molti feed sono simulated/partial e alcuni costi non commercial; non navigazione.
- [Awesome LLM Apps 09/10](https://www.reddit.com/r/BestGitHubRepos/comments/1x1jike/) — catalogo di template, scegliere una capability per volta.
- [Free AI Tools 11/10](https://www.reddit.com/r/BestGitHubRepos/comments/1x2zk4a/) — directory, cifre e promesse da verificare direttamente presso provider.
- [Skills for Real Engineers 04/09](https://www.reddit.com/r/BestGitHubRepos/comments/1w7aaav/) — gia presente nel catalogo donor.

## Decisioni anti-duplicazione e opportunita

- **CAP-0031** trascrizione offline esiste; OpenWhispr e VoiceStudio diventano nuovi reference, non nuovi CAP equivalenti.
- **CAP-0032** ricerca semantica e **CAP-0033** model pack gia coprono concept vicini.
- **CAP-0077** capability-permission health e gia catalogato; la parte Dextop utile e il probe OEM fail-closed, non un bypass degli accessi Android.
- Nuovi CAP-0083…CAP-0091 hanno scope separato: visualizzazione storage, toolbox local, diarizzazione, TTS, geodata con freshness, workspace Android, experiment log, scope creep, scene snapshot.
- **App candidato DevPocket Tools**: distinta da CmdPocket (che e' command reference), centrata su piccoli convertitori; non iniziare nuovo package prima di test SEO/uso.
- **DiskScope** prima *feature* Omni Cleaner, poi eventuale app.
- **GeoPulse Live** solo studio provider e costi, non release o allerta d'emergenza.
- **DeskPilot** scartare ora su Xiaomi/HyperOS; non usare API nascoste per aggirare le limitazioni di Android.

## Rapporto commerciale / realizzabilita
1. SUBITO DA VALUTARE: CAP-0083 (Omni), CAP-0084 (toolbox locali), CAP-0089 (provenance experiment).
2. CANDIDATA CON VERIFICA: CAP-0090 (scope creep, controllare AppLab esistente); CAP-0085 (diarization solo pack on demand); CAP-0091 (geo scene snapshot senza PII).
3. RINVIATA: CAP-0086 (TTS su mobile, prima sistema Android) e CAP-0087 (feed live con limiti licenza).
4. NON PRIORITARIA: CAP-0088 (desktop hidden API, OEM incompatibility, GPL-3.0).

Questa ricognizione non equivale a integrazione di librerie e non conferisce licenze.
