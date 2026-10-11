---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-deep-modules]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-improve-codebase-architecture"
sources: "Matt Pocock — Skills for Real Engineers (2026); v1.2.0 (2026-08-05)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-10-11
---

# improve-codebase-architecture

`/improve-codebase-architecture` — a user-invoked engineering skill that scans a codebase for **deepening opportunities** and presents them as a visual HTML report, then grills through whichever one you pick. The review/maintenance answer to failure mode #4 (ball of mud): surface entropy so it can be paid down deliberately, steering modules back toward [[pattern-deep-modules]].

**YAGNI scoping.** The Explore step scans where change is actually landing, not the whole repo evenly. If you name a direction it takes it; otherwise it reads the last ~20 commit messages to bias exploration toward actively developed paths. "A deepening opportunity in code nobody touches is a refactor you'll never cash in."

**Routing.** It is the **codebase-health** lane in [[mp-ask-matt]]: picking an opportunity "generates an idea" to take into [[mp-grill-with-docs]], and [[mp-codebase-design]] is "the bench you design the chosen one on". Together with [[mp-to-spec]] it covers the job of the deleted `request-refactor-plan` skill.

Implements [[stage-review]] in the maintenance sense — auditing built code — rather than feature UAT.

## See Also
- [[mp-codebase-design]] — the forward-looking design discipline this audits against.
- [[gsd-verify-work]] — GSD's verification counterpart.
- [[stage-review]] — the canonical stage this implements.

## Version history
- **v1.3.0 / v1.3.1 (2026-10-04):** [[mp-diagnosing-bugs]]'s Phase 6 post-mortem hand-off to this skill was removed (it is user-invoked, so unattended flows can't call it). [[mp-ask-matt]] points here from a bug fix only where the finding is a missing seam.
- **v1.2.0 (2026-08-05):** gained the YAGNI scoping filter; became the codebase-health lane in [[mp-ask-matt]]; absorbed part of the deleted `request-refactor-plan` skill (alongside [[mp-to-spec]]). Sub-agent dispatch became harness-neutral in v1.2.3.
- **Initial ingest (2026-06-28):** a whole-repo scan for architectural improvements, presented as HTML reports.
