"""Check GR-05 frozen content, shared ownership, candidate registries and tokens."""
from pathlib import Path
import json,re,hashlib,subprocess
import yaml
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)})
def read(p):return (ROOT/p).read_text(encoding='utf-8')
contract=json.loads(read('prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'))
page=read('golden-references/GR-05/index.html')
embedded=re.search(r'<script type="application/json" data-repair-contract>(.*?)</script>',page,re.S)
check('frozen revision 2 embedded exactly',embedded and json.loads(embedded.group(1))==contract and contract['contract']['revision']==2 and contract['contract']['prototype_implementation_authorized'])
check('no reference-local script or styles',not re.search(r'<style\b|\sstyle=',page) and not (ROOT/'golden-references/GR-05/reference.js').exists() and not (ROOT/'golden-references/GR-05/reference.css').exists())
dependencies=re.findall(r'(?:src|href)="([^"]+)"',page)
check('all runtime dependencies local and available',all(not re.match(r'https?:',x) and (ROOT/'golden-references/GR-05'/x).resolve().is_file() for x in dependencies if not x.startswith('#')))
objects={'IP-BUILD-REPAIR-01':('patterns','docs/patterns/build-repair'),'BLK-WORK-ARTIFACT-01':('components','learning-blocks/work-artifact'),'INT-BUILD-REPAIR-01':('components','interactions/build-repair'),'CMP-REPAIR-STUDIO-01':('compositions','compositions/repair-studio'),'TPL-DEEP-WORKSPACE-01':('templates','templates/deep-workspace'),'SVC-LEARNING-STATE-01':('components','state/learning-state')}
for oid,(registry,folder) in objects.items():
    data=json.loads(read(f'registries/{registry}.json'))
    check(f'{registry} JSON/YAML parity',data==yaml.safe_load(read(f'registries/{registry}.yaml')))
    entry=[x for x in data['objects'] if x['id']==oid]
    manifest=yaml.safe_load(read(folder+'/manifest.yaml'))
    check(oid+' registered PROTOTYPE in approved shared location',len(entry)==1 and entry[0]['status']=='PROTOTYPE' and entry[0]['implementation']==folder+'/manifest.yaml' and manifest['id']==oid and manifest['status']=='PROTOTYPE')
owned=[p for _,folder in objects.values() for p in (ROOT/folder).glob('*.js')]
check('no reference/view storage APIs',all(not re.search(r'\b(?:localStorage|sessionStorage|indexedDB)\b',p.read_text(encoding='utf-8')) for p in owned if 'state' not in p.relative_to(ROOT).parts))
service=read('state/learning-state/learning-state.js')
check('generic service contains no activity completion predicate',not re.search(r'\b(?:GR-05|firstReviewSnapshot|finalAcknowledgment|COMPLETE)\b',service))
tokens=set(re.findall(r'(--[\w-]+)\s*:',read('tokens/tokens.css')))
for p in ['learning-blocks/work-artifact/work-artifact.css','compositions/repair-studio/repair-studio.css']:
    css=read(p)
    check(p+' uses only existing tokens',set(re.findall(r'var\((--[\w-]+)',css))<=tokens and not re.search(r'--[\w-]+\s*:',css))
    check(p+' existing responsive breakpoints',set(re.findall(r'@media\s*\(max-width:([^\)]+)',css))<={'64rem','48rem','30rem'})
protected=['golden-references/GR-01','golden-references/GR-02','golden-references/GR-03','golden-references/GR-04','shell','tokens','foundations','locked-build-specs']
diff=subprocess.run(['git','diff','63133cb','--',*protected],cwd=ROOT,capture_output=True,text=True)
check('GR01–04 and locked shared production preserved from freeze',diff.returncode==0 and not diff.stdout)
result={'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','contract_sha256':hashlib.sha256(read('prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json').encode()).hexdigest(),'checks':checks}
(ROOT/'tests/GR05_STATIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
