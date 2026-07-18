---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); gstack — Garry Tan (2026); tao-hpu/nano-spec (2025)"
updated: 2026-07-13
---

# Pattern: Session handoff

Compact the working context — decisions, current state, next steps — into a durable form so
a fresh agent or session can resume without re-deriving it. Counters context loss across
session boundaries and agent transitions.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-handoff]] — compacts a conversation into a [[artifact-handoff-doc]].

GSD:

- [[gsd]] — structural persistence via `STATE.md` / `CONTEXT.md` and `pause-work` / `resume-work` (not yet a dedicated capability page).

gstack (the **third framework**; adds continuous WIP-checkpoint commits for crash recovery):

- [[gstack-context-save]] — save git state + decisions + remaining work; optional `WIP:` checkpoint commits with structured `[gstack-context]` bodies.
- [[gstack-context-restore]] — reconstruct session state from the saved context / checkpoint commits, even across Conductor workspaces.

nano-spec (the **fourth framework**; the handoff form is the always-current spec pack itself, not a separate doc):

- [[nano-spec-status]] — summarize a task's state (done vs. total, blockers, last-log date) from the pack.
- [[nano-spec-update]] — keep the [[artifact-nano-spec-pack|4-file pack]] (esp. dated `log.md`) current so "read all 4 files and explain the project" resumes a fresh agent or teammate without re-derivation.

## See Also
- [[artifact-handoff-doc]] — Matt's materialized handoff.
- [[pattern-fresh-context-subagents]] — the complementary GSD technique for staying within context.
- [[pattern-knowledge-compounding]] — carries *lessons* across iterations, versus this pattern's *working context* across a boundary.
