---
type: harness
subtype: terminal
source_url: "https://github.com/earendil-works/pi"
enables: ["[[pattern-session-handoff]]", "[[pattern-context-engineering]]"]
sources: "pi.dev/docs + github.com/earendil-works/pi (Mario Zechner / Earendil Inc., formerly badlogic/pi-mono; MIT, 2026); disler/super-simple-software-factory (2026)"
raw: ["../../raw/harness/2026-07-31-pi.md"]
updated: 2026-08-31
---

# pi

**Harness layer** — the agent *program*, not a process framework and not an execution runtime. A [harness](index.md) loads a framework's skills/commands and drives the model's tool-call loop; it performs no [SDLC stage](../sdlc-stage/index.md) and connects to the ontology only through the execution primitives it `enables:` as patterns. Frameworks `runs_on:` it; runtimes `runs:` it.

**pi** (Mario Zechner / `badlogic`, libGDX's creator; now published by Earendil Inc., MIT) is the wiki's **minimal-core** terminal harness. Its signature is *what it deliberately leaves out*: the core ships **four tools** (read, write, edit, bash) and pushes everything else — sub-agents, MCP, permission prompts, plan mode, to-dos — into an opt-in **TypeScript extension** system. It is **model-agnostic** (Anthropic/OpenAI/Google/Groq/xAI/Ollama/Kimi/… via one LLM API, with mid-session model switching) and terminal-only (TUI + print/JSON + an RPC mode + an embeddable SDK; no first-party IDE/desktop/web GUI). It is the opposite pole from batteries-included harnesses like [[claude-code]] and [[opencode]].

## What it provides (a minimal core)

- **Four built-in tools** — read · write · edit · bash. That is the whole default toolset.
- **Skills & prompt templates** — **Skills** (capability packages under `~/.pi/agent/skills/`) invoked `/skill:name`; Markdown **prompt templates** invoked `/<template>`.
- **Context files** — `AGENTS.md` + `SYSTEM.md` loaded from `~/.pi/agent/`, parent dirs, and cwd; **context compaction** with customizable summarization.
- **Sessions** — **tree-structured, shareable, resumable** session history at `~/.pi/agent/sessions/`.
- **Model access** — model-agnostic via `@earendil-works/pi-ai`; mid-session switching.
- **Deliberately NOT in core** — sub-agents, MCP, permission popups, plan mode, background bash: all **excluded from core** and delivered only as TypeScript **extensions** or third-party packages. This is the design thesis, not a gap.

## Interaction surface

Terminal **TUI** (native), plus print/JSON modes, an **RPC** interface (JSON over stdin/stdout), and an embeddable **SDK**. No first-party IDE/desktop/web GUI — hence `subtype: terminal`.

## Harness profile

| Capability | pi |
|---|---|
| Skill / command format | **Skills** (`/skill:name`) · Markdown prompt templates · `AGENTS.md` + `SYSTEM.md` |
| Sub-agents | **not in core** — via extension only |
| MCP | **not in core** — via extension only |
| Hooks / extensibility | **TypeScript extension system** (the primary extensibility surface) + SDK; Rust impl exists |
| Permissions & guardrails | **not in core** — relies on containerization/sandboxing or extensions |
| Model access | **model-agnostic** — many providers; mid-session switching |
| Memory & context files | `AGENTS.md` + `SYSTEM.md`; context compaction (customizable summarization) |
| Interaction surface | terminal TUI · print/JSON · RPC · SDK (no GUI) |
| Distribution / license | Earendil Inc. (Zechner), **MIT / open source**; npm `@earendil-works/pi-coding-agent` |

## Distinctive contribution

pi is the **minimalist pole** of the harness layer and the clearest evidence that *"harness primitive"* is a real, variable property rather than a given. Where [[claude-code]] and [[opencode]] both provide sub-agents and mutation guardrails as first-class primitives, **pi provides neither in core** — so [[pattern-fresh-context-subagents]] and [[pattern-edit-guardrails]] have *no* harness-side entry for pi, even though a framework that assumes them can still run on pi via extensions. A framework's portability to pi therefore depends on whether it needs a primitive pi omits: this is exactly the cross-harness question the `harness` layer exists to make visible. (It is the harness-layer analogue of [[nano-spec]]'s minimalism in the process layer.)

## Patterns provided

Only the two primitives pi keeps in its core qualify — a deliberately short roster:

- [[pattern-session-handoff]] — tree-structured, resumable, shareable sessions plus context compaction carry working context across a boundary *at the harness level*; arguably pi's signature.
- [[pattern-context-engineering]] — `AGENTS.md` + `SYSTEM.md` + skills + customizable compaction assemble the right context per turn.

It does **not** provide [[pattern-fresh-context-subagents]] or [[pattern-edit-guardrails]] as core primitives (extension territory) — the one harness here that omits them.

## Runs / spawned by (backlinks)

- **Frameworks that `runs_on:` it** — [[compound-engineering]] · [[superpowers]] (both officially name Pi among supported agents).
- **Stores that `integrates_with:` it** — [[seeds]], evidenced by the `.pi/` session store its repo dogfoods; both seeds and pi are also in [[warren]]'s built-in agent set. [[beads]] does **not** name pi among its thirteen `bd setup` recipes, so no edge — the one paged harness the larger store misses.
- **Runtimes that `runs:` it** — [[sandcastle]] (agent provider) · [[warren]] (harness option, `claude-code`/`sapling`/`pi`) · [[bernstein]] (the `pi` adapter, `@mariozechner/pi-coding-agent`) · [[sssf]] (**pi only** — the one runtime here that targets pi *exclusively*: `coding_agent: claude_code` is schema-valid and its interface raises `NotImplementedError` until v2) · [[gh-aw]] (the `pi` engine, production-status alongside copilot/claude/codex/gemini — Copilot auth by default, provider keys for prefixed models, and the one engine with an `engine.extensions:` plugin surface).

sssf is worth reading as an argument about *why* a minimal harness is the right worker for an orchestrated pipeline. It leans on three pi properties in particular: `--session-id` is create-or-continue, so re-prompting a live agent with a correction and starting one are the same call; the JSONL stdout stream can be tailed line by line into a trace database while the agent is still working; and `-e <path>` loads a per-agent extension, which is where sssf puts its `harness_engineering:` config key — one pi extension set per role. The same page also records the one place a minimal harness costs it: with no built-in permission surface (pi omits [[pattern-edit-guardrails]] from core), sssf has to enforce write boundaries itself, after the fact, by diffing the repo around every call.

## See Also
- [[claude-code]] · [[opencode]] — the batteries-included terminal harnesses pi is defined against (proprietary/Anthropic vs open/model-agnostic vs pi's minimal core). Cross-harness comparison: [harness/index.md](index.md).
- [[sandcastle]] · [[warren]] · [[bernstein]] · [[sssf]] · [[gh-aw]] — the runtimes that spawn this harness; sssf spawns nothing else.
- [[pattern-session-handoff]] · [[pattern-context-engineering]] — the two patterns pi provides as core primitives.
- [[nano-spec]] — the process-layer minimalist, pi's spiritual counterpart one layer up.
