"""Permanent W2-C01/C06 negative probes, only in disposable repository copies."""
from pathlib import Path
import copy,json,shutil,sys,tempfile
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from validators.validate_repository import validate_repository
from jsonschema import Draft202012Validator
checks=[]
def check(name,value,details=None):checks.append(dict(name=name,passed=bool(value),details=details))
with tempfile.TemporaryDirectory(prefix='w2-governance-') as directory:
 root=Path(directory)
 for d in ['registries','schemas','locked-build-specs','governance','prototype-specs']:shutil.copytree(ROOT/d,root/d)
 for a in json.loads((ROOT/'registries/assets.json').read_text(encoding='utf-8'))['assets']:
  p=root/a['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'path existence only')
 for p in (ROOT/'golden-references').glob('*/spec.yaml'):
  target=root/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
 initial=validate_repository(root)
 check('canonical specs, all frozen contracts and GR02 legacy string accepted',initial['status']=='pass' and initial['legacy_template_strings']==['GR-02'] and len(initial['contracts_checked'])==4,initial)
 def probe(label,path,mutate):
  target=root/path;before=target.read_bytes()
  data=yaml.safe_load(before) if target.suffix=='.yaml' else json.loads(before)
  mutate(data)
  target.write_text(yaml.safe_dump(data) if target.suffix=='.yaml' else json.dumps(data),encoding='utf-8')
  try:
   result=validate_repository(root)
   check(label,result['status']=='fail' and any(path.split('/')[-2] in e or path in e for e in result['errors']),result['errors'])
  finally:target.write_bytes(before)
 def setkey(k,v):return lambda d:d.__setitem__(k,v)
 for gr in ['GR-01','GR-02','GR-03','GR-04','GR-05','GR-06']:
  path=f'golden-references/{gr}/spec.yaml'
  for key,value in [('components',['UNKNOWN-COMPONENT']),('interaction','UNKNOWN-INTERACTION'),('learning_block','UNKNOWN-BLOCK'),('composition','UNKNOWN-COMPOSITION'),('instructional_pattern','UNKNOWN-PATTERN'),('supporting_pattern','UNKNOWN-SUPPORT'),('template',{'id':'UNKNOWN-TEMPLATE'}),('template',{'id':'TPL-CONCEPT-01','variant':'UNKNOWN-VARIANT'}),('composition_variant','UNKNOWN-VARIANT'),('build_mode','UNKNOWN-MODE'),('authority','UNRESTRICTED'),('authority',{}),('authority',{'UNCONTROLLED':['change anything']}),('components',['UI-NAV-CONTROLS-01']),('interactions',['BLK-WORK-ARTIFACT-01'])]:
   probe(gr+' rejects '+key+' '+str(value),path,setkey(key,value))
 for gr in ['GR-03','GR-05','GR-06']:
  path=f'prototype-specs/{gr}_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'
  for key,value in [('component_id','UNKNOWN'),('interaction_id','UNKNOWN'),('learning_block_id','UNKNOWN'),('composition_id','UNKNOWN'),('pattern_id','UNKNOWN'),('template_id','UNKNOWN'),('template',{'id':'TPL-DEEP-WORKSPACE-01','variant':'UNKNOWN'}),('composition',{'id':'CMP-EVIDENCE-DECISION-01','variant':'UNKNOWN'}),('build_mode','UNKNOWN'),('authority_mode','UNKNOWN'),('authority',{'meaning':'UNRESTRICTED'}),('owner_candidate','UNKNOWN')]:
   probe(gr+' frozen contract rejects '+key,path,setkey(key,value))
  probe(gr+' rejects unknown ID in nested prose',path,setkey('reference_note',{'owner':'Use BLK-UNREGISTERED-99 here.'}))
  probe(gr+' rejects nested unsupported authority',path,setkey('settings',{'authority':'UNRESTRICTED'}))
 probe('GR03 rejects nearby unknown dependency','prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json',lambda d:d['system_objects']['shared_ui'].__setitem__(3,'UI-NAV-CONTROLS-99'))
 probe('GR03 alias cannot move to another slot','prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json',lambda d:d['system_objects']['shared_ui'].reverse())
 probe('GR06 nested variant validation','prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json',lambda d:d['objects']['composition'].__setitem__('variant','BAD'))
 probe('GR06 nested build authority validation','prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json',lambda d:d['contract'].__setitem__('build_mode','BAD'))
 probe('unknown explicit null variant','golden-references/GR-06/spec.yaml',setkey('composition_variant',None))
 probe('conflicting template variants','golden-references/GR-06/spec.yaml',setkey('template_variant','BAD'))
 probe('missing frozen contract rejected','golden-references/GR-06/spec.yaml',setkey('prototype_contract','../../missing.json'))
 probe('registry mirror mismatch rejected','registries/components.json',lambda d:d['objects'][0].__setitem__('status','CORRUPT'))
 # Discover an unlinked frozen contract as well as linked contracts.
 extra=root/'prototype-specs/TEST_CONTRACT.json'
 extra.write_text(json.dumps({'contract':{'status':'FROZEN_FOR_TEST'},'component_id':'UNKNOWN'}))
 check('unlinked frozen contracts are validated',any('TEST_CONTRACT.json' in e for e in validate_repository(root)['errors']))
 extra.unlink()
 original=yaml.safe_load((root/'golden-references/GR-06/spec.yaml').read_text())
 future=copy.deepcopy(original);future['id']='GR-TEST';future.pop('prototype_contract',None)
 target=root/'golden-references/GR-TEST/spec.yaml';target.parent.mkdir()
 target.write_text(yaml.safe_dump(future))
 check('future reference missing brief rejected',any('requires experience_differentiation_brief' in e for e in validate_repository(root)['errors']))
 brief=json.loads((root/'prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.json').read_text())
 schema=json.loads((root/'schemas/experience-differentiation-brief.schema.json').read_text());v=Draft202012Validator(schema)
 check('blank authoring template cannot masquerade as complete brief',not v.is_valid(brief))
 for k in brief:
  if isinstance(brief[k],str):brief[k]='Test declaration only'
 brief['reference']='GR-TEST'
 for p in brief['validation_baseline']['universal'].values():p.update(method='Test method',evidence='tests/example',owner='Test owner')
 for p in brief['validation_baseline']['conditional'].values():p.update(applies=False,rationale='Test non-applicability rationale',validation=dict(method='Review rationale',evidence='tests/example',owner='Test owner'))
 briefpath=root/'prototype-specs/TEST_BRIEF.json';briefpath.write_text(json.dumps(brief))
 future.update(experience_differentiation_brief='prototype-specs/TEST_BRIEF.json',build_mode='CONSTRAINED_BUILD',authority={'LOCKED':['Frozen content'],'CONSTRAINED':['Registered assembly'],'EXPLORATORY':['No implementation changes']})
 target.write_text(yaml.safe_dump(future))
 check('complete test-only future brief accepted',validate_repository(root)['status']=='pass')
 for field in schema['required']:
  bad=copy.deepcopy(brief);bad.pop(field);check('brief requires '+field,not v.is_valid(bad))
 for kind in ['universal','conditional']:
  for key in brief['validation_baseline'][kind]:
   bad=copy.deepcopy(brief);bad['validation_baseline'][kind].pop(key);check('brief requires applicability/plan '+key,not v.is_valid(bad))
result=dict(status='PASS' if all(c['passed'] for c in checks) else 'FAIL',checks=checks,scope='Permanent regression probes in temporary copies; no production registry/spec/contract mutation.')
(ROOT/'tests/track-a-implementation/VALIDATOR_REGRESSION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),failures=[c for c in checks if not c['passed']]),indent=2));sys.exit(0 if result['status']=='PASS' else 1)
