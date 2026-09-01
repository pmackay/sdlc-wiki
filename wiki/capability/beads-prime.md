---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]", "[[pattern-session-handoff]]"]
equivalent_to: ["[[seeds-prime]]"]
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd prime

`bd prime` — inject beads' workflow rules **and the project's persistent memories** into the agent's context. The docs state the purpose without hedging: *"designed for Claude Code, Gemini CLI, and Codex SessionStart hooks to **prevent agents from forgetting bd workflow after context compaction**."*

**It sizes itself to the budget it detects**, which is the part worth copying:

- **MCP mode** — an MCP server is active, so the tools are already described: brief reminders, **~50 tokens**.
- **CLI mode** — the agent must be told the commands: full reference, **~1–2k tokens**.
- `--full` / `--mcp` force either; `--memories-only` emits just the memories, for compaction hooks that fire mid-session; `--hook-json` wraps the output in the `SessionStart` hook envelope so a harness can install it verbatim; `--stealth` drops the git steps when `no-git-ops` is set.
- `.beads/PRIME.md` overrides the content entirely per project, and `--export` dumps the default to start from.

That is [[pattern-context-engineering]] with the *tool* doing the budgeting rather than the agent. A ~109-command CLI cannot afford to describe itself every turn, so beads measures whether the description is already in the window and charges accordingly — and by injecting [[beads-remember|memories]] on the same call, the session's first tokens are the project's accumulated knowledge rather than a command list.

Its [[pattern-session-handoff]] edge is the store's whole reason to exist. Where [[mp-handoff]] compacts a *conversation* into a document and [[gstack-context-restore]] replays one, `bd prime` restores **rules plus durable memory** and leaves the work state to [[beads-ready]] — a fresh agent needs no narrative, only the standing knowledge and the frontier.

Maps to **no canonical SDLC stage** — session bootstrap. `bd quickstart` and `bd human` are the human-facing equivalents.

## See Also
- [[beads-remember]] — the memories this injects.
- [[beads-setup]] — installs the hook that calls this automatically.
- [[beads-compact]] — the other half of the context budget: shrinking what is there to inject.
- [[seeds-prime]] · [[mp-handoff]] · [[gstack-context-restore]] — counterparts elsewhere.
