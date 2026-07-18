---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Context Engineering

Feed the agent the right information at the right time — too little and it hallucinates, too
much and it loses focus. The mechanism is a **context hierarchy** from persistent to transient:
rules files (CLAUDE.md and its equivalents), then per-feature spec sections, then per-task source
files, then per-iteration error output, then conversation history. It favours selective
includes over brain-dumps, pulls in MCP integrations (Context7, Chrome DevTools, Postgres) for
richer context, and **resets the session when output quality degrades**.

It applies [[pattern-context-engineering]] and runs throughout the build to keep the agent on
project conventions. It implements [[stage-implement]].

## See Also
- [[pattern-context-engineering]] — the underlying pattern.
- [[stage-implement]] — the canonical stage this implements.
