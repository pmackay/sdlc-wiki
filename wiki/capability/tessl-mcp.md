---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl mcp

Two commands that carry most of the layer's integration weight: `tessl mcp start` and `tessl mcp proxy`.

**`mcp start` is how every harness talks to the registry.** It is the stdio MCP server that [[tessl-init]] writes into each agent's config, and through it an agent reaches the context in installed plugins as **tools** rather than as files. That single choice is what makes the product harness-agnostic: MCP is the one extension surface Claude Code, Cursor, Codex, Gemini CLI, Copilot, OpenCode, and OpenClaw all share, so targeting it reaches seven harnesses without seven integrations. The `integrates_with:` edges on [[tessl]] rest on this command.

**`mcp proxy` is the workspace MCP gateway.** A workspace declares MCP servers centrally and any agent connects to them through the proxy, so the servers an organization sanctions — and the credentials they need ([[tessl-environment]]) — are administered in one place rather than configured per developer. That is the supply-chain argument extended from instructions to tools: if a registry governs which skills may be installed, the same boundary is the natural place to govern which tools an agent may reach.

Worth noting against the wiki's [harness matrix](../harness/index.md): MCP appears there as a per-harness capability row. This layer treats it as the **portability substrate** — the thing that makes one capability run everywhere — which is a different use of the same primitive.

## See Also
- [[tessl-init]] — writes the `mcp start` entry into each detected agent.
- [[tessl-environment]] — the credentials the gateway carries.
- [[claude-code]] · [[opencode]] — the paged harnesses reached this way.
