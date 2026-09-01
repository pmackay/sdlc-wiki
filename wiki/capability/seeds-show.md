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

# sd show

`sd show <id> [<id2> …]` — print full detail for one or more issues: title, status, type, priority, assignee, description, dependency edges, timestamps, close reason, labels, and an `Extensions: key=value …` line when the opaque `extensions` bag is populated (values JSON-encoded, so strings stay quoted and nested objects are unambiguous). Multi-id output separates entries per format — a horizontal rule in human output, blank lines in `plain`, an `issues` array under `--json`.

It is also plan-aware: a seed whose plan is in `draft` shows a hint, and one whose plan is `approved` lists the children inline, so an agent inspecting a parent seed sees the decomposition without a second call to [[seeds-plan-show]].

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-list]] · [[seeds-search]] · [[seeds-ready]] — the other read surfaces, filtered rather than by id.
- [[seeds-plan-show]] — the plan-side counterpart.
- [[seeds]] — the parent framework.
