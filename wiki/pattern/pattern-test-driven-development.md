---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026); pstack v0.15.2 — Lauren Tan (2026)"
updated: 2026-10-11
---

# Pattern: Test-driven development (red-green-refactor)

Write a failing test first (red), make it pass with the simplest code (green), then refactor — repeat. Gives the agent ground-truth feedback before it commits to an implementation, a direct answer to "the code doesn't work."

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-tdd]] — dedicated red-green-refactor skill.
- [[mp-implement-spec]] — every implementer subagent builds its ticket by calling [[mp-tdd]] (v1.3.0).

GSD:

- [[gsd-plan-phase]] — `--tdd` mode plans test-first RED-GREEN cycles.

Addy Osmani — Agent Skills:

- [[addy-tdd]] — dedicated red-green-refactor skill.
- [[addy-test-engineer]] — writes and drives the tests.

Spec Kit:

- [[speckit-implement]] — TDD is "NON-NEGOTIABLE": tests are written and must fail (Red) before implementation code.

BMAD:

- [[bmad-dev-story]] — implements each story test-first; its persona [[bmad-dev]] (Amelia) is "disciplined in Kent Beck's TDD."

gstack:

- [[gstack-qa]] — auto-generates a regression test for every fix; /ship bootstraps a test framework and audits coverage (100% goal).

Superpowers:

- [[sp-test-driven-development]] — the dedicated RED-GREEN-REFACTOR skill; Iron Law "no production code without a failing test first," enforced by delete-and-restart.
- [[sp-writing-plans]] — bakes the test-first micro-loop directly into every plan task's steps.
- [[sp-writing-skills]] — applies red-green-refactor to *skill authoring itself* (baseline subagent failure → write skill → watch it comply).

Now a strong multi-framework cluster. Spec Kit is the strictest by *mechanism* — test-first is mandated by [[artifact-constitution|the project constitution]] (Article III) — while Superpowers matches its non-negotiability by *rhetoric*: any production code written before its test must be deleted and rewritten from the test.

pstack — **the cluster member that argues for its own limits**:

- [[pstack-tdd]] — restricted by its own frontmatter to an explicit request or an obviously cheap local test target, and it opens by listing when to skip: broad harness setup, brittle mocks, slow end-to-end infrastructure, production-only state, vague repro steps, large fixture churn. The skip is never silent — explain why, then use the closest executable regression check. *"Prefer no new test over a bad test."*
- [[pstack-principle-test-behavior-not-implementation]] — the falsifiable quality check the cluster was missing: **if the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test.**
- [[pstack-typescript-best-practices]] — *do not mock what you can run*; prefer the framework's real test primitives with leak and disposable checks.

## See Also
- [[pattern-systematic-debugging]] — the sibling feedback loop for bugs.
- [[pattern-deterministic-gates]] — the general form: a test suite is one program-decided gate among lint, types, and build.
- [[stage-implement]] — the stage where this applies.
