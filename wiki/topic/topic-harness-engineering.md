---
type: topic
sources: "Martin Fowler — 'Harness Engineering' (2026, martinfowler.com); wiki synthesis; disler/super-simple-software-factory (2026)"
raw: ["../../raw/reference/2026-08-05-fowler-harness-engineering.md"]
updated: 2026-08-31
---

# Topic: Harness engineering — steering agents toward project conventions, and refining that over time

> **This page is a curated overlay, not an ontology node.** It gathers pages from across the wiki around one theme and links *out* to them; it stores no edges and changes no synthesis. See [CONVENTIONS §The topic layer](../CONVENTIONS.md#the-topic-layer-curated-overlays).

**The question this topic answers:** how do you make an agent deliver according to a project's conventions — and improve that alignment as the project (and the model) evolve? Martin Fowler's *Harness Engineering* gives the sharpest available frame, and it maps almost one-to-one onto pages this wiki already holds. This page threads them together.

## A terminology warning first

Fowler uses **"harness"** for *everything a team builds around the model to steer it* — explicitly **not** the CLI. His **builder harness** (vendor-baked system prompt, retrieval, orchestration) overlaps this wiki's [[claude-code|harness]]-node *primitives*; his **user harness** (the controls a team constructs) is what this wiki splits across the `pattern`, `artifact`, and harness-config layers.

So **Fowler's *harness* ≠ this wiki's `harness` node.** This wiki pins `harness` to the agent *program* ([[claude-code]], [[pi]], …); Fowler's harness is a broader control system. When reading across the two, translate: *Fowler-harness ≈ (this wiki's harness primitives) + (the patterns and artifacts a team applies on top).* This page uses Fowler's vocabulary for the *controls* — guides, sensors, steering loop — while keeping "harness" (unqualified) meaning the wiki's agent-program node.

## The control system: guides + sensors, closed by a steering loop

Fowler frames the whole apparatus as a **cybernetic governor** — a regulator with two arms:

- **Guides (feedforward controls)** — steer the agent *before* it acts, to raise first-attempt quality. The wiki's *prescribed / externalized-knowledge* pages.
- **Sensors (feedback controls)** — let the agent (or a reviewer) self-correct *after* it acts. The wiki's *verification / review* pages.
- **The steering loop** — "whenever an issue happens multiple times, the controls should be improved." The wiki's *knowledge-compounding* pages, pointed at the controls themselves.

"A well-built outer harness … increases the probability that the agent gets it right in the first place, *and* provides a feedback loop that self-corrects." Neither arm is sufficient alone.

### Guides (feedforward) — what the wiki already has

Externalized, project-specific knowledge the agent reads *before* acting — the standing answer to *"we don't do it that way here,"* which the model has no intuition for:

- [[pattern-project-constitution]] — the strongest form: immutable project-wide principles, **mechanically gated** ([[artifact-constitution]]). The prescribed pole.
- [[pattern-context-engineering]] — the machinery that loads guides into the window at the right moment: rules files, `CLAUDE.md` / `AGENTS.md`, packed context, MCP (the harness-side primitives on [[claude-code]], [[opencode]], [[pi]], [[factory-droid]]).
- [[pattern-source-grounding]] — one high-value guide: cited authoritative docs fed into context.
- [[artifact-adr]] — per-decision rationale, so a settled choice is not re-litigated.
- [[artifact-standards]] — a default-conventions doc a team overrides per project (Agent OS's signature; see [[agent-os]]).
- [[artifact-story]] / [[artifact-spec-md]] — context engineered *into* the work unit so a fresh agent starts fully briefed.
- [[pattern-anti-rationalization]] — page-level guardrail text that pre-empts the excuses an agent talks itself into (a feedforward "don't" guide).

### Sensors (feedback) — what the wiki already has

Checks applied *after* the agent acts, catching what the guides didn't prevent:

- [[pattern-plan-verification-loop]] — a sensor on the *plan* before any code (gate + revise).
- [[pattern-adversarial-review]] — a fresh-context reviewer prompted to *disprove* the work.
- [[pattern-parallel-persona-review]] · [[pattern-cross-model-review]] — fan-out and second-model sensors.
- [[pattern-evidence-before-claims]] — a self-check honesty gate: no "done" without fresh command output.
- [[pattern-test-driven-development]] — the earliest sensor of all: a failing test *before* the code.

Fowler's own split cuts *across* these sensors by cost and reliability:

- **Computational controls** — deterministic, fast (ms–s): tests, linters, type checkers. In the wiki this is now its own node, [[pattern-deterministic-gates]] — [[gstack-health]] (type/lint/tests/dead-code), the CI gates of [[addy-ci-cd]], [[lfg]]'s watch-CI-until-green stop condition — plus the hooks under [[pattern-edit-guardrails]].
- **Inferential controls** — semantic, AI-based ("LLM as judge"), slower and richer: [[pattern-adversarial-review]], [[pattern-cross-model-review]], and every review-persona capability ([[ce-code-review]], [[addy-code-review]], [[gstack-review]], [[bmad-code-review]]).

The practical rule Fowler implies: **prefer a computational control when one exists** (cheap, deterministic, un-gameable), and reserve inferential controls for the semantic judgments no linter can make. A *small verifier* is exactly how you promote an advisory guide into a sensor without bloating the rules file.

**The clearest independent statement of that rule in the wiki is [[sssf]]'s**, arrived at from cost rather than from control theory and written into the skill as a hard rule: *"A known command is code, not an agent — if you can write the invocation down (`bun test`, `ruff check`), it belongs in a `kind="code"` phase."* Its argument for the preference is the economic one Fowler leaves implicit: *"An agent rediscovering your test runner burns a context window to learn what a subprocess already knows, and it charges you for the privilege every single run. Worse, it puts a passing test suite into a context window, which buys you nothing at all."* Two structural consequences are worth borrowing. The shipped roster has **no tester agent at all** — the suite is code, so no persona exists for it. And a computational control's result is adapted into the *same* envelope shape an agent report uses (`quality.as_envelope`), so a failing lint run and a failing review reach the next agent through one door and one repair loop: the sensor's *type* changes without the steering loop changing shape. The counterpart honesty is on the same page — its shipped quality blocks are placeholder `echo`s that exit 0, announced loudly, because *"a wrong-but-plausible command that silently passes is worse than one that says so out loud."*

> **Adjacent but distinct:** [[pattern-edit-guardrails]] is a *preventive* control — it blocks a destructive or out-of-scope action rather than detecting a defect after the fact. It belongs to the harness's safety envelope (permissions/hooks) more than to either guide or sensor; include it when reasoning about the full control set. **One caveat the frame needs:** [[sssf]] shows the guardrail can also be built as a *sensor with an actuator* — it lets the write happen, then diffs the repo around the call and reverts what the agent was not permitted to touch, on the reasoning that a tool allowlist can never be a boundary while `bash` can run `git checkout`. Preventive and detective versions of the same control are not interchangeable, and which one you can build depends on whether the harness offers a hook at all (pi does not).

### The steering loop (refinement over time) — what the wiki already has

The loop that improves the controls when a failure recurs — the answer to *"refine this over time"*:

- [[pattern-knowledge-compounding]] — harvest → externalize → re-inject, applied so the *next* agent doesn't repeat the lesson ([[ce-compound]], [[gstack-learn]], [[ce-compound-refresh]]).
- [[warren]] / `.mulch` — the same loop baked into the *runtime substrate*, so compounding happens without a process-layer skill asking.
- [[artifact-solution-doc]] — the machine-consumable form learnings accrete into.
- Promoting a proven control into a permanent, auto-triggering skill ([[sp-writing-skills]], [[gstack-skillify]]) — the steering loop's strongest move: the harness *gains a capability*, not just a note.

This is why a lifecycle can be a **loop** rather than a line — see [[stage-learn]], plausibly the first genuinely new SDLC stage of the agent era.

## Keep quality left

Fowler's **"keep quality left"** restates, for agents, the classic shift-left: push checks as early as possible, because a defect is cheapest where it is introduced. In the wiki this is [[pattern-shift-left]], with [[pattern-test-driven-development]] as its earliest gate and [[pattern-plan-verification-loop]] as a *pre-code* sensor on the plan. Under autonomy the argument only sharpens: a stray agent edit caught by a pre-commit hook never reaches review.

## Regulation dimensions (what is being governed)

Fowler taxonomizes control systems by *what* they regulate — a lens the wiki lacks and could adopt:

- **Maintainability harness** — code quality; the most developed. Wiki: [[pattern-deep-modules]], [[addy-code-simplification]] / [[ce-simplify-code]], the code-review cluster.
- **Architecture fitness harness** — fitness functions checking architectural characteristics. Wiki: [[pattern-contract-first]], [[bmad-architecture]], [[ce-architecture-strategist]], and the constitutional gate of [[speckit-analyze]] as a proto-fitness-function.
- **Behaviour harness** — functional correctness; least mature (specs + AI-generated coverage + manual testing). Wiki: [[stage-validate]], [[pattern-test-driven-development]], the browser-QA sensors ([[gstack-qa]], [[ce-dogfood]]).

## A gap this frame exposes: harnessability

Two Fowler concepts have **no home in the wiki yet** and are worth flagging:

- **Harnessability** — how amenable a codebase *is* to harness controls, given its structure.
- **Ambient affordances** — "structural properties of the environment itself that make it legible, navigable, and tractable to agents."

These sit *upstream* of every guide and sensor: a legible codebase needs fewer of both. The nearest existing pages are [[pattern-deep-modules]] and [[mp-domain-modeling]] (a legible domain/ubiquitous language), but neither captures "shape the environment so the agent needs less harness." A candidate future `pattern-ambient-affordances` (or a note on [[pattern-deep-modules]]) would close it.

**Partly closed (2026-08-07) by [[topic-agent-readiness]].** The agent-readiness rubrics — Factory's repo-scoped pillar/level report and VirtusLab's Visdom maturity matrix — are harnessability *operationalized*: they score the environment's amenability to control as 100+ binary signals or a 16-capability × 5-level grid. Read the two topics as a pair — this page is the controls you build, that one is the substrate those controls require ("a guide states the convention, a sensor catches the violation, readiness is whether a sensor is even possible here"). A `pattern-ambient-affordances` page is still unminted; the rubrics supply the evidence it would be built from.

## How the pieces map

| Fowler term | This wiki |
|---|---|
| Harness (whole control system) | harness-node primitives **+** the `pattern`/`artifact` layers on top — *not* the `harness` node alone |
| Builder harness | the [[claude-code]]-style harness primitives (system prompt, retrieval, sub-agents) |
| User harness | the guides + sensors a team applies ([[pattern-context-engineering]], the review patterns, …) |
| Guide (feedforward) | [[pattern-project-constitution]], [[pattern-context-engineering]], [[artifact-standards]], [[artifact-adr]], [[pattern-source-grounding]] |
| Sensor (feedback) | [[pattern-plan-verification-loop]], [[pattern-adversarial-review]], [[pattern-evidence-before-claims]] |
| Computational control | linters/tests/types — [[gstack-health]], [[addy-ci-cd]], [[pattern-test-driven-development]]; [[sssf]]'s `kind="code"` phases are the rule stated as a budget line |
| Inferential control | LLM-as-judge — [[pattern-adversarial-review]], [[pattern-cross-model-review]] |
| Steering loop | [[pattern-knowledge-compounding]], [[warren]]; an ADW script in [[sssf]] is a steering loop written as plain Python |
| Keep quality left | [[pattern-shift-left]] |
| Harnessability / ambient affordances | *(gap)* — nearest: [[pattern-deep-modules]] |

## How they adapt as models improve

The frame also settles the *"fewer conventions now needed"* debate by splitting the guide layer:

- **Derivable guides shrink.** Style, idiom, "write tests," framework best-practice — the model's priors increasingly cover these, so spelling them out becomes dead weight that dilutes attention. Delete them; lean on priors + a computational sensor to catch the rare miss.
- **Non-derivable guides persist and accumulate.** "We use X not the obvious Y because Z," domain language, past-incident lessons — never inferable from training data. This is the irreducible kernel the steering loop banks.
- **The centre of gravity moves from guide to sensor.** A stronger model responds better to a crisp sensor on its *output* than to a long guide on its *input*: *verify, don't instruct.*
- **Guardrails don't shrink with model IQ.** [[pattern-edit-guardrails]] exists for blast-radius under autonomy, not to patch ignorance — run more parallel agents and you need *more* of it.

Net: the authored guide layer thins toward the project-specific kernel; sensors and the steering loop grow in relative weight.

## See Also
- [[beads-rules]] — the only capability in the wiki that maintains the guide layer **mechanically**: it scans `.claude/rules/` for contradictions by Jaccard similarity and merges near-duplicates into composites. Everything else here either writes guides ([[agent-os-discover-standards]], [[beads-setup]]) or asks an LLM to curate them ([[ce-compound-refresh]]). Rule-set decay is the failure this topic describes, and a similarity threshold is a surprisingly direct answer to it.
- [The store layer](../store/index.md) — where durable project state lives once you stop hand-maintaining instruction files; [[beads-remember]] is that argument in one command.
- [[agent-os]] — the framework whose signature *is* the guide layer (layered standards + product docs + specs).
- [[pattern-project-constitution]] ↔ [[pattern-knowledge-compounding]] — the prescribed and emergent poles of the guide/steering axis.
- [[pattern-context-engineering]] — the delivery mechanism for guides.
- Martin Fowler, *Harness Engineering* — the source frame ([capture](https://github.com/pmackay/sdlc-wiki/blob/main/raw/reference/2026-08-05-fowler-harness-engineering.md)).
