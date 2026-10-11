---
type: pattern
sources: "gstack — Garry Tan (2026); Addy Osmani — Agent Skills (2026); EveryInc/compound-engineering-plugin (2026); Matt Pocock — Skills for Real Engineers (2026); obra/superpowers (2026); Martin Fowler — 'Harness Engineering' (2026); sipyourdrink-ltd/bernstein (2026); mattpocock/sandcastle (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026); github/gh-aw (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-10-11
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
- [[mp-retro]] — turns harvested lessons *into* gates: a mechanical coding-standards violation "gets a deterministic check, full stop" (linter rule, pre-commit hook, CI job), and a repo with no guardrail is itself a finding (v1.3.0).

Superpowers:

- [[sp-verification-before-completion]] — its gate function is mechanical: identify the command that proves the claim → run it fresh → **read the exit code and count failures** → only then speak. The deterministic-gate half of a skill whose thesis is honesty.

Seeds — the wiki's first framework that is itself a program, so its gates are the framework rather than something bolted onto it:

- [[seeds-plan-submit]] — an AJV schema generated from the project's plan template gates the plan before any child seed is spawned; fail-fast, pre-write, exit-code verdict.
- [[seeds-plan-validate]] — re-runs that gate against the *current* template, so tightening a rule after a failure applies retroactively to plans in flight.
- [[seeds-doctor]] — data-integrity checks over the store (gitattributes drift, non-object `extensions`) with `--fix`.

Beads — four program-decided checks, each with an exit code and no model involved:

- [[beads-doctor]] — installation and data health, and the single consolidation point for remediation (*"don't create separate commands like `bd recover`"*), including orphan detection against git history.
- [[beads-graph]] — `bd graph check` on the dependency graph's structural invariants.
- [[beads-lint]] — the unusual one: a linter for the *content of work items*, flagging beads whose template sections are empty before someone claims them.
- [[beads-preflight]] — a pre-PR checklist over the working tree, `--check` to run it.

pstack:

- [[pstack-reflect]] — a **structural-enforcement check** that re-reads its own synthesizer's Accepted list and demotes to Backlog any learning better served by a lint rule, script, metadata flag, or runtime check. A gate on the framework's own growth.
- [[pstack-no-comments]] — offers the cheapest in-scope type, runtime, test, or CI lint that makes a claimed constraint enforceable, then **encodes it and deletes the comment**.
- [[pstack-swarm]] — workers report `PASS`, `ISSUES`, or `BLOCKED` with evidence, and the race selection rule is declared **before spawning**, not after reading the results.
- [[pstack-maintain-verification-skill]] — a run declares one of **clean / changed / blocked** up front.
- [[pstack-principle-encode-lessons-in-structure]] — the principle: encode the rule as a check, not as more text.

Tessl — the [supply layer](../registry/index.md)'s gates, several of them metered because the judge costs money:

- [[tessl-review]] — `--threshold` fails the build when a skill scores below the bar, so substandard skills never merge.
- [[tessl-review-security]] — fails CI on a high or critical finding.
- [[tessl-change-verify]] — LLM-judge verifiers over changed files, with a **call ceiling that refuses broad runs** (default 300), deterministic sampling, verdict caching, and a dry-run that spends no judge calls. What a deterministic gate looks like when the "program" deciding it is a model.
- [[tessl-change-risk]] — exits non-zero when human review is required.
- [[tessl-code-review]] — versioned, pinnable review **lenses** as a PR gate.
- [[tessl-workspace]] — install and publish policies, and required skills, enforced across every workspace.

builder-skills (gates bound to the live head):

- [[builder-factory-babysit-pr]] — evidence tied to the exact current head, conditional merge only when the host can guarantee it, and a **soak**, an unchanged interval that *"missing history does not satisfy."*
- [[builder-factory-review-prs]] — re-read the exact head immediately before approval or merge, and restart the soak on any change.
- [[builder-factory-ship]] — configured formatter, tests, and release checks, with a head-match guard on merge. See [[pattern-action-gating]] for the per-action authority layer these gates sit under.

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) is where this pattern stops being a skill an agent may forget and becomes a condition of merging:

- [[bernstein]] (platform) — the fullest realization: a configurable **gate pipeline** of named checks (lint · type_check · tests · security_scan · pii_scan · coverage_delta · dep_audit · mutation_testing · …), each with a `required` flag and an execution condition, run on the diff after every agent completion. A failing *required* gate hard-blocks merge; a failing *optional* gate is reported only. Commands are repo-configurable (`lint_command`, `test_command`, …), results are cached while the diff is unchanged, and custom checks plug in as `GatePlugin` classes via `.bernstein/gates/*.py` or a `bernstein.gates` entry point. Alongside it the janitor's declarative **completion signals** (`path_exists`, `glob_exists`, `test_passes`, `file_contains`) gate the individual task the same way.
- [[sssf]] (library) — the pattern reduced to its economics and then enforced as a hard rule: *"A known command is code, not an agent"*, so anything whose invocation you can write down (`bun test`, `ruff check`) becomes a `kind="code"` phase rather than an agent phase, and its result reaches the next agent through the same envelope door an agent's report would have used. Alongside it, a gate is one callable — `gate(envelope, run) -> GateReport` — attached per call site, returning one `{item, ok, note}` check per thing it examined so a *green* gate records what it verified. Both the rule and the argument for it are unusually explicit: an agent rediscovering your test runner *"burns a context window to learn what a subprocess already knows, and it charges you for the privilege every single run."*
- [[sandcastle]] (library) — the script-it-yourself version: `sandbox.exec()` runs a shell command in the warm sandbox so a pipeline can gate an implement step on `npm test` before dispatching the review run.
- [[gh-aw]] (platform) — gates at two unusual points in the timeline. *Before anything runs*: `gh aw compile` refuses to emit a lock file that fails schema validation, expression allowlisting, action SHA pinning, or the `actionlint`/`zizmor`/`poutine` scanners — a deterministic gate on the *workflow itself*, left of execution entirely. *After the agent, before any write*: an isolated threat-detection job (a different agent plus optional deterministic steps such as TruffleHog) must return a passing verdict before any safe-output job executes. The honest scope note: these gate *safety*, not work quality — correctness gating is delegated to the CI of the PR the workflow opens.

## Persisted by (store)

- [[beads]] — four program-decided checks over the store and the tree: [[beads-doctor]], [[beads-graph]]'s integrity check, [[beads-lint]] (a linter for *work-item content*, not code), and [[beads-preflight]].
- [[seeds]] — the AJV plan gate on [[seeds-plan-submit]] and the integrity checks in [[seeds-doctor]].

Distinct from the infrastructure roster: a runtime gates the *work* before it merges, a store gates *its own state* — cycles, dangling edges, under-specified beads, drifted config.

## Supplied by (registry)

- [[tessl]] — the [supply layer](../registry/index.md) makes the gate a property of **distribution**: a skill cannot be published without a review score, cannot be installed against policy, and cannot merge below a threshold. The enforcement point is the index rather than a step in anyone's workflow, which is what makes it hold across an organization that has not agreed on a methodology.

## See Also
- [[pattern-tooling-leverage]] — the lever a lesson becomes once it is worth enforcing mechanically.
- [[pattern-shift-left]] — *when* to run the gate (as early as possible); this pattern is *what kind* of gate it is.
- [[pattern-evidence-before-claims]] — the honesty discipline whose proof is usually a deterministic gate's output; distinct in what failure means.
- [[pattern-test-driven-development]] — a deterministic gate placed at the earliest possible point, plus a red-green ordering rule.
- [[pattern-adversarial-review]] · [[pattern-cross-model-review]] · [[pattern-parallel-persona-review]] — the *inferential* sensors this pattern is the complement to; spend them on judgments no command can make.
- [[pattern-plan-verification-loop]] — the same gate-then-revise shape applied to a plan rather than a diff (and largely inferential, since plans have no exit code).
- [[pattern-edit-guardrails]] — *preventive* rather than detective: it blocks a disallowed action up front instead of failing the work afterwards.
- [[topic-harness-engineering]] — Fowler's computational/inferential control split, and the *"prefer a computational control when one exists"* rule this pattern states.
- [[stage-validate]] · [[stage-review]] — the stages these gates most often police.
- [[bernstein]] · [[sandcastle]] — the runtimes that provide the gate as substrate.

- [[pattern-action-gating]] — the authority layer above these gates; a passing gate is necessary for an action, never sufficient.
