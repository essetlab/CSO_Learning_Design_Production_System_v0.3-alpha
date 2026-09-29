> Current governed result — 2026-09-29: **PASS_FOR_WAVE_2_SYSTEM_REVIEW**. V05 and V25 passed ChatGPT architectural/HRBA review, explicitly communicated by the user. V21, V23 and physical-mobile V22 passed by user attestation; Codex did not independently perform those checks. Automated evidence remains separate. No manual requirements remain open. Q03/Q04 needs_follow_up are valid unresolved actions in the synthetic artifact, not validation failures. All six candidates remain PROTOTYPE; no Golden Reference acceptance. Earlier pending statements below are retained chronological history and superseded by this notice. GR-06 is authorized for preflight/specification only after the GR-05 checkpoint.

# GR-05 manual-validation evidence and remaining review

Current technical manual results: **V21 PASS (user-attested), V23 PASS (user-attested), physical-mobile software-keyboard portion of V22 PASS (user-attested)**. The user explicitly reported completing these checks in the chat requesting the V25 packet. Codex did not independently perform or verify them. Provenance, exact scope and unspecified environment details are recorded in `tests/GR05_USER_ATTESTED_MANUAL_EVIDENCE.json`. Existing automated reports remain unchanged and separate.

Overall status: **IMPLEMENTED_PENDING_MANUAL_VALIDATION** until ChatGPT returns the V25 judgment. The user has now explicitly reported **V05 = PASS** and approval of the architecture and substantive artifact. **V25 alone remains pending** for the criterion-review responses. Review `GR-05_V25_SEMANTIC_REVIEW_PACKET.md`, a separate synthetic semantic-review fixture with criterion-specific responses. The original example and `GR-05_V25_REVIEW_PACKET.md` remain unchanged historical evidence. The architectural decision is recorded in `tests/GR05_ARCHITECTURAL_REVIEW_DECISION.json`.

The technical instructions below are the retained checklist for the user-attested checks, not a request to repeat them or a Codex execution claim.

Preview from the repository: `python -m http.server 8776 --bind 127.0.0.1`, then open `http://127.0.0.1:8776/golden-references/GR-05/index.html` in Chrome. A local server is needed for JavaScript modules. The page starts blank. Use fictional information only. `tests/gr05-example-work.json` supplies a reviewable test example, not an answer embedded in the product.

## V21 — genuine Chrome 200%

Use Chrome's own menu to set **200%** and capture the indicator. At that setting complete evidence-linked diagnosis → write all four repair sections → review and preserve v1 → record all four criterion judgments/reasons (and required follow-ups) → release C01 → revise participation plus accountability or evidence → explain the connected revision → compare v1/current → final criterion review → acknowledge. Verify Continue enables and is reachable. Revise, verify Continue disables, then review/acknowledge again and verify it enables. Refresh once during authoring and verify recovery.

Capture drafting, full comparison/review, acknowledgment, revise and re-review states. At each stage explicitly report document horizontal scrolling, clipping, destructive overlap, readable full text, reachable controls and focus visibility. Include Chrome version, screen resolution/OS scale and native zoom evidence. A narrow viewport, device scale or CSS zoom is not a substitute.

## V23 — screen reader; V22 physical mobile keyboard

Record reader/browser/version and actual observations. Walk headings, evidence groups, required fields/bounds, stage availability, first-invalid-field focus and error links. Inspect changed/unchanged and v1/current labels. Check automatic recovery, device-save choice/receipts, stale-review feedback and final acknowledgment. Verify announcements do not repeat on every keystroke and instructions make sense in reading order. Check clipboard fallback and reset cancellation. On a physical mobile device, confirm the software keyboard does not obscure active text or trap scrolling; automated 844×390 coverage only approximates constrained space.

## V25 — remaining semantic review (V05 already PASS)

Review the original, evidence, authored example and retained versions. Confirm rights-holder specificity, realistic pre-decision influence, feasible access changes, public-authority responsibility boundaries, safe evidence and a meaningful response to C01. Review both criterion rounds and unresolved follow-ups. A concise draft must still show reasoning and connected improvement; passing T is not proof of quality. Confirm that the experience is deep authored repair rather than selection/reveal completion. Record reviewer, date, verdict, qualifications/role where relevant and any defects by shared-system/content/evidence class.

Only after all required evidence passes should the governed result be reconsidered for `PASS_FOR_WAVE_2_SYSTEM_REVIEW`. This does not authorize Golden Reference acceptance, candidate promotion or GR-06.
