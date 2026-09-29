# W2-C03 — GR05 bounded UTF-8 correction

**PASS, later bounded polish correction.** The earlier GR05 Wave-2 pass contained visible corrupted punctuation. Its original reports, screenshots and review outcomes remain historical evidence; this correction does not claim that the earlier build was defect-free.

Only `tools/build_gr05.py` and the shared view `interactions/build-repair/build-repair.js` were repaired. The generator regenerated `golden-references/GR-05/index.html` and `exercise.txt`. The exact substitutions were `Â·` → `·`, `â€“` → `–` and `â€”` → `—`: four occurrences in the generator and six in the shared view. Generated output contains three replacements in HTML and one in the text fallback. The source proof records original/current SHA-256 and verifies that applying only these substitutions to the preserved originals produces the new files exactly (line endings normalized for text comparison).

No frozen HRBA case/content contract, authored field, criterion, completion predicate, model, shared state service, CSS, token, breakpoint, candidate interface or review outcome changed. GR05 remains `PASS_FOR_WAVE_2_SYSTEM_REVIEW`; its six candidates remain PROTOTYPE. The current build manifest updates only affected source hashes and links its preserved historical version.

## Text, accessible names and visual evidence

`GR05_ENCODING_BROWSER.json`: 30 automated checks PASS at 1440px and 390px. Checks cover the document title, visible `25–35` duration, punctuation, field-label relationships, accessibility-tree text, retained-v1 label and absence of document horizontal scrolling across diagnosis, first review, C01 and comparison. Exact frozen content remains embedded. These are automated browser/tree checks, not a new actual screen-reader or native-zoom attestation.

Codex inspected the generated desktop/mobile screenshots. Corrected middle dots and range punctuation are readable; the inspected regions show no new overlap, clipped text or damaged control labels. Scroll-position crops are viewport captures, not missing document content. Complete-flow and maximum-content layout/reachability checks are in the full browser suite.

- `encoding-1440-diagnosis.png` and `encoding-390-diagnosis.png`: visible duration and case punctuation.
- `encoding-1440-first-review.png` and `encoding-390-first-review.png`: preserved-v1 label.
- `encoding-1440-challenge.png` and `encoding-390-challenge.png`: C01 label and exact challenge text.
- `encoding-1440-comparison.png` and `encoding-390-comparison.png`: comparison labels; corresponding `*-accessibility.txt` files retain accessible text.

## Complete GR05 regression

- Static ownership/content/token checks: 22 PASS.
- Model: 31 PASS; unchanged shared state service: 17 PASS.
- Browser/responsive/maximum-content: 321 PASS, seven frozen viewport sizes plus maximum-content/long-token stress and recovery/input/export checks.
- Keyboard/resilience/profile restart/two-tab conflict: 84 PASS.
- Existing automated and V25 semantic fixtures remain byte-for-byte preserved. Prior user-attested V21/V23/V22-mobile and ChatGPT V05/V25 passes remain their original provenance; none is represented as newly performed by Codex.

The first focused keyboard run timed out waiting for a field after 69 successful assertions. It is retained in `GR05_KEYBOARD_RESILIENCE_ATTEMPT_1.json`; the unchanged suite passed all 84 checks on rerun. No production assertion failure was observed and no production workaround was made. GR06's analogous initial recovery timeout and successful 65-check rerun are retained separately. The precise timeout cause was not established; concurrent execution/load is only a possible explanation.

Package verification is recorded in `tests/package-integrity.json` and performed again for the final review ZIP.
