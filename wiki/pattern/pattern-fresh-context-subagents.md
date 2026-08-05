---
type: pattern
sources: "Open GSD docs (2026); Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026)"
updated: 2026-07-31
---

# Pattern: Fresh-context subagents

Route heavy research and execution work through subagents that each start with a clean context window (GSD targets ~200k tokens per executor), while the main session stays lean. This directly counters **context rot** — quality degradation as a single agent's context window fills. Each subagent gets only "a precisely scoped prompt and the subset of artifacts it needs."

## Applied by (backlinks)

GSD:

- [[gsd-plan-phase]] — runs research/planning in fresh-context subagents.
- [[gsd-execute-phase]] — spawns a clean-context executor per task.
- [[gsd-phase-researcher]] — four parallel research instances.
- [[gsd-planner]] — plans in a fresh context, artifacts only.
- [[gsd-executor]] — implements in a clean ~200k-token context.

Addy Osmani — Agent Skills:

- [[addy-doubt-driven-development]] — spawns fresh-context subagents to double-check work.
- [[addy-code-reviewer]] — reviews in a clean context, artifacts only.
- [[addy-test-engineer]] — writes tests in an isolated context.
- [[addy-security-auditor]] — audits security in a fresh context.
- [[addy-web-performance-auditor]] — audits performance in a fresh context.

BMAD:

- [[bmad-dev-story]] — implements one story per fresh context, relying on the story file to carry everything it needs.
- [[bmad-create-story]] — makes the fresh dev context viable by front-loading all context into the story.
- [[bmad-code-review]] — reviews "in fresh context, ideally different LLM" than the one that wrote the code.

Compound Engineering:

- [[ce-code-review]] · [[ce-doc-review]] — stateless reviewer personas, one fresh context each.
- [[ce-compound]] — a research council of fresh-context sub-agents mines completed work.
- All 26 CE sub-agents run in a fresh context (e.g. [[ce-repo-profiler]], [[ce-security-sentinel]], [[ce-session-historian]], [[ce-spec-flow-analyzer]]).

gstack:

- [[gstack-spec]] — `--execute` spawns a fresh-worktree agent; the browser sidebar agent runs in an isolated session.

Superpowers (a foundational principle — *"they should never inherit your session's context or history — you construct exactly what they need"*):

- [[sp-subagent-driven-development]] — a fresh implementer subagent per task; a fresh reviewer per review; briefs and reports move as files, never pasted into the controller's context.
- [[sp-dispatching-parallel-agents]] — one fresh-context subagent per independent problem domain, dispatched concurrently.
- [[sp-requesting-code-review]] — the reviewer subagent gets precisely-crafted context, never the controller's session history.

## Provided by (harness)

The [harness layer](../harness/index.md) provides this pattern as a *primitive* — the sub-agent mechanism lives in the agent program itself, below any framework skill:

- [[claude-code]] — the **Agent / Task tool** spawns a sub-agent with its own fresh context window and a scoped toolset, returning only a final result to the caller; agent types are defined in `.claude/agents/*.md`, and several launched in one turn run concurrently. This is the harness affordance every fresh-context skill above is standing on.
- [[opencode]] — built-in **build / plan / explore / scout** agents plus background subagents, each with its own context and scoped tools.
- [[factory-droid]] — **Custom Droids** (Markdown+YAML in `.factory/droids/`), each with a fresh context window and its own session, model, tool policy, and autonomy level; delegated via the **Task** tool with `run_in_background` for concurrency.
- **Not [[pi]]** — pi's minimal core deliberately omits sub-agents (extension-only); a framework that needs them is not portable to pi without an extension. The clearest case of a pattern that is a harness primitive in some harnesses and absent from another.

## See Also
- [[pattern-wave-parallelism]] — how execution subagents are scheduled.
- [[pattern-worktree-isolation]] — the filesystem counterpart (isolate the files, not just the context).
- [[gsd]] · [[superpowers]] — context-engineering frameworks built on this pattern.
- [[claude-code]] · [[opencode]] · [[factory-droid]] — the harnesses whose sub-agent tools provide this as a primitive (pi omits it from core).
