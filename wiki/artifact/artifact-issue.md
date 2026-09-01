---
type: artifact
sources: "Matt Pocock — Skills for Real Engineers (2026); GitHub/spec-kit (2026); jayminwest/seeds (2026); gastownhall/beads (2026)"
updated: 2026-08-31
---

# Artifact: Tracker issue

An issue on the tracker (GitHub, Linear, or local files) materialised from a plan — or, in the [store layer](../store/index.md), the primitive the tracker is *made of* rather than an output of planning. Three frameworks and two stores produce these, from different directions:

- **Matt Pocock — [[mp-to-tickets]]**: *decomposes* a plan/spec into independently-grabbable **tracer-bullet vertical-slice** tickets, each declaring its blocking edges (see [[pattern-vertical-slice]]). Its siblings [[mp-wayfinder]] (investigation tickets) and [[mp-triage]] (agent-ready briefs) also write tracker issues.
- **Seeds — [[seeds-create]] / [[seeds-plan-submit]]**: the tracker *is* the repo. Issues are JSON objects in `.seeds/issues.jsonl` on the same branch as the code, merged by git rather than hosted — so an agent with no network and no tracker credentials can file, claim, and close work, and the issue state is a reviewable part of the diff.
- **Beads — [[beads-create]] / [[beads-mol]]**: the issue is the atom, not a derivative. A **bead** carries a content-hash id, typed dependency edges (only some of which gate work), knowledge-graph links, and structured `design` / `notes` / `acceptance` fields — an issue rich enough that an agent claiming it weeks later has what it needs. [[beads-lint]] checks that it does.
- **Spec Kit — [[speckit-taskstoissues]]**: *exports* an already-decomposed `tasks.md` ([[artifact-plan-md]]) to GitHub issues (one issue per task) — a mechanical bridge, not a decomposition.

## Produced by (backlinks)
- [[mp-to-tickets]] — decomposes plans/specs into tracer-bullet vertical-slice tickets with blocking edges.
- [[mp-wayfinder]] — writes investigation tickets as a shared map for oversized work.
- [[mp-triage]] — writes agent-ready briefs onto triaged issues/PRs.
- [[speckit-taskstoissues]] — exports the Spec Kit task list to GitHub issues.
- [[gstack-spec]] — files a deduped GitHub issue from the spec (auto-closed by /ship on merge).
- [[seeds-create]] — files one typed, prioritized seed into `.seeds/issues.jsonl`.
- [[seeds-plan-submit]] — spawns one child seed per plan step, with the plan's `blocks` indices translated into real dependency edges.
- [[seeds-tpl-pour]] — instantiates a convoy template into a serially-wired chain of issues.
- [[seeds-issue-workflow]] — the skill that routes a vague ask to whichever of the two paths above fits.
- [[beads-create]] — files a bead (with `bd q` for quick capture and `bd batch` for one transaction).
- [[beads-mol]] — pours a formula template into a whole graph of dependency-ordered beads at once.
- [[beads-todo]] — the deliberately-cheap wrapper, so a throwaway TODO is still a tracked issue.

## See Also
- [[artifact-prd]] — common upstream source.
- [[artifact-story]] — BMAD's richer counterpart: a tracker-issue-like unit with all implementation context inlined.
- [[artifact-plan-md]] — Spec Kit's `tasks.md`, the direct source for its issues.
- [[artifact-plan-record]] — the seeds plan row whose steps become these issues one-for-one, and which keeps a link back to each.
- [The store layer](../store/index.md) — where an issue stops being a plan's output and becomes the durable unit of state agents claim from.
- [[pattern-vertical-slice]] — the slicing principle (shared with GSD `--mvp`).
