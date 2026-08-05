---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026); pi.dev (Earendil, 2026); Agent OS — Builder Methods (2026)"
updated: 2026-08-05
---

# Pattern: Context engineering (right context, right time)

Deliberately curate what an agent sees: rules files, packed context, and MCP integrations that supply the relevant code, types, and conventions at the moment they are needed — no more, no less. Treats the context window as a managed resource rather than a dumping ground, so output quality stays high and degradation (drift, forgotten constraints) is caught and reset.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-context-engineering]] — rules files, context packing, MCP integrations.

BMAD:

- [[bmad-create-story]] — front-loads "all the context the agent will need" into the [[artifact-story|story file]].
- [[bmad-dev-story]] — implements from that self-contained context, so it can run fresh.
- [[bmad-prd]] — maintains a `.memlog.md` append-only decision/audit trail as durable run context.

A second framework promotes this from an Addy-only technique to a **two-framework** pattern. Addy curates context *at invocation* (rules files, packing, MCP); BMAD engineers it *into the work unit* — the story file, `project-context.md`, and `.memlog.md` carry the context forward so each agent starts fully briefed. Context engineering is arguably BMAD's organizing principle.

Compound Engineering:

- [[ce-plan]] · [[ce-brainstorm]] — read the `docs/solutions/` compound corpus + repo profile as grounding.
- [[ce-repo-profiler]] (cached project profile) · [[ce-git-history-analyzer]] (temporal context) · [[ce-learnings-researcher]] (past lessons) — the grounding scouts that engineer context into a work unit.

gstack:

- [[gstack-sync-gbrain]] — writes a GBrain search-guidance block into CLAUDE.md so the agent prefers the right context tools.
- [[gstack-learn]] — cross-session learnings fed back into new work.

Agent OS — the framework built almost entirely *around* this pattern:

- [[agent-os-inject-standards]] — the purest realization: deploy only the standards the current task needs, choosing file-reference vs embedded-snapshot payloads — *right context, right time* made an explicit, invocable act.
- [[agent-os-index-standards]] — the `index.yml` one-line-description **matcher** that lets standards be loaded selectively instead of all-at-once (*"Every word costs tokens"*), the mechanism that keeps the guide layer from becoming context rot.
- [[agent-os-discover-standards]] — authors the standard files this curates. See [[artifact-standards]].

## Provided by (harness)

The [harness layer](../harness/index.md) supplies the context-assembly machinery these skills configure — what actually loads into the window at each turn:

- [[claude-code]] — **`CLAUDE.md`** (project + `~/.claude/CLAUDE.md` global) loaded every session as standing instructions, a **file-based persistent memory** (`/memory`), **MCP** resource/tool loading (deferred until needed), and **description-triggered skill loading** — the primitive under [[addy-context-engineering]]'s rules-files-and-MCP and gstack's CLAUDE.md search guidance.
- [[opencode]] — **`AGENTS.md`** project config + configurable skills/rules + **MCP** assemble per-turn context.
- [[pi]] — **`AGENTS.md` + `SYSTEM.md`** loaded from `~/.pi/agent/`, parent dirs, and cwd, plus skills and customizable **compaction** summarization.
- [[factory-droid]] — **`AGENTS.md`** (shared standard, `CLAUDE.md`-compatible; discovery walks to the git root plus `~/.factory/` personal defaults) + skills + **40+ MCP servers** + plugins assemble per-turn context.

## See Also
- [[pattern-fresh-context-subagents]] — resetting context per task; the story file is what makes a fresh dev context safe.
- [[pattern-source-grounding]] — one high-value thing to put *into* context: cited docs.
- [[topic-harness-engineering]] — this pattern is the delivery mechanism for the *guide (feedforward)* layer.
- [[artifact-standards]] — Agent OS's injected convention corpus.
- [[claude-code]] · [[opencode]] · [[pi]] · [[factory-droid]] — the harnesses whose context files + skills + (compaction/MCP) assemble the context.
