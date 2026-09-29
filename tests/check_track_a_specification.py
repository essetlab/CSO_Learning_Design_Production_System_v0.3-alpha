"""Document-only checks; no prototype, browser, PM stress or runtime tests."""
from pathlib import Path
import json,hashlib,sys,re,subprocess
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from validators.validate_repository import validate_repository
from validators.validate_governance import load_registries,validate_references
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def check(n,v,detail=None):checks.append(dict(name=n,passed=bool(v),details=detail))
prefix='prototype-specs/TRACK_A_';c=read(prefix+'AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json');b=read(prefix+'EXPERIENCE_DIFFERENTIATION_BRIEF_v0.1.json');f=read(prefix+'SEMANTIC_REVIEW_FIXTURES_v0.1.json');inv=read(prefix+'RESOURCE_INVENTORY_v0.1.json');base=read('tests/track-a-preflight/BASELINE.json')
schema=read('schemas/experience-differentiation-brief.schema.json');check('Canonical differentiation schema',Draft202012Validator(schema).is_valid(b));check('Brief identity',b['reference']=='TRACK-A')
required=['contract','build_mode','authority','capability','distinction','case','criteria','mapping','decision_routes','authoring','roles','feedback','sequence','state','predicates','completion','representation','responsive','content_maxima','objects','validation_matrix','experience_differentiation_brief','specification_only']
proposal_schema={'$schema':'https://json-schema.org/draft/2020-12/schema','title':'Track A proposal structural review schema (not a runtime payload schema)','type':'object','required':required,'properties':{k:{'type':'object'} for k in ['contract','authority','case','mapping','authoring','roles','feedback','state','predicates','completion','representation','responsive','content_maxima','objects']}}
proposal_schema['properties'].update(contract={'type':'object','required':['reference','status','prototype_implementation_authorized'],'properties':{'reference':{'const':'TRACK-A'},'status':{'const':'PROPOSED_NOT_FROZEN'},'prototype_implementation_authorized':{'const':False}}},specification_only={'const':True},criteria={'type':'array','minItems':3,'maxItems':3},decision_routes={'type':'array','minItems':4,'maxItems':4})
(ROOT/'tests/track-a-preflight/PROPOSAL_REVIEW_SCHEMA.json').write_text(json.dumps(proposal_schema,indent=2)+'\n',encoding='utf-8')
check('Proposal structural schema',Draft202012Validator(proposal_schema).is_valid(c))
groups,errors=load_registries(ROOT);check('Registry parity',not errors,errors)
policy=read('governance/validation-policy.json');existing={'build_mode':c['build_mode'],'authority':c['authority'],'reuse':c['objects']['reuse']}
errors,_=validate_references(existing,groups,policy,'TRACK-A proposal existing references');check('Every reused ID and authority mode resolves',not errors,errors)
for p in c['objects']['proposed_candidates']:check('Proposed ID is unregistered '+p['id'],p['status']=='PROPOSED_NOT_REGISTERED' and p['id'] not in groups['all'] and not (ROOT/p['owner']).exists())
for p in c['objects']['proposed_variants']:check('Variant owner known, variant unregistered '+p['owner_id'],p['owner_id'] in groups['all'] and p['status']=='PROPOSED_NOT_REGISTERED' and p['variant'] not in groups['all'][p['owner_id']].get('variants',[]))
check('No Track A runtime or inferred GR number',not (ROOT/'golden-references/TRACK-A').exists() and not (ROOT/'golden-references/GR-07').exists() and c['contract']['reference']=='TRACK-A')
check('Four routes and assessment states',set(x['id'] for x in c['decision_routes'])=={'proceed','revise','seek_review','defer'} and set(c['mapping']['states'])=={'sufficient','insufficient','conflicting','missing'})
check('Two authored fields; no minimum/grade',len(c['authoring']['fields'])==2 and [x['max_words'] for x in c['authoring']['fields']]==[45,35] and c['authoring']['word_minima'] is None and not c['completion']['semantic_grading'])
check('Completion is practice-only',c['completion']['expression']=='E && M && J && C && U && R && F' and set(c['predicates'])==set('EMJCURF') and all(c['completion'][k] is False for k in ['requires_proceed','requires_all_sufficient','requires_no_gaps','requires_storage','requires_export']))
check('Shared state unchanged and independent',c['state']['retention']['service_id']=='SVC-LEARNING-STATE-01' and c['state']['retention']['unchanged'] and c['roles']['authorization_record'] is None and c['roles']['credential'] is None)
def words(s):return len(s.split())
m=c['content_maxima']
for e in c['case']['artifacts']:
 check(e['id']+' exact bounded source',words(e['title'])<=m['source_title_words'] and words(e['text'])<=m['source_text_words'] and words(e['limitation'])<=m['source_limitation_words'])
for q in c['criteria']:check(q['id']+' bounded criterion',words(q['label'])<=m['criterion_label_words'] and words(q['question'])<=m['criterion_question_words'] and words(q['sufficiency_anchor'])<=m['criterion_anchor_words'])
check('Update and feedback bounds',words(c['case']['update']['text'])<=m['update_text_words'] and words(c['feedback']['common_contrast'])<=m['common_contrast_words'] and all(words(d['consequence'])<=m['route_consequence_words'] for d in c['decision_routes']))
check('Four positive/eight negative fixtures separate',len(f['positive_examples'])==4 and len(f['negative_counterexamples'])==8 and f['human_judgment']=='PENDING_ARCHITECTURAL_REVIEW')
for x in f['positive_examples']:
 for kind in ['initial','current']:
  record=x[kind];version=record['bundle_version'];known={e['id']:2 if e['id']=='TA-E03' and version==2 else 1 for e in c['case']['artifacts']}
  valid=set(record['mappings'])=={q['id'] for q in c['criteria']};used=set()
  for row in record['mappings'].values():
   links=row['links'];ids=[l['artifact_id'] for l in links];roles=[l['role'] for l in links];used.update(ids)
   valid &= len(ids)==len(set(ids)) and len(ids)<=4 and all(l['artifact_id'] in known and l['version']==known[l['artifact_id']] and l['role'] in c['mapping']['link_roles'] for l in links)
   state=row['state'];valid &= state in c['mapping']['states'] and all(g in c['mapping']['gap_markers'] for g in row['gap_markers'])
   if state=='sufficient':valid &= 'supports' in roles
   if state=='insufficient':valid &= len(links)>0 and bool(row['gap_markers'])
   if state=='conflicting':valid &= len(links)>=2 and set(roles)==set(c['mapping']['link_roles']) and bool(row['gap_markers'])
   if state=='missing':valid &= 'supports' not in roles and bool(row['gap_markers'])
   if row['gap_markers']:valid &= row['gap_priority'] in c['mapping']['gap_priority']
  valid &= len(used)>=2
  for field,maxw in [('rationale',45),('next_step_note',35)]:valid &= words(record[field])<=maxw and len(record[field])<=600 and sum(ch.isalnum() for ch in record[field])>=2
  check(x['id']+' '+kind+' structural semantic-fixture bounds only',valid)
plan=read(prefix+'VALIDATION_PLAN_v0.1.json');check('V01–V22 all planned, no runtime pass', [v['id'] for v in plan['tests']]==[f'V{i:02}' for i in range(1,23)] and all(v['status']=='PLANNED_NOT_EXECUTED' for v in plan['tests']))
check('Ten pending human dimensions',len(plan['human_rubric'])==10 and all(h['status']=='PENDING_ARCHITECTURAL_REVIEW' for h in plan['human_rubric']))
allowed={'REUSE DIRECTLY','ADAPT','HARVEST PATTERN','REFERENCE ONLY','REJECT','SYSTEM GAP'}
check('Resource-first dispositions complete',len(inv['resources'])==23 and all(r['disposition'] in allowed for r in inv['resources']))
for resource in inv['resources']:
 check(resource['id']+' inspected file hashes',all(Path(p['path']).is_file() and sha(p['path'])==p['sha256'] for p in resource['files']))
for name in ['RESOURCE_FIRST_PREFLIGHT','EXPERIENCE_DIFFERENTIATION_BRIEF','DETERMINISTIC_LEARNING_DESIGN','VALIDATION_MATRIX','RESEARCH_AND_SOURCE_NOTES']:check('Required artifact '+name,(ROOT/(prefix+name+'_v0.1.md')).is_file())
protected=['assets/','compositions/','foundations/','interactions/','learning-blocks/','practice/','registries/','shell/','state/','templates/','tokens/','ui/','locked-build-specs/']
changed=[p for p,h in base['hashes'].items() if not (ROOT/p).is_file() or sha(ROOT/p)!=h]
bad=[p for p in changed if any(p.startswith(d) for d in protected) or (p.startswith('prototype-specs/GR-')) or (p.startswith('golden-references/') and Path(p).suffix in ['.html','.css','.js','.yaml','.txt'])]
check('All production, registry and frozen inputs byte-preserved',not bad,bad)
for folder in ['interactions','learning-blocks','golden-references','compositions','templates','state']:
 runtime=[p for p in (ROOT/folder).rglob('*') if p.suffix in ['.html','.js','.css']]
 check(folder+' has no semantic-fixture runtime dependency',all('TRACK_A_SEMANTIC_REVIEW_FIXTURES' not in p.read_text(encoding='utf-8') for p in runtime))
manual=read('tests/GR06_MANUAL_EVIDENCE.json');check('GR06 exact current provenance',manual['direct_technical_attestations'][0]['provenance']=='USER_ATTESTED' and manual['direct_technical_attestations'][0]['status']=='PASS' and {v['id'] for v in manual['checks']}=={'V19-screen-reader','V19-mobile'} and all(h['status']=='PASS' for h in manual['human_dimensions']))
check('GR06 still pending manual',read('tests/GR06_VALIDATION_RESULT.json')['status']=='IMPLEMENTED_PENDING_MANUAL_VALIDATION')
repo=validate_repository();check('Current repository schema and registered/frozen references',repo['status']=='pass',repo)
check('Existing branch/HEAD preserved',subprocess.check_output(['git','branch','--show-current'],text=True).strip()==base['branch'] and subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==base['head'])
result=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',scope='Specification/schema/reference/preservation only. No prototype validation or semantic judgment performed.',checks=checks,changed_baseline_files=changed)
(ROOT/'tests/track-a-preflight/SPECIFICATION_CONSISTENCY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),failures=[x for x in checks if not x['passed']]),indent=2));sys.exit(0 if result['status']=='PASS' else 1)
