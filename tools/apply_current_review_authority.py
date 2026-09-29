"""Apply explicit recorded human authority to current metadata, never infer passes."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def write(p,d):(ROOT/p).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def apply():
 path='governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json'
 if not (ROOT/path).exists():return
 decision=read(path);semantic=decision['GR06_semantic_review']
 assert semantic['status']=='PASS' and semantic['dimensions']==[f'H{i:02}' for i in range(1,10)]
 for reviewed_path,expected_hash in semantic['reviewed_hashes'].items():
  assert hashlib.sha256((ROOT/reviewed_path).read_bytes()).hexdigest()==expected_hash, 'Reviewed content changed: '+reviewed_path
 r=read('tests/GR06_VALIDATION_RESULT.json');r['manual']=[x for x in r['manual'] if x['id']!='V21']
 r['semantic_review']={**semantic,'authority_record':path}
 for x in r['matrix']:
  if x['id'] in ['V09','V21']:
   x['status']='PASS';x['note']='Structural automated evidence and separate ChatGPT H01–H09 semantic review PASS, explicitly reported by the user. No new Codex semantic judgment.'
   if path not in x['evidence']:x['evidence'].append(path)
 write('tests/GR06_VALIDATION_RESULT.json',r)
 m=read('tests/GR06_MANUAL_EVIDENCE.json');m['checks']=r['manual']
 m['human_dimensions']=[dict(id=id,status='PASS',reviewer=semantic['reviewer'],provenance=semantic['provenance'],authority_record=path) for id in semantic['dimensions']]
 m['attestations']=[semantic];m['direct_technical_attestations']=[];m['status']='TECHNICAL_CHECKS_PENDING_SEMANTIC_PASS'
 write('tests/GR06_MANUAL_EVIDENCE.json',m)
 manifest=read('golden-references/GR-06/GR-06_BUILD_MANIFEST.json');manifest['semantic_review']=dict(status='PASS',authority_record=path,provenance=semantic['provenance']);manifest['pending_direct_checks']=[x['id'] for x in r['manual']]
 write('golden-references/GR-06/GR-06_BUILD_MANIFEST.json',manifest)
 p=ROOT/'golden-references/GR-06/GR-06_RESULT_SUMMARY.md';s=p.read_text(encoding='utf-8')
 s=s.replace('Direct technical checks and independent semantic review remain pending.','H01–H09 independent semantic review is PASS (ChatGPT review, explicitly reported by the user). Three direct technical checks remain pending.')
 s=s.replace('## Manual and semantic work still required','## Current human evidence')
 s=s.replace('- V21 independent H01–H09 instructional/HRBA judgment: PENDING. V09 quality review depends on this judgment.','- V21 H01–H09 and V09 semantic quality: PASS, ChatGPT review reported by the user; see `../../governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json`.')
 s=s.replace('and has no semantic pass.','and has received the separate ChatGPT semantic PASS recorded above. Its original embedded pending label is preserved historical fixture metadata, superseded by the authority record.')
 p.write_text(s,encoding='utf-8')
 p=ROOT/'golden-references/GR-06/MANUAL_VALIDATION.md';s=p.read_text(encoding='utf-8')
 s=s.replace('Status: **PENDING**. No user attestation or independent semantic judgment has been received for GR-06.','Status: **three direct technical checks PENDING; H01–H09 semantic review PASS**. ChatGPT semantic review was explicitly reported by the user; no direct technical attestation has been received for GR-06.')
 s=s.replace('All nine judgments are **PENDING**.','All nine judgments are **PASS**, ChatGPT review explicitly reported by the user in the bounded-correction authorization. See `../../governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json` for provenance and reviewed fixture/packet hashes. The original checklist is preserved in `../../tests/wave2-corrections/baseline/golden-references/GR-06/MANUAL_VALIDATION.md`.')
 p.write_text(s,encoding='utf-8')
 from apply_track_a_authority import apply as apply_latest
 apply_latest()
 return dict(status=r['status'],semantic_review='PASS',direct_pending=len(read('tests/GR06_VALIDATION_RESULT.json')['manual']))
if __name__=='__main__':print(json.dumps(apply(),indent=2))
