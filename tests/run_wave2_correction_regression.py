"""Current bounded-correction command evidence; historical reports remain separate."""
from pathlib import Path
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1]
commands=[['python','validators/validate_repository.py','--output','tests/wave2-corrections/REPOSITORY_VALIDATION.json'],['python','tests/test_template_schema.py'],['python','tests/test_governed_references.py'],['python','tests/run_static_smoke.py'],['python','validators/validate_gr03.py'],['python','validators/validate_gr05.py'],['python','validators/validate_gr06.py'],['python','tools/validate_locked_build.py','locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json','golden-references/GR-01/index.html'],['python','tools/validate_locked_build.py','locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json','golden-references/GR-04/index.html'],['node','tests/test_gr05_model.mjs'],['node','tests/test_learning_state.mjs'],['node','tests/test_gr06_model.mjs'],['node','tests/test_gr06_state.mjs'],['python','tests/check_gr06_evidence.py']]
commands += [['node','--check',p.relative_to(ROOT).as_posix()] for p in sorted(ROOT.rglob('*')) if p.suffix in ('.js','.cjs','.mjs') and '.git' not in p.parts and 'baseline' not in p.parts]
results=[]
for command in commands:
 p=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace');results.append(dict(command=command,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr))
data=dict(passed=all(x['exit_code']==0 for x in results),commands=results)
(ROOT/'tests/wave2-corrections/REGRESSION_COMMANDS.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=data['passed'],commands=len(results),failures=[x for x in results if x['exit_code']]),indent=2));sys.exit(0 if data['passed'] else 1)
