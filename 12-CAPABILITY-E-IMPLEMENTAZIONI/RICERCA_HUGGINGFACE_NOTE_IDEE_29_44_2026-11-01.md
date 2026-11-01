# Ricerca Hugging Face Notes — terza raccolta #29–44 (conservazione integrale)

- **Data:** 2026-11-01
- **Factory baseline:** `riccardopinato/App-Factory-Core@63dd5e4f703cb23e4095a72beb253720bc1ca9a1`, Master v27.
- **Fonte originale:** https://huggingface.co/search/full-text?q=to+do (elenco dinamico non enumerato completamente).
- **Governance:** proposta di prodotto, non roadmap, donor approvato, test o rilascio. Le 16 idee sono quelle descritte nella terza ricerca in Chat.
- **Ricerca precedente:** [#1–12](RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md), [#13–28](RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md).
- **Valutazione:** numeri editoriali 0–10 del confronto in Chat; diverso dal punteggio CAP 0–100 ponderato.

## Inventario completo

| Idea # | Nome | Proposta conservata | Score idea | Capability canonica | Riferimenti |
|---|---|---|---|---|---|
| 29 | **Privacy Shield** | Individua PII nel testo di note/PDF e propone oscuramenti in una copia esportata, conservando l'originale e la scelta per campo. | 9,9/10 | [CAP-0114](REGISTRO_CAPABILITY/CAP-0114.md) | [redact](https://huggingface.co/spaces/desert-ant-labs/redact-demo) |
| 30 | **Contradiction Finder** | Evidenzia frasi potenzialmente in conflitto tra note, senza scegliere quale versione sia vera. | 9,8/10 | [CAP-0115](REGISTRO_CAPABILITY/CAP-0115.md) | [contradict](https://huggingface.co/spaces/sharath88/contradiction-entailment-demo) |
| 31 | **Duplicate Notes Cleaner** | Trova note semanticamente simili e suggerisce confronto/merge mantenendo allegati, riferimenti e cestino. | 9,7/10 | [CAP-0116](REGISTRO_CAPABILITY/CAP-0116.md) | [dedup](https://huggingface.co/spaces/minishlab/semantic-deduplication) |
| 32 | **Sketch-to-Diagram** | Converte un diagramma disegnato a mano in box, etichette e frecce editabili dentro la canvas. | 9,7/10 | [CAP-0117](REGISTRO_CAPABILITY/CAP-0117.md) | [tadpole](https://huggingface.co/Srinjoy99/tadpole-0.8b), [gguf](https://huggingface.co/Srinjoy99/tadpole-0.8b-GGUF) |
| 33 | **Document Delta** | Confronta due versioni dello stesso PDF/testo mettendo in evidenza modifiche puntuali e, se disponibile, differenze di layout. | 9,6/10 | [CAP-0118](REGISTRO_CAPABILITY/CAP-0118.md) | [diff](https://discuss.huggingface.co/t/document-processing-and-comparison-pipeline/172894) |
| 34 | **Citation Integrity Checker** | Controlla esistenza e metadati di citazioni e bibliografie, segnalandone anomalie senza dichiarare falsi positivi come inventati. | 9,5/10 | [CAP-0119](REGISTRO_CAPABILITY/CAP-0119.md) | [cite](https://huggingface.co/spaces/wz258/CiteAudit) |
| 35 | **Accessible Image Notes** | Genera bozze di descrizioni accessibili per foto e immagini collegate alle note, modificabili dall'utente. | 9,4/10 | [CAP-0120](REGISTRO_CAPABILITY/CAP-0120.md) | [alt](https://huggingface.co/spaces/abhilash88/ai-alt-tag-generator/blob/main/app.py) |
| 36 | **Easy Reading Mode** | Crea una versione semplificata affiancata a un documento, senza sostituire il testo originale. | 9,4/10 | [CAP-0121](REGISTRO_CAPABILITY/CAP-0121.md) | [simple](https://huggingface.co/datasets/ndgold/live-linguist-easylanguage-sft) |
| 37 | **Table Capture** | Estrae griglie e valori da tabella fotografata o PDF in celle modificabili con evidenza dei campi incerti. | 9,3/10 | [CAP-0122](REGISTRO_CAPABILITY/CAP-0122.md) | [table](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md) |
| 38 | **Bilingual Notes Reader** | Mostra originale e traduzione affiancati, con navigazione allineata di sezioni/pagine. | 9,2/10 | [CAP-0123](REGISTRO_CAPABILITY/CAP-0123.md) | [dual](https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md) |
| 39 | **Topic Discovery** | Propone collezioni tematiche ricavate dall'intero archivio di note, con cluster approvabili e origine visibile. | 9,2/10 | [CAP-0124](REGISTRO_CAPABILITY/CAP-0124.md) | [topics](https://huggingface.co/datasets/SIRIS-Lab/topic-modeling-maps) |
| 40 | **Chart-to-Data** | Stima serie numeriche da immagini di grafici e produce tabelle con incertezza e verifica manuale. | 9,1/10 | [CAP-0125](REGISTRO_CAPABILITY/CAP-0125.md) | [chart](https://huggingface.co/datasets/maurovidal/chart2data-v0) |
| 41 | **Living Glossary** | Crea glossario personale con definizioni, abbreviazioni e traduzioni consultabili durante la scrittura. | 9,0/10 | [CAP-0126](REGISTRO_CAPABILITY/CAP-0126.md) | [gloss](https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md) |
| 42 | **Video Chapter Notes** | Importa link video e crea note con timestamp e capitoli editabili che rinviano a punti specifici. | 9,0/10 | [CAP-0127](REGISTRO_CAPABILITY/CAP-0127.md) | [video](https://huggingface.co/abdulshakur/youtube_tutorial/blob/b4f7637fd69dbab34e0fda3edc784918cb4bbb40/README-HF.md) |
| 43 | **Form-to-Card** | Estrae coppie campo-valore da moduli e fatture in schede modificabili con link al file sorgente. | 8,9/10 | [CAP-0128](REGISTRO_CAPABILITY/CAP-0128.md) | [forms](https://huggingface.co/datasets/Voxel51/form_understanding_in_noisy_scanned_documents_plus) |
| 44 | **Knowledge Freshness** | Mostra revisioni di affermazioni e fonti nel tempo, proponendo il mantenimento della versione nuova e di quella storica. | 8,9/10 | [CAP-0129](REGISTRO_CAPABILITY/CAP-0129.md) | [memory](https://huggingface.co/papers/2606.10677) |

## Fonte, stato, perimetro e gate per idea

### 29 — Privacy Shield

- **Stato fonte:** `PAGE_PRESENT_DEMO_UNTESTED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Individua PII nel testo di note/PDF e propone oscuramenti in una copia esportata, conservando l'originale e la scelta per campo.
- **URL originali/alternativi:** [https://huggingface.co/spaces/desert-ant-labs/redact-demo](https://huggingface.co/spaces/desert-ant-labs/redact-demo)
- **Rischi e test:** Non certifica copertura IBAN/credenziali o privacy su tutte le lingue; regex locali e NER opzionale, redaction irreversibile sul file esportato.
- **Riuso/possibili overlap:** CAP-0039; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 30 — Contradiction Finder

- **Stato fonte:** `PAGE_PRESENT_DEMO_UNTESTED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Evidenzia frasi potenzialmente in conflitto tra note, senza scegliere quale versione sia vera.
- **URL originali/alternativi:** [https://huggingface.co/spaces/sharath88/contradiction-entailment-demo](https://huggingface.co/spaces/sharath88/contradiction-entailment-demo)
- **Rischi e test:** NLI e segnalazione probabilistica, necessita prova sulle negazioni, numeri, date e citazioni; nessuna correzione automatica.
- **Riuso/possibili overlap:** CAP-0032, CAP-0097; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 31 — Duplicate Notes Cleaner

- **Stato fonte:** `PAGE_PRESENT_DEMO_UNTESTED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Trova note semanticamente simili e suggerisce confronto/merge mantenendo allegati, riferimenti e cestino.
- **URL originali/alternativi:** [https://huggingface.co/spaces/minishlab/semantic-deduplication](https://huggingface.co/spaces/minishlab/semantic-deduplication)
- **Rischi e test:** SemHash dimostra dedup di testi/dataset, non merge sicuro di note personali. Usare ID e backup canonici.
- **Riuso/possibili overlap:** CAP-0017, CAP-0018; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 32 — Sketch-to-Diagram

- **Stato fonte:** `MODEL_CARD_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Converte un diagramma disegnato a mano in box, etichette e frecce editabili dentro la canvas.
- **URL originali/alternativi:** [https://huggingface.co/Srinjoy99/tadpole-0.8b](https://huggingface.co/Srinjoy99/tadpole-0.8b) · [https://huggingface.co/Srinjoy99/tadpole-0.8b-GGUF](https://huggingface.co/Srinjoy99/tadpole-0.8b-GGUF)
- **Rischi e test:** Q4 circa 529 MB + vision encoder circa 205 MB, quindi non nell'APK base; proof su diagrammi italiani e licensing.
- **Riuso/possibili overlap:** CAP-0028, CAP-0029, CAP-0098; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 33 — Document Delta

- **Stato fonte:** `COMMUNITY_DISCUSSION_ONLY` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Confronta due versioni dello stesso PDF/testo mettendo in evidenza modifiche puntuali e, se disponibile, differenze di layout.
- **URL originali/alternativi:** [https://discuss.huggingface.co/t/document-processing-and-comparison-pipeline/172894](https://discuss.huggingface.co/t/document-processing-and-comparison-pipeline/172894)
- **Rischi e test:** Il thread spiega diff testuale/semantico, non fornisce un'app donor: pattern di riferimento; attenzione a OCR e riconciliazione pagine.
- **Riuso/possibili overlap:** CAP-0037; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 34 — Citation Integrity Checker

- **Stato fonte:** `SPACE_EXISTS_RUNTIME_ERROR` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Controlla esistenza e metadati di citazioni e bibliografie, segnalandone anomalie senza dichiarare falsi positivi come inventati.
- **URL originali/alternativi:** [https://huggingface.co/spaces/wz258/CiteAudit](https://huggingface.co/spaces/wz258/CiteAudit)
- **Rischi e test:** La demo CiteAudit ha runtime error al controllo; verificare Crossref/DOI/ISBN prima di ogni integrazione; offline limitato.
- **Riuso/possibili overlap:** CAP-0097; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 35 — Accessible Image Notes

- **Stato fonte:** `SOURCE_FILE_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Genera bozze di descrizioni accessibili per foto e immagini collegate alle note, modificabili dall'utente.
- **URL originali/alternativi:** [https://huggingface.co/spaces/abhilash88/ai-alt-tag-generator/blob/main/app.py](https://huggingface.co/spaces/abhilash88/ai-alt-tag-generator/blob/main/app.py)
- **Rischi e test:** Il demo usa modelli BLIP/servizi che possono essere pesanti; l'accessibilita non equivale a certificazione WCAG. Test con screen reader.
- **Riuso/possibili overlap:** CAP-0035; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 36 — Easy Reading Mode

- **Stato fonte:** `DATASET_CARD_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Crea una versione semplificata affiancata a un documento, senza sostituire il testo originale.
- **URL originali/alternativi:** [https://huggingface.co/datasets/ndgold/live-linguist-easylanguage-sft](https://huggingface.co/datasets/ndgold/live-linguist-easylanguage-sft)
- **Rischi e test:** Dataset multilingue Easy-Language come riferimento; rischio di cambiare significato, soprattutto testi legali/medici.
- **Riuso/possibili overlap:** CAP-0032; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 37 — Table Capture

- **Stato fonte:** `README_SOURCE_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Estrae griglie e valori da tabella fotografata o PDF in celle modificabili con evidenza dei campi incerti.
- **URL originali/alternativi:** [https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md)
- **Rischi e test:** Paper2Any include extraction di tabelle in PPT, non un modulo Flutter pronto; integrare con CAP-0035 OCR locale e validazione cellule.
- **Riuso/possibili overlap:** CAP-0035; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 38 — Bilingual Notes Reader

- **Stato fonte:** `README_SOURCE_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Mostra originale e traduzione affiancati, con navigazione allineata di sezioni/pagine.
- **URL originali/alternativi:** [https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md](https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md)
- **Rischi e test:** Il donor traduce PDF con pipeline e servizi esterni; niente invio implicito di documenti privati; licenza, quote e uso commerciale da verificare.
- **Riuso/possibili overlap:** CAP-0022; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 39 — Topic Discovery

- **Stato fonte:** `DATASET_CARD_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Propone collezioni tematiche ricavate dall'intero archivio di note, con cluster approvabili e origine visibile.
- **URL originali/alternativi:** [https://huggingface.co/datasets/SIRIS-Lab/topic-modeling-maps](https://huggingface.co/datasets/SIRIS-Lab/topic-modeling-maps)
- **Rischi e test:** BERTopic/UMAP del progetto riguarda progetti UE, non note personali; modelli e footprint da valutare, fallback tag manuali.
- **Riuso/possibili overlap:** CAP-0013, CAP-0032; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 40 — Chart-to-Data

- **Stato fonte:** `DATASET_CARD_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Stima serie numeriche da immagini di grafici e produce tabelle con incertezza e verifica manuale.
- **URL originali/alternativi:** [https://huggingface.co/datasets/maurovidal/chart2data-v0](https://huggingface.co/datasets/maurovidal/chart2data-v0)
- **Rischi e test:** Dataset sintetico di grafici lineari semplici: non dimostra accuratezza su grafici reali complessi; non sostituire dati originali.
- **Riuso/possibili overlap:** CAP-0035; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 41 — Living Glossary

- **Stato fonte:** `PATTERN_REFERENCE_ONLY` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Crea glossario personale con definizioni, abbreviazioni e traduzioni consultabili durante la scrittura.
- **URL originali/alternativi:** [https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md](https://huggingface.co/spaces/MCP-1st-Birthday/gdrive-pdf-translator-mcp/blob/main/README.md)
- **Rischi e test:** La fonte descrive un glossario per coerenza nella traduzione, non un glossario automatico di note; revisione editoriale obbligatoria.
- **Riuso/possibili overlap:** CAP-0013; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 42 — Video Chapter Notes

- **Stato fonte:** `README_SOURCE_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Importa link video e crea note con timestamp e capitoli editabili che rinviano a punti specifici.
- **URL originali/alternativi:** [https://huggingface.co/abdulshakur/youtube_tutorial/blob/b4f7637fd69dbab34e0fda3edc784918cb4bbb40/README-HF.md](https://huggingface.co/abdulshakur/youtube_tutorial/blob/b4f7637fd69dbab34e0fda3edc784918cb4bbb40/README-HF.md)
- **Rischi e test:** Fonte descrive tutorial YouTube -> guida con timestamp; accesso a transcript, copyright/ToS e disponibilita offline da verificare.
- **Riuso/possibili overlap:** CAP-0027; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 43 — Form-to-Card

- **Stato fonte:** `DATASET_RIGHTS_RESTRICTED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Estrae coppie campo-valore da moduli e fatture in schede modificabili con link al file sorgente.
- **URL originali/alternativi:** [https://huggingface.co/datasets/Voxel51/form_understanding_in_noisy_scanned_documents_plus](https://huggingface.co/datasets/Voxel51/form_understanding_in_noisy_scanned_documents_plus)
- **Rischi e test:** FUNSD+ contiene annotazioni form con licenza custom; reference per layout, vietato incorporare dataset senza gate diritti.
- **Riuso/possibili overlap:** CAP-0035, CAP-0075; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

### 44 — Knowledge Freshness

- **Stato fonte:** `PAPER_ABSTRACT_REVIEWED` (verifica di pagina, README o scheda; non prova di funzionamento in Notes).
- **Problema e funzione:** Mostra revisioni di affermazioni e fonti nel tempo, proponendo il mantenimento della versione nuova e di quella storica.
- **URL originali/alternativi:** [https://huggingface.co/papers/2606.10677](https://huggingface.co/papers/2606.10677)
- **Rischi e test:** Infini Memory e ricerca per memoria agentica topic-based; l'adattamento a note locali e proposta, non software certificato.
- **Riuso/possibili overlap:** CAP-0097; non ricopiare codice o registri dati.
- **Stato prodotto:** `PROPOSTA`; non autorizzato in roadmap.

## Criteri di conservazione

- Niente cancellazione di riferimenti se il demo e temporaneamente non operativo: indicare `RUNTIME_ERROR` o `UNCONFIRMED` e rivedere in futuro.
- Un URL Hugging Face non equivale a permesso commerciale; verificare licenza **di ciascun modello, dataset, file e dipendenza** al momento del test.
- DPI, pagine PDF, dati finanziari, dati medici e foto sono privati: preferire elaborazione locale, opt-in, preview, copie sicure ed export, evitare telemetria e upload impliciti.
- Proporre un solo dominio canonico per note, media, allegati, citazioni e cross-links; rispettare lifecycle, ripristino, permessi e backup.
- Nessun APK, modello o dataset esterno incorporato per questa archiviazione.
