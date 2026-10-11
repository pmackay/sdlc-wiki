---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: ["[[builder-plow-ahead]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# principle-never-block-on-the-human

**Delegation principle.** Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible actions.

Applies when tempted to ask "should I do X?" on reversible work. [[pstack-poteto-mode]] sharpens it into a classification rule at the moment of asking: if the answer is a fact you could observe by running something, it is not the human's to answer — prototype it and let the result decide. Irreversible writes (force-push to shared branches, deploys, data deletion, customer messages) always pause.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
