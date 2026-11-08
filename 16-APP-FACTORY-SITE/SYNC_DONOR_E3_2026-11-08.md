# Site: aggiornamento rapido donor E3 · 08/11/2026

Fonte ufficiale: [App-Factory-Core PR #87](https://github.com/riccardopinato/App-Factory-Core/pull/87), commit `a6d7ff36db7f70b03ccfdf02fa265049d31ae2f1`. Sei donor storici sono stati normalizzati a `E3_EXACT_HEAD_TESTS` tramite SHA source/test identici anche sul main e CI success sul commit esatto. Non nuove app né Golden.

Source canonico: `donors/REGISTRO_DONOR_CAPABILITY.json` e `reuse/PASSPORTS.json` alla SHA centrale.

Su [data/snapshot.json](data/snapshot.json) sono aggiornati:
- 6 Passport (source, test, blob SHA-1, CI, confini/negative scope), tutti 20 link Passport al commit nuovo;
- 6 righe della tabella di riuso `DONOR:<id>` in `Donor certificato`, senza cambiare ID né cancellare gli stati manuali;
- baseline Factory e metadati contatori (**15 E3 exact-head, 4 E3 storici, 1 E2**) senza cambiare Golden/CAP/app/roadmap;
- nessuna build Vercel richiesta: il Site esistente sincronizza la snapshot del branch `main` con `syncGitHub`, preservando le voci protette manualmente.

Per aggiornare la UI: scegliere `Sincronizza` o ricaricare la pagina. Se un record è manualmente protetto, resta invariato come desiderato dall'utente.
