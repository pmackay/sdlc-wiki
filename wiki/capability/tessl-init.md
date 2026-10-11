---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[beads-setup]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl init · tessl project

Initialize Tessl in a repository, and anchor it there. `tessl init` **detects the coding agents present and configures them automatically** — Claude Code, Cursor, Codex, Gemini CLI, Antigravity, GitHub Copilot CLI, and GitHub Copilot for VS Code need no further setup; anything else that speaks MCP is configured by hand, with shipped recipes for **OpenCode** and **OpenClaw**.

The integration itself is deliberately thin: an MCP server entry (`command: tessl`, `args: ["mcp", "start"]`) plus written rules files. That is how one skill reaches seven harnesses without being rewritten — *"Write context once; Tessl distributes it everywhere"* — and it is the mechanism behind the `integrates_with:` edges on the [[tessl]] page.

`tessl project` handles the second half: create, link, repair, and list the **project**, which is Tessl's stable anchor for a repository. It exists so repository-connected results — evaluation runs above all — stay attached to the right codebase as branches and checkouts come and go. The three nouns are kept deliberately apart: a **plugin** is content, a **workspace** is ownership, a **project** is location.

`tessl project repair` earns its own subcommand, which is a small tell about how often the anchor breaks in practice (renamed repos, re-clones, forks).

## See Also
- [[tessl-workspace]] — the ownership boundary a project belongs to.
- [[tessl-eval]] — the results a project exists to anchor.
- [[beads-setup]] — the store layer's equivalent: a per-harness install recipe rather than auto-detection.
