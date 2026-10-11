---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-evidence-before-claims]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[mp-triage]]", "[[ce-sweep]]", "[[builder-factory-collect]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# triage-issue-reports

The first half of the **benny** automation pack. It classifies one Slack issue report and posts **one** useful verdict in its source thread, creating a tracker issue only for a clear, new bug. It explicitly does not reproduce or fix anything — that is [[pstack-benny-reproduce-and-fix]]'s job, and the split is what keeps the automation's blast radius small.

The mechanism is evidence review, **cause-aware routing**, tracker dedupe, and fail-closed ticket creation. Its frontmatter restricts it to one caller: *use only from the configured Benny triage automation.*

**Its defining property is fail-closed behavior.** It loads external configuration supplied by the automation, and *if the config is missing, malformed, or incomplete, it stops without posting or writing to the tracker*. An unattended agent with write access to a team's Slack and issue tracker is a genuinely risky surface, and benny's answer is that an incompletely configured automation does nothing at all rather than doing its best. The same rule appears on its sibling.

As a lifecycle capability it is an **intake** step: it takes unstructured human reports and turns them into a classified, deduplicated, routed tracker item that downstream work can start from. That puts it with [[mp-triage]] and [[ce-sweep]] in the intake flavor of [[stage-align]], with one difference worth noting — those are invoked by a developer, this one is triggered by an incoming report with no developer in the loop.

## See Also
- [[pstack-benny-reproduce-and-fix]] — the second half; it waits for this skill's trusted triage marker.
- [[pstack-benny-setup]] — configures and enables it.
- [[mp-triage]] · [[ce-sweep]] — the intake counterparts.
- [[stage-align]] — the canonical stage this implements.
