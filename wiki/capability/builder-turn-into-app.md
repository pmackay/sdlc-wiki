---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /turn-into-app

At the end of a thread, turn a **proven workflow** (the current thread, visible project context, a named skill such as `/turn-into-app /some-skill`, or a spreadsheet) into a runnable **Agent-Native app** with clear buttons, visible agent steps, a local preview, and a deployment handoff. *"The result should be the concrete workflow app, not a generic app-builder intake form."*

It first classifies the host. On a **local coding host** (Codex, Claude Code, Cursor) it scaffolds, builds, runs, and verifies the app in the checkout. On a **browser-only host** (Claude Web, ChatGPT) it writes a bounded source brief and hands it to Dispatch's `start-workspace-app-creation`, which starts a Builder Cloud Agent. It then reports exactly what Dispatch returned: *"Never invent a Builder branch URL… report the handoff as unverified."*

Filed under [[stage-learn]] next to [[gstack-skillify]] and [[pstack-automate-me]]: a workflow that worked once is packaged so it can be reused. The difference is the output, which is an application for people rather than a skill for agents.

## See Also
- [[gstack-skillify]] · [[pstack-automate-me]] — the same move with a skill as the output.
- [[pattern-knowledge-compounding]] — the pattern.
- [[stage-learn]] — the canonical stage this implements.
