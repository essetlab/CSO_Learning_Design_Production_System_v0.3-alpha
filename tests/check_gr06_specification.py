"""Document-only GR-06 consistency checks; no prototype behavior is claimed."""
from pathlib import Path
import json,hashlib,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'prototype-specs'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
c=read(P/'GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json');inventory=read(P/'GR-06_RESOURCE_INVENTORY_v0.1.json')
checks=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)})
check('proposal only, no implementation authorization',c['contract']['status']=='PROPOSED_FOR_ARCHITECTURAL_REVIEW' and not c['contract']['prototype_implementation_authorized'] and not c['objects']['registration_authorized'])
check('all authority tiers explicit',set(c['authority'])=={'LOCKED','CONSTRAINED','EXPLORATORY'})
check('five unique initial evidence IDs',len(c['case']['evidence'])==5 and len({e['id'] for e in c['case']['evidence']})==5)
check('update ID separate from initial batch',c['case']['update']['id'] not in {e['id'] for e in c['case']['evidence']})
check('all sources carry scope/provenance limitations',all(e.get('source') and e.get('scope') and e.get('limitation') for e in c['case']['evidence']) and c['case']['update'].get('provenance'))
check('differentiated interpretation roles and decision links',c['authoring']['interpretations']['ids']==c['authoring']['decision']['claim_ids_required']==['primary_interpretation','alternative_or_unresolved_interpretation'])
check('role prompts and no false symmetry explicit',len(c['authoring']['interpretations']['roles'])==2 and bool(c['authoring']['interpretations']['no_false_symmetry']))
check('four decision routes with no automatic correctness', [x['id'] for x in c['authoring']['decision']['options']]==['trial','verify','retain','escalate'] and c['authoring']['decision']['no_automatically_correct_route'])
check('all nine human rubric dimensions present', [x['id'] for x in c['human_semantic_validation']['dimensions']]==[f'H{i:02}' for i in range(1,10)])
check('case and U01 preserved from revision 1',hashlib.sha256(json.dumps(c['case'],sort_keys=True,ensure_ascii=False).encode()).hexdigest()==c['architectural_revision']['preserved_case_sha256'])
check('decision maxima preserved', {f['id']:f['max_words'] for f in c['authoring']['decision']['fields']}==c['architectural_revision']['preserved_decision_maxima'])
check('semantic composition and configurable template variants',c['objects']['composition']['id']=='CMP-EVIDENCE-DECISION-01' and c['objects']['template']['id']=='TPL-DEEP-WORKSPACE-01' and 'CMP-REPAIR-STUDIO-01' not in c['objects']['adapt_proposed'])
check('all new candidates explicitly proposed not registered',all(o['status']=='PROPOSED_NOT_REGISTERED' for o in c['objects']['new_unregistered_proposals']))
check('maxima positive and no hard minima',all(f['max_words']>0 for f in c['authoring']['decision']['fields']) and 'no word-count minimum' in c['authoring']['T'])
check('completion predicates complete',set(c['state']['predicates'])==set(c['state']['completion'].split(' && ')))
check('completion independent of saving',c['state']['storage_choice_gates_completion'] is False)
check('existing breakpoints/no new tokens',c['responsive']['breakpoints_rem']==[64,48,30] and not c['responsive']['new_tokens'])
registries={}
for name in ['components','patterns','templates','compositions']:
 for o in read(ROOT/f'registries/{name}.json')['objects']:registries[o['id']]=o
check('all proposed reused/adapted IDs exist',all(i in registries for i in c['objects']['reuse']+c['objects']['adapt_proposed']))
check('new proposals unregistered and unmaterialized',all(o['id'] not in registries and not (ROOT/o['path']).exists() for o in c['objects']['new_unregistered_proposals']))
allowed={'REUSE DIRECTLY','ADAPT','HARVEST PATTERN','REFERENCE ONLY','REJECT','SYSTEM GAP'}
check('all dispositions governed',all(x['disposition'] in allowed for x in inventory['resources']))
bad=[]
for source in inventory['resources']:
 for f in source['files']:
  p=Path(f['path'])
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:bad.append(f['path'])
check('inspected source hashes unchanged',not bad)
matrix=(P/c['validation_matrix']).read_text(encoding='utf-8')
check('22 unique future validation rows',re.findall(r'\| (V\d\d) \|',matrix)==[f'V{i:02}' for i in range(1,23)] and 'NOT EXECUTED AGAINST A PROTOTYPE' in matrix)
check('no GR06 Golden Reference built',not (ROOT/'golden-references/GR-06').exists())
protected=['golden-references','interactions','learning-blocks','compositions','templates','state','registries','tokens','shell','foundations','schemas','locked-build-specs','docs/patterns']
diff=subprocess.run(['git','diff',inventory['baseline_commit'],'--',*protected],cwd=ROOT,capture_output=True,text=True)
check('production and shared candidates unchanged since GR05 checkpoint',diff.returncode==0 and not diff.stdout)
g=read(ROOT/'tests/GR05_VALIDATION_RESULT.json')
check('GR05 pass and manual provenance preserved',g['final_status']=='PASS_FOR_WAVE_2_SYSTEM_REVIEW' and all(next(x for x in g['matrix'] if x['id']==k)['status']=='PASS_USER_ATTESTED' for k in ['V21','V22','V23']) and all(next(x for x in g['matrix'] if x['id']==k)['status']=='PASS_REVIEW_REPORTED' for k in ['V05','V25']))
check('GR05 six candidates still PROTOTYPE',all(registries[i]['status']=='PROTOTYPE' for i in read(ROOT/'golden-references/GR-05/GR-05_BUILD_MANIFEST.json')['candidate_objects']))
commands=[]
for args in [['python','validators/validate_repository.py'],['python','tests/test_template_schema.py'],['python','tools/validate_locked_build.py','locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json','golden-references/GR-04/index.html']]:
 p=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace');commands.append({'command':args,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
check('repository and canonical schema regression',all(x['exit_code']==0 for x in commands))
result={'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','scope':'Specification/source/production-preservation checks only; no GR06 prototype validation performed.','checks':checks,'commands':commands,'source_mismatches':bad,'baseline_commit':inventory['baseline_commit']}
(P/'GR-06_PREFLIGHT_VERIFICATION_v0.1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(checks),'failures':[x for x in checks if not x['passed']]},indent=2))
raise SystemExit(0 if result['status']=='PASS' else 1)
