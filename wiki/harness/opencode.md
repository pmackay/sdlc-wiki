---
type: harness
subtype: terminal
source_url: "https://github.com/anomalyco/opencode"
enables: ["[[pattern-fresh-context-subagents]]", "[[pattern-edit-guardrails]]", "[[pattern-session-handoff]]", "[[pattern-context-engineering]]"]
sources: "opencode.ai/docs + github.com/anomalyco/opencode (formerly sst/opencode; Anomaly, MIT, 2026)"
raw: ["../../raw/harness/2026-07-31-opencode.md"]
updated: 2026-07-31
---

# opencode

**Harness layer** — the agent *program*, not a process framework and not an execution runtime. A [harness](index.md) loads a framework's skills/commands and drives the model's tool-call loop; it performs no [SDLC stage](../sdlc-stage/index.md) and connects to the ontology only through the execution primitives it `enables:` as patterns. Frameworks `runs_on:` it; runtimes `runs:` it.

**opencode** (Anomaly — the team formerly SST/Serverless Stack; MIT, open source) is a terminal-first AI coding harness whose defining trait is **model-agnosticism**: unlike [[claude-code]] (Anthropic models only), it drives Claude, GPT, Gemini, Bedrock, Azure, Groq, OpenRouter, and its own curated "**OpenCode Zen**" model set behind one agent. It is otherwise **batteries-included** — first-class sub-agents, MCP, a native plugin+hook system, plan/build modes, and a permissions framework — making it, alongside Claude Code, one of the two full-primitive terminal harnesses here (and the opposite pole from [[pi]]'s minimal core). It ships a TUI (native), a desktop app, and an IDE extension.

## What it provides (primitives, not process)

- **Sub-agents** — built-in **build** (full tool access) and **plan** (read-only) agents, plus General / Explore / a Scout research agent, and background subagents.
- **MCP** — MCP servers supported.
- **Hooks** — a native plugin hook system (`tool.execute.before` / `.after`, `session.idle`, …) that can intercept, block, or modify tool calls.
- **Slash-commands & skills** — custom commands; configurable "skills," rules, and custom tools; **AGENTS.md** for project config.
- **Permissions & plan mode** — a permissions/policies framework (e.g. the plan agent set to "ask" before edits/bash); Plan vs Build modes.
- **Session persistence** — session management with undo/redo and shareable web links.
- **Model access** — multi-provider (Anthropic/OpenAI/Google/Bedrock/Azure/Groq/OpenRouter/…) + OpenCode Zen.

## Interaction surface

Terminal **TUI** (native), a **desktop app** (beta), and an **IDE extension**; sessions shareable via web links. Native surface is the terminal — hence `subtype: terminal`.

## Harness profile

| Capability | opencode |
|---|---|
| Skill / command format | `AGENTS.md` · custom slash-commands · configurable skills · custom tools |
| Sub-agents | **first-class** — build / plan / explore / scout + background subagents |
| MCP | **yes** |
| Hooks / extensibility | **native plugin + hook system**; SDK; community registry |
| Permissions & guardrails | permissions/policies framework + Plan vs Build modes |
| Model access | **model-agnostic** — many providers + OpenCode Zen curated set |
| Memory & context files | `AGENTS.md`; session undo/redo + shareable state |
| Interaction surface | terminal TUI (primary) · desktop app · IDE extension |
| Distribution / license | Anomaly (ex-SST), **MIT / open source** |

## Distinctive contribution

opencode is the wiki's **model-agnostic, open-source** terminal harness — the demonstration that the full primitive set ([[pattern-fresh-context-subagents]], [[pattern-edit-guardrails]], [[pattern-session-handoff]], [[pattern-context-engineering]]) is not unique to Claude Code, and that a framework's skills can run on the same primitives against *any* model provider. Its native plugin+hook system and multi-surface reach (TUI/desktop/IDE) make it the batteries-included counterpart to [[pi]]'s deliberately minimal core, and the open counterpart to [[claude-code]]'s Anthropic-hosted one.

## Patterns provided

- [[pattern-fresh-context-subagents]] — the build/plan/explore/scout agents (and background subagents) each run with their own context and scoped tools.
- [[pattern-edit-guardrails]] — the permissions/policies framework + the read-only plan agent + hooks that can block a tool call are the mutation-gating substrate.
- [[pattern-session-handoff]] — session management with undo/redo, resume, and shareable links carries working context across a boundary.
- [[pattern-context-engineering]] — `AGENTS.md` + configurable skills + MCP assemble the right context per turn.

## Runs / spawned by (backlinks)

- **Frameworks that `runs_on:` it** — [[gsd]] · [[addy-agent-skills]] · [[compound-engineering]] · [[gstack]] · [[nano-spec]] · [[superpowers]] (each officially names OpenCode among supported agents).
- **Runtimes that `runs:` it** — [[sandcastle]] (agent provider).

## See Also
- [[claude-code]] · [[pi]] — the other terminal harnesses; claude-code is the proprietary/Anthropic-models pole, pi the minimal-core pole, opencode the model-agnostic/batteries-included pole. Cross-harness comparison: [harness/index.md](index.md).
- [[sandcastle]] — the runtime that spawns this harness.
- [[pattern-fresh-context-subagents]] · [[pattern-edit-guardrails]] · [[pattern-session-handoff]] · [[pattern-context-engineering]] — the patterns it provides as primitives.
