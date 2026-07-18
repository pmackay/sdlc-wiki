---
type: capability
subtype: sub-agent
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-test-driven-development]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Test Engineer (persona)

A QA specialist persona focused on test strategy, test writing, and coverage-gap analysis. It analyzes code before writing, tests behavior rather than implementation, and picks the right level per the test pyramid — unit for pure logic, integration when a boundary is crossed, E2E only for critical user flows. For bugs it follows the Prove-It pattern: write a test that fails against the current code, confirm it fails, then hand it off for the fix. Its coverage analysis prioritizes tests that catch data-loss or security issues and core business logic.

It runs as a stateless review subagent with a fresh context and never invokes other personas — recommendations to add tests go in its report for the user or a slash command to act on. It is invoked directly via [[addy-tdd]] for the TDD workflow, and participates in the [[addy-shipping]] `/ship` fan-out, where three review subagents run in parallel to cover review, testing, and security.

## See Also
- [[addy-tdd]]
- [[addy-shipping]]
- [[stage-review]]
