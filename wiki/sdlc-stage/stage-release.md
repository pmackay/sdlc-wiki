---
type: sdlc-stage
aka: { gsd: "Ship", addy-agent-skills: "Ship", openspec: "sync + archive", compound-engineering: "commit-push-pr / promote", gstack: "Ship + land-and-deploy + canary", superpowers: "finishing-a-development-branch" }
sources: "Synthesized from GSD + Addy Osmani + OpenSpec + Compound Engineering + gstack + Superpowers (2026)"
updated: 2026-07-17
---

# Stage: Release

Canonical lifecycle stage: **finalize validated work and close the iteration** — for most
frameworks that means packaging, shipping safely, and keeping it healthy in production
(versioning, integration, deployment, launch, observability, and later
deprecation/migration); for a spec-first framework it means **folding the completed change
back into the durable source of truth**. Framework-neutral name (was `stage-ship`, GSD's term).

**Derived projection** — evidence is the capabilities that `implements: [[stage-release]]`.

> **No longer single-framework (updated 2026-07-04).** Was the weakest stage (GSD-only); Addy
> Osmani's Ship phase adds six capabilities spanning git/versioning, CI/CD, launch, observability,
> documentation, and deprecation, and OpenSpec adds its finalization step — making release a
> well-evidenced canonical stage. It is now the broadest activity on the delivery side and a
> candidate to split (see below).

> **Two flavors of "release" in the evidence.** GSD, Addy, Compound Engineering, and gstack
> finalize by **shipping to production** (commit, PR, launch checklist, deploy, announce). OpenSpec
> finalizes by **spec-maintenance** — [[openspec-sync]] merges the change's delta into the living
> spec and [[openspec-archive]] retires the change — with *no* deploy/CI/observability step at all.
> Same lifecycle slot (deliver completed, validated work), two different terminal acts.
>
> **gstack (2026-07-05) pushes the ship-to-prod flavor furthest** — it is the **first framework
> here to separate deploy from ship as its own command**: [[gstack-ship]] opens the PR,
> [[gstack-land-and-deploy]] merges + deploys + verifies production health, and [[gstack-canary]]
> monitors post-deploy. That deploy→verify→operate arc is the new evidence strengthening the
> `stage-operate` split candidate below.
>
> A former third flavor — BMAD's **learning close-out** ([[bmad-retrospective]]) — was
> **promoted out of this stage** on 2026-07-04 into its own [[stage-learn]] once Compound
> Engineering's [[ce-compound]] gave learning-capture a second framework. Extracting reusable
> lessons is a distinct activity from delivering the work; see [[stage-learn]].

## Implemented by (backlinks)

GSD:

- [[gsd-ship]] — pushes branch, opens PR with auto summary, tracks merge → [[artifact-pull-request]].

Addy Osmani — Agent Skills:

- [[addy-shipping]] — pre-launch checklist, staged rollout, rollback, `/ship` persona fan-out → [[artifact-launch-checklist]] ([[pattern-parallel-persona-review]], [[pattern-feature-flags]]).
- [[addy-git-workflow]] — trunk-based dev, atomic commits, semver, changelogs → [[artifact-atomic-commit]], [[artifact-changelog]] ([[pattern-trunk-based-development]]).
- [[addy-ci-cd]] — Shift Left quality-gate pipelines ([[pattern-shift-left]], [[pattern-feature-flags]]).
- [[addy-observability]] — structured logging, RED metrics, tracing, symptom-based alerting.
- [[addy-documentation]] — ADRs + API/inline docs → [[artifact-adr]].
- [[addy-deprecation]] — code-as-liability; safe sunsetting and migration.

Compound Engineering (ship-to-prod):

- [[ce-commit]] — one well-crafted atomic commit with convention awareness → [[artifact-atomic-commit]] ([[pattern-trunk-based-development]]).
- [[ce-commit-push-pr]] — working changes → open PR with adaptive descriptions → [[artifact-pull-request]]; finalize-cluster with [[gsd-ship]] + [[addy-shipping]].
- [[ce-resolve-pr-feedback]] — evaluate, fix, and reply to PR review feedback in parallel (the pre-merge resolution step).
- [[ce-promote]] — draft user-facing launch announcements (X / changelog / LinkedIn / email).
- [[ce-product-pulse]] — time-windowed post-release usage/perf/error report (operate/monitor).

OpenSpec (spec-maintenance, not deployment):

- [[openspec-sync]] — merge the change's [[artifact-spec-delta]] into the living main specs.
- [[openspec-archive]] — finalize the change; optionally sync, then move it to `archive/`.

gstack (ship-to-prod, with a genuine deploy + operate arc):

- [[gstack-ship]] — sync base, test, review, bump VERSION + CHANGELOG, commit, push, open PR → [[artifact-pull-request]], [[artifact-changelog]], [[artifact-atomic-commit]] ([[pattern-trunk-based-development]]).
- [[gstack-land-and-deploy]] — merge the PR, wait for CI + deploy, verify production health (the **deploy** step; no other framework ships one).
- [[gstack-canary]] — post-deploy monitoring loop (console errors, perf regressions) → counterpart to [[ce-product-pulse]] (operate/monitor).
- [[gstack-setup-deploy]] — one-time deploy configuration (enabling).
- [[gstack-landing-report]] — read-only ship-queue dashboard.
- [[gstack-document-release]] · [[gstack-document-generate]] — post-ship Diataxis docs update/generation → [[artifact-diataxis-docs]].
- [[gstack-ios-clean]] — strip the debug bridge before a Release build (enabling).

Superpowers (ship-to-prod flavor; stops at PR/merge — no deploy):

- [[sp-finishing-a-development-branch]] — verify tests → detect the workspace → present **exactly four options** (merge locally / push+PR / keep / discard) → execute → clean up the worktree per choice → [[artifact-pull-request]] ([[pattern-trunk-based-development]]). Distinctive for the **decision menu** — it doesn't assume ship-to-prod, it asks.

## Cross-framework equivalents
The **finalize / close-out** cluster spans five frameworks: OpenSpec's [[openspec-archive]] ↔
Addy's [[addy-shipping]] ↔ GSD's [[gsd-ship]] ↔ Compound Engineering's [[ce-commit-push-pr]] ↔
Superpowers' [[sp-finishing-a-development-branch]] —
each closes the iteration on a completed unit, but finalizes *different things*: GSD opens and
tracks a PR, Addy fans out parallel review personas for a go/no-go launch, Compound Engineering
goes working-changes→PR and (with [[ce-promote]]) announces the launch, OpenSpec merges the
spec delta and archives the change, and Superpowers presents a **merge/PR/keep/discard decision
menu** and cleans up its worktree accordingly (like GSD and OpenSpec, it stops at PR/merge with
**no deploy step**). Addy's other five capabilities (versioning, CI/CD,
observability, docs, deprecation) still have **no counterpart** in GSD, MP, OpenSpec, Spec Kit,
or BMAD; OpenSpec's spec-maintenance is unique. Compound Engineering is the closest match to the
GSD/Addy ship-to-prod flavor. (These are *not* set as `equivalent_to` edges: the terminal acts
differ too much to cluster as counterparts.) The former **learning close-out** flavor
([[bmad-retrospective]]) now lives in [[stage-learn]], alongside Compound Engineering's
[[ce-compound]].

> **Spec Kit ships no release capability (2026-07-04).** Like OpenSpec, Spec Kit stops at the
> validate loop: [[speckit-converge]] closes the spec↔code gap by re-planning, but there is no
> deploy / PR / launch / observability command. Its [[speckit-taskstoissues]] pushes tasks to
> GitHub issues (a [[stage-plan]] tracker bridge), not a release act. So Spec Kit adds no
> backlink here.

## Split candidates

### stage-operate / stage-maintain (deploy, run it in production, sunset it) — strengthening
- **Distinction:** *release* = ship the work (PR/merge); *operate* = deploy it and keep it healthy in production (deploy, verify, observability, alerting); *maintain* = retire/migrate it later. Distinct from opening/merging the PR.
- **Evidence so far (now capability-level in three frameworks, but not yet a distinct *phase*):**
  - Addy folds observability ([[addy-observability]]), CI/CD ([[addy-ci-cd]]), and deprecation ([[addy-deprecation]]) into Ship.
  - Compound Engineering adds post-release monitoring ([[ce-product-pulse]]).
  - **gstack (2026-07-05) is the first to give deploy its own command** ([[gstack-land-and-deploy]]) *separate from* ship, plus a dedicated post-deploy monitor ([[gstack-canary]]) and deploy config ([[gstack-setup-deploy]]) — a genuine deploy→operate arc. But gstack still nests these under the release/ship end of its sprint rather than naming a standalone *Operate* phase.
  - So deploy+operate is now a **dedicated capability in three frameworks** (Addy, CE, gstack) but a distinct *phase* in none.
- **Decisive trigger:** a framework that treats **operate/deploy as its own lifecycle phase** distinct from release (or a second framework separating deploy into its own command + phase) → clears the bar → split into `stage-operate`. Watch closely — gstack has brought this from one framework to three at the capability level.

## See Also
- [[stage-validate]] · [[stage-review]] — the functional and quality gates that must pass before this stage.
- [[stage-learn]] — the sibling close-out stage split out of release (2026-07-04): release *delivers* the work, learn *compounds* the lessons.
- [[stage-align]] — the next iteration begins here (reading [[stage-learn]]'s output as grounding).
