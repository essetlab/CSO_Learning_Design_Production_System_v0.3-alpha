"""Current authority, strict change scope, historical preservation and evidence checks."""
from pathlib import Path
import json,hashlib,sys,subprocess
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from validators.validate_bounded_encoding import validate as validate_encoding
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def hash(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
checks=[]
def check(name,value,details=None):checks.append(dict(name=name,passed=bool(value),details=details))
baseline=read('tests/wave2-corrections/BASELINE.json');index=read('WAVE_2_CURRENT_AUTHORITY.json');decision=read('governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json')
changed=[p for p,h in baseline['hashes'].items() if not (ROOT/p).is_file() or hash(p)!=h]
protected=['assets/','compositions/','docs/patterns/','foundations/','interactions/','learning-blocks/','practice/','prototype-specs/','registries/','shell/','state/','templates/','tokens/','ui/']
encoding={'interactions/build-repair/build-repair.js','golden-references/GR-05/index.html','golden-references/GR-05/exercise.txt'}
violations=[p for p in changed if (any(p.startswith(d) for d in protected) or (p.startswith('golden-references/') and Path(p).suffix in ['.js','.css','.html','.yaml','.txt'])) and p not in encoding]
check('Production, registries and frozen inputs unchanged except exact GR05 punctuation',not violations,violations)
check('Exact W2-C03 source/output normalization proof',validate_encoding(ROOT))
for p in changed:
 b='tests/wave2-corrections/baseline/'+p
 check('Historical bytes retained '+p,(ROOT/b).is_file() and hash(b)==baseline['hashes'][p])
for p in ['WAVE_2_CONSOLIDATED_SYSTEM_REVIEW_v0.1.md','WAVE_2_OBJECT_DISPOSITION_MATRIX_v0.1.md','WAVE_2_REMAINING_COVERAGE_AND_NEXT_REFERENCES_v0.1.md','WAVE_2_SYSTEM_REVIEW.json','tests/gr05-example-work.json','tests/gr05-v25-semantic-review-fixture.json','tests/gr06-semantic-fixtures.json']:
 if p in baseline['hashes']:check('Historical review/fixture unchanged '+p,hash(p)==baseline['hashes'][p])
check('Original ZIP unchanged',hash(baseline['review_archive'])==baseline['review_archive_sha256'])
for a in index['current_artifacts']+index['historical_evidence']:check('Index target/hash '+a['path'],(ROOT/a['path']).is_file() and hash(a['path'])==a['sha256'])
check('Capability governed, no assumed numbering or track permission',index['gate_architecture_recovery']['no_invented_numbering'] and index['gate_architecture_recovery']['no_mandatory_four_separate_builds'] and all(x=='PROPOSED_NOT_AUTHORIZED' for x in index['tracks'].values()))
check('All mandated experience families retained',len(index['remaining_gate8_capability_coverage'])==7)
objects={o['id']:o for r in ['components','compositions','patterns','templates'] for o in read(f'registries/{r}.json')['objects']}
check('All 15 candidate statuses unchanged; recommendations not promotions',len(index['candidates'])==15 and all(objects[o['id']]['status']==o['registry_status'] for o in index['candidates']))
check('Navigation dependency remains existing shell, not invented object','UI-NAV-CONTROLS-01' not in objects and 'SHELL-GR-W1-01' in objects and 'continueButton' in (ROOT/'shell/course-shell.js').read_text())
check('GR03 and GR05 governed passes unchanged',index['references']['GR-03']['status']==index['references']['GR-05']['status']=='PASS_FOR_WAVE_2_SYSTEM_REVIEW')
check('GR06 remains pending only three direct technical checks',read('tests/GR06_VALIDATION_RESULT.json')['status']=='IMPLEMENTED_PENDING_MANUAL_VALIDATION' and len(read('tests/GR06_VALIDATION_RESULT.json')['manual'])==3)
check('H01-H09 ChatGPT semantic PASS provenance',decision['GR06_semantic_review']['status']=='PASS' and decision['GR06_semantic_review']['provenance']=='CHATGPT_REVIEW_REPORTED_BY_USER' and all(h['status']=='PASS' for h in read('tests/GR06_MANUAL_EVIDENCE.json')['human_dimensions']))
for p in (ROOT/'schemas').glob('*.json'):
 try:Draft202012Validator.check_schema(json.loads(p.read_text(encoding='utf-8')));ok=True
 except Exception:ok=False
 check('Valid JSON schema '+p.name,ok)
reports=['tests/wave2-corrections/REGRESSION_COMMANDS.json','tests/wave2-corrections/VALIDATOR_REGRESSION.json','tests/wave2-corrections/REPOSITORY_VALIDATION.json','tests/wave2-corrections/GR05_ENCODING_BROWSER.json','tests/wave2-corrections/GR05_KEYBOARD_RESILIENCE_RESULTS.json','tests/wave2-corrections/GR06_BROWSER_RESULTS.json','tests/wave2-corrections/GR06_RECOVERY_RESULTS.json','tests/gr03-browser-validation-bounded-corrections.json','tests/gr05-browser-bounded-corrections.json']
for p in reports:
 d=read(p);passed=d.get('automated_pass') if 'gr03-browser' in p else d.get('passed',str(d.get('status','')).lower()=='pass');check('Current regression '+p,passed and all(c.get('passed',False) for c in d.get('checks',[])))
check('Branch and HEAD preserved',subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()==baseline['branch'] and subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==baseline['head'])
result=dict(status='PASS' if all(c['passed'] for c in checks) else 'FAIL',changed_baseline_files=changed,checks=checks)
(ROOT/'tests/wave2-corrections/CONSISTENCY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),changed_baseline_files=len(changed),failures=[c for c in checks if not c['passed']]),indent=2));sys.exit(0 if result['status']=='PASS' else 1)
