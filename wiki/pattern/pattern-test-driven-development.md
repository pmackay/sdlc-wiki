---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); GitHub/spec-kit (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Test-driven development (red-green-refactor)

Write a failing test first (red), make it pass with the simplest code (green), then refactor
— repeat. Gives the agent ground-truth feedback before it commits to an implementation, a
direct answer to "the code doesn't work."

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-tdd]] — dedicated red-green-refactor skill.

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

Now a strong multi-framework cluster. Spec Kit is the strictest by *mechanism* — test-first is
mandated by [[artifact-constitution|the project constitution]] (Article III) — while Superpowers
matches its non-negotiability by *rhetoric*: any production code written before its test must be
deleted and rewritten from the test.

## See Also
- [[pattern-systematic-debugging]] — the sibling feedback loop for bugs.
- [[stage-implement]] — the stage where this applies.
