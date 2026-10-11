---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /an

Open a granted **Agent-Native app** (Slides, Design, Forms, …) beside the conversation through **Dispatch MCP** (`https://dispatch.agent-native.com/mcp`), then work in it using the app's live UI and screen state. It ships as both a skill and a `/an <app> [request]` command (`commands/an.md`), which calls `open_app` with `embed: true` and forwards the rest of the arguments as the request.

Working rules: prefer direct page tools (`list-host-webmcp-tools` / `run-host-webmcp-tool`) over the app's own agent. *"You are the model doing the work: … author it yourself and save it with the app's create/update tools. Never hand off authoring to the app's own agent when those tools exist."* Call `view-screen` before any selection-dependent edit and never guess an ID from a title. Make the smallest atomic change and **read it back**, because *"a queued `ask_app_status` task is not proof an edit completed."* The user signs in inside the rendered surface, and the agent never handles passwords, cookies, or tokens.

Off-stage. It is a product front-end, recorded for completeness and for its read-back rule.

## See Also
- [[builder-webmcp]] — the general in-browser version for any WebMCP page.
- [[builder-skills]] — the framework.
