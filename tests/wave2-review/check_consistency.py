"""Read-only implementation review checks; mutation probes run in temporary copies."""
from pathlib import Path
import sys,json,hashlib,subprocess,tempfile,shutil,copy
import yaml
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'validators'))
from validate_repository import validate_repository
checks=[]
def check(name,passed,details=None):checks.append(dict(name=name,passed=bool(passed),details=details))
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
baseline=read('tests/wave2-review/input-snapshot.json')
changed=[p for p,h in baseline['protected_hashes'].items() if not (ROOT/p).is_file() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
check('Existing implementation, frozen contracts, registries and evidence remain unchanged',not changed,changed)
check('Branch unchanged',subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()==baseline['branch'])
current=validate_repository();check('Current repository schema/template checks pass',current['status']=='pass',current)
registries={r:read(f'registries/{r}.json') for r in ['components','patterns','compositions','templates']}
for r,data in registries.items():check(r+' registry JSON/YAML parity',data==yaml.safe_load((ROOT/f'registries/{r}.yaml').read_text()))
allids={o['id']:o for r in registries.values() for o in r['objects']}
contract_objects=read('prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json')['system_objects']
contract_ids=[item for value in contract_objects.values() for item in (value if isinstance(value,list) else [value])]
unknown_contract_ids=sorted(set(contract_ids)-set(allids))
check('Existing GR03 contract navigation dependency gap accurately identified',unknown_contract_ids==['UI-NAV-CONTROLS-01'],unknown_contract_ids)
for gr in ['GR-03','GR-05','GR-06']:
 spec=yaml.safe_load((ROOT/f'golden-references/{gr}/spec.yaml').read_text())
 ids=spec['components']+[spec['instructional_pattern'],spec['composition'],spec['template']['id']]+([spec['supporting_pattern']] if 'supporting_pattern' in spec else [])
 check(gr+' actual spec IDs resolve',all(i in allids for i in ids),ids)
 if 'composition_variant' in spec:check(gr+' actual composition variant resolves',spec['composition_variant'] in allids[spec['composition']].get('variants',[]))
probes=[]
with tempfile.TemporaryDirectory(prefix='wave2-validator-review-') as temp:
 dest=Path(temp)
 for folder in ['registries','schemas','locked-build-specs']:shutil.copytree(ROOT/folder,dest/folder)
 for entry in read('registries/assets.json')['assets']:
  p=dest/entry['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'temporary path-existence fixture')
 for p in (ROOT/'golden-references').glob('*/spec.yaml'):
  q=dest/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
 check('Temporary probe baseline passes',validate_repository(dest)['status']=='pass')
 target=dest/'golden-references/GR-06/spec.yaml';original=yaml.safe_load(target.read_text())
 mutations=[('unknown component','components',['UNKNOWN-COMPONENT']),('unknown composition','composition','UNKNOWN-COMPOSITION'),('unknown pattern','instructional_pattern','UNKNOWN-PATTERN'),('unknown supporting pattern','supporting_pattern','UNKNOWN-SUPPORTING'),('unknown composition variant','composition_variant','UNKNOWN-VARIANT'),('unknown build mode','build_mode','UNKNOWN-MODE'),('unknown template control','template',{'id':'UNKNOWN-TEMPLATE'})]
 for label,key,value in mutations:
  s=copy.deepcopy(original);s[key]=value;target.write_text(yaml.safe_dump(s));r=validate_repository(dest);probes.append(dict(name=label,validator_status=r['status'],errors=r['errors']))
 check('Validator blind spots reproduced, not falsely reported as production failures',all(x['validator_status']=='pass' for x in probes[:-1]) and probes[-1]['validator_status']=='fail',probes)
check('GR06 direct manual checks remain pending',all(x['status']=='PENDING' for x in read('tests/GR06_MANUAL_EVIDENCE.json')['checks']))
for f in ['tests/GR05_VALIDATION_RESULT.json','tests/GR06_VALIDATION_RESULT.json']:
 r=read(f);check(f+' automated evidence passed',r['automated_pass'])
if (ROOT/'WAVE_2_SYSTEM_REVIEW.json').exists():
 r=read('WAVE_2_SYSTEM_REVIEW.json');check('Governed bounded outcome without promotion',r['outcome']=='WAVE_2_PASS_WITH_BOUNDED_CORRECTIONS' and not r['golden_reference_acceptance'] and not r['system_v1_freeze'])
 check('All 15 reviewed object IDs resolve; literal statuses unchanged',len(r['object_dispositions'])==15 and len({o['id'] for o in r['object_dispositions']})==15 and all(o['id'] in allids and o['registry_status']==allids[o['id']]['status'] for o in r['object_dispositions']))
 allowed={'RETAIN AS PROTOTYPE','READY FOR APPROVAL CANDIDATE','REVISE BEFORE APPROVAL','CONSOLIDATE','DEPRECATE'}
 check('Recommendations use requested disposition vocabulary',all(o['recommendation'] in allowed for o in r['object_dispositions']))
 check('All evidence paths and recorded hashes current',all((ROOT/p).is_file() and hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in r['evidence_hashes'].items()))
 check('Every correction has class, timing, owner and acceptance',all(x.get('category') and x.get('timing') and x.get('owner') and x.get('acceptance') for x in r['corrections']))
 check('Cross-reference architecture map complete',set(r['architecture_map'])=={'GR-03','GR-05','GR-06'} and all(len(x)==15 for x in r['architecture_map'].values()))
 for p in r['deliverables']:check('Deliverable exists '+p,(ROOT/p).is_file())
 import re
 missing=[]
 for path in r['deliverables']:
  if not path.endswith('.md'):continue
  for link in re.findall(r'\]\(([^)]+)\)',(ROOT/path).read_text(encoding='utf-8')):
   if '://' not in link and not link.startswith('#') and not (ROOT/link.split('#')[0]).exists():missing.append(dict(document=path,target=link))
 check('Review Markdown evidence links resolve',not missing,missing)
result=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',scope='Review consistency and non-mutation verification. Existing browser evidence inspected; no new browser/manual/semantic pass generated.',checks=checks,validator_mutation_probes=probes)
(ROOT/'tests/wave2-review/consistency-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),failures=[x for x in checks if not x['passed']],probes=probes),indent=2));sys.exit(0 if result['status']=='PASS' else 1)
