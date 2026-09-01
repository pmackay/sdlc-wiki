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

# sd label

`sd label add <id> <label>` · `sd label remove` · `sd label list <id>` · `sd label list-all` — free-form tagging, with normalization (lowercased, trimmed, deduped) on the way in.

Labels are the framework's only classification axis beyond `type` and `priority`, and they carry more weight than they first appear to. They are a filter on [[seeds-list]], [[seeds-ready]] and [[seeds-search]] (including `--label-any` and `--unlabeled`); a plan step may declare `labels: [...]` that flow to the spawned child seed — merged **additively** into an adopted seed's existing labels, never clobbering them; and they are one of the inputs [[seeds-plan-prompt]] uses to infer which mulch domain to mine prior art from.

Maps to **no canonical SDLC stage** — metadata maintenance.

## See Also
- [[seeds-plan-submit]] — propagates step labels onto spawned and adopted children.
- [[seeds-plan-prompt]] — reads labels for mulch domain inference.
- [[seeds-list]] · [[seeds-ready]] — where labels are consumed as filters.
