## Shared template-schema correction — 2026-09-28

The previously open template-schema/validator inconsistency is now **RESOLVED IN CODE, awaiting architectural review**. See `docs/TEMPLATE_SCHEMA_RECONCILIATION.md`. One authoritative schema accepts canonical `{id, variant?}` objects plus transitional legacy strings; the episode schema references it. Repository validation now checks all four Golden Reference YAML specifications and verifies template IDs and declared variants against the registry. No specification migration or learner-code change was needed; GR-02 retains its supported legacy string.

Regression PASS: all 13 static/schema/syntax commands, eight schema test methods with positive/negative cases, exact GR-01/04 locked renders, and 423 browser assertions including 116 maximum-content checks. New browser evidence: `tests/gr03-browser-validation-schema-reconciliation.json`; summary: `tests/schema-reconciliation-summary.json`. The accepted native 200% attestation remains applicable to unchanged learner code; it was not repeated.

GR-03 remains **PASS_FOR_WAVE_2_SYSTEM_REVIEW**, not Golden Reference acceptance. Candidate objects remain PROTOTYPE / RETAIN CANDIDATE. Refresh persistence remains an open nonblocking architectural observation. No GR-05 work. Checkpoint: `775ae1bb4542c0495e31c66fb347aa1225e8e92a`, tag `v0.3-alpha-gr03-wave2-review-pass`. No remote or push.

Latest review archive: `package/GR03_Schema_Reconciliation_Review_2026-09-28.zip`; final integrity receipt: `tests/package-integrity.json`. Earlier OPEN schema statements below are historical and superseded by this correction.

---

# Shared template schema reconciliation — proposal for architectural approval

Status: **OPEN; proposed only, not implemented.** Resolve before GR-05 production.
Classification: repository/schema governance item (C), not a new component/System Gap.

## Exact scope found

| Reference | `golden-references/*/spec.yaml` template value | Generic schema compatibility |
| --- | --- | --- |
| GR-01 | `{id: TPL-COURSE-ENTRY-01, variant: editorial-split-illustrated}` | Fails string type |
| GR-02 | `TPL-CONCEPT-01` | Matches string type |
| GR-03 | `{id: TPL-CONCEPT-01}` | Fails string type |
| GR-04 | `{id: TPL-SCENARIO-01, variant: professional-judgement-dark-evidence}` | Fails string type |

Both `schemas/golden-reference.schema.json` **and** `schemas/episode.schema.json` define template as string. They share the same properties/required fields and currently duplicate the definition. No schema file was changed in this task.

`validators/validate_repository.py` reads only the GR-01/GR-04 locked **JSON** specifications. It validates registry references, template variants, build mode, D3 determinism and assets, but does not load any Golden Reference `spec.yaml` or invoke JSON Schema validation. `validators/validate_gr03.py` checks registry IDs, HTML structure and dependencies; it also does not validate spec.yaml against the schema. Wave-1 smoke checks HTML/shared assets and choice data. Locked-build checks compare generated HTML against the locked JSON renderer. Thus these checks legitimately pass within their scope without proving generic schema compliance.

## Comparison with architectural intent

The user identifies the upstream Gate-7 intent as authoritative. No standalone full Gate-7 specification is present in this working repository, so direct verification against an unavailable source is not claimed. Available local architectural evidence is consistent with structured templates:

- `package/system-version.yaml` names Gate 1–8 architecture as its basis.
- `Repository_Rebuild_Review_and_Duplicate_Build_Preparation_v0.1.md`, section 4, explicitly locks **template ID + variant**, shared dependencies, responsive/accessibility contracts, content order and D3 reproducibility.
- GR-01/GR-04 locked JSON specifications and `validators/validate_repository.py` consume `template.id` and `template.variant`.
- `registries/templates.json` records the two relevant variants; TPL-CONCEPT-01 has no declared variants.
- `docs/ai-build-contract.md` requires registered IDs and shared implementations.

Flattening the structured objects to strings would discard variant authority and conflict with that D3 design. This is not necessary for GR-03 browser validation and was not done.

## Smallest recommended reconciliation

For architectural approval: make `{id: string, variant?: string}` the canonical template representation. Permit the current string shorthand as a documented transitional `oneOf` alternative in both affected generic schemas, interpreted as `{id: <string>}` without an invented variant. This permits all four current references without rewriting locked learner artifacts. Require `id`, prohibit unknown template-object keys, validate IDs against the registry, and require a registered variant where a template defines variants. GR-01/04 remain structured; a separately approved normalization can later convert GR-02 to `{id: TPL-CONCEPT-01}` and retire the shorthand.

Add explicit validation of GR-01/02/03/04 spec.yaml against the reconciled canonical schema, plus registry/variant cross-checks and negative fixtures for unknown IDs/variants and malformed values. Use one schema source (reference it from the episode schema) to prevent future drift. Decide the YAML/JSON Schema dependency policy explicitly; the current core repository validator is dependency-free and this should not change silently.

Approval should confirm the transitional representation, dependency policy and whether the full Gate-7 source adds stricter requirements. Then implement the schema/validator correction as governed shared architecture work, rerun all locked/static/browser regressions, and update package integrity before GR-05. This proposal does **not** claim the inconsistency is resolved, authorize GR-05, or promote any Wave-2 candidate.
