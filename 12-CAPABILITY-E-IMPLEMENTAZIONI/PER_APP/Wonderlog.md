# Wonderlog — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0017](../REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | P1 | 94 | PROPOSTA | Regression entita-per-entita e file orfani; niente duplicazione lifecycle |
| [CAP-0027](../REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | P2 | 90 | PROPOSTA | Android share intent e consenso senza import occulto |
| [CAP-0023](../REGISTRO_CAPABILITY/CAP-0023.md) | Design System Flutter token-first | P2 | 89 | SOURCE_REPORTED | Riuso pattern non diventa Golden automaticamente |
| [CAP-0020](../REGISTRO_CAPABILITY/CAP-0020.md) | Shared Ecosystem Bridge COPY LINK | P2 | 88 | SOURCE_REPORTED | Verificare roundtrip reale e contratti consumer per versione |
| [CAP-0047](../REGISTRO_CAPABILITY/CAP-0047.md) | POI offline versionati e provenienza | P2 | 88 | PROPOSTA | Licenze ODbL provider e freshness; non scaricare tile pubblici |
| [CAP-0040](../REGISTRO_CAPABILITY/CAP-0040.md) | Deduplicazione foto per hash percettivo | P2 | 87 | PROPOSTA | Verificare algoritmo reale e precisione duplicati quasi identici |
| [CAP-0031](../REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | P2 | 86 | PROPOSTA | Licenza modello footprint benchmark 5 lingue e download opt-in |
| [CAP-0050](../REGISTRO_CAPABILITY/CAP-0050.md) | Riorganizzazione tappe e tempi itinerario | P2 | 85 | PROPOSTA | Tempi da routing verificato e controllo manuale ordine |
| [CAP-0010](../REGISTRO_CAPABILITY/CAP-0010.md) | Ricordi Then and Now | P2 | 83 | PROPOSTA | Usare media canonici e consenso foto |
| [CAP-0066](../REGISTRO_CAPABILITY/CAP-0066.md) | Trasferimento LAN QR HTTPS fidato | P2 | 83 | PROPOSTA | Pairing fingerprint HTTPS e test rete locale |
| [CAP-0011](../REGISTRO_CAPABILITY/CAP-0011.md) | Life Threads narrativi | P2 | 82 | PROPOSTA | Non introdurre archivio parallelo |
| [CAP-0113](../REGISTRO_CAPABILITY/CAP-0113.md) | Da appuntamento passato a ricordo privato | P2 | 81 | PROPOSTA | Collaudo fisico APK +116 V116-03…V116-05: annulla senza scrivere, anti-duplicato, Trash/restore e privacy; valutare riuso Wonderlog senza duplicare il diario. |
| [CAP-0120](../REGISTRO_CAPABILITY/CAP-0120.md) | Testi alternativi accessibili per immagini delle note | P2 | 81 | PROPOSTA | Il demo usa modelli BLIP/servizi che possono essere pesanti; l'accessibilita non equivale a certificazione WCAG. Test con screen reader. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0051](../REGISTRO_CAPABILITY/CAP-0051.md) | Mappe luoghi ricordi condivisi con ponte | P2 | 80 | SOURCE_REPORTED | Trasporto COPY LINK esplicito e autorizzato |
| [CAP-0012](../REGISTRO_CAPABILITY/CAP-0012.md) | Year in Review deterministico | P2 | 79 | PROPOSTA | Non ricostruire funzione gia integrata |
| [CAP-0087](../REGISTRO_CAPABILITY/CAP-0087.md) | Layer geografici pubblici con freshness e fallback | P2 | 79 | PROPOSTA | Per ogni feed dichiarare API, diritti commerciali, refresh, intervalli, limiti, simulazioni e disponibilita; nessuna navigazione operativa o allerta emergenza da data feed incompleti. Repo metadata NOASSERTION: verify license per file. |
| [CAP-0091](../REGISTRO_CAPABILITY/CAP-0091.md) | Snapshot condivisibile della vista mappa senza dati privati | P3 | 78 | PROPOSTA | Distinguere view state (camera, zoom, layers) da percorso/ricordi privati; share URL/file su azione volontaria, nessuna chiave API, token o posizione personale inclusa. |
| [CAP-0127](../REGISTRO_CAPABILITY/CAP-0127.md) | Note video navigabili per capitoli e timestamp | P3 | 78 | PROPOSTA | Fonte descrive tutorial YouTube -> guida con timestamp; accesso a transcript, copyright/ToS e disponibilita offline da verificare. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0009](../REGISTRO_CAPABILITY/CAP-0009.md) | Ricordi mappa geolocalizzata | P3 | 77 | PROPOSTA | Verificare permessi e nessuna condivisione GPS implicita |
| [CAP-0014](../REGISTRO_CAPABILITY/CAP-0014.md) | Cattura rapida contestuale da calendario | P3 | 75 | PROPOSTA | Conversione evento a ricordo sempre esplicita |
| [CAP-0021](../REGISTRO_CAPABILITY/CAP-0021.md) | QR inviti condivisi 24 ore | P3 | 75 | PROPOSTA | Serve prova camera e 2 account su device distinti |
| [CAP-0086](../REGISTRO_CAPABILITY/CAP-0086.md) | Sintesi vocale locale di note e contenuti editoriali | P3 | 72 | PROPOSTA | Prima valutare Android TextToSpeech sistema e licenze voci; modelli scaricabili solo opt-in; VoiceStudio AGPL: pattern solo, no code copy closed-source; nessuna imitazione vocale senza consenso. |
| [CAP-0085](../REGISTRO_CAPABILITY/CAP-0085.md) | Diarizzazione vocale locale per appunti riunioni | P3 | 70 | PROPOSTA | Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base. |
| [CAP-0132](../REGISTRO_CAPABILITY/CAP-0132.md) | Diario sonoro e classificazione eventi acustici | P3 | 69 | PROPOSTA | AudioDet classifica 17 suoni in dominio specifico; accuratezza universale non dimostrata. Nessuna registrazione senza consenso/azione. Verificare architettura e licensing nel Product Bible prima di integrare. |
| [CAP-0137](../REGISTRO_CAPABILITY/CAP-0137.md) | Oggetti 3D da fotografie collegati alle note | P3 | 52 | PROPOSTA | Stable Fast 3D Space esiste, ma infrastruttura, licenze commerciali e risorse GPU necessitano gate; non promettere offline. Verificare architettura e licensing nel Product Bible prima di integrare. |

**Totale associazioni:** 25. Non modificare automaticamente la roadmap del prodotto.
