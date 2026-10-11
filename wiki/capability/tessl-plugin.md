---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-capability-bundle]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl plugin

The full lifecycle of the layer's unit of trade: `plugin new`, `lint`, `migrate`, `pack`, `info`, `publish`, `unpublish`, `archive` → [[artifact-capability-bundle]].

A plugin bundles **skills, rules, MCP servers, and hooks**, versioned and installed as one unit *"much like a package in npm or pip"*. The composition matters more than the packaging: through hooks (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `SessionStart`, `Stop`) and MCP servers, installing a plugin extends the **harness's execution primitives**, not just the agent's prompt. This is the precise point where the supply layer reaches down into the harness layer.

The command set is ordinary package-manager vocabulary, and that ordinariness is the finding — `pack` produces a distributable, `info` inspects a specific version, `archive` retires versions without deleting them, `migrate` moves a bundle off the legacy `tile.json` format. A layer that has already accumulated a deprecated manifest format is not a new idea being tried out.

## See Also
- [[tessl-skill]] — the single unit a plugin packages.
- [[tessl-install]] — the consuming side.
- [[tessl-scenario]] · [[tessl-eval]] — the suite that ships inside the bundle and grades it.
- [[artifact-capability-bundle]] — the artifact this produces.
