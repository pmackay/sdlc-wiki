---
type: pattern
sources: "Warp — Warp Factories docs (2026); Zach Lloyd — 'Introducing Warp Factories' (2026-08-18); github/gh-aw (2026); disler/super-simple-software-factory (2026); Builder.io — BuilderIO/skills (2026); Dru Knox — 'Context-Driven Factories' (Tessl blog, 2026-09-15); Tessl docs — Schedules (2026)"
raw: ["../../raw/runtime/2026-10-24-warp-factories.md", "../../raw/runtime/2026-09-01-gh-aw.md", "../../raw/tessl/2026-09-15-context-driven-factories.md"]
updated: 2026-10-24
---

# Pattern: Factory as code (the agent system's configuration is reviewed, validated files)

Keep **everything that defines how the agents run** — which agents exist, their prompts, skills, models and harnesses, triggers, compute, credentials-by-reference, and evaluation rubrics — as a **versioned file tree** that is schema-validated and changed only through pull-request review, then applied to the running system as one unit. The factory's behavior at any point is whatever the files on the production branch say.

> In Warp, factories are defined as version-controlled code. This has the same benefits as other infrastructure-as-code platforms like Terraform: the factory is completely specified at any point in time. You can roll back or forward to factory versions, canary them, test them, and so on. In an agent-first world it also enables agentic changes to the factory, which is a huge driver of factory self-improvement. — [[warp-factories]] launch post

This is infrastructure-as-code applied to the agent layer, and most of its value is the ordinary IaC value: one reviewable source of truth, diffs instead of dashboard clicks, rollback by revert, and the same review rules as the product code. **Two things make it more than that in agent work.**

- **The configuration is mostly prose.** An agent's prompt and its skills are the parts most likely to change and the parts with the largest effect on output. Under this pattern a one-line edit to the review agent's instructions gets the same pull request, check, and approver as a change to its model or its secrets, rather than being edited live in a settings page nobody reviews.
- **Agents can propose changes to it.** Once the configuration is files, an agent can open a pull request against it like any other code. That turns *improving the factory* into ordinary factory work, which is what makes evaluation-driven self-improvement possible without giving the factory authority over itself: [[warp-factories]]' self-improvement runs edit `agents/*/agent.md` and `skills/*/SKILL.md` through the same review gate as a human would. It is the configuration-side precondition for [[pattern-knowledge-compounding]] aimed at the factory rather than the codebase.

**What separates a strong instance from a weak one** is the validation step, not the file format. A configuration file the agent reads as a convention protects nothing; one with a published schema that rejects unknown keys, a pull-request check, and atomic apply-or-keep-the-last-valid-version is a control. The evidence spans that range (see below).

**How it differs from its neighbours.** [[pattern-living-specification]] and [[pattern-project-constitution]] version the *product's* intent: what the software should do, and the principles it must respect. This pattern versions the *machine that builds the software*. [[pattern-capability-evals]] tests one capability's effect; factory-as-code is what lets a tested change to a capability or an agent configuration be shipped, reviewed, and rolled back.

## Applied by (backlinks)

- [[tessl-schedule]] — schedules declared in `tessl.json`, checked by `tessl schedule validate`, applied as a whole block from the default branch, and read-only everywhere else: *"To change it, change the file and push."*

## Enabled by (infrastructure)

- [[warp-factories]] (platform) — the signature instance. A factory is *"a versioned tree of YAML and Markdown files rooted at `factory.yaml`"* covering agents, automations, runners, model routers, scorers, benchmarks, skills, and webhooks, with paths as identities (`agents/reviewer/agent.md` defines `reviewer`). The definition lives in a Warp-managed repository or the team's own GitHub repository, where *"merges to the production branch (`main` by default) update the factory."* Validation is layered: published JSON Schemas that *"reject unknown keys"*, a `warp/factory-config` pull-request check, a local validator script, and validator tools for coding agents. *"Warp applies the definition as one unit and keeps the last valid definition if validation fails."* Factory roles separate *proposing* a change (any User) from editing (Editor) and force-merging a blocked change (Admin), and self-improvement runs propose edits to the definition as pull requests.
- [[gh-aw]] (platform) — the compiled instance. Each workflow is a Markdown file (YAML frontmatter for triggers, permissions, and allowed writes; prose for the agent) that `gh aw compile` turns into a hardened `.lock.yml`, refusing to emit one that fails schema validation, expression allowlisting, action SHA pinning, or the `actionlint`/`zizmor`/`poutine` scanners, so the policy a reviewer approves is the compiled job graph itself. `gh aw update` three-way-merges upstream workflow changes against local edits through the `source:` field, and `gh aw deploy` rolls workflows out to many repositories by pull request.

**Related instances, recorded as prose rather than edges:**

- [[sssf]] — the control plane itself is Python stamped into the repository by a skill and meant to be edited there, with the agent roster and per-phase models declared beside it in `sssf.config.yaml`. Versioned and reviewable, but there is no schema or apply step: the code is the configuration.
- [[builder-skills]] — the Factory's [[artifact-autonomy-policy]] (`.agent-factory/config.yaml`) is a committed file that sets every autonomy policy, and it describes itself as *"an agent-readable convention, not a validated schema."* The unvalidated end of the range: versioned and diffable, but enforced only by the agent choosing to read it.

## Supplied by (registry)

- [[tessl]] — the pattern taken furthest toward prose. Tessl's *context-driven factory* puts the workflows themselves in versioned plugins (*"Read a plugin and you know how the factory works. Change a plugin and you have changed the factory"*), pins standards owned by other teams as semver-ranged registry dependencies in `tessl.json`, and binds entry skills to schedules there too. Its argument for doing so is the one this page makes about agents proposing changes: *"Plain context files are easy for an agent to read and change safely, so the self-improvement step is tractable."* The validation is strongest on the schedule surface ([[tessl-schedule]]: a validator, atomic apply, and *"an error in the file is always safe"*); the event triggers and dependencies shown in its factory post are not yet documented. Its *"context as code"* premise applies the same discipline to the capabilities themselves.

## See Also

- [[pattern-knowledge-compounding]] — the loop this pattern lets an agent close on the factory itself, under review.
- [[pattern-capability-evals]] — the test step a definition change can pass through before it merges.
- [[pattern-deterministic-gates]] — the class of check that a schema validator and a configuration PR check belong to.
- [[topic-software-factory]] — the anatomy whose control plane this pattern makes reviewable.
- [[topic-compounding-loop]] — the steering loop that a reviewable, agent-editable configuration makes possible to automate.
