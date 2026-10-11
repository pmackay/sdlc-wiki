---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-eval-suite]]", "[[artifact-review-report]]"]
applies: ["[[pattern-capability-evals]]", "[[pattern-evidence-before-claims]]", "[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl eval

Run an agent on real tasks **twice — once without the context and once with it — and score the difference**: `eval run`, `list`, `view`, `retry`, `lint`. The anchor of [[pattern-capability-evals]], and the capability that closes an instrument [[topic-ai-native-sdlc]] had recorded as shipped by nobody.

> That difference is the skill's value: **proof it changes what the agent does, not just that it reads well.** Where a review checks the skill itself, an evaluation measures its effect.

The A/B is the mechanism. A skill can be well-structured, well-described, and clearly written and still change nothing about the output; without the baseline run you cannot tell, which is why [[tessl-review]] and this command are kept as separate instruments answering separate questions.

The flag surface shows how much the design has been thought through. You can pin the **agent and model** the eval runs under (so the result is attributable to the context rather than to a model change); run **only the with-context variant** when the baseline is already known; measure **context activation alone** — whether the skill even loads — without forcing use or scoring; test a **published** context, a **local directory**, a **glob of files**, or a local context **as it was at a specific commit**; and skip scenarios an LLM judge flags as misleading. Runs are labelled, listable, and retryable, and attach to a **project** so results stay tied to the right codebase.

The activation-only mode deserves the emphasis. It separates *the skill did not help* from *the skill never loaded* — two failures with identical symptoms and completely different fixes, the second being a [[tessl-review|description]] problem rather than a content one.

Evals are the expensive instrument: slower, more setup, and reached for *"before you publish it or share it into a repository where you will not see how others' agents use it."* That is the honest statement of when measurement is worth its cost.

## See Also
- [[tessl-scenario]] — generates the tasks this grades against.
- [[tessl-review]] — the cheap structural sibling; *well written* vs *works*.
- [[pattern-capability-evals]] — the technique this anchors.
- [[topic-ai-native-sdlc]] — recorded config-evals as unshipped by any framework; this is where they live instead.
