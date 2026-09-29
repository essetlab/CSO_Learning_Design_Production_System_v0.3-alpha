# BLK-EVIDENCE-LEDGER-01

PROTOTYPE only. Source metadata, typed evidence associations, field-aligned comparison and export representation.

`referenceContent` renders exact source metadata and limits; `sourceNotes` owns the five authored note fields. `interpretations` and `decision` render authored fields and typed evidence/role associations. `record`, `comparison` and `representation` retain immutable v1/current text, links, confidence, U01 and criterion follow-up in readable paired and export forms. Inputs are plain text (`textContent`/textarea values), never interpreted as markup.

The caller supplies the governed contract, state and edit/toggle callbacks. The block does not decide release timing, grant completion, write storage, score semantics or alter source records. Generic writing fields and criterion controls reuse the existing artifact primitives unchanged.

Frozen GR-06 Revision 2 supplies the case. Shared state service owns storage only. No AI grading, prepared answers, new tokens or local persistence.
