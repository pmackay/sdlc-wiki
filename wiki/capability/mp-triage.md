---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-grilling]]"]
equivalent_to: ["[[seeds-issue-workflow]]"]
docs_url: "https://www.aihero.dev/skills-triage"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-08-31
---

# triage

`/triage` — a user-invoked engineering skill that moves issues (and, per a repo toggle, external pull requests — "a PR is an issue with attached code") through a small **state machine of triage roles**: one **category** role (`bug` / `enhancement`) and one **state** role (`needs-triage` → `needs-info` / `ready-for-agent` / `ready-for-human` / `wontfix`). It categorises, verifies the claim, **grills if needed** ([[pattern-grilling]]), and writes **agent-ready briefs** for anything that reaches `ready-for-agent`, prefixing every posted comment with an AI-generated disclaimer. The canonical role names map to per-repo label strings configured by `/setup-matt-pocock-skills`.

Newly paged (was previously catalogued). It sits at the **front of the lifecycle** ([[stage-align]]) — turning raw incoming issues/PRs into fully-specified, agent-ready work — the intake counterpart to Compound Engineering's [[ce-sweep]] (which consolidates Slack/GitHub feedback into next-cycle inputs). Its `ready-for-agent` briefs feed [[mp-implement]] or [[mp-to-tickets]].

Its counterpart in [[seeds]] is [[seeds-issue-workflow]], which does the same conversion — unshaped request to agent-ready tracked item — but ends in a local JSONL store rather than a hosted tracker, and routes explicitly between a one-issue path and a full plan decomposition.

## See Also
- [[ce-sweep]] — Compound Engineering's feedback-intake relative (align-stage).
- [[mp-to-tickets]] · [[mp-implement]] — consume the agent-ready work triage produces.
- [[stage-align]] — the canonical stage this implements (issue/PR intake).
