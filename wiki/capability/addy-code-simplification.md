---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[ce-simplify-code]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Code Simplification

Reduces complexity while preserving **exact** behavior — same inputs, outputs, side effects,
error paths, and edge cases. The goal is comprehension speed, not fewer lines: every change
must pass the test "would a new team member understand this faster than the original?" It
opens with Chesterton's Fence — understand why code exists (read callers, check git blame)
before touching it — then scans for concrete signals (deep nesting, long functions, nested
ternaries, generic names, duplication, dead code) with named remedies.

Changes are applied incrementally: one simplification, run the tests, commit or revert if they
fail. The **Rule of 500** says any refactor touching more than 500 lines should be automated
(codemods, AST transforms) rather than hand-edited. Refactoring stays separate from feature
work and scoped to recently changed code.

## See Also
- [[mp-improve-codebase-architecture]] — the Matt Pocock structural-quality counterpart.
- [[addy-code-review]] — the review axis that flags simplification opportunities.
- [[stage-review]] — the canonical stage this implements.
