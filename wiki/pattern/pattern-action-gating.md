---
type: pattern
sources: "Builder.io — BuilderIO/skills, Factory (2026); pstack v0.15.2 — Lauren Tan (2026); github/gh-aw (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---

# Pattern: Action gating (authority decomposed per external action)

Split an agent's authority into **separately authorized kinds of external action** (fix, publish, reply, review, approve, merge, deploy, close, recover, notify). Give each its own policy, **never infer permission for one from another**, and recheck live state right before each write. Permission to fix a bug does not include replying to the reporter, and approving a PR does not include merging it. A merge does not include deploying.

The Factory in [[builder-skills]] states the rule most compactly: *"Fix, reply, close, review, approve, publish, merge, deploy, recover, and notify are independent decisions."* Its [[artifact-autonomy-policy]] gives each action a policy of `never`, `manual`, `criteria` (explicit `allow` and `stop` lists, where *all* allow conditions must pass and *no* stop condition may apply), or a named proof point (`after-fix`, `after-merge`). The default for anything unclear is to hold: *"Missing, unclear, or unavailable evidence means hold."*

**How it differs from its neighbours.** [[pattern-edit-guardrails]] limits what the agent may *write or touch* inside the workspace. [[pattern-deterministic-gates]] decides whether the *work* is good enough to accept. Action gating decides which of the agent's **effects on the outside world** it is allowed to cause, and it decides each one separately. The pattern exists because unattended agents fail at the boundary between steps. An agent allowed to fix and ship will, left alone, treat a green fix as permission to merge. Splitting authority at every external write is the fix, and in the Factory it goes as far as the notification layer (`DONT_NOTIFY` when nothing verifiable changed).

**Three details make it work in practice.**

- **Authorization is re-established, never assumed.** A PR number, label, green check, task title, or agent summary *"is not authorization"*. The original user request is re-read on every pass.
- **Evidence expires with the head.** Approval and merge evidence is tied to one exact head revision, and *"a changed head invalidates old check/review evidence and resets the soak."* A merge is conditioned on that head when the host supports it. When the host does not, the dependent action stays disabled.
- **Prompt text cannot widen it.** Project overlays add guidance but *"cannot grant permission, or weaken repository and host safeguards"*. On conflict, the more restrictive rule wins.

## Applied by (backlinks)

builder-skills (the signature instance):

- [[builder-factory]] sets the ten independent policies and their safe defaults. Replies, closure, approvals, merges, deploys, and recovery are off unless explicitly enabled.
- [[builder-factory-babysit-pr]] has a six-row gate table (Fix, Publish, Reply, Approve, Merge, Soak) for one authorized PR.
- [[builder-factory-review-prs]] keeps review findings separate from reply, approval, and merge.
- [[builder-factory-ship]] treats merge and deploy verification as separate proof points: *"a merge is not live proof."*
- [[builder-factory-collect]] and [[builder-factory-lookback]] only investigate when they find a problem or a recurring pattern. Replying, closing, and fixing each need their own authorization.
- [[builder-factory-human-digest]] is read-only by construction and routes every decision back to the module that owns it.
- [[builder-factory-watchdog]] and [[builder-factory-recover]] notify only on a verified next step and never repeat a completed write.

pstack (the earlier instance, stated as *autonomy decoupled from authority*):

- [[pstack-benny-reproduce-and-fix]] runs fully unattended and still stops at a **bounded draft PR**, with no merge authority at all.

## Enabled by (infrastructure)

- [[gh-aw]] — **safe outputs** are the structural form of this pattern. The agent job has no write permission. Each kind of write (create-issue, add-comment, create-pull-request, …) is a separate typed output applied by a separate job with a minimally scoped token, after a threat-detection verdict. The Factory writes its gates as prose policy the agent must follow. gh-aw compiles them into the CI job graph, where the agent cannot break them.

## See Also
- [[pattern-edit-guardrails]] — the neighbour that limits workspace writes rather than external actions.
- [[pattern-deterministic-gates]] — the gates that decide whether work is acceptable. Action gating decides what may be *done* with it.
- [[pattern-evidence-before-claims]] — the rule underneath every gate here. Unavailable is not empty, and a label is not proof.
- [[pattern-autonomous-loop]] — the pattern this makes safe to run unattended.
- [[topic-software-factory]] — *gate*, *safe outputs*, and *escalation* in the glossary.
