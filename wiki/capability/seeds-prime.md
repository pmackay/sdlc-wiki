---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]", "[[pattern-session-handoff]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd prime

`sd prime [--compact] [--json]` — emit the tracker's rules and command reference into the agent's context. `--json` returns typed `sections` so a harness can place them deliberately; `--compact` trims for a tighter budget.

It is step one of the framework's prescribed agent workflow — *"At session start run `sd prime` (and `ml prime` if mulch is the active context)"* — and the reason it exists is that seeds is a program, not a skill: an agent cannot read `sd`'s instructions the way it reads a `SKILL.md`, so the tool has to inject them itself. That inverts the usual direction of [[pattern-context-engineering]] in this wiki, where the framework's documents are loaded *into* the agent; here the framework hands over a rendered, versioned briefing on request, and `--compact` makes the cost of it a caller's decision.

Its [[pattern-session-handoff]] edge is the pairing with [[seeds-sync]]: state committed to git on one side, primed back into a fresh agent on the other. Where [[gstack-context-restore]] and [[mp-handoff]] reconstruct a *conversation*, `sd prime` restores the *queue* — a fresh agent needs no narrative, only the rules and what is ready.

Maps to **no canonical SDLC stage**; it is session bootstrap, filed alongside the wiki's other context-continuity capabilities.

## See Also
- [[seeds-onboard]] — the persistent counterpart: written into the memory file once, rather than emitted each session.
- [[seeds-ready]] — the query a primed agent runs next.
- [[gstack-context-restore]] · [[mp-handoff]] · [[sp-using-superpowers]] — session-bootstrap counterparts elsewhere.
