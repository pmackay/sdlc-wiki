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

# sd search

`sd search <query>` — case-insensitive substring match over issue title and description, with the full filter set layered on top (`--status`, `--type`, `--assignee`, `--label`, `--label-any`, `--unlabeled`, `--priority`, `--priority-max`, `--limit`, `--sort`, `--format`).

No index, no ranking, no embeddings — a linear scan of a JSONL file, which is all the data model needs. Its role in the workflow is **duplicate avoidance**: the [[seeds-issue-workflow]] skill puts `sd search "<keywords>"` in the pre-flight step, before filing, so an agent claims existing work instead of forking a second seed for it.

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-list]] — filter-based rather than text-based listing.
- [[seeds-issue-workflow]] — the skill that mandates a search before a create.
- [[seeds]] — the parent framework.
