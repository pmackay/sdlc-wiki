---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: ["[[mp-tdd]]", "[[mp-code-review]]"]
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-test-driven-development]]", "[[pattern-vertical-slice]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[openspec-apply]]", "[[speckit-implement]]", "[[addy-incremental-implementation]]", "[[bmad-dev-story]]", "[[ce-work]]", "[[sp-executing-plans]]"]
docs_url: "https://www.aihero.dev/skills-implement"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-08-31
---

# implement

`/implement` — a user-invoked engineering skill that **builds the work described by a spec or a set of tickets**. It drives [[mp-tdd]] where possible at pre-agreed seams, runs typechecking and single test files regularly (full suite once at the end), closes out by running [[mp-code-review]], and commits to the current branch → [[artifact-atomic-commit]].

**New in v1.1 (2026-07-09).** This is the first time Matt Pocock's toolkit has a first-class *execute* skill — previously "building" was only the test-first [[mp-tdd]] and throwaway [[mp-prototype]]. `implement` makes MP a full member of the cross-framework **execute** cluster: walk the plan/tickets unit-by-unit, test-driven — alongside [[gsd-execute-phase]], [[openspec-apply]], [[speckit-implement]], [[addy-incremental-implementation]], [[bmad-dev-story]], and [[ce-work]]. It is the tail of MP's main flow: `idea → grill → to-spec → to-tickets → implement (per ticket, fresh context) → code-review`.

## See Also
- [[mp-to-tickets]] — produces the tickets this builds (one per fresh context window).
- [[mp-tdd]] — the red-green engine this drives at seams.
- [[mp-code-review]] — the quality gate this runs before committing.
- [[pattern-deterministic-gates]] — the continuous typecheck/test discipline it runs while building.
- [[gsd-execute-phase]] · [[speckit-implement]] · [[ce-work]] · [[bmad-dev-story]] — execute-cluster counterparts.
- [[stage-implement]] — the canonical stage this implements.
