"""Idempotent authorized prototype registration; does not promote existing objects."""
from pathlib import Path
import json,yaml
ROOT=Path(__file__).resolve().parents[1]
contract='prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'
items=[('components','BLK-EVIDENCE-LEDGER-01','block','learning-blocks/evidence-ledger','Source metadata, typed evidence associations, field-aligned comparison and export representation.',{'engine':'evidence-ledger.js'}),('components','INT-EVIDENCE-DECISION-01','interaction','interactions/evidence-decision','E/I/D/U/A/R/F, immutable v1, update release, invalidation and acknowledgment. Sole completion owner.',{'engine':'evidence-decision.js','model':'model.js'}),('patterns','IP-EVIDENCE-DECISION-01','pattern','docs/patterns/evidence-decision','Evidence to differentiated interpretation to accountable decision to update and review; structural checks never semantic grading.',{})]
for reg,id,kind,path,owner,extra in items:
 p=ROOT/path;p.mkdir(parents=True,exist_ok=True)
 manifest=dict(id=id,version='0.3.0-alpha',status='PROTOTYPE',type=kind,ownership=owner,cross_course_validation='not-yet-tested',frozen_contract=contract,**extra)
 (p/'manifest.yaml').write_text(yaml.safe_dump(manifest,sort_keys=False),encoding='utf-8')
 if not (p/'README.md').exists():
  (p/'README.md').write_text(f'# {id}\n\nPROTOTYPE only. {owner}\n\nFrozen GR-06 Revision 2 supplies the case. Shared state service owns storage only. No AI grading, prepared answers, new tokens or local persistence.\n',encoding='utf-8')
 f=ROOT/f'registries/{reg}.json';r=json.loads(f.read_text());r['objects']=[o for o in r['objects'] if o['id']!=id]+[dict(id=id,version='0.3.0-alpha',status='PROTOTYPE',type=kind,implementation=f'{path}/manifest.yaml')];f.write_text(json.dumps(r,indent=2)+'\n')
for reg,id,variant,path in [('compositions','CMP-EVIDENCE-DECISION-01','source-interpretation-decision-update','compositions/evidence-decision'),('templates','TPL-DEEP-WORKSPACE-01','evidence-decision','templates/deep-workspace')]:
 f=ROOT/f'registries/{reg}.json';r=json.loads(f.read_text());o=next(o for o in r['objects'] if o['id']==id);o['variants']=list(dict.fromkeys(o.get('variants',[])+[variant]));f.write_text(json.dumps(r,indent=2)+'\n')
 f=ROOT/path/'manifest.yaml';m=yaml.safe_load(f.read_text());m['variants']=[dict(id=variant,status='PROTOTYPE',opt_in=True,ownership='Arrangement only; no state/completion authority',compatibility='Existing default markup, labels, selectors and behavior unchanged')];f.write_text(yaml.safe_dump(m,sort_keys=False),encoding='utf-8')
for reg in ['components','patterns','compositions','templates']:
 r=json.loads((ROOT/f'registries/{reg}.json').read_text());(ROOT/f'registries/{reg}.yaml').write_text(yaml.safe_dump(r,sort_keys=False),encoding='utf-8')
spec=dict(id='GR-06',system_version='0.3-alpha',build_mode='CONSTRAINED_BUILD',instructional_pattern='IP-EVIDENCE-DECISION-01',template={'id':'TPL-DEEP-WORKSPACE-01','variant':'evidence-decision'},composition='CMP-EVIDENCE-DECISION-01',composition_variant='source-interpretation-decision-update',components=['SHELL-GR-W1-01','UI-SAVE-STATE-01','BLK-EVIDENCE-LEDGER-01','INT-EVIDENCE-DECISION-01','SVC-LEARNING-STATE-01'],completion='E && I && D && U && A && R && F',prototype_contract='../../'+contract,local_css_allowed=False,candidate_objects_status='PROTOTYPE')
(ROOT/'golden-references/GR-06/spec.yaml').write_text(yaml.safe_dump(spec,sort_keys=False),encoding='utf-8')
print('Three shared PROTOTYPE candidates and two opt-in variants registered')
