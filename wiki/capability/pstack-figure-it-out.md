---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-plan]]"
delegates_to: ["[[pstack-architect]]", "[[pstack-arena]]", "[[pstack-show-me-your-work]]"]
produces: ["[[artifact-plan-md]]", "[[artifact-decision-log]]"]
applies: ["[[pattern-scale-adaptive-planning]]", "[[pattern-evidence-before-claims]]", "[[pattern-deterministic-gates]]", "[[pattern-vertical-slice]]", "[[pattern-worktree-isolation]]"]
equivalent_to: ["[[mp-wayfinder]]", "[[gsd-plan-phase]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /figure-it-out

**When the task matches no playbook, design one.** The escape hatch from [[pstack-poteto-mode]]'s twenty-three bundled playbooks, and the framework's nearest thing to a planning capability — notable because pstack otherwise refuses to plan on principle (*"i don't believe in planning. the best spec is code"*). The deliverable before any code is **the workflow itself**.

Its routing is precise. A large or cross-cutting effort — a migration across many call sites, an ambitious multi-part change, or work the user steps away from to trust later — comes here **even when a narrower playbook like Feature fits**. A standing project-scale program routes to the Orchestrate playbook instead. *figure-it-out designs one bespoke run; orchestrate runs the program.*

- **A. Frame.** Do not start until the definition of done is stated as a **falsifiable predicate**, scope is quantified in rough units and effort with the blockers grounding surfaced, and a rigor level is chosen — **biased high**, with one-way doors and high blast radius getting more and reversible low-stakes steps getting less. *Rigor is gates and artifacts, not "try harder".* A multi-hour run earns one checkpoint even though reversible work otherwise proceeds. This is the wiki's most explicit [[pattern-scale-adaptive-planning]] statement: where [[bmad]] and [[nano-spec]] size the *ceremony* to the change, figure-it-out sizes the **evidence burden** to the blast radius.
- **B. Design the workflow.** Decompose into atomic, independently-landable units, sequenced riskiest-unknown-first. **Build the verification harness before the work**, with the baseline captured from the pre-change state so every check reads as "old value vs new value". Run [[pstack-architect]] for one-way-door design decisions and skip it for mechanical work — *a second arena over a settled design is over-engineering*. Parallelize only across seams, each worker in its own worktree or branch. Write the designed phase list down; that list is what the human reviews.
- **C. Run the loop.** Each unit is an experiment: state the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced and revert it if it did not. *When something passes too easily, suspect the observation method before the system.* Delegated work is paired with a judge and audited directly. **A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Do not hide a negative.** If a worker games the gate, reset and harden the contract; if the gate itself is wrong, fix the gate in its own change rather than routing around it.
- **D. Keep the audit trail** via [[pstack-show-me-your-work]], woven through as each step lands rather than saved for the end.
- **E. Verify and hand back** against the Phase A predicate on the real product, not just the harness, and encode any recurring correction as a gate, lint rule, check, or script.

## See Also
- [[pstack-show-me-your-work]] — the Phase D trail.
- [[pstack-architect]] — the Phase B design decision path.
- [[pstack-poteto-mode]] — routes here whenever no bundled playbook fits.
- [[mp-wayfinder]] — the counterpart that maps an oversized effort as investigation tickets; [[gsd-plan-phase]] — the plan-then-verify loop.
- [[stage-plan]] — the canonical stage this implements.
