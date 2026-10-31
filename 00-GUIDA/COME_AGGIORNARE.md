# Come consultare e ampliare questo archivio

1. Parti dal README; entra nella cartella tematica. Non è necessario leggere tutti i file.
2. Ogni nuova idea va in [11-NUOVE-IDEE/INBOX_IDEE.md](../11-NUOVE-IDEE/INBOX_IDEE.md) prima di essere valutata. Solo i progetti promossi entrano nel portafoglio 01; non duplicare ID e conserva il riferimento alla proposta originale.
3. Crea scheda app con il template e descrizione cliente separata, senza claim non verificati.
4. Per librerie/repo registra URL, licenza, ref/commit, donor e progetto destinatario.
5. Per provider pubblici registra paese, diritto d'uso commerciale, attribution, rate limit, costi, data di verifica e fallback.
6. Per aggiornamenti di maturità app distingui codice presente, test, artifact e pubblicazione verificata, con fonte.
7. Se cambi una classifica mantieni il vecchio snapshot e crea una nuova versione datata.
8. Aggiorna README, indici e CHANGELOG quando introduci nuove categorie o decisioni.

Stati: [E] evidenza storica da chat/documento; [V] fonte esaminata alla data indicata; [C] candidata; [R] necessita di ulteriore verifica. Sono livelli di provenienza, non certificazioni. Per licenze e provider prevalgono condizioni correnti alla data dell'integrazione.

Confini: App-Factory-Core = Master/Golden; AppLab = QA; repo delle app = implementazione; questo repo = catalogo e ricerca.

## Capability trasversali e automazione

9. Nuove **funzioni** di un'app esistente o riusabili sono catalogate in `12-CAPABILITY-E-IMPLEMENTAZIONI`, non nell'inbox delle nuove **app**. Riutilizzare ID CAP esistente quando e la stessa responsabilita.
10. Per ogni app nuova aggiornare l'inventario e linkare le capability; per ogni stato di implementazione registrare fonte verificabile, esatto ref e prova disponibile.
11. Generare le viste con `python3 scripts/build_catalog.py`; la CI blocca il drift. Il monitoraggio trasversale e programmato tramite task con connettore GitHub (non webhook istantaneo, non accesso globale con GITHUB_TOKEN).
