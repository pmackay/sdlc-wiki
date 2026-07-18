---
type: pattern
sources: "Addy Osmani — Agent Skills (2026)"
updated: 2026-07-04
---

# Pattern: Shift Left

Move quality gates — tests, linting, type checks, security scans — as **early** in the
lifecycle as possible: into the developer's loop and the CI pipeline rather than a late,
separate QA phase. Catching a defect where it is introduced is cheaper than catching it
downstream, so "faster is safer": tight, automated feedback loops let teams ship quickly
*because* the guardrails run continuously.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-ci-cd]] — Shift Left, Faster is Safer, quality-gate pipelines, failure feedback loops.

## See Also
- [[pattern-test-driven-development]] — the earliest-possible quality gate: a test before the code.
- [[pattern-trunk-based-development]] — the integration discipline that makes fast, safe shipping work.
- [[stage-release]] — the stage this pattern serves.
