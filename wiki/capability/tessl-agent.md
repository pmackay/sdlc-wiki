---
type: capability
subtype: sub-agent
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# Tessl Agent

A conversational agent that drives the platform and *"autonomously monitors and improves your agentic setup"*, running alongside your existing coding agents (open beta). Invoked as `tessl agent` — interactive, one-shot, non-interactive with JSON output, resumable, model-selectable, with its own MCP server management (`agent mcp add/get/list/remove`) and a yolo mode that auto-approves permissions.

**Its subject is the toolchain, not the codebase**, which is what makes it unusual enough to page. The documented uses are things like mining PRs and session logs for recurring agent mistakes, turning those into a skill fix, and proving the fix with an eval; and spotting repetitive work in the development loop and turning it into an automated workflow. That is [[pattern-knowledge-compounding]] with the loop closed by a **separate agent whose job is the agent setup** — the framework-side instinct of [[pstack-reflect]] and [[ce-compound]], lifted out of the session and made continuous.

It also completes a circle worth noticing. [[tessl-observability]] data — where skills actually *activate* across sessions, not merely where they are installed — is what this agent mines, and the fixes it proposes are published back through [[tessl-plugin]] and measured by [[tessl-eval]]. Observe, diagnose, fix, prove, redistribute: the compounding loop the process layer runs on a developer's session, run instead on the organization's capability corpus.

Filed as `sub-agent` because that is what it is in the wiki's vocabulary — a delegated agent with a bounded remit — though it is a first-class product surface rather than something a command spawns.

## See Also
- [[tessl-eval]] — how its proposed improvements get proven.
- [[tessl-inventory]] — the estate it reasons over.
- [[pstack-reflect]] · [[ce-compound]] — the in-session, framework-side counterparts.
- [[pattern-knowledge-compounding]] — the loop, run on the toolchain.
