# CAP-0162 — QA e validazione

**ESITO: NON TESTATO NELL'APP / NO DONOR E3 / NO DEVICE / NO RELEASE.**

- Input vuoto, malformato, ripetuto, 1/100/5000 record, caratteri Unicode.
- Account switch, ACL revocata, source revision cambiata, cancellazione e restore.
- Writer canonico unico, no-loss, offline, conflitti, retry, undo e rollback.
- Timezone/DST, locale, date ricorrenti se applicabili.
- FGS/microfono/schermo/NFC/tastiera con permesso esplicito e disattivazione dove richiesto.
- Performance e footprint misurate prima/dopo sul consumer.
- E1 richiede SHA + path, E2 test presente, E3 CI pertinente, E4 device, E5 consumer.

Gate: Riconciliare con Knowledge Graph e link stabili già implementati
