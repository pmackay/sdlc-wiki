---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-specify]]"
produces: "[[artifact-checklist]]"
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-checklist

**`/speckit.checklist`** — "Generate custom quality checklists that validate requirements completeness, clarity, and consistency." An optional command the Spec Kit team describes as **"unit tests for your English"**: it produces a bespoke [[artifact-checklist]] that interrogates the *requirements themselves* for gaps, ambiguity, and internal contradiction — a quality gate on the spec before it flows downstream into planning.

## A spec-quality gate

`checklist` targets the specification's quality rather than a built system, so it belongs to [[stage-specify]] (getting the spec right) rather than [[stage-validate]]. It has **no counterpart in another framework** here — the others harden the spec through grilling or review prose, not a generated checklist artifact — so it stays a Spec-Kit-specific specialisation within the specify stage.

> **Source note:** the current docs frame checklist as validating *requirements*; the older conceptual `spec-driven.md` framed it as continuous validation of generated *code* against the spec. This page follows the current docs.

## See Also
- [[speckit]] — the framework.
- [[speckit-specify]] — produces the requirements this command quality-checks.
- [[speckit-clarify]] — the interactive counterpart (resolve) to this generated gate (measure).
- [[stage-specify]] — the canonical stage.
