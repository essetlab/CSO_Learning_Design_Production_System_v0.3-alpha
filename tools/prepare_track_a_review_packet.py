"""Copy exact frozen semantic evidence; never improve fixtures or grant a verdict."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
contract='prototype-specs/TRACK_A_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json';fixture='prototype-specs/TRACK_A_SEMANTIC_REVIEW_FIXTURES_v0.1.json'
c=load(contract);f=load(fixture);plan=load('prototype-specs/TRACK_A_VALIDATION_PLAN_v0.1.json');folder=ROOT/'golden-references/TRACK-A'
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
lines=['# Track A independent semantic-review packet','**PENDING — H01–H10 independent human judgment.**','Synthetic semantic-review evidence only. These are the exact approved specification fixtures, not model answers, learner-visible prepared answers, real plans or independent competence evidence.',c['freeze_authority']['boundary'],f'Frozen source: `{fixture}`. SHA-256: `{sha(fixture)}`.',f'Contract SHA-256: `{sha(contract)}`. No fixture text has been improved or rewritten. Automated trajectory execution establishes structural viability only.','## Case and bounded next step',c['case']['brief'],c['case']['next_step'],'## Exact initial evidence']
for a in c['case']['artifacts']:lines += [f"### {a['id']} v{a['version']} — {a['title']}",a['source'],a['text'],'Limitation: '+a['limitation']]
lines += ['## Transparent criteria']
for k in c['criteria']:lines += [f"### {k['id']} — {k['label']}",k['question'],k['sufficiency_anchor']]
lines += ['## Later clarification — only after initial record and consequence inspection',c['case']['update']['id'],c['case']['update']['text'],c['case']['update']['limitation'],'## Exact positive trajectories']
for x in f['positive_examples']:
 lines += [f"### {x['id']} — {x['purpose']}",'```json',json.dumps(x,ensure_ascii=False,indent=2),'```']
lines += ['## Exact negative counterexamples','Do not accept these simply because text and route fields are structurally valid. They are review-only negative evidence.','```json',json.dumps(f['negative_counterexamples'],ensure_ascii=False,indent=2),'```','## Independent judgment form','For each dimension record PASS / REVISE / FAIL, rationale, fixture IDs, reviewer/provenance and the exact fixture hash above. Do not infer semantic PASS from runtime navigation.']
for h in plan['human_rubric']:lines += [f"### {h['id']} — {h['title']}",h['requirement'],'Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.']
(folder/'SEMANTIC_REVIEW_PACKET.md').write_text('\n\n'.join(lines)+'\n',encoding='utf-8')
manual=['# Track A manual and direct validation checklist','Status: **IMPLEMENTED_PENDING_MANUAL_VALIDATION**. No direct human or semantic PASS is claimed. Prior GR attestations do not transfer to Track A.',
'Serve the repository with `python -m http.server 8776 --bind 127.0.0.1` and open `http://127.0.0.1:8776/golden-references/TRACK-A/index.html` in Chrome. Review the exact synthetic dossier; avoid entering personal or real participant data.',
'Record performer, date, OS, browser/version, device/reader, observations and evidence filenames for each check. The 8–12 minute target is a design hypothesis.',
'## Common complete flow',
'Inspect all four initial artifact versions. Map the three criteria with current support/limiting links; preserve missing/conflicting states, gaps and priority as appropriate. Choose proceed / revise / seek review / defer. Write the one rationale (maximum 45 words) and conditional next-step note (maximum 35 words). Record initial recommendation; inspect simulated consequence and common contrast. Request clarification. Inspect E03 v2; explicitly update/remove stale links. Choose retain/amend, confirm all three current criteria, record reconsideration, inspect comparison/consequence and acknowledge practice only. Verify Continue enables. Revise: Continue disables immediately, history and draft remain. Reconfirm/review/acknowledge and verify Continue enables again.',
'## V15 — genuine native Chrome 200%: PENDING',
'Use native Chrome zoom with its 200% indicator visible. Complete the common flow. Inspect every source, complete feedback/comparison, both fields and all controls. Check document horizontal scrolling, clipping, destructive overlap, readable text and reachable Continue. Capture indicator, stale state, current review, completed and revised states. Viewport emulation is not this evidence.',
'## V16 — actual screen reader: PENDING',
'Use an actual reader and record its version/settings. Check headings/reading order, criterion and source names, support/limiting roles, missing/conflicting state, gap priority, E03 version change, live/error announcements, current versus historical outcome, source-return focus and disabled/enabled Continue. Complete the flow without pointer reliance. Confirm that practice completion is not announced as competence or authorization.',
'## V17 — physical-mobile software keyboard: PENDING',
'On a physical device, inspect the criterion-first layout and source-return focus. Type and paste into both fields with the software keyboard open, including long/over-limit and Unicode input. Inspect caret, errors, scroll, keyboard dismissal, reconsideration and Continue reachability. No horizontal mapping matrix should be necessary.',
'## V19 — observed burden/differentiation: PENDING',
'Time an uncoached review and record effort, navigation and misunderstanding. Check the two-field/80-word ceiling and mapping/judgment rhythm. Reject excessive disclosure/scroll burden or a studio-like authoring experience even if structural tests pass. The all-disclosures-expanded screenshots are stress evidence, not the normal initial density.',
'## V20 — H01–H10 independent semantic review: PENDING',
'Use [the standalone packet](SEMANTIC_REVIEW_PACKET.md). Judge all four positive trajectories and eight negative counterexamples; attach verdicts/rationales to the exact fixture hash. Preserve candid gaps and all four structurally viable routes. No automatic semantic quality pass.',
'## Record',
'No performer/device/date/screenshot metadata for these direct checks has been supplied. Leave the checks PENDING until explicit evidence arrives. Store direct user attestations, independent/ChatGPT judgments and automated evidence in separate provenance classes.']
(folder/'MANUAL_VALIDATION.md').write_text('\n\n'.join(manual)+'\n',encoding='utf-8')
print('Exact semantic packet and pending direct checklist written.')
