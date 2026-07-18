---
type: pattern
sources: "gstack — Garry Tan (2026)"
updated: 2026-07-05
---

# Pattern: Edit guardrails (gate the agent's power to destroy or stray)

Give an autonomous coding agent **explicit, toggleable guardrails on mutating operations** so it
cannot destroy data or "fix" code outside the current scope. Two coupled moves:

1. **Confirm before destroying.** Warn before irreversible commands — `rm -rf`, `DROP TABLE`,
   force-push, `git reset --hard` — and let the human decide ([[gstack-careful]]).
2. **Lock edits to scope.** Restrict file edits to a named directory for the session as a **hard
   block, not a warning** ([[gstack-freeze]]), so a focused task (especially a debugging session)
   can't ripple into unrelated code. [[gstack-guard]] combines both; [[gstack-unfreeze]] releases
   the lock; [[gstack-investigate]] auto-freezes to the module under investigation.

## Why it's distinctive

This is gstack's **signature safety mechanism** and has no counterpart among the other frameworks
in this wiki — others rely on the harness's generic confirmations or on careful prompting.
Guardrails are the operational expression of gstack's *User Sovereignty* ethos ("models recommend,
users decide") and what makes running **10-15 parallel autonomous sprints** tolerable: each agent
is fenced so a stray edit or a fat-fingered destructive command can't cascade across workspaces. It
is the *complement* to [[pattern-worktree-isolation]] — that pattern isolates the filesystem so
parallel work can't collide; this one gates the mutations an agent is even allowed to attempt.

## Applied by (backlinks)

gstack:

- [[gstack-careful]] — warn before destructive commands (the confirm half).
- [[gstack-freeze]] — hard-lock edits to one directory (the scope half).
- [[gstack-guard]] — activate both at once.
- [[gstack-unfreeze]] — release the freeze boundary.
- [[gstack-investigate]] — auto-freezes to the module under investigation.

## See Also
- [[pattern-worktree-isolation]] — the filesystem-isolation complement (isolate *where* work happens vs gate *what* it may do).
- [[pattern-autonomous-loop]] — the autonomy these guardrails make safe.
- [[gstack]] — the framework this pattern is signature to.
