---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-sprint-planning (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-sprint-planning

**`bmad-sprint-planning`** — "Generate sprint status tracking from epics." Owned by [[bmad-dev]] (Amelia, in her absorbed Scrum-Master role), it reads the epic/story breakdown and generates `sprint-status.yaml` — the state file that drives the story loop, tracking each story through `backlog → ready-for-dev → in-progress → review → done`.

`sprint-status.yaml` is the backbone of BMAD's story-driven dev loop: the read-only `bmad-sprint-status` skill summarizes it and surfaces risks at any point.

## See Also
- [[bmad]] — the framework.
- [[bmad-create-story]] — reads the sprint backlog to prepare the next story.
- [[bmad-dev-story]] — advances a story's status as it implements.
- [[stage-plan]] — the canonical stage.
