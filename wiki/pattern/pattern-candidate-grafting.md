---
type: pattern
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# Pattern: Candidate grafting (bakeoff, then harvest the losers)

Run N independent attempts at the **same** artifact, pick the strongest as a base, then **walk each losing candidate for the one or two ideas worth porting into the base** before verifying the result. The losers are a parts bin, not waste.

The graft step is what distinguishes this from the two neighbouring patterns it is easily confused with. [[pattern-throwaway-prototype]] builds competing sketches to *make a decision* and then discards them — [[gstack-design-shotgun]]'s mockup variants and [[mp-prototype]]'s throwaway sketches both end that way. [[pattern-cross-model-review]] runs several models over *one* artifact to find its flaws. Candidate grafting has several models each produce a *whole* artifact and then treats the non-winners as a source of material. The claim is that a losing design is rarely uniformly worse; it usually solved one sub-problem better, and that part is recoverable at near-zero cost once the work already exists.

Three supporting mechanisms travel with it in the evidence:

- **The rubric is derived before fan-out and withheld from the candidates.** They see only the task; the rubric is the picker's tool afterwards. That keeps candidates from optimizing for the score instead of the problem.
- **Each candidate returns a rationale naming what it considered and rejected**, which is what makes the graft pass cheap — the alternatives are already articulated.
- **A cross-judge on a different model family scores independently**, and a disagreement between judge and parent is read as evidence that *the rubric was ambiguous*, not merely that one reader was wrong.

Isolation is a precondition: each candidate writes to its own worktree or output path, per [[pattern-worktree-isolation]], or the attempts contaminate each other.

## Applied by (backlinks)

pstack:

- [[pstack-arena]] — the pattern's full six-phase realization (frame, fan out, cross-judge, pick, graft, verify).
- [[pstack-architect]] — Phase B runs an arena over design sketches and requires two structurally distinct candidates before synthesis.
- [[pstack-principle-exhaust-the-design-space]] — the principle that mandates competing candidates before committing.
- [[pstack-blast-radius]] — escalates to an arena for a big or wide change, merging what different models each caught.

builder-skills:

- [[builder-plan-arbiter]] — the *Hybrid* outcome and the *Borrowed From Other Plans* section of its decision memo keep the parts of losing plans worth keeping. The candidates are produced by independent agents rather than fanned out by the arbiter.

## See Also
- [[pattern-throwaway-prototype]] — the discard-the-losers sibling; [[gstack-design-shotgun]] is its clearest instance.
- [[pattern-cross-model-review]] — many models over one artifact, rather than one artifact each.
- [[pattern-wave-parallelism]] — the fan-out mechanics; grafting is what happens after the wave returns.
- [[pattern-worktree-isolation]] — the precondition that keeps candidates independent.
