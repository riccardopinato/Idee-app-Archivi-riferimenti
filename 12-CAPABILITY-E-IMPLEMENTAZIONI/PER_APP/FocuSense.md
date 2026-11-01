# FocuSense — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Facilita integrazione (%) | Descrizione breve | Kit tecnico | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CAP-0065](../REGISTRO_CAPABILITY/CAP-0065.md) | Routine wearable e battery optimization audit | P1 | 94 | 80% | Matrice dei limiti foreground service batteria sensori | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0065/README.md) | PROPOSTA | Test OEM reale multi dispositivo e Doze |
| [CAP-0001](../REGISTRO_CAPABILITY/CAP-0001.md) | Pianificazione di slot liberi | P2 | 91 | 95% | Algoritmo locale che suggerisce fasce disponibili in calendario | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0001/README.md) | PROPOSTA | Verificare conflitti e non spostare eventi fissi |
| [CAP-0109](../REGISTRO_CAPABILITY/CAP-0109.md) | Sessioni Focus/Pomodoro collegate a note e protezione opzionale | P2 | 91 | 95% | Timer locale lavoro/pausa con attribuzione alla task o nota attiva e, se disponibile e autorizzato, controlli di… | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0109/README.md) | PROPOSTA | Riutilizzare eventuali timer FocusSense prima del codice; persistenza dopo app pause, gestione lifecycle e background Android, DND soltanto con permesso/azione esplicita; non promettere blocco siti. |
| [CAP-0062](../REGISTRO_CAPABILITY/CAP-0062.md) | Best Conditions Engine sensori | P2 | 80 | 85% | Usare luce rumore movimento per finestre di focus | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0062/README.md) | SOURCE_REPORTED | Score sensori non diagnosi e test runtime |
| [CAP-0063](../REGISTRO_CAPABILITY/CAP-0063.md) | Momenti ideali per focus in calendario | P2 | 80 | 90% | Suggerire intervalli di concentrazione da dati aggregati | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0063/README.md) | PROPOSTA | Consenso e niente spostamento eventi involontario |
| [CAP-0026](../REGISTRO_CAPABILITY/CAP-0026.md) | Sound feedback semantico opzionale | P3 | 78 | 80% | Feedback sonoro minimo e disattivabile | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0026/README.md) | PROPOSTA | Controllare silent mode e opzioni accessibilita |
| [CAP-0007](../REGISTRO_CAPABILITY/CAP-0007.md) | Scheda workout e storico multisport | P3 | 77 | 80% | Collega la scheda ad attività della giornata e storico | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0007/README.md) | PROPOSTA | Non creare doppio diario allenamenti |
| [CAP-0139](../REGISTRO_CAPABILITY/CAP-0139.md) | Studio del movimento da video con pose annotate | P3 | 63 | 45% | Motion Study Notes: Dai video estrae pose/fotogrammi di un movimento con annotazioni affiancate nella nota. | [Apri](../../13-KIT-INTEGRAZIONE/CAP-0139/README.md) | PROPOSTA | AIMoCap demo esiste; accuratezza tecnica e scientifica, privacy dei soggetti e permessi video da testare; non diagnosi medica. Verificare architettura e licensing nel Product Bible prima di integrare. |

**Totale associazioni:** 8. Non modificare automaticamente la roadmap del prodotto.
