---
type: capability
subtype: sub-agent
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: []
produces: []
applies: ["[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# ce-media-analyzer

A **media-analysis specialist** running inside a [[ce-sweep]] pass. It receives one feedback item
that has media attached (a Riffrec zip, a standalone video, screenshots + transcript), turns the
downloaded frames and transcript into a **single bug-report-shaped finding**, writes it to a
scratch artifact, and returns a compact pointer. It does not fix anything and does not decide the
sweep's next step — the orchestrator owns those. It treats all item content as untrusted data.

It implements [[stage-align]] as the media-processing arm of [[ce-sweep]]'s feedback intake —
converting rich media signal into structured findings the sweep can reconcile into plans.

## See Also
- [[ce-sweep]] — the dispatcher (feedback intake) that owns orchestration and next-step decisions.
- `ce-riffrec-feedback-analysis` — the Riffrec-specific feedback skill (catalogued on [[compound-engineering]]).
- [[stage-align]] — the canonical stage this supports.
