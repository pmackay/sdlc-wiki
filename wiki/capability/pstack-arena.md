---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: ["[[pstack-poteto-agent]]"]
produces: []
applies: ["[[pattern-candidate-grafting]]", "[[pattern-cross-model-review]]", "[[pattern-throwaway-prototype]]", "[[pattern-worktree-isolation]]", "[[pattern-wave-parallelism]]"]
equivalent_to: ["[[gstack-design-shotgun]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /arena

Spawns N parallel attempts at the **same** task, picks the strongest as a base, and grafts the best parts of the losers into it. The framework's design-and-code bakeoff primitive, and the engine [[pstack-architect]] Phase B runs on. Its division of labour against [[pstack-swarm]] is explicit in [[pstack-poteto-mode]]: swarm is for coverage matrices, races, gauntlets, and exploration partitions; arena is for **bakeoffs with base selection and grafting**.

Six phases.

- **A. Frame.** The N candidates receive the same prompt, so *the prompt is the contract*. State the artifact, then derive a rubric of three to six concrete gradeable criteria — held back from the candidates, who see only the task, because the rubric is the picker's tool in Phase D. Runners default to one candidate each on four different models; the same model N times is correct when the work is generation-bound rather than judgment-sensitive. Each candidate gets its own output location, a git worktree where possible, per [[pstack-principle-separate-before-serializing-shared-state]].
- **B. Fan out.** All N spawned in one message with `run_in_background: true`. Each returns the artifact **and a short rationale naming the alternatives it considered and what it rejected**. A dropout proceeds with N-1 and is noted in the synthesis record.
- **C. Cross-judge.** One readonly judge on a model from a configured pool, preferring a **different model family from the parent's**. It sees the rubric and the candidates by path label, scores each criterion, and recommends a base. It runs in parallel with the parent's own reading in Phase D, never while candidates are still writing.
- **D. Pick a base.** Read every candidate end to end first. Score criterion by criterion, not on holistic feel, then compare against the cross-judge. *Agreement confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous.* The tie-break is maintainability — which candidate a future maintainer can extend most easily without breaking invariants — with the cleaner boundary or smaller API preferred per [[pstack-principle-laziness-protocol]].
- **E. Graft.** Walk each losing candidate once more for what is worth porting into the base. *The signal is usually one or two things per candidate, not most of it.*
- **F. Verify** the synthesized result.

Phase E is the contribution. [[pattern-throwaway-prototype]] as practiced elsewhere (including [[gstack-design-shotgun]]'s mockup variants) discards the losers; arena treats them as a **parts bin**, which is what [[pattern-candidate-grafting]] names. The parent-versus-judge disagreement rule in Phase D is also unusual: a split verdict is read as evidence that *the rubric* was ambiguous, not merely that one reader was wrong.

## See Also
- [[pstack-swarm]] — the sibling fan-out primitive, partitioned by coverage rather than competition.
- [[pstack-architect]] — the main consumer; Phase B is an arena.
- [[pstack-blast-radius]] — escalates to an arena for a big or wide change.
- [[gstack-design-shotgun]] — the visual-variant counterpart, which discards rather than grafts.
- [[pattern-candidate-grafting]] — the technique this capability defines.
