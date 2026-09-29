"""Frozen authority, shared ownership, compatibility and fixture isolation."""
from pathlib import Path
import json,re,subprocess,hashlib,yaml
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'tests/track-a-implementation'
BASE=json.loads((OUT/'FREEZE_CHECKPOINT.json').read_text(encoding='utf-8'))
commit='d4e72e3a898e63ec084288925155781c4c58fce3'
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def before(p):return subprocess.check_output(['git','show',commit+':'+p],cwd=ROOT).decode('utf-8').replace('\r\n','\n')
checks=[]
def check(name,value,details=None):checks.append(dict(name=name,passed=bool(value),**({'details':details} if details else {})))
c=json.loads(read('prototype-specs/TRACK_A_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'));page=read('golden-references/TRACK-A/index.html')
for p in sorted((ROOT/'prototype-specs').glob('TRACK_A_*')):check('Frozen input unchanged '+p.name,read(p.relative_to(ROOT))==before(p.relative_to(ROOT).as_posix()))
check('Exact frozen contract embedded',json.loads(re.search(r'data-readiness-contract>(.*?)</script>',page,re.S).group(1))==c)
check('Freeze and explicit boundary',c['freeze_authority']['decision']=='TRACK_A_REVISION_1_FROZEN_FOR_PROTOTYPE_IMPLEMENTATION' and c['freeze_authority']['boundary'] in c['authority']['LOCKED'])
check('No reference-local scripts, styles or persistence',not re.search(r'<style\b|\sstyle=',page) and not list((ROOT/'golden-references/TRACK-A').glob('*.js')) and not list((ROOT/'golden-references/TRACK-A').glob('*.css')))
check('All page dependencies resolve',all((ROOT/'golden-references/TRACK-A'/p).resolve().is_file() for p in re.findall(r'(?:src|href)="([^"]+)"',page) if not p.startswith('#')))
for o in c['objects']['proposed_candidates']:
 reg='patterns' if o['id'].startswith('IP-') else 'components';entries=[x for x in json.loads(read('registries/'+reg+'.json'))['objects'] if x['id']==o['id']];manifest=yaml.safe_load(read(o['owner']+'manifest.yaml'))
 check(o['id']+' shared PROTOTYPE only',len(entries)==1 and entries[0]['status']=='PROTOTYPE' and manifest['status']=='PROTOTYPE' and manifest['ownership']==o['responsibility'])
for group in ['components','patterns','templates','compositions']:
 old=json.loads(before('registries/'+group+'.json'));now=json.loads(read('registries/'+group+'.json'));objects={o['id']:o for o in now['objects']}
 check(group+' registry parity',now==yaml.safe_load(read('registries/'+group+'.yaml')))
 for o in old['objects']:
  expected=dict(o)
  if o['id'] in ['CMP-EVIDENCE-DECISION-01','TPL-SCENARIO-01']:expected['variants']=o.get('variants',[])+['readiness-review']
  check('Existing registry authority preserved '+o['id'],objects.get(o['id'])==expected)
for path in ['templates/scenario/manifest.yaml','compositions/evidence-decision/manifest.yaml']:
 old=yaml.safe_load(before(path));now=yaml.safe_load(read(path));variants=now.pop('variants');check(path+' defaults semantically exact',{**now,'variants':variants[:-1]}==old and variants[-1]['id']=='readiness-review' and variants[-1]['opt_in'])
protected=['shell','tokens','foundations','state','ui','templates','compositions','interactions','learning-blocks','locked-build-specs']
files=subprocess.check_output(['git','ls-tree','-r','--name-only',commit,'--',*protected],cwd=ROOT,text=True).splitlines()
changed=[]
for p in files:
 if p in ['templates/scenario/manifest.yaml','compositions/evidence-decision/manifest.yaml']:continue
 try:
  if read(p)!=before(p):changed.append(p)
 except UnicodeDecodeError:
  if (ROOT/p).read_bytes()!=subprocess.check_output(['git','show',commit+':'+p],cwd=ROOT):changed.append(p)
check('All existing shared consumers/default sources byte-exact modulo Git line endings',not changed,changed)
for gr in range(1,7):
 for name in ['index.html','exercise.txt']:
  p=f'golden-references/GR-{gr:02}/{name}'
  if (ROOT/p).exists():check('Earlier learner output preserved '+p,read(p)==before(p))
for p in ['learning-blocks/assessment-bundle/assessment-bundle.js','interactions/readiness-review/model.js','interactions/readiness-review/readiness-review.js','templates/scenario/readiness-review.js']:
 check(p+' no storage APIs or semantic fixtures',not re.search(r'\b(?:localStorage|sessionStorage|indexedDB)\b|SEMANTIC_REVIEW_FIXTURES',read(p)))
css=read('compositions/evidence-decision/readiness-review.css');check('Existing breakpoints only',set(re.findall(r'max-width:([\d.]+rem)',css))<={'64rem','48rem','30rem'});check('No token definitions or raw new colors',not re.search(r'--[\w-]+\s*:|#[0-9a-fA-F]{3,8}\b|rgba?\(',css))
check('No tabs/deep workspace',not re.search(r'tablist|role=.tab|deep-workspace',read('interactions/readiness-review/readiness-review.js')))
result={'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','freeze_commit':commit,'checks':checks}
(OUT/'ownership.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':result['status'],'checks':len(checks),'failures':[x for x in checks if not x['passed']]},indent=2));raise SystemExit(result['status']!='PASS')
