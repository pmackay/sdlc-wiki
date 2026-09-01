---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); gstack — Garry Tan (2026); tao-hpu/nano-spec (2025); mattpocock/sandcastle (2026); jayminwest/warren (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026); pi.dev (Earendil, 2026); sipyourdrink-ltd/bernstein (2026); jayminwest/seeds (2026); gastownhall/beads (2026); disler/super-simple-software-factory (2026)"
updated: 2026-08-31
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

Seeds — the handoff object is the queue, not the conversation:

- [[seeds-sync]] — commits the `.seeds/` state to git, making it the durable boundary object between sessions and between branches.
- [[seeds-prime]] — restores it on the other side. A fresh agent needs no narrative reconstruction, only the rules plus `sd ready`; contrast [[mp-handoff]] and [[gstack-context-restore]], which compact and replay a *conversation*.

Beads — the pattern is the entire product thesis: *"Work survives the agent; the next session picks up where the last one died."*

- [[beads-prime]] — restores workflow rules **and** persistent memories at `SessionStart`, sized to the detected context budget. Where [[mp-handoff]] compacts a *conversation* and [[gstack-context-restore]] replays one, beads restores standing knowledge and leaves the work state to the graph — a fresh agent needs no narrative, only [[beads-ready]].
- [[beads-remember]] — the durable half of what `prime` hands back.

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) carries working context across a *run* boundary without a handoff document — the runtime itself is the persistence:

- [[sandcastle]] (library) — session **capture & resume** (`resumeSession`) and session **forking** continue or branch a prior agent conversation across `run()` invocations.
- [[warren]] (platform) — `.mulch/` priming on spawn, mid-run **steering**, and the persisted NDJSON event log let a run pick up (and be redirected on) prior state.
- [[sssf]] (library) — `agent_map.json` records agent → coding-agent session id → model per run id, so a second ADW invoked with the same `--adw-id` has each agent **resume its own existing context window** rather than starting cold (`adw_plan.py` then `adw_build.py --adw-id a1b2c3d4`). The map stores the model each session was created with and starts a *fresh* session if config drift changed it — *"never a bad resume."* The same mechanism serves within-phase corrections: because [[pi]] treats `--session-id` as create-or-continue, a failed envelope parse or gate violation re-prompts the live session instead of restarting it, since *"a cold restart throws away everything the agent learned. A correction costs one message."*
- [[bernstein]] (platform) — `bernstein handoff emit` / `claim` moves a **live** session between surfaces (terminal → web dashboard → chat bridge) on a short-lived single-use token, alongside durable suspend/resume, fork-from-step, and a `session_memory` compaction tier that distils a completed session into a durable cross-session summary.

## Provided by (harness)

The [harness layer](../harness/index.md) carries working context across a *context-window* or *session* boundary without any framework-level handoff document — the persistence is in the agent program:

- [[claude-code]] — automatic **compaction** summarizes a long session so work continues into a fresh context window, and **session resume** (`--resume` / persisted sessions) reopens a prior conversation; the harness primitive below [[mp-handoff]] / [[gstack-context-save]].
- [[opencode]] — session management with **undo/redo**, resume, and shareable web links.
- [[pi]] — **tree-structured, resumable, shareable** session history (`~/.pi/agent/sessions/`) plus context compaction with customizable summarization; arguably pi's signature primitive.
- [[factory-droid]] — subagents each carry their own session, the **Droid Sessions API** and persisted sessions reopen prior work, and headless **`droid exec`** runs are scriptable/resumable across a session boundary.

## Persisted by (store)

The [state layer](../store/index.md) is where this pattern stops being a document an agent writes and becomes a property of the project. Both stores make it their headline claim.

- [[beads]] — *"Coding agents lose their memory every time a session ends. Markdown plans rot, TODO comments scatter, and a crashed agent takes its context with it… Work survives the agent; the next session picks up where the last one died."* The handoff object is the graph plus the memory set, restored by [[beads-prime]] at `SessionStart`.
- [[seeds]] — the committed `.seeds/` queue is the handoff: a fresh agent reads `sd ready` instead of reconstructing where the last one stopped ([[seeds-sync]] → [[seeds-prime]]).

The distinction worth keeping from the process-layer roster above: [[mp-handoff]] and [[gstack-context-save]] preserve a **conversation**, and a store preserves **work state**. The second is cheaper, survives a crash rather than only an orderly exit, and is the reason this layer exists at all.

## See Also
- [[artifact-handoff-doc]] — Matt's materialized handoff.
- [[pattern-fresh-context-subagents]] — the complementary GSD technique for staying within context.
- [[pattern-knowledge-compounding]] — carries *lessons* across iterations, versus this pattern's *working context* across a boundary.
- [[sandcastle]] · [[warren]] · [[bernstein]] — the runtimes that persist/resume session state as infrastructure.
- [[claude-code]] · [[opencode]] · [[pi]] · [[factory-droid]] — the harnesses that compact/resume session context as a built-in.
