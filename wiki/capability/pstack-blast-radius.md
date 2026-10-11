---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-review]]"
delegates_to: ["[[pstack-why]]", "[[pstack-arena]]", "[[pstack-unslop]]"]
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-evidence-before-claims]]", "[[pattern-tooling-leverage]]", "[[pattern-cross-model-review]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /blast-radius

Finds what a small-looking change could break somewhere else, before it ships. The third member of the understanding trio: [[pstack-how]] tells you what the code does, [[pstack-why]] tells you why it is shaped that way, blast radius tells you what it breaks elsewhere.

It opens by ruling out the obvious job. *Listing the callers is not the job. The agent can grep those in a second. The job is the breakage grep will not show you.* What it looks for instead is where symbol search stops: the JSON an API returns, a DB column, a wire format, another language reading the same bytes, a feature flag, code three hops downstream, the pinned version and any local patch of the library being called, and when things run (microtasks, unmount and teardown).

**Its central move is to invert the deliverable.** *A blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it is true.* So the skill refuses to hand back the writeup as the product. It instead requires finding **the one fact the change is safe because of** — most risky-looking changes are safe because of a single fact, and if it holds, most risky cases clear at once — and then proving that fact by running code.

The proof requirement is graded on a five-rung **evidence ladder**, and the skill requires you to say where it stopped:

1. You said so. Worthless on its own.
2. You pointed at the line. A real `file:line`, or the library's own source.
3. You showed the bad case cannot happen. You walked the failure step by step and it does not reach.
4. You ran it. A script or test that calls the real code and fails loud if you are wrong.
5. You reproduced it in the running app.

Anything that cannot reach rung 4 must be written up as **unproven**, not as settled. This is the most operational statement of [[pattern-evidence-before-claims]] in the wiki — the cluster's other members ([[sp-verification-before-completion]], [[pstack-principle-prove-it-works]]) assert that evidence is required, while this one grades it and forces the grade into the output. Rung 4 is also [[pattern-tooling-leverage]] in miniature: *usually one small script that imports the same library the app ships and calls the exact function you are worried about*, and that script ships in the writeup as the cheapest test that catches the real bug.

For a big or wide change it escalates to [[pstack-arena]], asking several models the same question and merging the answers, on the reasoning that different models catch different real bugs.

## See Also
- [[pstack-how]] · [[pstack-why]] — the two skills it positions itself against, and whose citation rules it inherits.
- [[pstack-principle-prove-it-works]] — the principle whose sharpest operational form this is.
- [[pstack-interrogate]] — the broad multi-model review; blast radius is the single-question one.
- [[pattern-evidence-before-claims]] — the technique, graded here into five rungs.
- [[stage-review]] — the canonical stage this implements.
