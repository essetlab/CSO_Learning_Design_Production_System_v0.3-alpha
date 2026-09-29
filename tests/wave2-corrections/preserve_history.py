"""Copy superseded file bytes from the verified original review ZIP, without editing it."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[2]
baseline=json.loads((ROOT/'tests/wave2-corrections/BASELINE.json').read_text(encoding='utf-8'))
archive=ROOT/baseline['review_archive']
assert hashlib.sha256(archive.read_bytes()).hexdigest()==baseline['review_archive_sha256']
with zipfile.ZipFile(archive) as z:
 for p,h in baseline['hashes'].items():
  current=ROOT/p
  if current.exists() and hashlib.sha256(current.read_bytes()).hexdigest()==h:continue
  target=ROOT/'tests/wave2-corrections/baseline'/p
  assert target.resolve().is_relative_to((ROOT/'tests/wave2-corrections/baseline').resolve())
  data=z.read(ROOT.name+'/'+p);assert hashlib.sha256(data).hexdigest()==h,p
  if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==h,p
  else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
print('Superseded file bytes preserved; original review archive unchanged.')
