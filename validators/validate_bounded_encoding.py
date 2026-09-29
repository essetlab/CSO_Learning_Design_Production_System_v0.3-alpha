"""Narrow W2-C03 exception: exact declared punctuation repairs, no behavior edits."""
from pathlib import Path
import hashlib,json
def validate(root):
 root=Path(root);base=root/'tests/wave2-corrections/baseline'
 proof=json.loads((root/'tests/wave2-corrections/GR05_ENCODING_SOURCE_PROOF.json').read_text(encoding='utf-8'))
 expected={'tools/build_gr05.py','interactions/build-repair/build-repair.js','golden-references/GR-05/index.html','golden-references/GR-05/exercise.txt'}
 replacements={'\u00c2\u00b7':'\u00b7','\u00e2\u20ac\u201c':'\u2013','\u00e2\u20ac\u201d':'\u2014'}
 if proof['replacement_map']!=replacements or {c['path'] for c in proof['checks']}!=expected:return False
 baseline=json.loads((root/'tests/wave2-corrections/BASELINE.json').read_text(encoding='utf-8'))['hashes']
 for entry in proof['checks']:
  p=entry['path'];old=(base/p).read_bytes();new=(root/p).read_bytes()
  if hashlib.sha256(old).hexdigest()!=baseline[p] or hashlib.sha256(new).hexdigest()!=entry['after_sha256']:return False
  text=old.decode('utf-8').replace('\r\n','\n')
  for a,b in replacements.items():text=text.replace(a,b)
  if text!=new.decode('utf-8').replace('\r\n','\n'):return False
 return True
