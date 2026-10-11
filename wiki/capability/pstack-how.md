---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-wave-parallelism]]", "[[pattern-context-engineering]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[openspec-explore]]", "[[bmad-document-project]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /how

Answers *how does X work?* at the level of a senior engineer onboarding onto a subsystem — enough to build a working mental model, not so much that it reads like annotated source code. Together with [[pstack-why]] it forms the framework's two-skill understanding layer, and the pair is explicitly divided: **how** is what the code does, **why** is what forces led to its shape.

The skill is **scale-adaptive** by an explicit first step. A simple question (one module, a small utility) skips exploration entirely and runs one explainer in a single pass. A complex one (a subsystem spanning files or services, a cross-cutting feature, a full architectural overview) decomposes the question into two to four **exploration angles**, spawns all explorers in a single message on a fast cheap model, then hands their findings to one explainer on the strongest judgment model for synthesis. *When in doubt, take the simple path.*

The split is [[pattern-context-engineering]] with a **model-role split** layered on it: exploration is a bulk-reading job routed to a fast model, synthesis is a judgment job routed to a reasoning model, and every subagent runs `readonly: true`. The raw reading stays in the explorers; only findings reach the parent. The final step is a discipline rather than a mechanism — present the explainer's output with light edits for clarity, and **do not substantially rewrite it**.

`/how` is one of the most heavily consumed capabilities in the framework. [[pstack-architect]] runs it to ground Phase A, [[pstack-teach]] runs it as one of its two inputs, [[pstack-blast-radius]] positions itself against it, and [[pstack-comment-sicko]] fires it to check a comment's claim before killing the comment.

## See Also
- [[pstack-why]] — the motivation companion; the two are designed as a pair.
- [[pstack-teach]] — runs this and `why` and weaves one plain explanation for a person.
- [[pstack-blast-radius]] — the third member of the understanding trio, aimed at consequences rather than mechanism.
- [[openspec-explore]] — the cross-framework counterpart that aligns by investigating the codebase.
- [[stage-align]] — the canonical stage this implements.
