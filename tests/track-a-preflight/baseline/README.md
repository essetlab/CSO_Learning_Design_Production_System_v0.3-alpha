# CSO Learning Design & Production System v0.3-alpha

**Status:** Wave 1 repository alpha — baseline-reconciled for independent duplicate testing.

This version corrects the system/baseline mismatch identified by the first independent evaluator. GR-01 and GR-04 remain D3 locked references assembled from shared repository objects.

See `Baseline_Reconciliation_and_System_Correction_Report_v0.3-alpha.md`.


This is the first **executable local repository** produced by the Design System Transformation.

It is intentionally an **alpha**, not Design System v1.0.

## What changed

GR-01, GR-02 and GR-04 no longer own separate copies of the product foundations. They now consume:

- one central token source;
- one accessibility/foundation layer;
- one course shell;
- reusable buttons, option groups, status/feedback and save-state UI;
- shared choice/judgement behavior;
- a shared practice-focus component;
- registered templates/compositions/components/assets;
- machine-readable Golden Reference specifications;
- repository validators and browser smoke tests.

Reference-specific CSS now contains only the visual/composition treatment that has **not** earned global promotion.

## Why this matters

This is the first implementation of the intended future workflow:

> learner content + learning purpose + approved IDs + asset references → AI assembly from an existing system

rather than:

> broad prompt → AI redesign → local CSS fixes → drift.

## Open the Golden References

- `golden-references/GR-02/index.html`
- `golden-references/GR-04/index.html`
- `golden-references/GR-01/index.html`

Serve the repository over HTTP for best behavior.

## Validate

The repository validator checks every Golden Reference YAML specification against the shared schema and template registry. Install its dependencies first; see [template-schema reconciliation](docs/TEMPLATE_SCHEMA_RECONCILIATION.md) for compatibility and scope.

```bash
python -m pip install -r validators/requirements.txt
python validators/validate_repository.py
python tests/test_template_schema.py
python tests/run_static_smoke.py
```

## Current status

Repository Alpha is a **system proof**, not the production release.

Before Wave 2:

1. compare repository rebuilds to the accepted Wave 1 prototype quality;
2. complete human visual/accessibility review;
3. lock GR-04 and GR-01 specs;
4. run independent duplicate builds from this repository;
5. perform material-equivalence comparison.


## Wave 2 extension — GR-03

GR-03 adds three governed PROTOTYPE objects for guided perspective interpretation. It does not promote them to APPROVED and does not begin HRBA reconstruction.

## Wave 2 extension — GR-06

GR-06 implements the frozen evidence → interpretation → decision v1 → U01 adaptation → compare/review flow. Its status is **IMPLEMENTED_PENDING_MANUAL_VALIDATION**; the three new shared candidates remain PROTOTYPE. The existing GR01/04 locks, GR03/GR05 behavior and shared state service are preserved.

Serve the repository and open [GR-06](golden-references/GR-06/index.html). See the [governed result](golden-references/GR-06/GR-06_RESULT_SUMMARY.md), [direct-validation checklist](golden-references/GR-06/MANUAL_VALIDATION.md) and [synthetic semantic-review packet](golden-references/GR-06/GR-06_SEMANTIC_REVIEW_PACKET.md). H01–H09 semantic review is PASS (ChatGPT review explicitly reported by the user). Genuine Chrome 200%, actual screen-reader use and physical-mobile software-keyboard checks remain pending. No subsequent Golden Reference is authorized by this handoff.

## Current Wave-2 authority

Use the [current-decision index](WAVE_2_CURRENT_AUTHORITY.md) and its [machine-readable counterpart](WAVE_2_CURRENT_AUTHORITY.json). Earlier review/proposal documents remain historical evidence. Future coverage is governed by capability; Track A/B are not authorized. Every future specification must include the [experience-differentiation brief](prototype-specs/EXPERIENCE_DIFFERENTIATION_BRIEF_TEMPLATE.md). Repository validation now checks registered IDs, variants and authority in every specification and frozen contract; run `python tests/test_governed_references.py` for permanent negative tests.
