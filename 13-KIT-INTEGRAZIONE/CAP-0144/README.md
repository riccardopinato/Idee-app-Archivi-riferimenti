# CAP-0144 — Widget contestuali privacy-safe per agenda e contenuti condivisi

**KIT LIVELLO 1: RIFERIMENTI_ACQUISITI / SOLO IDEA.** Non è codice, non è READY o testato.

## Valore proposto

Widget OS alimentati da proiezioni canoniche autorizzate: prossimo evento/Crea, countdown e foto opt-in con mascheratura.

## App candidate e stato

- Agenda-per-Anna: `PROPOSTA`
- World-Days: `PROPOSTA`
- Wonderlog: `PROPOSTA`

## Provenienza e riuso

- [Idee NotebookLM originali — AD-NL26-05, AD-NL26-06, AD-NL26-11](../../11-NUOVE-IDEE/ANNA_NOTEBOOKLM_2026-11-02.md)
- [Mappa di deduplicazione e decisione](../../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_ANNA_NOTEBOOKLM_2026-11-02.md)
- Donor possibile: codice già esistente nell'app destinataria; nessuna dipendenza esterna acquisita.

## Documenti

- [Specifiche candidate](SPECIFICHE.md)
- [Codice di riferimento](CODICE_RIFERIMENTO.txt)
- [Integrazione Flutter](INTEGRAZIONE_FLUTTER.md)
- [Licenze e dipendenze](LICENZE_E_DIPENDENZE.md)
- [Test e validazione](TEST_E_VALIDAZIONE.md)
- [Compatibilità Anna preliminare](ANNA_SOURCE_COMPATIBILITA.md)

**Gate:** Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata.

[CAP canonica](../../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0144.md). Priorità CAP tecnica `P2 86/100` diversa dalla priorità idea editoriale. Nessuno sviluppo approvato.

## Re-audit v28 — 04/11/2026
Priorita corrente P2 88/100 (non release priority).
Motivo score: Anna private home-widget masking/source tested, OEM physical pending.
Facilita Agenda-per-Anna: 70% -> 73%. Anna/World-Days widget source and privacy gating, device QA pending.
Facilita World-Days: 45% -> 47%. Anna/World-Days widget source and privacy gating, device QA pending.
Riferimento: audit globale Factory Golden v28 nella cartella 12-CAPABILITY-E-IMPLEMENTAZIONI.
