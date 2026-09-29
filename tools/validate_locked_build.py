#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'tools'))
from render_locked_reference import load_spec,render_spec
ap=argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('html'); ap.add_argument('--output'); a=ap.parse_args()
spec=load_spec(a.spec); hp=Path(a.html); hp=hp if hp.is_absolute() else ROOT/hp
actual=hp.read_text(encoding='utf-8').replace('\r\n','\n'); expected=render_spec(spec).strip()+'\n'; errors=[]
if actual!=expected: errors.append('candidate HTML differs from deterministic locked renderer output')
for kind in ('styles','scripts'):
    for dep in spec.get('locked_dependencies',{}).get(kind,[]):
        if not (hp.parent/dep).resolve().is_file(): errors.append('missing locked dependency: '+dep)
asset=spec.get('asset')
if asset and not (hp.parent/asset['src']).resolve().is_file(): errors.append('missing locked asset: '+asset['src'])
res={'status':'pass' if not errors else 'fail','reference':spec['reference_id'],'exact_locked_render_match':actual==expected,'candidate_sha256':hashlib.sha256(actual.encode()).hexdigest(),'expected_sha256':hashlib.sha256(expected.encode()).hexdigest(),'external_python_packages_required':False,'errors':errors}
payload=json.dumps(res,indent=2)+'\n'; print(payload,end='')
if a.output:
    op=Path(a.output); op=op if op.is_absolute() else ROOT/op; op.parent.mkdir(parents=True,exist_ok=True); op.write_text(payload,encoding='utf-8')
raise SystemExit(0 if not errors else 1)
