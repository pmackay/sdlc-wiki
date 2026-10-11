---
type: artifact
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# Artifact: Decision log

A **single append-only TSV, one row per decision**, kept while an agent works unattended so a human who stepped away can audit what happened and decide whether to trust the result.

Six columns: `ts` (ISO8601), `phase`, `decision` (what was chosen, one line), `why` (the reason in plain words, *not* a jargon tag), `evidence` (a commit SHA, PR number, `file:line`, or an artifact, trace, or screenshot path — **never a paragraph**), and `result` (the outcome or predicate state: `tests green`, `reverted`, `pixel-diff 0`, `INCONCLUSIVE`, `open`).

```
ts	phase	decision	why	evidence	result
2026-05-24T09:40:00Z	harness	took screenshots of the old version before changing anything	so we can compare old against new and catch any visual change	scripts/snapshot.sh, baseline/	saved 120 reference screenshots
2026-05-24T11:15:00Z	widget	moved the widget styles over without changing how it looks	keep the change small and the result identical	commit 7c21e0a, pixel-diff 0	looks identical, tests pass
2026-05-24T12:30:00Z	widget	threw out a helper's work because its screenshots were blank	checked the real files instead of trusting its summary	worktree reset	reverted, tightened the instructions for next time
```

**Its distinguishing property among this wiki's artifacts is its reader.** [[artifact-handoff-doc]] and the state a work [[beads|store]] holds exist so the *next agent* can continue; a retrospective ([[artifact-retrospective]]) and a solution corpus ([[artifact-solution-doc]]) exist so *future work* starts ahead. A decision log exists so a **human who was not watching can reconstruct the reasoning after the fact** and locate the point where trust should stop. That is why evidence is a pointer rather than prose, why rows are single-line, and why the third example row above is a *reverted* decision — the log's value is concentrated in the moments the run went wrong.

Three rules govern it. **Append-only**: a wrong call gets a new row that supersedes it; history is never edited or deleted. **Decision points and checkpoints only** — a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed — not every action. And **prefer evidence produced by committed scripts** over hand-made one-offs ([[pattern-tooling-leverage]]).

**Where it lives is a deliberate default.** It is a working artifact at `decisions.tsv` (or `.audit/<task-slug>.tsv` when several efforts run at once) and is left out of git, committed only when the work is ambitious enough that a reviewer needs the trail to trust the result. The trail is always kept; it becomes a repository artifact only when it has a reader.

## Produced by (backlinks)

pstack:

- [[pstack-show-me-your-work]] — owns the format, ships the `log.sh` helper, and defines the commit policy.
- [[pstack-figure-it-out]] — Phase D weaves a row in as each unit lands rather than saving the trail for the end.

builder-skills:

- [[builder-plow-ahead]] — the *Key decisions* section of the final recap: assumptions and choices made without stopping, with short reasons, for a user who was away. Kept as a lightweight log during the run, and deliberately *not* committed to the repo unless the task needs it.

## See Also
- [[artifact-handoff-doc]] — the agent-facing counterpart; that one is read by the next agent, this one by a human.
- [[artifact-retrospective]] — the after-the-fact synthesis; the decision log is the contemporaneous record.
- [[pattern-evidence-before-claims]] · [[pattern-tooling-leverage]] — the disciplines the evidence column enforces.
