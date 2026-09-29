"""Materialize the authorized Track A contract through shared owners only."""
from pathlib import Path
import json,html,yaml
ROOT=Path(__file__).resolve().parents[1]
contract='prototype-specs/TRACK_A_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'
c=json.loads((ROOT/contract).read_text(encoding='utf-8'))
assert c['freeze_authority']['decision']=='TRACK_A_REVISION_1_FROZEN_FOR_PROTOTYPE_IMPLEMENTATION'
items=[('components','BLK-ASSESSMENT-BUNDLE-01','block','learning-blocks/assessment-bundle',{'engine':'assessment-bundle.js'}),('components','INT-READINESS-REVIEW-01','interaction','interactions/readiness-review',{'engine':'readiness-review.js','model':'model.js'}),('patterns','IP-READINESS-GATE-01','pattern','docs/patterns/readiness-gate',{})]
for reg,id,kind,path,extra in items:
 owner=next(o for o in c['objects']['proposed_candidates'] if o['id']==id)
 folder=ROOT/path;folder.mkdir(parents=True,exist_ok=True)
 m=dict(id=id,version='0.3.0-alpha',status='PROTOTYPE',type=kind,ownership=owner['responsibility'],frozen_contract=contract,**extra)
 (folder/'manifest.yaml').write_text(yaml.safe_dump(m,sort_keys=False),encoding='utf-8')
 (folder/'README.md').write_text(f"# {id}\n\nPROTOTYPE only. {owner['responsibility']}\n\n"+c['freeze_authority']['boundary']+'\n\nEvidence dossier → criterion mapping → gaps → recommendation → simulated consequence → versioned clarification → explicit reconsideration. Storage is owned exclusively by the unchanged shared service.\n',encoding='utf-8')
 f=ROOT/f'registries/{reg}.json';r=json.loads(f.read_text(encoding='utf-8'));r['objects']=[o for o in r['objects'] if o['id']!=id]+[dict(id=id,version='0.3.0-alpha',status='PROTOTYPE',type=kind,implementation=path+'/manifest.yaml')];f.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
for reg,id,path in [('compositions','CMP-EVIDENCE-DECISION-01','compositions/evidence-decision'),('templates','TPL-SCENARIO-01','templates/scenario')]:
 f=ROOT/f'registries/{reg}.json';r=json.loads(f.read_text(encoding='utf-8'));o=next(o for o in r['objects'] if o['id']==id);o['variants']=list(dict.fromkeys(o.get('variants',[])+['readiness-review']));f.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 f=ROOT/path/'manifest.yaml';m=yaml.safe_load(f.read_text(encoding='utf-8'));variants=m.setdefault('variants',[])
 if not any((v.get('id') if isinstance(v,dict) else v)=='readiness-review' for v in variants):variants.append(dict(id='readiness-review',status='PROTOTYPE',opt_in=True,ownership='Arrangement only',compatible_interactions=['INT-READINESS-REVIEW-01'],compatibility='All existing defaults and variants unchanged'))
 approved=next(v for v in variants if isinstance(v,dict) and v.get('id')=='readiness-review')
 if reg=='templates':approved.update(implementation={'arrangement':'readiness-review.js'},required_regions=['criteria','dossier','recommendation','history','retention'])
 else:approved.update(implementation={'css':'readiness-review.css'})
 f.write_text(yaml.safe_dump(m,sort_keys=False),encoding='utf-8')
for reg in ['components','patterns','compositions','templates']:
 r=json.loads((ROOT/f'registries/{reg}.json').read_text(encoding='utf-8'));(ROOT/f'registries/{reg}.yaml').write_text(yaml.safe_dump(r,sort_keys=False),encoding='utf-8')
folder=ROOT/'golden-references/TRACK-A';folder.mkdir(exist_ok=True)
spec=dict(id='TRACK-A',system_version='0.3-alpha',build_mode='CONSTRAINED_BUILD',instructional_pattern='IP-READINESS-GATE-01',template={'id':'TPL-SCENARIO-01','variant':'readiness-review'},composition='CMP-EVIDENCE-DECISION-01',composition_variant='readiness-review',components=c['objects']['reuse']+['BLK-ASSESSMENT-BUNDLE-01','INT-READINESS-REVIEW-01'],completion=c['completion']['expression'],prototype_contract='../../'+contract,experience_differentiation_brief=c['experience_differentiation_brief'],local_css_allowed=False,candidate_objects_status='PROTOTYPE')
spec['authority']={'LOCKED':['Frozen content, limits and assessment boundary; unchanged existing consumers and service'],'CONSTRAINED':['Approved PROTOTYPE owners and opt-in readiness-review variants'],'EXPLORATORY':['None during this frozen build']}
(folder/'spec.yaml').write_text(yaml.safe_dump(spec,sort_keys=False),encoding='utf-8')
styles=['tokens/tokens.css','foundations/base.css','foundations/accessibility.css','foundations/motion.css','shell/course-shell.css','ui/button/button.css','compositions/evidence-decision/readiness-review.css']
links='\n'.join(f'<link rel="stylesheet" href="../../{p}">' for p in styles)
encoded=json.dumps(c,ensure_ascii=False).replace('</','<\\/')
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Track A · Readiness rehearsal</title>{links}</head>
<body><div data-cso-shell data-variant="standard" data-course-title="Human Rights-Based Approach in CSO Practice" data-course-context="Readiness rehearsal" data-progress-label="Practice review" data-progress-percent="0"></div><template data-shell-menu><a href="#main">Review dossier</a></template>
<main id="main" class="readiness-page" tabindex="-1"><header><p>ASSESSMENT / READINESS REHEARSAL</p><h1>{html.escape(c['contract']['title'])}</h1><p>{html.escape(c['case']['brief'])}</p><details><summary>Practice and authority boundary</summary><p>{html.escape(c['freeze_authority']['boundary'])}</p></details></header>
<noscript><h2>Interactive review unavailable</h2><p>JavaScript is required for review and recovery; no completion is recorded. <a href="exercise.txt">Read the complete dossier and practice exercise as plain text</a> and retain work in your own document.</p></noscript><div data-readiness-workspace></div></main>
<div data-cso-learning-actions data-status="Complete the current practice review."></div><script src="../../shell/course-shell.js"></script><script type="application/json" data-readiness-contract>{encoded}</script><script type="module" src="../../interactions/readiness-review/readiness-review.js"></script></body></html>'''
(folder/'index.html').write_text(page,encoding='utf-8')
text=[c['case']['designation'],c['case']['brief'],c['freeze_authority']['boundary']]
for a in c['case']['artifacts']:text.append(f"{a['id']} v{a['version']} — {a['title']}\n{a['source']}\n{a['text']}\nLimitation: {a['limitation']}")
for k in c['criteria']:text.append(k['id']+' — '+k['label']+'\n'+k['question']+'\n'+k['sufficiency_anchor'])
text += ['Map support/limiting sources to each criterion; choose sufficient, insufficient, conflicting or missing, and retain gaps/priority. Choose proceed, revise, seek review or defer. Write one rationale (45 words/600 characters maximum) and one conditional next-step note (35 words/600 characters maximum). No word minimum. Preserve this initial recommendation before reading the clarification.']
text += [r['label']+'\n'+r['consequence'] for r in c['decision_routes']]
text += [c['feedback']['common_contrast'],'LATER CLARIFICATION: TA-U01 (read after initial review)',c['case']['update']['text'],c['case']['update']['limitation'],'Reassess all criteria using E03 v2. Retain or amend the recommendation explicitly. Compare original/current work, inspect consequences and acknowledge practice only. This text fallback records no runtime completion.']
(folder/'exercise.txt').write_text('\n\n'.join(text)+'\n',encoding='utf-8')
print('Track A materialized from frozen contract; three PROTOTYPE candidates; two opt-in variants.')
