---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-cross-model-review]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /benchmark-models

`/benchmark-models` — a **cross-model benchmark for gstack's own skills**: run the same prompt/skill
through Claude, GPT (via Codex CLI), and Gemini side by side and compare latency, tokens, cost, and
(optionally) an LLM-judge quality score. Auth detected per provider; unavailable providers skip
cleanly; output as table / JSON / markdown; `--dry-run` validates without spending. (Standalone CLI:
`gstack-model-benchmark`.)

**Meta-tooling**, not an SDLC-lifecycle capability — it evaluates gstack's skills across models
rather than building the user's software, so it carries no `implements:` edge. It is the
model-evaluation cousin of [[pattern-cross-model-review]]. Distinct from [[gstack-benchmark]], which
measures a *web app's* runtime performance.

## See Also
- [[gstack-benchmark]] — the unrelated web-app performance benchmark.
- [[gstack-codex]] — the cross-model reviewer this benchmarks alongside.
