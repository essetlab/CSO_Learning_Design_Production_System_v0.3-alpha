"""Governed result/provenance consistency; no human verdict inference."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'tests/track-a-implementation'
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
checks=[]
def check(name,value):checks.append({'name':name,'passed':bool(value)})
r=load('tests/track-a-implementation/VALIDATION_RESULT.json');m=load('golden-references/TRACK-A/BUILD_MANIFEST.json');a=load('WAVE_2_CURRENT_AUTHORITY.json');manual=load('tests/track-a-implementation/MANUAL_EVIDENCE.json')
check('Governed status consistent',r['status']==m['status']==a['references']['TRACK-A']['status']==a['tracks']['A']=='IMPLEMENTED_PENDING_MANUAL_VALIDATION')
pending={'V15','V16','V17','V19','V20'}
check('Exact pending direct/independent matrix',set(v['id'] for v in r['matrix'] if v['status'].startswith('PENDING'))==pending==set(m['pending'])==set(v['id'] for v in manual['checks']))
check('No fabricated human provenance',not manual['user_attestations'] and not manual['independent_semantic_judgments'] and not r['provenance_classes']['user_attested'] and not r['provenance_classes']['independent_semantic'])
check('H01-H10 pending independent judgment',[h['id'] for h in r['human_rubric']]==[f'H{i:02}' for i in range(1,11)] and all(h['status']=='PENDING_INDEPENDENT_REVIEW' for h in r['human_rubric']))
check('No acceptance/certification/Track B',not r['golden_reference_accepted'] and not r['competence_certification_or_authorization'] and not r['Track_B_authorized'] and a['tracks']['B']=='PROPOSED_NOT_AUTHORIZED')
for name,e in r['automated'].items():
 p=ROOT/e['path'];check('Evidence exists '+name,p.is_file())
 if 'sha256'in e:check('Evidence hash current '+name,hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'])
 else:check('Regression commands pass '+name,all(x['exit_code']==0 and (ROOT/x['log']).is_file() for x in json.loads(p.read_text(encoding='utf-8'))))
for entry in a['current_artifacts']:
 if 'TRACK_A' in entry['path'] or 'track-a-implementation' in entry['path']:check('Authority hash current '+entry['path'],hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()==entry['sha256'])
fixture_path='prototype-specs/TRACK_A_SEMANTIC_REVIEW_FIXTURES_v0.1.json';f=load(fixture_path);packet=(ROOT/'golden-references/TRACK-A/SEMANTIC_REVIEW_PACKET.md').read_text(encoding='utf-8')
check('Exact semantic fixture hash disclosed',hashlib.sha256((ROOT/fixture_path).read_bytes()).hexdigest() in packet)
blocks=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',packet,re.S)]
check('Four positives/eight negatives copied exactly',blocks[:-1]==f['positive_examples'] and blocks[-1]==f['negative_counterexamples'] and len(blocks[:-1])==4 and len(blocks[-1])==8)
check('Fixture isolated from runtime',all('SEMANTIC_REVIEW_FIXTURES' not in p.read_text(encoding='utf-8') for folder in ['interactions/readiness-review','learning-blocks/assessment-bundle','templates/scenario'] for p in (ROOT/folder).glob('*.js')))
for id in ['BLK-ASSESSMENT-BUNDLE-01','INT-READINESS-REVIEW-01','IP-READINESS-GATE-01']:
 check(id+' remains PROTOTYPE',next(o for o in a['candidates'] if o['id']==id)['registry_status']=='PROTOTYPE')
check('Earlier GR06 direct/semantic provenance unchanged',a['references']['GR-06']['status']=='IMPLEMENTED_PENDING_MANUAL_VALIDATION' and 'H01' in a['references']['GR-06']['semantic'] and 'PASS' in a['references']['GR-06']['semantic'] and 'user-attested' in a['references']['GR-06']['direct'])
result={'status':'PASS' if all(c['passed'] for c in checks) else 'FAIL','checks':checks};(OUT/'EVIDENCE_CONSISTENCY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':result['status'],'checks':len(checks),'failures':[c for c in checks if not c['passed']]},indent=2));raise SystemExit(result['status']!='PASS')
