# GR-05 V25 review packet — exact synthetic test example

Status: **AWAITING CHATGPT V25 JUDGMENT**. GR-05 remains `IMPLEMENTED_PENDING_MANUAL_VALIDATION`.

**Synthetic review evidence only. This is not a model answer, approved real-world plan or new learner content.** The text below is copied without improvement from the existing non-stress automated test example. No stronger reasons or follow-ups have been generated.

## Provenance and extraction

`tests/gr05-example-work.json` supplies the diagnoses, links, v1, two revised fields, rationale, reason and follow-up. `tests/run_gr05_browser_validation.cjs` applies every listed link, uses `needs_follow_up` for Q01–Q04 in **both** rounds, repeats the same reason and follow-up for each criterion, and changes only participation and evidence. This packet expands that existing test procedure; it is not a captured human learner submission. Objective and accountability carry forward unchanged into v2. The maximum-content and later keyboard/IME test mutations are not this example.

Existing execution evidence: `tests/gr05-browser-review-handoff.json` (non-stress completed flows). Criteria, original, evidence and C01 are copied from frozen contract revision 2. Formatting headings are editorial; quoted content is exact.

- `tests/gr05-example-work.json` SHA-256: `2e23ccdbf18c21d54ea2220cf629a5e63601da3298a31a755848a17138a94c31`

- `tests/run_gr05_browser_validation.cjs` SHA-256: `1436d3633c3a988e9df1642e9cdaf6c69d0c2e95838e6e473a456d371f1e7a71`

- `prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json` SHA-256: `6984c281878ed26fe3fa8533d5e43ed8859fda8dd1d49da29f9dccd9539efd75`

- `tests/gr05-browser-review-handoff.json` SHA-256: `13bba0507f9c55b5d4d100d124bbbc982b5766212899122f6639ef016488fa4b`

## Case brief

Awra is supporting consultation on a service-improvement plan in fictional Jiru Amba. Prepare a practical improvement note for the planning team. Focus on women vendors and persons with disabilities, while recognizing that the full case includes other groups. Show who can influence the decision, what access changes are needed, who responds, and what evidence would demonstrate an effect.

## Case evidence

**E01**: Women vendors leave discussions early because trading, care and household responsibilities compete with meeting time.

**E02**: Persons with disabilities face an inaccessible venue and long printed documents.

**E03**: Participants rank activity cards already chosen by the planning team; transparent stall allocation and influence over market budgets are not available as added priorities.

**E04**: The plan counts meetings and feedback boxes but does not show whether rights-holders gained influence or received a response.

**E05**: Awra supports analysis, facilitation, community voice and accountability; it does not replace public authorities.

## Deliberately weak original note

**objective — Repaired objective**

Improve market services by holding consultations and installing a feedback box.

**participation — Participation and access procedure**

Invite everyone to one public meeting to rank the activities already selected by the planning team.

**accountability — Responsibility and response pathway**

Awra will collect concerns in the feedback box and handle all decisions after the meeting.

**evidence — Sign of change and safe evidence**

Report success using the number of people attending and the number of feedback boxes installed.

## Four evidence-linked diagnoses

### objective

Meetings count activity, not whose priorities influence decisions.

Evidence links: E03, E04.

### participation

Timing and inaccessible documents exclude vendors and disabled participants; preset options prevent influence.

Evidence links: E01, E02, E03.

### accountability

Awra cannot replace public decision-makers; concerns need a named response route.

Evidence links: E04, E05.

### evidence

Attendance cannot show influence, safe access or whether concerns received responses.

Evidence links: E02, E04.

## Authored v1 — immutable first-reviewed draft

### objective

Enable women vendors and persons with disabilities to propose market priorities before the planning team finalizes decisions, and explain which proposals influenced the plan.

Evidence links: E03, E04.

### participation

Ask vendors about suitable times and participants about access needs. Hold an accessible discussion using spoken summaries. Invite additional priorities, including stall allocation and budget influence. Check proposed priorities with affected groups before decisions.

Evidence links: E01, E02, E03.

### accountability

Awra facilitates input and records concerns with consent. Ask the responsible public planning officer to confirm a response date and explain decisions through accessible channels. Identify an escalation route with participants if no response arrives.

Evidence links: E04, E05.

### evidence

Record suggested priorities and resulting plan changes without identifying contributors. Ask participants privately whether they could influence choices. Track responses and unresolved concerns, with access limited to agreed staff.

Evidence links: E02, E04.

## First criterion review — exact test responses

### Q01

Does the objective connect specific rights-holders and barriers to influence or response, rather than only listing activities?

Criterion guidance (contract): Name whose influence changes and the barrier addressed. Holding another meeting is not, by itself, the change sought.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q02

Can the named groups influence priorities before decisions are finalized, with workable timing and accessible information?

Criterion guidance (contract): Use early accessible information and a feasible small-group or other safe input route. Explain how that input reaches the decision, not just how people attend.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q03

Is a responsible actor distinct from Awra, with a safe response route and a way to communicate what changed?

Criterion guidance (contract): Do not promise that Awra can make public decisions. Identify the relevant planning or market actor and a non-identifying response process.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q04

Would the evidence show influence or response without identifying people, and can the proposed team check it?

Criterion guidance (contract): Link a sign of change to a decision or response and an appropriate review point. Counts of attendance or boxes alone are insufficient.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

## C01 — released after the first criterion review

For this exercise, the team cannot add a second large public meeting. Improve your note so affected groups can still influence priorities before the plan is finalized. Keep a feasible response and evidence pathway.

## Revised v2 — complete current artifact

### objective — unchanged from v1

Enable women vendors and persons with disabilities to propose market priorities before the planning team finalizes decisions, and explain which proposals influenced the plan.

Evidence links (unchanged): E03, E04.

### participation — changed

Use short visits at vendor-agreed times and accessible small conversations before finalization, without a second large meeting. Offer spoken summaries and a confidential way to add priorities. Ask women vendors and disabled participants to check the combined priorities before the planning team decides.

Evidence links (unchanged): E01, E02, E03.

### accountability — unchanged from v1

Awra facilitates input and records concerns with consent. Ask the responsible public planning officer to confirm a response date and explain decisions through accessible channels. Identify an escalation route with participants if no response arrives.

Evidence links (unchanged): E04, E05.

### evidence — changed

Keep a de-identified proposal-to-decision record from the visits and small conversations. Ask each group whether the summary reflects its priorities. Track the officer's response and unresolved points; agree access and deletion arrangements before collecting sensitive details.

Evidence links (unchanged): E02, E04.

## Revision rationale

Short visits replace another large meeting while preserving pre-decision influence. The revised evidence record links those conversations to decisions and responses; consent and deletion arrangements still need confirmation.

## Final criterion review — exact test responses

### Q01

Does the objective connect specific rights-holders and barriers to influence or response, rather than only listing activities?

Criterion guidance (contract): Name whose influence changes and the barrier addressed. Holding another meeting is not, by itself, the change sought.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q02

Can the named groups influence priorities before decisions are finalized, with workable timing and accessible information?

Criterion guidance (contract): Use early accessible information and a feasible small-group or other safe input route. Explain how that input reaches the decision, not just how people attend.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q03

Is a responsible actor distinct from Awra, with a safe response route and a way to communicate what changed?

Criterion guidance (contract): Do not promise that Awra can make public decisions. Identify the relevant planning or market actor and a non-identifying response process.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

### Q04

Would the evidence show influence or response without identifying people, and can the proposed team check it?

Criterion guidance (contract): Link a sign of change to a decision or response and an appropriate review point. Counts of attendance or boxes alone are insufficient.

**Judgment:** `needs_follow_up`

**Reason:** The note connects group input to decisions; confirm practical access arrangements with participants.

**Follow-up:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

## Unresolved follow-ups

All four criteria remain `needs_follow_up` in both rounds. The test does not record these actions as resolved. The repeated wording below is intentionally preserved, not replaced by criterion-specific justifications.

**Q01:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

**Q02:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

**Q03:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

**Q04:** Confirm accessible channels, response date and safe record retention with participants and the responsible officer.

## Existing completion versus requested review

The non-stress test flow acknowledges the package and verifies enabled Continue, then revises and re-reviews. That establishes software structure/state completion only. It does not establish HRBA quality or approve unresolved follow-ups.

ChatGPT: return the V25 judgment on this exact artifact, including rights-holder specificity, pre-decision influence, feasible C01 revision, public-authority responsibility boundaries, safe evidence and adequacy of both review rounds. Also state the related V05 instructional-depth disposition. Identify any deficiencies without silently repairing the example. No acceptance, candidate promotion or GR-06 authorization is implied by this packet.
