"""Materialize the machine-readable architectural review from the reviewed tables."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[2]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def text(p):return (ROOT/p).read_text(encoding='utf-8')
main=text('WAVE_2_CONSOLIDATED_SYSTEM_REVIEW_v0.1.md')
snapshot=read('tests/wave2-review/input-snapshot.json')
registries={name:read('registries/'+name+'.json') for name in ['components','patterns','compositions','templates']}
objects={o['id']:o for r in registries.values() for o in r['objects']}
def rows(section):
 return [[v.strip() for v in line.strip().strip('|').split('|')] for line in section.splitlines() if line.startswith('| ') and not line.startswith('| ---')]
map_section=main.split('| Dimension |',1)[1].split('Source anchors:',1)[0]
architecture={gr:{} for gr in ['GR-03','GR-05','GR-06']}
for row in rows(map_section):
 if len(row)==4:
  for gr,value in zip(architecture,row[1:]):architecture[gr][row[0]]=value
dispositions=[]
for row in rows(text('WAVE_2_OBJECT_DISPOSITION_MATRIX_v0.1.md')):
 if len(row)==3 and row[0] in objects:
  id,recommendation,basis=row
  dispositions.append(dict(id=id,registry_status=objects[id]['status'],registry_version=objects[id].get('version'),recommendation=recommendation,evidence_and_scope=basis,actual_status_changed=False))
owners={
 'W2-C01':'Shared schema/registry validator owner', 'W2-C02':'Gate architecture and production-governance owner', 'W2-C03':'Shared build-repair controller and materialization-pipeline owner',
 'W2-C04':'Candidate interaction/template/artifact maintainers', 'W2-C05':'Direct technical validators and independent HRBA/instructional reviewer', 'W2-C06':'Learning/experience architecture and validation governance',
 'W2-C07':'Independent build evaluator and Gate-8 review authority', 'W2-C08':'Shared learner-state architecture owner', 'W2-C09':'Shared UI/composition/template and taxonomy owners',
 'W2-C10':'Evidence/governance owner', 'W2-C11':'Future HRBA course design and learner evaluation owner'}
corrections=[]
for row in rows(main.split('## Governed decision and correction gates',1)[1]):
 if len(row)==3 and row[0].startswith('W2-C'):
  id,title=row[0].split(' — ',1);category,acceptance=row[1:]
  timing=('MUST_FIX_BEFORE_FURTHER_REFERENCES' if id in ['W2-C01','W2-C02','W2-C03','W2-C05','W2-C06'] else 'BEFORE_AFFECTED_REUSE_OR_GATE8' if id in ['W2-C04','W2-C08'] else 'DEFER_TO_GATE8_FINAL_REVIEW' if id in ['W2-C07','W2-C09','W2-C10'] else 'FUTURE_COURSE_DESIGN')
  corrections.append(dict(id=id,title=title,category=category,timing=timing,owner=owners[id],acceptance=acceptance,status='RECOMMENDED_NOT_IMPLEMENTED'))
evidence=[
 'tests/wave2-review/input-snapshot.json','package/system-version.yaml','docs/ai-build-contract.md','docs/resource-first-workflow.md','docs/system-gap-process.md','docs/TEMPLATE_SCHEMA_RECONCILIATION.md','docs/GR03_REFRESH_PERSISTENCE_OBSERVATION.md',
 'schemas/golden-reference.schema.json','schemas/episode.schema.json','schemas/component.schema.json','validators/validate_repository.py',
 'tests/GR05_VALIDATION_RESULT.json','tests/GR05_ARCHITECTURAL_REVIEW_DECISION.json','tests/GR05_USER_ATTESTED_MANUAL_EVIDENCE.json','tests/gr03-native-zoom-validation.json','tests/gr03-browser-validation-gr06-regression.json',
 'tests/GR06_VALIDATION_RESULT.json','tests/GR06_MANUAL_EVIDENCE.json','tests/GR06_REGRESSION_COMMANDS.json','tests/GR06_BROWSER_RESULTS.json','tests/GR06_RECOVERY_RESULTS.json','tests/GR06_MODEL_RESULTS.json','tests/GR06_STATE_RESULTS.json','tests/GR06_STATIC_RESULTS.json','tests/GR06_EVIDENCE_CONSISTENCY.json',
 'tests/gr05-browser-gr06-regression.json','tests/GR05_KEYBOARD_RESILIENCE_RESULTS.json','tests/GR05_MODEL_RESULTS.json','tests/GR05_STATE_SERVICE_RESULTS.json',
 'interactions/labeled-graphic/labeled-graphic.js','interactions/build-repair/model.js','interactions/build-repair/build-repair.js','interactions/evidence-decision/model.js','interactions/evidence-decision/evidence-decision.js',
 'learning-blocks/perspective/manifest.yaml','learning-blocks/work-artifact/work-artifact.js','learning-blocks/evidence-ledger/evidence-ledger.js','templates/deep-workspace/deep-workspace.js','state/learning-state/learning-state.js','state/learning-state/manifest.yaml','compositions/repair-studio/repair-studio.css','compositions/evidence-decision/source-interpretation-decision-update.css','compositions/perspective/perspective.css','compositions/evidence-decision/evidence-decision.css',
 'docs/patterns/build-repair/README.md','docs/patterns/evidence-decision/README.md','tools/build_gr05.py','golden-references/GR-05/index.html',
 'prototype-specs/GR-05_RESOURCE_FIRST_PREFLIGHT_v0.1.md','prototype-specs/GR-05_RESOURCE_INVENTORY_v0.1.json','prototype-specs/GR-05_ARCHITECTURAL_CORRECTIONS_AND_CANDIDATES_v0.1.md','prototype-specs/GR-06_RESOURCE_FIRST_PREFLIGHT_v0.1.md','prototype-specs/GR-06_RESOURCE_INVENTORY_v0.1.json',
 'tests/gr03-screenshots/gr06-regression-1440x900-initial.png','tests/gr05-screenshots/gr06-regression-1440x900-draft.png','tests/gr06-screenshots/1440x900-update.png',
 'tests/gr03-screenshots/gr06-regression-stress-320x568-feedback-completed.png','tests/gr05-screenshots/gr06-regression-max-content-comparison.png','tests/gr06-screenshots/stress-320-final.png']
for gr in ['GR-03','GR-05','GR-06']:
 evidence += [f'prototype-specs/{gr}_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json',f'prototype-specs/{gr}_VALIDATION_MATRIX_v0.1.md',f'golden-references/{gr}/spec.yaml',f'golden-references/{gr}/{gr}_BUILD_MANIFEST.json']
for registry in registries:evidence += [f'registries/{registry}.json',f'registries/{registry}.yaml']
for gr in ['GR-01','GR-04']:evidence.append(f'locked-build-specs/{gr}_LOCKED_BUILD_v0.1.json')
evidence += ['tests/wave2-review/visual-evidence.json']+[p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'tests/wave2-review').glob('*.png'))]
findings=[
 dict(id='W2-F01',finding='Generic validator accepts unknown non-template IDs, composition variants and build modes in ordinary GR specs',certainty='REPRODUCED_TEMPORARY_COPY_PROBES',evidence=['validators/validate_repository.py','tests/wave2-review/consistency-results.json'],correction='W2-C01'),
 dict(id='W2-F02',finding='GR05 visible mojibake exists in rendered evidence and controller/generator output',certainty='SOURCE_AND_EXISTING_SCREENSHOT_INSPECTED',evidence=['tools/build_gr05.py','golden-references/GR-05/index.html','interactions/build-repair/build-repair.js','tests/wave2-review/GR05-existing-evidence-top.png'],correction='W2-C03'),
 dict(id='W2-F03',finding='GR05/06 have distinct pedagogical/state logic but closely similar form/document presentation',certainty='ARCHITECTURAL_AND_VISUAL_JUDGMENT_NOT_LEARNER_STUDY',evidence=['tests/wave2-review/GR05-existing-evidence-top.png','tests/wave2-review/GR06-existing-evidence-top.png','compositions/repair-studio/repair-studio.css','compositions/evidence-decision/source-interpretation-decision-update.css'],correction='W2-C06'),
 dict(id='W2-F04',finding='Service is genuinely reused unchanged with independent activity validators and no completion authority',certainty='CODE_HASH_AND_AUTOMATED_EVIDENCE',evidence=['state/learning-state/learning-state.js','tests/GR06_STATIC_RESULTS.json','tests/GR06_STATE_RESULTS.json','tests/GR05_STATE_SERVICE_RESULTS.json'],correction=None),
 dict(id='W2-F05',finding='Candidate configurable interfaces contain fixed-case assumptions and generic UI helpers reside in a semantic block',certainty='SOURCE_INSPECTION',evidence=['learning-blocks/perspective/manifest.yaml','interactions/labeled-graphic/labeled-graphic.js','interactions/build-repair/model.js','learning-blocks/work-artifact/work-artifact.js','templates/deep-workspace/deep-workspace.js'],correction='W2-C04'),
 dict(id='W2-F06',finding='GR06 direct technical and independent semantic validation remain incomplete',certainty='CURRENT_GOVERNED_EVIDENCE',evidence=['tests/GR06_MANUAL_EVIDENCE.json','tests/GR06_VALIDATION_RESULT.json'],correction='W2-C05'),
 dict(id='W2-F07',finding='Complete upstream Gate1–8 and original GR07–10 allocation not located in bounded authority search',certainty='SOURCE_AVAILABILITY_LIMIT_NOT_ABSENCE_PROOF',evidence=['package/system-version.yaml','docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md'],correction='W2-C02')]
data=dict(review_id='WAVE_2_SYSTEM_REVIEW',version='0.1',recorded_at=datetime.now(timezone.utc).isoformat(),outcome='WAVE_2_PASS_WITH_BOUNDED_CORRECTIONS',decision_authority='Codex architectural review recommendation for ChatGPT review',golden_reference_acceptance=False,system_v1_freeze=False,candidate_status_changes=False,production_code_changed=False,next_reference_started=False,pm_stress_test_started=False,hrba_reconstruction_started=False,
 repository=dict(branch=snapshot['branch'],head=snapshot['head'],scope='Current working tree, including uncommitted GR06 implementation; HEAD alone is not the reviewed build',input_snapshot='tests/wave2-review/input-snapshot.json',input_package_manifest_sha256=snapshot['input_package_manifest_sha256'],remote_or_push_action=False),
 authority_limit=dict(full_gate_1_8_source_verified=False,original_GR07_10_allocation_verified=False,clarification_requested=True,limitation='No complete upstream authority located in repository or bounded nearby filename search; coverage groupings remain proposals conditional on source reconciliation.'),
 strategic_requirements={'Magnetic Experience':'BOUNDED_CORRECTIONS_REQUIRED','Transformative Learning':'CAPABILITY_ARCHITECTURE_DEMONSTRATED_TRANSFER_UNPROVEN_GR06_SEMANTICS_PENDING','Resilient System':'PROTOTYPE_REUSE_DEMONSTRATED_GOVERNANCE_AND_DIRECT_EVIDENCE_GAPS'},
 reference_statuses={'GR-03':'PASS_FOR_WAVE_2_SYSTEM_REVIEW','GR-05':'PASS_FOR_WAVE_2_SYSTEM_REVIEW','GR-06':'IMPLEMENTED_PENDING_MANUAL_VALIDATION'},architecture_map=architecture,findings=findings,object_dispositions=dispositions,corrections=corrections,
 state_recommendation=dict(GR03='RETAIN_BOUNDED_TRANSIENT_EXCEPTION_NO_RETROACTIVE_CODE_CHANGE',authored_work='AUTOMATIC_SESSION_RECOVERY_EXPLICIT_DURABLE_OPT_IN',service='GENERIC_STORAGE_ONLY_NEVER_COMPLETION_AUTHORITY',future_GR03_migration_trigger='Resumable course/portfolio or assessed prerequisite reuse requires approved shared adapter and preview isolation'),
 regression_evidence=dict(provenance='Existing GR06 handoff runs inspected, not rerun by this architectural task',counts=read('tests/GR06_VALIDATION_RESULT.json')['counts'],GR01_GR04_exact_locks='PASS_RECORDED',GR03_runner_caveat='423 checks and automated_pass true; generic raw overall FAIL omits earlier manual attestation, not a new production regression',package_integrity_at_input='PASS_RECORDED_687_FILES',independent_AI_duplicate_builds_for_Wave2='NOT_DEMONSTRATED'),
 manual_evidence=dict(GR03_native200='USER_ATTESTED_PASS',GR03_actual_reader='NOT_IDENTIFIED',GR05_native200_reader_mobile='USER_ATTESTED_PASS',GR05_V05_V25='CHATGPT_REVIEW_PASS_REPORTED_BY_USER',GR06_native200_reader_mobile_H01_H09='PENDING_UNCHANGED',current_review_supplies_no_new_manual_or_semantic_pass=True),
 remaining_coverage=dict(recommended_minimum_additional_prototype_tracks=2,numbering_status='PROPOSED_NOT_AUTHORIZED_RECONCILE_UPSTREAM_IDS',tracks=[dict(id='TRACK_A',title='Integrated evidence review and readiness gate',coverage=['decision/gate','integrated assessment']),dict(id='TRACK_B',title='Practice portfolio, dialogue and consented ecosystem handoff',coverage=['practice/transfer portfolio','course-to-practice and practice-to-Hub bridge','peer/practice-evidence dialogue','ecosystem contribution/co-creation'])],conditional_split='Add a separate ecosystem/peer reference only if distinct authority/moderation/integration lifecycle cannot be demonstrated coherently within Track B. Never cancel original GR07–10 assignments without authority reconciliation.'),
 deliverables=['WAVE_2_CONSOLIDATED_SYSTEM_REVIEW_v0.1.md','WAVE_2_OBJECT_DISPOSITION_MATRIX_v0.1.md','WAVE_2_REMAINING_COVERAGE_AND_NEXT_REFERENCES_v0.1.md','WAVE_2_SYSTEM_REVIEW.json'],consistency_evidence='tests/wave2-review/consistency-results.json',evidence_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(set(evidence))})
(ROOT/'WAVE_2_SYSTEM_REVIEW.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(objects=len(dispositions),corrections=len(corrections),map_dimensions={k:len(v) for k,v in architecture.items()},evidence_files=len(data['evidence_hashes'])),indent=2))
