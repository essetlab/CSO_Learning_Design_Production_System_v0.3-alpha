# GR-06 direct validation checklist

Status: **screen-reader and physical-mobile checks PENDING; native Chrome 200% user-attested PASS; H01–H09 semantic review PASS**. ChatGPT semantic review was explicitly reported by the user; native Chrome 200% PASS was explicitly attested by the user in the Track A request. Performer/device/date details were not supplied; none are invented. GR-03/GR-05 attestations do not transfer to this reference.

Serve the repository from its root with `python -m http.server 8776 --bind 127.0.0.1`, then open `http://127.0.0.1:8776/golden-references/GR-06/index.html`. Use fictional, non-identifying work. Automated headless Chrome evidence is recorded separately in `tests/GR06_BROWSER_RESULTS.json` and `tests/GR06_RECOVERY_RESULTS.json`.

## V18 — genuine Chrome 200%

Record date, OS and Chrome version; use Chrome's native zoom menu and capture the visible **200%** indicator. Do not substitute browser emulation, device scale or CSS zoom.

1. Begin with blank work. Author all five source notes and select their contribution types.
2. Write the primary interpretation and an alternative or unresolved interpretation. Link informing and limiting evidence for each; set confidence. Do not imply equal weight merely because there are two roles.
3. Choose any of the four routes and author all six decision fields, including responsibility/authorization boundaries. Link both interpretation roles. Preserve decision v1.
4. Confirm U01 appears only now and v1 is retained. Author its implication; link U01, meaningfully revise an interpretation and action/verification/account-back, and explain the adaptation. The route may stay the same.
5. Compare v1/current. Review all four criteria with specific reasons; leave at least one `needs_follow_up` with a next action. Acknowledge; inspect enabled/reachable Continue.
6. Revise; verify Continue immediately disables. Re-review and acknowledge; verify Continue enables again.
7. Inspect source text, long authoring, error feedback, comparison, criterion reasons/follow-ups, recovery choices and export. Record horizontal page scrolling, clipping, destructive overlap, unreadable text or unreachable controls. Capture critical authoring, U01, comparison, acknowledgment and revision states.

Result: **PASS — USER_ATTESTED**. Source: the user’s Track A request. Native Chrome 200% was reported PASS; Codex did not perform it. No additional date/device/screenshot details were supplied.

## V19 — actual screen reader and physical mobile keyboard

Record screen reader/version, OS/browser, date and performer. Walk the full five-stage flow using the reader and keyboard. Check landmarks/headings, stage prerequisites, labels, field limits, checkbox groups, differentiated interpretation roles, first-invalid-field focus and error association, U01 announcement/context, v1/current labels, review judgments/follow-up, acknowledgment, revision invalidation and Continue. Check restrained announcements, recovery receipts/version choices, and accessible export. Record actual observations and defects; an accessibility-tree snapshot alone is not a reader pass.

On a physical phone, record device/OS/browser. Open its software keyboard in source notes, interpretation, decision, adaptation and review. Test long pasted text, visible caret, focus/scroll behavior, errors, keyboard dismissal and reachability of review/Continue. Confirm there is no destructive overlap or document-level horizontal scroll. Desktop mobile emulation is separate evidence.

Screen-reader result: **PENDING**. Physical-mobile/software-keyboard result: **PENDING**.

## V21 — independent H01–H09 instructional/HRBA review

Review `GR-06_SEMANTIC_REVIEW_PACKET.md` and `tests/gr06-semantic-fixtures.json`. They contain four synthetic cases of learner work on the same frozen case, not learner-visible model answers or approved plans: retain with adaptation; change after U01; escalation with authority/interim actions; unresolved alternative without false symmetry. Review all five negative counterexamples as well.

Record PASS or DEFICIENCY and a brief basis for each dimension:

- H01: finding versus explanation.
- H02: grounded alternative/unresolved explanation without false symmetry.
- H03: no prevalence overclaim from six voluntary comments or attendance counts.
- H04: administrative closure versus explanation sent versus confirmed receipt.
- H05: proportionality and a feasible considered alternative.
- H06: public decision authority, Awra boundary, authorization/escalation and interim action.
- H07: feasible, minimal, safe verification with candid limits.
- H08: accessible account-back, receipt checking and unresolved-concern route.
- H09: meaningful interpretation and follow-up response to U01, including retaining a route.

Unresolved follow-up is allowed. Structural completion is not semantic approval; reject perfunctory or cosmetic reasoning without adding runtime language scoring. Identify reviewer, date, packet/fixture version or hash, scope and any required correction. All nine judgments are **PASS**, ChatGPT review explicitly reported by the user in the bounded-correction authorization. See `../../governance/WAVE_2_REVIEW_AUTHORITY_UPDATE.json` for provenance and reviewed fixture/packet hashes. The original checklist is preserved in `../../tests/wave2-corrections/baseline/golden-references/GR-06/MANUAL_VALIDATION.md`.

Only after required direct checks and independent review pass may a separately authorized evidence update consider `PASS_FOR_WAVE_2_SYSTEM_REVIEW`. No Golden Reference acceptance or candidate promotion is implied.
