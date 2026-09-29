# Wave-2 current architecture and authority index

Current outcome: **WAVE_2_PASS_WITH_BOUNDED_CORRECTIONS**, accepted by ChatGPT as explicitly conveyed by the user. Machine-readable authority: [WAVE_2_CURRENT_AUTHORITY.json](WAVE_2_CURRENT_AUTHORITY.json). Latest decision: [governance update](governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json).

The full original Gate-1–8 architecture and historical future-reference numbering source have **not been recovered**. Future coverage is governed by capability until an authoritative historical numbering source is located. No unrecovered numbering is invented; four mandatory separate GR-07/08/09/10 builds are not assumed. Track A Revision 1 is frozen and its prototype is implemented pending manual validation; see the current implementation authority below. Track B remains proposed and unauthorized.

## Precedence and current build authority

1. Latest explicit user-conveyed architectural decisions in governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json
2. Frozen build inputs and exact locked contracts within their scope
3. Current registries and shared schemas/validation policy
4. Historical reviews and proposal text as evidence, not current permission

| Artifact | Authority/scope |
| --- | --- |
| [governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json](governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json) | CURRENT: Latest explicit ChatGPT governance update, conveyed by user |
| [docs/ai-build-contract.md](docs/ai-build-contract.md) | CURRENT: Shared assembly/authority boundary |
| [docs/resource-first-workflow.md](docs/resource-first-workflow.md) | CURRENT: Resource-first preflight |
| [docs/system-gap-process.md](docs/system-gap-process.md) | CURRENT: System Gap escalation |
| [docs/TEMPLATE_SCHEMA_RECONCILIATION.md](docs/TEMPLATE_SCHEMA_RECONCILIATION.md) | CURRENT: Accepted canonical structured template compatibility |
| [governance/validation-policy.json](governance/validation-policy.json) | CURRENT: Current ID/variant/build/authority validation and scoped historical alias |
| [schemas/golden-reference.schema.json](schemas/golden-reference.schema.json) | CURRENT: One authoritative Golden Reference schema; episode schema delegates |
| [prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.md](prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.md) | CURRENT: Mandatory future experience differentiation specification |
| [schemas/experience-differentiation-brief.schema.json](schemas/experience-differentiation-brief.schema.json) | CURRENT: Machine-readable future differentiation contract |
| [governance/accessibility-resilience-baseline.json](governance/accessibility-resilience-baseline.json) | CURRENT: Universal/conditional future validation declaration |
| [locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json](locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json) | LOCKED: D3 locked build and rendering authority |
| [locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json](locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json) | LOCKED: D3 locked build and rendering authority |
| [prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json](prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) | FROZEN: GR-03 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-03_VALIDATION_MATRIX_v0.1.md](prototype-specs/GR-03_VALIDATION_MATRIX_v0.1.md) | FROZEN: GR-03 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json](prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) | FROZEN: GR-05 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-05_VALIDATION_MATRIX_v0.1.md](prototype-specs/GR-05_VALIDATION_MATRIX_v0.1.md) | FROZEN: GR-05 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json](prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) | FROZEN: GR-06 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-06_VALIDATION_MATRIX_v0.1.md](prototype-specs/GR-06_VALIDATION_MATRIX_v0.1.md) | FROZEN: GR-06 frozen build inputs; original proposal/permission labels are historical within the frozen content |
| [prototype-specs/GR-05_DETERMINISTIC_LEARNING_DESIGN_v0.1.md](prototype-specs/GR-05_DETERMINISTIC_LEARNING_DESIGN_v0.1.md) | ACCEPTED_FROZEN_INPUT: GR-05 accepted Revision 2 design/resource decisions; no new reinterpretation |
| [prototype-specs/GR-05_RESOURCE_FIRST_PREFLIGHT_v0.1.md](prototype-specs/GR-05_RESOURCE_FIRST_PREFLIGHT_v0.1.md) | ACCEPTED_FROZEN_INPUT: GR-05 accepted Revision 2 design/resource decisions; no new reinterpretation |
| [prototype-specs/GR-05_RESOURCE_INVENTORY_v0.1.json](prototype-specs/GR-05_RESOURCE_INVENTORY_v0.1.json) | ACCEPTED_FROZEN_INPUT: GR-05 accepted Revision 2 design/resource decisions; no new reinterpretation |
| [prototype-specs/GR-06_DETERMINISTIC_LEARNING_DESIGN_v0.1.md](prototype-specs/GR-06_DETERMINISTIC_LEARNING_DESIGN_v0.1.md) | ACCEPTED_FROZEN_INPUT: GR-06 accepted Revision 2 design/resource decisions; no new reinterpretation |
| [prototype-specs/GR-06_RESOURCE_FIRST_PREFLIGHT_v0.1.md](prototype-specs/GR-06_RESOURCE_FIRST_PREFLIGHT_v0.1.md) | ACCEPTED_FROZEN_INPUT: GR-06 accepted Revision 2 design/resource decisions; no new reinterpretation |
| [prototype-specs/GR-06_RESOURCE_INVENTORY_v0.1.json](prototype-specs/GR-06_RESOURCE_INVENTORY_v0.1.json) | ACCEPTED_FROZEN_INPUT: GR-06 accepted Revision 2 design/resource decisions; no new reinterpretation |

## Reference status and provenance

| Reference | Current status | Meaning / provenance |
| --- | --- | --- |
| GR-01 | D3_LOCKED_BUILD | Course entry; lock does not imply new acceptance decision.   |
| GR-02 | WAVE_1_EXISTING_BASELINE | Concept/choice/feedback; transitional template string retained; no new acceptance claimed.   |
| GR-03 | PASS_FOR_WAVE_2_SYSTEM_REVIEW | Guided interpretation; refresh persistence observation remains outside frozen contract.   |
| GR-04 | D3_LOCKED_BUILD | Professional judgment; exact default render and behavior protected.   |
| GR-05 | PASS_FOR_WAVE_2_SYSTEM_REVIEW | Deep repair; prior pass contained punctuation encoding defect, corrected later under W2-C03. V05/V25 PASS, ChatGPT review reported by user V21/V23/V22-mobile PASS, user-attested |
| GR-06 | IMPLEMENTED_PENDING_MANUAL_VALIDATION | Evidence to interpretation to decision to update to review. H01–H09 PASS, ChatGPT review explicitly reported by user Native Chrome 200% PASS, user-attested; actual screen reader and physical-mobile software keyboard PENDING |

Automated reports remain separate from user-attested direct checks and ChatGPT architectural/HRBA review. GR06 H01–H09 is PASS; native Chrome 200% is user-attested PASS; its screen-reader and physical-mobile checks remain pending. Existing synthetic packets retain exact reviewed content and original metadata; the current decision record supersedes their old pending labels.

## Candidate disposition

| ID | Literal registry status | Review recommendation (not promotion) |
| --- | --- | --- |
| BLK-PERSPECTIVE-01 | prototype | REVISE BEFORE APPROVAL |
| INT-LABELED-GRAPHIC-01 | prototype | REVISE BEFORE APPROVAL |
| CMP-PERSPECTIVE-01 | prototype | RETAIN AS PROTOTYPE |
| IP-INTERPRET-01 | prototype | REVISE BEFORE APPROVAL |
| IP-PERSPECTIVE-01 | prototype | REVISE BEFORE APPROVAL |
| IP-BUILD-REPAIR-01 | PROTOTYPE | READY FOR APPROVAL CANDIDATE |
| BLK-WORK-ARTIFACT-01 | PROTOTYPE | REVISE BEFORE APPROVAL |
| INT-BUILD-REPAIR-01 | PROTOTYPE | REVISE BEFORE APPROVAL |
| CMP-REPAIR-STUDIO-01 | PROTOTYPE | RETAIN AS PROTOTYPE |
| TPL-DEEP-WORKSPACE-01 | PROTOTYPE | REVISE BEFORE APPROVAL |
| SVC-LEARNING-STATE-01 | PROTOTYPE | READY FOR APPROVAL CANDIDATE |
| BLK-EVIDENCE-LEDGER-01 | PROTOTYPE | RETAIN AS PROTOTYPE |
| INT-EVIDENCE-DECISION-01 | PROTOTYPE | RETAIN AS PROTOTYPE |
| IP-EVIDENCE-DECISION-01 | PROTOTYPE | RETAIN AS PROTOTYPE |
| CMP-EVIDENCE-DECISION-01 | prototype | RETAIN AS PROTOTYPE |

## Remaining Gate-8 capability coverage

| Capability | Current proof | Remaining proof | Proposed grouping |
| --- | --- | --- | --- |
| Assessment | GR05/06 structural self-review and separately reviewed synthetic examples | Representative integrated capability/evidence assessment with explicit human/assessor roles; structural completion is not competence. | Track A proposed |
| Practice/application | GR05 authored repair; GR06 reasoned and adapted action | Own-context transfer, return with practice evidence and retained portfolio lifecycle remain unproven. | Track B proposed |
| Feedback/remediation | GR02/03/04 authored feedback; GR05/06 revision and unresolved follow-up | Assessment-linked remediation/reconsideration and peer evidence dialogue need representative coverage. | A/B proposed |
| Decision/gate | GR04 judgment; GR06 trial/verify/retain/escalate with authority boundaries | Integrated readiness gate over learner evidence with proportionate proceed/revise/review/defer consequences. | Track A proposed |
| Completion | Reference-level structural completion, stale-review invalidation and acknowledgment | Course/practice lifecycle completion semantics must distinguish progress, competence, delivery and consent. | Capability governed |
| Responsive/accessibility/resilience | Automated cross-reference responsive/stress/state tests; GR03/05 scoped manual attestations | GR06 screen-reader and physical-mobile checks; every future reference declares universal and conditional baseline; no cross-reference transfer of passes. | Universal/conditional, not a separate mandatory build |
| Related experience families: portfolio, bridge, peer dialogue, contribution | Local recovery and export only; no live Hub handoff or peer workflow proved | Provenance, consent, receipt/failure/retry, roles, moderation, update/withdrawal and accessible lifecycle coverage; mock is not live integration. | Track B proposed; split only for demonstrable independent lifecycle need |

## Preserved history

The four original consolidated review artifacts remain byte-for-byte historical baseline. Their earlier semantic-pending language and numbering proposals are superseded by this index. Prior reports/screenshots and the original reviewed ZIP remain evidence of the build as it then existed, including the GR05 encoding defect. The machine index records exact hashes of listed historical artifacts. No old review is rewritten to suggest the defect never existed.

- [WAVE_2_CONSOLIDATED_SYSTEM_REVIEW_v0.1.md](WAVE_2_CONSOLIDATED_SYSTEM_REVIEW_v0.1.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [WAVE_2_OBJECT_DISPOSITION_MATRIX_v0.1.md](WAVE_2_OBJECT_DISPOSITION_MATRIX_v0.1.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [WAVE_2_REMAINING_COVERAGE_AND_NEXT_REFERENCES_v0.1.md](WAVE_2_REMAINING_COVERAGE_AND_NEXT_REFERENCES_v0.1.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [WAVE_2_SYSTEM_REVIEW.json](WAVE_2_SYSTEM_REVIEW.json): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md](docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [Repository_Alpha_Materialization_Report_v0.2-alpha.md](Repository_Alpha_Materialization_Report_v0.2-alpha.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [Repository_Rebuild_Review_and_Duplicate_Build_Preparation_v0.1.md](Repository_Rebuild_Review_and_Duplicate_Build_Preparation_v0.1.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [Baseline_Reconciliation_and_System_Correction_Report_v0.2.2-alpha.md](Baseline_Reconciliation_and_System_Correction_Report_v0.2.2-alpha.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [tests/gr06-semantic-fixtures.json](tests/gr06-semantic-fixtures.json): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [golden-references/GR-06/GR-06_SEMANTIC_REVIEW_PACKET.md](golden-references/GR-06/GR-06_SEMANTIC_REVIEW_PACKET.md): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language
- [tests/wave2-review/consistency-results.json](tests/wave2-review/consistency-results.json): Preserved historical evidence; current authority/status overlays supersede any earlier pending/proposal language

No candidate promotion, Golden Reference acceptance, System v1 freeze, PM stress test, HRBA reconstruction, Track A/B implementation or new reference build is authorized by this index. Track A specification-only authorization is recorded in the latest decision. Future specifications must use the [differentiation brief](prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.md) and declare universal/conditional validation; existing frozen references are not redesigned.

## Historical Track A preflight authorization

Latest authority: [Track A request and GR06 attestation](governance/TRACK_A_PREFLIGHT_AUTHORITY.json). That preflight decision was specification-only; the later explicit Revision 1 freeze now authorizes the bounded prototype. GR06 is an upper bound on authored-work burden, not a future screen template. Track A must substantially reduce writing and distinguish its review rhythm. Exact prior index/evidence bytes are retained under tests/track-a-preflight/baseline.

Proposed package: [resource-first preflight](prototype-specs/TRACK_A_RESOURCE_FIRST_PREFLIGHT_v0.1.md), [deterministic design](prototype-specs/TRACK_A_DETERMINISTIC_LEARNING_DESIGN_v0.1.md), [exact JSON contract](prototype-specs/TRACK_A_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json) and [validation matrix](prototype-specs/TRACK_A_VALIDATION_MATRIX_v0.1.md). Historical preflight result: TRACK_A_READY_FOR_ARCHITECTURAL_FREEZE_REVIEW. Superseded for Track A by the explicit Revision 1 freeze below.

## Track A implementation authority — current

Latest authority: [explicit Revision 1 freeze](governance/TRACK_A_FREEZE_AUTHORITY.json). Checkpoint: `d4e72e3a898e63ec084288925155781c4c58fce3`. Current status: **IMPLEMENTED_PENDING_MANUAL_VALIDATION**. [Result](golden-references/TRACK-A/RESULT_SUMMARY.md).

Three new shared candidates remain **PROTOTYPE**. Only opt-in readiness-review variants were added to the selected composition and scenario template; prior consumers/defaults and the state service are unchanged. V15/V16/V17 direct checks, V19 observed burden and V20/H01–H10 independent semantic review are pending. Automated execution is separate evidence. No Golden Reference acceptance or assessment validity is claimed.

Track A is a rehearsal recommendation against transparent criteria, never independent competence judgment, certification, formal assessment or organizational/public authorization. Proposal-era status and no-build wording in the frozen source package are retained historically; this explicit freeze supersedes those authority fields for the bounded implementation only. Prior index snapshots remain under tests/track-a-preflight/baseline. Future coverage remains capability-governed; no GR number, Track B authorization, PM stress or HRBA reconstruction is inferred.
