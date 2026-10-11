---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /visual-edit

Open a **running local app** in Builder's hosted Design editor as iframe-backed screens on an infinite canvas, one per route, for visual inspection, route-state exploration, and **source-backed editing**. Unlike a static mockup, *"the canvas stays connected to the app's real routes and the local bridge."*

Most of the skill is host plumbing: never run Design locally, start agent-owned dev servers with `AUTH_DISABLED=1`, probe each route before placing it (*"never leave a dead localhost URL in the canvas"* and *"never present a sign-in page as the requested screen"*), leave servers the agent did not start alone, and go through the MCP App bridge or a page-world WebMCP evaluator.

[[stage-implement]], for UI work: the edit happens in the running app's source, with the canvas as the way to see and choose it.

## See Also
- [[builder-webmcp]] — the WebMCP bridge this reuses.
- [[gstack-design-review]] — a live-site visual audit, as a review step rather than editing.
- [[stage-implement]] — the canonical stage this implements.
