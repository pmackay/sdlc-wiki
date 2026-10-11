---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-10-11
---

# Pattern: Throwaway prototype

Build a quick, disposable version — a terminal app or toggleable UI variation — to validate a design or de-risk an unknown, then **discard it**. The deliverable is the knowledge gained, not the code; keeping the prototype invites it to harden into production by accident.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-prototype]] — builds throwaway prototypes for design validation. **v1.2.0 shifts the pattern's last step from *discard* to *archive off-trunk*:** "throwaway is a constraint on how the code is written, not a promise to destroy it". The prototype (now a single shareable HTML file on the logic branch) is kept as a primary source on a `prototype/<name>` branch out of main, pointed at from the implementation issue.

gstack:

- [[gstack-design-shotgun]] — generate disposable AI mockup variants to explore design before committing to code.

pstack:

- [[pstack-principle-exhaust-the-design-space]] — build 2-3 competing prototypes and compare side by side before committing.
- [[pstack-poteto-mode]] — the Prototype playbook, and a sharper use: when about to ask the human *"which approach"*, classify the question first. **If the answer is a fact you could observe by running something, it is not the human's to answer** — sketch it and let the result decide. Prototyping as a substitute for a blocking question is new here.
- [[pstack-arena]] — the variant that does **not** discard: see [[pattern-candidate-grafting]].

builder-skills:

- [[builder-visual-plan]] — UI and product plans open with a wireframe canvas or a live prototype as the review surface, before any production code.

## See Also
- [[pattern-candidate-grafting]] — the variant that keeps the losers: [[pstack-arena]] picks a base and then harvests the non-winners for parts instead of discarding them.
- [[stage-implement]] — the stage where this applies.
- [[pattern-spec-driven-development]] — turn validated learnings into a spec.
