---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-source-grounding]]", "[[pattern-trunk-based-development]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-resolving-merge-conflicts"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); removed in v1.3.0 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md", "../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# resolving-merge-conflicts

> **Removed in v1.3.0 (2026-10-04).** "It's no longer needed, and nothing replaces it: the agent works through an in-progress merge or rebase conflict without a dedicated skill." It left the Claude Code plugin, the README, and the [[mp-ask-matt]] router; its docs page stays up, marked archived. This page is kept as a historical record so existing links still resolve. Its `implements:` edge is retained for the record, and [[stage-implement]] lists it as removed.

`/resolving-merge-conflicts` was a model-invoked engineering skill for resolving an **in-progress git merge/rebase conflict**. It read the current merge/rebase state and found the **primary sources** for each conflicting change (commit messages, PRs, original issues) to understand each side's intent. It then resolved every hunk, preserving both intents where possible or picking the one that matched the merge's stated goal and noting the trade-off. It never invented new behaviour and never ran `--abort`. Finally it ran the project's automated checks (typecheck → tests → format), fixed anything the merge broke, and finished the merge/rebase with a commit.

It was an integration-time implementation skill: understanding change intent from primary sources ([[pattern-source-grounding]]) to keep a shared trunk mergeable ([[pattern-trunk-based-development]]). It had no cross-framework counterpart. The retirement itself is evidence: integration conflict handling was judged to be default agent competence, not a discipline worth a skill. Its nearest successor in spirit is [[mp-implement-spec]], which avoids most conflicts by design (each implementer merges the integration tip into its own branch first, so every merge is a fast-forward).

## See Also
- [[mp-implement]] · [[mp-implement-spec]] — the build skills whose work this integrated.
- [[stage-implement]] — the canonical stage this implemented.

## Version history
- **v1.3.0 (2026-10-04):** removed from the repo, the Claude Code plugin, the README, and the [[mp-ask-matt]] router; nothing replaces it. Its docs page stays up, marked archived.
- **v1.2.0 (2026-08-05):** added to the [[mp-ask-matt]] router, from which it had been missing.
- **v1.1.0 (2026-07-08; ingested 2026-07-09):** added as a model-invoked engineering skill.
