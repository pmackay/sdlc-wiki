# Source capture — ChaoYue, "Awesome Loop Engineering"

- URL: https://github.com/ChaoYue0307/awesome-loop-engineering (site: https://chaoyue0307.github.io/awesome-loop-engineering/)
- Captured: 2026-09-01
- Type: external reference (not a framework ingest) — grounding source for `wiki/topic/topic-software-factory.md`
- Scope of capture: the project's own conceptual artifacts (working definition, mental model, Loop Contract, design checklist, maturity model, and the full TAXONOMY.md verbatim). The 989-resource link atlas, pattern library bodies, and runtime starters are *not* mirrored — they are curation, not vocabulary. Quotes are verbatim where marked.

## Working definition (verbatim)

> **Loop Engineering** is the AI and coding-agent practice of designing recurring systems that discover work, delegate it to agents, verify results, persist state, decide next actions, and run again on a cadence, event, or until a verifiable goal is reached.

## Mental model — where it sits relative to prompt/context/harness engineering (verbatim)

> Prompt engineering asks: **what should I say to the model?**
>
> Context engineering asks: **what state and knowledge should the model see?**
>
> Harness engineering asks: **what tools, permissions, tests, sandboxes, and feedback should surround the agent?**
>
> Loop engineering asks: **what recurring system should discover work, delegate to agents, verify results, persist state, decide next actions, and re-run when the human is no longer in the inner loop?**
>
> Prompt, context, and harness engineering make one agent run better. Loop Engineering makes agent work repeatable, observable, and governable over time.

The canonical loop shape (verbatim):

```text
Objective
  -> Trigger / cadence
  -> Discover / intake work
  -> Delegate to agents
  -> Act in an isolated workspace
  -> Verify with tests, evals, traces, or reviewers
       -> if failed: feed back the evidence and retry
       -> if passed: persist state and decide what happens next
  -> Repeat, report, open a PR, or escalate to a human
```

## The Loop Contract

> A **Loop Contract** is a reviewable operating specification for one recurring agent job. It is not a legal agreement, a long prompt, or a particular runtime. It records the decisions a person normally supplies during a one-off session - what work is authorized, what the agent may touch, what evidence counts, what survives, and when control returns to a human - so those decisions remain stable across runs.

> The contract becomes necessary when an agent runs from a schedule, event, queue, or goal instead of waiting for live supervision. Unanswered questions become hidden defaults: the agent may select the wrong work, widen its own scope, approve its own output, forget a previous failure, or retry without a stopping rule.

> Prompt, context, and harness choices improve one run. A pattern describes how a class of recurring work should operate. The contract fixes the exact policy for one implementation, and the runtime executes it.

The eleven contract parts (table verbatim, artifacts column condensed):

| Part | Decision the contract must make |
| --- | --- |
| Objective | Which measurable outcome is worth repeating toward? |
| Trigger | Which event, schedule, or goal authorizes a run? |
| Discover / Intake | Which items qualify, and how are duplicates or stale work rejected? |
| Workspace | What may the agent read or change, and where is execution isolated? |
| Context | Which instructions and current evidence must be loaded fresh? |
| Delegation | Who explores, acts, and checks, and can the acting agent approve itself? |
| Verification | Which external evidence must pass before progress or completion is valid? |
| State | Which checkpoints and receipts survive, and when are they updated? |
| Budget | How much time, retry, token, cost, or concurrency may one run consume? |
| Escalation | Which conditions require a named human owner or review channel? |
| Exit | What proves success, and what stops the loop without success? |

Failure modes when parts are omitted (verbatim table):

| If the contract omits... | The recurring failure is predictable |
| --- | --- |
| Trigger and intake | The loop invents work, reprocesses the same item, or runs at the wrong time. |
| Workspace and permissions | A narrow repair expands into unrelated files, credentials, or production changes. |
| Independent verification | The acting model can declare its own output complete without external evidence. |
| Durable state and receipts | The next run repeats failed attempts and cannot explain what already happened. |
| Budget, escalation, and exit | The loop retries indefinitely, spends past its value, or stalls without an owner. |

## Loop design checklist (verbatim, questions column)

- Name one objective — does the loop optimize for a specific outcome instead of a vague goal such as "improve the repo"?
- Define the intake — where does work enter: PR comments, CI failures, issues, logs, eval failures, feedback, or schedule?
- Isolate execution — does the agent act in a worktree, sandbox, branch, container, or read-only mode?
- Write the feedback signal first — do tests, typechecks, lint, evals, policy checks, or trace graders exist before retries begin?
- Persist state outside the model — does progress survive in files, issue comments, checkpoints, traces, or a database?
- Separate maker and checker — does something other than the acting agent decide whether the work is done?
- Put a budget on autonomy — are runtime, turns, retries, token spend, and concurrent workers capped?
- Design escalation — is it clear when the loop should open a PR, file an issue, ask a human, or stop?
- Keep receipts — are commands, evidence, changed files, and stop reasons recorded?

## Loop Maturity Model (levels 0–6)

> The Loop Maturity Model is a capability ladder for **one recurring agent workflow**. It helps you choose the smallest operating model that can perform a job reliably. The level describes how the workflow is triggered, remembered, verified, divided, and supervised; it does not score model intelligence, team sophistication, or product quality.

Usage rules (verbatim, condensed): "Start with the job, not the target level." · "Treat levels as cumulative capabilities." · "Move up only for a recurring failure or operating need." · "Earn autonomy in order. Persist state before increasing unattended runtime, establish external verification before adding more agents, and add production controls before actions can affect users or infrastructure."

| Level | Operating model |
| --- | --- |
| 0 · Manual prompting | A person holds the state, supplies each next instruction, and judges the result. |
| 1 · Scripted retry | A bounded wrapper reruns one agent and feeds back an external failure. |
| 2 · Scheduled loop | A schedule or event triggers fresh intake, one bounded run, and a report or artifact. |
| 3 · Stateful loop | Durable checkpoints and receipts record completed work, blockers, evidence, and the next action outside the model. |
| 4 · Self-verifying loop | Tests, evals, policy checks, traces, or an independent evaluator gate progress and exit. |
| 5 · Multi-agent loop | Specialists divide discovery, action, review, and judgment through explicit handoffs and shared state. |
| 6 · Production-supervised loop | Telemetry, least privilege, budgets, approvals, rollback, incident ownership, and human escalation govern every run. |

> Levels describe **capability, not ambition**. Many useful workflows should stop at Level 2 or 3. A dependable Level 3 loop with durable state is more valuable than a Level 5 design with vague goals, weak checks, or ceremonial agent roles.

## When work should loop at all (verbatim table)

| Use a loop when... | Prefer one supervised run when... |
| --- | --- |
| Work returns through a schedule, event, queue, or recurring condition. | The task is genuinely one-off. |
| An external check can prove progress or completion. | "Done" depends mainly on open-ended human judgment. |
| Saved evidence, checkpoints, or receipts improve the next run. | No useful state should survive the session. |
| Permissions, retries, time, and cost can be bounded in advance. | A safe permission or budget boundary cannot be stated. |
| A named human owns ambiguity, exceptions, and high-impact decisions. | Every meaningful step already needs live human direction. |

## TAXONOMY.md (verbatim, complete)

# Loop Engineering Taxonomy

Classify recurrence first by where it lives, then classify an operational AI-agent loop by its trigger, work intake, verification method, state model, agent topology, and operating domain.

## By Loop Layer

- **Model layer**: a learned layer, block, module, or latent-state update repeats within one inference. This is an adjacent foundation for Loop Engineering, not a complete operational loop.
- **Agent layer**: a model alternates reasoning, tool calls, observations, and updates while solving one task.
- **Harness layer**: tools, context, permissions, sandboxes, evaluators, and checkpoints control one or more agent runs.
- **Workflow layer**: triggers, intake, delegation, verification, durable state, budgets, and next-action policy govern repeated work.
- **Operations layer**: telemetry, approvals, incident response, cost controls, rollback, and human ownership govern deployed loops.
- **Evaluation layer**: benchmarks, graders, trace analysis, and challenge sets measure behavior across the other layers.

Dataset rows pair this facet with `scope_fit`: `direct` for operational loop resources, `enabling` for components and evidence, and `adjacent` for model architectures or neighboring ecosystem maps.

## By Trigger

- **Scheduled loop**: runs on a cadence such as hourly, daily, weekly, or during a rollout window.
- **Event-triggered loop**: starts from a webhook, failed check, new comment, issue label, release event, or alert.
- **Goal-driven loop**: continues until a verifiable goal is met, such as passing tests or resolving all blocking comments.
- **Manual bootstrap loop**: starts from a human command, then follows a repeatable contract with state, verification, and exit rules.

## By Work Intake

- **Queue loop**: consumes work from issues, PRs, tickets, alerts, feedback streams, or triage inboxes.
- **Scan loop**: periodically searches a repository, dashboard, logs, docs, or benchmark output for new work.
- **Reactive loop**: responds to a specific failure signal such as CI, eval regression, deploy anomaly, or user report.

## By Verification

- **Deterministic loop**: uses tests, typechecks, lint, schemas, dashboards, or threshold checks as the main gate.
- **Evaluator loop**: uses a second model, rubric, reviewer, or judge agent to evaluate output.
- **Human-supervised loop**: requires human approval before sensitive actions or before completion is accepted.
- **Receipt-based loop**: records evidence such as commands, logs, trace IDs, screenshots, PR links, or issue comments.

## By State Model

- **Stateless retry loop**: feeds immediate failure evidence back into one session. Useful but fragile.
- **File-backed loop**: stores progress in `PROGRESS.md`, task files, runbooks, or generated reports.
- **Issue-backed loop**: stores progress in GitHub, Linear, Jira, Slack, or another system of record.
- **Checkpointed loop**: persists structured state in a database, workflow engine, trace store, or event log.

## By Agent Topology

- **Single-agent loop**: one agent acts, with deterministic checks or human review.
- **Maker-checker loop**: one agent changes the artifact and another verifies it.
- **Manager-worker loop**: an orchestrator decomposes work and assigns specialized agents.
- **Adversarial loop**: reviewer, critic, or security agents try to falsify the maker's output.

## By Operating Domain

- **Repository loop**: PR babysitting, CI repair, bug hunting, docs drift, dependency triage.
- **Release loop**: deploy verification, canary monitoring, rollback recommendation, incident handoff.
- **Feedback loop**: user feedback clustering, issue deduplication, community triage, roadmap signal collection.
- **Evaluation loop**: recurring benchmark runs, trace review, regression detection, prompt or harness hill-climbing.

## Maturity Path

Most teams should move in this order:

1. Manual bootstrap loop with explicit state.
1. Scheduled or event-triggered loop with deterministic gates.
1. Maker-checker loop with durable receipts.
1. Multi-agent or workflow-backed loop.
1. Production-supervised loop with observability, approvals, budgets, and rollback rules.

Higher maturity is not automatically better. The right loop is the simplest loop that can safely discover work, delegate, verify, persist state, decide the next action, and stop.
