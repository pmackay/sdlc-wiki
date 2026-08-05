---
type: pattern
sources: "gstack — Garry Tan (2026); Anthropic — Claude Code (2026); opencode.ai (Anomaly, 2026)"
updated: 2026-07-31
---

# Pattern: Edit guardrails (gate the agent's power to destroy or stray)

Give an autonomous coding agent **explicit, toggleable guardrails on mutating operations** so it cannot destroy data or "fix" code outside the current scope. Two coupled moves:

1. **Confirm before destroying.** Warn before irreversible commands — `rm -rf`, `DROP TABLE`, force-push, `git reset --hard` — and let the human decide ([[gstack-careful]]).
2. **Lock edits to scope.** Restrict file edits to a named directory for the session as a **hard block, not a warning** ([[gstack-freeze]]), so a focused task (especially a debugging session) can't ripple into unrelated code. [[gstack-guard]] combines both; [[gstack-unfreeze]] releases the lock; [[gstack-investigate]] auto-freezes to the module under investigation.

## Why it's distinctive

This is gstack's **signature safety mechanism** and has no counterpart among the other frameworks in this wiki — others rely on the harness's generic confirmations or on careful prompting. Guardrails are the operational expression of gstack's *User Sovereignty* ethos ("models recommend, users decide") and what makes running **10-15 parallel autonomous sprints** tolerable: each agent is fenced so a stray edit or a fat-fingered destructive command can't cascade across workspaces. It is the *complement* to [[pattern-worktree-isolation]] — that pattern isolates the filesystem so parallel work can't collide; this one gates the mutations an agent is even allowed to attempt.

## Applied by (backlinks)

gstack:

- [[gstack-careful]] — warn before destructive commands (the confirm half).
- [[gstack-freeze]] — hard-lock edits to one directory (the scope half).
- [[gstack-guard]] — activate both at once.
- [[gstack-unfreeze]] — release the freeze boundary.
- [[gstack-investigate]] — auto-freezes to the module under investigation.

## Provided by (harness)

The [harness layer](../harness/index.md) supplies the mutation-gating substrate that gstack's guardrail skills configure — the guardrails are policy on top of a harness primitive:

- [[claude-code]] — **hooks** (a `PreToolUse` hook can block or rewrite a tool call) plus **permission modes** (default / plan / acceptEdits / bypass) and allow/deny/ask rules in `settings.json` are the enforcement layer gstack's careful/freeze/guard skills sit on; plan mode is a read-only fence before any edit is allowed.
- [[opencode]] — a **permissions/policies** framework (e.g. the plan agent set to "ask" before edits/bash) plus **plan vs build** modes and hooks that can block a tool call.
- [[factory-droid]] — **autonomy levels** (off/low/medium/high, set via `--auto`) + a read-only/normal review mode + permission-checked tools + **hooks** for policy enforcement + approval workflows gate what an edit or shell command may do.
- **Not [[pi]]** — no built-in permission prompts (extension/sandbox territory); pi leans on containerization for boundaries.

## See Also
- [[pattern-worktree-isolation]] — the filesystem-isolation complement (isolate *where* work happens vs gate *what* it may do).
- [[pattern-autonomous-loop]] — the autonomy these guardrails make safe.
- [[gstack]] — the framework this pattern is signature to.
- [[claude-code]] · [[opencode]] · [[factory-droid]] — the harnesses whose hooks + permission frameworks provide the enforcement substrate (pi omits it from core).
