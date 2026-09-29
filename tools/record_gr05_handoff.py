"""Assemble evidence without converting unperformed manual checks into passes."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
def read(rel):return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def write(rel,value):(ROOT/rel).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
browser=read('tests/gr05-browser-review-handoff.json')
keyboard=read('tests/GR05_KEYBOARD_RESILIENCE_RESULTS.json')
model=read('tests/GR05_MODEL_RESULTS.json');service=read('tests/GR05_STATE_SERVICE_RESULTS.json');static=read('tests/GR05_STATIC_RESULTS.json');regression=read('tests/GR05_REGRESSION_COMMANDS.json');gr03=read('tests/gr03-browser-validation-gr05-regression.json')
automated=all([browser['passed'],keyboard['passed'],model['passed'],service['passed'],static['status']=='PASS',regression['passed'],all(x['passed'] for x in gr03['checks']),not gr03['errors']])
pending={'V05':'Human deep-work instructional review','V21':'Genuine Chrome native 200% full flow and indicator evidence','V22':'Physical mobile software-keyboard occlusion check; automated keyboard flow passes','V23':'Actual screen-reader walkthrough; structural accessibility checks pass','V25':'Human HRBA semantic review of a completed concise artifact'}
manual_path='tests/GR05_USER_ATTESTED_MANUAL_EVIDENCE.json'
manual=read(manual_path) if (ROOT/manual_path).exists() else {'checks':[]}
attested={x['id']:x for x in manual['checks'] if x['result']=='PASS' and x['evidence_type']=='USER_ATTESTATION'}
for key in attested:
    pending.pop(key,None)
review_path='tests/GR05_ARCHITECTURAL_REVIEW_DECISION.json'
review=read(review_path) if (ROOT/review_path).exists() else None
semantic_packet='golden-references/GR-05/GR-05_V25_SEMANTIC_REVIEW_PACKET.md'
if review and review['V05']=='PASS':
    pending.pop('V05',None)
    pending['V25']='ChatGPT final semantic judgment on separate criterion-specific synthetic review fixture; substantive artifact already passed review.'
if review and review.get('V25')=='PASS':
    pending.pop('V25',None)
matrix=[]
for n in range(1,31):
    key=f'V{n:02}'
    matrix.append({'id':key,'status':'PENDING_MANUAL' if key in pending else 'AUTOMATED_PASS' if automated else 'CHECK_AUTOMATED_FAILURE','note':pending.get(key,'See per-assertion browser, model/service, static and command evidence; automated scope only.')})
    if key in attested:
        matrix[-1].update(status='PASS_USER_ATTESTED',note=attested[key]['scope']+'; performed and reported by the user, not independently performed or verified by Codex.',manual_evidence=manual_path)
    if key in ('V05','V25') and review and review.get(key)=='PASS':
        matrix[-1].update(status='PASS_REVIEW_REPORTED',note=key+' PASS from ChatGPT architectural/HRBA review, communicated by the user; separate from automated and user-performed technical checks.',review_evidence=review_path)
result={'reference':'GR-05','final_status':'IMPLEMENTED_PENDING_MANUAL_VALIDATION' if automated else 'FAIL_AUTOMATED_VALIDATION','target_status':'PASS_FOR_WAVE_2_SYSTEM_REVIEW','candidate_status':'PROTOTYPE','golden_reference_accepted':False,'GR06_started':False,'automated_pass':automated,'user_direction':'Return the build with those checks pending (chat reply).','counts':{'browser':len(browser['checks']),'keyboard_resilience':len(keyboard['checks']),'model':len(model['checks']),'state_service':len(service['checks']),'static':len(static['checks']),'regression_commands':len(regression['commands']),'GR03_browser_stress':len(gr03['checks'])},'matrix':matrix,'evidence':['tests/gr05-browser-review-handoff.json','tests/GR05_KEYBOARD_RESILIENCE_RESULTS.json','tests/GR05_MODEL_RESULTS.json','tests/GR05_STATE_SERVICE_RESULTS.json','tests/GR05_STATIC_RESULTS.json','tests/GR05_REGRESSION_COMMANDS.json','tests/gr03-browser-validation-gr05-regression.json','tests/gr05-defect-log.md','golden-references/GR-05/MANUAL_VALIDATION.md'],'integrity_receipt':'tests/package-integrity.json'}
if attested:
    result['user_direction']='Record user-attested V21/V23 and physical-mobile V22 PASS; retain IMPLEMENTED_PENDING_MANUAL_VALIDATION until ChatGPT V25 judgment.'
    result['evidence'] += [manual_path,'golden-references/GR-05/GR-05_V25_REVIEW_PACKET.md']
    result['pending_manual']=pending
if review:
    result['evidence'] += [review_path,semantic_packet,'tests/gr05-v25-semantic-review-fixture.json','tests/GR05_V25_SEMANTIC_FIXTURE_CHECKS.json']
    result['user_direction']='V05 PASS; keep GR-05 status unchanged and return the separate criterion-specific V25 semantic review packet for ChatGPT judgment.'
if automated and not pending:
    result['final_status']='PASS_FOR_WAVE_2_SYSTEM_REVIEW'
    result['user_direction']='Close GR-05 at Wave 2 system review pass; candidates stay PROTOTYPE; GR-06 preflight only authorized separately.'
write('tests/GR05_VALIDATION_RESULT.json',result)
folders=['golden-references/GR-05','interactions/build-repair','learning-blocks/work-artifact','compositions/repair-studio','templates/deep-workspace','state/learning-state','docs/patterns/build-repair']
sources=[p for folder in folders for p in (ROOT/folder).iterdir() if p.suffix in ('.js','.css','.html','.yaml','.txt')]
sources.append(ROOT/'prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json')
manifest={'reference':'GR-05','build_id':'BUILD-GR-05-W2-0001','specification_checkpoint':'63133cbb0cfc0052b216502f5f94cf16ea579137','branch':subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),'contract_revision':2,'candidate_objects':['IP-BUILD-REPAIR-01','BLK-WORK-ARTIFACT-01','INT-BUILD-REPAIR-01','CMP-REPAIR-STUDIO-01','TPL-DEEP-WORKSPACE-01','SVC-LEARNING-STATE-01'],'candidate_objects_status':'PROTOTYPE','completion':'D && A && R1 && C && R2 && F','automated_pass':automated,'final_status':result['final_status'],'pending_manual':pending,'validation_result':'tests/GR05_VALIDATION_RESULT.json','package_integrity':'tests/package-integrity.json','source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(sources)}}
if attested:
    manifest['user_attested_manual_evidence']=manual_path
    manifest['user_attested_passes']=list(attested)
    manifest['V25_review_packet']='golden-references/GR-05/GR-05_V25_REVIEW_PACKET.md'
if review:
    manifest['review_decision_evidence']=review_path
    manifest['V05']='PASS_REVIEW_REPORTED'
    manifest['V25']='PASS_REVIEW_REPORTED' if review.get('V25')=='PASS' else 'PENDING_MANUAL'
    manifest['V25_review_packet']=semantic_packet
write('golden-references/GR-05/GR-05_BUILD_MANIFEST.json',manifest)
print(json.dumps({'status':result['final_status'],'counts':result['counts']},indent=2))
