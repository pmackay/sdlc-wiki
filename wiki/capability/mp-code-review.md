---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-parallel-persona-review]]", "[[pattern-adversarial-review]]"]
equivalent_to: ["[[addy-code-review]]", "[[bmad-code-review]]", "[[ce-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]", "[[builder-factory-review-prs]]"]
docs_url: "https://www.aihero.dev/skills-code-review"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); Builder.io — BuilderIO/skills (2026); v1.3.0 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# code-review

`/code-review` — a model-invoked engineering skill that reviews the diff since a fixed point (commit, branch, tag, or merge-base) along **two axes**, run as **parallel sub-agents** so neither pollutes the other's context, then aggregated:

- **Standards** — does the code follow the repo's documented coding standards, *plus* an always-on **Fowler smell baseline** (~12 curated "Bad Smells in Code": Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest). Two binding rules keep it safe: a documented repo standard overrides the baseline, and every smell is a judgement call, never a hard violation.
- **Spec** — does the code faithfully implement the originating issue / PRD / spec (found via commit refs, a passed path, or a `docs/`/`specs/` file)?

**New in v1.1 (2026-07-09)** — graduated from `in-progress/` (was `review`) into `engineering/`. The refactor stage of [[mp-tdd]] moved here (review owns refactoring now). It is the quality gate [[mp-implement]] runs before committing.

MP's member of the cross-framework **code-review** cluster ([[pattern-adversarial-review]] smell- hunting via [[pattern-parallel-persona-review]] sub-agents) — with [[addy-code-review]], [[bmad-code-review]], [[ce-code-review]], and [[gstack-review]] (now a **five-framework** cluster). Its distinctive shape is the explicit **Standards ∥ Spec** two-axis split.

> **v1.2.3–v1.3.0.** Harness-neutral sub-agent dispatch: Claude Code's tool and agent-type names were dropped so the step works on Codex too (v1.2.3). The spec axis now talks about "issue/spec" rather than "issue/PRD" (v1.2.0). In the v1.3.0 main flow it runs once per ticket under [[mp-implement]], or once over the whole integration branch under [[mp-implement-spec]]. [[mp-retro]] then tunes the coding standards it enforces, turning mechanical findings into deterministic checks and leaving `CODING_STANDARDS.md` for judgement calls.

## See Also
- [[mp-implement]] — invokes this to close out a build.
- [[mp-improve-codebase-architecture]] — MP's other [[stage-review]] skill (architecture audit, not diff review).
- [[addy-code-review]] · [[bmad-code-review]] · [[ce-code-review]] · [[gstack-review]] — code-review-cluster counterparts.
- [[stage-review]] — the canonical stage this implements.
- [[mp-retro]] — tunes the standards this enforces (v1.3.0).
