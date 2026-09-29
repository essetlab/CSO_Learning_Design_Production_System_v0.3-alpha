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

# Current architectural-review follow-up — 2026-09-28

This section supersedes historical counts, missing-limit descriptions and initial native-blocker wording below. Final governed decision remains **FAIL**, solely because the complete final-code native 200% flow is unverified.

- Preserved the five accepted shared fixes, unchanged learner HTML, zero-byte reference.css and candidate status.
- Restored frozen limits 8/45/45/35/28/65 into matrix/contract; added production word-count checks.
- Test-only response injection exposed marker overlap: content-limit-first run had 1 failure; a width-only correction had 3 failures. Both failed JSON/screenshot runs are retained as historical debugging evidence. The final shared geometry-driven normal-flow fallback passed the safe-flow run and the final rerun.
- Final canonical browser result: **423/423 PASS**, comprising 307 prior checks plus 116 stress checks at all six sizes. Final screenshots: 32 (20 regular + 12 stress). Selected 1024/768/320 stress images visually reviewed. The synthetic copy never changes production HTML; before/after SHA-256 matches.
- Full static rerun: repository, Wave-1 smoke, dedicated GR-03, locked GR-01/04 and seven JS/CJS syntax files: all 12 commands exit 0. Exact commands/results are in gr03-static-command-log.json.
- Browser runner now uses port 8766 by default (GR03_PORT override); port 8765 was already serving the user page. The initial EADDRINUSE attempt was infrastructure-only. Final command: bundled node tests/run_gr03_browser_validation.cjs with bundled NODE_PATH. No GR03_RUN override for canonical final evidence.
- Native retry used Computer Use @oai/sky, listed windows and attempted the returned regular Chrome window. get_window_state stopped at URL-policy verification before input. No alternate native route was attempted afterward. Prior native 200% images remain partial and predate the new shared fix. See gr03-native-zoom-validation.json. Local user page returned HTTP 200 on port 8765 at handoff.
- Schema investigation remains OPEN, proposal only. Both generic schemas and GR-01/02/03/04 were compared with available local architectural records; standalone full Gate-7 authority is absent. No schema or spec migration.
- Manifest-before-refresh failure evidence retained in package-integrity-before-refresh.json. No prior regeneration tool existed. tools/package_repository.py preserves the existing manifest/evidence convention. Run after all files stabilize: bundled python tools/package_repository.py --refresh --archive GR03_Gate8_Validation_Review_2026-09-28_updated.zip. Final receipt: package-integrity.json; archive verification checks membership, CRC and payload hashes. docs/PACKAGING.md records exclusions/self-reference handling.

Manual handoff: Chrome menu → 200%; Presence → Agenda → Voice → answer → Review → Revise → Review. Confirm feedback closes/Continue disables on revision and Continue enables again after review. Capture native zoom indicator, complete choices, readable feedback and final navigation; inspect for clipping/overlap/horizontal scrolling throughout.

No candidate promotion or GR-05/06 work. The updated validation-report.md is the current consolidated report.

---

# Historical session record (superseded where noted above)

# GR-03 browser validation session — 2026-09-28

Final governed decision: **FAIL**. The automated checks pass, but actual 200% browser zoom remains pending. This is not Golden Reference acceptance.

## Authority and baseline

Authority: `C:\Users\kidis\L-HUB\CSO_Learning_Design_Production_System_v0.3-alpha`.
No separate GR-03 repository was used. No AGENTS.md was found in this workspace.

Git was absent at the start. All existing files were committed before changing production content. Because no previous history existed, earlier changes relative to the original ZIP cannot be determined; no files were modified by this session before the baseline commit.

- Baseline: `1a263232c000495a567e56208a51f98b40826f64`
- Message: `baseline: CSO Learning Design & Production System v0.3-alpha`
- Baseline branch: `main`
- Tag: `v0.3-alpha-gr03-static-pass`
- Working branch: `gate8/wave2/gr03-browser-validation`
- Identity: repository-local `CSO Learning Design System <local-repository@invalid>`; no global identity was present. Replace before any public publishing if desired.
- No remote created; nothing pushed or uploaded.

Initial Git writes were denied by sandbox .git permissions. Approved elevated execution then encountered ownership validation because the sandbox created .git. A command-scoped `-c safe.directory=C:/Users/kidis/L-HUB/CSO_Learning_Design_Production_System_v0.3-alpha` exception was used for this exact folder; global Git settings were not changed.

## Resources inspected

- `golden-references/GR-03/index.html`, `reference.css`, `spec.yaml`, build manifest, validation/result/gap reports.
- `prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json` and `GR-03_VALIDATION_MATRIX_v0.1.md`.
- Shared `interactions/labeled-graphic/`, `compositions/perspective/`, `learning-blocks/perspective/`, `shell/`, `tokens/`, `foundations/`, UI dependencies, registries and schemas.
- Existing Python repository, locked-build, static-smoke, GR-03 and browser runners.

## Exact executable environment and commands

PowerShell on Windows_NT 10.0.26100 x64. Chrome 153.0.8010.53. Browser automation: bundled Node Playwright 1.62.1. Python 3.12 from the bundled runtime.

```powershell
$py='C:\Users\kidis\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$env:PYTHONPATH='C:\Users\kidis\AppData\Local\Temp\cso-gr03-static-deps'
$env:PYTHONDONTWRITEBYTECODE='1'
& $py -X utf8 validators/validate_repository.py
& $py -X utf8 tests/run_static_smoke.py
& $py -X utf8 validators/validate_gr03.py
& $py -X utf8 tools/validate_locked_build.py locked-build-specs/GR-01_LOCKED_BUILD_v0.1.json golden-references/GR-01/index.html
& $py -X utf8 tools/validate_locked_build.py locked-build-specs/GR-04_LOCKED_BUILD_v0.1.json golden-references/GR-04/index.html
rg --files -g '*.js' -g '*.cjs' | ForEach-Object { node --check $_; Write-Output "JS_CHECK $_ exit=$LASTEXITCODE" }

$env:NODE_PATH='C:\Users\kidis\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules'
$env:GR03_RUN='before-fixes'
node tests/run_gr03_browser_validation.cjs
# In fresh subsequent command processes GR03_RUN was unset:
node tests/run_gr03_browser_validation.cjs
```

The CJS companion runs a temporary HTTP server bound only to 127.0.0.1:8765, serving the full repository. Actual URL: `http://127.0.0.1:8765/golden-references/GR-03/index.html`. It shuts that server down after validation. The existing Python browser runner hardcodes `/usr/bin/chromium` and has weaker coverage; it was retained as historical source, not reported as executed successfully on Windows.

Static exact results (before browser work and after JS fixes): repository `status=pass`, checked GR-01/GR-04, errors=[]; Wave-1 smoke `status=pass`, errors=[]; GR-03 `status=pass`, one H1, three controls, three panels, four options, empty local CSS, shell placeholder=true, errors=[]. Every JavaScript syntax check exited 0. Both locked renders exactly match:

- GR-01 candidate/expected SHA256: `27fc55b9471e09d2c9f245b9cb0116592e2340668056ddbdf181b0548d096da2`.
- GR-04 candidate/expected SHA256: `dd6df39daa7ae59089b868b1866c208f8c2923c6e3c62f0c3ce11eba20f8f193`.

Initial static attempts stopped at `ModuleNotFoundError: No module named 'bs4'`. The restricted installer returned `WinError 10013` for PyPI. Approved installation command:

```powershell
& $py -m pip install --target 'C:\Users\kidis\AppData\Local\Temp\cso-gr03-static-deps' beautifulsoup4 PyYAML
```

Installed beautifulsoup4 4.15.0, PyYAML 6.0.3, soupsieve 2.10 and typing-extensions 4.16.0. Sandbox reads of that temporary directory were denied (`ImportError ... unknown location`); approved execution with access to it passed. One approval review timed out and the permitted retry succeeded. An earlier optional Python Playwright download into `cso-gr03-python-deps` was interrupted and canceled; it was not used. Bundled Node Playwright supplied all browser tests. These are environment setup issues, not unexplained static regressions.

## Executed browser coverage

See `gr03-browser-validation.json` for each assertion and exact details. All 307 automated assertions pass (`automated_pass=true`); overall `pass=false` and governed `status=FAIL` while zoom is pending. Final static outputs and exact executable arguments are preserved in `gr03-static-command-log.json` (all exit codes 0).

- 1920×1080, 1440×900, 1024×768, 768×1024, 390×844 and 320×568: initial state, all lenses, visited text, selected expanded panel, reopening, interpretation unlock only after three lenses, no answer preselection, review gating, all A/B/C/D option-specific title/body comparisons, feedback, completion, revision and re-review.
- Each viewport: document width equals viewport width; visible text horizontal bounds; controls scrolled into view and checked with hit testing. Intended hidden drawer and screen-reader-only text excluded from visible clipping checks.
- Mobile DOM: each panel is directly after its corresponding control; order is orientation, scene, Presence, Agenda, Voice, interpretation, feedback, takeaway, navigation. Desktop retains shared scene/detail rail.
- Keyboard at 1440×900 and 390×844: Tab-only navigation between controls, Enter and Space activation, native radio Space/ArrowDown, review, revision, re-review, Continue focus; visible focus recorded for each tab stop; Menu opens by Enter, Escape closes and returns focus. No mouse or programmatic focus shortcut was used in these keyboard flows.
- Reduced motion: actual media emulation, full flow and revision, computed 0.01ms animation/transition, auto scrolling and no explicit smooth-scroll call after correction.
- Image request aborted at desktop/mobile: fallback visible, failed image hidden, text/control non-overlap, full learning/revision flow still works. Asset was never deleted.
- Delayed image at 390×844: completion before request release; caption document position before/after loading differs by less than 2px.
- Feedback meaning reviewed against embedded approved content: observation, evidence and uncertainty are distinguished, and no option requires choosing B to complete.

Completion here means the governed enabled-Continue state. The reference shell does not implement next-episode navigation; no new course navigation was invented.

## Defect classification and fixes

All production fixes are **B — shared-system defect**, located in the shared files:

1. Image error could precede listener registration. Check already-complete images with zero natural width as well as handling future error events.
2. Explicit smooth feedback scrolling ignored reduced-motion preference. Choose auto when reduced motion is requested.
3. Empty instructional prompt remained after selecting a perspective. Hide the empty prompt on selection.
4. Mobile CSS hid Menu's only accessible text. Add the stable `aria-label="Menu"` to the existing shared button.
5. After the image fallback began working, visual review revealed a spatial marker overlapping fallback text. Put fallback text, caption and controls into distinct normal-flow regions using existing tokens; retain mobile disclosure behavior.

The first automated run also incorrectly flagged the intentionally inert closed drawer and screen-reader-only live region as visible clipping. These were **validation-harness defects**, corrected in the test, not by changing product styling. Before-fix results retain the raw failures for transparency. Screenshot captures fast-forward finite animations through Playwright's `animations: 'disabled'` option to capture settled states; no production styling was changed for screenshots. Motion behavior itself is tested separately.

No learner content, completion expression, shared IDs, tokens, type system or breakpoints were changed. `GR-03/reference.css` remains empty. Candidate objects remain PROTOTYPE / RETAIN CANDIDATE.

## Pending/blockers and specification observations

**D — Actual 200% browser zoom: PENDING.** Headed Chrome successfully opened the actual localhost page using Playwright, viewport:null (observed innerWidth=1427, innerHeight=788, devicePixelRatio=1.25 at the initial OS scale). No genuine 200% zoom was performed. A native Computer Use route initialized and located the GR-03 Chrome window, but its next observation returned:

> Computer Use has been stopped for this turn because it could not determine the current browser URL on Windows with enough confidence to enforce policy. Stop your work and send a final message noting why Computer Use ended.

Native Computer Use stopped immediately. No keyboard input, alternate native input route or security bypass followed. Post-blocker work was limited to preserving evidence, reviewing saved screenshots, finishing non-native automated checks and reporting. Chrome localhost itself is available; this is not the old `ERR_BLOCKED_BY_ADMINISTRATOR` navigation failure. Edge is installed but was not required as an alternative to working Chromium, and no claim of cross-browser testing is made.

Smallest manual action: in the already-open GR-03 Chrome page, use Chrome's three-dot menu to set Zoom to **200%**. Explore all lenses, select an answer, review, revise and review again. Check readable full text, reachable controls/Continue, no horizontal page scroll, clipping or overlap, and understandable selected/visited states. Save a screenshot showing Chrome's 200% indicator plus page screenshots of feedback and navigation. Return those results for evidence review. Refreshing after the temporary test server stops requires Codex to restart localhost; the user need not run commands.

For this handoff, Codex restarted a local-only server with `& $py -m http.server 8765 --bind 127.0.0.1` so the existing browser page can be refreshed while this session remains available. No native UI interaction was resumed.

**C — Schema-limit overflow ambiguity:** the frozen GR-03 contract contains no maximum text lengths; the perspective manifest bounds item count 2–4 while this instance requires exactly three. No invented prose maximum or fourth learner perspective was added. Maximum-length content stress testing is pending governed limits. Also `schemas/golden-reference.schema.json` declares template as a string while this GR spec uses an object; the existing static validator does not check that schema. This pre-existing authority mismatch is recorded for architectural review, not silently rewritten or labeled a newly failed static test.

No genuine System Gap requiring a new component was identified. These observations do not authorize candidate approval, Golden Reference acceptance, GR-05 or GR-06.

## Review handoff

Use the full repository review ZIP in `package/GR03_Browser_Validation_Review_2026-09-28.zip`. It includes shared fixes, authoring/specification sources and `tests/` evidence, excludes .git, and is not a standalone GR-03 production repository. Review this journal, `golden-references/GR-03/validation-report.md`, the browser JSON, before-fix JSON and `tests/gr03-screenshots/` together. Real 200% evidence is still required before reconsidering the decision.
