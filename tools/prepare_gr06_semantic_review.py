"""Synthetic test-only review material. Never imported by learner runtime."""
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json').read_text(encoding='utf-8'))
notes=[
 'Forty attendees and 24 women describe attendance, not influence or coverage of eligible vendors. No denominator supports a participation rate.',
 'Four voluntary comments flag timing as a possible barrier; the other two are silent. Self-selection prevents a population estimate or explanation for everyone leaving.',
 'Entrance access was checked, but usable information remains uncertain. A long printed list and absent format check do not establish access for everyone.',
 'Six administrative closures out of eight suggestions do not show explanation, receipt or influence. The meaning of closed needs verification.',
 'Priorities remain open, but Awra facilitates rather than decides. A feasible input route must fit the remaining window without another large meeting.'
]
primary=dict(claim='The comments suggest that timing may have limited some contributors’ chance to influence priorities. Attendance alone cannot show that influence occurred.',limitation='Six self-selected comments cannot establish how common the barrier is, or whether timing caused other people to leave.',confidence='moderate',informing=['G6-E02'],limiting=['G6-E01','G6-E02'])
alternative=dict(claim='It remains unresolved whether the long printed priority list also limited usable input. This is a grounded question, not an equally likely explanation for early departure.',limitation='The checklist records format availability, not anyone’s experience or reason for leaving. The comments neither confirm nor exclude a materials barrier.',confidence='low',informing=['G6-E03'],limiting=['G6-E02','G6-E03'])
base=dict(route='verify',interpretationIds=c['authoring']['interpretations']['ids'],choiceReason='Check the timing and information-access uncertainties before a wider change. The comments give a concrete timing concern; the materials barrier remains a weaker unresolved question. Attendance is insufficient evidence of influence.',alternative='A small timing trial might help, but first check whether contributors can use the priority information and whether input can still reach the planning team.',action='Before finalization, Awra should request a short input window from the planning team and offer brief voluntary conversations at convenient trading times, checking preferred accessible ways to discuss priorities.',responsibility='The public planning team decides priorities and whether the input window is feasible. Awra facilitates and requests reasons, without promising a changed priority or permission already granted.',verification='Use a non-identifying summary linking suggestions to recorded planning responses. Ask whether offered formats and timing worked without collecting complaint details. This cannot establish population-wide access or causal impact.',accountBack='Before finalization, ask the planning team to explain how input was considered through brief oral and readable summaries. Awra should check preferred routes and return unanswered concerns to the team at the next agreed contact.')
reviews={
 'Q01':dict(judgment='addressed',reason='Timing is a supported concern for some commenters, not a population cause. The materials issue stays unresolved and lower-confidence, linked to the access checklist rather than invented as equally likely.',followUp=''),
 'Q02':dict(judgment='needs_follow_up',reason='The bounded action respects public decision authority and the absence of a large meeting. The planning team has not confirmed the proposed input or response window.',followUp='Awra should request the window before finalization and explain any refusal or delay to contributors without promising a change.'),
 'Q03':dict(judgment='needs_follow_up',reason='U01 separates administrative closure from an explanation sent. Neither the four internally closed entries nor the two sent explanations establish receipt. The account-back route still needs accessibility checking.',followUp='Ask the planning team for non-identifying response status and offer voluntary confirmation through contributors’ preferred routes; retain unknown receipt explicitly.'),
 'Q04':dict(judgment='addressed',reason='The revision adds a closure-process gap to the interpretation and separates sent from received in verification. It seeks limited process evidence without names and preserves uncertainty about understanding and influence.',followUp='Check whether a safe voluntary receipt check is feasible; lack of a response is not proof that an explanation was never received.')
}
def example(id,label,route,current_route):
 d=copy.deepcopy(base);d['route']=route
 if route=='trial':
  d['choiceReason']='Try a small reversible timing and format adaptation while checking uncertainty. Four comments justify testing access, not a universal redesign. The possible information barrier remains unresolved rather than equal to the timing concern.'
  d['alternative']='Verification alone could delay an accessible input opportunity before finalization. A limited trial can gather feedback without asserting that it will solve every barrier.'
 if route=='escalate':
  d['choiceReason']='The planning team must authorize a route for input before finalization. Escalate that decision while Awra gathers safe, voluntary access preferences. Timing concerns support urgency, but do not establish a general failure.'
  d['alternative']='Awra could trial conversations immediately, but should not imply their suggestions will enter a decision process until the planning team confirms that route.'
  d['action']='Ask the public planning team to authorize a short pre-finalization input and response window. Meanwhile Awra may collect voluntary, non-identifying access preferences; formal priority changes must await the team’s decision.'
 v1=dict(sourceNotes={e['id']:dict(text=n,use='both') for e,n in zip(c['case']['evidence'],notes)},interpretations=dict(primary_interpretation=copy.deepcopy(primary),alternative_or_unresolved_interpretation=copy.deepcopy(alternative)),decision=d)
 current=copy.deepcopy(v1)
 current['interpretations']['primary_interpretation']['claim']='Timing may constrain some input, and U01 now shows a recorded account-back gap: four closed entries lack a recorded explanation sent. Two sent explanations still have unverified receipt; this is process evidence, not proof of understanding or influence.'
 current['interpretations']['primary_interpretation']['limitation']='These records do not establish whether any explanation was received or understood. Missing records do not prove non-receipt, and the comments still cannot estimate prevalence.'
 current['interpretations']['primary_interpretation']['informing']=['G6-E02','G6-U01']
 current['interpretations']['primary_interpretation']['limiting']=['G6-E02','G6-U01']
 current['decision']['route']=current_route
 current['decision']['verification']='Ask for a non-identifying status summary distinguishing internal closure, explanation sent and voluntarily confirmed receipt. Keep unknown receipt explicit. Check which suggestions affected priorities and request reasons otherwise, without collecting identities or treating silence as proof of non-receipt.'
 current['decision']['accountBack']='Before finalization, ask the planning team to provide brief oral and readable explanations for the four internally closed entries and check receipt voluntarily for sent explanations. Awra checks preferred channels and returns unanswered concerns at the agreed follow-up; understanding remains unverified.'
 if current_route!=route:
  current['decision']['choiceReason']='Change from a small access trial to seeking planning-team authorization for a response process. U01 identifies a recorded account-back gap that Awra cannot resolve alone. Timing and format concerns remain, but do not warrant claiming a population-wide barrier.'
  current['decision']['action']='Request planning-team authorization for a pre-finalization response window covering internally closed entries and unverified receipt. Awra can meanwhile check accessible contact preferences voluntarily; only the planning team can commit public decisions or explanations.'
  current['decision']['alternative']='Continuing only the timing trial would leave the recorded response gap unaddressed. Preserve its access questions, but seek authority for the additional account-back step before claiming it can proceed.'
 elif route=='escalate':
  current['decision']['action']='Add a request for planning-team authorization of explanations and receipt checks to the pending input-window request. Awra can prepare a non-identifying status checklist and ask access preferences meanwhile; public decisions and formal explanations remain with the team.'
 review=copy.deepcopy(reviews)
 if current_route=='escalate':review['Q02']['reason']='Escalation names the planning team’s authorization role and an interim access-check action for Awra. Neither authorization nor a decision change is assumed; the response window remains to be agreed.'
 return dict(id=id,label=label,provenance='Synthetic semantic-review evidence only; not a model answer, professional approval or actual project data.',v1=v1,updateNote='U01 shows four internally closed entries without a recorded explanation sent, alongside two sent explanations with unverified receipt. That adds a response-process gap without proving non-receipt or fair decisions.',current=current,adaptationDisposition='retain_decision' if route==current_route else 'change_decision',adaptationRationale='U01 changes the interpretation from uncertain closure meaning to a recorded account-back gap. Keep access questions open, distinguish sent from received in verification, and request an accessible response route without claiming missing records prove non-receipt.',criterionReview=review)
examples=[example('retain','Retain verification route with meaningful adaptation','verify','verify'),example('change','Change trial route to authorization request','trial','escalate'),example('escalate','Escalation with interim action and explicit boundary','escalate','escalate'),example('unresolved','Retain a bounded trial with unresolved materials alternative','trial','trial')]
examples[-1]['current']['interpretations']['alternative_or_unresolved_interpretation']['limitation']='U01 clarifies response records, not whether formats were usable. The possible materials barrier remains unconfirmed; it need not compete equally with the timing concern.'
negatives=[
 dict(id='N01',dimension='H03',target='interpretations.primary_interpretation.claim',text='Four of six vendors left early, so two thirds of all vendors were prevented from influencing priorities.',expected_human_deficiency='Self-selected comments become a population prevalence estimate; all vendors has no denominator.'),
 dict(id='N02',dimension='H04',target='interpretations.primary_interpretation.claim',text='Six suggestions were closed, so all six contributors received an explanation; the two sent responses confirm successful receipt.',expected_human_deficiency='Administrative closure and sending are both confused with confirmed receipt.'),
 dict(id='N03',dimension='H02',target='interpretations.alternative_or_unresolved_interpretation.claim',text='Timing and inaccessible documents are equally likely causes of every early departure, so give both explanations equal weight.',expected_human_deficiency='Unsupported equal weight and causal certainty erase the evidence asymmetry.'),
 dict(id='N04',dimension='H06',target='decision.responsibility',text='Awra will authorize the public priorities and guarantee adoption of the vendors’ requests before finalization.',expected_human_deficiency='Awra assumes the public planning team’s authority and promises an outcome.'),
 dict(id='N05',dimension='H09',target='cosmetic adaptation',text='Append “after further thought” to the v1 claim and action; link U01 but leave their substantive meaning unchanged.',expected_human_deficiency='A structural text difference is not meaningful response to U01. The human rubric must reject this even if runtime structure passes.')]
package=dict(classification='SYNTHETIC_SEMANTIC_REVIEW_EVIDENCE_ONLY',runtime_input=False,contract='GR-06 Revision 2',case=c['case'],examples=examples,negative_counterexamples=negatives,human_dimensions=c['human_semantic_validation']['dimensions'],human_judgment='PENDING_INDEPENDENT_REVIEW')
(ROOT/'tests/gr06-semantic-fixtures.json').write_text(json.dumps(package,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=['# GR-06 independent semantic review packet','**SYNTHETIC SEMANTIC-REVIEW EVIDENCE ONLY.** Not model answers, actual project data or approved plans. These test-only examples are never loaded by the learner runtime. Structural completion is not semantic approval. Human H01–H09 judgment remains pending.','## Frozen case',c['case']['brief']]
for e in c['case']['evidence']:out += [f"### {e['id']} · {e['source']}",e['scope'],e['text'],'Limitation: '+e['limitation']]
out += ['## G6-U01 (released after v1)',c['case']['update']['text'],c['case']['update']['limitation']]
for x in examples:
 out += ['## '+x['id']+' · '+x['label'],x['provenance']]
 for version in ['v1','current']:
  out += ['### '+version]
  for id,n in x[version]['sourceNotes'].items():out += [f"**{id} ({n['use']})**: {n['text']}"]
  for id,n in x[version]['interpretations'].items():out += [f'**{id}**',n['claim'],'Limitation: '+n['limitation'],f"Confidence: {n['confidence']}; informing: {', '.join(n['informing'])}; limiting: {', '.join(n['limiting'])}"]
  for k,v in x[version]['decision'].items():out += [f'**{k}**: '+(', '.join(v) if isinstance(v,list) else v)]
 out += ['### Adaptation',x['updateNote'],x['adaptationDisposition'],x['adaptationRationale'],'### Criterion review and unresolved follow-up']
 for q,a in x['criterionReview'].items():out += [f"**{q} — {a['judgment']}**",a['reason'],'Follow-up: '+(a['followUp'] or 'None recorded.')]
out += ['## Negative counterexamples','These intentionally deficient changes are for human discrimination, not learner feedback or runtime keyword scoring.']
for n in negatives:out += [f"### {n['id']} · {n['dimension']}",n['text'],'Expected deficiency for reviewer to assess: '+n['expected_human_deficiency']]
out += ['## H01–H09 judgment sheet','Record PASS or DEFICIENCY for every dimension across the examples and counterexamples. No automated semantic pass is claimed.']
for h in package['human_dimensions']:out += [f"- {h['id']} **PENDING** — {h['dimension']}: {h['acceptance']}"]
(ROOT/'golden-references/GR-06/GR-06_SEMANTIC_REVIEW_PACKET.md').write_text('\n\n'.join(out)+'\n',encoding='utf-8')
print('Four substantive synthetic examples and five negative counterexamples prepared')
