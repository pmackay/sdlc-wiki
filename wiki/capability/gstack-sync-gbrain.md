---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /sync-gbrain

`/sync-gbrain` — keep gbrain current with this repo's code and refresh the agent's search guidance.
Registers the cwd as a federated source (`gbrain sources add`), runs `gbrain sync --strategy code`,
and writes a `## GBrain Search Guidance` block into the project's `CLAUDE.md` so the agent prefers
`gbrain search` / `code-def` / `code-refs` over Grep (auto-removed if the capability check fails).
`--incremental` (default) / `--full` / `--dry-run`; idempotent.

An **enabling** learn-stage capability that keeps the compounding memory ([[gstack-setup-gbrain]])
accurate and **engineers the context** by writing search guidance into CLAUDE.md
([[pattern-context-engineering]], [[pattern-knowledge-compounding]]).

## See Also
- [[gstack-setup-gbrain]] — stands up the brain this syncs.
- [[gstack-learn]] — the learnings layer this complements.
- [[stage-learn]] — the stage this enables.
