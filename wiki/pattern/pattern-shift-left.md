---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); Martin Fowler — 'Harness Engineering' (2026)"
updated: 2026-08-05
---

# Pattern: Shift Left

Move quality gates — tests, linting, type checks, security scans — as **early** in the lifecycle as possible: into the developer's loop and the CI pipeline rather than a late, separate QA phase. Catching a defect where it is introduced is cheaper than catching it downstream, so "faster is safer": tight, automated feedback loops let teams ship quickly *because* the guardrails run continuously.

In the agent era Martin Fowler restates this as **"keep quality left"**: distribute an agent's sensors (feedback controls) across the whole lifecycle so recurring failures are caught at the cheapest point. Under autonomy the case sharpens — a stray agent edit caught by a pre-commit hook never reaches review. See [[topic-harness-engineering]] for the guides/sensors control-system frame this sits inside.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-ci-cd]] — Shift Left, Faster is Safer, quality-gate pipelines, failure feedback loops.

## See Also
- [[pattern-test-driven-development]] — the earliest-possible quality gate: a test before the code.
- [[pattern-trunk-based-development]] — the integration discipline that makes fast, safe shipping work.
- [[topic-harness-engineering]] — Fowler's "keep quality left" and the guides/sensors control system.
- [[stage-release]] — the stage this pattern serves.
