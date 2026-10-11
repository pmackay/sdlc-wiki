---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-deterministic-gates]]", "[[pattern-wave-parallelism]]"]
equivalent_to: ["[[addy-code-review]]", "[[ce-code-review]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl change verify

Run configured **verifiers** — LLM judges, declared in a manifest and grouped — over changed files: `tessl change verify`, with `suggest-scopes` to propose the manifest and `lint` to check it.

Its contribution to the wiki is operational rather than conceptual. Everyone ships LLM-judge review; almost nobody documents **what it costs to run one at repository scale**, and this command's flag surface is a catalogue of exactly that problem:

- `--max-concurrency` (default 48) and `--max-calls` (default 300, *"refuse broad runs above this many judge calls"*) — a hard budget ceiling, with the refusal as the default behavior.
- `--sample` — a *deterministic* sample of verifier targets, so a large sweep is affordable and still reproducible.
- `--no-cache` / `--refresh-cache` — judge verdicts are cached, which is the only way a per-file LLM gate is viable on every push.
- `--dry-run` with `--show-files` — see what a run would do *without spending judge calls*.
- `--changed-files-mode introduced-only | whole-file` — gate on diff-attributable violations only, or judge each changed file in full. The choice between "don't make it worse" and "make it right", as a flag.
- `--strict-coverage`, `--fail-on-warn`, `--github` annotations, `--report-json`.

Cached, sampled, budget-capped, and dry-runnable is what [[pattern-deterministic-gates]] looks like when the "program" deciding the gate is a model that costs money per call. The wiki's existing gate instances read an exit code from a linter; this one has to *ration* its judge, and the rationing is the design.

`introduced-only` as the default is the quiet policy choice worth recording: a gate that judged whole files would fail every legacy file anyone touched, so the default makes the gate adoptable in an existing codebase at the price of never fixing what is already there.

## See Also
- [[tessl-change-risk]] — decides whether a human should look; this decides what fails.
- [[tessl-code-review]] — the PR-level review.
- [[pattern-deterministic-gates]] — the technique, here with a metered judge.
- [[stage-review]] — the canonical stage this implements.
