---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-validate]]"
produces: "[[artifact-plan-md]]"
equivalent_to: ["[[openspec-verify]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-converge

**`/speckit.converge`** — "Assess the codebase against spec/plan/tasks and append remaining
work as new tasks." A brownfield/iterative loop-closer: it measures the actual code against
the intended spec, plan, and task list, identifies the gap, and **appends the outstanding
work back into `tasks.md`** ([[artifact-plan-md]]) — turning drift between intent and
implementation into a fresh backlog.

## A validate-then-replan bridge

The assessment half — comparing implementation against the spec — is a [[stage-validate]]
activity, which is why it clusters with:

- [[openspec-verify]] — validate implementation vs the spec artifacts (completeness /
  correctness / coherence).

The difference: OpenSpec's verify is advisory and non-blocking (it *reports*), whereas
Spec Kit's converge is action-oriented — it *writes new tasks*, feeding [[stage-plan]] and
another [[speckit-implement]] pass. It is the concrete embodiment of Spec Kit's
"bidirectional feedback" principle: implementation reality flows back to reshape the plan.

## See Also
- [[speckit]] — the framework.
- [[speckit-implement]] — the pass whose output converge assesses; converge feeds the next one.
- [[bmad-correct-course]] — BMAD's related mid-flight re-planning valve; both fold reality back into the plan, but converge is driven by measured spec-drift while correct-course responds to a deliberate scope change.
- [[stage-validate]] — the canonical stage.
