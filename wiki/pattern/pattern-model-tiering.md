---
type: pattern
sources: "Builder.io — BuilderIO/skills (2026); pstack v0.15.2 — Lauren Tan (2026); GSD docs (2026); Factory.ai — Droid docs (2026); Warp — Warp Factories docs (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md", "../../raw/runtime/2026-10-24-warp-factories.md"]
updated: 2026-10-24
---

# Pattern: Model tiering (expensive model for judgment, cheap models for bounded work)

Assign models to roles by **what each role's decisions are worth**. The most capable and most expensive model decomposes the work, resolves conflicts, chooses the path, and does the final review. Cheaper and faster models do the bounded, token-heavy work: repository scans, docs extraction, log reduction, test runs, browser passes, and mechanical edits. The expensive model **re-verifies** whatever it relies on from them.

[[builder-efficient-frontier]] puts it in one line: *"Use the expensive frontier model where its marginal judgment matters. Push repeatable, bounded, or token-heavy work to cheaper/faster subagents."* [[builder-efficient-fable]] gives the same split for Claude Fable specifically and puts the payoff at *"up to 3-5x more cost-efficient and 2-4x faster"* when the work parallelizes. It labels that figure a workload-dependent estimate.

**What keeps it from being plain delegation** is that the trust boundary follows the price boundary. Cheap-model output is *"leads, not facts"*. *"Before using a high-impact finding, opening a PR, or telling the user the work is done,"* the expensive model reopens the cited files and checks the line refs. Without that step, tiering just moves the errors down to the cheaper model. The pattern depends on [[pattern-fresh-context-subagents]] (self-contained handoff packets, since the cheap agent *"has no useful chat context"*) and on [[pattern-evidence-before-claims]] (the re-verification step).

**How it differs from [[pattern-cross-model-review]].** Cross-model review uses model *diversity* to find errors: different vendors look at the same artifact. Model tiering uses model *price* to allocate work: different tiers do different jobs. A framework can do both. [[pstack]] does, with a per-role model map and a cross-vendor review panel.

## Applied by (backlinks)

builder-skills:

- [[builder-efficient-fable]] names Fable as orchestrator, architect, synthesizer, and final judge, with cheaper subagents for research, coding, testing, and log reduction.
- [[builder-efficient-frontier]] generalizes this to any high-cost frontier model, with the guardrails *do not delegate the immediate blocker* and *do not let two agents edit the same files*.

pstack:

- [[pstack-setup-pstack]] maps each role (architect, reviewer, worker, …) to a model and records the map in an always-applied rule. This is tiering done once as configuration rather than decided per task.

GSD:

- [[gsd-planner]] runs on an **Opus-tier** model, while execution goes to other agents. This is the earliest example in the wiki, implicit in which model each sub-agent runs on.

## Enabled by (infrastructure)

- [[warp-factories]] (platform) — tiering by **role and by router**. Each factory agent has its own model or harness, chosen by *"what each agent has to do well"* (orchestration and long conversations for the foreman, research for triage, coding strength for implement). Factory-owned **model routers** go one level finer: a `complexity` router maps easy, medium, and hard tasks to concrete models, and a `prompt` router picks a model from an ordered list of task descriptions (*"Routine documentation changes"* → a small model; *"Complex implementation or debugging"* → a large one). **Benchmarks** price the trade on the team's own tasks before a change is adopted. The re-verification step this pattern requires is left to the agents' prompts.

## Provided by (harness)

- [[factory-droid]] has multi-model routing as a harness primitive. It **routes subagent work to a model tier by task complexity**, swaps models mid-session, and offers a free open-weight tier (Droid Core) plus BYOK. The harness does the tiering itself, so a framework does not have to build it out of subagent definitions.

## See Also
- [[pattern-cross-model-review]] — the neighbour, which uses diversity for error-finding rather than price for allocation.
- [[pattern-fresh-context-subagents]] — the handoff discipline tiering depends on.
- [[pattern-context-engineering]] — keeping the expensive model's context for decisions, not raw material.
- [[builder-stay-within-limits]] — the budget-window guard that pairs with it in [[builder-skills]].
