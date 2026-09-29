# GR-03 refresh persistence — architectural observation

Status: OPEN, NONBLOCKING for PASS_FOR_WAVE_2_SYSTEM_REVIEW. Date: 2026-09-28.

The user reports that current learner selection/state does not persist after a browser refresh. This was not part of the frozen GR-03 validation contract; it does not invalidate the manual 200% pass. No production change or GR-03-local persistence fix was made.

## Classification from available repository authority

Refresh persistence is **currently unspecified for GR-03 and for a general shared learning-state lifecycle in the available repository**. This is an architectural question, not a demonstrated violation of an existing global persistence requirement. The conclusion is limited to available local authority; it does not claim to resolve unavailable upstream architectural documents.

- `prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json` freezes completion as `all_perspectives_visited && interpretation_submitted && feedback_viewed`, optional revision and interaction structure. It does not define storage, refresh restoration or session continuity. The validation matrix likewise has no refresh-persistence requirement.
- `interactions/labeled-graphic/labeled-graphic.js` holds visited perspectives in a new in-memory Set and answer/feedback/completion in DOM state. No storage adapter or restoration mechanism is present. Its `state=complete` / `choice` query parameters initialize a preview state; they do not save actual learner state.
- `shell/course-shell.js` creates navigation and progress display from host attributes; it does not implement a shared learner-state store or reload restoration.
- `ui/save-state/manifest.yaml` has global scope but its implementation is `save-state.css`. The presence of shared save-state presentation does not define persistence behavior for every interaction.
- `locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json` explicitly sets `practice_focus_persistence: local_if_available` with a practice-focus storage key. `practice/practice-focus/practice-focus.js` implements that scoped requirement using localStorage with failure handling. This establishes persistence for practice-focus, not a universal requirement for GR-03.

## Architectural review needed

Decide whether shared learning state must survive refresh and, if so, define its ownership, scope, storage lifetime, version/reset behavior, unavailable-storage behavior, and which visited/selected/reviewed/completed fields must restore consistently. Any resulting implementation belongs in governed shared architecture, with an explicit contract and validation scope; no reference-local workaround is proposed or authorized here.

The separate template-schema inconsistency has been resolved in code under explicit user authorization; see `TEMPLATE_SCHEMA_RECONCILIATION.md`. Architectural review remains pending. This persistence observation remains open and does not authorize GR-05, Golden Reference acceptance, or candidate promotion.
