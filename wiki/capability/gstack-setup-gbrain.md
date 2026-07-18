---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /setup-gbrain

`/setup-gbrain` — **GBrain onboarding**: from zero to a running persistent knowledge base in under 5
minutes. Four paths — PGLite local (zero accounts), Supabase existing URL, Supabase auto-provision
(via Management API), or remote gbrain MCP. Registers gbrain as an MCP server for Claude Code and
captures a per-repo **trust triad** (read-write / read-only / deny). [GBrain](https://github.com/garrytan/gbrain)
is "the memory your agent actually keeps between sessions."

An **enabling** capability for the learn stage: it stands up the persistent-memory substrate that
[[gstack-learn]] and [[gstack-sync-gbrain]] write into and future sessions read ([[pattern-knowledge-compounding]]).
Cross-machine memory sync means learnings follow you across machines.

## See Also
- [[gstack-sync-gbrain]] — keeps the brain current with repo code.
- [[gstack-learn]] — the cross-session learnings this memory backs.
- [[stage-learn]] — the stage this enables.
