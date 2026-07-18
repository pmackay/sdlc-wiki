---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-wave-parallelism]]"]
equivalent_to: []
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# dispatching-parallel-agents

Handle **2+ independent problems concurrently** by dispatching one focused subagent per problem
domain, then integrating ([[pattern-fresh-context-subagents]]). *"Dispatch one agent per independent
problem domain. Let them work concurrently."* The canonical trigger is multiple unrelated test files
failing for different root causes — investigating them sequentially wastes time when each is
independent.

The pattern: **identify independent domains** (no shared state) → **create focused agent tasks** (each
gets a specific scope, a clear goal, constraints like *"do NOT change production code"*, and an
expected output) → **dispatch in parallel** (all subagent calls in one response = concurrent; one per
response = sequential) → **review and integrate** (read summaries, check for conflicts, run the full
suite). A Common-Mistakes list guards the failure modes: too-broad scope, no context, no constraints,
vague output. It explicitly says **not** to use it for *related* failures (fix one may fix others),
when you need whole-system context, or when agents would fight over the same files.

Related but distinct from [[gsd]]'s [[pattern-wave-parallelism]] (which adds dependency-ordering of
waves) and the persona fan-outs ([[addy-shipping]]'s `/ship`, [[gstack-autoplan]]'s panel): those run
*specialists on one artifact*; this runs *one generalist per independent bug/subsystem*. No single
cross-framework counterpart is paged — it is Superpowers' explicit codification of concurrent
fresh-context dispatch. (Not set `equivalent_to`.)

## See Also
- [[sp-subagent-driven-development]] — the sequential per-task dispatch engine (this is its concurrent-independent-problems sibling).
- [[gsd-execute-phase]] — GSD's dependency-ordered [[pattern-wave-parallelism]] executor.
- [[pattern-fresh-context-subagents]] · [[pattern-wave-parallelism]] — the techniques applied.
- [[stage-implement]] — the canonical stage this implements.
