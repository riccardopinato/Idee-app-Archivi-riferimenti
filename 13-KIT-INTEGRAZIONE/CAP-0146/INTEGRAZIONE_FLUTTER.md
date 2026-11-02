# Piano di integrazione Flutter — CAP-0146

**NON ESEGUITO / SOLO CANDIDATO.**

1. Fissare nuovo SHA di Anna's Diary, Product Bible e roadmap; non sbloccare Privacy #215.
2. Ispezionare `lib/src/screens/private_vault.dart` e i servizi/schermate collegati; verificare realmente lo spazio di riuso.
3. Definire contratto dati piccolo e idempotente: Nessun codice fino a threat model. Solo dopo: singolo PDF limitato, stream cifrato, preview temporanea protetta e recupero verificato.
4. Collegare flusso ai dati e servizi canonici: Vault canonico/Keystore Android, envelope encryption, file store protetto; non importare PDF engine come percorso plaintext.
5. Nessuna UI/billing/cloud/pubblicazione prima di approvazione specifica. Se native/privacy, progetto separato e gate fisici.
6. Flutter analyze, unit/widget test, exact-head CI, backup/regressione, APK firmato e QA OS secondo ambito reale.

## Blocco

Security HIGH: plaintext temporanei/thumbnail/indici, backup/cloud, perdita chiavi, iOS/Web, memoria; Privacy #215 ON HOLD; no claim Keystore universale.

Non qualificare la proposta come donor copy-ready o asserire Device PASS.
