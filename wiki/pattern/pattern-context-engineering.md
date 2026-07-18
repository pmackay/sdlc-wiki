---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026)"
updated: 2026-07-05
---

# Pattern: Context engineering (right context, right time)

Deliberately curate what an agent sees: rules files, packed context, and MCP integrations that
supply the relevant code, types, and conventions at the moment they are needed — no more, no
less. Treats the context window as a managed resource rather than a dumping ground, so output
quality stays high and degradation (drift, forgotten constraints) is caught and reset.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-context-engineering]] — rules files, context packing, MCP integrations.

BMAD:

- [[bmad-create-story]] — front-loads "all the context the agent will need" into the [[artifact-story|story file]].
- [[bmad-dev-story]] — implements from that self-contained context, so it can run fresh.
- [[bmad-prd]] — maintains a `.memlog.md` append-only decision/audit trail as durable run context.

A second framework promotes this from an Addy-only technique to a **two-framework** pattern.
Addy curates context *at invocation* (rules files, packing, MCP); BMAD engineers it *into the
work unit* — the story file, `project-context.md`, and `.memlog.md` carry the context forward so
each agent starts fully briefed. Context engineering is arguably BMAD's organizing principle.

Compound Engineering:

- [[ce-plan]] · [[ce-brainstorm]] — read the `docs/solutions/` compound corpus + repo profile as grounding.
- [[ce-repo-profiler]] (cached project profile) · [[ce-git-history-analyzer]] (temporal context) · [[ce-learnings-researcher]] (past lessons) — the grounding scouts that engineer context into a work unit.

gstack:

- [[gstack-sync-gbrain]] — writes a GBrain search-guidance block into CLAUDE.md so the agent prefers the right context tools.
- [[gstack-learn]] — cross-session learnings fed back into new work.

## See Also
- [[pattern-fresh-context-subagents]] — resetting context per task; the story file is what makes a fresh dev context safe.
- [[pattern-source-grounding]] — one high-value thing to put *into* context: cited docs.
