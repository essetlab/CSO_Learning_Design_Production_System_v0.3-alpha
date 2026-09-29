> Revision 2 follow-up: source inspection/dispositions below are retained. The two architectural corrections and six final candidate naming proposals are recorded in [the correction record](GR-05_ARCHITECTURAL_CORRECTIONS_AND_CANDIDATES_v0.1.md). This preflight does not authorize a build.

# GR-05 resource-first preflight — Deep Build / Repair Studio

Status: **SPECIFICATION FOR ARCHITECTURAL REVIEW; NO PROTOTYPE IMPLEMENTED**. Date: 2026-09-28.

The accepted template-schema correction is preserved in commit `300362b72f714ea152d0b7812c42906938acb24c` on `gate8/wave2/gr03-browser-validation`. The current branch is `gate8/wave2/gr05-deep-build-repair`, created from that commit. No remote was configured and nothing was pushed. GR-03 remains PASS_FOR_WAVE_2_SYSTEM_REVIEW; its candidate objects were not promoted.

## Learning need before resource choice

GR-05 should develop a CSO practitioner's ability to turn an evidence-based diagnosis into a practical, coherent improvement note, then revise it when a constraint changes. Its proof is authored work and an explainable revision, not selecting the preferred sentence. The recommended bounded task is **repairing the market participation and response arrangements in the fictional Jiru Amba plan**. A whole project, logframe or multi-screen course would dilute this reference's test of deep work.

The strongest existing content source is HRBA's Project Design Repair and its editable objective/activity/logic templates. The strongest complementary mechanic is PM's connected-plan repair and invalidation of dependent decisions. Mighty contributes document rows, aligned comparison and labeled writing areas. No inspected source supplies a directly reusable, registered studio satisfying the full need.

## Inspection scope and provenance

The [resource inventory](GR-05_RESOURCE_INVENTORY_v0.1.json) records 24 classified source groups, exact file paths, SHA-256 hashes and inspection scope. Paths are provenance records, not runtime dependencies. Source repositories were read only; no source code, learner records, branding binaries or external templates were copied into this repository.

| Resource family | Inspected local source | Authority and limits |
| --- | --- | --- |
| Current shared system | Authoritative D: v0.3-alpha repository | Registries, shared implementations, GR-01–04, frozen GR-03 contract, schema correction and state observation inspected. `repo-alpha-ready` and `prototype` are reported literally; neither means universally APPROVED. |
| Mighty Studio pack | `D:/templates_elearning_resource_pack`; HEAD `e5569a9097091cab97f2c57ddadfa9fa69e07743` | Catalog, selection/use-case guidance, manifest and selected previews inspected. Visual inspection of TPL-LAY-003, TPL-ACC-008 and TPL-REF-002. Their images are pattern references, not working code. Historical readiness counts are not current inventory counts. |
| HRBA R&D | `D:/eLearn_CDP_Lg`; HEAD `de8a8857f27a903662c417998f73a09bbf1cdc9d` | Jiru Amba narrative, relevant renderer/state sections, reusable Markdown templates and a report recording accepted integrated-repair refinements inspected. Selected source files have no working-tree diff. The report describes an earlier release candidate, not proof that every current line has fresh acceptance. |
| HRBA visual evidence | `D:/Module 3 Final Pilot Version Full Screenshots` | Generated repair package and own-project input screenshots inspected. These are partial scrolled states; no new live-browser accessibility claim. |
| PM R&D | `D:/pm-certified-release-20260924`; HEAD `8a6dabd3e8e8dc763eb3289a57472edc7d575871` | Accepted-current config, source-authority hierarchy, frozen Module 3 acceptance record, relevant runtime and state helpers inspected. Config points to FinalModule3Plan; its acceptance record reports 70 tests at that historical acceptance. No fresh PM regression run is claimed. |
| Hub/assets/institutional branding | Current shared shell/assets; HRBA state and partner file inventory; PM's HRBA reuse audit | Supports reuse decisions only. No remote deployment was revisited, learner data inspected or branding approval inferred from a file's presence. |

Office tool files in PM were inventoried through their authoritative README, not content-audited. They are not selected for ingestion. The preliminary `hrba-in-practice` file-tree scan was a discovery lead only; the richer implemented HRBA source superseded it as the chosen reference. Other unrelated D: repositories were not exhaustively inspected.

## Disposition of every relevant source group

| ID | Source / pattern | Disposition | Decision for GR-05 |
| --- | --- | --- | --- |
| R01 | Current tokens and foundations | REUSE DIRECTLY | Use existing typography, spacing, color, focus and reduced-motion values. No new token proposed. |
| R02 | Shared shell, buttons, status, progress | REUSE DIRECTLY | Preserve global behavior and branding. Add any approved workspace integration through shared ownership. |
| R03 | Explainer/evidence/feedback/takeaway blocks | ADAPT | Supply brief, case evidence and criterion feedback. Preserve actual registry status, including prototype evidence block. |
| R04 | GR-03 perspectives; GR-04 judgment | REFERENCE ONLY | Borrow clarity of evidence and feedback. Their interaction/output model does not meet deep authoring needs. |
| R05 | Single-choice/answer-review as primary flow | REJECT | Cannot demonstrate creating and improving the learner's own output. |
| R06 | Practice-focus local save / save-state UI | HARVEST PATTERN | Failure tolerance and honest state labels; single-value persistence cannot retain a revision package. |
| R07 | Mighty catalog, selection matrix and manifests | REFERENCE ONLY | Establish available patterns, provenance and confidence; external IDs are not local registered IDs. |
| R08 | TPL-LAY-003 Content Rows | HARVEST PATTERN | Field-aligned, calm document reading. Use semantic rows without importing vendor style. |
| R09 | TPL-ACC-008 Reveal table content | HARVEST PATTERN | Aligned before/after details. Do not conceal mandatory evidence or review behind optional clicks. |
| R10 | TPL-REF-002 Stacked Reflection | HARVEST PATTERN | Labeled writing areas and retained output affordances. Screenshot “Saved” text does not establish storage behavior. |
| R11 | TPL-ACC-009, TPL-TRANS-001, TPL-SCEN-002 | REFERENCE ONLY | Stage orientation, responsive grouping and guided prompts, catalog-level inspection only. |
| R12 | Image slider, flip/card/reveal paradigms | REJECT | Unsuitable as the main editable artifact or completion model. Rejection is scoped to GR-05. |
| R13 | HRBA fictional Jiru Amba narrative | ADAPT | Ground the evidence in access, influence, responsibility and response; explicitly distinguish proposed exercise text. |
| R14 | HRBA Project Design Repair runtime | HARVEST PATTERN | Reuse the staged reasoning, package continuity and stale-output concept. Reject copying prepared-answer gates or the monolithic renderer. |
| R15 | HRBA repair/output screenshots | REFERENCE ONLY | Useful output hierarchy; do not copy fixed-height frames, tool sidebars or donor bars. |
| R16 | HRBA objective/activity/logic/section-repair tools | ADAPT | Best foundation for the improvement note and portable artifact structure. Condense, do not reproduce the whole tool pack. |
| R17 | HRBA learning-state infrastructure | HARVEST PATTERN | External precedent for versioned state. It does not establish an already-approved persistence contract in this repository. |
| R18 | PM connected-plan repair and records | HARVEST PATTERN | Diagnose ambiguity, repair connected consequences and show an authentic record; do not import PM case facts. |
| R19 | PM change-control dependency invalidation | HARVEST PATTERN | Editing upstream work invalidates downstream review. Preserve text while clearing completion. |
| R20 | PM local screen-state helper | HARVEST PATTERN | Useful fallback behavior; add explicit payload/version/conflict policy through architecture, not a local copy. |
| R21 | PM tool-pack / HRBA-Hub audit records | REFERENCE ONLY | Support optional download and reuse boundaries; do not infer a completion gate from download availability. |
| R22 | Existing registered HRBA illustrations | REFERENCE ONLY | Available asset alternatives; no hero needed because the working document is the main visual object. |
| R23 | Existing DEC/partner branding files | REFERENCE ONLY | Inventory only. Use current shared shell branding; no additional logo treatment. |
| R24 | Missing registered deep-work capability | SYSTEM GAP | Propose G05-01/02/03 below. Names/IDs are now explicitly proposed in revision 2; no code or registry entries created. |

No source has been classified REUSE DIRECTLY solely because it looks attractive. Every external source requires normalization, accessibility/responsive validation and explicit candidate registration before production ingestion. Medium-confidence or `needs-review` pack items are not selected as authoritative templates.

## Chosen synthesis and limits

Use the HRBA template sequence **weakness → evidence → repaired wording → responsibility → safe evidence**, PM's **change → affected work → review invalidation**, and Mighty-style **labeled writing rows / aligned comparisons**. The work surface, not a decorative hero or character, carries the experience.

The required HRBA source path primarily completes through selecting prepared objectives/actions/indicators; authored own-CSO work is optional. That is a useful precedent but insufficient for this reference. GR-05 makes writing and revising four connected sections mandatory. A constrained case keeps subject-matter demands manageable; it does not turn prose into an auto-graded answer bank.

The learner produces one bounded note with diagnosis, v1, criterion review, v2 and revision rationale. Completion proves the work/review cycle, not that the note is professionally approved. Comparison must reveal the learner's own changed fields, not only an authoritative model.

## Legitimate System Gaps — proposals, not registration

| Gap | Requirement | Why existing objects are insufficient | Proposed shared ownership / review |
| --- | --- | --- | --- |
| G05-01 | Authored artifact, evidence binding, immutable first-review snapshot and revision-bound feedback | Choice/perspective interactions and feedback blocks do not own editable versions or field comparison | Shared artifact block and repair interaction, plus a deep-build learning pattern. Revision 2 proposes IP-BUILD-REPAIR-01, BLK-WORK-ARTIFACT-01 and INT-BUILD-REPAIR-01; final freeze authorizes registration. |
| G05-02 | Deep-workspace composition/template | Current concept/scenario templates define explanation or decision screens, not a persistent document workspace | Shared composition/template assembled from the shell, existing blocks and G05-01. No unapproved tokens or reference-local overrides. |
| G05-03 | Draft retention, truthful save/recovery, snapshot serialization and copy/export | Save-state UI is CSS; practice-focus stores one selection. HRBA/PM adapters exist elsewhere but are not registered services here | Shared learning-state adapter with explicit schema/case version, session-only fallback and conflict policy. Revision 2 applies the accepted two-tier rule: automatic session recovery plus explicit opt-in durable device saving. Final shared interfaces await freeze. |

These are documentation gap identifiers. Revision 2 proposes six named shared objects in `GR-05_ARCHITECTURAL_CORRECTIONS_AND_CANDIDATES_v0.1.md`; none is registered. The builder must not change the final frozen ownership or register IDs before authorization. A shared typography/color redesign, a new illustration, AI grading, a backend, an LMS bridge or a whole-course portfolio system is not justified by this reference.

## Authority and review boundary

**LOCKED now:** user scope and stop boundary, shared repository authority, preservation of accepted references/candidates, fictional-case provenance, no implementation.

**CONSTRAINED:** reuse/adaptation must follow current tokens, accessibility behavior, resource provenance and shared ownership. Copy adjustments cannot change the capability or erase revision work.

**Architectural review update:** capability, case/task sequence and retained work/review design are substantially accepted. Revision 2 applies the required automatic-session/opt-in-device retention rule and removes hard word minima while retaining maxima. Final candidate IDs/interfaces, minimal T check and operational detail await final freeze and implementation authorization; no prototype is built.

Review the [deterministic specification](GR-05_DETERMINISTIC_LEARNING_DESIGN_v0.1.md), [machine-readable proposal](GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) and [validation matrix](GR-05_VALIDATION_MATRIX_v0.1.md). No runnable `golden-references/GR-05` directory is created before its objects and specification are approved.
