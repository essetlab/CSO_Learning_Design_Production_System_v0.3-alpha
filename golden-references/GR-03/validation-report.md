## Shared template-schema correction — 2026-09-28

The previously open template-schema/validator inconsistency is now **RESOLVED IN CODE, awaiting architectural review**. See `docs/TEMPLATE_SCHEMA_RECONCILIATION.md`. One authoritative schema accepts canonical `{id, variant?}` objects plus transitional legacy strings; the episode schema references it. Repository validation now checks all four Golden Reference YAML specifications and verifies template IDs and declared variants against the registry. No specification migration or learner-code change was needed; GR-02 retains its supported legacy string.

Regression PASS: all 13 static/schema/syntax commands, eight schema test methods with positive/negative cases, exact GR-01/04 locked renders, and 423 browser assertions including 116 maximum-content checks. New browser evidence: `tests/gr03-browser-validation-schema-reconciliation.json`; summary: `tests/schema-reconciliation-summary.json`. The accepted native 200% attestation remains applicable to unchanged learner code; it was not repeated.

GR-03 remains **PASS_FOR_WAVE_2_SYSTEM_REVIEW**, not Golden Reference acceptance. Candidate objects remain PROTOTYPE / RETAIN CANDIDATE. Refresh persistence remains an open nonblocking architectural observation. No GR-05 work. Checkpoint: `775ae1bb4542c0495e31c66fb347aa1225e8e92a`, tag `v0.3-alpha-gr03-wave2-review-pass`. No remote or push.

Latest review archive: `package/GR03_Schema_Reconciliation_Review_2026-09-28.zip`; final integrity receipt: `tests/package-integrity.json`. Earlier OPEN schema statements below are historical and superseded by this correction.

---

# Current governed decision — 2026-09-28

**PASS_FOR_WAVE_2_SYSTEM_REVIEW**. This supersedes earlier FAIL/incomplete/native-pending decisions below. The user completed genuine Chrome 200%: Presence → Agenda → Voice → interpretation → Review Interpretation → feedback/Continue → Revise → Review again. Choices and complete feedback were readable; Continue was reachable/enabled after review, disabled with feedback closed after Revise, and reachable/enabled again after re-review. No document-level horizontal scrolling, clipping, destructive overlap, unreadable text or unreachable controls was reported.

Evidence provenance: explicit user manual pass in this chat. The user reports screenshots covering the native 200% indicator, choices, feedback, revision and final states. No new attachment or identifiable new local screenshot was available for independent agent inspection in this turn; no screenshot filename or independent visual verification is invented. `tests/gr03-native-zoom-validation.json` and `tests/gr03-relocation-native-zoom.json` preserve the prior blocked attempts as history and record this manual result.

Existing automated evidence remains 423/423 PASS (307 regular + 116 maximum-content), with 12 static commands passing. The browser JSON governed decisions are updated from that existing automated evidence plus the manual result; this is not a new automated browser run.

Refresh observation: current GR-03 learner selection/state does not persist after refresh, as reported by the user. This is outside the frozen GR-03 contract and does not block this pass. Available repository architecture specifies local persistence for GR-01 practice-focus only; no global/GR-03 restore contract was found. See `docs/GR03_REFRESH_PERSISTENCE_OBSERVATION.md`. No production code or frozen contract changed.

Candidate objects BLK-PERSPECTIVE-01, INT-LABELED-GRAPHIC-01 and CMP-PERSPECTIVE-01 remain PROTOTYPE / RETAIN CANDIDATE. This is not GOLDEN_REFERENCE_ACCEPTED. Template-schema reconciliation remains OPEN. Stop for ChatGPT architectural review before GR-05; no GR-05 work is authorized here.

Current package: `package/GR03_System_Review_2026-09-28.zip`; final integrity receipt: `tests/package-integrity.json`. Earlier archives are historical snapshots.

---

## Historical record (superseded where inconsistent with the current decision)

## Relocation follow-up — 2026-09-28

The authoritative D: repository retains its original Git history, baseline/tag and accepted fixes. No active old-path dependencies were found; historical path evidence remains unchanged. The full D: rerun passes all 12 static commands and all 423 Chrome assertions (307 regular + 116 maximum-content), with 32 new screenshots and no failures/errors. Current browser environment: 154.0.8037.58, Playwright 1.62.1. Selected 1024/768/320 stress screenshots were reviewed for layout; no destructive overlap or missing feedback/navigation was observed. No production source change was made.

**Final GR-03 status remains FAIL; genuine Chrome 200% is PENDING.** This session has no compatible native desktop-control tool and lacks the earlier @oai/sky runtime. No new native flow or native screenshot is claimed. This supersedes the previous session's blocker description for this attempt only. No candidate promotion, Golden Reference acceptance or GR-05 work occurred. Template-schema reconciliation remains OPEN.

Current evidence: `tests/gr03-relocation-audit.md`, `tests/gr03-relocation-static-command-log.json`, `tests/gr03-browser-validation-relocation.json`, `tests/gr03-relocation-native-zoom.json`, and `tests/gr03-screenshots/relocation-*.png`. Final package verification: `tests/package-integrity.json`; relocation review archive: `package/GR03_Relocation_Review_2026-09-28.zip`. Earlier runs and archives remain historical evidence.

---

# GR-03 validation report — architectural-review follow-up, 2026-09-28

Build `BUILD-GR-03-W2-0001`; system `0.3-alpha`; mode `CONSTRAINED_BUILD`.

**Final status: FAIL.** All 423 automated browser assertions and static regressions pass. Complete genuine Chrome 200% validation is still pending, so GR-03 cannot be designated PASS_FOR_WAVE_2_SYSTEM_REVIEW. No candidate is promoted or Golden Reference accepted. GR-05/06 were not started.

## What changed

The five accepted shared fixes are preserved: early image-error handling, reduced-motion feedback scrolling, introductory prompt removal after exploration starts, persistent Menu accessible name, and image-fallback overlap prevention.

The frozen content limits were restored to the validation matrix and machine-readable authoring contract: perspective label 8 words, observation 45, interpretation 45, limitation 35, answer option 28, feedback 65. These synchronize existing authority supplied in the architectural review; they are not new design decisions. The dedicated GR-03 validator now checks production content against these limits.

Maximum-length labels exposed a shared marker overlap at 1024 pixels. Shared labeled-graphic CSS/JS now detects unsafe marker/caption geometry and puts controls into normal document flow when needed. It re-evaluates after state, width and font changes. This sixth shared correction uses existing tokens and responsive rules. Approved production HTML is unchanged from the baseline; reference.css remains zero bytes. Synthetic text is injected only into test responses.

## Executed validation

| Check | Result |
| --- | --- |
| Existing automated interaction/responsive/accessibility/resilience suite | PASS: 307 assertions |
| Maximum-content stress suite | PASS: 116 assertions |
| Combined final browser run | PASS: 423 assertions, no failures/errors |
| Repository, Wave-1 smoke and dedicated GR-03 validation | PASS |
| GR-01 and GR-04 locked-build validation | PASS |
| JavaScript/CJS syntax | PASS: 7 files |
| Full native Chrome 200% flow | PENDING — tool blocked |

Chrome 153.0.8010.53 / Playwright 1.62.1 executed locally at 1920×1080, 1440×900, 1024×768, 768×1024, 390×844 and 320×568. Normal content exercises all A/B/C/D feedback routes, revision/re-review and completion at every size, plus desktop/mobile keyboard completion, focus/Menu/Escape, reduced motion, image failure and delayed images.

Stress tests inject all six exact maximum word counts, verify actual DOM counts, and execute exploration, answer D, review, revision, re-review and reachable Continue at every size. Assertions cover document overflow, text bounds/clipping, answer visibility, marker/caption overlap, mobile disclosure and control dimensions. Screenshots support visual review. The 44-pixel target minimum and half-viewport control-height ceiling are test heuristics, not newly frozen authoring limits. Ordinary synthetic words exercise word-count limits; this is not a guarantee for arbitrary unbroken tokens or every language.

There are 32 final automated screenshots (20 regular, 12 stress). Selected stress screenshots were visually inspected at 1024, 768 and 320 pixels: labels flow without destructive overlap, mobile disclosure stays coherent, and feedback/navigation remain present. Production HTML SHA-256 before/after test injection is identical. Static command records contain 12 successful command entries. No locked-reference regression was found.

## Native 200% evidence and remaining blocker

Earlier screenshots genuinely show Chrome's native 200% indicator and partial initial/Presence/Agenda exploration. They remain partial evidence and predate the latest layout correction. They do not validate the final full flow.

The fresh native attempt stopped before input because Computer Use could not determine Chrome's current URL confidently enough to enforce policy. Only native testing stopped; independent repository work continued. No CSS zoom, scaling or narrowed viewport is claimed as native zoom evidence.

Manual completion: open the local GR-03 page, set Chrome menu zoom to 200%, visit Presence → Agenda → Voice, select an interpretation and Review. Confirm readable full feedback and enabled Continue; choose Revise (feedback closes, Continue disables), then Review again (Continue enables). Check for clipping, overlap and horizontal scrolling throughout. Capture the 200% menu indicator, choices, feedback and final Continue. Localhost port 8765 returned HTTP 200 at handoff.

## Governance findings

The content-limit omission is resolved by authority synchronization. The template schema mismatch remains OPEN: GR-01/03/04 use objects, GR-02 a string, while both generic schemas specify strings. Existing validators do not validate Golden Reference spec.yaml against those schemas. The available local architectural evidence supports retaining template ID plus optional variant; the full standalone upstream Gate-7 source was unavailable, so no direct comparison with that missing source is claimed.

The proposed correction is documented separately: canonical structured template, transitional string support, one schema source and explicit YAML/schema/registry validation. No schema migration was implemented. Architectural reconciliation is required before GR-05.

## Package and resource disposition

The original package inventory contained stale hashes and already included validation evidence. No regeneration tool existed. A small reusable tool now refreshes and verifies the same PACKAGE_MANIFEST.json, preserving that evidence convention. The final integrity receipt is tests/package-integrity.json; it is authoritative for the post-stabilization verification result. The updated review ZIP supersedes the earlier ZIP. Package integrity does not confer product acceptance.

The existing resource-first asset decision is unchanged: the preferred VA-012 binary was unavailable and the governed fallback reused the course-specific HRBA voice-and-safety illustration as AST-HRBA-GR03-VOICE-SAFETY-EXISTING-01. No new artwork or global asset promotion occurred. BLK-PERSPECTIVE-01, INT-LABELED-GRAPHIC-01 and CMP-PERSPECTIVE-01 remain PROTOTYPE / RETAIN CANDIDATE.

## Current evidence

- tests/gr03-browser-validation.json — canonical final 423-check result, including stress assertions and native status.
- tests/gr03-native-zoom-validation.json — precise partial evidence and blocker.
- tests/gr03-static-command-log.json and tests/gr03-static-validation.json — static results and exact commands.
- tests/gr03-screenshots/final-*.png — current automated evidence; zoom200-*.png is older partial native evidence.
- tests/gr03-validation-session.md — current follow-up plus historical journal.
- prototype-specs/GR-03_VALIDATION_MATRIX_v0.1.md and GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json — restored authority.
- docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md — open architecture proposal.
- PACKAGE_MANIFEST.json, tests/package-integrity.json and docs/PACKAGING.md — integrity and process.
