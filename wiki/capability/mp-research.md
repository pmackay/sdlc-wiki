---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-research-md]]"]
applies: ["[[pattern-source-grounding]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[gsd-phase-researcher]]"]
docs_url: "https://www.aihero.dev/skills-research"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# research

`/research` — a model-invoked engineering skill that spins up a **background agent** to investigate a question against **high-trust primary sources** — official docs, source code, specs, first-party APIs, "not a secondary write-up of them" — following every claim back to the source that owns it, and captures the findings as a single **cited Markdown file** in the repo ([[artifact-research-md]]). "Delegable reading legwork": you keep working while it reads, and get back a document to grill, plan, or design against.

**New in v1.1 (2026-07-09).** It enacts [[pattern-source-grounding]] (cite primary sources, flag the unverified) and runs as a [[pattern-fresh-context-subagents|fresh-context background agent]]. Its closest cross-framework counterpart is GSD's [[gsd-phase-researcher]] (parallel domain research → `RESEARCH.md`); it also relates to BMAD's [[bmad-research]] (align-time market/domain/tech research) and the Compound Engineering researcher sub-agents.

## See Also
- [[gsd-phase-researcher]] — GSD's parallel-research counterpart → [[artifact-research-md]].
- [[bmad-research]] — BMAD's align-time research relative.
- [[addy-source-driven-development]] — the same cite-primary-sources discipline as an implementation skill.
- [[stage-plan]] — the canonical stage this implements (research as planning input).
