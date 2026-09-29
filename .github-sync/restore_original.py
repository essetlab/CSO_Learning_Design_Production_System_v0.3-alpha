"""Recover original history and working files into a NEW destination only."""
from pathlib import Path
import argparse,hashlib,json,subprocess,tempfile,shutil
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--destination',required=True);args=ap.parse_args()
 source=Path(__file__).resolve().parents[1];metadata=json.loads((source/'.github-sync/ORIGINAL_HISTORY.json').read_text(encoding='utf-8'));inventory=json.loads((source/'.github-sync/WORKING_TREE_INVENTORY.json').read_text(encoding='utf-8'))
 dest=Path(args.destination).resolve()
 if dest.exists():raise SystemExit('Destination already exists. Choose a new path; nothing was changed.')
 def path_under(base,relative):
  path=(base/relative).resolve()
  if not path.is_relative_to(base.resolve()) or '.git' in Path(relative).parts:raise ValueError('Unsafe path: '+relative)
  return path
 for e in inventory['files']:
  p=path_under(source,e['path'])
  if not p.is_file() or p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:raise SystemExit('Missing/changed/LFS-unhydrated file: '+e['path']+'; run git lfs pull and verify the checkout.')
 for e in metadata['bundle']['parts']:
  p=path_under(source,e['path'])
  if not p.is_file() or p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:raise SystemExit('Invalid or unhydrated history part: '+e['path'])
 with tempfile.TemporaryDirectory(prefix='cso-history-recovery-') as tmp:
  bundle=Path(tmp)/'original-history.bundle'
  with bundle.open('wb') as target:
   for e in metadata['bundle']['parts']:
    with path_under(source,e['path']).open('rb') as stream:shutil.copyfileobj(stream,target,8*1024*1024)
  if sha(bundle)!=metadata['bundle']['sha256']:raise SystemExit('Bundle checksum mismatch; destination not created.')
  subprocess.run(['git','init',str(dest)],check=True)
  def git(*a,data=None):return subprocess.check_output(['git','-C',str(dest),*a],input=data)
  git('config','core.autocrlf',metadata['source_core_autocrlf'])
  git('fetch','--no-tags',str(bundle),'refs/heads/*:refs/heads/*','refs/tags/*:refs/tags/*')
  refs={line.split()[0]:line.split()[1] for line in git('for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/tags').decode().splitlines()}
  if refs!={r['ref']:r['oid']for r in metadata['original_refs']}:raise RuntimeError('Restored ref mismatch; recovered repository retained for inspection.')
  git('fsck','--full','--strict');git('symbolic-ref','HEAD','refs/heads/'+metadata['source_branch'])
  git('read-tree','--empty')
  index=b''.join(f"{e['mode']} {e['oid']} {e['stage']}\t{e['path']}\0".encode('utf-8') for e in metadata['original_index'])
  git('update-index','-z','--index-info',data=index)
  for e in inventory['files']:
   target=path_under(dest,e['path']);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path_under(source,e['path']),target)
  print('Recovered exact original history and current working-file bytes at '+str(dest))
  print(git('status','--short').decode('utf-8'))
if __name__=='__main__':main()
