# Specifiche candidate — CAP-0144

## Responsabilità distinta

Widget OS alimentati da proiezioni canoniche autorizzate: prossimo evento/Crea, countdown e foto opt-in con mascheratura.

## MVP delimitato

Android Home: prossimo evento e apertura Crea; countdown su data scelta. Foto partner solo fase differita con consenso per immagine e revoca cache.

## Vincoli architetturali

- Existing home_widget_bridge, Agenda store, shared media privacy gate, native Android AppWidget e iOS WidgetKit separati.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
