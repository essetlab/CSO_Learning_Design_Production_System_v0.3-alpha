"""Materialize the W2-C06 authoring contract; does not create a Golden Reference."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
def write(path,data): (ROOT/path).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fields={
 'professional_capability':'Observable professional capability and authentic transfer context.',
 'dominant_learner_action':'What learners primarily do; distinguish the action from the UI control.',
 'emotional_cognitive_rhythm':'Intended attention, uncertainty, effort, feedback and relief over time.',
 'visual_interaction_metaphor':'Principal metaphor using governed visual resources; no new visual system implied.',
 'density_scroll_expectation':'Expected information density, scroll length and maximum-content behavior.',
 'reference_work_balance':'What remains available as reference while the learner works, and why.',
 'authored_writing_burden':'Authored fields, hard maxima, structural sufficiency and concise guidance; justify any pedagogically necessary minimum.',
 'desktop_mobile_transformation':'Changes in arrangement, reading order, controls and comparisons at existing breakpoints.',
 'magnetic_experience_moment':'Specific moment of curiosity, agency or meaningful discovery, with a testable rationale.',
 'reuse_rationale':'Registered patterns/components and variants, their fit and limits; declare System Gaps explicitly.',
 'difference_from_recent_references':'Compare dominant action, rhythm, metaphor, density and writing burden with recent references; avoid cosmetic differentiation.'}
universal={
 'U01':'Repository/schema/registry/authority validation and exact locks; no unintended shared regressions.',
 'U02':'Keyboard-only task, logical focus/order, visible focus, names/roles/states, error and feedback reachability.',
 'U03':'Actual screen-reader walkthrough of the task and state/feedback changes; automated tree is separate evidence.',
 'U04':'Genuine Chrome 200% plus responsive viewport and maximum-content/long-token checks; no document overflow, clipping, destructive overlap or unreachable controls.',
 'U05':'Readable contrast/text, semantic structure, non-color cues and reduced-motion preference.',
 'U06':'Loading/failure, offline-after-load and honest no-JavaScript fallback; never falsely report completion or storage success.',
 'U07':'Separate automated, user-attested and independent semantic provenance; pending direct checks cannot be replaced by emulation.',
 'U08':'Human instructional/subject-matter review of authentic capability, limitations, feedback and completion meaning.'}
conditional={
 'C01':'Authored input: physical-mobile software keyboard, IME/multilingual/plain text, focus/scroll, maxima, paste/long tokens, revision invalidation and retained work.',
 'C02':'State/recovery: shared service ownership, refresh recovery, opt-in durable persistence, denial/quota, restore envelope, recomputed completion, conflicts/corruption/clear and privacy.',
 'C03':'Media/illustrations: meaningful alternatives, blocked/slow asset fallback, keyboard access and reduced-motion/static alternatives.',
 'C04':'Comparison/dense evidence: narrow-screen transformation, source traceability, reading order and no horizontal-only dependency.',
 'C05':'Assessment/gates: branch/attempt/feedback/remediation rules, honest limits, no prepared-answer bypass, invalidation and accessible completion signals.',
 'C06':'Export/clipboard/download: complete plain-text representation, safe input, truthful success and denial/fallback behavior.',
 'C07':'Timed/audio/drag/motion interactions if authorized: equivalent untimed/keyboard/text alternatives and interruption/recovery tests.'}
baseline={'id':'W2-ACCESSIBILITY-RESILIENCE-BASELINE','scope':'Mandatory declaration and evidence planning for future Golden References; not retroactive passes for GR01–06.','universal':universal,'conditional':conditional}
write('governance/accessibility-resilience-baseline.json',baseline)
text={'type':'string','minLength':1,'pattern':r'\S'}
plan={'type':'object','required':['method','evidence','owner'],'properties':{k:text for k in ['method','evidence','owner']},'additionalProperties':False}
condition={'type':'object','required':['applies','rationale','validation'],'properties':{'applies':{'type':'boolean'},'rationale':text,'validation':plan},'additionalProperties':False}
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','title':'EXPERIENCE_DIFFERENTIATION_BRIEF','type':'object','required':['reference',*fields,'validation_baseline'],'properties':{'reference':text,**{k:{**text,'description':v} for k,v in fields.items()},'validation_baseline':{'type':'object','required':['id','universal','conditional'],'properties':{'id':{'const':baseline['id']},'universal':{'type':'object','required':list(universal),'properties':{k:plan for k in universal},'additionalProperties':False},'conditional':{'type':'object','required':list(conditional),'properties':{k:condition for k in conditional},'additionalProperties':False}},'additionalProperties':False}},'additionalProperties':False}
write('schemas/experience-differentiation-brief.schema.json',schema)
template={'reference':'',**{k:'' for k in fields},'validation_baseline':{'id':baseline['id'],'universal':{k:dict(method='',evidence='',owner='') for k in universal},'conditional':{k:dict(applies=False,rationale='',validation=dict(method='',evidence='',owner='')) for k in conditional}}}
write('prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.json',template)
lines=['# EXPERIENCE_DIFFERENTIATION_BRIEF — mandatory future specification contract','','Authority: W2-C06, user-authorized bounded correction. Applies to every future Golden Reference; existing GR-01–06 are explicitly grandfathered. No new reference number is assigned. This governs specification review, not visual-system design or implementation authorization.','','Copy the JSON template, fill every field and link it from the future `spec.yaml` using the repository-relative `experience_differentiation_brief` property. The blank template intentionally fails validation. The canonical brief schema is `schemas/experience-differentiation-brief.schema.json`. Root build mode and authority must also be declared. A structurally valid brief is not architectural approval; freeze and implementation authorization remain separate governed decisions.','','## Required design declarations','']
lines += [f'- **{k}**: {v}' for k,v in fields.items()]
lines += ['','## Universal and conditional validation baseline','','Every U requirement needs a method, planned evidence path and accountable owner. Every C requirement needs explicit applicability, rationale and validation plan. For a non-applicable requirement, explain why and state the evidence/reviewer for that decision; do not silently omit it. Any requested exception to a universal check is a System Gap requiring architectural decision, never an automatic waiver. Validation plans are not validation passes. Existing frozen matrices and provenance remain intact.','']
lines += [f'- **{k}**: {v}' for k,v in {**universal,**conditional}.items()]
lines += ['','Review must reject cosmetic differentiation, silent component/token/breakpoint invention and writing burden unrelated to the professional capability. Use LOCKED / CONSTRAINED / EXPLORATORY authority and the System Gap process. Tracks A/B remain proposals, not implementation permission.']
(ROOT/'prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
