---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-parallel-persona-review]]", "[[pattern-adversarial-review]]"]
equivalent_to: ["[[addy-code-review]]", "[[bmad-code-review]]", "[[ce-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]"]
docs_url: "https://www.aihero.dev/skills-code-review"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# code-review

`/code-review` — a model-invoked engineering skill that reviews the diff since a fixed point (commit, branch, tag, or merge-base) along **two axes**, run as **parallel sub-agents** so neither pollutes the other's context, then aggregated:

- **Standards** — does the code follow the repo's documented coding standards, *plus* an always-on **Fowler smell baseline** (~12 curated "Bad Smells in Code": Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest). Two binding rules keep it safe: a documented repo standard overrides the baseline, and every smell is a judgement call, never a hard violation.
- **Spec** — does the code faithfully implement the originating issue / PRD / spec (found via commit refs, a passed path, or a `docs/`/`specs/` file)?

**New in v1.1 (2026-07-09)** — graduated from `in-progress/` (was `review`) into `engineering/`. The refactor stage of [[mp-tdd]] moved here (review owns refactoring now). It is the quality gate [[mp-implement]] runs before committing.

MP's member of the cross-framework **code-review** cluster ([[pattern-adversarial-review]] smell- hunting via [[pattern-parallel-persona-review]] sub-agents) — with [[addy-code-review]], [[bmad-code-review]], [[ce-code-review]], and [[gstack-review]] (now a **five-framework** cluster). Its distinctive shape is the explicit **Standards ∥ Spec** two-axis split.

## See Also
- [[mp-implement]] — invokes this to close out a build.
- [[mp-improve-codebase-architecture]] — MP's other [[stage-review]] skill (architecture audit, not diff review).
- [[addy-code-review]] · [[bmad-code-review]] · [[ce-code-review]] · [[gstack-review]] — code-review-cluster counterparts.
- [[stage-review]] — the canonical stage this implements.
