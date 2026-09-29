# Governed template-schema reconciliation — 2026-09-28

Implemented under the user's shared-system correction authorization, after preserving GR-03 at commit `775ae1b` and annotated local tag `v0.3-alpha-gr03-wave2-review-pass`. No remote configured or push performed. Architectural review remains the next gate; GR-05 has not started.

## Authority and compatibility

`schemas/golden-reference.schema.json` is the authoritative Golden Reference / episode specification schema. Its `templateReference` definition canonically accepts an object with required nonempty string `id`, optional nonempty string `variant`, and no other object keys. The transitional nonempty string alternative is marked deprecated and means an ID without a variant. `schemas/episode.schema.json` delegates to that file through a relative `$ref`, removing the duplicate definition. Resolve that reference relative to the schema file URI when using an external JSON Schema tool; no network retrieval is needed.

No specification migration is required: GR-01/03/04 already use canonical objects, and GR-02 retains its existing legacy string. Learner HTML, CSS, JavaScript, registry dispositions, frozen contracts and locked build specifications remain unchanged. No variants are inferred or synthesized.

The repository validator discovers all `GR-*` directories, reads each `spec.yaml` with safe YAML loading, validates the entire specification with JSON Schema Draft 2020-12, and reports missing/invalid YAML and schema violations as failures. After schema validation it verifies the template ID against `registries/templates.json` and any explicitly declared variant against that template's own variants. A variant on a template with no registered variants fails. Variants remain optional in the generic contract, as requested; the existing GR-01/04 locked-build checks still require their governed variants and retain all previous D3, pattern, component, composition and asset checks.

## Explicit dependency policy

The repository validator now requires PyYAML and jsonschema. Install its tested versions with:

```powershell
python -m pip install -r validators/requirements.txt
python validators/validate_repository.py
python tests/test_template_schema.py
```

`validators/requirements.txt` pins PyYAML 6.0.3 and jsonschema 4.26.0. Both were already installed in the validation environment; no installation or runtime dependency was added to learner pages. JSON output now truthfully reports the external Python packages. Existing HTML smoke/GR-03 tests continue to use their existing Beautiful Soup dependency.

## Validation scope

`tests/test_template_schema.py` covers canonical objects, legacy strings, optional variants, malformed references, missing required specification fields, unknown template IDs, wrong-template variants, offline episode-schema delegation, all four current references, and discovery/failure of added missing or invalid specifications in a temporary repository fixture. No production specification is mutated by these tests.

Full regression commands/results are recorded in `tests/schema-reconciliation-command-log.json`; browser/stress results are in `tests/gr03-browser-validation-schema-reconciliation.json`. The existing browser runner conservatively emits FAIL for every automated run because it cannot make a manual governed decision. The reviewed evidence explicitly combines successful automated assertions with the already accepted native 200% attestation; it does not claim that native work was repeated. No learner code changed since that attestation.

Final integrity receipt: `tests/package-integrity.json`. Review archive: `package/GR03_Schema_Reconciliation_Review_2026-09-28.zip`. Package integrity does not constitute Golden Reference acceptance.

GR-03 remains PASS_FOR_WAVE_2_SYSTEM_REVIEW only. Candidate objects remain PROTOTYPE / RETAIN CANDIDATE. Refresh persistence remains an open, nonblocking architectural observation; it is not implemented here.
