---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); gstack — Garry Tan (2026); tao-hpu/nano-spec (2025); mattpocock/sandcastle (2026); jayminwest/warren (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026); pi.dev (Earendil, 2026)"
updated: 2026-07-31
---

# Pattern: Session handoff

Compact the working context — decisions, current state, next steps — into a durable form so a fresh agent or session can resume without re-deriving it. Counters context loss across session boundaries and agent transitions.

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

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) carries working context across a *run* boundary without a handoff document — the runtime itself is the persistence:

- [[sandcastle]] (library) — session **capture & resume** (`resumeSession`) and session **forking** continue or branch a prior agent conversation across `run()` invocations.
- [[warren]] (platform) — `.mulch/` priming on spawn, mid-run **steering**, and the persisted NDJSON event log let a run pick up (and be redirected on) prior state.

## Provided by (harness)

The [harness layer](../harness/index.md) carries working context across a *context-window* or *session* boundary without any framework-level handoff document — the persistence is in the agent program:

- [[claude-code]] — automatic **compaction** summarizes a long session so work continues into a fresh context window, and **session resume** (`--resume` / persisted sessions) reopens a prior conversation; the harness primitive below [[mp-handoff]] / [[gstack-context-save]].
- [[opencode]] — session management with **undo/redo**, resume, and shareable web links.
- [[pi]] — **tree-structured, resumable, shareable** session history (`~/.pi/agent/sessions/`) plus context compaction with customizable summarization; arguably pi's signature primitive.
- [[factory-droid]] — subagents each carry their own session, the **Droid Sessions API** and persisted sessions reopen prior work, and headless **`droid exec`** runs are scriptable/resumable across a session boundary.

## See Also
- [[artifact-handoff-doc]] — Matt's materialized handoff.
- [[pattern-fresh-context-subagents]] — the complementary GSD technique for staying within context.
- [[pattern-knowledge-compounding]] — carries *lessons* across iterations, versus this pattern's *working context* across a boundary.
- [[sandcastle]] · [[warren]] — the runtimes that persist/resume session state as infrastructure.
- [[claude-code]] · [[opencode]] · [[pi]] · [[factory-droid]] — the harnesses that compact/resume session context as a built-in.
