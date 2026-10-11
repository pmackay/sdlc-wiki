---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-cross-model-review]]", "[[pattern-adversarial-review]]", "[[pattern-wave-parallelism]]"]
equivalent_to: ["[[gstack-codex]]", "[[mp-code-review]]", "[[addy-code-review]]", "[[sp-requesting-code-review]]", "[[ce-code-review]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /interrogate

Spawns one reviewer per configured model to adversarially review a change, then synthesizes a verdict. *"Adversarial review", "multi-model review", "challenge this", "stress test this code", "find blind spots", "tear this apart".*

**Its defining design decision is stated as a negative: the adversarial signal comes from model diversity, not assigned personas.** Every reviewer gets the *same* prompt and the *same* rubric; the four default reviewers differ only in which model runs them. That is a direct rejection of the approach [[gstack]], [[bmad]], and [[addy-agent-skills]] take, where a review panel is diversified by giving each seat a named role ([[pattern-parallel-persona-review]]). pstack argues the variance you want is between *models*, not between costumes, which makes this the wiki's purest [[pattern-cross-model-review]] instance — [[gstack-codex]] gets a second opinion from one other vendor, interrogate makes the whole panel cross-vendor by construction.

The flow is short. Determine scope (pointed-at files, or `git diff main...HEAD` on a feature branch). **State the intent explicitly** in one paragraph derived from the user's message, commit messages, the PR description, and the code itself, asking the user if unsure — reviewers judge against stated intent rather than guessing it. Spawn all reviewers in a single message, `readonly: true`, one per configured entry, each filling a shared reviewer-prompt template with the intent, the diff, and a shipped rubric. Then synthesize.

**The deliverable is a synthesized verdict, and the skill explicitly does not auto-apply changes.** It also ships a graceful-degradation rule that reveals how fast the model landscape moves under a framework like this: if a model slug is rejected as unresolvable, pick the closest equivalent from the error message (preferring the highest-reasoning tier of the same family), spawn with the valid slug, and open a *separate PR* to fix the configured value — **do not block the review on the slug issue**.

## See Also
- [[pstack-blast-radius]] — the single-question review; interrogate is the broad one.
- [[pstack-comment-sicko]] — the framework's single-axis persona reviewer, the one place it does use a costume.
- [[pstack-architect]] — runs interrogate on a synthesized sketch for pre-implementation pressure.
- [[gstack-codex]] · [[mp-code-review]] · [[addy-code-review]] · [[sp-requesting-code-review]] · [[ce-code-review]] — the review cluster.
- [[stage-review]] — the canonical stage this implements.
