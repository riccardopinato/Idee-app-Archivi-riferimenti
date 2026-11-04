#!/usr/bin/env python3
"""One-time, idempotent 23-ML-to-CAP admission with evidence-preserving Golden map."""
import json, re
# E0 proposals for Anna are intentionally not assigned invented source-audit paths.
# GitHub Projects mirror batch tests must remain bounded as proposal count grows.
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"12-CAPABILITY-E-IMPLEMENTAZIONI"
KIT=ROOT/"13-KIT-INTEGRAZIONE"
REG=CAT/"REGISTRO_CAPABILITY.json"
INBOX=ROOT/"11-NUOVE-IDEE/INBOX_IDEE.md"
INTAKE=ROOT/"11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md"
IDXT=KIT/"INDICE.md"
STAMP="ML23_CAP_ADMISSION_2026-11-04"
DATE="2026-11-04"
BASELINE="riccardopinato/App-Factory-Core@6cbb3449ba375496029bee93b45bc9f939dcd794"
REPORT="AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md"
GITHUB="https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/"
DEFS=json.loads(r'''[{"intake":"ML26-004","id":"CAP-0151","name":"Riassunti estrattivi di note con TextRank e citazioni","domain":"organizzazione","f":[5,4,4,3,4],"apps":{"Notes-Ecosistema":84,"Agenda-per-Anna":72,"Wonderlog":73,"PDF-Unifier":64},"deps":["CAP-0032","CAP-0097","CAP-0148"],"engine":"LEXICAL_TEXT","why":"Ranking di frasi originali con offset e fonte; sintesi estrattiva non generativa","gate":"Segmentazione multilingua, citazioni/negazioni, source-revision, test di frasi non inventate, fallback a estratto lineare."},{"intake":"ML26-001","id":"CAP-0152","name":"Ricerca fuzzy offline per refusi e alias","domain":"ricerca","f":[5,5,5,4,4],"apps":{"Notes-Ecosistema":93,"Agenda-per-Anna":89,"Wonderlog":88,"PDF-Unifier":83},"deps":["CAP-0015","CAP-0032"],"engine":"LEXICAL_TEXT","why":"Distanza Levenshtein/Jaro-Winkler solo su candidati autorizzati, Unicode-aware","gate":"Top-K bounded, grapheme, token di 1 carattere, soglie false-match, 500/5000 record e nessuna fuga da Shared Spaces."},{"intake":"ML26-008","id":"CAP-0153","name":"Previsione prudente di completamento studio e progetti","domain":"pianificazione","f":[4,4,4,3,4],"apps":{"Notes-Ecosistema":74,"Agenda-per-Anna":71,"FocuSense":66},"deps":["CAP-0108","CAP-0104","CAP-0102"],"engine":"SCHEDULING_FORECAST","why":"Media robusta o regressione locale con intervallo e fallback senza previsione","gate":"Minimo storico, anomalie, weekend e pause, intervallo di confidenza onesto, mai date certe da campioni scarsi."},{"intake":"ML26-009","id":"CAP-0154","name":"Routine predittive con Markov solo opt-in","domain":"organizzazione","f":[4,3,4,3,3],"apps":{"Agenda-per-Anna":71,"Notes-Ecosistema":69,"SleepMax-Coach":63,"FocuSense":68},"deps":["CAP-0111","CAP-0148"],"engine":"BEHAVIORAL_PATTERNS","why":"Transizioni tra stati locali e frequenze smussate per suggerimenti reversibili","gate":"Opt-in, minimal retention, cancellazione, min-sample, divieto inferenze sensibili e zero notifiche automatiche."},{"intake":"ML26-013","id":"CAP-0155","name":"Associazioni ingredienti e ricette offline con Apriori","domain":"ricette","f":[5,4,5,3,4],"apps":{"TasteAI":84,"In-Cucina-con-gli-Anime":82,"MealMate":77},"deps":["CAP-0044","CAP-0045"],"engine":"BEHAVIORAL_PATTERNS","why":"Frequent itemset e regole con supporto/confidenza, mai dedurre allergeni o causalità","gate":"Corpus minimo, support/confidence/lift, ingredienti canonici, lingua, allergeni, nessuna aggiunta automatica a spesa."},{"intake":"ML26-016","id":"CAP-0156","name":"Semplificazione reversibile di tracce e polilinee GPX","domain":"geografia","f":[4,5,5,4,4],"apps":{"TrailPath":82,"Wonderlog":89,"CamperBoss":86},"deps":["CAP-0048","CAP-0049","CAP-0050"],"engine":"GEO_GEOMETRY","why":"Ramer–Douglas–Peucker parametrizzato in metri, originale immutato","gate":"Lat/lon finiti, antimeridiano e poli, endpoint/waypoint protetti, errore massimo verificato, nessuna mutazione dello storico."},{"intake":"ML26-018","id":"CAP-0157","name":"Gesti volontari locali tramite Dynamic Time Warping","domain":"sensori","f":[4,4,3,3,3],"apps":{"Phone-Guard":61,"Pocket-Guard":72,"Tabletop-Motion-Alarm":67,"FocuSense":65},"deps":["CAP-0057","CAP-0062"],"engine":"SENSOR_SIGNAL","why":"Distanza DTW con template scelto dall'utente; cap sensori/FGS obbligatorio","gate":"Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita."},{"intake":"ML26-019","id":"CAP-0158","name":"Soglie adattive con isteresi per luce e prossimità","domain":"sensori","f":[5,5,5,4,4],"apps":{"Pocket-Guard":91,"Phone-Guard":86,"FocuSense":89,"Tabletop-Motion-Alarm":84},"deps":["CAP-0057","CAP-0062"],"engine":"SENSOR_SIGNAL","why":"EWMA e debounce per segnali rumorosi, impossibile inferire contesto da un solo campione","gate":"Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM."},{"intake":"ML26-015","id":"CAP-0159","name":"Clustering spaziale privacy-safe per ricordi e POI","domain":"geografia","f":[4,5,4,4,4],"apps":{"Wonderlog":88,"TrailPath":79,"CamperBoss":82,"Agenda-per-Anna":70},"deps":["CAP-0009","CAP-0051","CAP-0048"],"engine":"GEO_GEOMETRY","why":"DBSCAN in metri o griglia geospaziale con source visibility","gate":"Antimeridiano/poli, GPS nullo/non finito, raggio geodesico, permesso luoghi condivisi, dati privati non esportabili per default."},{"intake":"ML26-002","id":"CAP-0160","name":"Estrazione TF-IDF di parole chiave e tag suggeriti","domain":"organizzazione","f":[5,4,5,4,4],"apps":{"Notes-Ecosistema":91,"Agenda-per-Anna":80,"Wonderlog":84,"PDF-Unifier":74},"deps":["CAP-0124","CAP-0148","CAP-0032"],"engine":"LEXICAL_TEXT","why":"TF-IDF sparse per keyword e ranking, distinto da embeddings semantici","gate":"Tokenizzazione IT/EN/ES/FR/DE/PT, stopwords, IDF stabile, shared ACL, gestione corpus piccolo, preview prima di tag writer."}]''')
MAP=json.loads(r'''{"ML26-001":["CAP-0152"],"ML26-002":["CAP-0160"],"ML26-003":["CAP-0124"],"ML26-004":["CAP-0151"],"ML26-005":["CAP-0002","CAP-0092","CAP-0148"],"ML26-006":["CAP-0001","CAP-0102"],"ML26-007":["CAP-0102","CAP-0050"],"ML26-008":["CAP-0153"],"ML26-009":["CAP-0154"],"ML26-010":["CAP-0057","CAP-0062"],"ML26-011":["CAP-0041"],"ML26-012":["CAP-0032","CAP-0044"],"ML26-013":["CAP-0155"],"ML26-014":["CAP-0048","CAP-0049"],"ML26-015":["CAP-0159"],"ML26-016":["CAP-0156"],"ML26-017":["CAP-0057"],"ML26-018":["CAP-0157"],"ML26-019":["CAP-0158"],"ML26-020":["CAP-0061"],"ML26-021":["CAP-0032"],"ML26-022":["CAP-0132"],"ML26-023":["CAP-0148","CAP-0111"]}''')
FAMILIES=json.loads(r'''{"LEXICAL_TEXT":{"mode":"NEW GOLDEN CANDIDATE","core":"GOLDEN_HYBRID_LOCAL_SEARCH_ENGINE_v1_DRAFT","needs":"Pure Dart tokenizer/TF-IDF, bounded fuzzy and cited extractive summaries","downstream":["CAP-0015","CAP-0032","CAP-0093","CAP-0097","CAP-0124","CAP-0148"]},"SCHEDULING_FORECAST":{"mode":"EXTEND EXISTING GOLDEN RULES DRAFT","core":"GOLDEN_LOCAL_RULES_AUTOMATION_ENGINE_v1_DRAFT","needs":"Greedy bounded slots + robust forecast separated from canonical calendar writes","downstream":["CAP-0001","CAP-0102","CAP-0104","CAP-0106","CAP-0108","CAP-0111"]},"BEHAVIORAL_PATTERNS":{"mode":"NEW GOLDEN CANDIDATE","core":"GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT","needs":"Explainable Markov/Apriori with support and minimum observations","downstream":["CAP-0044","CAP-0045","CAP-0111","CAP-0148"]},"GEO_GEOMETRY":{"mode":"EXTEND EXISTING GPX/SPATIAL GOLDENS","core":"GOLDEN_GPX_INTEROPERABILITY_ENGINE_v1_DRAFT + GOLDEN_SPATIAL_CLUSTERING_ENGINE_v1_DRAFT","needs":"Bounded reversible simplifier and meter-scale density clustering","downstream":["CAP-0009","CAP-0048","CAP-0049","CAP-0050","CAP-0051"]},"SENSOR_SIGNAL":{"mode":"EXTEND SENSOR FUSION GOLDEN DRAFT","core":"GOLDEN_SENSOR_FUSION_ANDROID_v1_DRAFT","needs":"Portable EWMA/hysteresis core + optional DTW bounded gestures; OEM adapters separate","downstream":["CAP-0057","CAP-0061","CAP-0062"]}}''')

def save(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(content.rstrip()+"\n",encoding="utf-8")

def score(vals):
    weights=[.35,.25,.20,.10,.10]
    return int(20*sum(x*y for x,y in zip(vals,weights))+.5)

def priority(s):
    return "P1" if s>=92 else "P2" if s>=79 else "P3"

def kits(spec, rec):
    folder=KIT/rec["id"]
    label=rec["id"]+" — "+rec["title"]
    src=GITHUB+"11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md"
    dependent=", ".join(spec["deps"])
    family=spec["engine"]
    apps="\n".join("- "+a+": PROPOSTA, facilita stimata "+str(v)+"%" for a,v in spec["apps"].items())
    md={
        "README.md":"# "+label+"\n\n**RIFERIMENTI_ACQUISITI — SOLO PROPOSTA.** Non e codice riusabile o Golden certificato.\n\n"+rec["description"]+"\n\n## App candidate\n"+apps+"\n\nFattori score "+str(rec["score"])+" ("+rec["priority"]+"); facilità indipendente per app.\n\n- Motore candidato: "+family+"\n- CAP a monte: "+dependent+"\n- Fonte: "+src+"\n- Gate: "+spec["gate"]+"\n\nAltri file: [Specifiche](SPECIFICHE.md), [Codice riferimento](CODICE_RIFERIMENTO.txt), [Flutter](INTEGRAZIONE_FLUTTER.md), [Licenze](LICENZE_E_DIPENDENZE.md), [Test](TEST_E_VALIDAZIONE.md).\n",
        "SPECIFICHE.md":"# "+label+"\n\nMVP read-only: "+spec["why"]+".\n\nConfini: "+spec["gate"]+"\n\n- Input: dati canonicali visible/permission-scoped e revision delle fonti.\n- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.\n- Dipendenze: "+dependent+". No nuovo database o sync cross-app.\n- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.\n",
        "CODICE_RIFERIMENTO.txt":"CAP: "+rec["id"]+"\nORIGINE: Machine Learning.txt e audit ML26\nCANDIDATE_ENGINE: "+family+"\nFACTORY_BASELINE: "+BASELINE+"\nSOURCE_REF: "+src+"\nEVIDENCE_LEVEL: E0 (SPECIFICA), salvo donor preesistente separato\nCODE_EXTRACTED: NO\nDART_CODE_COPY_READY: NO\nMODEL_WEIGHT_MEASURED: NO\nPRIVACY_CONSENT: REQUIRED BEFORE USER CONTENT IS WRITTEN\n",
        "INTEGRAZIONE_FLUTTER.md":"# "+label+"\n\n1. Risolvere la Product Bible e lo SHA dei repo app al momento dell'implementazione.\n2. Selezionare la piu piccola fonte Golden E3 pertinenti, senza promuovere l'intero motore in automatico.\n3. Adapter puro Dart (o Kotlin nativo se richiesto) per "+family+"; nessuna rete o modello predefinito.\n4. Data filtering e ACL prima degli algoritmi; no source mutation e idempotenza per conferme ripetute.\n5. Test proprietà/determinismo e negative/fuzz; analisi Dart/Flutter, CI exact-head, hardware se coinvolti sensori/batteria.\n6. E3 donor dopo direct tests+CI; E5 solo dopo consumer indipendente e prove scope.\n\nGATE: "+spec["gate"]+"\n",
        "LICENZE_E_DIPENDENZE.md":"# "+label+" — licenze\n\nFonte: user-authored Machine Learning.txt, audit "+src+".\n\nAlgoritmi matematici astratti non equivalgono a una licenza di implementazione. Codice clean-room da scrivere; eventuali librerie/modelli/dataset richiedono licenza/file SHA, OS support, attribution, costi e footprint.\n\n- Non includere scikit-learn, TFLite/CoreML o modelli di terzi automaticamente.\n- No remote API a pagamento, nessun transfer di note personali o geodati.\n- Golden DRAFT e donor di altre app non significano certificazione qui.\n",
        "TEST_E_VALIDAZIONE.md":"# "+label+" — gate QA\n\n- Invarianti: input finiti e validati, risultati riproducibili/tie-break, permessi e source revision, zero write implicit.\n- Negativi: empty/one element, dati raddoppiati, unicode/locale, stale/deleted/archived, device capability absent, no model, no network.\n- Eseguire piccoli + 500/5000 synthetic fixtures, misurare correctness prima di p50/p95, dimensione apk diff e RAM/batteria su device distinto.\n- "+spec["gate"]+"\n- Solo evidence a commit SHA e CI exact-head puo portare a donor E3; consumer indipendente E5 resta futuro.\n\nESITO: NOT TESTED IN THIS AUDIT / NOT COPY READY.\n"
    }
    for name,content in md.items():
        if (folder/name).exists():
            raise RuntimeError("New kit unexpectedly already exists "+str(folder/name))
        save(folder/name,content)

def main():
    registry=json.loads(REG.read_text(encoding="utf-8"))
    if registry.get("ml_golden_audit_stamp")==STAMP:
        print("Already admitted; no duplicate CAP");return
    records=registry["records"]
    if len(records)!=150 or records[-1]["id"]!="CAP-0150" or sum(len(x["app_states"]) for x in records)!=346:
        raise RuntimeError("Unexpected registry baseline, do not overwrite newer CAPs")
    if len(DEFS)!=10 or len(MAP)!=23:
        raise RuntimeError("Incomplete ML intake mapping")
    if sorted(int(x["id"][4:]) for x in DEFS)!=list(range(151,161)):
        raise RuntimeError("Non-monotone CAP identity")
    text=INTAKE.read_text(encoding="utf-8")
    original={}
    for row in text.splitlines():
        if row.startswith("| ML26-"):
            cols=[v.strip() for v in row.strip("|").split("|")]
            if len(cols)!=7 or cols[0] in original:raise RuntimeError("Malformed source table")
            original[cols[0]]=cols
    if set(original)!=set(MAP) or len(original)!=23:
        raise RuntimeError("Intake source drift 23 rows")
    by_id={x["id"]:x for x in records}
    if len(by_id)!=150:raise RuntimeError("duplicate CAP")
    path_ref=GITHUB+REPORT
    observed_existing={}
    for alg,targets in MAP.items():
        for cap in targets:
            if cap not in by_id and cap not in {x["id"] for x in DEFS}:
                raise RuntimeError("Unmapped CAP for "+alg+": "+cap)
            if cap in by_id:
                observed_existing.setdefault(cap,[]).append(alg)
    for cap,ids in observed_existing.items():
        rec=by_id[cap]
        rec["ml_20261104_reuse"]={
            "algorithms":sorted(set(ids)),
            "decision":"REUSE_FIRST; existing scope only, no automatic code or score promotion",
            "audit":path_ref,"factory_baseline":BASELINE
        }
    # Only genuinely relevant new app-category associations; no fake releases.
    palette=by_id["CAP-0041"]
    for app, ease in [("TasteAI",78),("In-Cucina-con-gli-Anime",82)]:
        if app not in palette["app_states"]:
            palette["app_states"][app]="PROPOSTA"
            palette["integration_ease_percent"][app]=ease
            palette.setdefault("ml_20261104_new_app_basis",{})[app]={
              "reason":"Visual color palette matching is a related extension of existing photo palette CAP; NOT ingredient recognition",
              "audit":path_ref,"status":"candidate"
            }
    scores=[]
    for s in DEFS:
        vals=s["f"]
        if len(vals)!=5 or any(not isinstance(v,int) or v<1 or v>5 for v in vals):
            raise RuntimeError("Invalid factor scores")
        result=score(vals)
        fields=["user_value","cross_app_reuse","feasibility","evidence_strength","risk_control"]
        item={
            "id":s["id"],"title":s["name"],"domain":s["domain"],
            "score":result,"priority":priority(result),
            "scores":dict(zip(fields,vals)), "description":s["why"],
            "app_states":{a:"PROPOSTA" for a in s["apps"]},
            "source":{"type":"USER_ML23_ALGORITHM_AUDIT","ref":GITHUB+"11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md"},
            "next_gate":s["gate"],"reviewed_at":DATE,
            "certification":"NOT_VERIFIED_BY_THIS_AUDIT",
            "integration_ease_percent":s["apps"],
            "algorithm_intake_id":s["intake"],
            "golden_candidate_family":s["engine"],
            "upstream_capabilities":s["deps"],
            "source_evidence_grade":"E0_SPEC_ONLY",
            "ml_20261104_ease_basis":{a:{"estimate":v,"method":"engineering heuristic based on existing source and Golden maturity, not a measured success rate","factory_baseline":BASELINE} for a,v in s["apps"].items()}
        }
        records.append(item);by_id[item["id"]]=item
        kits(s,item)
        scores.append((item,s))
    registry["updated_at"]=DATE
    registry["factory_baseline"]=BASELINE
    registry["ml_golden_audit_stamp"]=STAMP
    registry["ml_golden_audit_ref"]=path_ref
    save(REG,json.dumps(registry,ensure_ascii=False,indent=2))
    index=IDXT.read_text(encoding="utf-8")
    if not index.startswith("# Indice — 150 kit"):
        raise RuntimeError("Kit count drift")
    index=index.replace("# Indice — 150 kit","# Indice — 160 kit",1)
    for cap,_ in scores:
        index+="\n| "+cap["id"]+" | "+cap["title"]+" | "+", ".join(cap["app_states"])+" | [Apri]("+cap["id"]+"/README.md) |"
    save(IDXT,index)
    kitread=KIT/"README.md"
    x=kitread.read_text(encoding="utf-8")
    x=x.replace("**150 cartelle kit","**160 cartelle kit",1)
    x+="\n## 10 nuovi kit algortimi ML26 — 04/11/2026\n\n[Audit Golden cross-app](../12-CAPABILITY-E-IMPLEMENTAZIONI/"+REPORT+"). Tutti livello 1 (E0), nessun donor/certificazione runtime ottenuta dall'ammissione.\n"
    save(kitread,x)
    registryRead=CAT/"README.md"
    x=registryRead.read_text(encoding="utf-8")
    x=x.replace("**150 capability individuali, 48 app/idee beneficiarie e 346 associazioni app-capability**","**160 capability individuali, 48 app/idee beneficiarie e "+str(sum(len(y["app_states"]) for y in records))+" associazioni app-capability**",1)
    x=x.replace("[150 kit tecnici]","[160 kit tecnici]",1)
    x+="\n## Audit ML23 / Golden reuse — 04/11/2026\n\n[23 algoritmi mappati a 160 CAP](./"+REPORT+") e [grafo dipendenze](CATENE_MOTORI_ML_2026-11-04.json). Questa e catalogazione E0, non codice certificato.\n"
    save(registryRead,x)
    readme=ROOT/"README.md"
    x=readme.read_text(encoding="utf-8")
    x+="\n## Motori ML on-device replicabili — audit 04/11/2026\n\n[Audit ML23 / Golden](12-CAPABILITY-E-IMPLEMENTAZIONI/"+REPORT+") con 10 nuove CAP e grafo dipendenze che abilita riuso a catena. Nessun import in app per effetto del catalogo.\n"
    save(readme,x)
    inbox=INBOX.read_text(encoding="utf-8")
    addition="\n**Aggiornamento di ammissione 04/11:** le dieci candidature ML26-001/002/004/008/009/013/015/016/018/019 sono state registrate rispettivamente come CAP-0152/0160/0151/0153/0154/0155/0159/0156/0157/0158, tutte PROPOSTA/E0. Le altre 13 restano riferite a CAP gia esistenti. [Audit Golden completo](../12-CAPABILITY-E-IMPLEMENTAZIONI/"+REPORT+").\n"
    marker="Nessun modello o codice integrato; 10 voci NUOVA CANDIDATA sono intake, non CAP canoniche e non modificano ranking esistenti."
    if marker not in inbox:raise RuntimeError("Unexpected intake inbox text")
    save(INBOX,inbox.replace(marker,"Nessun modello o codice integrato. Le 10 idee sono ora ammesse come CAP proposte, senza mutare le app."+addition,1))
    # Existing historical intake preserved, with explicit newer status banner.
    start="**Origine:** file utente Machine Learning.txt"
    marker2="## Presupposti rigorosi"
    if start not in text or marker2 not in text:raise RuntimeError("intake format drift")
    amend="## Stato canonico successivo all'audit Golden — 04/11/2026\n\nLe dieci righe storiche NUOVA CANDIDATA sono ora **registrate come CAP-0151…0160 (PROPOSTA, E0)**, senza codice applicativo. I riferimenti completi e la mappatura in ordine sono nella [matrice Golden](../12-CAPABILITY-E-IMPLEMENTAZIONI/"+REPORT+"). La sezione qui sotto resta lo snapshot di input precedente all'ammissione.\n\n"
    save(INTAKE,text.replace(marker2,amend+marker2,1))
    # Atomic machine-readable dependency map and acceptance scopes.
    graph={"version":1,"date":DATE,"source":BASELINE,"audit":STAMP,
        "families":FAMILIES,
        "algorithms":[{"intake":alg,"alg_name":original[alg][1],"target_caps":caps,
            "entry_type":"NEW_CAP" if any(x["id"] in caps for x in DEFS) else "EXISTING_CAP_REUSE",
            "original_research_priority":original[alg][5],"source_note":original[alg][6]}
            for alg,caps in sorted(MAP.items())],
        "new_capabilities":[{"id":a["id"],"title":a["title"],"engine":a["golden_candidate_family"],
            "prerequisites":a["upstream_capabilities"],"consumer_apps":list(a["app_states"]),
            "score":a["score"],"priority":a["priority"]} for a,_ in scores],
        "release_gate":"E0 intake; E1 source SHA; E2 tests present; E3 exact head test PASS scoped donor; E4 physical; E5 independently tested consumer"
    }
    save(CAT/"CATENE_MOTORI_ML_2026-11-04.json",json.dumps(graph,ensure_ascii=False,indent=2))
    assoc=sum(len(rec["app_states"]) for rec in records)
    lines=[
        "# Audit completo 23 algoritmi ML e motori candidati Golden — 04/11/2026",
        "",
        "**Core baseline SHA** "+BASELINE+" (Master v27; Golden Index v28). **Ideas baseline** 150 CAP / 346 associazioni. **Dopo** 160 CAP / "+str(assoc)+" associazioni / 48 app.",
        "",
        "Audit source: [Machine Learning.txt riportato nell'intake](../11-NUOVE-IDEE/CATALOGO_ALGORITMI_ON_DEVICE_2026-11-04.md). 23 tecniche analizzate; 10 nuovi comportamenti ammessi CAP-0151…0160, 13 riusi di capability già esistenti, senza duplicare funzioni.",
        "",
        "### Stato Golden e metodo probatorio",
        "",
        "E0 idea/specifica -> E1 sorgente SHA + file -> E2 test presenti (non necessariamente eseguiti) -> **E3** direct tests + exact-head CI per scope donor -> **E4** test piattaforma fisica/provider se applicabili -> **E5** consumer indipendente provato. Nessuna nuova CAP acquisisce E3/E5 semplicemente entrando nel catalogo.",
        "",
        "Goldens esistenti pertinenti: Hybrid Search (DRAFT, limited independent consumer), Local Rules (DRAFT), Explainable Recommendation (DRAFT), GPX (DRAFT, limited read-only consumer), Spatial (DRAFT), Sensor Fusion Android (DRAFT), Performance Fixture (DRAFT). **Non dichiararli universalmente COPY-READY.**",
        "",
        "Android limita sensor sampling e background activity: https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview. BatteryManager current/capacity dipende dal fuel gauge: https://developer.android.com/reference/android/os/BatteryManager. Per K-Means e TF-IDF sparse la stabilità del clustering va misurata: https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html.",
        "",
        "### Mappa 23/23: algoritmo → capability canonica",
        "",
        "| Intake | Algoritmo | CAP canoniche | Esito | Priorità di approfondimento |",
        "| --- | --- | --- | --- | --- |",
    ]
    for alg,caps in sorted(MAP.items()):
        mode="NUOVA CAP E0" if any(x["id"] in caps for x in DEFS) else "RIUSO CAP ESISTENTE"
        lines.append("| "+alg+" | "+original[alg][1]+" | "+", ".join(caps)+" | "+mode+" | "+original[alg][5]+" |")
    lines+=["","### Nuove 10 capability e facilità per tutte le app candidate",
        "","| CAP | Motore | Score globale | Facilità per app (euristica) | Dipendenze di ingresso |",
        "| --- | --- | ---: | --- | --- |"]
    for rec, spec in scores:
        lines.append("| "+rec["id"]+" "+rec["title"]+" | "+spec["engine"]+" | "+str(rec["score"])+" ("+rec["priority"]+") | "+", ".join(a+" "+str(v)+"%" for a,v in spec["apps"].items())+" | "+", ".join(spec["deps"])+" |")
    lines+=["","### Cinque famiglie di motori e cascata abilitata",
        "",
        "| Famiglia | Golden esistente o nuova candidatura | Port puramente algoritmico | CAP a valle |",
        "| --- | --- | --- | --- |"]
    for key,value in FAMILIES.items():
        lines.append("| "+key+" | "+value["mode"]+": "+value["core"]+" | "+value["needs"]+" | "+", ".join(value["downstream"])+" |")
    lines+=["","### Priorità di realizzazione, non approvazione prodotto",
        "",
        "1. **A — motore testo**: tokenizer multilingua, TF-IDF, fuzzy bounded; tests provenance / Unicode / retrieval privacy. E3 probabile con zero modelli; E5 da Notes o Wonderlog.",
        "2. **B — motore sensor signal**: EWMA/hysteresis pure; Physical/OEM required for E4. CAP-0158 sblocca qualità CAP-0057 e CAP-0062; non utilizzare sensor service background senza check OS.",
        "3. **C — scheduling & forecast**: riusare CAP-0001/0102 e Local Rules; regressione con campione minimo, opt-in. Nessun evento spostato automaticamente.",
        "4. **D — recommender / associations**: Apriori per catalogo ricette e Markov routine (solo consenso); l'output dev'essere spiegabile e privo di write impliciti.",
        "5. **E — geospatial**: RDP sopra GPX, DBSCAN/grid sopra Spatial Clustering, con coordinate valide, antimeridiano e origine inalterata.",
        "6. **F — DTW / embedding / modelli**: data collection etichettata e hardware baseline prima; non introdurre pacchetti pesanti nella base.",
        "",
        "### Metriche di certificazione (e non metriche inventate)",
        "",
        "- Correttezza: golden input-output vectors, proprietà determinate, tie-break stabile, output null su input non sufficienti, test negativi per ciclo/ACL/stale data.",
        "- CPU: median/p95 su N=0/1/100/500/5000, budget e memoria registrati; non assumere complessità lineare per TextRank/DBSCAN/DTW.",
        "- APK: baseline vs engine size diff, pacchetti transitivi, nessun file modello di default; Web e Android toolchain se usati come consumer.",
        "- Sicurezza: no data export, source-scoped permission filtering, cancellazione/undo e Privacy-by-design per suggerimenti. False positive/negative test sui sensori reali.",
        "- Prove: SHA 40 caratteri, file donor e test, URL CI exact SHA, licenza, compatibilità, data di revisione e successivo consumer indipendente.",
        "",
        "### Cosa NON è stato fatto da questa ammissione",
        "",
        "- Nessuna delle 10 CAP implementata nelle app, nessun nuovo Golden certificato o registro centrale promosso, nessun LLM/model download/API e nessun rilascio.",
        "- Non modificare gli score delle 150 capability esistenti per il semplice fatto di aver proposto un algoritmo. I 2 nuovi collegamenti CAP-0041 alle app ricette sono solo PROPOSTA.",
        "- I 10 kit sono al livello E0 (specifica e piano), non source-extracted. L'inventario di nuove implementazioni vive nel registro canonico e la vista è generata.",
        "",
        "Grafo machine-readable: [CATENE_MOTORI_ML_2026-11-04.json](CATENE_MOTORI_ML_2026-11-04.json).",
    ]
    save(CAT/REPORT,"\n".join(lines))
    changelog=ROOT/"09-AGGIORNAMENTI/CHANGELOG.md"
    x=changelog.read_text(encoding="utf-8")
    marker="# Changelog dell'archivio\n\n"
    if not x.startswith(marker):raise RuntimeError("changelog missing header")
    block="## 2026-11-04 — Ammissione completa ML23 a capability e Golden readiness\n- Convertite 10 idee ML26 in CAP-0151...0160, 60 file kit E0, mappa 23/23 con 13 riusi CAP, cross-app score e facilità per 160 CAP e "+str(assoc)+" associazioni.\n- Cinque engine family con dipendenze a catena, contratti E0->E5, baseline Core @6cbb3449; nessun Golden o runtime app falsamente promosso.\n- Vista e classifica rigenerate dal solo REGISTRO_CAPABILITY.json; catalogo storico ML conservato con collegamento.\n\n"
    save(changelog,x.replace(marker,marker+block,1))
    print("ML23_CAP_ADMITTED",len(records),"ASSOCIATIONS",assoc,"FAMILIES",len(FAMILIES),"KIT_FILES",len(DEFS)*6)
if __name__=="__main__":
    main()
