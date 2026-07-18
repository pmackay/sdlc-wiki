---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: ["[[addy-code-reviewer]]"]
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-anti-rationalization]]"]
equivalent_to: ["[[bmad-code-review]]", "[[ce-code-review]]", "[[mp-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-09
---

# Code Review & Quality

Reviews every change before merge across five axes — correctness, readability, architecture, security, and performance — approving when a change definitely improves overall code health rather than demanding perfection. Its distinctive machinery is severity-labelled findings (Critical / no-prefix Required / Nit / Optional / FYI) so authors can tell what is mandatory from what is discretionary, paired with change-sizing norms (~100 lines is reviewable, ~1000 must be split), splitting strategies (stack, file-group, horizontal, vertical), and review-speed expectations (respond within one business day).

It emits an [[artifact-review-report]] and can delegate the actual reviewing to the [[addy-code-reviewer]] persona. The skill applies [[pattern-anti-rationalization]] — its rationalization tables and structural-remedy prompts exist to stop reviewers rubber-stamping or softening real issues.

## See Also
- [[addy-code-reviewer]] — the persona this delegates the review to.
- [[bmad-code-review]] — BMAD's counterpart; adversarial parallel review layers over one diff (both emit an [[artifact-review-report]]).
- [[artifact-review-report]] — the labelled findings it produces.
- [[stage-review]] — the canonical stage this implements.
