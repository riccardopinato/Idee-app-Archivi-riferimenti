# Monitoraggio e aggiornamento incrementale

## Ingresso
- Repository GitHub accessibili a `riccardopinato`, compresi i nuovi; leggere main/default branch, Product Bible/roadmap/AGENTS e diff significativi se cambiati.
- Nuove funzionalita nominate in Project e fonti di ricerca quando rese disponibili nella conversazione/tasked context.
- Nuove Golden, donor, Design-App e stato AppLab quando realmente pertinenti.

## Procedura idempotente
1. Elencare i repo con GitHub. Confrontare con l'inventario precedente e distinguere **new repo**, **new implementation**, **changed evidence**, **no change**.
2. Per ogni nuovo repository, prima classificarlo come app/prodotto, donor, infrastruttura o archivio. Non promuovere un README a prova runtime.
3. Per ogni nuova funzione, cercare un CAP ID simile. Se trovato, collegare solo la nuova app o aggiornare evidence/stage senza duplicare. Se distinto, assegnare CAP-(max+1), monotono e senza riuso.
4. Aggiornare `REGISTRO_CAPABILITY.json` e il file audit; rigenerare tutte le viste con lo script e validare `--check`.
5. Creare branch e PR nel repository dell'archivio. Fare merge **solo** con exact-head gate verde e review non bloccanti; non modificare altri repository per catalogazione.
6. In caso di errori, diritti insufficienti o evidenze ambigue: segnare `DA_VERIFICARE`, non inventare stato e non forzare merge.
7. Segnalare solo aggiornamenti materiali: nuovi CAP, nuove app, cambi comprovati di stato, problemi licensing o blocchi.

## Garanzie e limiti
- Monitoraggio **periodico**, non realtime: aggiornamenti al prossimo controllo, sempre che il task e il connettore GitHub siano attivi e autorizzati.
- Il GitHub Actions `GITHUB_TOKEN` locale puo validare lo stesso repo ma non esplorare arbitrariamente tutti i repository privati del proprietario. Il controllo trasversale usa una automazione ChatGPT separata, non secrets replicati.
- Il catalogo NON cambia automaticamente le roadmap delle app; ogni promozione prodotto richiede il contratto della app.
- Lo stato reale di una build/release richiede evidence-specifica, non deduzione da descrizioni.

## Baseline discovery

Il file [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json) elenca i 31 repository accessibili al 01/11/2026 e distingue quelli campionati con roadmap dai repository censiti solo come presenza. I SHA `null` sono intenzionali: il prossimo controllo deve leggere il commit reale del default branch prima di un confronto; non inventare SHA. Per qualsiasi nuova app senza repository pubblico si mantiene PROPOSTA e si segnala la mancata verifica.
