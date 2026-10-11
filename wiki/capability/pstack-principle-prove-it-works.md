---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-prove-it-works

**Verification principle.** Verify against the real artifact, not a proxy, a self-report, or "it compiles".

Applies after completing a task, before declaring done. pstack's member of the [[pattern-evidence-before-claims]] cluster alongside [[sp-verification-before-completion]]. Its sharpest operational form is the evidence ladder in [[pstack-blast-radius]], which grades a safety claim from "you said so" up to "you reproduced it in the running app" and requires you to say where it stopped.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
