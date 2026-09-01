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

# bd comment

`bd comment <id> "text"` and `bd comments <id>` — threaded discussion attached to a bead, with `--thread` for reply structure.

Two details make this more than a comment box. First, **authorship is recorded in the events journal**: the `actor` column is stamped inside the mutating transaction, and *"on a `comment` row it is the comment's author"* — so a multi-agent database can answer "which agent said this?" rather than just "what was said". Second, comments are the payload of the messaging surface: a `message`-type bead with threading, an ephemeral lifecycle, and delegation via [[beads-mail]] turns the comment mechanism into agent-to-agent correspondence.

This is where a store starts to absorb something the process frameworks do in prose. [[mp-handoff]] compacts a conversation into a document; beads keeps the conversation attached to the work item it is about, permanently and per-actor.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-mail]] — messaging built on the same substrate.
- [[beads-supersede]] — `replies-to`, the threading edge.
- [[beads-human]] — the comment channel reserved for people.
