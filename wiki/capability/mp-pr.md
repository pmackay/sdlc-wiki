---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[ce-commit-push-pr]]", "[[gsd-ship]]"]
docs_url: "https://www.aihero.dev/skills-pr"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04); Summary visuals adapted from Dex Horthy (HumanLayer) show-me"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# pr

`pr` — a **model-invoked** engineering skill whose whole description is "Use when writing a PR body." It is the **shape a pull request body should take** → [[artifact-pull-request]]. Being model-invoked, the agent reaches for it whenever it writes a PR, with no slash command needed.

**New in v1.3.0 (2026-10-04), graduated from `in-progress/`.** It is Matt Pocock's first capability on [[stage-release]], but only the *write-up* part of it: it does not commit, push, open, or merge anything. Those stay with the agent or with [[mp-implement-spec]], which opens a draft PR when the tracker works that way.

## The template

Three sections. No preamble, brief prose, and the user's domain language from `GLOSSARY.md`:

- **Summary**: "the smallest view that makes the key point clear". Pick one or more of pseudocode (logic), a call tree (runtime control flow), a component tree (UI structure), a shallow file tree (a refactor), Mermaid (interaction / data flow), or a `diff` shaped to the topic (component, file layout, call stack, state). Show the whole block only when most of it is new. "You may use one of these, you may use several, it is unlikely you will use all of them." The visual menu is adapted from Dex Horthy's `show-me` skill (HumanLayer), credited in the skill's `CREDITS.md`.
- **Evidence**: a before and after. "Screenshots are S-tier" when the change is visual; execution-based evidence (the exact test that now fails then passes, console output) is A-tier ([[pattern-evidence-before-claims]]).
- **Merge Danger**: a **door** call, one-way (destructive, hard to reverse) or two-way (cheap to roll back), plus a one-word **blast radius** and its possible ramifications.

## Why it matters

Most release-cluster capabilities (e.g. [[ce-commit-push-pr]], [[gsd-ship]], [[gstack-ship]]) treat the PR description as a by-product of shipping. `pr` treats it as a **review artifact** for a human reader: one visual, evidence the change works, and how risky the merge is. The merge-danger call reuses the one-way/two-way-door framing to make the reviewer's risk decision explicit.

## See Also
- [[mp-code-review]] — runs before the PR goes up; `pr` describes what passed it.
- [[mp-implement-spec]] — the one MP skill that opens a (draft) PR itself.
- [[ce-commit-push-pr]] · [[gsd-ship]] — release-cluster counterparts that also open the PR.
- [[artifact-pull-request]] — what it shapes.
- [[stage-release]] — the canonical stage this (partially) implements.
