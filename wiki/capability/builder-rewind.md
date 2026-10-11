---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /rewind

Retrieve recent **local screen context** from Clips Rewind (Builder's macOS Clips Desktop app) when the user says *"Look at Rewind"* or refers to something they recently said or saw. It works through a local `clips-screen-memory` MCP.

Retrieval works from coarse to fine: check `screen_memory_status` (and wait if the newest segment is still open), search chapters, ask when several plausibly match (*"do not blend separate workstreams together"*), read the smallest useful range of transcript and OCR, then single frames or contact sheets. A bounded private cloud Clip handoff is used only when local text and frames are not enough.

It stands out for its consent and privacy boundaries. Setup is gated on explicit permission (*"never bypass Gatekeeper, accept macOS permission prompts, or enable screen/audio capture on the user's behalf"*). Recordings, frames, and indexes stay local, the skill never reveals archive paths or bypasses the MCP broker, and it treats *"foreground apps and chapter labels as evidence, not proof of intent."* Off-stage context retrieval, closer to a personal memory store than to a lifecycle step.

## See Also
- [[builder-an]] · [[builder-webmcp]] — the other Agent-Native host integrations.
- [[pattern-context-engineering]] — retrieving the smallest relevant range of context.
