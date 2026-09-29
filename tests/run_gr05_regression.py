"""Run non-browser GR-05/system checks and retain exact command evidence."""
from pathlib import Path
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1]
commands=[['git','branch','--show-current'],['git','rev-parse','HEAD'],['git','remote','-v'],['python','--version'],['node','--version'],['python','validators/validate_repository.py'],['python','tests/run_static_smoke.py'],['python','validators/validate_gr03.py'],['python','validators/validate_gr05.py'],['python','tests/test_template_schema.py'],['python','tools/validate_locked_build.py','locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json','golden-references/GR-01/index.html'],['python','tools/validate_locked_build.py','locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json','golden-references/GR-04/index.html'],['node','tests/test_gr05_model.mjs'],['node','tests/test_learning_state.mjs']]
commands += [['node','--check',p.relative_to(ROOT).as_posix()] for p in sorted(ROOT.rglob('*')) if p.suffix in ('.js','.cjs','.mjs') and '.git' not in p.parts]
results=[]
for command in commands:
    p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace')
    results.append({'command':command,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
data={'passed':all(x['exit_code']==0 for x in results),'commands':results,'browser_evidence':['tests/gr05-browser-review-handoff.json','tests/GR05_KEYBOARD_RESILIENCE_RESULTS.json','tests/gr03-browser-validation-gr05-regression.json'],'integrity_evidence':'tests/package-integrity.json'}
(ROOT/'tests/GR05_REGRESSION_COMMANDS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':data['passed'],'commands':len(results),'failures':[x for x in results if x['exit_code']]}));sys.exit(0 if data['passed'] else 1)
