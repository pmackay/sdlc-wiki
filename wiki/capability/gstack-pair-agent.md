---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026); ARCHITECTURE.md"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /pair-agent

`/pair-agent` — the **Multi-Agent Coordinator**. Shares your browser with **any AI agent** — OpenClaw, Hermes, Codex, Cursor, or anything that can `curl` — each in its own isolated tab. One command prints a paste-block; the other agent exchanges a one-time setup key for a session token, opens its own tab, and starts browsing. An ngrok tunnel auto-starts for remote agents (dual-listener architecture: scoped tokens, tab isolation, rate limiting, domain restrictions, activity attribution). "The first time AI agents from different vendors can coordinate through a shared browser with real security."

A **cross-cutting collaboration** capability — genuinely novel in this wiki, with no counterpart in any other framework. Filed under [[stage-implement]] as a multi-agent build-time collaboration tool; built on the [[gstack-open-gstack-browser]] / [[gstack-browse]] infrastructure.

## See Also
- [[gstack-open-gstack-browser]] — the shared browser this coordinates through.
- [[gstack-codex]] — the in-Claude cross-vendor second-opinion (a different vendor-integration angle).
- [[stage-implement]] — the stage this supports (collaboration during build).
