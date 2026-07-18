---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: ["[[ce-external-evidence-researcher]]", "[[ce-precedent-activity-scout]]", "[[ce-project-grounding-scout]]"]
produces: []
applies: ["[[pattern-source-grounding]]", "[[pattern-adversarial-review]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-pov

`/ce-pov` — "Form a decisive verdict on external inputs with dual grounding and graded
Adopt/Trial/Hold/Reject outcomes." Given an external input (a library, technique, article,
tool), it grounds the assessment in **two** evidence sources (repo reality + web/docs) and
returns a graded verdict — Adopt / Trial / Hold / Reject (ThoughtWorks-Radar-style) — rather
than an open-ended discussion.

It is the **evaluate-and-decide** flavor of [[stage-align]]: deciding *whether* to bring
something in before it shapes a plan. No direct cross-framework counterpart — it is closest in
spirit to BMAD's [[bmad-forge-idea]] (adversarial hardening) but applied to *external* inputs
and terminating in a graded verdict, and to [[pattern-source-grounding]] (Addy's cite-the-docs
discipline) turned into a decision procedure.

## See Also
- [[ce-ideate]] — generates internal directions; `ce-pov` judges external inputs.
- [[bmad-forge-idea]] — adversarial idea hardening (internal analogue).
- [[addy-source-driven-development]] — the cite-official-docs discipline `ce-pov` operationalizes.
- [[stage-align]] — the canonical stage this implements.
