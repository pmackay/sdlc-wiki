---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd todo

`bd todo add|list|done` — *"manage TODO items as lightweight task issues"*, and the docs are refreshingly explicit that it is nothing but sugar:

```
bd todo add "Title"   ->  bd create "Title" -t task -p 2
bd todo               ->  bd list --type task --status open
bd todo done <id>     ->  bd close <id>
```

It exists to win an argument the README states directly: *"Do not use markdown TODO lists for task tracking."* The friction of `bd create -t task -p 2` versus jotting a `- [ ]` line in a file is exactly the friction that sends an agent back to markdown, so beads made the tracked version as cheap to type as the untracked one. *"TODOs can be promoted to full issues by changing type or priority"* — the throwaway and the tracked item are the same object, so nothing needs migrating when a TODO turns out to matter.

That is a store-layer answer to a documented failure mode: markdown plans rot, TODO comments scatter, and neither survives the session.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-create]] — what it wraps.
- [[beads-mol]] — wisps, the same throwaway-vs-durable question at workflow scale.
- [[beads-remember]] — the same argument applied to `MEMORY.md`.
