---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]", "[[pattern-idempotent-operations]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl schedule

Run a registry plugin against a repository on a cron: `schedule create/list/view/runs/pause/resume/update/trigger/delete`. Timezone-aware, able to copy the configuration of an existing launch run, and able to pin the agent and model.

The documented example is the whole idea in one line: *"Run a registry plugin against a repo every Friday at 09:00 UTC."* A capability is no longer something a developer invokes — it is a **scheduled job with an owner, a cadence, and a run history**.

This is the second runtime-adjacent surface, and the more consequential of the two. [[tessl-launch]] runs one thing on demand; a schedule runs it **unattended, repeatedly, with nobody watching** — which is [[pattern-autonomous-loop]] provided by the supply layer. Pause, resume, and manual trigger are the operational controls that come with admitting you run a fleet of recurring jobs.

It is filed as prose on [[tessl]] rather than as a runtime node for the same reason as launch: the unit scheduled is a registry plugin, and there is no coordination between runs. Against the [execution layer](../runtime/index.md)'s trigger taxonomy this is the *scheduled* cell only — no event triggers, no goal-driven autonomy, no queue. The closest paged comparison is [[gh-aw]], which also puts agent runs on a cron (including deliberately-scattered fuzzy schedules) but wraps them in compiled authorization, budget ceilings, and a threat-verdict gate that this does not have.

**This is the command to watch for the layer's boundary.** A supply platform that distributes capabilities, measures them, governs who may install them, *and* runs them on a schedule is most of a [software factory](../topic/topic-software-factory.md) — which is exactly where Tessl says it is going.

## See Also
- [[tessl-launch]] — the on-demand form of the same execution surface.
- [[gh-aw]] — scheduled agent runs with the authorization layer this lacks.
- [[topic-software-factory]] — the destination Tessl names for itself.
- [[pattern-autonomous-loop]] — the technique, supplied from the registry layer.
