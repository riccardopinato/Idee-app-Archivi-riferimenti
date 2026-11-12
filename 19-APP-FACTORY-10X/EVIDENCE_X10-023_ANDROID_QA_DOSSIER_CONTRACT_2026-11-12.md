# X10-023 — Contratto per prove Android reali (non attestatore)

**Factory baseline**: `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27, Golden Index v29. **Golden**: Notification Reliability, COPY_READY ma provider-sensitive/NEEDS_REVIEW. **Stato del task**: ancora `PLANNED`, non sono stati eseguiti test fisici Android.

## Componente sviluppato

[`scripts/factory_10x_notification_evidence.py`](../scripts/factory_10x_notification_evidence.py) è un ispettore deterministico **offline** di dossier che provengono da un futuro test Android reale, non uno strumento di acquisizione hardware. Il formato lega almeno repository/source SHA immutabile, hash SHA-256 APK, package ID, versionCode, fingerprint build Android (senza seriale dispositivo/persona), 18 scenari e prove con digest. Il parser rifiuta fonti mismatch, versioni non valide, record duplicati, scenari sconosciuti e PASS privi di riferimenti a prove.

I 18 scenari comprendono permessi consentiti/negati, canale attivo/bloccato, exact/inexact con consenso esplicito, visibilità immediata, registrazione vs reale consegna programmata, stable ID, edit/delete, date nel passato, fuso IANA, reboot, tap da app chiusa, salvataggio core indipendente dal fallimento di schedule e identità release. Un singolo scenario mancante, FAIL, BLOCKED o NOT_VERIFIED resta distinto da PASS.

**Limite essenziale:** anche se un dossier auto-dichiara 18/18 PASS e contiene digest plausibili, lo script restituisce *solo* `UNTRUSTED_COMPLETE_CLAIM_REQUIRES_INDEPENDENT_VERIFICATION`. Gli hash riportati non vengono verificati contro i byte, l'APK non viene installato, la notifica non viene osservata, nessuna attestazione può essere generata da dati JSON non affidabili. L'uscita contiene sempre `device_verified:false`, `platform_release_verified:false`, `golden_promoted:false`. Questo impedisce che una fixture sintetica risolva X10-023.

La review reale successiva deve usare AppLab come fonte indipendente per la rehash dell'APK e delle prove, verificare OS/runtime, hardware ed effettiva delivery prima di dichiarare qualsiasi risultato di livello device. Le prove locali dovranno rimanere private ed escludere identificativi sensibili o segreti.

**Test**: [`factory_10x_notification_evidence_test.py`](../tests/factory_10x_notification_evidence_test.py) include fixture 18/18 volutamente falsa per verificare il divieto di certificazione, dossier incompleti, SHA errati, proof assenti/malformati, errore fisico simulato, risultati BLOCKED/FAIL e duplicati; CI [queue 10x](../.github/workflows/app-factory-10x-queue.yml) verifica l'ispettore su SHA PR esatto.

**Comando quando esisterà un dossier acquisito da un dispositivo:**

```bash
python3 scripts/factory_10x_notification_evidence.py --input <dossier.json> --source-sha <40-character-sha>
```

X10-023 resta PLANNED finché non sono presenti adapter nativi reali e test piattaforma/dispositivo Android; il validator non li sostituisce. Non sono stati toccati repository consumer o App Factory Core.
