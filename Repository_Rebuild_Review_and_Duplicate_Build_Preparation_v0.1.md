# Repository Rebuild Review + Locked Duplicate-Build Preparation v0.1

**System:** CSO Learning Design & Production System v0.2.1-alpha  
**Stage:** Gate 8 — Wave 1 hardening  
**Status:** **READY FOR LOCAL BROWSER REGRESSION + INDEPENDENT LOCKED DUPLICATE BUILD**  
**Date:** 27 September 2026

---

# 0. Executive result

Repository Alpha has now been hardened specifically for the duplicate-build test.

The most important improvement is architectural:

> **GR-01 and GR-04 no longer own their visual layout CSS.**

Their previously reference-specific visual rules have been promoted into real registered template implementations:

- `TPL-COURSE-ENTRY-01 / editorial-split-illustrated`
- `TPL-SCENARIO-01 / professional-judgement-dark-evidence`

The transfer was **byte-for-byte for the existing visual CSS rules**. No visual redesign was introduced during this ownership change.

Their local `reference.css` files are now empty.

This substantially strengthens the test of the user's intended future workflow:

> exact content + approved IDs + registered asset → system template/renderer → learner experience

rather than:

> AI receives a design description → invents layout/CSS → review/correction cycle.

---

# 1. Why the hardening was necessary

The first repository materialization successfully centralized:

- tokens;
- foundations;
- shell;
- buttons/options/status;
- interaction mechanics;
- practice-focus behavior;
- registries and validators.

But GR-01 still owned about **7.5 KB** of visual CSS and GR-04 about **5.4 KB**.

That meant an independent builder could still have been asked to infer too much of the actual composition.

That would not be a strong enough test of determinism.

The correct response was not a longer prompt.

The correct response was to move those design decisions into the system.

---

# 2. What changed in v0.2.1-alpha

## GR-01

The full accepted prototype visual treatment previously in:

`golden-references/GR-01/reference.css`

now lives in:

`templates/course-entry/course-entry.css`

Template variant:

`editorial-split-illustrated`

The course-entry template now owns:

- hero editorial field;
- image field treatment;
- headline scale/relationship;
- question-thread treatment;
- journey section treatment;
- Practice Focus composition;
- closing course-entry band;
- mobile recomposition.

GR-01 supplies:

- content;
- asset ID;
- shell configuration;
- practice-focus options.

It does not supply visual CSS.

## GR-04

The full accepted prototype visual treatment previously in:

`golden-references/GR-04/reference.css`

now lives in:

`templates/scenario/scenario.css`

Template variant:

`professional-judgement-dark-evidence`

The scenario template now owns:

- evidence-field visual treatment;
- evidence list;
- decision relationship;
- takeaway treatment;
- response-path treatment;
- tablet/mobile transformations.

GR-04 supplies:

- scenario/evidence content;
- decision options;
- feedback;
- practitioner reasoning;
- pathway labels.

It does not supply visual CSS.

---

# 3. Visual-fidelity protection during extraction

The CSS was **moved rather than redesigned**.

SHA-256 comparison confirms:

- GR-01 old `reference.css` == new `templates/course-entry/course-entry.css`
- GR-04 old `reference.css` == new `templates/scenario/scenario.css`

Therefore the extraction itself did not alter the visual-rule content.

A fresh browser regression is still required because this environment blocks local/loopback browser navigation.

---

# 4. Locked build specifications now exist

Two content-complete D3 specifications have been created:

- `locked-build-specs/GR-01_LOCKED_BUILD_v0.1.yaml`
- `locked-build-specs/GR-04_LOCKED_BUILD_v0.1.yaml`

They lock:

- instructional pattern;
- template ID + variant;
- composition ID;
- shell configuration;
- exact learner-facing content;
- content order;
- asset ID;
- interaction behavior;
- completion behavior;
- responsive contract;
- accessibility contract;
- permitted stylesheet/script dependencies;
- prohibition on local CSS;
- prohibition on new tokens/components/assets.

These specifications are now materially closer to a true deterministic production contract than the earlier short registry references.

---

# 5. A deterministic renderer now exists

New tool:

`tools/render_locked_reference.py`

It reads the locked YAML specification and registered template structure and generates the page.

This is an important evolution in the production model.

Codex no longer needs to decide:

- where content goes;
- how the shell is constructed;
- what CSS is required;
- what visual regions exist;
- what responsive model applies.

For these locked references, Codex can simply invoke the system.

That is a stronger and more efficient interpretation of:

> **AI as assembler rather than designer.**

---

# 6. Locked-build validator now exists

New tool:

`tools/validate_locked_build.py`

It checks, among other things:

- exactly one H1;
- all locked CSS/JS dependencies present;
- shared shell present;
- no local stylesheet when prohibited;
- exact locked learner-facing content present;
- correct registered hero asset for GR-01;
- five Practice Focus options;
- GR-04 option IDs/order;
- GR-04 structured feedback payload;
- shared course action footer;
- no arbitrary inline visual styling.

Both current generated references pass.

---

# 7. Repository/static validation result

After hardening:

- repository validation: **PASS**;
- static smoke suite: **PASS**;
- GR-01 locked-build validation: **PASS**;
- GR-04 locked-build validation: **PASS**;
- JavaScript syntax validation: **PASS**.

The original browser limitation remains:

`net::ERR_BLOCKED_BY_ADMINISTRATOR`

for local file navigation in this environment.

Therefore no new claim of pixel/browser equivalence is being made here.

---

# 8. What the independent Codex test should now receive

The independent builder should receive **only**:

- shared repository system files;
- registered asset(s);
- locked GR-01 and GR-04 specifications;
- deterministic renderer;
- validators;
- build instructions.

It should **not** receive:

- existing GR-01/GR-04 HTML;
- existing reference implementation code;
- baseline screenshots;
- prior rendered screenshots as design instructions.

This preserves the integrity of the duplicate-build test.

---

# 9. Independent-build expected behavior

The clean agent should:

1. read the repository README and AI build contract;
2. run repository validation;
3. read the locked spec;
4. run the registered renderer;
5. run locked-build validation;
6. run browser smoke/regression in its normal local environment;
7. return build evidence.

It should **not create CSS or JavaScript** for GR-01 or GR-04.

If it believes new CSS/component logic is required, it must stop and raise a System Gap.

That is the central test.

---

# 10. What success will prove

If a clean Codex session can reproduce the references using only the system + locked specifications, then we have direct evidence that:

- visual design resides in the repository;
- content resides in the specification;
- behavior resides in reusable components;
- responsive/accessibility rules are inherited;
- AI does not need a broad visual prompt;
- local screen-level CSS invention is unnecessary.

This is the practical future-course workflow the project is aiming for.

---

# 11. What failure would mean

If the clean build diverges materially, we should not ask Codex to “try again more carefully.”

We should identify what remains underspecified or unimplemented in:

- template;
- component;
- schema;
- renderer;
- token;
- asset contract.

Then fix the system and rerun.

Failure therefore becomes useful design-system evidence.

---

# 12. Immediate execution sequence

## Step 1 — local browser regression

In the normal Codex/local repository environment:

- render GR-01 and GR-04;
- capture required viewports;
- compare against Wave 1 baselines;
- verify interaction states;
- verify keyboard/reduced-motion;
- correct any **system-level** regression centrally.

## Step 2 — independent locked duplicate build

Use the separate `Independent_Locked_Duplicate_Build_Kit_v0.1.zip`.

## Step 3 — material-equivalence review

Compare:

- IDs;
- exact locked copy;
- template/composition;
- asset IDs;
- interactions;
- completion;
- responsive behavior;
- accessibility structure;
- screenshots.

## Step 4 — Gate 8 decision

If successful:

- record D3 reproducibility evidence;
- promote the proven repository objects appropriately;
- then proceed to Wave 2 from the shared repository.

---

# 13. Current decision

**REPOSITORY REBUILD/HARDENING: PASS**

**INDEPENDENT DUPLICATE BUILD: READY TO EXECUTE**

**GATE 8: STILL IN EXECUTION UNTIL BROWSER + DUPLICATE + LEARNER VALIDATION ARE COMPLETE**
