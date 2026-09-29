# Repository Alpha Materialization Report v0.2-alpha

**System:** CSO Learning Design & Production System  
**Status:** **EXECUTABLE REPOSITORY ALPHA MATERIALIZED**  
**Date:** 27 September 2026

---

# 1. Executive result

The first real local reusable repository now exists.

This is the point at which the Design System Transformation moves beyond:

- architecture documents;
- prototype screenshots;
- separate HTML/CSS experiments;

and begins operating as an actual reusable production system.

GR-01, GR-02 and GR-04 are no longer treated as independent implementations owning their own design foundations.

They now consume a shared repository containing:

- one token source;
- shared foundations/accessibility/motion rules;
- one course shell implementation;
- shared UI controls;
- reusable feedback/status behavior;
- one shared single-choice feedback engine used by the choice and judgement interactions;
- shared Practice Focus behavior;
- composition definitions;
- template manifests;
- component, template, composition, pattern and asset registries;
- machine-readable Golden Reference specs;
- validation scripts;
- baseline visual-reference screenshots.

This is the first operational version of the future workflow the user described:

> **content + learning purpose + approved object IDs + asset references → assemble from the system rather than redesigning.**

---

# 2. What is now genuinely centralized

## Tokens

There is now **one executable token source**:

`tokens/tokens.css`

The six Wave 1 token differences were deliberately normalized rather than inheriting one prototype blindly.

Repository-alpha decisions:

- focus offset → `2px`;
- standard subtle shadow → quieter GR-02/04 value;
- a separate `shadow-feature` token retains the stronger Peak Experience elevation where justified;
- body type → common GR-02/04 measure;
- metadata → `0.78rem`;
- standard content width → `76rem`;
- wide width → `90rem`;
- immersive width → separate `100rem` token rather than making all pages wider.

The display **role** is centralized, while the exact final display family remains intentionally provisional.

---

## Foundations

Centralized:

- box sizing/base reset;
- page/body defaults;
- content canvas behavior;
- episode-heading structure;
- focus treatment;
- skip link;
- visually-hidden utility;
- reduced-motion behavior.

Golden Reference folders no longer declare their own `:root` token blocks.

---

## Course shell

There is now one shared `SHELL-GR-W1-01` implementation:

- app bar;
- DEC identity;
- course/module context;
- progress;
- menu/drawer;
- Escape behavior;
- focus return;
- responsive collapse;
- optional shared Previous/Continue action footer.

Each Golden Reference supplies only configuration such as:

- course title;
- module context;
- progress label/value;
- menu links;
- standard or immersive shell variant.

This is a major change from the previous three duplicated shell implementations.

---

# 3. Shared interaction mechanics

A particularly important architectural improvement occurred during materialization.

GR-02 `INT-CHOICE-01` and GR-04 `INT-JUDGMENT-01` now use the same underlying **single-choice feedback engine** while remaining separate registered learning interactions.

That means the system reuses the stable mechanics:

- single selection;
- explicit review/commit;
- explanatory feedback;
- feedback-viewed completion;
- revise;
- Continue enablement;
- deterministic QA state.

But the two experiences can still differ in:

- learning purpose;
- evidence treatment;
- feedback semantics;
- composition;
- visual intensity.

This is exactly the desired principle:

> **reuse mechanics without forcing visual sameness.**

---

# 4. Reference-specific code has materially reduced

Before repository extraction, each reference owned its own foundational CSS and JavaScript.

After extraction, reference folders own only their still-unpromoted composition/course-specific styling and content configuration.

| Reference | Previous local CSS+JS | New reference-owned CSS+JS | Reduction |
|---|---:|---:|---:|
| GR-02 | 22,084 B | 4,971 B | **77.5%** |
| GR-04 | 26,015 B | 5,401 B | **79.2%** |
| GR-01 | 22,634 B | 7,530 B | **66.7%** |

The important issue is not byte savings by itself.

It is that future fixes to:

- focus;
- shell;
- buttons;
- option controls;
- choice/judgement state mechanics;

can now be made once rather than separately in every module/screen.

---

# 5. Registries now exist as executable production controls

The repository now has machine-readable registries for:

- components;
- instructional patterns;
- compositions;
- templates;
- assets;
- tokens.

Golden Reference specs reference IDs such as:

- `TPL-SCENARIO-01`;
- `CMP-EVIDENCE-DECISION-01`;
- `INT-JUDGMENT-01`;
- `AST-HRBA-GR01-HERO-EXISTING-01`.

The repository validator rejects unknown IDs and local token/system duplication.

This is the first tangible step toward a future Codex instruction such as:

> Build this episode using `TPL-SCENARIO-01` + `INT-JUDGMENT-01` + the supplied content and asset IDs.

rather than asking Codex to design the interaction.

---

# 6. Resource-first visual production is represented in the repository

GR-01 retains:

- the harvested Mighty editorial composition logic;
- the reused existing HRBA hero asset;
- source provenance.

The asset is now centrally registered:

`AST-HRBA-GR01-HERO-EXISTING-01`

The Golden Reference consumes the registered local asset rather than owning a duplicate copy.

The Resource-First Visual Production Workflow is also stored under `/docs` as a standing repository rule.

---

# 7. Validation completed in this environment

## Repository validation — PASS

The executable validator confirmed:

- all reference component IDs exist;
- all composition IDs exist;
- all template IDs exist;
- all instructional-pattern IDs exist;
- asset IDs resolve;
- no Golden Reference has a local `:root` token block;
- no Golden Reference locally duplicates the shared app bar, drawer, action footer or base button implementation;
- no reference-specific CSS contains raw hex colors.

## Static smoke test — PASS

Confirmed:

- one H1 in each reference;
- shared shell placeholder present;
- no copied shell markup in Golden Reference HTML;
- all local CSS/JS/image dependencies resolve;
- GR-02 option values match its structured feedback data;
- GR-04 option values match its judgement feedback data;
- GR-04 retains the strongest-response state;
- GR-01 retains five optional Practice Focus choices;
- all three references consume the same central tokens, shell CSS, shell JS and button implementation.

## JavaScript syntax — PASS

Shared JavaScript files pass Node syntax validation.

---

# 8. Browser regression limitation in this session

A fresh browser regression could not be executed **inside this current tool environment** because browser navigation to local/loopback pages is blocked by the environment administrator.

This is an environment limitation, not a repository design decision.

Therefore I have **not** claimed that Repository Alpha has passed a new pixel/viewport browser regression.

Instead:

- the previously browser-validated Wave 1 screenshots have been copied into `/tests/baseline-screenshots`;
- a future/local `run_browser_smoke.py` is included;
- the duplicate-build phase must execute the actual browser comparison in the normal local/Codex development environment.

This keeps the evidence honest.

---

# 9. What remains intentionally reference-specific

The repository did **not** globalize:

- GR-02's exact radial Rights Lens geometry;
- GR-04's dark evidence-panel visual treatment;
- GR-04's response-path diagram;
- GR-01's vertical HRBA marker;
- GR-01's five-question hero overlay;
- the HRBA hero artwork itself.

These remain course/reference-level expression.

This is important: repository materialization has not flattened the visual experience into one universal template.

---

# 10. Repository Alpha status

## Successfully materialized

- executable shared tokens;
- shared foundations;
- shared shell;
- shared UI layer;
- shared interaction engine;
- reusable practice-focus behavior;
- registered assets;
- schemas;
- registries;
- validators;
- three repository-consuming Golden References.

## Still PROTOTYPE

- exact display font;
- `INT-JUDGMENT-01` cross-course status;
- `CMP-IMMERSIVE-01`;
- `CMP-EVIDENCE-DECISION-01`;
- `CMP-EDITORIAL-01`;
- three page templates;
- exact shell visual density.

This repository is **v0.2-alpha**, not v1.0.

---

# 11. The practical workflow change is now visible

Previously GR-04 effectively said:

> Here is a judgement screen. Build its shell, option controls, feedback mechanics, responsiveness and visual treatment.

The repository version now says, structurally:

> `SHELL-GR-W1-01`  
> `TPL-SCENARIO-01`  
> `CMP-EVIDENCE-DECISION-01`  
> `UI-OPTION-GROUP-01`  
> `INT-JUDGMENT-01`  
> `BLK-FEEDBACK-01`  
> plus this learner content.

The reference-specific layer no longer owns the basic control mechanics.

That is the intended transition from **AI-as-designer** toward **AI-as-assembler**.

---

# 12. Right next step

The next step is now:

# **Repository Rebuild Review + Locked Duplicate-Build Preparation**

Specifically:

1. inspect the repository-driven GR-02/04/01 against their Wave 1 visual baselines in a browser-capable local/Codex environment;
2. correct any regression **in the shared system first**, not per reference;
3. lock the GR-04 and GR-01 acceptance specifications;
4. give the repository + locked specs to a clean independent AI build;
5. compare material equivalence.

Only after that should Gate 8 Wave 2 begin.

This is now a much stronger test than simply producing another screen.
