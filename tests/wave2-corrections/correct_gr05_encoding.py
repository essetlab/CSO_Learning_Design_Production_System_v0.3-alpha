"""One-time bounded UTF-8 repair, proven against preserved pre-correction sources."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[2]
base=ROOT/'tests/wave2-corrections/baseline'
replacements={'\u00c2\u00b7':'\u00b7','\u00e2\u20ac\u201c':'\u2013','\u00e2\u20ac\u201d':'\u2014'}
sources=['tools/build_gr05.py','interactions/build-repair/build-repair.js']
outputs=['golden-references/GR-05/index.html','golden-references/GR-05/exercise.txt']
def normalize(text):
 for old,new in replacements.items():text=text.replace(old,new)
 return text
for p in sources:
 old=(base/p).read_text(encoding='utf-8');current=(ROOT/p).read_text(encoding='utf-8')
 assert current in [old,normalize(old)],f'Unexpected intervening source change: {p}'
 (ROOT/p).write_text(normalize(old),encoding='utf-8')
subprocess.run(['python','tools/build_gr05.py'],cwd=ROOT,check=True)
checks=[]
for p in sources+outputs:
 old=(base/p).read_text(encoding='utf-8');new=(ROOT/p).read_text(encoding='utf-8')
 checks.append(dict(path=p,passed=normalize(old)==new and not any(x in new for x in replacements),replacements={k:old.count(k) for k in replacements if k in old},before_sha256=hashlib.sha256((base/p).read_bytes()).hexdigest(),after_sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()))
result=dict(status='PASS' if all(c['passed'] for c in checks) else 'FAIL',authority='W2-C03',scope='Only UTF-8 punctuation replacement in generator/shared view and generated output; no model, state, content-contract, CSS or candidate interface change.',historical_disclosure='The earlier GR05 Wave-2 pass contained these visible encoding defects. This is a later bounded polish correction, not a rewritten earlier review.',replacement_map=replacements,checks=checks)
(ROOT/'tests/wave2-corrections/GR05_ENCODING_SOURCE_PROOF.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
assert result['status']=='PASS'
print(json.dumps(result,indent=2))
