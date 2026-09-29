"""GR-06 frozen content/ownership, fixture isolation and compatibility evidence."""
from pathlib import Path
import json,re,hashlib,subprocess,yaml
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value,details=None): checks.append(dict(name=name,passed=bool(value),**({'details':details} if details else {})))
def read(p):return (ROOT/p).read_text(encoding='utf-8')
c=json.loads(read('prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'))
page=read('golden-references/GR-06/index.html')
embedded=re.search(r'<script type="application/json" data-evidence-contract>(.*?)</script>',page,re.S)
check('V01 exact frozen revision 2 embedded',embedded and json.loads(embedded.group(1))==c)
check('V01 frozen contract text unchanged from checkpoint (Git line endings normalized)',subprocess.check_output(['git','show','4c2ce06:prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'],cwd=ROOT,text=True,encoding='utf-8')==read('prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'))
check('V01 local dependencies exist',all((ROOT/'golden-references/GR-06'/x).resolve().is_file() for x in re.findall(r'(?:src|href)="([^"]+)"',page) if not x.startswith('#')))
check('V01 no local learner script/style',not re.search(r'<style\b|\sstyle=',page) and not list((ROOT/'golden-references/GR-06').glob('*.js')) and not list((ROOT/'golden-references/GR-06').glob('*.css')))
for id,reg,folder in [('BLK-EVIDENCE-LEDGER-01','components','learning-blocks/evidence-ledger'),('INT-EVIDENCE-DECISION-01','components','interactions/evidence-decision'),('IP-EVIDENCE-DECISION-01','patterns','docs/patterns/evidence-decision')]:
 r=json.loads(read(f'registries/{reg}.json'));m=yaml.safe_load(read(folder+'/manifest.yaml'));entries=[o for o in r['objects'] if o['id']==id]
 check(id+' PROTOTYPE shared ownership',len(entries)==1 and entries[0]['status']=='PROTOTYPE' and entries[0]['implementation']==folder+'/manifest.yaml' and m['status']=='PROTOTYPE')
for reg in ['components','patterns','templates','compositions']:check(reg+' JSON/YAML parity',json.loads(read(f'registries/{reg}.json'))==yaml.safe_load(read(f'registries/{reg}.yaml')))
for reg,id,v in [('templates','TPL-DEEP-WORKSPACE-01','evidence-decision'),('compositions','CMP-EVIDENCE-DECISION-01','source-interpretation-decision-update')]:
 o=next(o for o in json.loads(read(f'registries/{reg}.json'))['objects'] if o['id']==id);check(id+' approved variant only',o['variants']==([v,'readiness-review'] if id=='CMP-EVIDENCE-DECISION-01' else [v]))
for p in ['learning-blocks/evidence-ledger/evidence-ledger.js','interactions/evidence-decision/model.js','interactions/evidence-decision/evidence-decision.js','templates/deep-workspace/deep-workspace.js']:
 check(p+' no direct storage APIs',not re.search(r'\b(?:localStorage|sessionStorage|indexedDB)\b',read(p)))
protected=['golden-references/GR-01','golden-references/GR-02','golden-references/GR-03','golden-references/GR-04','golden-references/GR-05','shell','tokens','foundations','locked-build-specs','state/learning-state','interactions/build-repair','learning-blocks/work-artifact','compositions/repair-studio','compositions/evidence-decision/evidence-decision.css','tests/gr05-example-work.json']
from validate_bounded_encoding import validate as validate_encoding
changed=subprocess.check_output(['git','diff','--name-only','4c2ce06','--',*protected],cwd=ROOT,text=True).splitlines()
encoding_paths={'golden-references/GR-05/index.html','golden-references/GR-05/exercise.txt','interactions/build-repair/build-repair.js'}
# Only the authorized punctuation repair may differ in protected production.
# Current manifest metadata is checked independently against its preserved baseline.
manifest_path='golden-references/GR-05/GR-05_BUILD_MANIFEST.json'
unexpected=[p for p in changed if p not in encoding_paths|{manifest_path}]
manifest=json.loads(read(manifest_path));prior=json.loads(read('tests/wave2-corrections/baseline/'+manifest_path))
manifest.pop('bounded_correction',None)
for p in encoding_paths:
 if p in manifest['source_hashes']:manifest['source_hashes'][p]=prior['source_hashes'][p]
check('V22 protected owners preserved except exact authorized W2-C03 punctuation and manifest evidence',not unexpected and validate_encoding(ROOT) and manifest==prior,unexpected)
original=subprocess.check_output(['git','show','4c2ce06:templates/deep-workspace/deep-workspace.js'],cwd=ROOT,text=True)
current=read('templates/deep-workspace/deep-workspace.js')
marker="  const nav=node('nav',{'aria-label':'Repair stages'"
check('V22 exact GR05 default arrangement body retained',original[original.index(marker):]==current[current.index(marker):])
css=read('compositions/evidence-decision/source-interpretation-decision-update.css');tokens=set(re.findall(r'(--[\w-]+)\s*:',read('tokens/tokens.css')))
check('V22 no new tokens',set(re.findall(r'var\((--[\w-]+)',css))<=tokens and not re.search(r'--[\w-]+\s*:',css))
check('V22 existing breakpoints only',set(re.findall(r'@media\s*\(max-width:([^\)]+)',css))=={'64rem','48rem','30rem'})
f=json.loads(read('tests/gr06-semantic-fixtures.json'));packet=read('golden-references/GR-06/GR-06_SEMANTIC_REVIEW_PACKET.md')
check('V21 semantic fixture exact frozen case',f['case']==c['case'])
check('V21 historical fixture has four examples/five negatives; current judgment is in authority record',len(f['examples'])==4 and len(f['negative_counterexamples'])==5 and f['human_judgment']=='PENDING_INDEPENDENT_REVIEW')
check('V21 packet copies exact authored evidence',all(packet.find(q['reason'])>=0 and packet.find(q['followUp'])>=0 for x in f['examples'] for q in x['criterionReview'].values()))
runtime=[p for d in ['golden-references','interactions','learning-blocks','compositions','templates','state','shell'] for p in (ROOT/d).rglob('*') if p.suffix in ['.html','.js','.css']]
check('V21 no runtime dependency on review fixtures',all('gr06-semantic-fixtures' not in p.read_text(encoding='utf-8') and 'GR-06_SEMANTIC_REVIEW_PACKET' not in p.read_text(encoding='utf-8') for p in runtime))
result=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',contract_sha256=hashlib.sha256((ROOT/'prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json').read_bytes()).hexdigest(),checks=checks)
(ROOT/'tests/GR06_STATIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
