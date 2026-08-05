---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-strategy-md]]"]
applies: ["[[pattern-source-grounding]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[agent-os-plan-product]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-08-05
---

# /ce-strategy

`/ce-strategy` — "Create or maintain `STRATEGY.md` — the upstream anchor read by ideate, brainstorm, and plan." It establishes a durable product/engineering strategy document that sits *above* the per-feature loop and grounds everything downstream: [[ce-ideate]] filters ideas against it, [[ce-brainstorm]] scopes requirements to it, and [[ce-plan]] aligns work with it → [[artifact-strategy-md]].

It is the highest-altitude Compound Engineering capability — a standing anchor rather than a per-change act. It has no direct cross-framework counterpart: it is a **product-strategy** anchor, distinct from Spec Kit's code-governance [[artifact-constitution|constitution]] (the closest structural analogue — a durable document consulted by later steps), which parks the `stage-govern` split candidate on [[stage-align]].

## See Also
- [[speckit-constitution]] — Spec Kit's durable upstream anchor (governance flavor; see `stage-govern` on [[stage-align]]).
- [[ce-ideate]] · [[ce-brainstorm]] · [[ce-plan]] — the downstream steps that read `STRATEGY.md`.
- [[stage-align]] — the canonical stage this implements.
