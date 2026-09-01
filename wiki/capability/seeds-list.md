---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd list

`sd list` — the general filtered listing: `--status`, `--type`, `--assignee`, `--label`, `--priority`, `--priority-max`, `--limit`, `--all`, `--sort`, and `--format`.

The `--format` set is where the command earns its [[pattern-context-engineering]] edge. Five renderings of the same query — `markdown`, `compact`, `plain`, `ids`, `json` — let the caller pay only for the tokens it needs. `compact` is a one-line-per-issue table for dropping into an agent's context; `ids` prints bare ids one per line for shell pipelines (`sd list --label bug --format ids | xargs sd close`), turning the tracker into a composable Unix filter rather than something an agent has to parse prose out of. Colors respect `NO_COLOR`.

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-ready]] — the same listing narrowed to actionable work.
- [[seeds-search]] — substring query rather than field filters.
- [[seeds-stats]] — the aggregate view.
- [[pattern-context-engineering]] — the pattern the format modes serve.
