---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-vertical-slice]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-sequence-verifiable-units

**Verification principle.** Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer.

Applies to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. The third clause is the distinctive one: sequencing is treated as a *review* affordance, not just an execution tactic, which is what connects it to the stacked-PR playbooks and to [[pstack-show-me-your-work]].

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
