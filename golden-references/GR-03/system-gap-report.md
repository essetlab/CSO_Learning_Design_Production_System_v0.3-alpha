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

# GR-03 System Gap / governance record — 2026-09-28

No new design-system gap or candidate promotion is declared.

- **Shared defect, corrected (B):** maximum-length perspective labels could overlap at desktop widths. Shared geometry-driven flow fallback fixes this; all six stress viewports and existing regressions pass. The five previously accepted fixes remain intact.
- **Authority synchronization, resolved:** the abbreviated repository matrix omitted already-frozen word limits. The matrix and authoring contract now restore 8/45/45/35/28/65 words exactly as supplied by architectural review. Historical notes calling these limits undefined are superseded.
- **Repository/schema governance, OPEN (C):** both generic schemas declare string templates; GR-01/03/04 use structured objects and GR-02 uses a string. Existing checks do not validate these YAML specs against the generic schemas. See docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md for available Gate-7-related evidence, its limits, and the proposed correction. No schema migration was implemented. Resolve before GR-05.
- **Environment validation blocker (D):** complete genuine Chrome 200% flow remains unverified. The latest native retry stopped before input at the Computer Use URL-policy check. Earlier native screenshots show only partial exploration and predate the final shared fix. This alone prevents the required GR-03 PASS designation despite automated passes.
- **Package integrity:** stale pre-fix hashes are addressed by the reusable tool against the existing manifest. See the final tests/package-integrity.json receipt; package consistency is separate from acceptance.

The prior resource-first fallback from unavailable VA-012 to the existing course-specific HRBA voice-and-safety illustration remains a recorded build deviation, not a System Gap. GR-05/06 have not started.
