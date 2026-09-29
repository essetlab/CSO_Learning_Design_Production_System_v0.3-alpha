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

# GR-03 result summary — 2026-09-28

**FAIL: complete genuine Chrome 200% validation remains pending.**

GR-03 remains implemented within the full shared production repository in CONSTRAINED_BUILD mode. The five accepted shared fixes are preserved. The frozen 8/45/45/35/28/65-word limits are synchronized into the matrix and contract. A further shared layout correction prevents maximum-length perspective labels from overlapping; approved learner HTML is unchanged and reference.css is empty.

All 423 automated browser assertions pass: 307 existing checks and 116 maximum-content checks across all six viewport sizes. Static repository, Wave-1, dedicated GR-03, locked GR-01/04 and seven JavaScript syntax checks pass. No locked-reference regression was found.

Earlier native Chrome 200% screenshots prove only partial exploration. The fresh retry was blocked before input by Computer Use's URL safety check. The full final-code flow through feedback, revision/re-review and Continue remains unverified.

The content-limit omission is resolved. The shared template schema/validator inconsistency remains OPEN; docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md contains the recommendation for approval before GR-05. No schema migration was made.

Package hashes are regenerated after evidence stabilizes using tools/package_repository.py; tests/package-integrity.json records the final verification. The updated review ZIP supersedes the stale earlier ZIP without implying GR-03 acceptance.

The existing course-specific fallback illustration is retained. Candidate objects remain PROTOTYPE / RETAIN CANDIDATE. No promotion, Golden Reference acceptance, GR-05 or GR-06 work occurred. See validation-report.md for the complete updated report and evidence list.
