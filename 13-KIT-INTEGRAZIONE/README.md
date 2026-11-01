# Kit di integrazione — App Factory

**140 cartelle kit, una per capability CAP.** [Indice](INDICE.md) · [Facilità integrazione](METODOLOGIA_FACILITA.md).

Ogni kit contiene: `README.md`, `SPECIFICHE.md`, `CODICE_RIFERIMENTO.txt`, `INTEGRAZIONE_FLUTTER.md`, `LICENZE_E_DIPENDENZE.md`, `TEST_E_VALIDAZIONE.md`.

## Prime compatibilità approfondite

[Audit e prove CAP-0134, CAP-0114 e CAP-0138](COMPATIBILITA_2026-11-01.md): codice originale limitato, test Dart, snapshot reale di Notes, licenze e limiti; nessun runtime Flutter/Android certificato.

## Livelli di preparazione

1. **RIFERIMENTI_ACQUISITI:** link, necessità, specifiche candidate e gate. Tutti i kit attualmente partono da qui.
2. **SPECIFICHE_ESTRATTE:** codice/API reali letti a un commit SHA e analizzati, licenza registrata.
3. **CODICE_PREPARATO:** adattamento legalmente riutilizzabile o originale, con test predisposti.
4. **INTEGRAZIONE_VALIDATA:** test effettivi, CI exact-head e runtime/device dove necessario.

Le schede di questo commit NON attestano i livelli 2, 3 o 4. Nessun codice OSS viene copiato soltanto perché una fonte è linkata. Scope e merge negli app repository restano subordinati a Product Bible, roadmap e gate.
