---
type: index
updated: 2026-08-05
---

# Harness — the agent-program layer

The `framework` / `capability` / `sdlc-stage` triad models the **process layer** — *what* an agent does across the lifecycle. This namespace models the **harness** — the agent *program* itself: the loop that loads a framework's skills/commands, assembles context, calls the model, executes the model's tool calls under a permission/hook policy, spawns sub-agents, and returns a result. Claude Code, pi, OpenCode, Codex, Cursor, and Copilot are harnesses.

A harness is neither a **framework** (it ships no SDLC methodology — it *loads* one) nor a **runtime** (it doesn't sandbox/parallelize/AFK agents — a runtime does that *to* it). It is the pivot both other layers were already defined against: frameworks are *"cross-harness"* and runtimes are *"harness-agnostic"*, and both phrases mean *"…across these harnesses."* Making it a node turns those into stored edges — `framework --runs_on--> harness` and `runtime --runs--> harness` — and it connects to the rest of the wiki at one seam: the `pattern` namespace, via `enables:` (the execution primitives capabilities build on). See [CONVENTIONS §The harness layer](../CONVENTIONS.md#the-harness-layer).

## Members

| Harness | Subtype | One-liner |
|---------|---------|-----------|
| [claude-code](claude-code.md) | terminal | Anthropic's official agentic coding harness — tool-call loop + first-class sub-agents, skills, MCP, hooks, permission/plan modes; Anthropic models only. The **reference / batteries-included proprietary** pole; nearly every framework here runs on it. |
| [opencode](opencode.md) | terminal | Anomaly's (ex-SST) open-source, **model-agnostic** harness — same full primitive set (sub-agents, MCP, native hooks, plan/build, permissions) across many model providers + OpenCode Zen; TUI/desktop/IDE. The **open, model-agnostic** pole. |
| [pi](pi.md) | terminal | Zechner/Earendil's **minimal-core** harness — 4 built-in tools; sub-agents, MCP, permissions, plan mode all deliberately excluded from core → TypeScript extensions. Model-agnostic, terminal-only. The **minimalist** pole. |
| [factory-droid](factory-droid.md) | terminal | Factory.ai's terminal harness — full primitive set (Custom Droids, skills, 40+ MCP servers, hooks, plugins, autonomy levels) over the **AGENTS.md standard**, plus **multi-model routing** (Anthropic/OpenAI/Google/open-weight, mid-session swap, BYOK, free Droid Core) and **Missions** multi-agent orchestration. The **model-routing** pole. |

*Ingest queue (not yet paged, named as officially-supported by ≥1 framework/runtime):* **Codex** · **Cursor** · **GitHub Copilot** · **Gemini CLI** · **Kimi** · **Windsurf** · **Antigravity** · **sapling**.

## Harness profile (the synthesis axis)

The harness layer's analogue of the SDLC-stage synthesis: the dimensions harnesses are compared on are **execution capabilities**, not lifecycle stages. Held as this matrix (not their own node namespace) until the layer grows enough to warrant graduating them — see [CONVENTIONS](../CONVENTIONS.md#the-harness-layer).

| Capability | [[claude-code]] | [[opencode]] | [[pi]] | [[factory-droid]] |
|---|---|---|---|---|
| Skill / command format | `SKILL.md` · `.claude/commands/*` · plugins | `AGENTS.md` · custom commands · skills · custom tools | Skills (`/skill:name`) · prompt templates · `AGENTS.md`+`SYSTEM.md` | `AGENTS.md` (standard) · SKILL.md skills · slash-commands · plugins |
| Sub-agents | first-class (Agent/Task, fresh context, concurrent) | first-class (build/plan/explore/scout + background) | **not in core** — extension only | first-class (Custom Droids, fresh ctx + own session, per-droid model, Task/`run_in_background`) |
| MCP | yes (local + remote, deferred) | yes | **not in core** — extension only | yes — **40+ pre-configured** + OAuth |
| Hooks / extensibility | lifecycle hooks · plugins · Agent SDK | native plugin+hook system · SDK · registry | TypeScript extensions · SDK · Rust impl | lifecycle hooks · plugins (cmd/droid/skill/hook bundles) · Sessions API |
| Permissions & guardrails | modes (default/plan/acceptEdits/bypass) + plan mode | permissions/policies + Plan vs Build | **not in core** — sandbox/extension | autonomy levels off/low/medium/high (`--auto`) + read-only review + approval workflows |
| Model access | **Anthropic only**; Fast mode | **model-agnostic** — many providers + Zen | **model-agnostic** — many providers; mid-session switch | **multi-model routing** — Anthropic/OpenAI/Google/open-weight, mid-session, complexity-tiered, BYOK, free Droid Core |
| Memory & context files | `CLAUDE.md` + memory · auto-compaction | `AGENTS.md` · session undo/redo | `AGENTS.md`+`SYSTEM.md` · compaction | `AGENTS.md` (git-root discovery + `~/.factory/`) |
| Interaction surface | terminal · desktop · web · VS Code/JetBrains | terminal TUI · desktop · IDE ext | terminal TUI · print/JSON · RPC · SDK | terminal TUI · headless `droid exec` (CI) · IDE · web · Sessions API |
| Distribution / license | Anthropic, **proprietary** | Anomaly, **MIT** | Earendil, **MIT** | Factory.ai, **proprietary** (free Droid Core tier) |

The comparison is the point of the layer. Two axes stand out: **model access** and **primitive completeness**. On model access the four now span a full spectrum — Claude Code is Anthropic-only, opencode and pi are provider-neutral, and **Factory Droid** pushes furthest by making *routing between models* (frontier + open-weight, mid-session, complexity-tiered, BYOK) a first-class feature rather than a config choice. On primitive completeness, Claude Code, opencode, and Factory Droid all ship sub-agents/MCP/permissions as core (Droid's set maps almost 1:1 onto Claude Code's), while **pi deliberately omits all three** — the property that decides whether a framework assuming those primitives is portable to pi without extensions. These axes, not SDLC stages, are the harness-layer synthesis.

## Patterns this layer supplies

The harness layer touches the wiki only through the patterns it `enables:` — each gains a **harness-side** roster alongside the process-side (capabilities that `apply` it) and infra-side (runtimes that `enable` it) rosters:

- [[pattern-fresh-context-subagents]] — claude-code (Agent/Task tool) · opencode (build/plan/explore/scout) · factory-droid (Custom Droids + Task/`run_in_background`) — **not pi** (extension only)
- [[pattern-edit-guardrails]] — claude-code (hooks + permission modes) · opencode (permissions/policies + plan-ask + hooks) · factory-droid (autonomy levels + hooks + approval workflows) — **not pi** (extension only)
- [[pattern-session-handoff]] — claude-code (compaction + resume) · opencode (session mgmt/undo/resume) · pi (tree-structured resumable sessions + compaction) · factory-droid (own-session subagents + Sessions API + headless `droid exec`)
- [[pattern-context-engineering]] — claude-code (`CLAUDE.md` + memory + MCP) · opencode (`AGENTS.md` + skills + MCP) · pi (`AGENTS.md`+`SYSTEM.md` + skills + compaction) · factory-droid (`AGENTS.md` standard + skills + 40+ MCP + plugins)

The two patterns pi omits are the layer's sharpest finding: a pattern can be a first-class *harness primitive* in one harness and entirely absent from another's core — which is precisely the cross-harness portability signal capabilities alone can't express.

## Framework support (the `runs_on:` inverse)

Which harnesses each framework **officially documents** support for (its own docs' claim — not "could run there"). **Bold** = has a page (a stored `runs_on:` edge points here); plain = officially supported but not yet paged (prose-only per the [support-scope rule](../CONVENTIONS.md#the-harness-layer)). This matrix is the central home for the full support data; the stored edges cover only the paged subset.

| Framework | Officially-supported harnesses |
|---|---|
| [[gsd]] | **claude-code** · **opencode** · Gemini CLI · Kimi CLI · Kilo · Codex · Copilot · Cursor · Windsurf |
| [[matt-pocock-skills]] | **claude-code** *(only one named; soft "any agent" claim)* |
| [[addy-agent-skills]] | **claude-code** · **opencode** · Cursor · Gemini CLI · Antigravity · Windsurf · Copilot · Kiro · Codex |
| [[openspec]] | **claude-code** · Copilot · Cursor · Windsurf · Kimi CLI · Trae *(claims "30+")* |
| [[speckit]] | **claude-code** · Copilot · Gemini CLI · Qwen Code · Codex CLI *(claims "30+")* |
| [[bmad]] | **claude-code** · Cursor · Copilot *(+ Gemini Gems / ChatGPT GPTs = planning surfaces, not harnesses)* |
| [[compound-engineering]] | **claude-code** · **opencode** · **pi** · **factory-droid** · Cursor · Codex · Kimi · Copilot · Qwen · Antigravity |
| [[gstack]] | **claude-code** · **opencode** · **factory-droid** · Codex CLI · Cursor · Slate · Kiro · Hermes · GBrain *(Claude-Code-native)* |
| [[bm-skills]] | **claude-code** *(Claude Code plugin marketplace; emits `AGENTS.md`/`CLAUDE.md` for others)* |
| [[superpowers]] | **claude-code** · **opencode** · **pi** · **factory-droid** · Antigravity · Codex (App/CLI) · Cursor · Copilot CLI · Kimi Code |
| [[nano-spec]] | **claude-code** · **opencode** · Codex · Gemini CLI · Antigravity · Cline · Cursor · Windsurf · Trae · Copilot |
| [[agent-os]] | **claude-code** *(primary — slash commands)* · Cursor · Windsurf · Codex · Antigravity *("any AI assistant that reads markdown")* |

Claude Code is the universal target; **opencode** is the most broadly officially-supported *second* harness (6 frameworks); **factory-droid** is named by the three individual-author cross-harness frameworks ([[compound-engineering]], [[gstack]], [[superpowers]]); **pi** by two of them (Compound Engineering, Superpowers). Two frameworks are effectively Claude-Code-only in what they name: [[bm-skills]] (a CC plugin marketplace) and [[matt-pocock-skills]] (soft "any agent" claim, no others named).

## The broader category

Four documented instances are the start, not the extent. The same layer includes the other **terminal** harnesses named across the frameworks/runtimes above — OpenAI's **Codex** CLI, **Cursor** (also IDE), GitHub **Copilot** CLI, Google's **Gemini CLI**, **Kimi**, **Qwen Code**, **Antigravity**, **Windsurf**, **sapling** (Warren's), plus **Aider** and Sourcegraph's **Amp**; and **ide**-pole harnesses like **Cursor**, **Copilot**, and **Windsurf**. Ingest more as they warrant pages — Codex and Cursor are the strongest next candidates (named by the most frameworks); graduate the matrix into derived nodes if it stops scaling.
