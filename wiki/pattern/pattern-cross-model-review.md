---
type: pattern
sources: "gstack — Garry Tan (2026); EveryInc/compound-engineering-plugin (2026); sipyourdrink-ltd/bernstein (2026)"
updated: 2026-08-31
---

# Pattern: Cross-model review (an independent second opinion from another model)

Run a review of the same work through a **different model or vendor**, then surface where the two **agree vs disagree** — overlapping findings are high-confidence, unique findings are each model's blind-spot catch. Independence is the point: a second instance of the *same* model shares its failure modes, so a genuinely different model (a different vendor entirely, ideally) catches errors the first cannot see, and disagreement is signal rather than noise.

Crucially, cross-model agreement is **signal, not a mandate** — gstack's *User Sovereignty* ethos is explicit that "two AI models agreeing on a change is a strong signal, not a mandate; the user decides." The pattern feeds a generation-verification loop, it does not automate the decision.

## Why it's distinctive

Distinct from [[pattern-adversarial-review]] (one reviewer *tasked* to find fault) and [[pattern-parallel-persona-review]] (many *personas* on the same model): here the diversity comes from the **model itself**. Two frameworks realize it — gstack ([[gstack-codex]] runs an OpenAI Codex review against Claude's [[gstack-review]] and reports overlap vs unique findings; also the quality gate behind [[gstack-spec]]) and Compound Engineering (whose [[ce-code-review]] includes an adversarial + cross-model pass). gstack's [[gstack-benchmark-models]] applies the same different-models-side-by-side idea to *evaluating skills* rather than reviewing code.

## Applied by (backlinks)

gstack:

- [[gstack-codex]] — OpenAI Codex second opinion; cross-model overlap/unique analysis vs [[gstack-review]].
- [[gstack-spec]] — uses the Codex cross-model gate to block low-quality specs.
- [[gstack-benchmark-models]] — the model-evaluation cousin (same prompt across Claude/GPT/Gemini).

Compound Engineering:

- [[ce-code-review]] — adversarial + cross-model review pass.

## Enabled by (infrastructure)

- [[bernstein]] (platform) — the **review gate** makes a distinct-model reviewer a *configuration* property rather than a convention: `ModelSelection` is one of `SameModelOk` / `DifferentModelPreferred` / `DifferentModelRequired`, and the last raises `EvalGateConfigError` when it cannot be satisfied. The reviewer sees only `(spec, diff, test_output)` and returns a three-valued structured verdict — pass · fail · questions — that drives auto-merge. An optional **cross-model verifier** additionally runs the diff past a second provider's model for A/B review (shipped, disabled by default). The runtime's rationale matches this pattern's: *"Same-model self-critique is empirically weak at catching the implementer's own blind spots."*

## See Also
- [[pattern-adversarial-review]] — fault-finding by mandate (same model); often combined with this.
- [[pattern-parallel-persona-review]] — diversity by persona rather than by model.
- [[pattern-deterministic-gates]] — the cheap, un-gameable checks that run first, so this inferential sensor is spent only on judgment.
- [[stage-review]] — the stage this reinforces (Review side).
- [[bernstein]] — the runtime that makes a different-model reviewer a configuration requirement (`DifferentModelRequired`) rather than a convention.
