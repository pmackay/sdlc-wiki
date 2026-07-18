---
type: artifact
sources: "Matt Pocock — Skills for Real Engineers (2026); GitHub/spec-kit (2026)"
updated: 2026-07-05
---

# Artifact: Tracker issue

An issue on the tracker (GitHub, Linear, or local files) materialised from a plan. Two frameworks produce these, from opposite directions:

- **Matt Pocock — [[mp-to-tickets]]**: *decomposes* a plan/spec into independently-grabbable **tracer-bullet vertical-slice** tickets, each declaring its blocking edges (see [[pattern-vertical-slice]]). Its siblings [[mp-wayfinder]] (investigation tickets) and [[mp-triage]] (agent-ready briefs) also write tracker issues.
- **Spec Kit — [[speckit-taskstoissues]]**: *exports* an already-decomposed `tasks.md` ([[artifact-plan-md]]) to GitHub issues (one issue per task) — a mechanical bridge, not a decomposition.

## Produced by (backlinks)
- [[mp-to-tickets]] — decomposes plans/specs into tracer-bullet vertical-slice tickets with blocking edges.
- [[mp-wayfinder]] — writes investigation tickets as a shared map for oversized work.
- [[mp-triage]] — writes agent-ready briefs onto triaged issues/PRs.
- [[speckit-taskstoissues]] — exports the Spec Kit task list to GitHub issues.
- [[gstack-spec]] — files a deduped GitHub issue from the spec (auto-closed by /ship on merge).

## See Also
- [[artifact-prd]] — common upstream source.
- [[artifact-story]] — BMAD's richer counterpart: a tracker-issue-like unit with all implementation context inlined.
- [[artifact-plan-md]] — Spec Kit's `tasks.md`, the direct source for its issues.
- [[pattern-vertical-slice]] — the slicing principle (shared with GSD `--mvp`).
