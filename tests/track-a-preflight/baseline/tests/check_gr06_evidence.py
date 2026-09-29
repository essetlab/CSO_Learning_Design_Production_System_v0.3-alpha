"""Evidence consistency only; does not grant any manual or semantic pass."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
checks=[]
def check(name,value):checks.append(dict(name=name,passed=bool(value)))
r=read('tests/GR06_VALIDATION_RESULT.json');m=read('golden-references/GR-06/GR-06_BUILD_MANIFEST.json');manual=read('tests/GR06_MANUAL_EVIDENCE.json')
check('status remains implemented pending manual',r['status']==r['final_status']==m['status']=='IMPLEMENTED_PENDING_MANUAL_VALIDATION')
check('all 22 matrix IDs present once', [x['id'] for x in r['matrix']]==[f'V{i:02}' for i in range(1,23)])
authority=read('governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json')['GR06_semantic_review']
check('three direct technical categories explicitly pending',{x['id'] for x in r['manual']}=={'V18','V19-screen-reader','V19-mobile'} and all(x['status']=='PENDING' for x in r['manual']))
check('ChatGPT semantic PASS explicitly reported by user, not independently performed by Codex',manual['attestations']==[authority] and len(manual['human_dimensions'])==9 and all(x['status']=='PASS' and x['reviewer']==authority['reviewer'] and x['provenance']=='CHATGPT_REVIEW_REPORTED_BY_USER' for x in manual['human_dimensions']) and manual['direct_technical_attestations']==[])
check('V09 and V21 current semantic outcome updated',all(x['status']=='PASS' for x in r['matrix'] if x['id'] in ['V09','V21']))
for p,h in authority['reviewed_hashes'].items():check('exact reviewed content preserved '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
check('no promotion or Golden Reference acceptance',r['candidate_status']==m['candidate_status']=='PROTOTYPE' and not r['golden_reference_accepted'] and not m['golden_reference_accepted'])
check('checkpoint and branch preserved',r['freeze_commit']==m['freeze_commit']=='4c2ce06' and subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='gate8/wave2/gr06-evidence-to-decision')
for name,path in m['reports'].items():
 d=read(path);passed=d.get('automated_pass') if name=='GR03_browser' else d.get('passed',d.get('status')=='PASS')
 check(name+' exact counts and successful automated evidence',passed and r['counts'][name]==len(d.get('commands',d.get('checks',[]))) and all(x.get('passed',False) for x in d.get('checks',[])))
for path,expected in m['sources'].items():check('current source hash '+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected)
check('screenshots exist',bool(m['screenshots']) and all((ROOT/p).is_file() for p in m['screenshots']))
check('manual checklist and review packet exist',all((ROOT/r[k]).is_file() for k in ['manual_checklist','semantic_review_packet','semantic_fixture']))
result=dict(status='PASS' if all(x['passed'] for x in checks) else 'FAIL',checks=checks)
(ROOT/'tests/GR06_EVIDENCE_CONSISTENCY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=result['status'],checks=len(checks),failures=[x for x in checks if not x['passed']]),indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
