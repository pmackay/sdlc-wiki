---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-implement]]"
delegates_to: ["[[pstack-why]]", "[[pstack-unslop]]"]
produces: ["[[artifact-handoff-doc]]"]
applies: ["[[pattern-session-handoff]]", "[[pattern-context-engineering]]", "[[pattern-wave-parallelism]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[gstack-context-restore]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /recall

Rebuilds the user's recent working context before starting or resuming work, and hands back a tight current-state brief. *"Catch me up", "what have I been working on", "where did I leave off".*

Its distinctive claim is that **your context lives in two records, and reconstructing from one is not enough**. Your own chat history holds what you did and decided. The shared record holds everything that happened around the same code under other names — the symptoms users keep reporting, the fixes that shipped and got reverted, the errors still firing in production. *A feature with a long bug tail keeps most of its story there, so do not reconstruct it from your transcripts alone.* This is [[pattern-session-handoff]] widened from *what the last agent was doing* to *what the organization knows about this work*, and it is the wiki's first capability to page that distinction.

The two records are mined in parallel. Chat history is fanned out to subagents on a fast cheap model, each taking a slice, each ordering candidates by real modification time (never by UUID name), grepping the topic first and reading only matching regions, and returning one block per chat to a fixed schema: topic, goal, decisions, open threads, struggles and corrections, artifacts, each citing the chat UUID. Raw transcripts stay in the subagents. The shared record is swept by handing the job to [[pstack-why]]'s source investigators with the question re-pointed from *why was this built this way* to *what is the current state, what has been tried and did not hold, and what are users still reporting*. That sweep is the default, not a judgment call. Whatever both surface is then **verified against live state** with `git` and `gh`.

The output contract is strict enough to be worth recording. A **capsule** of at most five bullets, then **threads** one line each carrying exactly one status tag (`[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, `[planned, not started]`), then at most five recurring **problems** including any fix that shipped and was reverted so the next attempt starts where the last one failed, then a single concrete **next move**. When it outgrows a screen, cut detail before cutting threads.

It also routes away from itself deliberately: one specific prior chat to resume is the Session pickup playbook, and turning habits into a durable skill is [[pstack-automate-me]].

## See Also
- [[pstack-why]] — supplies the shared-record sweep and its per-source playbooks.
- [[pstack-poteto-mode]] — its Session pickup and Pause safely playbooks are the neighbouring resumption procedures.
- [[gstack-context-restore]] — the cross-framework counterpart, which restores saved state rather than reconstructing it.
- [[stage-implement]] — the canonical stage this implements.
