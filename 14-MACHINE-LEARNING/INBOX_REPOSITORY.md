# Inbox dei repository Machine Learning

**Stato del 08/11/2026:** acquisiti e analizzati i primi **10 riferimenti MLR-0001...0010**. Fonte: elenco inviato nella chat del progetto e relativo materiale algoritmi. Ogni voce ha uno SHA fissato e una [scheda](AUDIT_10_REPOSITORY_ML_2026-11-08.md). Nessun modello, dataset o test esterno e stato eseguito/instaurato nelle app.

| ID stabile | GitHub verificato | Ricezione | Stato | SHA fonte | Scheda |
|---|---|---|---|---|---|
| MLR-0001 | [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 08/11/2026 | AUDIT_SORGENTE_E1 | 6e37063f7ab7ef7a7e257b9d44bc3ec6ee1b1bcd | [Scheda](SCHEDE/MLR-0001.md) |
| MLR-0002 | [mljs/ml](https://github.com/mljs/ml) | 08/11/2026 | AUDIT_SORGENTE_E1_ORG_NORMALIZZATA | 6e26dc30f09717129cb8614e67af0d310887cc21 | [Scheda](SCHEDE/MLR-0002.md) |
| MLR-0003 | [online-ml/river](https://github.com/online-ml/river) | 08/11/2026 | AUDIT_SORGENTE_E1 | 4768de0579f977315e65cd23ee658534c1d62c26 | [Scheda](SCHEDE/MLR-0003.md) |
| MLR-0004 | [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | 08/11/2026 | ANALISI_DOCUMENTALE_E1 | 8e5c0dfffdb56181450363f9ccd880bc69737ae8 | [Scheda](SCHEDE/MLR-0004.md) |
| MLR-0005 | [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) | 08/11/2026 | ANALISI_DOCUMENTALE_E1 | 73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde | [Scheda](SCHEDE/MLR-0005.md) |
| MLR-0006 | [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning) | 08/11/2026 | AUDIT_SORGENTE_E1 | 963d77f17f66da1f8357cb71e3680fb212e4684d | [Scheda](SCHEDE/MLR-0006.md) |
| MLR-0007 | [ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) | 08/11/2026 | ANALISI_DOCUMENTALE_E1_NO_LICENSE | 5f104458e9e081bf0b24df78bbe3bc839edca899 | [Scheda](SCHEDE/MLR-0007.md) |
| MLR-0008 | [faridrashidi/kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) | 08/11/2026 | ANALISI_DOCUMENTALE_E1_IDENTITA_PROVVISORIA | 2eaf7bbe9e541c1b127b860f0b27403c15d98771 | [Scheda](SCHEDE/MLR-0008.md) |
| MLR-0009 | [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | 08/11/2026 | ANALISI_DOCUMENTALE_E1 | 3fc9a9a436d5177902999d630324a37a7f1b29cf | [Scheda](SCHEDE/MLR-0009.md) |
| MLR-0010 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | 08/11/2026 | ANALISI_DOCUMENTALE_E1_LICENSE_AMBIGUA | 12bc9dc1504135ba9affe5f64da74276c9142955 | [Scheda](SCHEDE/MLR-0010.md) |

## Precisazioni per identificazione

- **MLR-0002:** l'input https://github.com/mljs punta a una organizzazione. Abbiamo documentato il repository aggregatore [mljs/ml](https://github.com/mljs/ml) e, nella scheda, **5 moduli satellite** con i relativi SHA. Non e una libreria Dart nativa.
- **MLR-0008:** l'utente ha scritto solo **Kaggle Solutions** senza URL univoco. Abbiamo analizzato [faridrashidi/kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) come **rappresentante provvisorio**, non come fonte confermata; alternativa verificata [EliotAndres/kaggle-past-solutions](https://github.com/EliotAndres/kaggle-past-solutions). In un prossimo messaggio con URL preciso si mantiene l'ID e si corregge la risoluzione.
- **MLR-0007, MLR-0008, MLR-0009 e MLR-0010:** raccolte di link/dati di riferimento, non pacchetti contenenti tutto il codice esterno citato.
- **MLR-0007 e MLR-0010:** code reuse bloccato da assenza/ambiguita di LICENSE, pur essendo consentito un audit di idee e link.

## Come continuare

I nuovi ingressi riceveranno **MLR-0011, MLR-0012, ...** e manterranno la cronologia. Per uno stesso repository gia registrato usare delta SHA e aggiornare la scheda invece di duplicare l'ID.

La sezione 14 rimane ricerca/provenienza E0/E1; [registro canonico delle CAP](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json) e Golden Registry restano gli unici luoghi di ammissione/promozione. I riferimenti a fonti figlie richiedono audit autonomi, anche quando l'indice e MIT.
