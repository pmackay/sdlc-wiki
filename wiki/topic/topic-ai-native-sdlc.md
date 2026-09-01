---
type: topic
sources: "Louis Claxton, Anthropic Applied AI — 'The AI-Native SDLC playbook' (2026-08-21); wiki synthesis"
raw: ["../../raw/reference/2026-08-21-ai-native-sdlc-playbook.md"]
updated: 2026-09-01
---

# Topic: The AI-native SDLC — the vendor's own playbook, read against the wiki

> **This page is a curated overlay, not an ontology node.** It gathers pages from across the wiki around one theme and links *out* to them; it stores no edges and changes no synthesis. See [CONVENTIONS §The topic layer](../CONVENTIONS.md#the-topic-layer-curated-overlays).

**The question this topic answers: what does the organization-level transformation look like — and how far does Anthropic's own enterprise playbook agree with what the wiki's twelve community frameworks independently converged on?** The playbook ([capture](../../raw/reference/2026-08-21-ai-native-sdlc-playbook.md)) is the first *vendor-authored, enterprise-governance* treatment of the lifecycle in the wiki's raw set. Every other source here is a community framework, a runtime, or an independent essay; this one is written by the harness vendor's Applied AI team for regulated organizations, and its unit of analysis is the *organization's process*, not one engineer's session. That makes it less a thirteenth framework than an independent check on the synthesis — and the degree of convergence is the finding.

## The thesis: the bottleneck moved, so the controls must too

The playbook's opening argument is the cleanest statement in the wiki's sources of *why* any of this tooling exists. When agents collapse the build phase from weeks to hours, three things follow: the bottleneck relocates to the human-speed stages either side of build (plan, review/test, deploy); line-by-line human review "can't keep up once agents write most of the diff"; and governance cost climbs because exceptions still route through weekly committees. The traditional SDLC's ceremony — PRDs, estimation rituals, staged sign-offs — existed to force alignment across what used to be months of implementation, and loses its rationale when implementation is no longer the expensive part.

The proposed replacement keeps the old *control objectives* and swaps the *enforcement*: a linear handoff chain becomes a loop, and every stage ends by committing an artifact the next stage begins by reading. This is [[pattern-shift-left]] applied to governance itself — policy read and applied while the spec is written rather than discovered in a review weeks later — and the loop's closure at maintenance is [[pattern-autonomous-loop]] operated at organizational scale.

## The artifact chain

The playbook's connective tissue is a chain of committed markdown artifacts: `intent.md` → `spec.md` → `plan.md` → the diff and its tests → the PR with review findings → the incident record, which becomes the next `intent.md`. Each acceptance triggers the next stage; the chain of commits doubles as the audit trail (who asked, what the agent produced, who approved). The wiki already pages most of these under other names:

- **`intent.md`** — a "proto-spec in the originator's own terms": problem, proposed outcome, affected users/systems, constraints, open questions. The closest paged artifacts are [[artifact-product-brief]] and [[artifact-prd]]; the distinctive move is that the *originator* authors it with an agent, cutting the product-team transcription handoff. Its committed acceptance is the trigger for the next stage.
- **`spec.md`** — requirements and design collapsed into one prompted session, constrained by org skills, with concerns flagged for policy owners. The wiki's [[artifact-spec-md]], and the play is [[pattern-spec-driven-development]] verbatim.
- **`plan.md`** — files that change, order of work, risks, and the tests that prove it; produced in plan mode, interrogated until implementable by a stranger, committed, and later *diffed against the merged result*. The wiki's [[artifact-plan-md]]; the interrogation step is [[pattern-plan-verification-loop]], and the rule that implementation departures update `plan.md` in the same commit is [[pattern-living-specification]].
- **The PR and its findings** — [[artifact-pull-request]] plus a `REVIEW.md` policy file defining severity tiers and nit caps, which is [[artifact-review-report]] territory and [[pattern-adversarial-review]] in mechanism.

The sidebar on legacy systems is worth reading for one decision rule: for every artifact, name **one** system as source of truth (repo-first, legacy-tool-first, or bidirectional linkage as the admitted-two-truths minimum) — the enterprise-integration question no community framework addresses because none of them has to coexist with a change board.

## Six stages against the wiki's eight

The playbook's six stages are coarser than the wiki's derived set, but map onto it without remainder — evidence that the canonical stages are carving at real joints:

| Playbook stage | Wiki stage(s) | The play, in wiki vocabulary |
|---|---|---|
| Plan | [[stage-align]] | intent captured once, in the originator's words, as a committed artifact |
| Design | [[stage-specify]] | requirements + design in one session, skills as policy constraints |
| Build | [[stage-plan]] + [[stage-implement]] | plan mode as mandatory entry; CLAUDE.md, skills, hooks, worktree parallelism |
| Test | [[stage-validate]] | self-verification loop + continuous evals of the agent's own configuration |
| Deploy | [[stage-review]] + [[stage-release]] | bidirectional AI review; hooks as human approval gates; agent stops at the production gate |
| Maintain | [[stage-learn]] (and back to [[stage-align]]) | monitoring, scans, and incidents written back as the next `intent.md` |

Two of the wiki's distinctions the playbook confirms by construction: it splits plan-mode planning from implementation *within* its Build stage (the wiki's [[stage-plan]]/[[stage-implement]] seam), and it splits self-verification (Test) from PR review (Deploy) — the [[stage-validate]]/[[stage-review]] distinction most homegrown setups miss.

## The convergence — patterns the playbook independently confirms

Read as evidence-in-prose (a topic link is never graph evidence), the playbook lands on a striking share of the wiki's pattern layer:

- **[[pattern-deterministic-gates]]** — the playbook's sharpest contribution is a two-tier control vocabulary: a *skill* is an advisory control, a *hook* is the deterministic layer behind it; "the skill makes violations rare and the hook makes them close to impossible." Any policy that must always hold needs the deterministic backstop. This is the same advisory-vs-enforced split the [[topic-software-factory]] worked example draws across four layers.
- **[[pattern-edit-guardrails]]** — build-phase hooks blocking protected paths, keeping credentials out of the diff; plus the managed-settings worked example (permission deny-lists, OS sandbox with egress allowlist, credential blocks, marketplace pinning) — the enterprise, MDM-deployed form of the pattern.
- **[[pattern-evidence-before-claims]]** — verification is part of "done": paste the literal `make test` output; the evidence must come from the toolchain, not the agent's assertion.
- **[[pattern-test-driven-development]]** — for bug fixes: commit the failing test first, then forbid the agent from editing it (enforced by hook), so the pre-existing test is proof the bug is gone. The playbook adds the guardrail rationale explicitly: an agent fixing code must not be able to weaken the check on that code.
- **[[pattern-fresh-context-subagents]]** — the verifier subagent runs the final check in a fresh context window "so the verdict is not colored by the assumptions that produced the code," carefully distinguished from the in-task feedback loop.
- **[[pattern-worktree-isolation]] and [[pattern-wave-parallelism]]** — parallel sessions in worktrees, ceiling set by how many streams one person can review, not by compute.
- **[[pattern-knowledge-compounding]]** — the CLAUDE.md working rule ("when Claude makes a mistake twice, the correction goes into CLAUDE.md"), review findings feeding back into CLAUDE.md, incidents becoming permanent evals, and post-mortems written to a version-controlled lessons file.
- **[[pattern-context-engineering]]** — keep CLAUDE.md under a page; "anything stale is taking up context for no benefit."
- **[[pattern-measure-first]]** — in spirit: every play ships a leading and lagging indicator, read from git timestamps, PR metadata, or the OpenTelemetry export rather than from surveys.

One genuinely novel instrument: **continuous evals of the agent's configuration**. The suite of 20–50 real tasks re-runs on any change to CLAUDE.md, skills, or hooks — the steering configuration gets the regression testing that code gets, and a skill change that drops the pass rate is blocked at merge. No community framework in the wiki ships this; it is the QA gate rebuilt for the thing that now varies (the agent's setup, not just the code).

## The factory, from the governance side

Stage 6 describes a [[topic-software-factory|software factory]] in all but name, and lands on the same anatomy from the compliance direction. A version-controlled `bands.yaml` defines response tiers over a deterministic detection script — log at 1σ, diagnose read-only at 2σ, act at 3σ but only by opening a PR into the review gate or triggering a pre-approved runbook — with the emphatic rule that *detection stays deterministic, no model involved*. In factory vocabulary: an event/schedule **trigger**, a code-owned **control plane** (the tiers are config, not prompt), sandboxed stateless workers, **gates** the agent cannot pass ("the agent may act up to the production gate and cannot pass it"), and **escalation** as PR-into-review. The tiered-autonomy config is the closest any wiki source comes to [[gh-aw]]'s compiled-policy shape expressed as a governance document, and the headless stage-to-stage handoff — "an independent confidence gate between stages… deciding whether the previous stage's output continues or is escalated to a human" — is the maker/checker rule from the factory glossary, applied between lifecycle stages rather than within a run.

The separation-of-duties principle recurs at every gate: the agent that wrote the code has no way to approve it; the agent that proposed a security patch has no route to merge it; each non-interactive run acts under the agent's own identity so logs separate agent actions from the triggering engineer's.

## What this page deliberately does not do

The playbook is a vendor document: its plays name Claude products (Claude Code, Cowork, Claude Design, Code Review, Claude Security, Claude Tag, the Agent SDK) where the wiki's other sources name mechanisms. This page reads it for the mechanisms, which are product-independent; the capture preserves the product framing. It is also not ingested as a `framework` — it ships prose and templates, not an installable capability set, and the wiki's [[claude-code]] harness page already carries the primitives (plan mode, hooks, skills, subagents, managed settings) the plays are built from. If Anthropic later ships the plays as an installable plugin, that would be a framework ingest with `runs_on: [[claude-code]]`.

## See Also

- [[topic-software-factory]] — the execution-layer architecture Stage 6 arrives at from the governance side; its glossary defines the vocabulary used above.
- [[topic-harness-engineering]] — the per-run steering controls (guides/sensors) the playbook's CLAUDE.md/skills/hooks plays instantiate; the playbook is that frame scaled to an organization with auditors.
- [[topic-agent-readiness]] — the maturity axis: the playbook's prerequisite graph ("adopt plays in dependency order") is a transformation *sequence*, where readiness scores the *substrate*; VirtusLab's org-scoped matrix is the closest sibling.
- [[stage-align]] · [[stage-specify]] · [[stage-plan]] · [[stage-validate]] · [[stage-review]] · [[stage-learn]] — the derived stages the six-stage frame maps onto.
- [[pattern-deterministic-gates]] · [[pattern-spec-driven-development]] · [[pattern-evidence-before-claims]] · [[pattern-knowledge-compounding]] — the load-bearing patterns the playbook confirms from outside the community-framework pool.
- Louis Claxton, *The AI-Native SDLC playbook* ([capture](../../raw/reference/2026-08-21-ai-native-sdlc-playbook.md)).
