---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-learn]]"
delegates_to: ["[[ce-session-historian]]", "[[ce-pattern-recognition-specialist]]", "[[ce-security-sentinel]]", "[[ce-performance-oracle]]", "[[ce-best-practices-researcher]]", "[[ce-framework-docs-researcher]]", "[[ce-data-integrity-guardian]]"]
produces: ["[[artifact-solution-doc]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-compound

`/ce-compound` — "Close the loop by capturing learnings into `docs/solutions/` so the next
iteration starts smarter." Step 6 of the loop and, per Every, **"the money step… the whole
point."** A council of research sub-agents (session-historian, pattern-recognition-specialist,
security-sentinel, performance-oracle, best-practices-researcher, framework-docs-researcher,
data-integrity-guardian) mines the just-completed work — its bugs, failed tests, and reusable
solutions — and writes structured, schema-validated learnings to **`docs/solutions/`**
([[artifact-solution-doc]]). Future [[ce-brainstorm]], [[ce-plan]], and [[ce-code-review]] runs
read these notes as grounding (via the `learnings-researcher` persona), so *"the next agent does
not have to learn the same lesson from scratch."*

**This is the capability that promoted [[stage-learn]] as a canonical stage.** It gives
learning-capture a second framework (alongside BMAD's [[bmad-retrospective]]), clearing the
≥2-framework bar to split learning out of [[stage-release]]. It is the reference realization of
[[pattern-knowledge-compounding]] — its output is *consumed by the front of the next loop*,
making the lifecycle circular. See [[stage-learn]] for the full rationale.

## Cross-framework equivalents
Learning-capture cluster: `ce-compound` ↔ [[bmad-retrospective]] — both harvest lessons at
iteration close so the next starts ahead. Deliberately *not* an `equivalent_to` edge: the
terminal acts differ (a maintained, machine-consumable [[artifact-solution-doc|solution corpus]]
vs a one-off human retrospective). OpenSpec's [[openspec-sync]] is a *spec-level* cousin (fold
the change into the living spec) — noted on [[stage-learn]].

## See Also
- [[bmad-retrospective]] — the team-process flavor of the same [[stage-learn]] activity.
- [[ce-compound-refresh]] — keeps the corpus this produces healthy over time.
- [[pattern-knowledge-compounding]] — the signature technique; [[artifact-solution-doc]] — the output.
- [[stage-learn]] — the canonical stage this implements (and promoted).
