---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-worktree-isolation]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl launch

Run a capability rather than merely distribute it: `tessl launch <agent>` starts a coding agent (`tessl launch claude`, `tessl launch cursor`), and `tessl launch skill` executes an installed skill — locally, interactively through a harness, or **in the cloud against a repository**, with `launch list`, `view`, and `logs` over the runs.

**This is the clearest runtime-adjacent surface in the [supply layer](../registry/index.md)**, and it is recorded as prose on the [[tessl]] page rather than treated as a second node, under the [harness/runtime boundary rule](../CONVENTIONS.md#the-harness-layer). A cloud launch takes a registry plugin, a repository, and an environment, and runs the whole thing somewhere else — which is, by the [execution layer](../runtime/index.md)'s own definition, what a runtime does.

What keeps it filed here is direction of service. Launch exists so a **registry plugin** can be run: it takes its input from the index, it is how [[tessl-eval]] exercises a skill against a real codebase, and it has no orchestration surface of its own — no fan-out, no steering, no queue, no isolation model to speak of beyond the sandbox. It runs one thing. Compare [[warren]] (dispatch and live steering), [[bernstein]] (fleet scheduling and gates), or [[gh-aw]] (compiled authorization): those own coordination policy, and this does not.

The `--launchable skill` schema is the part that hints where it goes next: a skill can declare **typed input and output JSON Schemas** and a cloud launch returns a structured result. A capability with a typed signature that runs in the cloud and returns data is a **function call**, not a prompt — and that is the shape an orchestrator consumes.

Watch this command. If it grows fan-out, queuing, or steering, [[tessl]] becomes a genuine two-layer product and its page needs splitting.

## See Also
- [[tessl-schedule]] — the same execution surface, on a cron.
- [[tessl-eval]] — the main consumer: launching a skill against real tasks is how impact gets measured.
- [[tessl-environment]] — supplies the secrets a sandboxed cloud run needs.
- [[warren]] · [[bernstein]] · [[gh-aw]] — the execution layer proper, for the contrast.
