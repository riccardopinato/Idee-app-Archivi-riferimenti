# App Factory 10x — programma continuo

**Direzione strategica approvata:** 12/11/2026. La Factory deve costruire e distribuire prodotti con meno passaggi manuali, sfruttando agenti, Golden versionati, AppLab, metriche business e conoscenza inter-app.

- [Roadmap con 57 task e 8 ondate](ROADMAP_10X.md)
- [Coda machine-readable e dipendenze](PROGRAM_QUEUE.json)
- [Contratto per la continuità](OPERATING_CONTRACT.md)
- [Script che seleziona i successori](../scripts/factory_10x_queue.py)
- [GitHub Actions giornaliera di validazione e proposta](../.github/workflows/app-factory-10x-queue.yml)

La coda non si arresta ai primi cinque: ogni task approvato e verificato sblocca automaticamente il prossimo nel resolver; ai gate umani si continua nelle lane indipendenti. Il job Actions propone la sequenza ma **non sviluppa codice automaticamente**. L'esecuzione autonoma del coding-agent richiede invece import dell'agente locale o un runner reale e testato, CI, credenziali autorizzate, approval gates e misura della qualità.

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. Nessuna modifica di Master, Golden o Product Bible implicita.
