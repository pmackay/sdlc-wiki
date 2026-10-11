---
type: capability
subtype: command
belongs_to: "[[pstack]]"
implements: []
delegates_to: ["[[pstack-poteto-agent]]", "[[pstack-how]]", "[[pstack-why]]", "[[pstack-architect]]", "[[pstack-arena]]", "[[pstack-swarm]]", "[[pstack-interrogate]]", "[[pstack-unslop]]", "[[pstack-no-comments]]", "[[pstack-technical-writing]]", "[[pstack-tdd]]", "[[pstack-figure-it-out]]", "[[pstack-show-me-your-work]]"]
produces: []
applies: ["[[pattern-scale-adaptive-planning]]", "[[pattern-context-engineering]]", "[[pattern-autonomous-loop]]", "[[pattern-project-constitution]]"]
equivalent_to: ["[[gstack-router]]", "[[addy-using-agent-skills]]", "[[sp-using-superpowers]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /poteto-mode

The framework's single entry point and its router. `/poteto-mode` reads the request, matches it to one of **twenty-three playbooks**, opens a todo list whose first items are that playbook's steps **copied in verbatim**, and then routes to the other skills as the steps fire. Everything else in pstack is situational; the README's whole getting-started instruction is run [[pstack-setup-pstack]] once, then use this.

It is a **sticky mode** (`mode: true` in its frontmatter, with a `reminder` field the harness re-injects each turn). Once entered it stays on across turns, applying itself when a playbook matches or the task needs rigor and staying out of the way otherwise. The user opts out by saying so. This is a materially different router design from the wiki's other dispatchers: [[gstack-router]] and [[addy-using-agent-skills]] dispatch per invocation, and [[sp-using-superpowers]] achieves persistence by making every leaf skill auto-trigger. pstack instead makes the *router* persistent and leaves every leaf skill explicitly non-auto-invocable (`disable-model-invocation: true` on all of them).

## The three parts of the skill

**Triggers.** A list of standing if-then rules mapping a situation to a skill: nontrivial change or an "are we sure?" question goes to [[pstack-how]]; code crossing a function boundary goes to [[pstack-architect]]; parallel fan-out splits between [[pstack-swarm]] (coverage, races, gauntlets) and [[pstack-arena]] (design and code bakeoffs); a contested design goes to [[pstack-interrogate]]; any prose surface goes to [[pstack-unslop]]; anything the user steps away from goes to [[pstack-show-me-your-work]]. Two triggers exist purely to beat a *name collision* with a Cursor built-in — any PR-status request must route to pstack's Babysit playbook rather than Cursor's own `babysit` skill, whose description matches the same words.

**The inline principles index.** All twenty-three `principle-*` skills, grouped Core / Architecture / Verification / Delegation / Meta, each with its trigger condition in one line. The index is read at task start; the leaf SKILL.md is read in full only for a principle actually being applied. The non-negotiable at the top of the file closes the loop: *name each principle that shaped a decision and the specific choice it changed, and cite only principles whose leaf you read this session.* That citation requirement is what makes the principle set auditable rather than decorative — pstack's analogue of a [[pattern-project-constitution]], carried as skills rather than as a constitution file.

**Autonomy, subagents, and reply style.** Reversible work and external actions proceed without asking; irreversible writes always pause. Every `Task` call defaults to `run_in_background: true`, file pointers rather than inlined context, and an **explicit model per role**. The reply rules are unusually specific, banning the em dash outright and barring a colon as a mid-sentence connector, and they require every claim to carry its evidence or its label — measured, inferred, or guess — in the same sentence.

## The twenty-three playbooks

Stored as separate files under `playbooks/` and copied into the todo list verbatim rather than summarized, which keeps the step text out of the router's own context until it is needed.

- **Understand.** Investigation (a read-only question with a cited answer as the deliverable).
- **Diagnose.** Bug fix, Perf issue, Hillclimb (sustained metric improvement with one commit per accepted win), Runtime forensics (a live symptom), Trace forensics (a captured profiling artifact). The two forensics playbooks deliver a *diagnosis, not a fix*.
- **Build.** Feature, Refactoring, Prototype, Visual parity.
- **Meta.** Authoring a skill, Eval (blinded testing of how a skill or prompt change moves agent behavior).
- **Deliver.** Babysit (drive a PR to merge-ready), Shipping (independently verify a green stack, then land only the contiguous verified run bottom-up), Opening a PR (invoked at the end of every other playbook).
- **Run long.** Autonomous run, Orchestrate (a standing multi-day program under one coordinator), Autopilot-full (independent PRs to merged, one owner each), Autopilot-stack (one linear stack for the operator to land), Multi-phase plan.
- **Suspend and resume.** Session pickup, Pause safely — an explicitly paired complement, and the wiki's first framework to page *suspension* as its own procedure rather than only resumption.
- **Housekeeping.** Worktree cleanup.

The router scales ceremony to the work ([[pattern-scale-adaptive-planning]]): a large or cross-cutting effort routes to [[pstack-figure-it-out]] even when a narrower playbook fits, and a standing program routes to Orchestrate instead. *figure-it-out designs one bespoke run; orchestrate runs the program.*

## See Also
- [[pstack-poteto-agent]] — the subagent that routes through the same wrapper; spawned for any delegate inside a playbook step.
- [[pstack-figure-it-out]] — the escape hatch when no bundled playbook fits.
- [[gstack-router]] · [[addy-using-agent-skills]] · [[sp-using-superpowers]] — the other framework routers.
- [[pstack]] — the framework this fronts.
