# Factory Droid (Droid CLI) — source capture (2026-08-02)

Sources: docs.factory.ai (CLI overview, custom-droids, agents-md, pricing) + factory.ai/product/droids + web research (DeepWiki factory-ai/factory, Developers Digest, every.to), captured 2026-08-02. Immutable capture for the sdlc-wiki harness layer.

## Identity

- Name: **Droid** — the CLI agent from **Factory** (Factory.ai). "Droid CLI" / "Factory Droid".
- Vendor/author: **Factory.ai**.
- Docs: https://docs.factory.ai/cli/getting-started/overview
- Product: https://factory.ai/product/droids
- License/distribution: **proprietary** (commercial SaaS). Plans: **Pro $20/mo · Plus $100/mo · Max $200/mo**, plus Business/Enterprise via sales. **Droid Core** = a free tier of leading open-weight models with its own separate rate limits (keep working at no extra cost once standard limits are exhausted).

## One-line identity

A terminal-native AI coding agent from Factory.ai, distinguished by **multi-model routing** (Anthropic + OpenAI + Google + open-weight, swappable mid-session, plus BYOK) and **Missions** multi-agent orchestration; runs interactive TUI, headless in CI (`droid exec`), and via IDE integration.

## Interaction surface

Primary/native = **interactive terminal UI** (full-screen TUI, keyboard-first; `!` toggles bash mode to run shell directly without AI interpretation, `Esc` returns to normal mode). Also: **headless execution** via `droid exec` for scripts/CI/CD; **IDE integrations**; a **web app** (Factory App at app.factory.ai). A **Droid Sessions API** gives programmatic access. Native surface is the terminal → `subtype: terminal`.

## Model access

**Multi-model / model-routing** — the signature axis. Swap between **Anthropic (Claude Opus/Sonnet), OpenAI (GPT-5/Codex), Google (Gemini)**, and a growing roster of **open-weight** models **mid-session**. **Droid Core** ships open-weight models free (e.g. MiniMax M2.5/M2.7, Kimi K2.5/K2.6, DeepSeek V4 Pro, Nemotron 3 Ultra, GLM-5.1). **BYOK** supports Anthropic, OpenAI, and any generic chat-completion-compatible endpoint (OpenRouter, Fireworks, Together AI, Groq, Ollama, …). Subagents can route by task **complexity** to a model tier. (Contrast: Claude Code is Anthropic-only; opencode/pi are model-agnostic too but without Droid's routing/Missions framing.)

## Execution primitives

- **Sub-agents (Custom Droids)** — YES, first-class. Reusable subagents defined as **Markdown files with YAML frontmatter** in `<repo>/.factory/droids/` (project) or `~/.factory/droids/` (personal). Frontmatter: `name`, `description`, `model` (`inherit` or a specific model id), `reasoningEffort` (optional), `tools`, `mcpServers` (optional); body = system prompt. Each **runs in a fresh context window and its own session**, with its own **system prompt, tool policy, model, and autonomy level** — "so the parent session stays focused and lean." Restrict to **read-only, edit-only, or a curated tool set**; `mcpServers` scopes which servers it can reach. Delegated via the **Task** tool (`subagent_type`, `prompt`, `complexity`, `run_in_background`) or directly ("Use the subagent `code-reviewer` on the staged diff"). `run_in_background` enables asynchronous/concurrent subagents.
- **MCP** — YES, mature: **40+ pre-configured servers** + OAuth flows. `droid mcp add` or `/mcp`.
- **Hooks** — YES. Run shell commands around agent lifecycle events (pre/post-edit workflows, policy enforcement). `/hooks`.
- **Skills** — YES. Reusable procedures the agent invokes on demand; `/skills`, `/create-skill`. SKILL.md units (distinct from AGENTS.md briefing and DESIGN.md visual guidance).
- **Slash commands** — YES (`/missions`, `/droids`, `/skills`, `/mcp`, `/hooks`, `/plugins`, `/create-skill`, …).
- **Plugins** — YES. Package bundles of **commands, droids, skills, and hooks** for team distribution; `droid plugin install` / `/plugins`.
- **Permissions / autonomy** — YES. **Autonomy levels** `off` / `low` / `medium` / `high` control permission level for file and system operations; set via `--auto` flag (e.g. `--auto high`) or settings; a normal/read-only mode reviews planned changes without execution. Tool interaction is via **transparent, permission-checked tools**; approval workflows for governance. Tool categories: `read-only` (explore), `edit` (generate), `execute` (shell).
- **Missions (multi-agent orchestration)** — launch multi-agent Missions via `/missions` or `droid exec --mission`. Harness-level parallel/multi-agent orchestration (runtime-adjacent per the boundary test).
- **Memory / context files** — **AGENTS.md** project briefing (install/run/test/edit/verify + repo boundaries), loaded at startup and via dynamic discovery. Follows the shared **AGENTS.md standard**: `AGENTS.md`/`agents.md`/`CLAUDE.md` (+ title-case variants) all recognized → compatible with other tools' instruction files. Discovery walks up to the git root checking repo root, `.factory/`, `.agents/`/`.agent/`; personal defaults in `~/.factory/`, `~/.agents/`, `~/.agent/`. Precedence: current user request → nested project files → root project files → personal defaults.

## Integrations

Jira, Notion, Slack, Linear, PagerDuty (via MCP/connectors). Plans, implements, tests, and reviews changes end-to-end.

## Distinctive

- **Model routing** — the deepest multi-model story of any harness paged here: frontier + open-weight, mid-session swap, BYOK, per-subagent model + complexity-based tier routing, and a free open-weight **Droid Core** fallback. Where Claude Code is single-vendor and opencode/pi are "model-agnostic," Droid makes *routing between models* a first-class product feature.
- **Missions** — harness-native multi-agent orchestration (parallel droid fan-out) beyond one-off subagents.
- **AGENTS.md-standard-native + Claude-Code-shaped primitive set** — Custom Droids/Skills/Hooks/Plugins mirror Claude Code's sub-agents/skills/hooks/plugins almost 1:1, but with a portable AGENTS.md/CLAUDE.md-compatible config surface and multi-model backends.

## Wiki cross-references

- Officially a `runs_on:` target of cross-harness frameworks already paged: **Compound Engineering**, **gstack**, **Superpowers** all name Factory Droid. (These currently record it in prose only; this ingest lets the stored edges point at a real page.)
- Patterns it provides as primitives: fresh-context-subagents (Custom Droids, fresh context + own session, Task tool, `run_in_background`), edit-guardrails (autonomy levels + tool policies + hooks + permission-checked tools + approval workflows), session-handoff (own-session subagents + Droid Sessions API + headless `droid exec` resumable runs), context-engineering (AGENTS.md standard + skills + 40+ MCP servers + plugins).
