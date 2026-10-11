---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-plan-md]]"]
applies: ["[[pattern-contract-first]]", "[[pattern-throwaway-prototype]]", "[[pattern-source-grounding]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /visual-plan

Turn a text plan into an **interactive visual plan**: a scannable MDX document with inline diagrams, file maps, annotated code, open questions, and, for UI work, a top canvas with wireframes, a live prototype, or both. It is viewed and commented on in Builder's hosted Agent-Native Plans app, or served locally in *local-files* privacy mode. It exists for *"plans that are too important to bury in chat."*

The **plan discipline** section applies to any planning skill. Gate thoughtfully: skip trivial work, *"never pad a plan with filler and never ship a single-step plan."* Research before drafting and name real files and symbols, *"lead[ing] with reuse"* so the plan describes only the new delta. **Decide the hard-to-reverse bets first**: wire format, public IDs, data-model shape, and auth boundaries, then *"scope to the smallest first cut that proves the approach without foreclosing it."* Keep examples at the right altitude: do not collapse a broad framework change into the first provider the user mentioned. Publish a standalone plan that someone who never saw the chat can read, with no revision language.

[[stage-plan]]. It builds on an existing Codex, Claude Code, or Markdown plan instead of starting over, so it is a review surface for plans as much as a way of writing them.

## See Also
- [[builder-visual-recap]] — the same data model pointed backwards at a diff.
- [[builder-plan-arbiter]] — accepts visual-plan links as source plans.
- [[stage-plan]] — the canonical stage this implements.
