---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd tpl

`sd tpl create --name <text>` · `sd tpl step add <id> --title <text>` · `sd tpl list` · `sd tpl show <id>` — author and inspect **convoy templates**: a named, ordered list of step titles (each with an optional `type` and `priority`) stored in `.seeds/templates.jsonl` under a `tpl-{4hex}` id. Step titles support `{prefix}` interpolation, filled in at pour time.

Convoy templates predate plan templates and answer a different question. A **plan template** ([[seeds-plan-templates]]) describes the *shape of the thinking* an LLM must do — sections, validation, prompts — and is filled in fresh each time. A **convoy template** is a checklist whose content is already known: the same five steps you run for every service migration, instantiated verbatim by [[seeds-tpl-pour]]. One is a schema for reasoning; the other is a macro.

Maps to **no canonical SDLC stage** — authoring reusable scaffolding rather than planning any particular work.

## See Also
- [[seeds-tpl-pour]] — instantiates a template into real issues.
- [[seeds-tpl-status]] — tracks a poured convoy's completion.
- [[seeds-plan-templates]] — the planning-side templates, a different mechanism.
