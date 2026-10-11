---
type: sdlc-stage
aka: { matt-pocock-skills: "code-review + architecture audit", addy-agent-skills: "Review (/review, /code-simplify, /webperf, /ship personas)", bmad: "code-review (adversarial) + TEA", compound-engineering: "Simplify (step 4) + Review (step 5) + optimize", gstack: "Review (code/design/DX/security)", superpowers: "requesting-code-review + receiving-code-review", pstack: "interrogate / blast-radius / no-comments" , tessl: "code review / change risk / change verify (registry)", builder-skills: "factory-review-prs / agent-watchdog / visual-recap" }
sources: "Synthesized from Matt Pocock + Addy Osmani + BMAD + Compound Engineering + gstack + Superpowers + pstack + Tessl + Builder Skills (2026)"
updated: 2026-09-26
---

# Stage: Review

Canonical lifecycle stage: **judge that the built software is *good* before it ships** — a quality gate over the code and its design, distinct from confirming it *works* ([[stage-validate]]). Review asks *is it good?* — is it correct under scrutiny, secure, performant, simple, well-architected, on-brand — and produces **assessments and fixes** (review reports, security/perf audits, simplifications), not a pass/fail on runtime behaviour. It runs after the build and typically gates entry to [[stage-release]].

**Derived projection** — evidence is the capabilities that `implements: [[stage-review]]`.

> **New stage (split out of [[stage-validate]] on 2026-07-05).** Long the strongest parked split candidate on [[stage-validate]]: *validate* = confirm the software **works** (functional: UAT, runtime/browser tests, spec-conformance); *review* = confirm it is **good** (quality gate). Addy Osmani was the first framework to treat these as **two distinct phases** (a *Verify* phase ∥ a *Review* phase). **gstack cleared the ≥2-framework bar**: its sprint runs a distinct **Review** phase (code [[gstack-review]] + cross-model [[gstack-codex]] + design/DX/security) held separate from a distinct **Test** phase (functional QA [[gstack-qa]]). Two frameworks with the clean Verify∥Review partition → promoted, exactly as [[stage-specify]] was split from [[stage-plan]] and [[stage-learn]] from [[stage-release]]. See [Why a distinct stage](#why-a-distinct-stage-not-a-flavor-of-validate). **Superpowers (2026-07-17) is now a third framework with the partition** — functional [[sp-verification-before-completion]] ∥ quality [[sp-requesting-code-review]] — further confirming the split.

## Why a distinct stage, not a flavor of validate

[[stage-validate]] executes the software and observes: does the feature work, do the tests pass, does the build match the spec? Review never runs the feature to check behaviour — it **reads the artifact and judges its quality**: a reviewer finding a race condition that passes CI, a security auditor modelling an exploit, a performance engineer flagging a regression, a simplifier removing complexity, an architect checking module boundaries. The two are adjacent (both gate release) but categorically different: validate is *empirical* (run it, observe), review is *evaluative* (read it, judge). Three frameworks (GSD, OpenSpec, Spec Kit) ship a functional validator but **no** quality-review capability at all — the cleanest evidence that the two activities are separable.

## Implemented by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-code-review]] — two-axis diff review, Standards (+ Fowler smell baseline) ∥ Spec, parallel sub-agents → [[artifact-review-report]] (v1.1; graduated from in-progress) ([[pattern-parallel-persona-review]], [[pattern-adversarial-review]]).
- [[mp-improve-codebase-architecture]] — architectural audit with HTML reports ([[pattern-deep-modules]]).

Addy Osmani — Agent Skills (its **Review** phase — skills + the `/ship` persona fan-out):

- [[addy-code-review]] — five-axis review with severity labels → [[artifact-review-report]] ([[pattern-anti-rationalization]]).
- [[addy-code-simplification]] — reduce complexity while preserving behavior ([[pattern-deep-modules]]).
- [[addy-security]] — OWASP hardening → [[artifact-security-audit]].
- [[addy-performance]] — measure-first optimization → [[artifact-perf-audit]] ([[pattern-measure-first]]).
- [[addy-code-reviewer]] — Staff-Engineer five-axis review persona → [[artifact-review-report]] ([[pattern-parallel-persona-review]]).
- [[addy-test-engineer]] — QA persona: coverage analysis + Prove-It (in the `/ship` fan-out).
- [[addy-security-auditor]] — security-engineer persona: threat model + OWASP → [[artifact-security-audit]].
- [[addy-web-performance-auditor]] — Core Web Vitals audit persona → [[artifact-perf-audit]].

BMAD:

- [[bmad-code-review]] — adversarial parallel review layers (Blind Hunter / Edge Case Hunter / Acceptance Auditor) in fresh context → [[artifact-review-report]] ([[pattern-adversarial-review]], [[pattern-parallel-persona-review]]). (Optional **TEA** module adds enterprise quality gates.)

Compound Engineering (loop steps 4–5, plus review sub-agents):

- [[ce-simplify-code]] — reduce complexity in fresh code, behavior-preserving ([[pattern-deep-modules]]); counterpart to [[addy-code-simplification]].
- [[ce-code-review]] — ~16-persona confidence-gated review, adversarial + cross-model → [[artifact-review-report]] ([[pattern-parallel-persona-review]], [[pattern-adversarial-review]], [[pattern-cross-model-review]]).
- [[ce-optimize]] — metric-driven, parallel-experiment optimization ([[pattern-measure-first]]); counterpart to [[addy-performance]].
- [[ce-security-sentinel]] — attacker-minded security audit → [[artifact-security-audit]]; counterpart to [[addy-security-auditor]].
- [[ce-performance-oracle]] — bottleneck analysis → [[artifact-perf-audit]]; counterpart to [[addy-web-performance-auditor]].
- [[ce-pattern-recognition-specialist]] — design / anti-pattern + recurring-problem analysis.
- [[ce-data-integrity-guardian]] — data-safety / migration-integrity / privacy review.
- [[ce-repo-research-analyst]] — repo research converted to optimization inputs for [[ce-optimize]].

gstack (its **Review** sprint phase — distinct from its **Test** phase):

- [[gstack-review]] — Staff-Engineer pre-landing PR review; auto-fixes the obvious → [[artifact-review-report]] ([[pattern-adversarial-review]]).
- [[gstack-codex]] — cross-model OpenAI Codex second opinion; overlap/unique analysis → [[artifact-review-report]] ([[pattern-cross-model-review]]).
- [[gstack-cso]] — OWASP Top 10 + STRIDE audit with exploit scenarios → [[artifact-security-audit]].
- [[gstack-design-review]] — live visual audit + fix loop → [[artifact-review-report]], [[artifact-atomic-commit]].
- [[gstack-devex-review]] — live developer-experience audit (measured TTHW) → [[artifact-review-report]].
- [[gstack-ios-design-review]] — designer's-eye iOS audit on real hardware; 10-dim Apple HIG rubric → [[artifact-review-report]].
- [[gstack-health]] — standing code-quality dashboard (type/lint/tests/dead-code).

Superpowers (review as a dispatched fresh-context gate + the reception discipline):

- [[sp-requesting-code-review]] — dispatch a fresh-context code-reviewer subagent (never the controller's history); act on findings by severity → [[artifact-review-report]] ([[pattern-adversarial-review]], [[pattern-fresh-context-subagents]]). Wired into the execution loop (a review between every task).
- [[sp-receiving-code-review]] — how to *respond* to review: technical evaluation over performative agreement ("You're absolutely right!" is forbidden), verify before implementing, push back with reasoning ([[pattern-anti-rationalization]]). **Novel — the review-reception side no other framework here pages.**

pstack (the densest review roster relative to framework size, and the one that rejects the persona mechanism):

- [[pstack-interrogate]] — one reviewer per configured model, identical prompt and rubric; *"the adversarial signal comes from model diversity, not assigned personas"* → [[artifact-review-report]] ([[pattern-cross-model-review]], [[pattern-adversarial-review]]).
- [[pstack-blast-radius]] — what a small-looking change breaks elsewhere; find the one fact it is safe because of and prove it by running code, grading every claim on a five-rung evidence ladder ([[pattern-evidence-before-claims]], [[pattern-tooling-leverage]]).
- [[pstack-no-comments]] — acts on Comment Sicko's findings: smallest root-cause fix in scope, and an encoding offer (type, runtime, test, or CI lint) for any claimed constraint before the comment is deleted.
- [[pstack-comment-sicko]] — the read-only comment reviewer (sub-agent); flags a comment on our own code as `MUST KILL` on the guilty *symbol*, converting prose into a reshape task ([[pattern-persona-agents]]).

Tessl — a [registry](../registry/index.md), not a framework, and the only non-process layer with a real presence in this stage (see [how to weight it](#a-note-on-the-registry-entries) below):

- [[tessl-code-review]] — agentic PR review with versioned, pinnable **lenses** → [[artifact-review-report]] ([[pattern-parallel-persona-review]] rebuilt as installable units).
- [[tessl-change-risk]] — assess a diff and exit non-zero only when human review is required; reviewer attention allocated by measured blast radius ([[pattern-scale-adaptive-planning]]).
- [[tessl-change-verify]] — LLM-judge verifiers over changed files, cached, sampled, and capped by a call ceiling that refuses broad runs ([[pattern-deterministic-gates]]).

builder-skills:

- [[builder-factory-review-prs]] — a scheduled sweep of a filtered queue of **other people's** PRs, with findings kept apart from reply, approval, and merge gates → [[artifact-review-report]]. It joins the code-review cluster.
- [[builder-agent-watchdog]] — reviews another *agent's* whole run by investigating the same problem independently and diffing the two → [[artifact-review-report]] ([[pattern-cross-model-review]], [[pattern-adversarial-review]]).
- [[builder-visual-recap]] — a reviewer's aid rather than a reviewer: the diff as an interactive recap at a higher altitude than line-by-line → [[artifact-explainer]].

## Cross-framework equivalents

The quality-review clusters span the six frameworks that ship a review capability:

- **Code review:** [[addy-code-review]] ↔ [[bmad-code-review]] ↔ [[ce-code-review]] ↔ [[gstack-review]] ↔ [[mp-code-review]] ↔ [[sp-requesting-code-review]] (+ the [[addy-code-reviewer]] persona) — a six-framework cluster, all producing [[artifact-review-report]]. MP's is distinctive in its explicit **Standards ∥ Spec** two-axis split; Superpowers' in treating review as a **dispatched fresh-context subagent gate between every task** rather than a standalone command.
- **Receiving review:** [[sp-receiving-code-review]] stands alone — every other framework models *producing* review; Superpowers is the only one to codify how the author should *receive* it (no performative agreement, verify-then-implement, reasoned pushback). No counterpart (not `equivalent_to`).
- **Cross-model review:** [[gstack-codex]] ↔ [[ce-code-review]]'s cross-model pass — an independent second opinion from a different vendor ([[pattern-cross-model-review]]).
- **Simplification:** [[addy-code-simplification]] ↔ [[ce-simplify-code]] ([[pattern-deep-modules]]).
- **Security audit:** [[addy-security]] ↔ [[addy-security-auditor]] ↔ [[ce-security-sentinel]] ↔ [[gstack-cso]] → [[artifact-security-audit]].
- **Performance audit:** [[addy-performance]] ↔ [[addy-web-performance-auditor]] ↔ [[ce-optimize]] ↔ [[ce-performance-oracle]] ↔ [[gstack-benchmark]] → [[artifact-perf-audit]] ([[pattern-measure-first]]).
- **Design / DX review** is a gstack specialty ([[gstack-design-review]], [[gstack-devex-review]], [[gstack-ios-design-review]]) with no cross-framework counterpart — a lens the other frameworks leave to general code review.

Note **GSD, OpenSpec, and Spec Kit ship no review capability** — they validate functionally ([[gsd-verify-work]], [[openspec-verify]], [[speckit-converge]]) but do not treat quality review as a step. Their absence here is what makes review and [[stage-validate]] cleanly separable.

## A note on the registry entries

Three of the capabilities above belong to [[tessl]], which is a [registry](../registry/index.md) rather than a framework. They are listed because they genuinely perform this stage, but they should not be read as a framework's stage coverage: a registry's command surface is overwhelmingly off-stage by construction, and these are the product growing sideways into the lifecycle it was built to supply. The [conventions](../CONVENTIONS.md#the-supply-layer-registries) call this out as the expected shape for the layer.

What they *do* add is a distinct **posture**. The framework-side review capabilities optimize one engineer's rigor — [[pstack-blast-radius]] demands a safety fact be proven by running code, [[gstack-review]] reads like a staff engineer. The registry-side ones optimize an organization's throughput: a risk verdict as an exit code, a judge budget with a hard ceiling, a review roster you pin like a dependency. Same stage, different scaling problem, and the contrast is the reason to keep them on the page.

## See Also
- [[stage-validate]] — the sibling it was split from: validate confirms the software **works**, review confirms it is **good**. Both gate [[stage-release]].
- [[stage-implement]] — produces what is reviewed.
- [[stage-release]] — runs once review (and validate) pass.
- [[pattern-adversarial-review]] · [[pattern-parallel-persona-review]] · [[pattern-cross-model-review]] — the techniques review leans on.
