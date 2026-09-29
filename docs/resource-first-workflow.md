# Resource-First Visual Production Workflow v0.1

**Status:** Standing workflow rule for the Design System Transformation  
**Applies from:** Gate 8 onward

## Principle

Before creating any new visual prototype, layout, interaction, illustration, component, template, or supporting asset:

> **Check what already exists first.**

The preferred order is:

**Reuse directly → adapt a strong existing resource → harvest its underlying pattern/mechanics → create new only when a genuine gap remains.**

This is not a shortcut around design quality.

It is a way to start from the strongest available work, reduce repeated invention, and move more quickly toward a polished, reusable system.

---

## 1. Visual Resource Preflight

Before any visual build, inspect:

1. the approved local CSO design/production repository;
2. Mighty Studio / `templates_elearning_resource_pack`;
3. accepted HRBA R&D;
4. accepted PM R&D;
5. reusable Hub components and assets;
6. existing illustration/asset registers;
7. approved institutional assets such as partner branding.

The build brief must record that this check occurred.

---

## 2. Classify each useful resource

Every relevant resource receives one disposition.

### REUSE DIRECTLY

Use when it is already approved and fit for purpose.

Example:
- approved responsive partner-branding strip.

### ADAPT

Use when the underlying resource is strong but needs:
- DEC brand mapping;
- accessibility adjustment;
- responsive transformation;
- content/schema normalization;
- removal of external/platform styling.

### HARVEST PATTERN / MECHANICS

Use when:
- layout principle is strong;
- interaction mechanics are useful;
- exact design should not be copied.

Example:
- a Mighty editorial composition;
- decision-judgement interaction mechanics.

### REFERENCE ONLY

Use for quality direction but not implementation.

### REJECT

Use when:
- visual treatment conflicts with learning;
- accessibility/mobile cost is too high;
- it is too generic;
- it adds duplication;
- it does not fit the CSO experience.

### NEW SYSTEM GAP

Only when no existing resource adequately serves the legitimate learning need.

---

## 3. External-source rule

Mighty and other strong external resources may accelerate the system.

But after selection, the target process is:

**External source → DEC adaptation → accessibility/responsive validation → token normalization → local component/template ID → local repository**

The future course should not depend on the external gallery remaining unchanged.

The reusable DEC implementation becomes the production object.

---

## 4. Learning remains upstream

Existing resources may influence:

- composition;
- visual treatment;
- interaction mechanics;
- responsive behavior;
- authoring experience.

They do **not** determine:

- capability;
- learning objective;
- judgement task;
- assessment;
- feedback principle;
- privacy;
- practice transfer.

Those remain governed by Gates 2–4.

---

## 5. No from-scratch rule

Do not start a visual prototype from a blank page until the Resource Preflight has shown either:

- no strong existing candidate; or
- existing candidates fail a documented requirement.

If a strong existing composition already solves 70–90% of the visual problem, adapt it.

---

## 6. Code/resource ingestion rule

When working source code is available from Mighty or another owned/authorized resource:

1. preserve the source copy;
2. inspect its dependencies;
3. strip unrelated vendor styling/logic;
4. remap all visual values to DEC semantic tokens;
5. replace vendor-specific semantics with our accessibility contract;
6. define editable/locked fields;
7. test mobile/200%/keyboard/screen reader;
8. assign a DEC candidate ID;
9. store the normalized implementation locally;
10. keep provenance.

If only screenshots/reference assets are available, harvest the composition rather than pretending the screenshot is reusable code.

---

## 7. Efficiency target

The resource-first workflow should reduce:

- repeated layout invention;
- correction cycles;
- CSS duplication;
- Codex visual drift;
- inconsistent responsive behavior;
- time spent explaining familiar patterns in prompts.

It should increase:

- visual quality;
- speed;
- reuse;
- confidence;
- deterministic production;
- ability to learn from already-proven design.

---

## 8. Production brief field

Every future visual build brief should include:

```yaml
resource_preflight:
  checked:
    - local_approved_repository
    - mighty_resource_pack
    - hrba_prior_rd
    - pm_prior_rd
    - hub_reusable_assets

  selected_source:
  disposition:
    - reuse_directly
    - adapt
    - harvest_pattern
    - reference_only
    - new_system_gap

  reason:
  provenance:
```

---

## 9. Governance principle

Resource-first does not mean template-first learning.

The correct sequence is:

**Learning need → search existing resources → choose strongest fit → adapt into governed system → validate → reuse.**

Not:

**Template found → force content into it.**

---

## 10. Standing decision

This workflow becomes a standing Design System Transformation rule.

Before any future visual work, the assistant should first ask internally:

> **What strong approved or owned resource already exists that can save us from rebuilding this?**
