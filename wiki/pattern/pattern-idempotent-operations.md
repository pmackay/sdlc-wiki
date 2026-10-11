---
type: pattern
sources: "pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-10-11
---

# Pattern: Idempotent operations

Design commands, lifecycle steps, and processing loops to **converge to the same end state regardless of partial prior runs**. Re-running is always safe; a crash, a restart, or a retry mid-way leaves no half-state the next run has to reason about.

This is classic operational engineering, but it acquires a specific edge in agent work, which is why it earns a pattern page here rather than staying an implementation detail. Agent runs are **interrupted far more often than human ones** — context compaction, a session ending, a killed subagent, a cloud worker dropping out, an operator pressing stop. Every long-horizon capability in this wiki therefore depends on its steps being re-enterable, and the frameworks that run unattended lean on it hardest. It is the precondition that makes [[pattern-autonomous-loop]] and [[pattern-session-handoff]] safe: a resumed session can re-run the last step rather than having to determine exactly how far the dead one got.

Its most visible expression is a setup or configuration command that **overwrites its whole output** rather than patching it, so a second run cannot accumulate drift from the first.

## Applied by (backlinks)

pstack:

- [[pstack-principle-make-operations-idempotent]] — the principle statement, scoped to commands, lifecycle steps, and loops that run amid crashes and retries.
- [[pstack-setup-pstack]] — overwrites the whole model-role rule file on every run so re-runs stay idempotent.
- [[pstack-benny-setup]] — a re-runnable install that preserves destination-only files and reviews conflicts instead of overwriting local edits.

Tessl:

- [[tessl-environment]] — an update **replaces** an environment's values rather than merging them, so a re-run converges on exactly the supplied set. Safety over convenience, and the right default for a secret store.
- [[tessl-schedule]] — recurring unattended runs, which only make sense if each run is safe to repeat.

builder-skills:

- [[builder-factory-recover]] — the resumption side. Recheck external state before retrying an uncertain action, and *"do not repeat completed writes, replies, approvals, merges, or deployments."*

Matt Pocock — Skills for Real Engineers:

- [[mp-wizard]] — generated wizards upsert values into `.env` files idempotently and write `gh secret`/`gh variable` with graceful degradation, so a re-run is safe (v1.2.0).

## See Also
- [[pattern-autonomous-loop]] — long unattended runs depend on their steps being re-enterable.
- [[pattern-session-handoff]] — resumption is cheap when re-running a step is free.
- [[pattern-deterministic-gates]] — both make a run's outcome independent of how it got there.
