---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-test-driven-development]]", "[[pattern-systematic-debugging]]"]
equivalent_to: ["[[mp-tdd]]", "[[sp-test-driven-development]]", "[[speckit-implement]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /tdd

Make the broken behavior executable before changing production code: write the focused regression test that fails before the fix and passes after it. Understand the bug, choose the narrowest executable check, write the failing test, **run it before fixing** to confirm it fails for the intended reason, make the smallest production change, rerun, then run nearby validation.

**pstack's member of the [[pattern-test-driven-development]] cluster is the one that argues against itself**, and that is what makes it worth a page. Where [[speckit]] makes TDD non-negotiable and [[superpowers]] auto-triggers [[sp-test-driven-development]] as a gate, this skill's own frontmatter restricts it to cases where the user explicitly asks *or* the bug has an obvious cheap local test target, and its body opens by telling you when not to use it. A test is skipped when it would need broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state, vague reproduction steps, or large unrelated fixture churn.

The skipping is not silent. *Do not silently skip the regression step* — explain before fixing why a failing test is impossible or not worth the cost, then use the closest executable regression check available: a targeted script, a manual reproduction command, browser automation, a snapshot comparison, a log assertion, a focused integration check. The obligation is to executable evidence, not to a test file.

It ships a definition of the thing it is avoiding. **A bad test** is one that mostly tests mocks, encodes current implementation details, depends on timing or unrelated global state, needs expensive infrastructure for a small fix, or would be deleted immediately after proving the fix. *Prefer no new test over a bad test.* The companion falsifiable check lives in [[pstack-principle-test-behavior-not-implementation]]: if the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test.

Guardrails close it out: do not change tests merely to match a wrong implementation, and do not weaken existing assertions unless the expected behavior has genuinely changed and the reason is clear.

## See Also
- [[pstack-principle-test-behavior-not-implementation]] — the test-quality rule this defers to.
- [[pstack-create-verification-skill]] — the answer when there is no cheap local test path at all.
- [[mp-tdd]] · [[sp-test-driven-development]] — the TDD cluster; both treat the practice as more nearly mandatory than this does.
- [[stage-implement]] — the canonical stage this implements.
