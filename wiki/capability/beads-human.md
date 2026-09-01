---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd human

`bd human list|respond|dismiss|stats` — **the queue of things that need a person**, and one of the more quietly original ideas in this wiki.

An issue labelled `human` is one an agent has escalated. `bd human list` shows the pending set, `bd human respond <id> --response "Use OAuth2"` records the answer as a comment and closes the bead, `bd human dismiss` closes it unanswered with a reason, and `bd human stats` reports total / pending / responded / dismissed.

Every other tool here handles "I need a decision" by *writing it into the conversation* — an agent asks, and if nobody is watching the terminal, the question is gone with the session. Beads makes the question **durable, queryable, and countable**: it survives the agent that asked, it can be answered hours later by someone who was never in that session, and the answer lands back on the work item where the next agent will read it. Paired with a `human`-type [[beads-gate]], the blocked step also leaves the ready frontier until the person replies, so nothing spins waiting.

Two things follow that are worth stating. **`bd human stats` measures the human bottleneck** — a pending count is a queue depth, and a dismissal rate says something about whether agents are escalating well. And this is the store-layer form of human-in-the-loop, distinct from [[warren]]'s mid-run `steer` (interrupt a running agent) — asynchronous rather than real-time, which is what unattended work actually needs.

Bare `bd human` does something else entirely: it prints the ~15 essential commands *"that human users need most often"*, because *"bd has 70+ commands — many for AI agents, integrations, and advanced workflows."* A tool built for agents, with a smaller door for people.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-gate]] — the `human` gate type that blocks on these.
- [[beads-comment]] — where a response is recorded.
- [[warren]] — real-time steering, the synchronous alternative.
- [[beads-label]] — the `human` label this queries.
