---
type: capability
subtype: skill
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[mp-triage]]"]
sources: "Jaymin West — jayminwest/seeds .factory/skills/seeds-issue-workflow/SKILL.md + AGENTS.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# seeds-issue-workflow

`seeds-issue-workflow` (`.factory/skills/seeds-issue-workflow/SKILL.md`) — the framework's one capability that is a **skill** rather than a program: a repo-local agent skill that turns a vague ask into a tracked, ready unit of work. Its frontmatter declares `tools: [sd, git]`, its input is *"a description of the work (a sentence or a multi-step feature)"*, and its output is *"one or more seeds in `.seeds/issues.jsonl`, ready (unblocked) or correctly blocked."*

It encodes two procedures and the rule for choosing between them — the framework's [[pattern-scale-adaptive-planning]] dial made explicit:

- **Pre-flight** — `sd prime`, then `sd ready` to see what is already unblocked, then `sd search "<keywords>"` to avoid a duplicate. If a seed already covers the work, claim it instead of filing another.
- **Procedure A — create-then-ready**, for work that fits in one focused commit: [[seeds-create]], then [[seeds-label]] and [[seeds-dep]], then verify with `sd ready | grep <id>`. The skill's sharpest line is the warning against over-wiring: *"Add dependencies for real ordering only — every unnecessary `sd dep add` hides the work from `sd ready`."*
- **Procedure B — plan-decomposition**, for multi-step or ambiguous work: [[seeds-plan-prompt]] → fill → [[seeds-plan-submit]] → [[seeds-plan-show]].
- **Finish** — [[seeds-close]] with a `--reason`, then [[seeds-sync]]; do not push unless asked; never hand-edit the JSONL, so locks and atomic writes are honored.

It is worth its own page for what it reveals about the classification: seeds is a program, but a program still needs a prompt to teach an agent *when* to reach for which part of it. The skill is thin — a decision rule plus command sequences — because everything a prompt would otherwise have to enforce is already enforced by the commands.

Implements [[stage-plan]]. Its closest cross-framework counterpart is [[mp-triage]], which likewise converts an unshaped request into an agent-ready tracked item.

## See Also
- [[seeds-create]] · [[seeds-plan-submit]] — the two branches it routes between.
- [[seeds-onboard]] — the lighter, always-loaded version of the same guidance.
- [[mp-triage]] · [[mp-to-tickets]] — skill-shaped counterparts elsewhere.
- [[stage-plan]] — the canonical stage this implements.
