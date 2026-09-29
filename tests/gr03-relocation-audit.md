# Current governed decision — 2026-09-28

**PASS_FOR_WAVE_2_SYSTEM_REVIEW**. This supersedes earlier FAIL/incomplete/native-pending decisions below. The user completed genuine Chrome 200%: Presence → Agenda → Voice → interpretation → Review Interpretation → feedback/Continue → Revise → Review again. Choices and complete feedback were readable; Continue was reachable/enabled after review, disabled with feedback closed after Revise, and reachable/enabled again after re-review. No document-level horizontal scrolling, clipping, destructive overlap, unreadable text or unreachable controls was reported.

Evidence provenance: explicit user manual pass in this chat. The user reports screenshots covering the native 200% indicator, choices, feedback, revision and final states. No new attachment or identifiable new local screenshot was available for independent agent inspection in this turn; no screenshot filename or independent visual verification is invented. `tests/gr03-native-zoom-validation.json` and `tests/gr03-relocation-native-zoom.json` preserve the prior blocked attempts as history and record this manual result.

Existing automated evidence remains 423/423 PASS (307 regular + 116 maximum-content), with 12 static commands passing. The browser JSON governed decisions are updated from that existing automated evidence plus the manual result; this is not a new automated browser run.

Refresh observation: current GR-03 learner selection/state does not persist after refresh, as reported by the user. This is outside the frozen GR-03 contract and does not block this pass. Available repository architecture specifies local persistence for GR-01 practice-focus only; no global/GR-03 restore contract was found. See `docs/GR03_REFRESH_PERSISTENCE_OBSERVATION.md`. No production code or frozen contract changed.

Candidate objects BLK-PERSPECTIVE-01, INT-LABELED-GRAPHIC-01 and CMP-PERSPECTIVE-01 remain PROTOTYPE / RETAIN CANDIDATE. This is not GOLDEN_REFERENCE_ACCEPTED. Template-schema reconciliation remains OPEN. Stop for ChatGPT architectural review before GR-05; no GR-05 work is authorized here.

Current package: `package/GR03_System_Review_2026-09-28.zip`; final integrity receipt: `tests/package-integrity.json`. Earlier archives are historical snapshots.

---

## Historical record (superseded where inconsistent with the current decision)

# Gate 8 / Wave 2 relocation audit â€” 2026-09-28

Authoritative repository: `D:\CSO_Learning_Design_Production_System_v0.3-alpha`.

## Git and preservation

- `.git` exists; no initialization, checkout, reset, commit, pruning or remote change performed.
- Branch: `gate8/wave2/gr03-browser-validation`.
- HEAD, baseline and tag `v0.3-alpha-gr03-static-pass` resolve to `1a263232c000495a567e56208a51f98b40826f64`.
- All-ref history contains the original single baseline commit. Reflog retains initial commit and checkout from main to the current branch. No remotes configured.
- `git fsck --full` exits 0: no corruption; dangling blobs reported and preserved.
- Arrival status contains 13 modified tracked files plus existing untracked reports, browser harnesses, screenshots, packaging tool and archives. These changes were retained, including accepted shared GR-03 fixes. No production source changes were needed for relocation.
- Before adding relocation evidence, `python tools/package_repository.py` passed all 282 entries with no errors. Manifest SHA-256: `9aba0bb770d20a01d04408597d238884a9dfe6a540bf944489828662c8388675`. This establishes that inventoried payloads, including accepted fixes, match the relocated inventory.

## Path audit

Case-insensitive recursive hidden-file search for `kidis|L-HUB` found old machine paths only in `tests/gr03-validation-session.md` and `tests/gr03-static-command-log.json`. They describe historical authority, commands and environment; retained unchanged. Git configuration contains no old path. Active repository/test/package code resolves its root dynamically or uses repository-relative paths. No executable/configuration dependency on the old repository path was found; no path replacement made.

## Environment and regression evidence

System Python: `C:\Python314\python.exe`; system Node: `C:\Program Files\nodejs\node.exe`. Beautiful Soup was missing and was installed into the current user's Python environment; PyYAML was already available. No dependency was installed into the repository.

Playwright resolves through `NODE_PATH` set with `Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'`. Browser invocation: `GR03_RUN=relocation node tests/run_gr03_browser_validation.cjs`, from the authoritative repository. The run label preserves earlier JSON and screenshots. This existing runner includes the complete automated suite and maximum-content stress suite.

Static commands and outputs: `tests/gr03-relocation-static-command-log.json`. All 12 commands pass: repository, Wave-1 static smoke, dedicated GR-03, GR-01/04 locked renders and seven JS/CJS syntax checks. Locked hashes remain `27fc55b9471e09d2c9f245b9cb0116592e2340668056ddbdf181b0548d096da2` (GR-01) and `dd6df39daa7ae59089b868b1866c208f8c2923c6e3c62f0c3ce11eba20f8f193` (GR-04).

## Genuine Chrome 200% limitation

No compatible native desktop-control tool is exposed in this session, and the previously used `@oai/sky` package is absent from the current bundled runtime. The computer-use skill requires explaining this limitation and providing manual steps. No current native 200% flow was executed and no new native screenshot is claimed. Earlier partial zoom evidence is preserved and does not establish a pass for final code. This is a current capability limitation, distinct from the earlier session's URL-policy rejection.

To complete on final code: serve this repository locally (`python -m http.server 8765 --bind 127.0.0.1`), open `http://127.0.0.1:8765/golden-references/GR-03/index.html` in Chrome, and use Chrome's menu to set 200%. Capture the menu indicator. Follow Presence â†’ Agenda â†’ Voice â†’ interpretation â†’ Review Interpretation. Inspect every line of feedback and scroll to enabled, reachable Continue. Select Revise; verify feedback closes and Continue disables. Review again; verify Continue enables and is reachable. Throughout, inspect horizontal scrolling, clipping, overlap, readability and control reachability; capture choices, complete feedback, revision state and re-review/Continue evidence. Do not substitute CSS zoom or a smaller viewport.

GR-03 remains **FAIL**, with native 200% **PENDING**. Promotion to `PASS_FOR_WAVE_2_SYSTEM_REVIEW` is conditional on completing that verification. No Golden Reference acceptance, candidate promotion or GR-05 work.

## Architectural handoff

`schemas/golden-reference.schema.json` and `schemas/episode.schema.json` specify `template` as a string. GR-01/03/04 use objects; GR-02 uses a string. Existing validators do not schema-validate Golden Reference YAML, so their passing results do not resolve this mismatch. `docs/GR03_SCHEMA_RECONCILIATION_PROPOSAL.md` remains OPEN and unchanged. Architectural decision is required before GR-05; no schema migration performed.

## Completed automated run

All 423 assertions PASS (307 regular + 116 stress), no failures/errors, 32 new screenshots. Browser: 154.0.8037.58; Playwright 1.62.1. Current evidence: `tests/gr03-browser-validation-relocation.json`. Selected 1024/768/320 feedback stress screenshots visually inspected; no destructive overlap or missing feedback/navigation observed. GR-03 HTML remains identical to baseline and reference.css is zero bytes. Final package inventory is refreshed after these evidence updates; see `tests/package-integrity.json` and the verified `package/GR03_Relocation_Review_2026-09-28.zip`.
