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
- **Spec** — does the code faithfully implement the originating issue / spec (found via commit refs, a passed path, or a `docs/`/`specs/` file)?

The sub-agent dispatch is written harness-neutrally, so the step works on Codex as well as Claude Code. Refactoring belongs to this skill rather than to [[mp-tdd]].

In the main flow it is the quality gate after the build: once per ticket under [[mp-implement]], or once over the whole integration branch under [[mp-implement-spec]]. [[mp-retro]] then tunes the coding standards it enforces, turning mechanical findings into deterministic checks and leaving `CODING_STANDARDS.md` for judgement calls.

MP's member of the cross-framework **code-review** cluster ([[pattern-adversarial-review]] smell- hunting via [[pattern-parallel-persona-review]] sub-agents), with [[addy-code-review]], [[bmad-code-review]], [[ce-code-review]], and [[gstack-review]] (a **five-framework** cluster). Its distinctive shape is the explicit **Standards ∥ Spec** two-axis split.

## See Also
- [[mp-implement]] — invokes this to close out a build.
- [[mp-retro]] — tunes the standards this enforces.
- [[mp-improve-codebase-architecture]] — MP's other [[stage-review]] skill (architecture audit, not diff review).
- [[addy-code-review]] · [[bmad-code-review]] · [[ce-code-review]] · [[gstack-review]] — code-review-cluster counterparts.
- [[stage-review]] — the canonical stage this implements.

## Version history

### v1.3.0 (2026-10-04)
- Runs once per ticket under [[mp-implement]] or once over the integration branch under [[mp-implement-spec]]; [[mp-retro]] added downstream to tune its standards.

### v1.2.0 – v1.2.3 (2026-08-05 – 2026-08-06)
- The spec axis talks about "issue/spec" rather than "issue/PRD" (v1.2.0).
- Claude Code's tool and agent-type names dropped from the sub-agent dispatch, so it works on Codex too (v1.2.3).

### Added in v1.1.0 (2026-07-08; ingested 2026-07-09)
- Graduated from `in-progress/` (was `review`) into `engineering/`. The refactor stage of [[mp-tdd]] moved here, and it became the quality gate [[mp-implement]] runs before committing.
