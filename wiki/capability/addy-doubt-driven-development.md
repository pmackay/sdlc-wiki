---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-adversarial-review]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Doubt-Driven Development

Materialize a fresh-context reviewer — biased to **disprove, not approve** — before any
non-trivial decision stands. The cycle is **CLAIM → EXTRACT → DOUBT → RECONCILE → STOP**: name
the claim and why it matters, hand the reviewer only the artifact plus contract (never the claim,
which would bias it toward agreement), prompt adversarially for issues, classify each finding,
and stop after trivial findings or three cycles. In interactive use it always offers
user-authorized cross-model escalation (Gemini/Codex CLI) via a read-only sandbox.

It applies [[pattern-adversarial-review]] and [[pattern-fresh-context-subagents]]. Distinctively,
it runs **in-flight during the build** where course-correction is cheap — review-flavored, but
not the post-hoc PR gate. It implements [[stage-implement]].

## See Also
- [[pattern-adversarial-review]] — the underlying disprove-don't-approve pattern.
- [[addy-code-review]] — the post-hoc verdict this deliberately precedes.
- [[stage-implement]] — the canonical stage this implements.
