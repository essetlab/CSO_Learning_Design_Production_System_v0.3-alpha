"""Evidence-only packet; never consumed by the learner runtime or regression fixture."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
x=read('tests/gr05-example-work.json')
c=read('prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json')
def response(judgment,reason,followUp):return dict(judgment=judgment,reason=reason,followUp=followUp)
first={
 'Q01':response('addressed','The objective names women vendors and persons with disabilities and connects their proposals to planning decisions, replacing meeting counts with intended influence.','Check that the final note keeps these groups and the proposed decision change explicit.'),
 'Q02':response('needs_follow_up','The draft invites additional priorities before decisions and proposes suitable times and spoken summaries, but its discussion format leaves practical access arrangements unspecified.','Check suitable times and accessible ways to contribute with the named groups before arranging the discussion.'),
 'Q03':response('needs_follow_up','Awra facilitates and records concerns while a public planning officer responds. The draft requests a response date and escalation route but does not establish either.','Confirm who can respond, the response date and the escalation route with participants and the responsible public actor.'),
 'Q04':response('needs_follow_up','Priority changes and unresolved concerns could show influence and response beyond attendance. Non-identifying records and consent are proposed, but safe retention and access arrangements remain broad.','Clarify who may access the records and when they should be deleted before collecting sensitive information.')}
final={
 'Q01':response('addressed','The unchanged objective still names both groups and the intended influence on the plan. The revision changes the input method without replacing that intended outcome with activity counts.','When checking the combined priorities, retain the connection between these groups’ proposals and the eventual planning decisions.'),
 'Q02':response('addressed','Short visits and accessible small conversations replace another large meeting. The draft includes spoken summaries, confidential input and checking combined priorities with both groups before the planning team decides.','Check whether the proposed times, summaries and confidential input route are usable by the participants concerned.'),
 'Q03':response('needs_follow_up','The unchanged accountability section keeps Awra in a facilitation role and assigns responses to a public planning officer. A confirmed response date and escalation route are still missing.','Confirm the responsible officer’s response date and agree how participants can escalate an unanswered concern.'),
 'Q04':response('needs_follow_up','The revised proposal-to-decision record connects conversations to changes and tracks responses. De-identification and agreed access and deletion are proposed, but those arrangements are not yet settled.','Agree access and deletion arrangements before sensitive details are collected, and check that the record can show decisions without identifying contributors.')}
fixture={
 'purpose':'SYNTHETIC SEMANTIC-REVIEW EVIDENCE ONLY. Not a model answer, learner/runtime input or approved real-world plan. Awaiting ChatGPT V25 judgment.',
 'source_hashes':{p:sha(p) for p in ['tests/gr05-example-work.json','prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json']},
 'scope':'Only criterion-review responses differ from the historical non-stress example. All case and artifact content is copied unchanged. Synthetic judgments are not the reviewer verdict.',
 'case':c['case'],'criteria':c['criteria'],
 'diagnoses':x['diagnoses'],'links':x['links'],'draft':x['draft'],'revision':x['revision'],'current':{**x['draft'],**x['revision']},'rationale':x['rationale'],
 'firstCriterionReview':first,'finalCriterionReview':final}
fixture_path='tests/gr05-v25-semantic-review-fixture.json'
(ROOT/fixture_path).write_text(json.dumps(fixture,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
parts=['# GR-05 V25 — criterion-specific synthetic semantic review',
 '**SYNTHETIC SEMANTIC-REVIEW EVIDENCE ONLY.** Not a model answer, approved real-world plan, learner submission or replacement regression fixture.',
 'V05 = PASS, as explicitly reported by the user. Architecture and the substantive learner artifact have passed review. **V25 awaits ChatGPT’s final semantic judgment.** Overall GR-05 status remains `IMPLEMENTED_PENDING_MANUAL_VALIDATION`.',
 '## Provenance and permitted change',
 'The frozen case, E01–E05, weak original, four diagnoses and links, authored v1, C01, revised v2 and rationale below are copied unchanged from the existing sources. Only the synthetic Q01–Q04 judgments, reasons and follow-ups in the two review rounds are newly authored under the user’s explicit instruction. They describe proposals and remaining uncertainties; they do not assert that any consultation, official confirmation or agreement has occurred.',
 '`tests/gr05-example-work.json` and the earlier `GR-05_V25_REVIEW_PACKET.md` remain unchanged historical/automated evidence. This separate fixture is not loaded by the runtime or existing regression runners. Structural checks are not semantic approval.']
for p,h in {**fixture['source_hashes'],fixture_path:sha(fixture_path)}.items():parts.append(f'- `{p}` SHA-256: `{h}`')
def add(title,text):parts.extend([title,text])
add('## Frozen case brief',c['case']['brief'])
add('## Evidence E01–E05','\n\n'.join(f"**{e['id']}**: {e['text']}" for e in c['case']['evidence']))
add('## Weak original note','\n\n'.join(f"### {f['id']}\n\n{c['case']['original_note'][f['id']]}" for f in c['authoring']['fields']))
add('## Four evidence-linked diagnoses','\n\n'.join(f"### {f['id']}\n\n{x['diagnoses'][f['id']]}\n\nEvidence: {', '.join(x['links'][f['id']])}." for f in c['authoring']['fields']))
add('## Authored v1 — unchanged','\n\n'.join(f"### {f['id']}\n\n{x['draft'][f['id']]}\n\nEvidence: {', '.join(x['links'][f['id']])}." for f in c['authoring']['fields']))
def review(title,data):
 parts.append(title)
 for q in c['criteria']:
  row=data[q['id']]
  parts.extend([f"### {q['id']}",q['question'],f"**Judgment:** `{row['judgment']}`",f"**Reason:** {row['reason']}",f"**Follow-up:** {row['followUp']}"])
review('## First criterion review — synthetic criterion-specific responses',first)
add('## C01 — unchanged',c['case']['challenge']['text'])
add('## Revised v2 — unchanged approved artifact','\n\n'.join(f"### {f['id']} — {'changed from v1' if f['id'] in x['revision'] else 'unchanged from v1'}\n\n{fixture['current'][f['id']]}\n\nEvidence (unchanged): {', '.join(x['links'][f['id']])}." for f in c['authoring']['fields']))
add('## Revision rationale — unchanged',x['rationale'])
review('## Final criterion review — synthetic criterion-specific responses',final)
add('## Unresolved follow-ups', 'Q03 and Q04 remain `needs_follow_up`. No evidence is supplied that the following actions have been completed:\n\n'+'\n\n'.join(f"**{key}:** {value['followUp']}" for key,value in final.items() if value['judgment']=='needs_follow_up')+'\n\nQ01 and Q02 are marked addressed in the written draft; their follow-ups are prospective checks, not claims of real-world implementation or perfect quality. Completion does not require all-positive judgments. The separate narrow structural check exercises this fixture through the unchanged interaction model; it is not a new browser or human semantic pass.')
add('## Requested ChatGPT disposition','Judge whether these eight criterion-specific responses adequately review their own criteria and the unchanged artifact, including candid unresolved issues. Return V25 PASS or the remaining specific deficiency. V05 is already PASS. Do not infer real-world approval, candidate promotion, Golden Reference acceptance or GR-06 authorization.')
(ROOT/'golden-references/GR-05/GR-05_V25_SEMANTIC_REVIEW_PACKET.md').write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('Separate semantic fixture and standalone packet created.')
