# GR-06 governed result

**IMPLEMENTED_PENDING_MANUAL_VALIDATION**. Automated implementation is complete. Direct technical checks and independent semantic review remain pending. No Golden Reference acceptance or candidate promotion.

## Delivered build

The frozen five-stage flow is implemented through shared owners: Evidence → Interpretation → Decision v1 → Adaptation after U01 → Compare and review. The exact frozen evidence and U01 are embedded. All four decision routes remain structurally valid; none is automatically correct. Immutable v1, differentiated interpretation roles, hard maxima/T, revision invalidation and E && I && D && U && A && R && F are enforced.

The three new objects are registered PROTOTYPE only. The composition/template variants are opt-in. GR04 default selectors, markup, CSS and locked output remain unchanged. GR05 default template DOM and settled screenshot bytes match the checkpoint. SVC-LEARNING-STATE-01 is unchanged; automatic session recovery and opt-in device persistence use that service.

## Automated results

- model: **PASS**, 72 named checks/commands; `tests/GR06_MODEL_RESULTS.json`.

- state_integration: **PASS**, 16 named checks/commands; `tests/GR06_STATE_RESULTS.json`.

- browser: **PASS**, 336 named checks/commands; `tests/GR06_BROWSER_RESULTS.json`.

- recovery: **PASS**, 65 named checks/commands; `tests/GR06_RECOVERY_RESULTS.json`.

- static: **PASS**, 25 named checks/commands; `tests/GR06_STATIC_RESULTS.json`.

- commands: **PASS**, 41 named checks/commands; `tests/GR06_REGRESSION_COMMANDS.json`.

- GR03_browser: **PASS**, 423 named checks/commands; `tests/gr03-browser-validation-gr06-regression.json`.

- GR05_browser: **PASS**, 321 named checks/commands; `tests/gr05-browser-gr06-regression.json`.

- GR05_keyboard_resilience: **PASS**, 84 named checks/commands; `tests/GR05_KEYBOARD_RESILIENCE_RESULTS.json`.

- GR05_model: **PASS**, 31 named checks/commands; `tests/GR05_MODEL_RESULTS.json`.

- shared_state_service: **PASS**, 17 named checks/commands; `tests/GR05_STATE_SERVICE_RESULTS.json`.



The GR03 runner’s generic overall FAIL flag concerns absent manual evidence in that runner; automated_pass is true with 423 checks and no errors. Existing governed GR03 and GR05 review passes remain untouched. GR05’s historical semantic-fixture preservation baseline belongs to its earlier evidence-only task; the newly authorized template extension is checked by default-body preservation, exact DOM/PNG comparison and full regressions, without rewriting that historical baseline.

All seven frozen viewport sizes were exercised, plus all-maxima/long-token stress at 320px and 1440px. Browser tests include keyboard-only completion, refresh recovery, explicit opt-in followed by actual Chrome profile closure/restart, corruption and two-tab conflicts, denied storage/clipboard, offline input, IME/multilingual/plain HTML input, reduced motion, font fallback, and honest no-JavaScript text fallback. Source hashes and screenshots are in the build manifest.

## Manual and semantic work still required

- V18 genuine Chrome 200%: PENDING.
- V19 actual screen reader and physical-mobile software keyboard: PENDING.
- V21 independent H01–H09 instructional/HRBA judgment: PENDING. V09 quality review depends on this judgment.

Use `MANUAL_VALIDATION.md` for the exact checklist. `GR-06_SEMANTIC_REVIEW_PACKET.md` contains four substantive synthetic examples (retain, change, escalate, unresolved alternative) and the five frozen negative counterexamples. The fixture is separate from learner/runtime inputs, is not a model answer, and has no semantic pass.

## Governance, integrity and Git

Freeze checkpoint: `4c2ce06` — `gate8: freeze GR-06 evidence-to-decision specification`, on `gate8/wave2/gr06-evidence-to-decision`. Implementation/evidence changes remain uncommitted for architectural review. No remote was configured or pushed. No subsequent Golden Reference was started.

Harness defects and their corrections are recorded by test ownership in `tests/gr06-validation-session.md`; no shared production regression or G06-03 compatibility gap was observed. Package inventory/hash verification is in `tests/package-integrity.json`; the GR06 review ZIP is verified separately by the packaging command.
