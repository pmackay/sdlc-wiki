---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd kv

`bd kv set|get|list|clear` — a plain key-value store inside the beads database.

It is the least glamorous capability on this page and a genuinely revealing one. Once a project has a durable, synced, versioned store that every agent can reach, agents will want to keep things in it that are neither work items nor insights — a cursor into a long migration, a cached lookup, a flag that a one-off has already run. Without `bd kv` that state goes back into ad-hoc files, which is the failure mode the whole tool exists to eliminate.

Where [[beads-remember]] is for prose an agent should be *reminded of*, `kv` is for values an agent should *look up*. Nothing is injected at prime time; nothing is interpreted.

Beads' own charter suggests the boundary to respect: per-issue orchestration data belongs in issue `metadata`, and only project-wide state belongs here.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-remember]] — the primed, prose counterpart.
- [[beads-update]] — `--metadata`, for per-issue state instead of project-wide.
- [[beads-config]] — for configuration, as opposed to data.
