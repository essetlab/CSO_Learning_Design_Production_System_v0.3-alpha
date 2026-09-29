# GR-03 Validation Matrix v0.1

Status: **FROZEN FOR PROTOTYPE BUILD**

Required checks: architecture/governance; interpretation-not-recall; three meaningful perspectives; evidence-versus-assumption; bounded inference; feedback-gated completion; all option-specific feedback paths; revision reset/re-review; desktop 1920/1440/1024; tablet 768; mobile 390/320; keyboard; Escape/focus-return shell; actual 200% zoom; reduced motion; image failure; delayed image; no horizontal scroll; schema-limit overflow; system-drift checks.

Critical learning failures: interpretation degenerates to recall; evidence and assumption are not distinguished; silence is over-interpreted; takeaway does not transfer beyond the case.

Immediate target status: **PASS_FOR_WAVE_2_SYSTEM_REVIEW**, not final Golden Reference acceptance.

## Frozen maximum-content requirements (authority synchronization)

Restored on 2026-09-28 from the already-frozen full matrix as supplied in the user's architectural review instruction. The abbreviated repository copy omitted these values; this is an authority synchronization correction, not a new design decision.

| Field | Maximum words |
| --- | ---: |
| Perspective label | 8 |
| Observation | 45 |
| Interpretation | 45 |
| Limitation | 35 |
| Answer option | 28 |
| Feedback | 65 |

At these limits desktop must remain coherent and mobile readable, with no clipped text, document-level horizontal scrolling, destructive overlap, or unusably tall/narrow controls. The layout must not depend on the exact Jiru Amba copy length. Test at 1440×900, 768×1024, 390×844 and 320×568 at minimum, preferably all six standard viewports. Use test-only substitutions; do not rewrite production learner content. Machine-readable values are in the GR-03 authoring/content/state contract under `content_limits.maximum_words`.
