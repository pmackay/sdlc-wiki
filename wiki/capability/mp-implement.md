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
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.3.0 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# implement

`/implement` — a user-invoked engineering skill that **builds the work described by a spec or a set of tickets**. It drives [[mp-tdd]] where possible at pre-agreed seams, runs typechecking and single test files regularly (full suite once at the end), closes out by running [[mp-code-review]], and commits to the current branch → [[artifact-atomic-commit]].

It is Matt Pocock's member of the cross-framework **execute** cluster: walk the plan/tickets unit-by-unit, test-driven, alongside [[gsd-execute-phase]], [[openspec-apply]], [[speckit-implement]], [[addy-incremental-implementation]], [[bmad-dev-story]], and [[ce-work]].

In MP's main flow (`idea → grill → to-spec → to-tickets → implement → code-review → pr → retro`) it is the **per-ticket** build path: one ticket per fresh context window, with tdd + code-review each time. It is also the in-place path for work too small for a spec. Its parallel sibling [[mp-implement-spec]] builds a whole spec in one run instead: implementer subagents across the ready frontier, landing on one integration branch, with one [[mp-code-review]] at the end. When the work goes up as a PR, [[mp-pr]] shapes the body, and [[mp-retro]] follows as the main flow's last step.

## See Also
- [[mp-to-tickets]] — produces the tickets this builds (one per fresh context window).
- [[mp-tdd]] — the red-green engine this drives at seams.
- [[mp-code-review]] — the quality gate this runs before committing.
- [[mp-implement-spec]] — the parallel, whole-spec sibling.
- [[pattern-deterministic-gates]] — the continuous typecheck/test discipline it runs while building.
- [[gsd-execute-phase]] · [[speckit-implement]] · [[ce-work]] · [[bmad-dev-story]] — execute-cluster counterparts.
- [[stage-implement]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- [[mp-implement-spec]] added as the parallel, whole-spec alternative; `/implement` stays the per-ticket and in-place path. [[mp-pr]] and [[mp-retro]] joined the main flow after code-review.

### Added in v1.1.0 (2026-07-08; ingested 2026-07-09)
- The toolkit's first first-class *execute* skill. Before it, "building" was only the test-first [[mp-tdd]] and the throwaway [[mp-prototype]]. At the time it was the tail of the main flow, ending at code-review.
