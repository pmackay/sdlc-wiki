---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-explainer]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /visual-recap

Turn a PR, branch, commit, or diff into an **interactive visual recap**: *"a visual plan built from a diff, not toward one."* Schema, API, file, and architecture changes become the same `data-model`, `api-endpoint`, `file-tree`, and `diagram` blocks a forward plan would use, so *"a reviewer scans the shape of the change before spending attention on the literal lines."*

Its rules: the output is always a published Agent-Native plan and never inline chat (*"an inline summary is not a degraded recap, it is the thing a recap replaces"*), with local-files mode as the one privacy exception. The default scope is the **whole work unit or thread**, not the latest fix, and it excludes unrelated edits that were already there. The body carries no boilerplate. The skill also says when **not** to use it: *"a tiny change reviews faster as plain diff."* The installer can add a GitHub Action that generates a recap on every PR.

[[stage-review]], as a reviewer's aid rather than a reviewer. It produces an [[artifact-explainer]] of the change for the human doing the review.

## See Also
- [[builder-visual-plan]] — the forward-planning twin.
- [[stage-review]] — the canonical stage this supports.
