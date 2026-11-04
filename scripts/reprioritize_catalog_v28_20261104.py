#!/usr/bin/env python3
"""Evidence-gated, idempotent full CAP/consumer rescoring, Factory Golden v28."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "12-CAPABILITY-E-IMPLEMENTAZIONI"
KIT = ROOT / "13-KIT-INTEGRAZIONE"
FILE = CAT / "REGISTRO_CAPABILITY.json"
DATE = "2026-11-04"
FACTORY = "riccardopinato/App-Factory-Core@cea0a6d9ecbf17aabd1f7df177043fd863b3f754"
STAMP = "v28-full-scope-20261104"
GH = "https://github.com/riccardopinato/"
CORE = GH + "App-Factory-Core/"
NOTES = GH + "Notes-Ecosistema/"
ANNA = GH + "Agenda-per-Anna/"
IDEAS = GH + "Idee-app-Archivi-riferimenti/"

# Regrade only changed, scoped evidence. Factor: target value, why, citation.
FACTORS = {
 "CAP-0029": ({"feasibility":4}, "Ink/viewport pure reference now exists, but consumer pen/device remains pending", CORE+"blob/main/golden/ui/GOLDEN_INFINITE_CANVAS_INK_ENGINE_v1_DRAFT.txt"),
 "CAP-0032": ({"feasibility":3,"evidence_strength":4}, "Notes semantic retrieval and independent limited Wonderlog hybrid consumer verified by source", GH+"Wonderlog/pull/21"),
 "CAP-0093": ({"evidence_strength":4}, "Notes canonical NoteToChecklist source implementation; full nested workflow not proved", NOTES+"blob/main/flutter_app/lib/src/domain/note_to_checklist.dart"),
 "CAP-0096": ({"evidence_strength":4}, "Notes explicit blocker/cycle source; recurrence/editing parity incomplete", NOTES+"pull/53"),
 "CAP-0098": ({"feasibility":4}, "Knowledge Graph and canvas reduce effort, not complete derived mind map", NOTES+"blob/main/flutter_app/lib/src/domain/knowledge_graph.dart"),
 "CAP-0112": ({"evidence_strength":4}, "Guided source-based Q/A exists; scheduled repetition and PDF OCR not fully certified", NOTES+"pull/52"),
 "CAP-0116": ({"feasibility":3,"risk_control":3}, "Similarity/duplicate Golden still design-only; safe personal-note merge not proven", CORE+"blob/main/golden/data/GOLDEN_DUPLICATE_SIMILARITY_REVIEW_GATE_v1_DRAFT.txt"),
 "CAP-0134": ({"feasibility":3,"evidence_strength":3,"risk_control":3}, "DocRex 3-class scope lacks Italian mobile validation despite former 98 score", IDEAS+"blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md"),
 "CAP-0142": ({"evidence_strength":2}, "Anna future-letter source merged but shared capsules still not proven", ANNA+"pull/218"),
 "CAP-0144": ({"evidence_strength":3}, "Anna private home-widget masking/source tested, OEM physical pending", ANNA+"pull/216"),
}
# Application-specific ease changes; no universal Golden promotion.
SPEC = {
 "CAP-0017":{"Notes-Ecosistema":2},
 "CAP-0020":{"Agenda-per-Anna":-2,"Wonderlog":-2,"Notes-Ecosistema":-2,"TrailPath":-2},
 "CAP-0028":{"Notes-Ecosistema":2},
 "CAP-0029":{"Notes-Ecosistema":6},
 "CAP-0032":{"Notes-Ecosistema":7,"TasteAI":2,"Agenda-per-Anna":2},
 "CAP-0040":{"Android-Omni-Cleaner":-3,"Wonderlog":-3,"app-fotografia":-3},
 "CAP-0042":{"World-Days":5,"In-Cucina-con-gli-Anime":2},
 "CAP-0067":{"Battery_Guard":3,"AppLab":2},
 "CAP-0068":{"CamperBoss":2},
 "CAP-0071":{"World-Days":4,"CamperBoss":2,"Notes-Ecosistema":2},
 "CAP-0077":{"Battery_Guard":2},
 "CAP-0093":{"Notes-Ecosistema":2},
 "CAP-0094":{"Notes-Ecosistema":2},
 "CAP-0096":{"Notes-Ecosistema":4},
 "CAP-0098":{"Notes-Ecosistema":5},
 "CAP-0102":{"Agenda-per-Anna":6},
 "CAP-0103":{"Notes-Ecosistema":6},
 "CAP-0106":{"Notes-Ecosistema":6},
 "CAP-0112":{"Notes-Ecosistema":6},
 "CAP-0116":{"Notes-Ecosistema":-8},
 "CAP-0134":{"Notes-Ecosistema":-12,"Agenda-per-Anna":-8,"PDF-Unifier":-11},
 "CAP-0142":{"Agenda-per-Anna":7},
 "CAP-0144":{"Agenda-per-Anna":3,"World-Days":2},
}
REASON = {
 "CAP-0017":"Archived/deleted source gating now merged in Notes #43; full lifecycle not certified",
 "CAP-0020":"Cross-app paired installed-device transport has no end-to-end physical proof",
 "CAP-0028":"Existing Note/Whiteboard graph and bounded ink references reduce geometry work",
 "CAP-0029":"Golden ink reference and Notes canvas core present, device stylus pending",
 "CAP-0032":"Limited Notes/Wonderlog local retrieval reference; not a trained model or hardware guarantee",
 "CAP-0040":"Similarity gate remains DRAFT design and destructive actions need proof",
 "CAP-0042":"World-Days multilingual editorial catalog and reusable editorial reference",
 "CAP-0067":"Signed Anna +122 artifact now exists but independent app release remains gated",
 "CAP-0068":"Factory exact-source fixtures improve QA reuse, not device verification",
 "CAP-0071":"Versioned offline packs and consumer source available, actual device delivery distinct",
 "CAP-0077":"Scoped permission/service health donor contracts; native OEM validation pending",
 "CAP-0093":"Canonical Notes checklist conversion exists; full hierarchy not yet proven",
 "CAP-0094":"Existing project/task workspace reduces canvas-to-task adapter effort",
 "CAP-0096":"Explicit blocker/cycle notes now in main, recurrence and edge editing pending",
 "CAP-0098":"Existing derived Knowledge Graph reduces mind-map work, not a finished UX",
 "CAP-0102":"Anna assisted replanning source #217 merged; full alternative plans pending",
 "CAP-0103":"Notes dependency diagnostics merged #53, no user-facing edge editing yet",
 "CAP-0106":"Notes workload/WIP merged #45, meeting heatmap unimplemented",
 "CAP-0112":"Notes Guided Study #52 merged, OCR provenance and SRS remain",
 "CAP-0116":"Golden similarity review still design-only, safe merge/undo absent",
 "CAP-0134":"No supported Italian Android benchmark for constrained 3-class DocRex",
 "CAP-0142":"Anna personal future letters merged; shared capsule still pending",
 "CAP-0144":"Anna/World-Days widget source and privacy gating, device QA pending",
}
PARTIAL = {
 ("CAP-0032","Notes-Ecosistema"):("flutter_app/lib/src/domain/semantic_embeddings.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","local deterministic search, not external multilingual embeddings"),
 ("CAP-0093","Notes-Ecosistema"):("flutter_app/lib/src/domain/note_to_checklist.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","selected checklist items become one canonical task"),
 ("CAP-0096","Notes-Ecosistema"):("flutter_app/lib/src/domain/project_dependency_review.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","read-only dependency cycle checks, no recurrence"),
 ("CAP-0098","Notes-Ecosistema"):("flutter_app/lib/src/domain/knowledge_graph.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","derived knowledge graph, not complete mindmap"),
 ("CAP-0103","Notes-Ecosistema"):("flutter_app/lib/src/domain/project_dependency_review.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","read-only dependency diagnostics"),
 ("CAP-0106","Notes-Ecosistema"):("flutter_app/lib/src/domain/project_workload_guard.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","workload budget, no full meeting heatmap"),
 ("CAP-0112","Notes-Ecosistema"):("flutter_app/lib/src/domain/guided_study.dart","cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7","authored Q/A, no certified PDF OCR/SRS"),
 ("CAP-0042","World-Days"):("lib/domain/observance_detail_facts.dart","bb662cb21506b6157658f43070c2059c960637b5","sourced six-locale stories; no Store claim"),
 ("CAP-0102","Agenda-per-Anna"):("lib/src/quick_wins2.dart","ab5360b78187a643e2b101be21e6951441406059","assisted rescheduling source, not an alternative-plan optimizer"),
 ("CAP-0142","Agenda-per-Anna"):("lib/src/diary/diary_memories.dart","ab5360b78187a643e2b101be21e6951441406059","personal future letters, not shared capsules"),
 ("CAP-0144","Agenda-per-Anna"):("lib/src/home_widget_bridge.dart","ab5360b78187a643e2b101be21e6951441406059","privacy-masked launcher bridge; hardware not validated"),
 ("CAP-0032","Wonderlog"):("flutter/lib/features/search/domain/hybrid_search.dart","b4840e845336fb6df6f823986b8cf0a731e66a35","independent hybrid search consumer without persisted ANN"),
}
NEW = [
 ("CAP-0148","Smart Inbox verificabile da fonte ad azione canonica","organizzazione", [5,4,4,4,4],80, NOTES+"issues/46","Suggerimento da fonte con motivazione, preview, consenso, writer Task/Tag/Project canonico, verifica ACL e revisione, undo dove supportato; niente auto-write."),
 ("CAP-0149","Interoperabilita JSON Canvas v1 con report di perdita","canvas",[5,4,3,3,4],67,"https://github.com/obsidianmd/jsoncanvas/blob/main/spec/1.0.md","Import/export esplicito nodi e archi JSON Canvas, con report lossiness di strokes, media, metadati e originali preservati."),
 ("CAP-0150","Daily Note Hub derivato opzionale","organizzazione",[4,3,4,2,4],82,NOTES+"issues/50","Vista opt-in costruita da note, task e planner canonici, senza nuovo database o sincronizzazione implicita."),
]
HEADS = {
 "Agenda-per-Anna":"ab5360b78187a643e2b101be21e6951441406059",
 "App-Factory-Core":"cea0a6d9ecbf17aabd1f7df177043fd863b3f754",
 "CamperBoss":"ae30d08f23aa7e8c835927bc98127f25662d2f6a",
 "Idee-app-Archivi-riferimenti":"9b7c470a8b4392c679a483d6ae30e9be354057cd",
 "Notes-Ecosistema":"cd3e28f3a22bbd9cd25bf8c6b76b44dc66bdb4f7",
 "Wonderlog":"b4840e845336fb6df6f823986b8cf0a731e66a35",
 "World-Days":"bb662cb21506b6157658f43070c2059c960637b5",
}

def score(s):
    return int(20*(.35*s["user_value"]+.25*s["cross_app_reuse"]+
                   .20*s["feasibility"]+.10*s["evidence_strength"]+
                   .10*s["risk_control"])+.5)

def priority(v):
    return "P1" if v>=92 else "P2" if v>=79 else "P3"

def save(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")

def csvsave(name, rows, fields):
    with (CAT/name).open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    data=json.loads(FILE.read_text(encoding="utf-8"))
    if data.get("score_audit_revision")==STAMP:
        print("Already audited, immutable scores; no second increment.");return
    records=data["records"]
    if len(records)!=147 or sum(len(r["app_states"]) for r in records)!=342:
        raise SystemExit("Snapshot mismatch: explicit baseline recheck required")
    inventory_path=CAT/"SOURCE_INVENTORY.json"
    inventory=json.loads(inventory_path.read_text(encoding="utf-8"))
    known={x["name"] for x in inventory["repositories"]}
    if len(known)!=31:raise SystemExit("Unexpected inventory size")
    for x in inventory["repositories"]:
        x["head_sha"]=HEADS.get(x["name"],x["head_sha"])
        x["head_observed_at"]=DATE
    save(inventory_path,json.dumps(inventory,ensure_ascii=False,indent=2)+"\n")

    oldranks={x["id"]:i for i,x in enumerate(sorted(records,key=lambda x:(-x["score"],x["id"])),1)}
    one=next(r for r in records if r["id"]=="CAP-0032")
    one["app_states"]["Wonderlog"]="SOURCE_REPORTED"
    one["integration_ease_percent"]["Wonderlog"]=64
    priority_rows=[];ease_rows=[];changed_status=[]
    for r in records:
        id=r["id"];old_score=r["score"];old_priority=r["priority"]
        old_factors=dict(r["scores"]);rule=FACTORS.get(id)
        if rule:r["scores"].update(rule[0])
        r["score"]=score(r["scores"]);r["priority"]=priority(r["score"])
        r["original_reviewed_at"]=r.get("original_reviewed_at",r["reviewed_at"])
        r["reviewed_at"]=DATE
        rationale=rule[1] if rule else "RETAIN: no new feature-specific evidence sufficient for numerical score change"
        evidence=rule[2] if rule else ""
        r["priority_audit_v28"]={"before":old_score,"after":r["score"],
                                 "before_factors":old_factors,"rationale":rationale,
                                 "source":evidence,"factory":FACTORY}
        priority_rows.append(dict(id=id,title=r["title"],before=old_score,after=r["score"],
                                  delta=r["score"]-old_score,old_priority=old_priority,
                                  new_priority=r["priority"],rationale=rationale,source=evidence))
        for app in list(r["app_states"]):
            old_ease=r["integration_ease_percent"][app];old_status=r["app_states"][app]
            delta=SPEC.get(id,{}).get(app,0)
            penalty=-4 if app not in known and old_status=="PROPOSTA" else 0
            new_ease=max(0,min(100,old_ease+delta+penalty))
            r["integration_ease_percent"][app]=new_ease
            why=[]
            if delta:why.append(REASON[id])
            if penalty:why.append("No app source listed in 31-repo inventory; add conservative bootstrap/verification friction")
            if not why:why.append("RETAIN: no new exact app source/GOLDEN scope proves a different effort")
            cite=(rule[2] if rule else "") if delta else ""
            if (id,app) in PARTIAL:
                path,sha,scope=PARTIAL[(id,app)]
                if r["app_states"][app] not in {"CI_VERIFIED","DEVICE_VERIFIED","RELEASE"}:
                    r["app_states"][app]="SOURCE_REPORTED"
                r.setdefault("partial_source_evidence_v28",{})[app]={
                    "source_sha":sha,"source_path":path,"scope":scope,
                    "url":GH+app+"/blob/"+sha+"/"+path,
                    "full_capability_complete":False,"device_pass":False}
                changed_status.append((id,app,old_status,r["app_states"][app]))
            r.setdefault("integration_ease_audit_v28",{})[app]={
                "before":old_ease,"after":new_ease,"rationale":"; ".join(why),
                "source":cite,"not_success_probability":True}
            ease_rows.append(dict(id=id,app=app,before=old_ease,after=new_ease,
                                  delta=new_ease-old_ease,status_before=old_status,
                                  status_after=r["app_states"][app],rationale="; ".join(why),source=cite))
    for id,title,domain,factors,ease,source,description in NEW:
        keys=["user_value","cross_app_reuse","feasibility","evidence_strength","risk_control"]
        s=dict(zip(keys,factors));v=score(s)
        rec=dict(id=id,title=title,domain=domain,score=v,priority=priority(v),
                 scores=s,description=description,app_states={"Notes-Ecosistema":"PROPOSTA"},
                 source={"type":"SOURCE_SCOPED_FOUR_SITE_AUDIT","ref":source},
                 next_gate="Confirm Product Bible; scoped source, permission/revision checks, no silent write, exact-head tests, physical gate where relevant",
                 reviewed_at=DATE,certification="NOT_VERIFIED_BY_THIS_AUDIT",
                 integration_ease_percent={"Notes-Ecosistema":ease},
                 priority_audit_v28={"before":None,"after":v,"rationale":"NEW distinct scoped CAP","source":source,"factory":FACTORY},
                 integration_ease_audit_v28={"Notes-Ecosistema":{"before":None,"after":ease,"rationale":"NEW proposal; existing canonical Notes adapters lower cost; remaining full workflow not built","source":source,"not_success_probability":True}})
        records.append(rec)
        priority_rows.append(dict(id=id,title=title,before="",after=v,delta="",
                                  old_priority="",new_priority=rec["priority"],
                                  rationale="New distinct source-scoped CAP",source=source))
        ease_rows.append(dict(id=id,app="Notes-Ecosistema",before="",after=ease,delta="",
                              status_before="",status_after="PROPOSTA",rationale="New candidate scope, not implemented",source=source))
        d=KIT/id;d.mkdir(parents=True,exist_ok=True)
        contents={
          "README.md":f"# {id} — {title}\n\nRIFERIMENTI_ACQUISITI / SOLO PROPOSTA; non copy-ready.\n\n{description}\n\nFonte: {source}\n\nNotes: PROPOSTA; facilita stimata {ease}%.\n\nGate: {rec['next_gate']}\n",
          "SPECIFICHE.md":f"# Specifiche candidate {id}\n\n{description}\n\nRiutilizzare dati e permessi canonici, nessun secondo archivio, preview prima di commit e limiti di conversione visibili.\n",
          "CODICE_RIFERIMENTO.txt":f"CAP: {id}\nFONTE: {source}\nCODICE_ACQUISITO: NO\nDONOR_E3: NON CERTIFICATO\nAPP_NOTES_QA: NON VERIFICATO\n",
          "INTEGRAZIONE_FLUTTER.md":f"# Integrazione Flutter {id}\n\n1. Audit del modello Notes e dei permessi effettivi.\n2. Adapter su sorgenti canoniche, niente copia non licenziata.\n3. Preview con consenso, source revision check e nessuna scrittura implicita.\n4. CI Flutter/Web + device se necessario; nessuna promozione automatica.\n",
          "LICENZE_E_DIPENDENZE.md":f"# Provenienza {id}\n\nFonte {source}. Nessun codice OSS copiato e nessuna dipendenza nuova approvata. Licenze e attribution per ogni futura implementazione da validare. Golden DRAFT non equivale a runtime certificato.\n",
          "TEST_E_VALIDAZIONE.md":f"# Test di accettazione {id}\n\n- Source deleted/archived/stale, duplicate IDs, permessi account/shared-space.\n- Preview/cancel/confirm, no auto-write, backup, undo e export-loss report ove pertinenti.\n- Fonti, localizzazione, offline, regressioni e CI exact-head; device QA separata.\n\nESITO: NON TESTATO, SOLO CONTRATTO.\n"}
        for name,body in contents.items():save(d/name,body)

    data["updated_at"]=DATE;data["factory_baseline"]=FACTORY
    data["score_audit_revision"]=STAMP
    data["score_audit_method"]="score = round_half_up(20*(.35 user+.25 reuse+.20 feasibility+.10 evidence+.10 risk)); P1>=92 P2>=79; per-app ease is heuristic, not a success chance"
    save(FILE,json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    ranks={x["id"]:i for i,x in enumerate(sorted(records,key=lambda x:(-x["score"],x["id"])),1)}
    for row in priority_rows:
        row["old_rank"]=oldranks.get(row["id"],"");row["new_rank"]=ranks[row["id"]]
    csvsave("AUDIT_PRIORITA_TUTTE_CAP_V28_2026-11-04.csv",priority_rows,
            ["id","title","before","after","delta","old_priority","new_priority","old_rank","new_rank","rationale","source"])
    csvsave("AUDIT_FACILITA_TUTTE_APP_V28_2026-11-04.csv",ease_rows,
            ["id","app","before","after","delta","status_before","status_after","rationale","source"])
    sc=[x for x in priority_rows if isinstance(x["delta"],int) and x["delta"]]
    ec=[x for x in ease_rows if isinstance(x["delta"],int) and x["delta"]]
    lines=["# Audit integrale priorita e facilita — Golden v28 / 04-11-2026","",
      "Baseline: "+FACTORY, "",
      f"**Prima:** 147 CAP, 342 associazioni, 48 app. **Dopo:** {len(records)} CAP, {len(ease_rows)} associazioni, 48 app.",
      f"Riviste tutte le 147 capability preesistenti e 342 stime di facilita preesistenti. Cambi reali: {len(sc)} score, {len(ec)} ease; {len(changed_status)} osservazioni di source parziale; 3 CAP nuove e un nuovo consumer parziale Wonderlog.",
      "",
      "La priorita globale segue la formula storica a cinque fattori; la facilita per singola app e una stima ingegneristica, non probabilita di successo, retention o business case.",
      "31/31 repository nell'inventario controllati tramite SHA; gli altri nomi app non hanno source osservata in questo inventario, non e prova che non esista un repo.",
      "I Golden DRAFT (Hybrid Search limited, Ink, Rules, Explainable Recommendations, Duplicate Gate) non sono promossi a certificazione. CivilDate copy-ready e circoscritto alla pura aritmetica civile. Niente nuovi billing/cloud/AI o release.",
      "",
      "## Movimenti score", "",
      "| CAP | Prima | Dopo | Motivo |","| --- | ---: | ---: | --- |"]
    for r in sorted(sc,key=lambda z:(-abs(z["delta"]),z["id"])):
        lines.append(f"| {r['id']} | {r['before']} | {r['after']} | {r['rationale']} |")
    lines+=["", "## Movimenti di facilita per app (prime 50 variazioni)", "",
            "| CAP / app | Prima | Dopo | Motivo |","| --- | ---: | ---: | --- |"]
    for r in sorted(ec,key=lambda z:(-abs(z["delta"]),z["id"],z["app"]))[:50]:
        lines.append(f"| {r['id']} / {r['app']} | {r['before']} | {r['after']} | {r['rationale']} |")
    lines+=["","## Copertura tutte le app","","| App | Associazioni | Facilita variata |","| --- | ---: | ---: |"]
    for app in sorted({a for r in records for a in r["app_states"]}):
        lines.append(f"| {app} | {sum(app in r['app_states'] for r in records)} | {sum(x['app']==app for x in ec)} |")
    lines+=["","## Audit trail completo",
      "- CSV CAP: [tutti i punteggi e ranking](AUDIT_PRIORITA_TUTTE_CAP_V28_2026-11-04.csv).",
      "- CSV associazioni: [tutte le facilita per app](AUDIT_FACILITA_TUTTE_APP_V28_2026-11-04.csv).",
      "- Ogni record CAP conserva fattori ed evidenza in priority_audit_v28; ogni associazione conserva valori prima/dopo e ragione in integration_ease_audit_v28.",
      "- SOURCE_REPORTED rappresenta solo delta implementativo: non promuovere la CAP intera a Già integrati senza prova puntuale full-scope.",
      "- Lo score e relativo al catalogo, non decide automaticamente la roadmap prodotto. CI exact-head e fisico sono gate indipendenti.",""]
    save(CAT/"AUDIT_RIPRIORITIZZAZIONE_GOLDEN_V28_2026-11-04.md","\n".join(lines))
    for id in sorted(set([x["id"] for x in sc+ec])):
        path=KIT/id/"README.md";txt=path.read_text(encoding="utf-8")
        rec=next(r for r in records if r["id"]==id)
        if "## Re-audit v28 — 04/11/2026" not in txt:
            addition=["","## Re-audit v28 — 04/11/2026",
              f"Priorita corrente {rec['priority']} {rec['score']}/100 (non release priority)."]
            if id in FACTORS:addition.append("Motivo score: "+FACTORS[id][1]+".")
            for x in ec:
                if x["id"]==id:addition.append(f"Facilita {x['app']}: {x['before']}% -> {x['after']}%. {x['rationale']}.")
            addition.append("Riferimento: audit globale Factory Golden v28 nella cartella 12-CAPABILITY-E-IMPLEMENTAZIONI.")
            save(path,txt.rstrip()+"\n"+"\n".join(addition)+"\n")
    idx=KIT/"INDICE.md";txt=idx.read_text(encoding="utf-8")
    if not txt.startswith("# Indice — 147 kit"):raise SystemExit("Kit index base drift")
    txt=txt.replace("# Indice — 147 kit","# Indice — 150 kit",1)
    for r in records[-3:]:
        txt+=f"| {r['id']} | {r['title']} | Notes-Ecosistema | [Apri]({r['id']}/README.md) |\n"
    save(idx,txt)
    kr=KIT/"README.md";txt=kr.read_text(encoding="utf-8")
    txt=txt.replace("**147 cartelle kit","**150 cartelle kit",1)
    save(kr,txt+"\n## Audit Golden v28 04/11/2026\n\nTre nuovi kit CAP-0148...0150 sono soltanto proposte. Rapporto completo in cartella 12-CAPABILITY-E-IMPLEMENTAZIONI.\n")
    cr=CAT/"README.md";txt=cr.read_text(encoding="utf-8")
    txt=txt.replace("**147 capability individuali, 48 app/idee beneficiarie e 342 associazioni app-capability**, stato catalogo 01/11/2026","**150 capability individuali, 48 app/idee beneficiarie e 346 associazioni app-capability**, ri-audit 04/11/2026")
    txt=txt.replace("[147 kit tecnici]","[150 kit tecnici]")
    save(cr,txt+"\n## Score Golden v28 — 04/11/2026\n\n[Rapporto audit completo](AUDIT_RIPRIORITIZZAZIONE_GOLDEN_V28_2026-11-04.md); due CSV includono ogni CAP e associazione, anche invariata.\n")
    main_readme=ROOT/"README.md";txt=main_readme.read_text(encoding="utf-8")
    txt=txt.replace("48 app/342 associazioni","48 app/346 associazioni")
    txt=txt.replace("[147 kit di integrazione]","[150 kit di integrazione]")
    save(main_readme,txt+"\n## Re-audit Factory Golden v28 — 04/11/2026\n\n[150 CAP e 346 associazioni](12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_RIPRIORITIZZAZIONE_GOLDEN_V28_2026-11-04.md); numeri unchanged quando manca nuova evidenza.\n")
    log=ROOT/"09-AGGIORNAMENTI"/"CHANGELOG.md";txt=log.read_text(encoding="utf-8")
    marker="# Changelog dell'archivio\n\n"
    if not txt.startswith(marker):raise SystemExit("Changelog header drift")
    note=f"## {DATE} — Audit integrale Golden v28, tutte le app\n- Revisione 147 CAP, 342 associazioni storiche e 31 repository reali, con {len(sc)} score e {len(ec)} valori facilita ricalibrati sulla nuova evidenza; altri valori conservati.\n- Tre CAP nuove (0148 Smart Inbox, 0149 JSON Canvas, 0150 Daily Hub), un consumer parziale Wonderlog, kit e indici rigenerati.\n- Provenienza SHA e delta conservati nel registro e nei CSV; nessuna nuova certificazione device/Store/Golden.\n\n"
    save(log,txt.replace(marker,marker+note,1))
    print(f"AUDIT_OK: {len(records)} CAP; {len(ease_rows)} app associations; {len(sc)} scores and {len(ec)} ease movements; {len(changed_status)} partial implementations")

if __name__=="__main__":
    main()
