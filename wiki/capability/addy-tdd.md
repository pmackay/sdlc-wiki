---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-test-driven-development]]"]
equivalent_to: ["[[mp-tdd]]", "[[sp-test-driven-development]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Test-Driven Development

Write a failing test before the code that passes it — **Red → Green → Refactor** — treating
tests as proof rather than "seems right" (see [[pattern-test-driven-development]]). It carries a
rich rubric: the **test pyramid** (~80% unit / 15% integration / 5% E2E), a Small/Medium/Large
test-size model, **DAMP over DRY** in tests, and the **Beyoncé Rule** (if you liked it you should
have put a test on it). For bugs it mandates the **Prove-It Pattern** — a failing test that
reproduces the bug first, then the fix.

It is the **third framework in the TDD cluster**, converging with Matt Pocock's [[mp-tdd]]. It
implements [[stage-implement]].

## See Also
- [[mp-tdd]] — the Matt Pocock equivalent in the TDD cluster.
- [[pattern-test-driven-development]] — the underlying pattern.
- [[stage-implement]] — the canonical stage this implements.
