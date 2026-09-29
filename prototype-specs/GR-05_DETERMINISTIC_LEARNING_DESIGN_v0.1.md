> FROZEN FOR PROTOTYPE IMPLEMENTATION by user architectural approval. Revision 2 is authoritative; earlier pending-authorization wording below is historical. Six shared candidates are authorized at PROTOTYPE only. Validation results must be recorded separately; no Golden Reference acceptance or GR-06.

# GR-05 deterministic learning-design specification

**Deep Build / Repair Studio — Repair the market participation plan**

Status: **REVISION 2 — REVISED FOR FINAL FREEZE; NOT AUTHORIZED FOR IMPLEMENTATION**. Date: 2026-09-28. The accompanying [JSON contract](GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) is the exact proposed source for case wording, field IDs/bounds, criteria, state transitions and completion predicates. This document explains that contract. Resolve any discrepancy at review; do not let a builder choose silently.

## 1. Capability and authentic task

The learner is a local CSO project officer or facilitator who understands introductory HRBA concepts. The professional capability is to **diagnose a participation plan from evidence, author a coherent improvement note, and revise it under a practical constraint without losing the connection between rights-holders, access, influence, responsibility and evidence**.

The learner acts as a member of fictional Awra preparing a note for the planning team in fictional Jiru Amba. The task is bounded to market participation and response arrangements. Women vendors and persons with disabilities are the focus of this exercise; the broader case includes other groups. The draft must distinguish Awra's facilitation role from the relevant planning/market actor's decision and response responsibilities. Do not infer statutory mandates or promise authority the case does not establish.

The output is a working improvement note, not a quiz score or a professionally approved plan. Estimated working time is 25–35 minutes; timing is not a gate. The learner may leave and revisit available stages without losing text.

**Evidence of depth:** four learner-authored connected sections; diagnosis tied to source evidence; a frozen first draft; four explicit review judgments with reasons; a new feasibility constraint; a changed participation procedure and changed response/evidence arrangement; a final comparison and rationale. A flow that can be completed by selecting prepared answers or merely revealing panels fails this design even if it looks polished.

## 2. Authority and source transformation

The resource preflight identifies the exact inspected sources and their dispositions. The case evidence E01–E05 paraphrases the existing fictional narrative: livelihood/care timing, inaccessible venue/documents, already-selected activity priorities, activity counts without influence/response evidence, and Awra's supporting role.

The deliberately weak four-section note and challenge C01 are **accepted bounded exercise adaptations retained unchanged by this correction**. They are not presented as quotations from accepted HRBA content. This distinction remains in authoring provenance, while learners see a concise fictional-case label rather than implementation notes.

LOCKED by architectural review: the accepted capability, task sequence, original note, E01–E05, C01, immutable v1, structural/self-review distinction and stale-review invalidation; automatic session recovery and opt-in durable persistence; hard maxima without word-count minima. The no-implementation boundary remains LOCKED. CONSTRAINED: current tokens, accessibility, provenance and shared ownership. Pending final freeze: the concrete minimal text check, operational recovery details and proposed shared candidate IDs/interfaces. No field/interaction may be replaced with a multiple-choice shortcut. See the architectural corrections and candidate record for the explicit decision history.

## 3. Initial material

Opening instruction: **“Repair this note so affected groups can influence market decisions and receive a response. Use the evidence, write your own improvements, then test and revise your work.”**

The original note remains read only:

| Section | Deliberately weak original |
| --- | --- |
| Objective | Improve market services by holding consultations and installing a feedback box. |
| Participation | Invite everyone to one public meeting to rank the activities already selected by the planning team. |
| Accountability | Awra will collect concerns in the feedback box and handle all decisions after the meeting. |
| Evidence | Report success using the number of people attending and the number of feedback boxes installed. |

The five evidence items remain accessible throughout. They are short text statements with stable IDs, not hotspots, picture-dependent content or optional correctness clues. Original sentences are never prefilled as the learner's repaired draft. Labels, maximum word counts and concise soft guidance are visible before writing; no minimum word target is shown. There is no need for video, a new hero, an illustration-generation task or a remote dependency.

## 4. Learner task sequence

| Stage | Learner does | Work retained | Exit condition |
| --- | --- | --- | --- |
| S1 Diagnose the note | Read original/evidence; explain one weakness per section and bind it to evidence | Four diagnosis rows with explanation and evidence IDs | D: each explanation satisfies T and the 50-word maximum, with 1–3 distinct valid evidence links |
| S2 Write the repair | Author objective, procedure, response pathway and evidence plan | Four editable sections, each with 1–3 evidence links | A: complete bounded draft, D true, sections differ from original |
| S3 Review draft 1 | Explicitly review; compare original with v1; judge and explain all four criteria | Immutable v1 + diagnosis snapshot; first criterion review | R1: four addressed/needs-follow-up judgments, justification and any follow-up |
| S4 Improve under constraint | Read C01; revise procedure and accountability or evidence; explain the change | Current draft, preserved v1, revision rationale | A and C: required fields changed, rationale satisfies T and the 70-word maximum |
| S5 Compare and retain | Compare v1 with current draft; re-review all four criteria; acknowledge the current package | Version-bound final review and acknowledged note | COMPLETE: all current predicates valid |

Stage transitions are explicit actions, not automatic navigation on typing or selecting an evidence reference. Revisiting a stage does not clear its work. Later stages explain prerequisites when unavailable. Work may be saved/copied before it satisfies a completion gate; validity and retention are distinct.

The challenge appears only after R1: **“For this exercise, the team cannot add a second large public meeting. Improve your note so affected groups can still influence priorities before the plan is finalized. Keep a feasible response and evidence pathway.”** This introduces a realistic design tradeoff instead of demanding an arbitrary rewrite. It is clearly an exercise constraint. Small-group or other safe routes are possibilities, not a mandatory phrase or hidden correct answer.

The second draft must change `participation` and at least one of `accountability` or `evidence` relative to v1. This makes the learner reconnect a procedure to its response or evidence consequences. An already strong first draft can improve timing, role clarity, response details or how influence is checked. The learner explains that improvement; the software does not pretend to infer its quality.

## 5. Artifact fields and bounded authoring

| ID | Label | Hard maximum words | Required learning function |
| --- | --- | --- | --- |
| `objective` | Repaired objective | 70 | Specific rights-holders, barrier, desired influence/response change |
| `participation` | Participation and access procedure | 110 | Access/timing, how input arrives before a decision, route beyond one public meeting |
| `accountability` | Responsibility and response pathway | 100 | Responsible planning/market actor, separate CSO role, safe feedback and communication back |
| `evidence` | Sign of change and safe evidence | 80 | Sign of influence/response, feasible non-identifying evidence, reviewer and review point |

Diagnosis explanations have a hard maximum of 50 words each; criterion justifications and conditional follow-ups, 35 each; revision explanation, 70. The four field maxima are unchanged. There are **no hard minimum word counts**. Counts remain whitespace-delimited tokens after trimming; these GR-05 bounds do not replace GR-03's limits.

The proposed minimal authored-text rule **T** applies to every required authored section, diagnosis, justification, required follow-up and revision rationale: after trimming Unicode whitespace, contain at least two Unicode code points in general categories Letter (L*) or Number (N*). This rejects empty, punctuation-only and single-character placeholders. It does not count English words, demand sentences, enforce grammar or certify meaning. Short phrases, bullets and non-English writing are permitted. Do not replace the removed word minima with an equivalent character quota.

Soft guidance asks for the necessary idea: whose influence changes; how input reaches the decision; who responds; what evidence to check; why a criterion is addressed; what the revision changed. A concise response can be sufficient. Soft guidance never disables a stage, produces a below-length warning, or alters completion. No pedagogically necessary hard word minimum is identified for this bounded task.

Depth is proved by evidence-linked authorship, retained versions, explained review and a real revision, with human evaluation of meaning. T alone cannot reject every meaningless two-letter response; the product must not claim it can. The Golden Reference's human learning review must reject demonstrations that lack adequate reasoning, while runtime structural completion remains explicitly separate from semantic approval.

Evidence links refer to E01–E05. Learners can use the same evidence in more than one section. A link is not proof of a valid inference: the explanation carries the reasoning. No live keyword matching or generated prose fills the artifact. Learner input is always plain text. The product must never interpret a pasted script, Markdown link or HTML as executable content.

Over-limit or incomplete work stays visible and retained; show the error rather than silently truncating it. Long unbroken tokens and multiline pastes must wrap without widening the document. A whitespace-only edit does not count as a revision. A wording change is detectable; a *meaningful* improvement requires learner/reviewer judgment and cannot be certified by length or diff alone.

## 6. Feedback and revision model

There are two separate feedback layers:

1. **Structural checks:** missing/non-trivial text, maximum word limits, invalid evidence IDs, unchanged original wording, missing rubric responses, unchanged required revision fields, or a stale review. These are deterministic and can block stage completion.
2. **Criterion guidance and self-review:** Q01 rights-holder/change specificity; Q02 pre-decision influence and practical access; Q03 responsible response and CSO boundaries; Q04 useful, safe evidence. Each has fixed guidance in the JSON. The learner selects `addressed` or `needs_follow_up`, gives a concise reason satisfying T and the 35-word maximum, and records a next action if follow-up is needed. This is retained self-assessment, not a machine quality score.

The interface must label feedback as **“Structure checked”** and **“Your criterion review”**, never “HRBA-correct” or “professionally approved.” It may display fixed criterion prompts beside the learner's text; it must not fabricate individualized semantic praise. Choosing `needs_follow_up` does not trap the learner: a concrete follow-up is a valid reviewed outcome. Both passes retain unresolved issues.

Proposed exact structural messages:

| Condition | Message |
| --- | --- |
| Required blank text | “Write your {field label} before reviewing this draft.” |
| Empty/trivial authored text | “Add a brief note for {field label}; words or short phrases are enough.” |
| Maximum exceeded | “Keep {field label} to {maximum} words or fewer. Your work is retained.” |
| Missing/invalid evidence selection | “Link this section to 1–3 evidence items from the case.” |
| Same as original | “This section still matches the original. Write your repair before reviewing.” |
| Incomplete criterion | “Review {criterion label} and explain your judgment.” |
| Follow-up selected but missing | “Record one next action for the point that still needs follow-up.” |
| Required revision absent | “Revise the participation procedure and the response or evidence plan, then explain what changed.” |
| Current review stale | “Your work changed after review. Review this version before continuing.” |

Show all relevant errors in a linked summary and at the fields; focus the summary or first error following the explicit action. Do not mark fields red continuously while the learner is composing. Keep fixed guidance available and feedback associated with the correct snapshot.

## 7. State, comparison and completion

Maintain a stable activity/contract/case version and a local draft identifier. `contentRevision` increases when normalized content, diagnosis, evidence binding or revision explanation changes. The first reviewed snapshot is immutable and includes its diagnosis/evidence bindings. Current fields may continue to change; never regenerate v1 from the latest text.

Comparison shows two versions at a time: original/v1 in S3, then v1/current in S5. Every row has an explicit field name, version labels and changed/unchanged text. Full before and after content must remain readable; no hover-only diff, image slider, color-only deletion or horizontally scrolling table is required. Original text can be revisited from S5 without overwriting the selected comparison.

Editing work invalidates the final review/acknowledgment immediately and disables Continue. It does not delete any draft text or historical first review. Editing final criterion responses also clears the final acknowledgment. Revising after completion clears final review and acknowledgment even before a new edit. First-review rubric edits recompute R1; if incomplete they invalidate downstream final review and acknowledgment while preserving the challenge and all text. Reset requires a confirmation naming loss of both versions and affects GR-05 only.

The exact structural completion expression is:

```text
D && A && R1 && C && R2 && F

C = challenge_revealed
    && participation_changed_since_v1
    && (accountability_changed_since_v1 || evidence_changed_since_v1)
    && valid_revision_explanation
```

D and A are valid diagnosis/current draft; R1 is the completed first-snapshot review; R2 is the final criterion review bound to current revision; F is the final package acknowledgment bound to current revision and current criterion responses. Downloading, agreeing that every criterion is addressed, selecting a model answer, time spent and opening every panel are not completion requirements.

Final label: **“Reviewed training draft — not approved for real-world use.”** The Continue button uses the existing shell contract; this reference does not invent next-episode navigation or a course-level approval state.

## 8. Retained work and persistence proposal

The package retains the fictional-case/source label, original note, diagnosis, frozen v1, current/final version, field-aligned comparison, both criterion reviews, unresolved follow-ups, C01 and revision rationale, contract/case versions and completion status. Display it as a semantic on-page document. Optional UTF-8 plain-text download and selectable-copy fallback serialize the same content in that order; no personalized dossier, uploaded attachment or backend is needed.

**Accepted shared two-tier rule (G05-03):** automatic session recovery protects work across refresh without consent or an explicit save action; persistence beyond session closure requires the explicit **Save on this device** opt-in. Storage choice and storage success never alter D/A/R1/C/R2/F or learning completion.

**Tier 1 — automatic session recovery.** The proposed shared service uses a sessionStorage adapter to checkpoint the complete draft on each accepted input/state change, including unfinished or over-limit text, evidence/diagnosis, v1, both reviews, C01 and rationale. Saving only at blur, stage transitions or unload is insufficient. Preserve IME composition text and apply completion checks to committed edits. Normal refresh in the active page session restores work without asking the learner to enable device saving. Show “Recoverable after refresh in this session” only after a successful checkpoint; a new uncheckpointed edit cannot retain a false success indication. Independent tabs have separate session drafts; duplicated tabs are not implicitly one shared writable draft.

**Tier 2 — explicit device saving.** Off by default. Explain shared-device visibility before opt-in. A shared localStorage adapter writes the current version immediately on consent and saves later edits; tier 1 stays active. Show “Saved on this device” only for a successful durable write of the relevant revision. Without consent, no fallback writes may be made to durable storage. On a later session with no session draft, offer a valid device draft for explicit resume, not automatic silent replacement. Consent belongs to that draft; visiting the page does not opt the user in. Disabling device saving stops writes and removes that draft's durable copy, retaining automatic session recovery. If removal fails, state that the old device copy remains.

**Restore and conflict rules.** Read before writing; validate envelope schema, activity/draft identity, contract version/revision, case version, known IDs and snapshot/review consistency. Incomplete/over-limit text is valid recoverable draft content. Recompute all completion predicates, never trust a stored complete flag. Stale reviews clear completion without erasing authored work. Missing or inconsistent immutable snapshot structure must trigger recovery handling, not regenerated v1. Prefer the valid matching session draft only when no divergent durable version conflicts. Do not choose by wall-clock timestamp or silently roll back to an older tier.

Corrupt/incompatible records remain untouched until an explicit recovery/discard decision. Show which tier failed and any valid alternate version with provenance. Never silently migrate, erase, overwrite or complete work. A divergent device update from another tab pauses affected writes, retains current memory and offers copy/export, explicit load-other-version or keeping local work as a new draft. No silent merge or last-write-wins. The state service owns these mechanics; the repair interaction supplies completion/review recomputation.

**Failure is an explicit degraded condition.** If tier 1 is denied/full, retain current memory, mark refresh recovery unavailable and offer copy/export immediately. This exception is not the normal memory-only policy and does not qualify as successful recovery. Do not silently switch to durable storage. If only tier 2 fails, report that independently: refresh recovery may still work while newer edits are not saved across closure. In either case in-memory learning completion remains possible. Export failure leaves selectable text available.

**Session boundaries and clear.** Automatic session recovery does not promise secure erasure on close: browser session restoration may revive page-session data. Cross-session retention is only promised under successful opt-in device saving. Provide an explicit Clear this draft action that confirms and removes this draft from both tiers, clears its consent and truthfully reports removal failures. It must not clear another activity or draft. No browser close/unload event is relied on for save or erasure guarantees.

The shared candidate is **SVC-LEARNING-STATE-01** under proposed `state/learning-state/`, using generic envelopes and callbacks. UI-SAVE-STATE-01 displays its receipts; INT-BUILD-REPAIR-01 owns the activity predicates. GR-05 must not call storage APIs directly or carry a local recovery implementation. This correction does not retroactively invalidate GR-03. No state service or prototype code is implemented here.

## 9. Composition and mobile transformation

The primary object is the work document. On wide screens, use one active writing/review stage with a reference region for original/evidence; keep readable input width and avoid a dashboard of unrelated cards. Stage navigation is compact and names the work, while output progress reflects authored/reviewed state rather than clicks.

At narrower widths, stack reference context, current fields, feedback and actions in a single coherent reading order. Use the existing shared 64rem/48rem/30rem conventions after G05-02 approval; do not create arbitrary reference-specific breakpoint rules. Keep evidence reachable through clearly labeled in-document links/disclosures. Mandatory feedback is open. Comparison becomes field-by-field “Before” followed by “After,” with repeated labels rather than a compressed multi-column grid.

Use normal document scrolling. Textareas can grow and remain manually resizable; long review text must not be clipped in a fixed-height pane. The mobile keyboard and sticky shell must not hide the focused control or actions. Returning from evidence restores the editing location without stealing text selection. No drag-and-drop, nested scroll region or modal is necessary for the core flow.

## 10. Accessibility and resilience

Use native fields with visible labels, associated instructions/counts, explicit fieldset legends where needed, visible keyboard focus and `aria-current="step"`. Announce meaningful save/review/stale-state changes politely, not every character. Errors identify the affected field and a recovery action. Changed state must use words as well as styling. Honor reduced motion, system font fallback and the current focus/accessibility tokens; flag a genuine shared token defect rather than inserting local fixes.

The validation matrix requires full keyboard and genuine Chrome 200% execution, screen-reader reading/label/error checks, narrow/mobile/landscape layouts, input-method composition and pasted multiline/long-token text. All original, evidence, input, feedback, comparison and Continue controls must remain reachable. Missing decorative imagery cannot affect completion; there is no required media. An offline interruption after load must not erase editing state or require an AI service. Without JavaScript, show the case and a clear unavailable-workspace notice with a plain-text exercise fallback, never false completion.

## 11. Required shared objects and implementation boundary

Existing IDs are listed in the JSON and verified against the local registry: shell, button/link/status/progress/save-state UI, explainer, case-evidence, feedback and takeaway. Case-evidence remains prototype. The save-state UI does not provide a persistence engine. Current concept/scenario/perspective objects do not become a studio through a renamed screen.

Final naming proposals, **not registered or implemented**:

| Gap | Proposed ID / name | Ownership and boundary |
| --- | --- | --- |
| G05-01 | IP-BUILD-REPAIR-01 — Deep Build / Repair | Shared learning architecture; capability and work/review cycle |
| G05-01 | BLK-WORK-ARTIFACT-01 — Working Artifact | Shared learning block; fields, evidence associations, comparison and output serialization |
| G05-01 | INT-BUILD-REPAIR-01 — Build / Repair Review | Shared interaction reducer; immutable v1, predicates, invalidation and acknowledgment |
| G05-02 | CMP-REPAIR-STUDIO-01 — Repair Studio | Shared responsive composition; no persistence or completion logic |
| G05-02 | TPL-DEEP-WORKSPACE-01 — Deep Workspace | Shared template assembly/authoring slots; no HRBA-specific behavior |
| G05-03 | SVC-LEARNING-STATE-01 — Shared Learning State and Recovery | Shared `state/learning-state/` service; two-tier recovery, validated envelopes, receipts, conflicts and clear/export hooks |

The JSON and [candidate/architecture record](GR-05_ARCHITECTURAL_CORRECTIONS_AND_CANDIDATES_v0.1.md) specify proposed paths, registry destinations and owner roles. The service type in the existing component registry and shared state root are explicit proposals requiring final freeze, not silent architecture additions. No token, registry entry, service code or candidate promotion is made.

## 12. Review decisions and stop

The accepted learning design and two architectural corrections are preserved. Final review should freeze revision 2, including T and the operational recovery details, confirm the six proposed shared IDs/ownership interfaces, and explicitly authorize implementation and validation. The existing proposed validation scope is retained and extended for both corrections; it has not been executed against a prototype.

This task ends with the preflight and deterministic proposal. No HTML/CSS/JS prototype, new registry entry, generated artwork, external resource ingestion or runtime schema migration is authorized or performed.
