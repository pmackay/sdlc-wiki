---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-learn]]"
delegates_to: ["[[pstack-how]]", "[[pstack-why]]", "[[pstack-unslop]]"]
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-source-grounding]]"]
equivalent_to: ["[[ce-explain]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /teach

Explains a change or subsystem so a person actually understands it, rather than summarizing it. It runs [[pstack-how]] and [[pstack-why]] in parallel and weaves their findings into one plain account — what the thing is, how it works, why it is that way — pitched at the person's pace. The goal is explicitly *that they understand it, not that you change anything*.

Two mechanisms make it more than a prettier explainer, and both are unusual enough to be worth recording.

**Build the picture up diagram by diagram.** For anything with three or more moving parts the skill forbids one diagram containing all of them. It requires a *short series* instead, where each diagram redraws the last and adds a single part, so the reader watches the system assemble. To teach a flow from A to B to C, draw it three times: A to B, then redraw and add C, then redraw and add the return edge. A single all-at-once diagram, especially one saved for the end, is ruled *reference, not teaching*. The medium is matched to the idea — mermaid where labels carry the meaning, a generated marker-on-whiteboard image where the idea is spatial (layout, overlap, scroll position, a before and after).

**Anti-pedagogy-theater rules.** No quizzes, no "pause and say it back", no announcing that a part is important or tricky, no printed framing labels ("the key insight", "at its core", "TL;DR"). Give the smallest complete answer first, a sentence or two, then stop and let them respond. Layers get added when asked.

Its cross-framework counterpart is [[ce-explain]] — both turn work into a human-facing explainer that feeds understanding forward rather than shipping anything, which is why both sit in [[stage-learn]]. The difference is the audience model: [[ce-explain]] produces a dense visual artifact, `/teach` produces a paced conversation.

## See Also
- [[pstack-how]] · [[pstack-why]] — the two skills it runs and blends; it must not redo their work.
- [[pstack-unslop]] — every response is written through it.
- [[ce-explain]] — the cross-framework counterpart.
- [[stage-learn]] — the canonical stage this implements.
