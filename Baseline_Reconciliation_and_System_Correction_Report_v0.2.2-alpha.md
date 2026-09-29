# Baseline Reconciliation & System Correction Report v0.2.2-alpha

## Decision

The independent duplicate builder is accepted as a faithful deterministic assembler of the supplied v0.2.1 system. The failed visual-equivalence result is classified as a **system/baseline mismatch**, not builder drift.

## Corrections made at system level

### GR-01 — Course Entry

1. Restored the accepted **DEC blue filled primary CTA with navy text** inside the course-entry template while preserving the scenario template's navy primary action.
2. Restored the accepted **green emphasized headline**.
3. Restored the accepted hero fallback surface and visual-detail mix values.
4. Restored the course-entry copy alignment to the Wave 1 reference width.
5. Added a template-level cross-platform mobile line-break guard so the emphasized phrase retains the accepted three-line rhythm at narrow mobile widths.
6. Removed inherited link underlining from anchor-rendered button components.

### GR-04 — Professional Judgement

Restored the accepted mobile response pathway:

- one-column sequence;
- numbered circular step markers;
- separator rows;
- no rounded-card treatment on mobile;
- arrows removed after recomposition.

## Tooling corrections

- locked specs and registries are available as JSON;
- repository validator uses Python standard library only;
- locked renderer uses Python standard library only;
- locked build validator uses Python standard library only;
- line-ending normalization is explicit;
- no BeautifulSoup/PyYAML dependency is required by the independent kit or evaluator.

## Governance interpretation

These corrections are **not new design exploration**. They restore the accepted visual contracts that were lost when prototype code was decomposed into shared repository objects.

The lesson is important: extraction into a design system must preserve not only semantic behavior but also the **material visual contract** of the accepted source reference.
