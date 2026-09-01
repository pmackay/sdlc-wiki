---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd close

`sd close <id> [<id2> …] --reason <text>` — close one or more issues, stamping `closedAt` and storing `closeReason`.

The `--reason` is the interesting field. It is free text, unvalidated, and the repo's own convention is to make it evidential rather than declarative — *"Fixed; covered by store.test.ts"*, *"Implemented with exponential backoff"* — so the closed seed carries a pointer to what makes the claim checkable. That is a weak, convention-only instance of [[pattern-evidence-before-claims]]: nothing enforces it, unlike [[bernstein]]'s janitor, which *"does not trust agent claims—verifies them"*. It is recorded here because the field exists and the framework's docs consistently fill it that way, not because seeds gates on it.

Closing is also what unblocks: every seed listing this id in `blockedBy` becomes eligible for [[seeds-ready]] the moment this command returns.

Maps to **no canonical SDLC stage** — it records the end of work rather than performing any.

## See Also
- [[seeds-ready]] — the queue this command feeds by unblocking downstream seeds.
- [[seeds-sync]] — commits the close to git.
- [[seeds-plan-outcome]] — the plan-level counterpart, recorded once all children are closed.
- [[pattern-evidence-before-claims]] — the pattern `--reason` gestures at.
