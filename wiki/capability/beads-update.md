---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-update]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd update

`bd update <id>` — the mutation surface, and the command an agent runs most after [[beads-ready]]. `--claim` atomically sets assignee and `in_progress` together; other flags set `--title`, `--description`, `--priority`, `--assignee`, `--design`, `--notes`, `--acceptance`, `--metadata`. It accepts several ids at once.

Six thin siblings are the same operation with a friendlier name, and live here: `bd assign` (shorthand for `--assignee`), `bd priority`, `bd note` (append rather than replace), `bd set-state` / `bd state` (operational state as an event plus a label, queryable per dimension), `bd promote` (turn a wisp into a permanent bead), and `bd defer` / `bd undefer` (put a bead on ice; deferred beads leave the ready frontier without being closed).

Two things the docs are emphatic about:

- **`bd edit` is a trap for agents.** It opens `$EDITOR`, which an agent cannot drive, and the docs say so in capitals in three places. Use `bd update` with flags, or pipe via `--description=-`.
- **Read the metadata before the prose.** Beads' schema boundary pushes orchestration-specific data into `metadata`, and by convention an orchestrator writes execution hints there: `execution_agent_type`, `execution_suggested_model`, `execution_reasoning_effort`, `execution_mode`, `execution_parallel_group`. The instruction to agents is to *"treat them as the authoritative execution hints"* and, for a parent spawning subagents, to read them **before** launching, *"because a running subagent cannot change its model or reasoning effort after launch."*

That second point is the charter's layering in miniature: beads stores the routing decision without making it. The orchestration layer owns *"model choice"*; the store just carries it, unvalidated, in the same way [[seeds-update]]'s `extensions` bag carries warren's scheduling state.

Maps to **no canonical SDLC stage** — recording that implementation is in progress is not implementing.

## See Also
- [[beads-ready]] — supplies the id, and can claim inline.
- [[beads-close]] — the terminal transition.
- [[beads-mol]] — where `promote` and the wisp lifecycle belong.
- [[seeds-update]] — the cross-store counterpart, including the same metadata-bag trick.
