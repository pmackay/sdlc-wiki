---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-plan]]"
delegates_to: ["[[pstack-how]]", "[[pstack-why]]", "[[pstack-arena]]", "[[pstack-interrogate]]"]
produces: ["[[artifact-architecture]]", "[[artifact-adr]]"]
applies: ["[[pattern-deep-modules]]", "[[pattern-contract-first]]", "[[pattern-candidate-grafting]]", "[[pattern-cross-model-review]]", "[[pattern-throwaway-prototype]]"]
equivalent_to: ["[[mp-codebase-design]]", "[[gstack-plan-eng-review]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /architect

Settles the shape before writing code. It sketches types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode, synthesizes across multiple model perspectives, then fills in code against the chosen sketch. [[pstack-poteto-mode]] fires it on any code crossing a function boundary.

Five phases, opened as a todo list before anything starts.

- **A. Ground.** Build a real mental model of every system the new code touches by running [[pstack-how]] over the relevant subsystems. *Naming a file is not grounding* — produce the traced model `how` prescribes. If the design redefines ownership or layering, also run [[pstack-why]] on the existing shape so the rationale becomes a constraint rather than a guess. Skipped only for genuinely greenfield work.
- **B. Sketch.** Run [[pstack-arena]] with the design-sketch task, one candidate per configured architect runner across four different models. **Design it twice** — at least two *structurally distinct* candidates are required before synthesis, even when the first looks sufficient, and they must be whole-shape alternatives rather than point fixes inside one shape. Every candidate is screened against a shipped `design-red-flags.md` and rejected or revised for **shallow modules, information leakage, temporal decomposition, and pass-through methods**. Surviving candidates are compared on **interface depth**: prefer the design that hides more complexity behind a smaller, simpler public surface.
- **C. Agree.** Opt-in only. The default is to proceed straight to implementation with no human checkpoint, per [[pstack-principle-never-block-on-the-human]]. The synthesized sketch may ship as its own commit either way — the scaffold-first mode of [[pstack-principle-foundational-thinking]]. For adversarial pressure before implementing, run [[pstack-interrogate]] on the sketch.
- **D. Implement against the sketch.** The synthesized sketch is the contract. **Deviations are signal worth surfacing, not friction to absorb silently** — a function needing a parameter the sketch did not anticipate raises the question of whether the sketch was wrong, the requirement was missed, or the implementation is overreaching.
- **E. Scrap.** When implementation keeps producing friction the sketch cannot absorb, throw the sketch out rather than bolting fixes onto a wrong design. The signal is a *pattern*, not single instances, and the tells are listed: the same shape of workaround recurring across unrelated code, multiple unrelated edge cases each needing a special-case branch, types needing escape hatches (`any`, casts, optional fields always set in practice) to compile, the "we need a lock" reflex when the sketch said the state was not shared, callers having to know the abstraction's internal rules, and two or more independent Phase D deviations of the same shape.

Phases B and E are what separate it from the wiki's other design capabilities. The red-flag screen is a direct import of Ousterhout's design vocabulary, making this the sharpest [[pattern-deep-modules]] instance here alongside [[mp-codebase-design]]; and the scrap phase pages *abandoning* a design as a named step with falsifiable triggers, which no other framework does.

## See Also
- [[pstack-arena]] — the fan-out engine Phase B runs on.
- [[pstack-how]] · [[pstack-why]] — the Phase A grounding.
- [[pstack-interrogate]] — optional adversarial pressure on the synthesized sketch.
- [[mp-codebase-design]] — the deep-modules counterpart; [[gstack-plan-eng-review]] — the eng-manager architecture lock.
- [[stage-plan]] — the canonical stage this implements.
