# Metodo stime «Facilità integrazione (%)»

**Scala:** 0% impossibile o quasi; 100% facilissimo. **Le percentuali sono stime editoriali iniziali per coppia CAP/app**, non probabilità statistiche né test/compatibilità certificati. La fonte canonica è il campo `integration_ease_percent` di ciascun record in `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json`.

## Bootstrap della stima

`percent = clamp(5,95,round_to_5(14 + 14*feasibility + 2*risk_control + domain_fit - heavy_penalty))`

- Fattibilità e controllo rischio sono punteggi 1–5 già registrati.
- Aderenza dominio/app: aggiustamento euristico limitato (-7 a +8); app senza una valutazione esplicita = 0.
- Penalità di complessità/footprint per i CAP 0117, 0120, 0130, 0131, 0132, 0136, 0137 e 0140.
- Prima verifica del singolo repository e della sua architettura, il valore iniziale resta tra 5 e 95 e si arrotonda a multipli di 5. **Non è un giudizio misurato.**

Il generatore legge i valori memorizzati e **non li ricalcola**: dopo un audit tecnico si possono sostituire per singola app, registrando SHA, dipendenze, fonte del codice e test. Lo Score di classifica CAP misura priorità/opportunità (0–100), non facilità. Lo Stato nell'app indica evidence ladder, non facilità.
