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

# bd mail

`bd mail [subcommand]` — delegate mail operations to an external provider configured via `BEADS_MAIL_DELEGATE` or `bd config set mail.delegate "gt mail"`.

The docstring is the most candid statement of the layer boundary anywhere in beads, and it is worth quoting in full:

> Agents often type `bd mail` when working with beads, but mail functionality **is typically provided by the orchestrator**. This command bridges that gap by delegating to the configured mail provider.

So `bd mail` exists because agents *reach for it* — a UX bug report turned into a shim. Rather than build messaging (which the charter would forbid: cross-system coordination is the orchestration layer's) beads forwards the whole subcommand to whatever the orchestrator provides. That is a store declining to grow into a runtime, in one command.

Beads does have a real messaging substrate, though, and it is built from tracker primitives rather than a message bus: a **`message` issue type** with threading (`--thread`), an ephemeral lifecycle, and the `replies-to` knowledge link ([[beads-supersede]]). Agent-to-agent correspondence as beads that expire — which fits the layer, because a message is state, and delivery is somebody else's problem.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-comment]] — the threading and authorship mechanism messages ride on.
- [[beads-human]] — the durable channel to a person, which beads *does* own.
- [[warren]] — an orchestrator of the kind this delegates to.
