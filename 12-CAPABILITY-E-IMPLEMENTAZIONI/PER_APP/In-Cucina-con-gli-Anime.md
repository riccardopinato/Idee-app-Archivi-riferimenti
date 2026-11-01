# In-Cucina-con-gli-Anime — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0044](../REGISTRO_CAPABILITY/CAP-0044.md) | Ricette anti-spreco da ingredienti | P1 | 95 | 95% | Suggerire ricette fattibili usando ingredienti disponibili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0044/README.md) | PROPOSTA | Non clonare TasteAI; validare differenziazione |
| [CAP-0022](../REGISTRO_CAPABILITY/CAP-0022.md) | Localizzazione cinque o piu lingue | P1 | 94 | 80% | Fallback lingua dispositivo manuale e stringhe corrette | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0022/README.md) | SOURCE_REPORTED | Controllare parita lingua in native notifications |
| [CAP-0042](../REGISTRO_CAPABILITY/CAP-0042.md) | Catalogo editoriale multilingua offline | P1 | 94 | 80% | Pacchetti contenuti verificabili e localizzabili | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0042/README.md) | SOURCE_REPORTED | Riusare pattern non mescolare dati editoriali di prodotti differenti |
| [CAP-0073](../REGISTRO_CAPABILITY/CAP-0073.md) | AdMob UMP consent gating | P1 | 92 | 75% | Monetizzazione con richiesta ads soltanto quando consentita | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0073/README.md) | SOURCE_REPORTED | Test permessi consent e policy store |
| [CAP-0034](../REGISTRO_CAPABILITY/CAP-0034.md) | OCR scontrino e parsing spese | P2 | 90 | 80% | Estrarre data totale negozio da scontrino | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0034/README.md) | PROPOSTA | OCR locale poi conferma prima di transazione |
| [CAP-0072](../REGISTRO_CAPABILITY/CAP-0072.md) | Entitlement RevenueCat provider truth | P2 | 88 | 60% | Servizio entitlement con stato verificato e fallback | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0072/README.md) | ROADMAP_STORICA | IAP compliance e no premium unlocked falsely |
| [CAP-0043](../REGISTRO_CAPABILITY/CAP-0043.md) | Raccolta fonti contenuti e audit artwork | P2 | 85 | 65% | Workflow fonti licenze immagini e verifica contenuto | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0043/README.md) | SOURCE_REPORTED | Rispettare copyright e revisioni umane obbligatorie |
| [CAP-0036](../REGISTRO_CAPABILITY/CAP-0036.md) | Riconoscimento etichette senza barcode | P3 | 78 | 80% | OCR etichette e match con catalogo | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0036/README.md) | PROPOSTA | Conferma manuale prodotto gradazione ingredienti |
| [CAP-0046](../REGISTRO_CAPABILITY/CAP-0046.md) | Ingredienti da foto e confezioni | P3 | 78 | 80% | Scansione lista o confezione per scegliere ricetta | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0046/README.md) | PROPOSTA | OCR poi conferma attributi e nessuna promessa nutrizionale |
| [CAP-0086](../REGISTRO_CAPABILITY/CAP-0086.md) | Sintesi vocale locale di note e contenuti editoriali | P3 | 72 | 60% | Leggere ad alta voce ricordi, guide e ricette con controlli di velocita e ascolto offline. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0086/README.md) | PROPOSTA | Prima valutare Android TextToSpeech sistema e licenze voci; modelli scaricabili solo opt-in; VoiceStudio AGPL: pattern solo, no code copy closed-source; nessuna imitazione vocale senza consenso. |

**Totale associazioni:** 10. Non modificare automaticamente la roadmap del prodotto.
