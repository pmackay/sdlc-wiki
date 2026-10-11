---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-test-driven-development]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-test-behavior-not-implementation

**Verification principle.** Call the code the way its users do and assert the result they observe against a literal expected value.

Applies when you write, change, or keep a test. It ships with the sharpest falsifiable test-quality heuristic in the wiki: if the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test. That single check is what [[pstack-tdd]] and [[pstack-typescript-best-practices]] both defer to.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
