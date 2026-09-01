---
type: sdlc-stage
aka: { gsd: "Plan", matt-pocock-skills: "to-tickets / design / research", addy-agent-skills: "Plan / task breakdown", openspec: "propose (design.md + tasks.md)", speckit: "plan + tasks + analyze", bmad: "Solutioning (architecture + epics/stories) + sprint/story prep", compound-engineering: "plan (guardrails) + doc-review", gstack: "plan reviews (CEO/eng/design/DX) + autoplan + design-consultation", superpowers: "writing-plans", seeds: "plan (prompt → submit) + create/dep", beads: "mol pour (formula instantiation)" }
sources: "Synthesized from GSD + Matt Pocock + Addy Osmani + OpenSpec + Spec Kit + BMAD + Compound Engineering + gstack + Superpowers + Seeds + Beads (2026)"
updated: 2026-08-31
---

# Stage: Plan

Canonical lifecycle stage: **research, design, and decompose work into verified units** — turning an approved specification into an ordered set of implementable, acceptance-checked tasks. Name kept in the re-derivation — "plan" is already framework-neutral. The *specify* activity (authoring the spec/PRD itself) was **split out** to [[stage-specify]] on the 2026-07-04 ingest; one candidate (design) remains parked (see [Split candidates](#split-candidates)).

**Derived projection** — evidence is the capabilities that `implements: [[stage-plan]]`.

## Implemented by (backlinks)

GSD:

- [[gsd-plan-phase]] — orchestrates research → plan → verification loop.
- [[gsd-phase-researcher]] — parallel domain research → [[artifact-research-md]].
- [[gsd-planner]] — atomic plans → [[artifact-plan-md]].
- [[gsd-plan-checker]] — eight-dimension plan gate ([[pattern-plan-verification-loop]]).

Matt Pocock — Skills for Real Engineers:

- [[mp-to-tickets]] — decompose into tracer-bullet tickets with blocking edges → [[artifact-issue]] ([[pattern-vertical-slice]]).
- [[mp-domain-modeling]] — build the domain model → [[artifact-domain-model]].
- [[mp-codebase-design]] — design deep modules ([[pattern-deep-modules]]).
- [[mp-research]] — background primary-source investigation → [[artifact-research-md]] (v1.1; counterpart to [[gsd-phase-researcher]]).

Addy Osmani — Agent Skills:

- [[addy-planning]] — decompose the spec into small, verifiable, dependency-ordered tasks → [[artifact-plan-md]] ([[pattern-vertical-slice]]).

Spec Kit:

- [[speckit-plan]] — technical plan + design (`plan.md`/`data-model.md`/`contracts/`) + [[artifact-research-md]], gated against the constitution.
- [[speckit-tasks]] — decompose the plan into a `[P]`-parallelizable, test-first task list → [[artifact-plan-md]].
- [[speckit-analyze]] — cross-artifact consistency & coverage gate ([[pattern-plan-verification-loop]]).
- [[speckit-taskstoissues]] — export the task list to GitHub issues → [[artifact-issue]].

BMAD:

- [[bmad-architect]] — the Solutioning persona (Winston).
- [[bmad-architecture]] — the invariants-only architecture spine → [[artifact-architecture]].
- [[bmad-create-epics-and-stories]] — decompose requirements into epics of stories → [[artifact-story]] ([[pattern-vertical-slice]]).
- [[bmad-check-implementation-readiness]] — PASS/CONCERNS/FAIL readiness gate ([[pattern-plan-verification-loop]]).
- [[bmad-sprint-planning]] — generate the sprint backlog/status from epics.
- [[bmad-create-story]] — author the context-filled story spec → [[artifact-story]] ([[pattern-context-engineering]]).
- [[bmad-correct-course]] — mid-flight re-planning valve.

Compound Engineering:

- [[ce-plan]] — enrich requirements into implementation-ready **guardrails** with U-IDs + test scenarios → [[artifact-plan-md]] (the WHAT; ~40% of dev time — the 80/20 front-load).
- [[ce-doc-review]] — persona fan-out over the requirements/plan *before* code ([[pattern-plan-verification-loop]] via [[pattern-parallel-persona-review]]).

gstack (a persona **plan-review panel**, distinctive here — gstack reviews the plan in plan-mode rather than authoring a checklist):

- [[gstack-plan-ceo-review]] — CEO/founder scope review; find the 10-star product; four scope modes.
- [[gstack-plan-eng-review]] — Eng-Manager review; lock architecture/data-flow/edge-cases/tests ([[pattern-plan-verification-loop]]).
- [[gstack-plan-design-review]] — Senior-Designer review; rate each design dimension 0-10.
- [[gstack-plan-devex-review]] — DX-Lead review; TTHW, personas, friction traces.
- [[gstack-autoplan]] — run the panel (CEO→design→eng→DX) with auto-decisions + smart review routing ([[pattern-parallel-persona-review]], [[pattern-scale-adaptive-planning]]).
- [[gstack-plan-tune]] — self-tune the panel's question sensitivity (meta).
- [[gstack-design-consultation]] — build the `DESIGN.md` design system from scratch → [[artifact-design-md]] (design flavor).

Superpowers:

- [[sp-writing-plans]] — decompose the approved design into bite-sized (2-5 min) tasks with exact files, complete code, interfaces, and verification steps → [[artifact-plan-md]] ([[pattern-vertical-slice]], [[pattern-test-driven-development]]); distinctive for baking the TDD micro-loop into every task and forbidding placeholders outright.

Seeds — a [store](../store/index.md), not a framework, and the only implementation of this stage that is a **program** rather than a prompt (see [Stores on the stage map](index.md#stores-on-the-stage-map) for how to weight store evidence):

- [[seeds-plan-prompt]] — emit the template-driven planning request an LLM fills, enriched with mulch prior art ([[pattern-knowledge-compounding]], [[pattern-source-grounding]]).
- [[seeds-plan-submit]] — AJV-validate the filled plan, spawn one child seed per step, translate the step `blocks` indices into real dependency edges → [[artifact-plan-record]] + [[artifact-issue]] ([[pattern-plan-verification-loop]], [[pattern-deterministic-gates]], [[pattern-vertical-slice]]).
- [[seeds-plan-validate]] — re-run the gate against the *current* template, so a rule tightened after a failure applies to plans already in flight.
- [[seeds-plan-edit]] — field-level plan fixes that propagate to the spawned child seeds.
- [[seeds-plan-create]] · [[seeds-plan-adopt]] · [[seeds-plan-release]] · [[seeds-plan-reorder]] — compose a plan from work that already exists, and pin the order a runtime will execute it in.
- [[seeds-create]] — file one unit of work directly; the low-ceremony tier of the framework's explicit two-tier dial ([[pattern-scale-adaptive-planning]]).
- [[seeds-dep]] · [[seeds-block]] — the dependency edges that decide what [[seeds-ready]] will hand out.
- [[seeds-tpl-pour]] — instantiate a stored convoy template into a serially-wired chain of issues; decomposition as a macro rather than as reasoning.
- [[seeds-issue-workflow]] — the skill that routes a vague ask between the create and plan paths.

Beads — the other [store](../store/index.md), with exactly one on-stage capability by charter:

- [[beads-mol]] — `bd mol pour` instantiates a **formula** (a declarative TOML DAG, compiled to a template by [[beads-cook]]) into real, dependency-ordered beads that flow through the ready frontier → [[artifact-issue]] ([[pattern-wave-parallelism]], [[pattern-vertical-slice]]). Decomposition **stamped from a reusable template** rather than reasoned out per task — closer to a macro than to planning, which is why beads' charter tolerates it while forbidding *"workflow semantics"* generally. `bd mol distill` runs it backwards, extracting a formula from an epic that already happened.
OpenSpec **folds this in**: [[openspec-propose]] emits [[artifact-design-md]] (`design.md`, the *how*) and [[artifact-plan-md]] (`tasks.md`, the numbered checklist) as part of the same one-step proposal that authors the spec — so its `implements:` edge points at [[stage-specify]], but the design + task-decomposition work lands here. BMAD, by contrast, gives design its own **Solutioning phase** (architecture + decomposition), distinct from its Planning/specify phase.

## Cross-framework equivalents
Seven frameworks share the **vertical-slice / decompose** technique: Matt's [[mp-to-tickets]] ↔ GSD's [[gsd-plan-phase]] `--mvp` ↔ Addy's [[addy-planning]] ↔ Spec Kit's [[speckit-tasks]] ↔ BMAD's [[bmad-create-epics-and-stories]] ↔ Superpowers' [[sp-writing-plans]], plus both stores ([[seeds-plan-submit]], [[beads-mol]]), clustered at [[pattern-vertical-slice]] — Superpowers' is distinctive for the task granularity (each task is the smallest unit carrying its own test cycle) and for embedding the TDD steps directly in the plan. The **plan-verification** gate is now a **six-framework** cluster: GSD's [[gsd-plan-checker]] ↔ Spec Kit's [[speckit-analyze]] ↔ BMAD's [[bmad-check-implementation-readiness]] ↔ Compound Engineering's [[ce-doc-review]] ↔ gstack's [[gstack-plan-eng-review]] ↔ Seeds' [[seeds-plan-submit]] ([[pattern-plan-verification-loop]]) — and Seeds is the one that breaks the mould, gating on an AJV schema generated from the project's plan template rather than on a model's judgment: un-arguable, and blind to everything except shape — CE and **gstack** are distinctive in gating with a **parallel persona fan-out** ([[gstack-autoplan]] runs a whole review panel) rather than a single multi-dimension checker. On design granularity the frameworks diverge: GSD folds design into planning (the [[gsd-planner]]) and Addy folds it into the build phase ([[addy-api-design]]), while Matt breaks it out into dedicated [[mp-domain-modeling]] / [[mp-codebase-design]] skills and Spec Kit emits dedicated design artifacts (`data-model.md` + `contracts/`, the [[pattern-contract-first]] surface) within [[speckit-plan]] — same underlying activity, different placement (see the design split candidate below).

## Split candidates
Two candidates remain parked to split into their own canonical stage **once ≥2 frameworks evidence the finer distinction as a distinct phase** (per the re-derivation rules in [CONVENTIONS.md](../CONVENTIONS.md)). Review on every ingest.

> **Resolved 2026-07-04:** `stage-specify` (author the spec/PRD) was **promoted** to a canonical stage — Addy's [[addy-spec-driven-development]] became the second framework to treat spec authoring as its own step (with Matt's [[mp-to-spec]]), clearing the bar. See [[stage-specify]].

### stage-schedule (order already-planned units for execution)
- **Distinction:** *decompose* = produce the units; *schedule* = fix the order and gating in which existing units run. The two are usually the same act, but seeds separates them into different commands with different inputs.
- **Evidence so far (two *stores*, no framework — still short of the bar):**
  - Seeds treats scheduling as its own surface: [[seeds-plan-create]] makes a plan with **zero** decomposed steps, [[seeds-plan-adopt]] pulls in work that already exists, and [[seeds-plan-reorder]] pins the order with a permutation check — a "release train" whose whole content is ordering. Nothing is decomposed at any point.
  - Beads goes further and expresses *coordination* as data: [[beads-gate]] parks a step on a human decision, a timer, or a GitHub run by making the wait a blocking bead, and [[beads-merge-slot]] serializes trunk merges the same way — scheduling constraints stored rather than reasoned. Its charter is explicit that the *deciding* belongs elsewhere.
  - Both are [stores](../store/index.md) rather than frameworks, and per the [store-evidence rule](index.md#stores-on-the-stage-map) a candidate stage evidenced only by stores has not cleared the bar — a store expresses a constraint as state; that is not the same as a framework treating scheduling as a lifecycle step.
  - The rest of the evidence sits in the [execution layer](../runtime/index.md), which implements no stage by construction: [[warren]]'s plan-run walks `plan.children` verbatim, one run per child, gated on PR merge; [[bernstein]] batches a task DAG topologically in deterministic Python (*"zero LLM tokens on coordination"*). Both consume an order rather than deciding one.
  - Every other framework folds ordering into decomposition — [[speckit-tasks]]'s `[P]` markers, [[mp-to-tickets]]'s blocking edges, [[sp-writing-plans]]'s ordered bite-sized tasks — so no second *framework* treats it as a distinct step.
- **Decisive trigger:** a **framework** with a capability that orders or re-orders work it did not itself decompose → paired with either store, clears the bar → split into `stage-schedule`. Until then the runtime evidence stays filed where it belongs, as [[pattern-wave-parallelism]] and the runtimes' `enables:` edges.
### stage-design (design deep modules / architecture)
- **Distinction:** *design* = shape module boundaries and interfaces; distinct from *decompose into tasks*.
- **Evidence so far (still borderline — one framework treats it as a distinct *phase*):**
  - Matt Pocock **splits it out pre-build**: [[mp-domain-modeling]] + [[mp-codebase-design]] ([[pattern-deep-modules]]) are dedicated design skills in the plan/design stage.
  - Addy has a **dedicated design skill** too — [[addy-api-design]] (contract-first, [[pattern-contract-first]]) — but **folds it into the Build phase** rather than a distinct design step.
  - GSD **folds it in**: design happens inside [[gsd-planner]].
  - OpenSpec has a **dedicated design artifact** — [[artifact-design-md]] (`design.md`) — as a discrete step in its `proposal → specs → design → tasks` chain (generated one-at-a-time by `/opsx:continue` in the expanded profile), but it is still an artifact *inside* [[openspec-propose]], not a standalone lifecycle phase.
  - Spec Kit likewise emits **dedicated design artifacts** — `data-model.md` + `contracts/` (the [[pattern-contract-first]] surface) — but *within* [[speckit-plan]], not as a standalone phase.
  - BMAD has a **dedicated architecture capability** ([[bmad-architecture]] → [[artifact-architecture]]) and even a named **Solutioning phase** — but that phase *bundles* design with decomposition ([[bmad-create-epics-and-stories]]), so it isolates *plan-as-a-whole* as a phase, not *design distinct from decomposition*. So BMAD does not clear the finer distinction either.
  - So design is now a *dedicated capability/artifact* in **five** frameworks (MP splits it pre-build; Addy folds it into Build; OpenSpec and Spec Kit make it discrete artifacts within propose/plan; BMAD gives it a capability inside Solutioning), but a *distinct phase, isolated from task decomposition,* in only one (MP). Strengthening, still not decisive.
- **Decisive trigger:** a framework that treats design as its own lifecycle phase *distinct from task decomposition* (not folded into plan, propose, build, or a design+decompose solutioning phase) → clears the bar → split into `stage-design`.

## See Also
- [[stage-specify]] — authors the spec this stage decomposes (split out 2026-07-04).
- [[stage-align]] — supplies locked context.
- [[stage-implement]] — consumes the approved plan.
- [[artifact-plan-record]] — the stage's one non-prose output form, and the reason its ordering is executable rather than advisory.
