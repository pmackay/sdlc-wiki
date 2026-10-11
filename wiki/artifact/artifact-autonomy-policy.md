---
type: artifact
sources: "Builder.io — BuilderIO/skills, docs/factory/configuration.md (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---

# Artifact: Autonomy policy

A durable, per-project document that states **which external actions an agent may take unattended, and under what conditions**. It is read by every automated workflow before any write. The documented instance is the Factory's `.agent-factory/config.yaml` in [[builder-skills]].

```yaml
workflows:
  collect:
    implement:
      mode: criteria
      allow: [verified defects in owned code]
      stop: [security-sensitive changes, unclear product intent]
    reply:
      mode: criteria
      require: [one missing detail blocks triage or verification]
    close:
      mode: never
  pr-babysitting:
    approve: { mode: never }
    merge:   { mode: never }
    soak: 10 minutes
```

It has four parts. **Scope**: the `repositories` and `sources` the workflows may read, each with an exact channel, project, or repo boundary. **Per-action policies**: separate `implement` / `reply` / `close` / `approve` / `merge` / `publish` / `notify` entries, each `never`, `manual`, `criteria` (with `allow`/`stop` lists), or a named proof point (`after-fix`, `after-merge`). **Schedules and isolation**: requested cadences and the worktree mode (`fresh-per-run` from `origin/main`). **Prompt overlays**: `skill_prompts.<skill>` text that adds project guidance and cannot grant permission.

**Three properties make it distinct from its neighbours.**

- **It governs authority, not design or style.** [[artifact-constitution]] holds principles a plan must satisfy, and [[artifact-standards]] holds conventions the code must follow. This document says what the agent may *do* to the outside world: reply to a customer, approve a PR, merge, deploy, close an issue. It is the document form of [[pattern-action-gating]].
- **It is a convention, not a schema.** *"The config is an agent-readable convention, not a validated schema. Unknown fields do not install connectors or create jobs."* The agent reads it as policy text, so nothing checks it mechanically. That is why the Factory insists on reading back every host automation the policy asks for.
- **It must not hold secrets or customer data.** It names connections and opaque references only. *"Never put tokens, passwords, private URLs, or copied customer records in it."*

## Produced by (backlinks)

builder-skills:

- [[builder-factory]] writes and maintains it interactively, preserving existing choices and asking about missing ones.

Read (not produced) by every other Factory module: [[builder-factory-collect]], [[builder-factory-lookback]], [[builder-factory-human-digest]], [[builder-factory-review-prs]], [[builder-factory-babysit-pr]], [[builder-factory-ship]], [[builder-factory-watchdog]], [[builder-factory-recover]].

## See Also
- [[pattern-action-gating]] — the pattern this document configures.
- [[artifact-constitution]] · [[artifact-standards]] — the principle and convention documents it is easily confused with.
- [[gh-aw]] — the runtime equivalent, where workflow frontmatter declares permissions and safe outputs that are compiled into CI rather than read as prose.
