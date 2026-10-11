---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026); pi.dev (Earendil, 2026); Agent OS — Builder Methods (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-10-11
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

Seeds — the pattern inverted, because the framework is a program rather than a prompt bundle:

- [[seeds-prime]] — the tool emits its own rules and command reference into the agent's context on request (`--compact`, or `--json` for typed sections a harness can place deliberately); an agent cannot read a CLI the way it reads a `SKILL.md`.
- [[seeds-onboard]] — the persistent counterpart: writes the seeds section into `CLAUDE.md` / `AGENTS.md` once, so every later session starts primed.
- [[seeds-list]] · [[seeds-ready]] — five renderings of one query (`markdown`, `compact`, `plain`, `ids`, `json`) so the caller pays only for the tokens it needs; `ids` makes the tracker a shell filter rather than prose to parse.

Beads — a ~109-command store that budgets its own footprint:

- [[beads-prime]] — measures whether an MCP server is present and charges ~50 tokens instead of ~1–2k; `--memories-only` for mid-session compaction hooks.
- [[beads-compact]] — semantic "memory decay" summarizes old closed beads specifically *"to save context window"*.
- [[beads-list]] — every read command narrows (filters, limits, `--json`), because with a store this large what an agent pulls in is a budget decision.
- [[beads-setup]] · [[beads-rules]] — write into and then mechanically *compact* the harness's guide layer, merging near-duplicate rules above a similarity threshold.

pstack — enforced at every fan-out boundary, and stated as a principle:

- [[pstack-principle-guard-the-context-window]] — route bulk to subagents, keep summaries in the main thread, not raw payloads.
- [[pstack-how]] — raw exploration stays in the explorers; only findings reach the explainer.
- [[pstack-recall]] — *"the raw transcripts stay in the subagents. the main thread gets only their findings."*
- [[pstack-swarm]] — ***do not paste raw worker dumps***; the parent returns a compact table, one-line evidenced issues, and explicit gaps.
- [[pstack-poteto-mode]] — every `Task` call defaults to file pointers rather than inlined context.

Tessl — context budgeting as product architecture rather than as advice:

- [[tessl-install]] · [[tessl-plugin]] — the **two kinds of context** model: *rules* apply always (team standards on every task), *skills* load when relevant (procedural workflows matched by description). What loads when is a property of the packaging.
- [[tessl-mcp]] — installed context reaches the agent as **MCP tools** rather than as files, which is what makes one capability portable across seven harnesses.
- [[tessl-init]] — writes the rules files and MCP entries into each detected agent.

builder-skills:

- [[builder-rewind]] — find the right moment coarse to fine, then read only the smallest relevant range of local screen memory.
- [[builder-quick-recap]] — installed as a managed `AGENTS.md` / `CLAUDE.md` block because *"this convention is only automatic when it is present in project or user instructions."*
- [[builder-visual-recap]] — summarizes a diff *"at a higher altitude than line-by-line review"* so the reviewer's attention goes to the change's overall shape first.

Matt Pocock — Skills for Real Engineers:

- [[mp-writing-for-agents]] — the toolkit's explicit theory of it: **context pointers** whose wording decides when material is reached, the **two loads** (context vs cognitive), progressive disclosure, leading words, and the environment as a source of truth that docs should not cache (v1.2.0).
- [[mp-implement-spec]] — subagent communication by context pointers to spec, tickets, research notes and commits, never restated content (v1.3.0).
- [[mp-retro]] — keeps `CLAUDE.md`/`AGENTS.md` to navigation pointers and moves rules to review-time standards or checks (v1.3.0).
- [[mp-wait-what]] — a three-line skill steered entirely by one leading word (v1.2.0).

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) decides what is in the window when an agent is spawned, and what crosses between agents:

- [[sssf]] (library) — context crosses a seam **in code, not in conversation**. An agent has exactly two output channels (files in the session's shared `context_handoff/`, and one final JSON envelope), and the runtime — not the model — persists that envelope and injects it into the next agent's rendered prompt as `{{previous_envelope}}`. A failing test's output rides back inside the envelope with a bounded tail (`TAIL_CHARS`) *"so a runaway stack trace can't swamp the next agent's context"*, and the *"a known command is code, not an agent"* rule is partly a context argument: running the suite in a `kind="code"` phase keeps a passing test suite out of the window entirely, which *"buys you nothing at all."* Occupancy is measured rather than assumed — `context_tokens` / `context_window` is recorded per agent session, computed the way [[pi]] computes it for its own auto-compaction trigger. Its operator skill applies the discipline to itself: nine cookbooks lazy-loaded one per request, with a stated ban on surveying state before the request arrives (*"Volunteered state is guessed state… It is stale on arrival"*).

## Provided by (harness)

The [harness layer](../harness/index.md) supplies the context-assembly machinery these skills configure — what actually loads into the window at each turn:

- [[claude-code]] — **`CLAUDE.md`** (project + `~/.claude/CLAUDE.md` global) loaded every session as standing instructions, a **file-based persistent memory** (`/memory`), **MCP** resource/tool loading (deferred until needed), and **description-triggered skill loading** — the primitive under [[addy-context-engineering]]'s rules-files-and-MCP and gstack's CLAUDE.md search guidance.
- [[opencode]] — **`AGENTS.md`** project config + configurable skills/rules + **MCP** assemble per-turn context.
- [[pi]] — **`AGENTS.md` + `SYSTEM.md`** loaded from `~/.pi/agent/`, parent dirs, and cwd, plus skills and customizable **compaction** summarization.
- [[factory-droid]] — **`AGENTS.md`** (shared standard, `CLAUDE.md`-compatible; discovery walks to the git root plus `~/.factory/` personal defaults) + skills + **40+ MCP servers** + plugins assemble per-turn context.

## Persisted by (store)

- [[beads]] — the store measures and manages its *own* context cost, which no other layer here does. [[beads-prime]] detects whether an MCP server already describes the tools and emits ~50 tokens instead of ~1–2k; [[beads-compact]] semantically decays old closed work *"to save context window"*; [[beads-mol]]'s wisps are born deletable so operational runs never accumulate.
- [[seeds]] — five output formats over one query, and `sd prime --compact`, so the caller pays only for what it needs ([[seeds-list]], [[seeds-prime]]).

The state-side insight is that a store that never forgets eventually costs more context than it saves, so forgetting has to be designed. Beads is the only tool in the wiki that treats that as a first-class problem.

## Supplied by (registry)

- [[tessl]] — the supply-side realization: **what loads, and when, becomes a packaging decision**. Rules ship as always-on, skills ship as description-matched, and both travel in a versioned bundle that also carries MCP servers and hooks. [[tessl-observability]] then closes the loop by measuring which ones actually *activate* in real sessions, which is the only way to find context that is installed everywhere and firing nowhere.

## See Also
- [[pattern-fresh-context-subagents]] — resetting context per task; the story file is what makes a fresh dev context safe.
- [[pattern-source-grounding]] — one high-value thing to put *into* context: cited docs.
- [[topic-harness-engineering]] — this pattern is the delivery mechanism for the *guide (feedforward)* layer.
- [[artifact-standards]] — Agent OS's injected convention corpus.
- [[claude-code]] · [[opencode]] · [[pi]] · [[factory-droid]] — the harnesses whose context files + skills + (compaction/MCP) assemble the context.
