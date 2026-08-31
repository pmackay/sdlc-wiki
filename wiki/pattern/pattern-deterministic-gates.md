---
type: pattern
sources: "gstack — Garry Tan (2026); Addy Osmani — Agent Skills (2026); EveryInc/compound-engineering-plugin (2026); Matt Pocock — Skills for Real Engineers (2026); obra/superpowers (2026); Martin Fowler — 'Harness Engineering' (2026); sipyourdrink-ltd/bernstein (2026); mattpocock/sandcastle (2026)"
updated: 2026-08-31
---

# Pattern: Deterministic gates (let a program decide, not a model)

Gate the agent's work on checks whose verdict is **computed by a program** — a linter, a type checker, a test suite, a build, a security scanner — rather than inferred by a model. The check runs a command, reads an exit code, and returns pass or fail. It is cheap (milliseconds to seconds), reproducible across runs, and **un-gameable**: an agent can talk its way past a reviewer's judgment, but it cannot talk `pytest` into exiting 0.

The practical rule, in Martin Fowler's framing: **prefer a computational control when one exists**, and reserve inferential controls — LLM review, adversarial critique, a second model's opinion — for the semantic judgments no linter can make. The two are complements, not competitors: deterministic gates cover the large, boring surface cheaply so the expensive inferential sensors are spent only where judgment is actually required.

## Why it's distinctive

This is the **computational** half of the sensor split that [[topic-harness-engineering]] draws, and the wiki already carries three nodes for the *inferential* half — [[pattern-adversarial-review]], [[pattern-cross-model-review]], [[pattern-parallel-persona-review]]. This page is the missing counterweight.

It sits close to three neighbours and is distinct from each:

- **[[pattern-shift-left]]** answers *when* — push checks as early as possible. This pattern answers *what kind* — the verdict is computed, not judged. The axes are orthogonal: a deterministic gate can run late (a merge gate) and an inferential one can run early (a plan checker).
- **[[pattern-evidence-before-claims]]** is an **honesty discipline** — do not *assert* done without proof. This pattern is a **gate** — the work does not proceed, whether or not anyone claimed anything. They overlap in practice ([[sp-verification-before-completion]] applies both, since the evidence it demands is a command's exit code) but they fail differently: violate evidence-before-claims and you get a false statement; violate a deterministic gate and you get a blocked merge.
- **[[pattern-test-driven-development]]** is one *instance* of a deterministic gate placed at the earliest possible point, plus an ordering discipline (red before green) this pattern does not require.

Its second distinguishing property is **where it can live**. An inferential review needs a model, so it is always a process-layer act. A deterministic gate is just a command, so it can be pushed down the stack — into a runtime's merge pipeline, or a harness hook — where no skill has to remember to ask for it. That is what makes it the pattern the substrate layers reach for first.

## Applied by (backlinks)

gstack:

- [[gstack-health]] — the purest instance: a standing dashboard aggregating type checker, linter, tests, and dead-code detection into one always-on readout, with no model in the verdict.

Addy Osmani — Agent Skills:

- [[addy-ci-cd]] — a sequential quality-gate pipeline (lint → type check → tests → build → security audit) where **no gate can be skipped**: *"if lint fails you fix lint, you don't disable the rule"*, plus a failure feedback loop piping CI errors straight back to the agent.

Compound Engineering:

- [[lfg]] — the autonomous loop's terminal condition is a *machine-checked* one: it watches CI until green and returns only when the PR is merge-ready.

Matt Pocock — Skills for Real Engineers:

- [[mp-implement]] — runs typechecking and single test files continuously during the build, with the full suite once at the end.

Superpowers:

- [[sp-verification-before-completion]] — its gate function is mechanical: identify the command that proves the claim → run it fresh → **read the exit code and count failures** → only then speak. The deterministic-gate half of a skill whose thesis is honesty.

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) is where this pattern stops being a skill an agent may forget and becomes a condition of merging:

- [[bernstein]] (platform) — the fullest realization: a configurable **gate pipeline** of named checks (lint · type_check · tests · security_scan · pii_scan · coverage_delta · dep_audit · mutation_testing · …), each with a `required` flag and an execution condition, run on the diff after every agent completion. A failing *required* gate hard-blocks merge; a failing *optional* gate is reported only. Commands are repo-configurable (`lint_command`, `test_command`, …), results are cached while the diff is unchanged, and custom checks plug in as `GatePlugin` classes via `.bernstein/gates/*.py` or a `bernstein.gates` entry point. Alongside it the janitor's declarative **completion signals** (`path_exists`, `glob_exists`, `test_passes`, `file_contains`) gate the individual task the same way.
- [[sandcastle]] (library) — the script-it-yourself version: `sandbox.exec()` runs a shell command in the warm sandbox so a pipeline can gate an implement step on `npm test` before dispatching the review run.

## See Also
- [[pattern-shift-left]] — *when* to run the gate (as early as possible); this pattern is *what kind* of gate it is.
- [[pattern-evidence-before-claims]] — the honesty discipline whose proof is usually a deterministic gate's output; distinct in what failure means.
- [[pattern-test-driven-development]] — a deterministic gate placed at the earliest possible point, plus a red-green ordering rule.
- [[pattern-adversarial-review]] · [[pattern-cross-model-review]] · [[pattern-parallel-persona-review]] — the *inferential* sensors this pattern is the complement to; spend them on judgments no command can make.
- [[pattern-plan-verification-loop]] — the same gate-then-revise shape applied to a plan rather than a diff (and largely inferential, since plans have no exit code).
- [[pattern-edit-guardrails]] — *preventive* rather than detective: it blocks a disallowed action up front instead of failing the work afterwards.
- [[topic-harness-engineering]] — Fowler's computational/inferential control split, and the *"prefer a computational control when one exists"* rule this pattern states.
- [[stage-validate]] · [[stage-review]] — the stages these gates most often police.
- [[bernstein]] · [[sandcastle]] — the runtimes that provide the gate as substrate.
