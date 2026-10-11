---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-cross-model-review]]", "[[pattern-evidence-before-claims]]", "[[pattern-adversarial-review]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /agent-watchdog

Audit another agent's work, given a Codex session ID, a Claude Code transcript, a PR, a branch, a CI run, or a pasted summary. The skill describes itself as *"a reviewer with a pager who is also a second investigator."* It has four modes, inferred from the request: watch only, audit, audit and fix, and compare. *"If authority is unclear, default to audit-only."*

**The idea worth taking: investigate independently, then diff.** *"Anchoring is the failure mode: reading their work first and nodding along."* The watchdog forms its own hypotheses, ideally before reading the other agent's conclusions, and uses the wait while that agent is still running to pre-map the problem. It prioritizes evidence the watched agent probably did not look at: production ledgers, session replays, error trackers, deploy state, and other worktrees. It then diffs the two investigations (what each found that the other missed, where the approaches diverge, and *"any product or design fork they took silently"*) and turns the difference into concrete add-on directions to pass along.

**Relay sparingly.** A mid-run agent *"re-plans around every note it receives"*, so the watchdog interrupts only for a defect in code being touched now, a correction, or an answer the agent is blocked on. Everything else waits for a checkpoint and goes as one batch. *"Never hand a mid-run agent an unranked list… an unranked backlog reliably produces several half-finished surfaces instead of a few complete ones."* It also reports what it verified as correct, *"so they stop re-litigating settled ground."*

It classifies each issue as a gap, a bug, a verification miss, scope drift, or no issue. [[stage-review]], with the reviewer set up as a separate agent (often a different vendor) instead of a subagent of the author: [[pattern-cross-model-review]] at the level of whole sessions.

## See Also
- [[builder-plan-arbiter]] — the same cross-agent stance, applied to plans instead of finished work.
- [[gstack-codex]] — a second opinion from another model; this goes further and reconstructs the whole run.
- [[stage-review]] — the canonical stage this implements.
