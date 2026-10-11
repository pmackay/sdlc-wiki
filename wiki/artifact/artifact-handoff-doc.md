---
type: artifact
sources: "Matt Pocock — Skills for Real Engineers (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-09-26
---

# Artifact: Handoff document

A compacted summary of a conversation — decisions, state, next steps — produced by [[mp-handoff]] so a fresh agent or session can resume without re-deriving context. The portable counterpart to GSD's in-repo `STATE.md` persistence; both realize [[pattern-session-handoff]].

## Produced by (backlinks)
- [[mp-handoff]] — compacts the conversation into this document.

pstack:

- [[pstack-recall]] — a current-state brief to a strict contract: a capsule of at most five bullets, thread lines each carrying exactly one status tag (`[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, `[planned, not started]`), at most five recurring problems including any fix that shipped and was reverted, and one concrete next move. Reconstructed from **two** records — the agent's own chat history and the shared organizational record.

builder-skills:

- [[builder-stay-within-limits]] — the self-contained wake prompt a budget pause leaves for the agent's own next turn.
- [[builder-plow-ahead]] — the blocked-state handoff (what was done, what blocks progress, the exact input needed, the next command or file).

## See Also
- [[artifact-decision-log]] — the human-facing counterpart; a handoff doc is read by the next agent, a decision log by a person who was not watching.
- [[pattern-session-handoff]] — the shared technique.
