---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-review-report]]"
applies: ["[[pattern-adversarial-review]]"]
equivalent_to: ["[[addy-code-review]]", "[[bmad-code-review]]", "[[ce-code-review]]", "[[mp-code-review]]", "[[sp-requesting-code-review]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-09
---

# /review

`/review` — the **Staff Engineer**. Pre-landing PR review that "finds the bugs that pass CI but blow up in production." **Auto-fixes the obvious ones** and flags completeness gaps and unnecessary complexity / drive-by edits. Produces a review report ([[artifact-review-report]]).

This is gstack's member of the cross-framework **code-review** cluster — alongside [[addy-code-review]], [[bmad-code-review]], and [[ce-code-review]]. In gstack's sprint, `/review` anchors a distinct **Review** phase (quality gate), separate from the **Test** phase ([[gstack-qa]]) — the clean Review∥Test partition that (with Addy) promoted [[stage-review]] as its own stage (2026-07-05). When paired with [[gstack-codex]], the two produce a cross-model analysis of overlapping vs unique findings ([[pattern-cross-model-review]]).

## See Also
- [[gstack-codex]] — the cross-model second-opinion reviewer; cross-analyzed against this one.
- [[gstack-qa]] — the functional **Test**-phase sibling.
- [[addy-code-review]] · [[bmad-code-review]] · [[ce-code-review]] — code-review-cluster counterparts.
- [[stage-review]] — the canonical stage this implements (Review side).
