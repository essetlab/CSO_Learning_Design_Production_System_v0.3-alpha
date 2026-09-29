"""Current user attestation and specification authorization; no runtime mutation."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def write(p,d):(ROOT/p).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def apply():
 authority_path='governance/TRACK_A_PREFLIGHT_AUTHORITY.json'
 if not (ROOT/authority_path).exists():return
 authority=read(authority_path);a=authority['GR06_native_zoom']
 r=read('tests/GR06_VALIDATION_RESULT.json');r['manual']=[x for x in r['manual'] if x['id']!='V18'];r['user_attested_native_zoom']=a
 for x in r['matrix']:
  if x['id']=='V18':x.update(status='PASS_USER_ATTESTED',note='User explicitly reports native Chrome 200% PASS. Codex did not perform this check.',evidence=[authority_path])
 write('tests/GR06_VALIDATION_RESULT.json',r)
 m=read('tests/GR06_MANUAL_EVIDENCE.json');m['checks']=r['manual'];m['direct_technical_attestations']=[a];m['status']='TWO_TECHNICAL_CHECKS_PENDING';write('tests/GR06_MANUAL_EVIDENCE.json',m)
 m=read('golden-references/GR-06/GR-06_BUILD_MANIFEST.json');m['pending_direct_checks']=[x['id'] for x in r['manual']];m['user_attested_native_zoom']=a;write('golden-references/GR-06/GR-06_BUILD_MANIFEST.json',m)
 for p in ['golden-references/GR-06/GR-06_RESULT_SUMMARY.md','golden-references/GR-06/MANUAL_VALIDATION.md','README.md']:
  path=ROOT/p;s=path.read_text(encoding='utf-8')
  s=s.replace('Three direct technical checks remain pending.','Actual screen-reader and physical-mobile software-keyboard checks remain pending. Native Chrome 200% is user-attested PASS.')
  s=s.replace('- V18 genuine Chrome 200%: PENDING.','- V18 genuine Chrome 200%: PASS, user-attested; see governance/TRACK_A_PREFLIGHT_AUTHORITY.json. No new Codex performance claimed.')
  s=s.replace('**three direct technical checks PENDING; H01–H09 semantic review PASS**','**screen-reader and physical-mobile checks PENDING; native Chrome 200% user-attested PASS; H01–H09 semantic review PASS**')
  s=s.replace('no direct technical attestation has been received for GR-06.','native Chrome 200% PASS was explicitly attested by the user in the Track A request. Performer/device/date details were not supplied; none are invented.')
  s=s.replace('Result: **PENDING**. Provenance must identify the person who performed this check.','Result: **PASS — USER_ATTESTED**. Source: the user’s Track A request. Native Chrome 200% was reported PASS; Codex did not perform it. No additional date/device/screenshot details were supplied.')
  s=s.replace('Genuine Chrome 200%, actual screen-reader use and physical-mobile software-keyboard checks remain pending.','Native Chrome 200% is user-attested PASS; actual screen-reader use and physical-mobile software-keyboard checks remain pending.')
  path.write_text(s,encoding='utf-8')
 index=read('WAVE_2_CURRENT_AUTHORITY.json');index['latest_authority']=authority_path;index['authority_precedence'][0]='Latest explicit user decisions: governance/TRACK_A_PREFLIGHT_AUTHORITY.json then prior Wave-2 update within retained scope'
 index['tracks']['A']='SPECIFICATION_ONLY_AUTHORIZED_NOT_FROZEN';index['references']['GR-06']['direct']='Native Chrome 200% PASS, user-attested; actual screen reader and physical-mobile software keyboard PENDING'
 index['GR06_design_learning']=authority['GR06_design_learning']
 index['track_a_specification_package']={'status':'PROPOSED_NOT_FROZEN','result':'TRACK_A_READY_FOR_ARCHITECTURAL_FREEZE_REVIEW','implementation_authorized':False,'files':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'prototype-specs').glob('TRACK_A_*')) if p.is_file()}}
 for x in index['remaining_gate8_capability_coverage']:
  x['remaining']=x['remaining'].replace('GR06 three direct checks','GR06 screen-reader and physical-mobile direct checks')
 write('WAVE_2_CURRENT_AUTHORITY.json',index)
 p=ROOT/'WAVE_2_CURRENT_AUTHORITY.md';s=p.read_text(encoding='utf-8')
 s=s.replace('Track A and Track B remain proposed groupings, with no implementation authorization.','Track A preflight/specification is now authorized by the [latest user decision](governance/TRACK_A_PREFLIGHT_AUTHORITY.json), but is NOT FROZEN and has no implementation authorization. Track B remains proposed and unauthorized.')
 s=s.replace('Native Chrome 200%, actual screen reader and physical-mobile software keyboard PENDING','Native Chrome 200% PASS, user-attested; actual screen reader and physical-mobile software keyboard PENDING')
 s=s.replace('its three direct checks alone remain pending','native Chrome 200% is user-attested PASS; its screen-reader and physical-mobile checks remain pending')
 s=s.replace('GR06 three direct checks','GR06 screen-reader and physical-mobile checks')
 s=s.replace('HRBA reconstruction, Track A/B or new reference is authorized by this index.','HRBA reconstruction, Track A/B implementation or new reference build is authorized by this index. Track A specification-only authorization is recorded in the latest decision.')
 if '## Track A specification authorization' not in s:s+='\n## Track A specification authorization\n\nLatest authority: [Track A request and GR06 attestation](governance/TRACK_A_PREFLIGHT_AUTHORITY.json). It supersedes earlier Track A no-work language only for preflight/specification. GR06 is an upper bound on authored-work burden, not a future screen template. Track A must substantially reduce writing and distinguish its review rhythm. Exact prior index/evidence bytes are retained under tests/track-a-preflight/baseline.\n'
 if 'TRACK_A_RESOURCE_FIRST_PREFLIGHT' not in s:s+='\nProposed package: [resource-first preflight](prototype-specs/TRACK_A_RESOURCE_FIRST_PREFLIGHT_v0.1.md), [deterministic design](prototype-specs/TRACK_A_DETERMINISTIC_LEARNING_DESIGN_v0.1.md), [exact JSON contract](prototype-specs/TRACK_A_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) and [validation matrix](prototype-specs/TRACK_A_VALIDATION_MATRIX_v0.1.md). Status: TRACK_A_READY_FOR_ARCHITECTURAL_FREEZE_REVIEW, NOT FROZEN. No registration or prototype authorization.\n'
 p.write_text(s,encoding='utf-8')
 from apply_track_a_implementation_authority import apply as apply_implementation
 apply_implementation()
if __name__=='__main__':apply()
