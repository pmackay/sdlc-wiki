---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]", "[[pattern-idempotent-operations]]", "[[pattern-factory-as-code]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026); Tessl docs — Automations and Schedules (captured 2026-10-24); Dru Knox — 'Context-Driven Factories' (Tessl blog, 2026-09-15)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md", "../../raw/tessl/2026-09-15-context-driven-factories.md"]
updated: 2026-10-24
---

# tessl schedule

Run a plugin against a repository on a cron. *"No CI setup, no GitHub Actions config. Declare a schedule in your tessl.json, push to your default branch, and Tessl runs it for you."* Each firing starts a cloud run and records its result in the schedule's run history.

**The primary form is a file.** A `schedules` block in the repo's `tessl.json` maps a kebab-case name to an `action` (the plugin to run, as a registry ref or a repo-local `file:` skill, plus an optional environment, base branch, workdir, agent, model, effort, inputs, and per-schedule `instructions`) and a timing (`cron`, readable shorthand such as `weekly on friday at 09:00`, or a structured object; five-minute minimum; IANA timezone). An `actions` block declares an action once so several schedules can share it and one run history. The same plugin can serve several jobs, steered differently by `instructions`.

**The file is the source of truth, and an error in it is always safe.** `tessl schedule validate` checks the blocks locally (and, when signed in, that the plugin, environment, agent, model, and workspace limits will resolve) and exits non-zero, so it runs as a CI check. On push to the default branch Tessl applies the whole `schedules` block or none of it: *"Tessl never deletes a schedule because it could not understand your file. Deletion only ever follows from a file it read cleanly."* When repo-defined schedules are enabled, the web app and CLI show them read-only, so the only way to change one is to change the file. Creating a schedule directly with `schedule create` or the web app remains available as *"the older path and is not version-controlled."* This is [[pattern-factory-as-code]] for the automation surface.

**Run semantics.** A run without an environment gets a read-only GitHub token and cannot open PRs. If the previous run from the same schedule is still active, *"Tessl skips a tick… There is no queue: a skipped tick does not run later."* Supported agents are Claude Code (default), Cursor, Codex, Gemini, and the Tessl Agent.

**In Tessl's factory vocabulary, a schedule is what turns a skill into a loop**: *"A schedules entry in tessl.json turns a plugin into a loop."* The documented examples are the "continuous" jobs other factories run as standing automations: a docs audit, a weekly changelog, a flaky-test monitor, a release-readiness check, and a **review miner** that reads the last 50 code reviews and proposes *"a lint rule, an automated check, or a documented convention"* for feedback that keeps recurring. That last one is a learn-stage loop aimed at a computational control, the move [[topic-compounding-loop]] lists as missing; it still proposes rather than lands the check.

This is the second runtime-adjacent surface, and the more consequential of the two. [[tessl-launch]] runs one thing on demand; a schedule runs it **unattended, repeatedly, with nobody watching**, which is [[pattern-autonomous-loop]] provided by the supply layer.

It is filed as a capability of [[tessl]] rather than as a runtime node: the unit scheduled is a plugin, and there is no coordination between runs (no queue, no fan-out, no steering). Against the [execution layer](../runtime/index.md)'s trigger taxonomy the documented surface is the *scheduled* cell. Event triggers appear in Tessl's [context-driven factories](../registry/tessl.md#the-factory-thesis-context-driven-factories) post (a `triggers` block binding `linear:issue.delegated` or `github:pull_request.opened` to a skill) but not yet in the docs. The closest paged comparisons are [[gh-aw]], which also puts agent runs on a cron but wraps them in compiled authorization, budget ceilings, and a threat-verdict gate, and [[warp-factories]], whose schedule automations sit beside event triggers in a reviewed definition.

**This is the command to watch for the layer's boundary.** A supply platform that distributes capabilities, measures them, governs who may install them, *and* runs them from repo-defined schedules is most of a [software factory](../topic/topic-software-factory.md), which is where Tessl says it is going. The boundary was re-checked on 2026-10-24 and held; see [the layer boundary](../registry/tessl.md#the-layer-boundary-honestly).

## See Also
- [[tessl-launch]] — the on-demand form of the same execution surface.
- [[gh-aw]] — scheduled agent runs with the authorization layer this lacks.
- [[warp-factories]] — schedules as one trigger kind among many, in a reviewed factory definition.
- [[topic-software-factory]] — the destination Tessl names for itself.
- [[pattern-autonomous-loop]] — the technique, supplied from the registry layer.
- [[pattern-factory-as-code]] — the configuration discipline the `tessl.json` form follows.

## Version history

### Docs as of 2026-10-24 (ingested 2026-10-24)
- Schedules are declared in `tessl.json` (`schedules` and `actions` blocks), validated by `tessl schedule validate`, applied atomically from the default branch, and read-only in the web app and CLI when repo-defined schedules are enabled. CLI and web-app creation became the older, unversioned path.
- Added: skip-not-queue tick behavior, read-only token without an environment, readable cron shorthand, `effort`, and the example schedules (including the review miner).

### Initial ingest (2026-09-12)
- Documented at CLI v0.108.0 as `schedule create/list/view/runs/pause/resume/update/trigger/delete`: timezone-aware, able to copy an existing launch run's configuration, able to pin agent and model.
