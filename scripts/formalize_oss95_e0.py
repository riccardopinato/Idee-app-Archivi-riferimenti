#!/usr/bin/env python3
"""Create 39 scoped E0 capability records and kits from audited OSS95 atlas.
Never approves product scope, donor code, licenses, implementation or release.
"""
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"12-CAPABILITY-E-IMPLEMENTAZIONI"
ATLAS=BASE/"AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json"
REG=BASE/"REGISTRO_CAPABILITY.json"
KITS=ROOT/"13-KIT-INTEGRAZIONE"
FACTORY="riccardopinato/App-Factory-Core@85ecbb19aeb02da1b9d04348e043f69bab77bcb9"
ATLAS_URL="https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/12-CAPABILITY-E-IMPLEMENTAZIONI/AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json"
HIGH={"N07","N08","N09","N16","N17","N19","N26","N32","N38","N40"}
MEDIUM={"N04","N05","N12","N21","N25","N28","N37"}
VALUE5={"N01","N02","N05","N09","N10","N11","N20","N24","N34"}
DOMAIN={
"N01":"editor","N02":"ricerca","N03":"organizzazione","N04":"automazioni","N05":"database",
"N06":"organizzazione","N07":"sincronizzazione","N08":"sicurezza","N09":"agenda",
"N10":"agenda","N11":"agenda","N12":"condivisione","N13":"pianificazione",
"N14":"organizzazione","N15":"pianificazione","N16":"analisi","N17":"analisi",
"N18":"editor","N19":"accessibilita","N20":"organizzazione","N21":"interoperabilita",
"N22":"widget","N23":"gamification","N24":"benessere","N25":"automazioni",
"N26":"sincronizzazione","N27":"editor","N28":"editoriale","N29":"ricerca",
"N30":"documenti","N31":"esperienza","N32":"sicurezza","N33":"interoperabilita",
"N34":"esperienza","N35":"analisi","N36":"documenti","N37":"android",
"N38":"voce","N40":"integrazione"}
DATE="2026-11-08"

def write(path,content):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(content.rstrip()+"\n",encoding="utf8")

def safe_score(key,apps):
    factors={
        "user_value":5 if key in VALUE5 else 4,
        "cross_app_reuse":4 if len(apps)>1 else 3,
        "feasibility":2 if key in HIGH else 3 if key in MEDIUM else 4,
        "evidence_strength":1,
        "risk_control":2 if key in HIGH else 3 if key in MEDIUM else 4
    }
    score=int(20*(0.35*factors["user_value"]+0.25*factors["cross_app_reuse"]+
        0.20*factors["feasibility"]+0.10*factors["evidence_strength"]+
        0.10*factors["risk_control"])+0.5)
    return factors,score,"P1" if score>=92 else "P2" if score>=79 else "P3"

def ease(key,app):
    n=34 if key in HIGH else 55 if key in MEDIUM else 70
    if app=="Agenda-per-Anna" and key in {"N09","N32","N37"}: n-=8
    if app=="CmdPocket" and key in {"N19","N40"}: n-=6
    if app=="Notes-Ecosistema" and key in {"N01","N06","N15","N25","N31"}: n+=12
    if app=="Work-Time-Keeper" and key in {"N16","N17","N35"}: n+=9
    return max(10,min(90,n))

def kits(rec,cand,atlas):
    cap=rec["id"]
    base=KITS/cap
    title=rec["title"]
    upstream=", ".join(rec["upstream_capabilities"])
    sources=cand["source_repositories"]
    links="\n".join("- https://github.com/"+n for n in sources)
    app_lines="\n".join("- "+a+": PROPOSTA; DA_VALUTARE; facilita euristica "+
        str(rec["integration_ease_percent"][a])+"%" for a in rec["app_states"])
    gate=rec["next_gate"]
    anti=rec["non_duplication_scope"]
    licence_lines=[]
    lookup={r["repo"]:r for r in atlas["repos"]}
    for n in sources:
        obj=lookup[n]
        details=obj.get("license_file_audit_20261108")
        license_name=(details["classification"]+": "+details["declared_terms"]
            if details else "REST "+obj["licence_repo_metadata"]+
            "; license per source file must be independently verified")
        licence_lines.append("- "+n+": "+license_name)
    kit={
      "README.md":f"# {cap} — {title}\n\nE0 / RIFERIMENTI_ACQUISITI: catalogato, NON approvato nella roadmap, NON riusabile come codice.\n\n{rec['description']}\n\n## App / stati\n{app_lines}\n\n## Contratto anti-duplicazione\n{anti}\nCAP correlate: {upstream}.\n\n## Repository di riferimento\n{links}\n\nFonte: {ATLAS_URL}\nFactory: {FACTORY}\n\n## Prossimo gate\n{gate}\n\nScore {rec['score']}/100 ({rec['priority']}), stima non misurata.\n\nSei file: README, SPECIFICHE, CODICE_RIFERIMENTO, INTEGRAZIONE_FLUTTER, LICENZE_E_DIPENDENZE, TEST_E_VALIDAZIONE.",
      "SPECIFICHE.md":f"# {cap} — Specifiche E0\n\n## Ambito\n{title}\n\n{anti}\n\n## Input\nEntita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.\n\n## Output\nPreview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.\n\n## Invarianti\nIdentita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.\n\n## Esclusioni\nNon sostituire {upstream}, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.\n\n## Acceptance gate\n{gate}",
      "CODICE_RIFERIMENTO.txt":f"CAP={cap}\nOSS95_WORKING_ID={cand['id']}\nEVIDENCE_GRADE=E0_SPEC_ONLY\nCODE_EXTRACTED=NO\nDART_READY=NO\nDONOR_CERTIFIED=NO\nAPP_IMPLEMENTED=NOT_VERIFIED\nSOURCE_ATLAS={ATLAS_URL}\nFACTORY={FACTORY}\nSOURCE_REPOSITORIES:\n{links}\n\nNo third-party code, weights or media has been copied. Require exact SHA/path, file license and direct E3 evidence before donor reuse.",
      "INTEGRAZIONE_FLUTTER.md":f"# {cap} — Piano integrazione Flutter\n\n1. Leggere Product Bible e roadmap attuali. Lo stato PROPOSTA non autorizza implementazione.\n2. Audit dell'owner canonico e delle CAP parent: {upstream}.\n3. Definire DTO, puro Dart adapter ove possibile; permessi/API native solo con gate esplicito.\n4. Filtrare ACL e revision prima di calcoli, export, notifiche o suggerimenti.\n5. Implementare preview, conferma, idempotenza, errori/undo e rollback.\n6. Test unitari e di integrazione; CI exact-head e QA reale device/provider se pertinente.\n7. Misurare differenza dimensione APK, RAM, batteria e latenza prima di adottare dipendenze.\n\nGate: {gate}",
      "LICENZE_E_DIPENDENZE.md":f"# {cap} — Licenze e dipendenze\n\nRicerca funzionale E0: nessuna licenza conferisce qui una autorizzazione automatica di riuso commerciale del codice.\n\n## Fonti e classificazione disponibile\n"+"\n".join(licence_lines)+"\n\nVerificare file, directory, commit, notice e transitive dependencies prima di ogni copia; GPL/AGPL/LGPL, source-available e asset con vincoli sono distinti. Non aggiungere dipendenze né token segreti in questo step.",
      "TEST_E_VALIDAZIONE.md":f"# {cap} — QA e validazione\n\n**ESITO: NON TESTATO NELL'APP / NO DONOR E3 / NO DEVICE / NO RELEASE.**\n\n- Input vuoto, malformato, ripetuto, 1/100/5000 record, caratteri Unicode.\n- Account switch, ACL revocata, source revision cambiata, cancellazione e restore.\n- Writer canonico unico, no-loss, offline, conflitti, retry, undo e rollback.\n- Timezone/DST, locale, date ricorrenti se applicabili.\n- FGS/microfono/schermo/NFC/tastiera con permesso esplicito e disattivazione dove richiesto.\n- Performance e footprint misurate prima/dopo sul consumer.\n- E1 richiede SHA + path, E2 test presente, E3 CI pertinente, E4 device, E5 consumer.\n\nGate: {gate}"
    }
    for file,text in kit.items():
        dest=base/file
        if dest.exists(): raise RuntimeError("Kit path already exists: "+str(dest))
        write(dest,text)

def main():
    atlas=json.loads(ATLAS.read_text(encoding="utf8"))
    data=json.loads(REG.read_text(encoding="utf8"))
    old=data["records"]
    if atlas["repositories_total"]!=95 or len(atlas["candidate_families"])!=39:
        raise RuntimeError("Unexpected atlas source count")
    formal=[x for x in old if "oss95_formalization_20261108" in x]
    if formal:
        if len(formal)==39 and len(old)==199:
            print("NO-OP: already formally admitted")
            return
        raise RuntimeError("Partial formalization detected; manual review required")
    if len(old)!=160 or old[-1]["id"]!="CAP-0160":
        raise RuntimeError("Unexpected old canonical registry")
    old_assoc=sum(len(x["app_states"]) for x in old)
    if old_assoc!=385: raise RuntimeError("Unexpected old app associations")
    valid={x["id"] for x in old}
    new=[]
    for i,c in enumerate(atlas["candidate_families"],161):
        key=c["id"].split("-")[-1]
        targets=[x.strip() for x in c["targets"].split(";") if x.strip()]
        if key not in DOMAIN or not targets: raise RuntimeError("Missing candidate metadata")
        factors,score,priority=safe_score(key,targets)
        counts=Counter(
          f["ref"] for row in atlas["repos"] if row["repo"] in c["source_repositories"]
          for f in row["feature_facets"] if f["kind"]=="CAP_EXISTENTE_MATCH_TEMATICO"
        )
        related=[n for n,count in counts.most_common(3)]
        if not related:
            fallback={
              "analisi":"CAP-0108","editor":"CAP-0093","ricerca":"CAP-0013",
              "organizzazione":"CAP-0096","sincronizzazione":"CAP-0100",
              "sicurezza":"CAP-0018","agenda":"CAP-0004",
              "condivisione":"CAP-0100","pianificazione":"CAP-0102",
              "accessibilita":"CAP-0084","interoperabilita":"CAP-0075",
              "widget":"CAP-0144","gamification":"CAP-0145","benessere":"CAP-0145",
              "automazioni":"CAP-0148","editoriale":"CAP-0042",
              "documenti":"CAP-0134","esperienza":"CAP-0025",
              "android":"CAP-0077","voce":"CAP-0031","integrazione":"CAP-0020",
              "database":"CAP-0096"
            }
            related=[fallback[DOMAIN[key]]]
        if any(x not in valid for x in related):
            raise RuntimeError("Related CAP not found: "+key)
        anti="Delta circoscritto a "+c["title"]+". Non duplicare la responsabilita delle CAP "+", ".join(related)+". Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice."
        rec={
          "id":f"CAP-{i:04d}","title":c["title"],"domain":DOMAIN[key],
          "score":score,"priority":priority,"scores":factors,
          "description":"Contratto E0 di ricerca: "+c["title"]+
            ". Input solo consentiti, preview e writer canonico dopo conferma; nessun motore parallelo.",
          "app_states":{x:"PROPOSTA" for x in targets},
          "source":{"type":"OSS95_README_E0","ref":ATLAS_URL},
          "next_gate":c["gate"],
          "reviewed_at":"2026-11-08","certification":"NOT_VERIFIED_IN_APP_E0",
          "source_evidence_grade":"E0_SPEC_ONLY",
          "integration_ease_percent":{x:ease(key,x) for x in targets},
          "app_product_decisions":{x:{"decision":"DA_VALUTARE","approved_roadmap":False,
                                    "origin":"OSS95_RESEARCH_FORMALIZATION"} for x in targets},
          "upstream_capabilities":related,"non_duplication_scope":anti,
          "oss95_formalization_20261108":{
            "working_id":c["id"],"original_verdict":c["verdict"],
            "reference_repositories":c["source_repositories"],
            "status":"E0_FORMALIZED_PROPOSAL_NOT_PRODUCT_ADOPTION",
            "factory":FACTORY,"scoring":"FORMULA_WITH_EVIDENCE_STRENGTH_1",
            "integration_ease":"RISK_BASED_HEURISTIC_NOT_PROBABILITY",
            "product_approved":False,"app_implementation_verified":False,
            "donor_code_reuse_cleared":False
          }
        }
        kits(rec,c,atlas)
        new.append(rec)
    if len(new)!=39: raise RuntimeError("Wrong new CAP count")
    data["records"].extend(new)
    added=sum(len(x["app_states"]) for x in new)
    history=data["oss95_research_intake"]
    indexed={r["oss95_formalization_20261108"]["working_id"]:r["id"] for r in new}
    for item in history["pending_candidate_families"]:
        item["formalized_cap_id"]=indexed[item["working_id"]]
        item["formalization"]="ADMITTED_E0 / APP_PRODUCT_DA_VALUTARE"
    history["formalization_20261108"]={"date":"2026-11-08","admitted":39,
      "range":["CAP-0161","CAP-0199"],"new_assoc":added,
      "total_cap":len(data["records"]),"total_assoc":old_assoc+added,
      "meaning":"Research contracts; does not approve products or certify implementations"}
    data["updated_at"]="2026-11-08"
    write(REG,json.dumps(data,indent=2,ensure_ascii=False))
    index=BASE/"README.md"
    content=index.read_text(encoding="utf8")
    header="# Catalogo centrale capability — App Factory\n"
    if not content.startswith(header): raise RuntimeError("Unexpected README")
    section="\n## 08/11/2026 — Formalizzate 39 nuove CAP E0 OSS95\n\n"
    section+=f"**{len(data['records'])} CAP, {old_assoc+added} associazioni app–CAP**. "
    section+="Aggiunte CAP-0161..CAP-0199 come PROPOSTA E0 e decisione per app DA_VALUTARE, non funzionalita implementate. "
    section+="Ogni CAP ha sei file kit, donor README OSS e controllo anti-duplicato. "
    section+="Le 160 CAP e 385 associazioni precedenti restano preservate; nessuna roadmap o app mutata.\n\n"
    content=header+section+content[len(header):]
    content=content.replace("**160 capability individuali, 48 app/idee beneficiarie e 385 associazioni app-capability**",
       f"**{len(data['records'])} capability individuali, 48 app/idee beneficiarie e {old_assoc+added} associazioni app-capability**")
    content=content.replace("[160 kit tecnici","[199 kit tecnici")
    write(index,content)
    changelog=ROOT/"09-AGGIORNAMENTI"/"CHANGELOG.md"
    oldtext=changelog.read_text(encoding="utf8")
    top,rest=oldtext.split("\n",1)
    changes=f"\n## 2026-11-08 — Formalizzazione OSS95: 39 CAP E0\n\n- CAP-0161..CAP-0199: 39 contratti E0, {added} app-associazioni in PROPOSTA / DA_VALUTARE; {len(data['records'])} CAP e {old_assoc+added} associazioni totali.\n- Nessuna implementazione o donor certificato; sei file kit per ogni CAP, riscontro non duplicazione e stime euristiche.\n- Rigenerate schede, ranking e code tramite scripts/build_catalog.py e status generator.\n\n"
    write(changelog,top+changes+rest)
    print("FORMALIZED=39 TOTAL_CAP="+str(len(data["records"]))+
          " NEW_ASSOC="+str(added)+" TOTAL_ASSOC="+str(old_assoc+added))

if __name__=="__main__":
    main()
