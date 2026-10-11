---
type: standard
subtype: format
steward: "Agentic AI Foundation, under the Linux Foundation (AGENTS.md, a Series of LF Projects, LLC)"
spec_url: "https://agents.md/"
spec_version: "unversioned"
enables: ["[[pattern-context-engineering]]"]
sources: "AGENTS.md — agents.md (captured 2026-10-11)"
raw: ["../../raw/standard/2026-10-11-agents-md.md"]
updated: 2026-10-11
---

# AGENTS.md

**Contract layer** — a [standard](index.md), not a product. `AGENTS.md` is *"a simple, open format for guiding coding agents"*: *"a README for agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project."* The site claims use by over 60,000 open-source projects. It is the always-loaded half of context engineering, where [[std-agent-skills]] is the on-demand half.

## The format

There is almost nothing to conform to, and that is the design. *"Are there required fields? No. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide."* The whole contract is three behaviours an adopting agent promises:

- **Location and precedence.** The file sits at the repository root. In a monorepo, nested files go inside each package, and *"agents automatically read the nearest file in the directory tree, so the closest one takes precedence."* The site's example is the main OpenAI repository with 88 `AGENTS.md` files.
- **Override order.** *"The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything."*
- **Checks are executed.** *"Will the agent run testing commands found in AGENTS.md automatically? Yes—if you list them. The agent will attempt to execute relevant programmatic checks and fix failures before finishing the task."*

The recommended content is what a new teammate would need and a README would not carry: project overview, build and test commands, code style, testing instructions, security considerations, commit and PR conventions, deployment steps. The README stays for humans; `AGENTS.md` takes *"the extra, sometimes detailed context coding agents need"*.

Migration is by rename and symlink (`mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`). Agents that default to their own filename adopt it by configuration: Aider via `read: AGENTS.md`, Gemini CLI via `"context": { "fileName": "AGENTS.md" }`.

## Governance

*"AGENTS.md emerged from collaborative efforts across the AI software development ecosystem, including OpenAI Codex, Amp, Jules from Google, Cursor, and Factory,"* and *"is now stewarded by the Agentic AI Foundation under the Linux Foundation."* The site names no version, change process, or deprecation policy; with no required fields, there is little for a version to change.

## Adoption (`conforms_to:` backlinks)

**Harnesses:**

- [[factory-droid]] — the most committed adopter: `AGENTS.md` is the project briefing, discovered by walking to the git root plus `~/.factory/` personal defaults, and Factory is one of the format's named originators.
- [[opencode]] — `AGENTS.md` is the project configuration file.
- [[pi]] — `AGENTS.md` plus `SYSTEM.md`, loaded from `~/.pi/agent/`, parent directories, and cwd.

**Frameworks** — each writes `AGENTS.md` into the user's repository:

- [[builder-skills]] — the installer can write managed `AGENTS.md` / `CLAUDE.md` blocks, including the [[builder-quick-recap]] status line.
- [[bm-skills]] — `AGENTS.md` / `CLAUDE.md` guardrails so later agents defer to the design system ([[bm-design-system]]).
- [[nano-spec]] — installs its instructions as `AGENTS.md` (or `.codex/AGENTS.md`) for Codex and OpenCode, beside per-harness files for the others.

**Stores** — each writes an `AGENTS.md` section so any agent learns the store exists:

- [[beads]] — `bd init` *"creates or updates AGENTS.md by default"*, and `--agents-file` changes the filename.
- [[seeds]] — `sd onboard` writes a seeds section into `CLAUDE.md` / `AGENTS.md` ([[seeds-onboard]]).

**Not yet paged** (from the site's adopter strip): Codex, Jules, Aider, goose, Zed, Warp, VS Code, Devin, UiPath Autopilot, Junie, Amp, Cursor, RooCode, Gemini CLI, Kilo Code, Phoenix, Semgrep, GitHub Copilot's coding agent, Ona, Windsurf, Augment Code.

## The absence: Claude Code

[[claude-code]] is **not** an adopter. It is missing from the site's adopter strip, and the wiki's captured Claude Code documentation names `CLAUDE.md` (project and `~/.claude/CLAUDE.md` global) as its context file, with no mention of `AGENTS.md`. Because Claude Code is also the harness nearly every framework here targets first, the gap shows up as a **dual-file tax** across the wiki:

- [[matt-pocock-skills]] symlinks `AGENTS.md` to `CLAUDE.md` in its own repository.
- [[builder-skills]], [[bm-skills]], and [[seeds]] each write *both* files.
- [[factory-droid]] describes its `AGENTS.md` as `CLAUDE.md`-compatible.
- [[mp-retro]] and [[mp-writing-for-agents]] always name the pair together (`CLAUDE.md` / `AGENTS.md`).

The pattern is consistent enough to read as the standard's main open issue rather than a quirk of any one tool.

## Relationship to other standards

- [[std-agent-skills]] is the on-demand counterpart. A healthy split, as [[mp-retro]] states it, keeps `AGENTS.md` to navigation pointers and moves procedures into skills and rules into review-time checks, so the always-loaded file stays small.
- [[std-mcp]] is how live tools reach the agent, where `AGENTS.md` is how standing instructions do.

## See Also
- [Standard layer](index.md) — the adoption matrix across all three standards.
- [[pattern-context-engineering]] — the technique this file is the most common vehicle for.
- [[topic-harness-engineering]] — `AGENTS.md` is the canonical *guide (feedforward)* control.
- [[topic-agent-readiness]] — Factory's Agent Readiness rubric scores `AGENTS.md` under its Documentation pillar, and its fix pass can write one.
