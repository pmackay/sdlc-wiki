---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-source-grounding]]", "[[pattern-trunk-based-development]]"]
equivalent_to: []
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# resolving-merge-conflicts

`/resolving-merge-conflicts` — a model-invoked engineering skill for resolving an **in-progress git merge/rebase conflict**. It reads the current merge/rebase state, finds the **primary sources** for each conflicting change (commit messages, PRs, original issues) to understand each side's intent, then resolves every hunk — preserving both intents where possible, or picking the one matching the merge's stated goal and noting the trade-off (never inventing new behaviour, never `--abort`). It runs the project's automated checks (typecheck → tests → format), fixes anything the merge broke, and finishes the merge/rebase with a commit.

**New in v1.1 (2026-07-09).** An integration-time implementation skill: understanding change intent from primary sources ([[pattern-source-grounding]]) to keep a shared trunk mergeable ([[pattern-trunk-based-development]]). No cross-framework counterpart — the other frameworks handle integration inside their ship/execute steps rather than as a dedicated conflict-resolution skill.

## See Also
- [[mp-implement]] · [[mp-tdd]] — the build skills whose work this integrates.
- [[stage-implement]] — the canonical stage this implements.
