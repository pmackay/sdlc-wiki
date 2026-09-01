---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd audit

`bd audit record|label` — an **append-only log of agent interactions** at `.beads/interactions.jsonl`, *"intended to be versioned in git"*, with two stated purposes:

> - auditing ("why did the agent do that?")
> - dataset generation (SFT/RL fine-tuning)

An entry is one event with a `kind` (`llm_call`, `tool_call`, `label`), and the fields to match: `--model`, `--prompt`, `--response`, `--error` for a model call; `--tool-name`, `--exit-code` for a tool call; `--issue-id` to tie it to the work. `bd audit label <entry-id> --label good --reason "…"` appends a *new* entry referencing the parent — labels never mutate history.

**The second purpose is unique in this wiki.** No other tool here captures its own execution traces as training data. Every framework's answer to "learn from what happened" is prose for a human or a later agent to read — [[ce-compound]]'s solution docs, [[gstack-learn]]'s corpus, [[bmad-retrospective]]'s action items. Beads records structured, labelled prompt/response pairs keyed to the work item they were produced for, which is a fine-tuning dataset accumulating as a side effect of ordinary work. That is [[pattern-knowledge-compounding]] pointed at the *model* rather than at the agent's context, and it is the sort of thing only the state layer can do, because only the state layer is still there afterwards.

Its [[pattern-evidence-before-claims]] edge is the audit half: a claim an agent made is checkable against the recorded call that produced it. Beads records; it does not verify — contrast [[bernstein]]'s janitor, which *"does not trust agent claims—verifies them"*. Commits carry a matching `Agent-Signature:` trailer with model and reasoning metadata (or `unknown-model` when unavailable).

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-comment]] — the events journal's `actor` column, the same attribution question inside the database.
- [[bernstein]] — verification rather than recording.
- [[pattern-knowledge-compounding]] — compounding aimed at context; this aims at weights.
