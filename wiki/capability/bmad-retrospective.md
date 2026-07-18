---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: []
applies: ["[[pattern-persona-agents]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-retrospective (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-retrospective

**`bmad-retrospective`** — "Post-epic review to extract lessons and assess success." Owned by
[[bmad-dev]] and run as a Party-Mode roundtable ([[pattern-persona-agents]]), it closes out a
completed epic by harvesting lessons and appending action items that later sprints surface —
[[pattern-knowledge-compounding]] in its **team-process** flavor.

It implements [[stage-learn]] — the canonical learning-capture stage. It was the wiki's
original evidence for that activity (long parked as the "learning close-out" flavor of
[[stage-release]]); when Compound Engineering's [[ce-compound]] became a **second** framework
treating learning capture as a first-class step, the activity cleared the ≥2-framework bar and
was promoted out of release into its own stage (2026-07-04). BMAD's is the human-facing
retrospective; Compound Engineering's is a machine-consumable [[artifact-solution-doc|solution
corpus]]. Like [[speckit]], BMAD core ships no deploy/PR/observability step — it closes by
learning, not shipping.

## See Also
- [[bmad]] — the framework.
- [[ce-compound]] — Compound Engineering's counterpart; the agent-grounding flavor of the same [[stage-learn]] activity.
- [[gsd-ship]] — GSD's [[stage-release]] step (ships to prod); the sibling close-out, delivery rather than learning.
- [[stage-learn]] — the canonical stage this implements.
