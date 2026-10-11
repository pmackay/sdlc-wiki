---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-eval-suite]]"]
applies: ["[[pattern-capability-evals]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl scenario

Generate the tasks a capability is graded against: `scenario generate`, `list`, `view`, `download` → [[artifact-eval-suite]]. Each scenario pairs a **task** with a **rubric of weighted criteria**, and lands in the bundle's `evals/` directory, one scenario per subdirectory.

Three sources, and the second and third are the interesting ones: from the **plugin** itself (what does this skill claim to do?), from **two commits** (what changed?), and from **real PRs** — generating the assessment tasks from work your team actually did rather than from invented examples.

**Generated scenarios pass a server-side feasibility check before being saved.** *"Only scenarios that pass are saved, so the generator gives you tests that actually exercise the skill rather than filler."* A quality gate on the tests themselves is unusual and is what stops the suite from padding to hit a requested count — a narrowly scoped skill legitimately returns fewer scenarios than asked for.

Scenarios can equally be hand-written, and the docs are careful that the generator is a convenience rather than the mechanism. What matters is that the suite lives **with** the capability, so it becomes a regression test any later editor can re-run.

The documentation's sharpest warning is operational and worth preserving: `--strategy replace` clears the plugin's `evals/` wherever you invoke it from, and the default `merge` overwrites same-named scenarios — and since names are canonical (`scenario-1/`, `scenario-2/`), a re-download silently replaces hand-edited scenarios.

## See Also
- [[tessl-eval]] — runs what this generates.
- [[artifact-eval-suite]] — the artifact.
- [[pattern-capability-evals]] — the technique.
