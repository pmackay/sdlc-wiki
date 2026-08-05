# Claude Code — source capture (2026-07-31)

Source: Anthropic — Claude Code documentation (docs.claude.com/en/docs/claude-code) and the Claude Agent SDK docs, captured 2026-07-31. Claude Code is Anthropic's official agentic coding tool. Immutable capture for the sdlc-wiki harness layer.

## What it is

Claude Code is an agentic coding **harness**: an agent program that runs in the terminal (and as a desktop app on macOS/Windows, a web app at claude.ai/code, and via IDE extensions for VS Code and JetBrains). You give it a prompt; it assembles context, calls a Claude model, and runs an agentic loop — reading files, running shell commands, editing code, executing tests — pausing for permission on sensitive actions. It is model-hosted by Anthropic's Claude models (the Claude 5 family, Opus 4.8, Haiku 4.5, etc.); "Fast mode" gives Opus faster output without downgrading the model.

It ships no opinionated SDLC methodology of its own. It is the substrate other frameworks' skills/commands run on: GSD, Superpowers, gstack, Compound Engineering, Addy's Agent Skills, BMAD, SpecKit, etc. are all authored to be loaded and executed *by* Claude Code (and, for the cross-harness ones, by other harnesses too).

## Interaction surfaces

- **Terminal CLI / TUI** — the primary surface; an interactive REPL plus one-shot/headless (`-p`/`--print`) mode.
- **Desktop app** — macOS and Windows.
- **Web app** — claude.ai/code.
- **IDE extensions** — VS Code and JetBrains.
- **Headless / CI** — scriptable non-interactive runs; the basis for automation and for being spawned by runtimes.

## Execution primitives (what a framework builds on)

- **Tool-call loop** — the core agentic cycle: the model requests tool calls (Read, Edit, Write, Bash, Grep, Glob, web fetch/search, etc.), the harness executes them and feeds results back, until the task is done.
- **Sub-agents / the Agent (Task) tool** — Claude Code can spawn sub-agents that run with their own fresh context window and a scoped toolset, returning only a final result to the caller. Sub-agent *types* are defined in `.claude/agents/*.md` (frontmatter: name, description, tools, model, etc.) or via the Agent SDK. This is the harness primitive behind every framework's "fresh-context subagent" / parallel-fan-out skill. Multiple sub-agents launched in one turn run concurrently.
- **Skills** — loadable `SKILL.md` units (plus supporting files) that the model invokes when relevant; auto-discovered from plugin/marketplace or project/user skill directories. Frameworks like Superpowers are distributed as skills. The harness's skill loader + description-based auto-trigger is what makes "if there's a 1% chance a skill applies you must use it" work.
- **Slash commands** — invocable entrypoints (`/command`), both built-in (`/review`, `/init`, `/compact`, `/config`, `/memory`, …) and user/project-defined in `.claude/commands/`. Frameworks ship their commands this way.
- **MCP (Model Context Protocol)** — connect external tool/resource/prompt servers (local stdio or remote). Tools can be deferred and loaded on demand. This is how Claude Code reaches Slack, Linear, Figma, Chrome automation, databases, etc.
- **Hooks** — user-configured shell commands the harness runs automatically at lifecycle events (PreToolUse, PostToolUse, Stop, Notification, etc.), configured in `settings.json`. Hooks can block or modify a tool call. This is the substrate under "guardrail"-type skills (e.g. gstack careful/freeze/guard) and automated policy.
- **Permissions model** — permission modes (default / plan / acceptEdits / bypassPermissions) and allow/deny/ask rules in `settings.json`; sensitive or hard-to-reverse actions prompt for approval. Plan mode makes the agent research and propose a plan before it is allowed to edit.
- **Plan mode** — a read-only research/design mode; the agent produces a plan and exits it (with approval) before making changes.
- **Memory & context files** — `CLAUDE.md` (project + user global at `~/.claude/CLAUDE.md`) is loaded into context each session as standing instructions; `/memory` and a file-based persistent memory let facts persist across sessions; context is auto-summarized when a session grows long (compaction) so work continues across context windows.
- **Settings & config** — layered `settings.json` (user/project/local): permissions, env vars, hooks, model, status line, etc. Configurable via the `/config` command and the update-config skill.
- **Background tasks** — long-running commands can run detached and re-invoke the agent when they finish; scheduled/loop mechanisms (CronCreate, /loop, /schedule) exist for recurring work.
- **Keybindings** — customizable via `~/.claude/keybindings.json`.

## Extensibility & distribution

- **Plugins & marketplaces** — skills, commands, sub-agents, and hooks are packaged and shared; a plugin can namespace its skills (`plugin:skill`).
- **Claude Agent SDK** — a programmable SDK (TypeScript/Python) for building custom agents on the same harness primitives; supports defining `agents`, custom tools, a tool runner, managed agents with a managed sandbox, prompt caching, and token counting. (When the SDK is used to orchestrate/host agents programmatically, that is runtime-adjacent — the boundary test in CONVENTIONS pages the interactive loop as the harness.)
- **License / vendor** — Anthropic, proprietary (free tier + paid plans / API billing).

## Cross-references relevant to the wiki

- Runs frameworks: essentially every framework in this wiki targets Claude Code as (at least) one of its harnesses; several (GSD, gstack, Compound Engineering) are Claude-Code-native.
- Spawned by runtimes: Sandcastle lists Claude Code as a provider; Warren lists claude-code as a harness.
- Patterns it provides as primitives: fresh-context sub-agents (Agent/Task tool + agent defs), edit guardrails (hooks + permission modes), session handoff (compaction + `--resume`/session persistence), context engineering (CLAUDE.md/memory + MCP + skill auto-loading).
