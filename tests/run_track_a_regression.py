"""Existing system baselines, with Track A evidence kept in its own namespace."""
from pathlib import Path
import subprocess,json,os,sys
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'tests/track-a-implementation';OUT.mkdir(exist_ok=True)
env=os.environ.copy();env.update(GR03_RUN='track-a-regression',GR05_RUN='track-a-regression',W2_EVIDENCE_DIR='tests/track-a-implementation',PYTHONIOENCODING='utf-8',NODE_PATH=str(Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'))
commands=[['python','validators/validate_repository.py'],['python','tests/test_template_schema.py'],['python','tests/test_governed_references.py'],['python','tests/run_static_smoke.py'],['python','validators/validate_gr03.py'],['python','validators/validate_gr05.py'],['python','validators/validate_gr06.py'],['python','tools/validate_locked_build.py','locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json','golden-references/GR-01/index.html'],['python','tools/validate_locked_build.py','locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json','golden-references/GR-04/index.html'],['node','tests/test_gr05_model.mjs'],['node','tests/test_learning_state.mjs'],['node','tests/test_gr06_model.mjs'],['node','tests/test_gr06_state.mjs'],['node','tests/run_gr03_browser_validation.cjs'],['node','tests/run_gr05_browser_validation.cjs'],['node','tests/run_gr05_keyboard_resilience.cjs'],['node','tests/run_gr06_browser.cjs'],['node','tests/run_gr06_recovery.cjs']]
if '--structural' in sys.argv:commands=commands[:13]
if '--browser' in sys.argv:commands=commands[13:]
results=[]
for i,cmd in enumerate(commands):
 print('Running '+' '.join(cmd),flush=True)
 try:
  p=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=900)
  suffix='-'+Path(cmd[2]).stem if Path(cmd[1]).stem=='validate_locked_build' else ''
  log=OUT/('regression-'+Path(cmd[1]).stem+suffix+'.log');log.write_text(p.stdout+'\n'+p.stderr,encoding='utf-8')
  results.append(dict(command=cmd,exit_code=p.returncode,log=log.relative_to(ROOT).as_posix()))
  print('Exit '+str(p.returncode),flush=True)
 except Exception as e:results.append(dict(command=cmd,error=str(e)))
suffix='browser' if '--browser' in sys.argv else 'structural' if '--structural' in sys.argv else 'full'
(OUT/f'regression-{suffix}.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
raise SystemExit(any(r.get('exit_code')!=0 for r in results))
