---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-throwaway-prototype]]", "[[pattern-candidate-grafting]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-exhaust-the-design-space

**Core principle.** Build 2-3 competing prototypes and compare side by side before committing.

Applies when facing a novel UI interaction or architectural decision with no precedent in the codebase. [[pstack-arena]] is this principle made concrete, and [[pstack-architect]] Phase B enforces it as a hard floor: at least two *structurally distinct* candidates before synthesis, even when the first looks sufficient.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
