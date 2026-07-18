---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-review-report]]"
applies: ["[[pattern-cross-model-review]]", "[[pattern-adversarial-review]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /codex

`/codex` — the **Second Opinion**. An independent review from the **OpenAI Codex CLI** — a
completely different AI looking at the same diff. Three modes: **review** (pass/fail gate),
**adversarial challenge** (actively tries to break your code), and **open consultation** (session
continuity). When both [[gstack-review]] (Claude) and `/codex` (OpenAI) have reviewed the same
branch, gstack surfaces a **cross-model analysis** of which findings overlap and which are unique
to each.

gstack's signature realization of [[pattern-cross-model-review]] — get an independent second opinion
from a different vendor's model — shared with Compound Engineering (whose [[ce-code-review]] runs an
adversarial + cross-model pass). The adversarial-challenge mode also applies
[[pattern-adversarial-review]]. Also the quality gate behind [[gstack-spec]].

## See Also
- [[gstack-review]] — the Claude-side review this is cross-analyzed against.
- [[gstack-spec]] — uses `/codex` as its spec quality gate.
- [[ce-code-review]] — Compound Engineering's cross-model review.
- [[pattern-cross-model-review]] — the technique.
- [[stage-review]] — the canonical stage this implements (Review side).
