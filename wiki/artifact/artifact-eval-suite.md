---
type: artifact
sources: "Tessl docs (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# Artifact: Eval suite

A directory of **scenarios that grade a capability**, versioned alongside the capability itself. Each scenario pairs a **task** an agent is asked to perform with a **rubric of weighted criteria** used to score the result. Running the suite means running the task twice — once with the capability loaded and once without — and comparing ([[pattern-capability-evals]]).

In [[tessl]] it lives at `evals/` inside the bundle, one scenario per subdirectory, and can be generated or hand-written. Generated scenarios pass a server-side **feasibility check** before being saved, *"so the generator gives you tests that actually exercise the skill rather than filler"* — a quality gate on the tests themselves, which is unusual and worth recording.

**Its function is to make a shared skill corpus editable.** The failure mode it addresses is stated plainly by the product it comes from: *"You can't tell whether a skill actually improves agent output, so no one risks changing it."* Once the suite exists, *"anyone who changes it later can re-run the same scenarios and confirm it still behaves as expected"* — the same role a regression test plays for code, for a thing that is not code.

**It is a regression suite for prose**, which is what makes it new. Every other test artifact in this wiki grades the software the agent produced. This one grades the instructions that produced it, and it is the durable half of the instrument [[topic-ai-native-sdlc]] recorded as shipped by nobody: 20–50 real tasks re-run whenever the configuration changes, with the score enforced at merge.

## Produced by (backlinks)

Tessl:

- [[tessl-scenario]] — generates scenarios from a plugin, from two commits, or from real PRs; feasibility-checks them server-side; downloads them into the bundle's `evals/`.
- [[tessl-eval]] — runs the suite, scores the with/without difference, and can lint the scenarios themselves.

## See Also
- [[pattern-capability-evals]] — the technique this artifact serves.
- [[artifact-capability-bundle]] — where the suite lives and what it grades.
- [[artifact-review-report]] — the cheap structural sibling: *is it well written?* rather than *does it work?*
- [[artifact-uat-md]] — the product-side acceptance artifact; this is its configuration-side counterpart.
