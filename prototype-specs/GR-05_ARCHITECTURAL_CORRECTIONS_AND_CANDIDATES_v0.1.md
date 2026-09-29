> FROZEN FOR PROTOTYPE IMPLEMENTATION by user architectural approval. Revision 2 is authoritative; earlier pending-authorization wording below is historical. Six shared candidates are authorized at PROTOTYPE only. Validation results must be recorded separately; no Golden Reference acceptance or GR-06.

# GR-05 architectural corrections and final candidate proposals

Revision 2, 2026-09-28. Status: **RETURNED FOR FINAL FREEZE AND IMPLEMENTATION AUTHORIZATION**. The user's architectural review substantially accepts the capability and learning sequence and requires the two corrections below. No prototype, registry entry, shared service or token is implemented.

## Accepted learning authority preserved

Evidence-linked diagnosis → authored four-section repair → immutable v1 review → C01 → revision → v1/current comparison → final review/acknowledgment remains intact. The weak original note, E01–E05, C01, criteria, no-AI-grading rule, no prepared-answer completion and stale-review invalidation are preserved. The JSON records hashes of seven preserved sections; verification checks them against the revised contract. Layout/accessibility and the original V01–V26 scope remain, with corrected cases and added V27–V30.

## Correction 1: two-tier shared learning state

The old default held work in memory and warned that refresh would lose it. **That policy is superseded.** Automatic recovery must now preserve unfinished artifact work through refresh in the active browser session without an opt-in. Explicit **Save on this device** governs only persistence beyond session closure.

The proposed shared implementation uses sessionStorage for tier 1 and localStorage for opt-in tier 2. These are service adapters, not GR-05 code. Keep independent per-tier success/failure receipts and saved revisions. Never show success before a write succeeds or silently use durable storage when session storage fails. Incomplete/over-limit writing is valid recovery content even when it cannot pass a review gate.

Restore validates schema/identity/contract revision/case and snapshot/review consistency, then recomputes completion. Corrupt, incompatible or divergent records cannot silently overwrite, migrate, roll back or complete work. Conflict handling preserves local work and requires explicit selection of a version or a new draft. Opt-out stops durable writes and removes that draft's device copy while preserving refresh recovery; deletion failures remain visible. Confirmed clear affects only this draft and both tiers. Neither storage choice nor save success appears in the learning completion expression.

Session-storage behavior is not a promise of secure erasure on closing a browser: browsers may restore page-session data. The design explicitly distinguishes refresh protection, durable retention, degraded storage failure and deliberate clear. A failed session write is an honest degraded condition with copy/export recovery, not an acceptable default loss-on-refresh implementation.

## Correction 2: concise authored work, no filler gates

Removed every hard minimum word count: artifact minima 25/45/40/30; diagnosis 15; criterion justifications/follow-ups 10; rationale 20. Their unchanged hard maxima are respectively **70/110/100/80, 50, 35/35 and 70**.

Proposed structural rule **T** requires at least two Unicode Letter/Number code points after trimming whitespace for each required authored response. It prevents empty/punctuation-only/single-character placeholders without an English-word, grammar or sentence requirement. Short phrases and bullets are valid; qualitative soft prompts describe the idea needed and never gate progression. No specific hard word minimum is pedagogically necessary for this task.

T is intentionally not a meaning detector. Adequate authored evidence still comes from four evidence-linked diagnoses, four original repairs, both criterion reviews, a constraint-driven change in two connected fields and an explained revision. Human instructional/HRBA review evaluates that substance for Golden Reference quality. Runtime structural completion cannot certify professional judgment, and no AI/keyword grader is introduced to replace the removed minima.

## Final proposed shared names, IDs and ownership

All IDs below have status **PROPOSED_NOT_REGISTERED**, proposed version `0.1.0-proposed`, scope `shared-cso-system`. Owner names are responsibility roles, not invented staff assignments. No path listed below has been created.

| Gap | Candidate ID and name | Proposed ownership/location | Proposed registry |
| --- | --- | --- | --- |
| G05-01 | **IP-BUILD-REPAIR-01 — Deep Build / Repair** | Learning architecture; `docs/patterns/build-repair/`; capability, authored work and review/revision cycle | `registries/patterns.json` |
| G05-01 | **BLK-WORK-ARTIFACT-01 — Working Artifact** | Shared learning-block maintainer; `learning-blocks/work-artifact/`; fields/evidence associations, semantic comparison and output serialization | `registries/components.json`, type `block` |
| G05-01 | **INT-BUILD-REPAIR-01 — Build / Repair Review** | Shared interaction/state maintainer; `interactions/build-repair/`; activity reducer, immutable snapshot, predicates, invalidation and acknowledgment | `registries/components.json`, type `interaction` |
| G05-02 | **CMP-REPAIR-STUDIO-01 — Repair Studio** | Shared composition/accessibility maintainer; `compositions/repair-studio/`; responsive reference/document/stage layout | `registries/compositions.json` |
| G05-02 | **TPL-DEEP-WORKSPACE-01 — Deep Workspace** | Shared template/authoring maintainer; `templates/deep-workspace/`; assemble registered shell, composition, artifact and required slots | `registries/templates.json` |
| G05-03 | **SVC-LEARNING-STATE-01 — Shared Learning State and Recovery** | Shared learning-state architecture maintainer; **`state/learning-state/`**; two-tier adapters, validated envelopes, receipts, conflict/restore/reset and serialization hooks | `registries/components.json`, proposed explicit type `service` |

The `service` type and shared `state/` location are explicit final-freeze proposals. They fit the existing generic system-object schema's ID convention; schema compatibility alone is not registration or authorization. Use the existing component registry rather than silently introducing a second service registry. Synchronize JSON/YAML registries only after final implementation/registration authorization. No new visual token or save-state UI object is proposed; UI-SAVE-STATE-01 displays truthful receipts from the service.

## Interfaces and ownership boundaries to freeze

- **Artifact block:** accepts approved field definitions and current/snapshot data; emits plain-text edits; renders complete comparison and produces a safe output representation. It has no direct browser-storage calls and no grading logic.
- **Repair interaction:** owns D/A/R1/C/R2/F, immutable v1 and review invalidation; accepts validated restored state and recomputes predicates. It checkpoints state via the service. The state service cannot mark the learner complete.
- **Learning-state service:** accepts activity identity/version, a payload validator, serializers and reducer/revalidation callbacks. It owns tier selection, consent, receipts, compatibility/conflict/clear behavior and recovery. It is independent of HRBA wording, evidence IDs and correct answers; the activity adapter supplies those constraints.
- **Composition/template:** arrange the existing shared shell and blocks. They do not persist data, decide completion or reimplement activity logic. Any future reference contains content/configuration and wiring only.
- **Export:** the artifact block defines content/order; the service supplies generic safe serialization/download hooks. Clipboard failure must leave selectable on-page text. Export is never a completion gate.

## Final decision requested

Freeze revision 2's concrete T rule and operational two-tier behavior, approve the six proposed IDs and shared ownership boundaries, then explicitly authorize prototype implementation. Until then, only specifications and integrity evidence change. Existing references and candidate statuses remain untouched.
