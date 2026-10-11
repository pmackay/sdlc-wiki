---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /quick-recap

A **final status-line convention**. Every response that completes a unit of work ends with one line under 100 characters: 🟢 when the work is finished, 🟡 when *non-routine* follow-up remains (named), 🔴 only when blocked on the user. Nothing may follow the line. Example: *"🟡 Code updated, set PROVIDER_WEBHOOK_SECRET before testing webhooks"*.

The skill notes that it only works when installed: *"This convention is only automatic when it is present in project or user instructions."* The installer therefore prefers to write it as a **managed `AGENTS.md` / `CLAUDE.md` block** instead of relying on skill loading. That makes it one of the few capabilities in the wiki meant to live in always-on context rather than be invoked.

Off-stage. It is a small reporting convention that tells the reader at a glance whether an unattended run ended done, pending, or blocked, which is what [[builder-plow-ahead]]'s recap and the Factory's reports need to end with.

## See Also
- [[builder-plow-ahead]] — the autonomous-run recap this caps.
- [[builder-skills]] — the framework.
