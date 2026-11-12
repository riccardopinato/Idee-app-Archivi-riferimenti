# App Factory 10x — programma continuo

**Direzione strategica approvata:** 12/11/2026. La Factory deve costruire e distribuire prodotti con meno passaggi manuali, sfruttando agenti, Golden versionati, AppLab, metriche business e conoscenza inter-app.

- [Roadmap con 57 task e 8 ondate](ROADMAP_10X.md)
- [Primi due audit di partenza](EVIDENCE_X10-001_BASELINE_2026-11-12.md) · [Mappa AppLab riutilizzabile](EVIDENCE_X10-004_APPLAB_REUSE_2026-11-12.md) — X10-001 e X10-004 con prove source e review.
- [Coda machine-readable e dipendenze](PROGRAM_QUEUE.json)
- [Contratto per la continuità](OPERATING_CONTRACT.md)
- [Script che seleziona i successori](../scripts/factory_10x_queue.py)
- [GitHub Actions giornaliera di validazione e proposta](../.github/workflows/app-factory-10x-queue.yml)

**Parallelismo dinamico dal 12/11/2026:** nessun tetto di tre task; il selettore espone tutti i READY, anche dello stesso repo se READ_ONLY. Blocchi sostituiti con altri READY; writer concorrenti solo con isolamenti e review espliciti. Non implica avere 57 agenti attivi simultaneamente: il numero effettivo dipende dalle dipendenze e dai runner.\n\nLa coda non si arresta ai primi cinque: ogni task approvato e verificato sblocca automaticamente il prossimo nel resolver; ai gate umani si continua nelle lane indipendenti. Il job Actions propone la sequenza ma **non sviluppa codice automaticamente**. L'esecuzione autonoma del coding-agent richiede invece import dell'agente locale o un runner reale e testato, CI, credenziali autorizzate, approval gates e misura della qualità.

**Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. Nessuna modifica di Master, Golden o Product Bible implicita.
